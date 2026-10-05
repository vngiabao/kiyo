-- Apply only to a local Supabase instance until the owner approves live setup.
create table public.kiyo_sync_state (
  user_id uuid primary key references auth.users(id) on delete cascade,
  schema_version integer not null default 1 check (schema_version = 1),
  revision bigint not null default 0,
  epoch uuid not null default gen_random_uuid(),
  deleted boolean not null default false
);
create table public.kiyo_learning_records (
  user_id uuid not null references auth.users(id) on delete cascade,
  kind text not null check (kind in ('attempts','sessions','memories','mistakes','profiles')),
  id text not null check (length(id) between 1 and 256),
  schema_version integer not null check (schema_version = 1),
  payload jsonb not null check (jsonb_typeof(payload) = 'object' and payload->>'id' = id),
  primary key (user_id, kind, id),
  constraint learning_payload_keys check (
    payload - case kind
      when 'attempts' then array['id','phraseId','modality','correct','answer','expected','at','latencyMs','support','context']
      when 'sessions' then array['id','lessonId','completedAt','attempts','seconds','kind']
      when 'memories' then array['id','phraseId','modality','card','due','successes','failures','lastEvidence']
      when 'mistakes' then array['id','phraseId','modality','answer','expected','at','count','context']
      when 'profiles' then array['id','name','minutes','goals','locale','onboarded','pinyin','quiet','examMode','path','toneColors','mascotEnabled','mascotMotion','showStreak','updatedAt','updatedBy']
    end = '{}'::jsonb
  )
);
alter table public.kiyo_sync_state enable row level security;
alter table public.kiyo_sync_state force row level security;
alter table public.kiyo_learning_records enable row level security;
alter table public.kiyo_learning_records force row level security;
create policy own_sync_state on public.kiyo_sync_state for all to authenticated
  using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));
create policy own_learning_records on public.kiyo_learning_records for all to authenticated
  using (user_id = (select auth.uid())) with check (user_id = (select auth.uid()));
-- No anonymous access, and no direct client writes bypassing the revision lock.
revoke all on public.kiyo_sync_state, public.kiyo_learning_records from anon, authenticated;
grant select on public.kiyo_sync_state, public.kiyo_learning_records to authenticated;

create function public.kiyo_sync_pull(p_after text default '', p_known_revision bigint default null) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare
  learner uuid := auth.uid();
  s public.kiyo_sync_state;
  records jsonb;
  cursor_next text;
begin
  if learner is null then raise exception 'authentication_required'; end if;
  insert into public.kiyo_sync_state(user_id) values(learner) on conflict do nothing;
  select * into s from public.kiyo_sync_state where user_id = learner for update;
  if s.revision = p_known_revision and not s.deleted then
    return jsonb_build_object('schema_version',s.schema_version,'revision',s.revision,
      'epoch',s.epoch,'deleted',s.deleted,'rows','[]'::jsonb,'unchanged',true,'next',null);
  end if;
  select coalesce(jsonb_agg(jsonb_build_object('kind', r.kind, 'id', r.id,
    'schema_version', r.schema_version, 'payload', r.payload) order by r.cursor_key collate "C"), '[]'::jsonb),
    case when count(*) = 500 then max(r.cursor_key collate "C") else null end
    into records, cursor_next
  from (select *, kind || ':' || id as cursor_key from public.kiyo_learning_records
    where user_id = learner and (kind || ':' || id) collate "C" > p_after collate "C"
    order by (kind || ':' || id) collate "C" limit 500) r;
  return jsonb_build_object('schema_version',s.schema_version,'revision',s.revision,
    'epoch',s.epoch,'deleted',s.deleted,'rows',records,'next',cursor_next);
end $$;

create function public.kiyo_sync_push(p_revision bigint, p_epoch uuid, p_rows jsonb, p_resume boolean default false) returns jsonb
language plpgsql security definer set search_path = '' as $$
declare learner uuid := auth.uid(); s public.kiyo_sync_state; r jsonb; old_payload jsonb;
begin
  if learner is null then raise exception 'authentication_required'; end if;
  if p_rows is null or jsonb_typeof(p_rows) <> 'array' or jsonb_array_length(p_rows) > 200 then raise exception 'invalid_batch'; end if;
  select * into s from public.kiyo_sync_state where user_id = learner for update;
  if not found or s.revision is distinct from p_revision or s.epoch is distinct from p_epoch then raise exception 'sync_conflict'; end if;
  if s.deleted and p_resume is not true then raise exception 'cloud_deleted_sync_paused'; end if;
  for r in select value from jsonb_array_elements(p_rows) loop
    if (r->>'schema_version')::integer <> 1 then raise exception 'unsupported_schema'; end if;
    if r->>'kind' in ('attempts','sessions') then
      select payload into old_payload from public.kiyo_learning_records
        where user_id = learner and kind = r->>'kind' and id = r->>'id';
      if found and old_payload <> r->'payload' then raise exception 'immutable_record_conflict'; end if;
    end if;
    insert into public.kiyo_learning_records(user_id,kind,id,schema_version,payload)
      values(learner,r->>'kind',r->>'id',(r->>'schema_version')::integer,r->'payload')
      on conflict(user_id,kind,id) do update set payload = excluded.payload, schema_version = excluded.schema_version;
  end loop;
  update public.kiyo_sync_state set revision = revision + 1, deleted = false where user_id = learner returning * into s;
  return jsonb_build_object('schema_version',s.schema_version,'revision',s.revision,'epoch',s.epoch,'deleted',s.deleted);
end $$;

create function public.kiyo_sync_delete() returns jsonb
language plpgsql security definer set search_path = '' as $$
declare learner uuid := auth.uid(); s public.kiyo_sync_state;
begin
  if learner is null then raise exception 'authentication_required'; end if;
  insert into public.kiyo_sync_state(user_id) values(learner) on conflict do nothing;
  select * into s from public.kiyo_sync_state where user_id = learner for update;
  delete from public.kiyo_learning_records where user_id = learner;
  -- Minimal deletion marker prevents old devices silently restoring deleted data.
  update public.kiyo_sync_state set revision = revision + 1, epoch = gen_random_uuid(), deleted = true
    where user_id = learner returning * into s;
  return jsonb_build_object('schema_version',s.schema_version,'revision',s.revision,'epoch',s.epoch,'deleted',s.deleted);
end $$;
revoke all on function public.kiyo_sync_pull(text,bigint), public.kiyo_sync_push(bigint,uuid,jsonb,boolean), public.kiyo_sync_delete() from public, anon;
grant execute on function public.kiyo_sync_pull(text,bigint), public.kiyo_sync_push(bigint,uuid,jsonb,boolean), public.kiyo_sync_delete() to authenticated;
