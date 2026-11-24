/*
  De prijs van het oefenplatform staat hier, en alleen hier.
  Pas je hem hier aan, dan verandert hij meteen op elke pagina en bij de betaling.

  Black Friday (Kim, 24 november 2026): tot en met vrijdag 27 november 2026
  kost een schooljaar nog €20. Vanaf zaterdag 28 november 2026 wordt het
  vanzelf €50, zonder dat er iets opnieuw gezet moet worden. De datum telt in
  Belgische tijd: om middernacht in de nacht van vrijdag op zaterdag.

  PRIJS_ACTIE_EUR     = de oude, tijdelijke prijs (tot en met ACTIE_LAATSTE_DAG)
  PRIJS_STRAKS_EUR    = de gewone prijs daarna
  ACTIE_LAATSTE_DAG   = de laatste dag aan de oude prijs, als jjjj-mm-dd

  Wil je de actie langer laten lopen? Schuif dan ACTIE_LAATSTE_DAG op en pas de
  datum in de teksten hieronder mee aan.
*/

export const PRIJS_ACTIE_EUR = 20;
export const PRIJS_STRAKS_EUR = 50;
export const ACTIE_LAATSTE_DAG = "2026-11-27";

/* De datum van vandaag in België, als jjjj-mm-dd. */
function vandaagInBelgie(): string {
  return new Intl.DateTimeFormat("sv-SE", { timeZone: "Europe/Brussels" }).format(new Date());
}

/* Loopt de oude prijs nog? Tot en met vrijdag 27 november 2026. */
export function actieLoopt(): boolean {
  return vandaagInBelgie() <= ACTIE_LAATSTE_DAG;
}

/* Wat een gezin vandaag betaalt voor een volledig schooljaar. */
export function prijsNu(): number {
  return actieLoopt() ? PRIJS_ACTIE_EUR : PRIJS_STRAKS_EUR;
}

/*
  Wat dit gezin betaalt. Betalers die de enquête en een review instuurden,
  houden als dank hun vaste prijs (20 euro) zolang ze lid blijven, ook als de
  gewone prijs stijgt (Kim, 5 november 2026). Is de gewone prijs ooit lager,
  dan betalen ze die.
*/
export function prijsVoor(profile: { vaste_prijs_eur?: number | null } | null | undefined): number {
  const vast = profile?.vaste_prijs_eur;
  return vast && vast > 0 ? Math.min(vast, prijsNu()) : prijsNu();
}

/** Heeft dit gezin een vaste prijs die lager is dan de gewone? */
export function heeftVastePrijs(profile: { vaste_prijs_eur?: number | null } | null | undefined): boolean {
  return prijsVoor(profile) < prijsNu();
}

/*
  Het zinnetje dat bij de prijs hoort zolang de actie loopt. Vanaf zaterdag
  verdwijnt het overal vanzelf.
*/
export function tijdelijkePrijsUitleg(): string {
  return (
    `Black Friday: nog tot vrijdag 27 november om 24u betaal je €${PRIJS_ACTIE_EUR} voor een volledig schooljaar, ` +
    `voor het hele gezin. Vanaf zaterdag 28 november wordt dat €${PRIJS_STRAKS_EUR}. ` +
    `Wie nu betaalt, heeft toegang tot het einde van dit schooljaar.`
  );
}

/* Korte versie, voor waar weinig plaats is. */
export function tijdelijkePrijsKort(): string {
  return `Black Friday-prijs tot vrijdag 27 november 24u, daarna €${PRIJS_STRAKS_EUR}`;
}
