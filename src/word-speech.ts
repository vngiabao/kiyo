/** Keep ambiguous readings and neutral suffixes in a meaningful speech context. */
export function wordSpeech(text: string, pinyin: string) {
  const reading = pinyin.toLowerCase().replace(/[\s,.!?]/gu, "");
  if (text === "地") {
    if (reading === "de") return "认真地读";
    if (reading === "dì") return "地上";
  }
  if (text === "干") {
    if (reading === "gān") return "干净";
    if (reading === "gàn") return "干什么";
  }
  if (text === "还" && reading === "huán") return "还书";
  if (text === "们" && reading === "men") return "朋友们";
  if (text === "子" && reading === "zi") return "桌子";
  if (text === "头" && reading === "tou") return "里头";
  if (text === "得") {
    if (reading === "de") return "说得清楚";
    if (reading === "dé") return "得到";
    if (reading === "děi") return "我得去";
  }
  if (text === "过" && reading === "guo") return "去过";
  if (text === "长") {
    if (reading === "zhǎng") return "长大";
    if (reading === "cháng") return "很长";
  }
  if (text === "行" && reading === "háng") return "一行字";
  if (text === "只" && reading === "zhī") return "一只猫";
  return text;
}
