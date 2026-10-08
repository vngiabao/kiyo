import type { SupabaseClient } from "@supabase/supabase-js";

/** Probe existing owner-scoped reads without calling the state-creating pull RPC. */
export async function verifyCloudConnection(
  client: Pick<SupabaseClient, "rpc" | "from">,
  userId: string,
) {
  const signal = AbortSignal.timeout(20000);
  const owner = await client.rpc("learning_owner_allowed").abortSignal(signal);
  if (owner.error || owner.data !== true)
    throw new Error(
      "This cloud account could not be verified. Sign in with the configured Google account.",
    );
  const state = await client
    .from("kiyo_sync_state")
    .select("schema_version,revision")
    .eq("user_id", userId)
    .abortSignal(signal)
    .maybeSingle();
  const records = await client
    .from("kiyo_learning_records")
    .select("id", { head: true, count: "exact" })
    .eq("user_id", userId)
    .abortSignal(signal);
  if (
    state.error ||
    records.error ||
    (state.data && state.data.schema_version !== 1)
  )
    throw new Error(
      "Cloud storage could not be checked. Your progress stays on this device.",
    );
  return "Google account and cloud storage are reachable. No progress was uploaded or merged; your sync setting is unchanged.";
}
