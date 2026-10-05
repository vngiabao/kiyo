export type SayoMood =
  "clear" | "cool" | "playful" | "intense" | "soft" | "deadpan";
export const voiceKey = (text: string) =>
  text.replace(/[\s，。！？,.!?、]/g, "");
/** Old saved voice preferences resolve to Sayo without changing learner data. */
export function sayoVoiceURI(uri = "") {
  return !uri || uri === "local:zf_001" || uri === "local:zm_010"
    ? "local:clear"
    : uri;
}
const reactionMoods: Record<string, SayoMood> = {
  认真一点开始吧: "cool",
  不错下一关: "deadpan",
  先改错再往前: "cool",
  看清题目别急: "cool",
  来了开始吧: "playful",
  再听一遍: "cool",
  大声说: "cool",
  看清楚: "playful",
  一笔一笔来: "soft",
  想一想: "cool",
  下次不看提示: "deadpan",
  太棒了: "intense",
  不错嘛: "deadpan",
  再来: "soft",
  声调呢: "deadpan",
  还记得吗: "cool",
  今天够了: "soft",
  又断了: "deadpan",
  升级了: "intense",
  天天来: "cool",
  对了: "intense",
  很好: "intense",
  漂亮: "intense",
  差一点: "soft",
  没关系再试试: "soft",
  从这儿开始: "cool",
  今天学得不错: "deadpan",
};
export const reactionMood = (text: string): SayoMood =>
  reactionMoods[voiceKey(text)] ?? "cool";
export const dialogueMood = (turn: number): SayoMood =>
  ["cool", "playful", "soft"][turn % 3] as SayoMood;
