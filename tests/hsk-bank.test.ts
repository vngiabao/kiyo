import { expect, it } from "vitest";
import { selectBankItems } from "../src/hsk-bank";

const pool = ["a", "b", "c", "d"].map((id) => ({ id, level: 2, unit: "daily" }));
it("selects unseen first, then the least seen and oldest exposures", () => {
  const history = [
    { id: "r1", itemIds: ["a", "b", "c"], startedAt: 10 },
    { id: "r2", itemIds: ["a"], startedAt: 20 },
    { id: "r3", itemIds: ["b"], startedAt: 30 },
  ];
  expect(selectBankItems(pool, history, 2, "daily", 4, "seed")).toEqual(["d", "c", "a", "b"]);
});
it("uses actual exposures when available and preserves input order and history", () => {
  const history = [{ id: "r1", itemIds: ["a", "b", "c"], seenItemIds: ["a", "a"], startedAt: 10 }];
  const before = structuredClone({ pool, history });
  const selected = selectBankItems(pool, history, 2, "daily", 3, "stable");
  expect(selected.sort()).toEqual(["b", "c", "d"]);
  expect({ pool, history }).toEqual(before);
  expect(selectBankItems(pool, history, 2, "daily", 3, "stable").sort()).toEqual(selected);
});
it("does not leak another level or silently underfill a sample", () => {
  expect(() => selectBankItems(pool, [], 1, "daily", 1, "s")).toThrow("Insufficient");
  expect(() => selectBankItems([...pool, pool[0]], [], 2, "daily", 2, "s")).toThrow("Duplicate");
  expect(() => selectBankItems(pool, [], 2, "daily", 0, "s")).toThrow("Invalid");
});
