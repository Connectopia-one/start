/**
 * Meerkeuzevragen met méér dan één juist antwoord.
 *
 * Waarom dit bestaat: op het examen van de examencommissie staat bij een
 * meerkeuzevraag niet hoeveel antwoorden juist zijn. Duidt een kind er één aan
 * terwijl er twee juist waren, dan is de hele vraag fout — geen halve punten.
 * Wie dat nooit geoefend heeft, loopt daar punten mis. Vanaf ✨ Spark staan er
 * daarom vragen tussen waarbij je álle juiste antwoorden moet aanklikken.
 *
 * In de databank verandert er niets aan de tabel: `antwoord` is jsonb, dus een
 * vraag met meerdere juiste antwoorden bewaart daar gewoon een lijstje
 * nummers, bijvoorbeeld [0, 2], in plaats van één nummer. Wat een kind
 * antwoordde (`gegeven_antwoord`) wordt op dezelfde manier bewaard.
 *
 * Belangrijk voor het oefenen: zodra er in een hoofdstuk één zo'n vraag staat,
 * krijgen álle meerkeuzevragen van dat hoofdstuk aankruisvakjes. Anders zou het
 * vakje zelf verklappen bij welke vraag er meer dan één antwoord juist is, en
 * dan oefen je net niet wat je moet oefenen.
 */

/** De juiste antwoorden van een meerkeuzevraag, altijd als lijstje nummers. */
export function juisteKeuzes(antwoord: unknown): number[] {
  if (Array.isArray(antwoord)) {
    return antwoord.map(Number).filter((n) => Number.isInteger(n));
  }
  return typeof antwoord === "number" && Number.isInteger(antwoord) ? [antwoord] : [];
}

/** Heeft deze vraag meer dan één juist antwoord? */
export function heeftMeerdereAntwoorden(vraag: { type: string; antwoord: unknown }): boolean {
  return vraag.type === "meerkeuze" && Array.isArray(vraag.antwoord) && vraag.antwoord.length > 1;
}

/** Wat een kind aanklikte, altijd als lijstje nummers. */
export function gegevenKeuzes(waarde: unknown): number[] {
  if (Array.isArray(waarde)) return waarde.map(Number).filter((n) => Number.isInteger(n));
  return typeof waarde === "number" && Number.isInteger(waarde) ? [waarde] : [];
}

/** Twee lijstjes keuzes zijn gelijk als ze precies dezelfde nummers bevatten. */
export function zelfdeKeuzes(a: number[], b: number[]): boolean {
  if (a.length !== b.length) return false;
  const gesorteerd = [...a].sort((x, y) => x - y);
  return [...b].sort((x, y) => x - y).every((n, i) => n === gesorteerd[i]);
}

/**
 * De tekst van wat er aangeduid werd, voor de pagina's waar een ouder of
 * begeleider meekijkt: "Parijs" of "Parijs en Rome".
 */
export function schrijfKeuzes(opties: string[] | null | undefined, waarde: unknown): string {
  const keuzes = gegevenKeuzes(waarde);
  if (!keuzes.length) return "—";
  const teksten = keuzes.map((i) => opties?.[i] ?? "—");
  if (teksten.length === 1) return teksten[0];
  return teksten.slice(0, -1).join(", ") + " en " + teksten[teksten.length - 1];
}
