import { readFileSync } from "node:fs";
import { expect, it } from "vitest";

it("the proposed course covers the audit budgets and all grammar owners with later retrievals", () => {
  const plan = JSON.parse(
    readFileSync("prompts/research/course-plan.json", "utf8"),
  ) as {
    units: {
      id: string;
      gfLevel: number;
      wordBudget: number;
      prerequisite: string;
      grammar: { code: string; role: string }[];
    }[];
    grammarOwnershipAndRecycling: {
      code: string;
      canonicalOwner: string;
      laterRetrievals: string[];
    }[];
  };
  const audit = JSON.parse(
    // The approved allocation is against C1, not the shrinking live remainder.
    readFileSync("prompts/research/c1-coverage-baseline.json", "utf8"),
  ) as {
    levels: {
      level: number;
      words: { remaining: number };
      grammar: { items: { code: string }[] };
    }[];
  };
  expect(plan.units).toHaveLength(96);
  expect(new Set(plan.units.map((u) => u.id)).size).toBe(96);
  for (const [i, u] of plan.units.entries()) {
    expect(u.prerequisite).toBe(i ? plan.units[i - 1].id : "s1-u12");
    expect(u.wordBudget).toBeGreaterThanOrEqual(15);
    expect(u.wordBudget).toBeLessThanOrEqual(25);
    expect(u.grammar.length).toBeGreaterThanOrEqual(2);
    expect(u.grammar.length).toBeLessThanOrEqual(3);
  }
  for (const l of audit.levels)
    expect(
      plan.units
        .filter((u) => u.gfLevel === l.level)
        .reduce((n, u) => n + u.wordBudget, 0),
    ).toBe(l.words.remaining);
  const allCodes = audit.levels.flatMap((l) =>
    l.grammar.items.map((g) => g.code),
  );
  expect(plan.grammarOwnershipAndRecycling.map((g) => g.code).sort()).toEqual(
    allCodes.sort(),
  );
  for (const g of plan.grammarOwnershipAndRecycling) {
    expect(new Set(g.laterRetrievals).size).toBe(2);
    const owner = plan.units.findIndex((u) => u.id === g.canonicalOwner);
    if (owner === -1)
      expect(g.canonicalOwner.startsWith("existing:")).toBe(true);
    else
      expect(
        plan.units
          .filter((u) =>
            u.grammar.some(
              (p) => p.code === g.code && p.role === "first-complete-treatment",
            ),
          )
          .map((u) => u.id),
      ).toEqual([g.canonicalOwner]);
    for (const id of g.laterRetrievals)
      expect(plan.units.findIndex((u) => u.id === id)).toBeGreaterThan(owner);
  }
});
