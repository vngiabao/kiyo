# Optional Kiyo cloud sync

This change is built and tested locally with a fake transport. No live project is connected. The SQL migration and the SQL isolation script have not yet been executed against Supabase/Postgres. Run the checks below on a local Supabase instance before approving a live connection.

## Local setup

1. Start a local Supabase development stack using its CLI and Docker. Do not link a hosted project or run a remote database push. This repository does not automatically install or start either service.
2. Apply `migrations/202610040001_learning_sync.sql` to the local database as its administrator. It creates two tables and three RPC functions. It is a first migration, not a repeatable seed script.
3. Run `tests/rls.sql` with `psql --set ON_ERROR_STOP=1` against that same local database. All fixture users, rows, temporary grants and test deletions are inside a rolled-back transaction. Any raised exception fails the check.
4. Copy the repository `.env.example` to `.env.local`. Set only the LOCAL API URL and public anonymous/publishable key. Never use a service-role or secret key in a `VITE_` variable; those values are bundled into the browser.
5. Configure local Auth redirects to `http://127.0.0.1:5173`. Email code sign-in can use the local mail catcher; Google/Apple require separate provider configuration. Restart the development server after setting environment variables.
6. Test with two local Auth users and two isolated browser profiles. Stop here until the owner supplies and authorizes live project credentials.

## Written security check

- Both new tables (`kiyo_sync_state`, `kiyo_learning_records`) ENABLE and FORCE RLS. Each policy has both USING and WITH CHECK restricted to `user_id = (select auth.uid())`.
- Anonymous users have no table or RPC privileges. Authenticated users can directly SELECT only their own rows; all production writes go through RPCs.
- All three RPCs have an empty search path, reject missing identity, derive identity from Auth, and expose no user-id argument. Every read, write and delete filters by that identity. The definer functions therefore require their explicit identity checks as well as table RLS.
- Push locks the owner's state row, checks revision and deletion epoch (including null inputs), limits each batch to 200 records, and refuses changes to immutable attempts/sessions. Pull pages at 500 records and rejects revision changes across pages in the client. An unchanged revision avoids downloading the whole history again.
- Server records and sync state carry `schema_version = 1`. Future migrations must deliberately update constraints and client decoders together. An unsupported version pauses with an error without replacing local learning data.
- Learning payloads use explicit field allowlists. Recordings, imported video, lesson positions, auth identity and device voice preferences are excluded. The public key is not an authorization boundary; RLS and the guarded RPCs are.

The SQL script checks own-row reads, cross-user read/update/insert/delete restrictions, RPC read/deletion isolation, null-revision rejection and anonymous denial. The unit suite checks these rules statically as well; a static check alone does not prove deployed RLS works. Before enabling a live project, also inspect `pg_tables.rowsecurity`, `pg_policies`, grants and function privileges in that actual project and rerun equivalent two-user checks there with owner approval.

Official references: [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) and [database functions](https://supabase.com/docs/guides/database/functions).

## Merge, offline and deletion behavior

The database name stays `tingjian-v1`; version 2 adds only a local sync-state store. Existing learning stores and backup format remain intact. Local records themselves are the durable pending work: a hash of the last acknowledged snapshot survives reload, and startup/reconnection scans find unsent edits. Failed requests retry without replacing local records. An in-flight edit stays pending for the next sync.

Attempts and completed sessions merge by immutable ID. Conflicting values for one ID stop sync instead of silently choosing. Schedules and mistake counts rebuild from all merged attempts sorted by timestamp, then a locale-independent ID comparison. The shared FSRS scheduler has fuzz off. Supported/unscored responses keep their evidence restrictions. Profile preferences use last-write-wins timestamps with stable tie-breakers; device clocks therefore affect profile conflict resolution. Recordings and unfinished lesson positions never sync.

First sign-in with guest data asks “Add this device’s progress to your account?” Declining persists for that account, including reloads. Sign-out keeps local data and its owner binding. Signing in as a different account cannot upload the previous learner's data; export and explicitly remove local data first. Settings keeps Export learning record, Last sync, Sync now and Delete my cloud data. Cloud deletion keeps local data and Auth login, deletes all cloud learning rows, and retains a minimal user-id/revision/epoch deletion marker. Devices seeing a changed epoch pause until the learner explicitly enables upload again.

## Manual acceptance on the local stack

1. Study as a guest, sign in, decline: verify no learning rows upload. Reload; verify sync stays paused. Enable in Settings and verify one copy of each attempt.
2. On another browser profile, sign into the same account and confirm history, profile and schedule match. Study offline in both, including matching timestamps, then reconnect in either order. Confirm identical memory cards and mistake counts.
3. Interrupt an upload after the server commit and retry. Confirm no duplicate evidence. Sign out during a slow request: local data remains, and no old download is applied to a new account.
4. Export a backup, delete cloud data, reconnect the second device: it must pause rather than restore deleted history. Explicitly enable sync to restore. Confirm the other test user's rows remain intact.
5. Check Settings and the consent page at 320px, keyboard-only, and reduced motion. Run the normal type, unit, content, browser and build checks.
