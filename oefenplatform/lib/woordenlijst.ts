export type Woord = { woord: string; uitleg: string };

/**
 * De woordenlijst van een leestekst wordt in Beheer ingetypt als één woord per
 * regel, "woord = uitleg". Dat leest een mens vlotter dan JSON.
 */
export function leesWoordenlijst(ruw: string): Woord[] {
  return ruw
    .split("\n")
    .map((regel) => regel.trim())
    .filter(Boolean)
    .map((regel) => {
      const scheiding = regel.indexOf("=");
      if (scheiding < 0) return null;
      const woord = regel.slice(0, scheiding).trim();
      const uitleg = regel.slice(scheiding + 1).trim();
      return woord && uitleg ? { woord, uitleg } : null;
    })
    .filter((w): w is Woord => w !== null);
}

/** Omgekeerd: de lijst terug naar regels om in het tekstvak te tonen. */
export function schrijfWoordenlijst(lijst: Woord[] | null | undefined) {
  return (lijst ?? []).map((w) => `${w.woord} = ${w.uitleg}`).join("\n");
}
