export type ClipEntry = {
  chunk: string;
  offset: number;
  length: number;
  sha256: string;
};
export type AudioIndex = { version: 1; files: Record<string, ClipEntry> };

export function indexShard(filename: string): string {
  let hash = 2166136261;
  for (const c of filename) hash = Math.imul(hash ^ c.charCodeAt(0), 16777619);
  return (hash & 255).toString(16).padStart(2, '0');
}
