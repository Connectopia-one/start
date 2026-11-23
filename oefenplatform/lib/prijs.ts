/*
  De prijs van het oefenplatform staat hier, en alleen hier.
  Pas je hem hier aan, dan verandert hij meteen op elke pagina en bij de betaling.

  PRIJS_NU_EUR      = wat een gezin vandaag betaalt voor een volledig schooljaar.
  PRIJS_STRAKS_EUR  = de prijs waar we naartoe gaan zodra het platform af is.
  TIJDELIJKE_PRIJS  = zet dit op  false  zodra de gewone prijs ingaat. Dan betaalt
                      iedereen PRIJS_NU_EUR en verdwijnt overal vanzelf het
                      zinnetje over de tijdelijke prijs.
*/

export const PRIJS_NU_EUR = 20;
export const PRIJS_STRAKS_EUR = 50;
export const TIJDELIJKE_PRIJS = true;

/*
  Wat dit gezin betaalt. Betalers die de enquête en een review instuurden,
  houden als dank hun vaste prijs (20 euro) zolang ze lid blijven, ook als de
  gewone prijs stijgt (Kim, 5 november 2026). Is de gewone prijs ooit lager,
  dan betalen ze die.
*/
export function prijsVoor(profile: { vaste_prijs_eur?: number | null } | null | undefined): number {
  const vast = profile?.vaste_prijs_eur;
  return vast && vast > 0 ? Math.min(vast, PRIJS_NU_EUR) : PRIJS_NU_EUR;
}

/** Heeft dit gezin een vaste prijs die lager is dan de gewone? */
export function heeftVastePrijs(profile: { vaste_prijs_eur?: number | null } | null | undefined): boolean {
  return prijsVoor(profile) < PRIJS_NU_EUR;
}

/*
  Het zinnetje dat bij de prijs hoort zolang die tijdelijk is.
  Je mag de tekst gerust herschrijven; de bedragen vullen zichzelf in.
*/
export const TIJDELIJKE_PRIJS_UITLEG =
  `Tijdelijk €${PRIJS_NU_EUR} in plaats van €${PRIJS_STRAKS_EUR}, omdat het platform nog volop in opbouw is. ` +
  `Met die bijdrage kunnen we blijven verder ontwikkelen. Zodra het platform volledig is, ` +
  `wordt de toegang €${PRIJS_STRAKS_EUR} per schooljaar voor een heel gezin.`;

/* Korte versie, voor waar weinig plaats is. */
export const TIJDELIJKE_PRIJS_KORT =
  `tijdelijke prijs — later €${PRIJS_STRAKS_EUR} per schooljaar per gezin`;
