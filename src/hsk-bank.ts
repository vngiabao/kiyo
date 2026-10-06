export interface BankQuestion {
  id: string;
  unit: string;
  level: number;
}
export interface BankHistory {
  id: string;
  itemIds: string[];
  startedAt: number;
  seenItemIds?: string[];
}

/** Count real exposure for new runs; older runs retain their recorded selection. */
export function selectBankItems(
  pool: BankQuestion[],
  history: BankHistory[],
  level: number,
  unit: string,
  count: number,
  seed: string,
): string[] {
  if (!Number.isInteger(count) || count < 1) throw new Error("Invalid bank sample size");
  const seen = new Map<string, { count: number; last: number }>();
  const runs = [...history].sort((a, b) => a.startedAt - b.startedAt || a.id.localeCompare(b.id));
  for (const run of runs)
    for (const id of new Set(run.seenItemIds ?? run.itemIds)) {
      const prior = seen.get(id);
      seen.set(id, { count: (prior?.count ?? 0) + 1, last: Math.max(prior?.last ?? 0, run.startedAt) });
    }
  const hash = (id: string) => {
    let h = 2166136261;
    for (const char of `${seed}:${id}`) h = Math.imul(h ^ char.charCodeAt(0), 16777619);
    return h >>> 0;
  };
  const eligible = pool.filter((q) => q.level === level && q.unit === unit);
  if (new Set(eligible.map((q) => q.id)).size !== eligible.length) throw new Error("Duplicate bank item ID");
  if (eligible.length < count) throw new Error("Insufficient verified bank items");
  return [...eligible].sort((a, b) => {
    const av = seen.get(a.id) ?? { count: 0, last: 0 };
    const bv = seen.get(b.id) ?? { count: 0, last: 0 };
    return av.count - bv.count || av.last - bv.last || hash(a.id) - hash(b.id) || a.id.localeCompare(b.id);
  }).slice(0, count).map((q) => q.id);
}
