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
