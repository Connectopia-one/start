export function slugify(input: string): string {
  const normalized = input.normalize("NFD");
  let stripped = "";
  for (const ch of normalized) {
    const code = ch.codePointAt(0) ?? 0;
    const isCombiningMark = code >= 0x0300 && code <= 0x036f;
    if (!isCombiningMark) stripped += ch;
  }
  return stripped
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "");
}
