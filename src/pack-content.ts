/**
 * Validated content packs, compiled once. src/generated/packs.json is written
 * by scripts/build-packs.ts and only ever contains packs that passed checks.
 */
import generated from "./generated/packs.json" with { type: "json" };
import { compilePack, type ContentPack } from "./packs";

export const packs = (generated as unknown as ContentPack[])
  .slice()
  .sort((a, b) => a.unit.stage - b.unit.stage || a.unit.order - b.unit.order);
export const compiledPacks = packs.map(compilePack);
