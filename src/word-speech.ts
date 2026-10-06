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
  return text;
}
