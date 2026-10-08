import { expect, it } from "vitest";
import type { SupabaseClient } from "@supabase/supabase-js";
import { verifyCloudConnection } from "../src/cloud-connection";

function probe(owner = true, fail = false) {
  const reads: unknown[][] = [];
  const client = {
    rpc(name: string) {
      reads.push(["rpc", name]);
      return { abortSignal: async () => ({ data: owner, error: null }) };
    },
    from(table: string) {
      reads.push(["table", table]);
      const query = {
        select(fields: string, options?: unknown) {
          reads.push(["select", fields, options]);
          return query;
        },
        eq(field: string, value: string) {
          reads.push(["eq", field, value]);
          return query;
        },
        maybeSingle: async () => ({
          data: null,
          error: fail ? { message: "unavailable" } : null,
        }),
        abortSignal: () => ({
          maybeSingle: query.maybeSingle,
          then: (resolve: (result: unknown) => unknown) =>
            resolve({
              data: null,
              error: fail ? { message: "unavailable" } : null,
            }),
        }),
      };
      return query;
    },
  } as unknown as Pick<SupabaseClient, "rpc" | "from">;
  return { client, reads };
}
it("checks owner-scoped storage with reads only, even before a cloud state exists", async () => {
  const { client, reads } = probe();
  expect(await verifyCloudConnection(client, "owner-id")).toContain(
    "No progress was uploaded or merged",
  );
  expect(reads.filter((r) => r[0] === "rpc")).toEqual([
    ["rpc", "learning_owner_allowed"],
  ]);
  expect(reads.filter((r) => r[0] === "eq")).toEqual([
    ["eq", "user_id", "owner-id"],
    ["eq", "user_id", "owner-id"],
  ]);
});
it("does not read progress tables when owner authorization fails", async () => {
  const { client, reads } = probe(false);
  await expect(verifyCloudConnection(client, "wrong-id")).rejects.toThrow(
    "could not be verified",
  );
  expect(reads).toEqual([["rpc", "learning_owner_allowed"]]);
});
it("does not report a successful connection when table access fails", async () => {
  const { client } = probe(true, true);
  await expect(verifyCloudConnection(client, "owner-id")).rejects.toThrow(
    "could not be checked",
  );
});
