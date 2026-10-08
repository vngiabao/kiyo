/** Dictionary exports sometimes spell ü as u:, including before a marked e. */
export const normalizePinyinReference = (pinyin: string) =>
  pinyin.normalize("NFC").replace(/u:/gi, (v) => (v[0] === "U" ? "Ü" : "ü"));
