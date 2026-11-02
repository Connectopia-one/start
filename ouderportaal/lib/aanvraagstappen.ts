/*
  Wat er met een aanvraag al gebeurde.

  Kim op 2 november 2026: "als ik afgehandeld zet, is dat afgehandeld, maar
  dat betekent niet dat dat bezig is. Ik heb meer knoppen nodig: mail
  verstuurd, ingeschreven of niet ingeschreven." Eén vinkje "afgehandeld"
  zei niet wát er gebeurd was.

  Elke stap is een knop bij de aanvraag en een filter bovenaan. Een aanvraag
  kan meerdere stappen hebben (mail verstuurd én ingeschreven). Een stap
  erbij zetten kan hier, zonder SQL: de databank bewaart enkel de naam.

  "tegenover" zijn twee stappen die niet samen kunnen: wie ingeschreven is,
  is niet ook niet-ingeschreven. Zet je de ene aan, dan gaat de andere uit.

  "Behandeld" staat hier niet bij: dat is de bestaande kolom afgehandeld, en
  die beslist of een aanvraag bij Te behandelen of bij Behandeld staat.
*/
export const STAPPEN = [
  { sleutel: "mail verstuurd", naam: "Mail verstuurd" },
  { sleutel: "gebeld", naam: "Gebeld" },
  { sleutel: "wacht op antwoord", naam: "Wacht op antwoord" },
  { sleutel: "ingeschreven", naam: "Ingeschreven", tegenover: "niet ingeschreven" },
  { sleutel: "niet ingeschreven", naam: "Niet ingeschreven", tegenover: "ingeschreven" },
  /* Kim op 2 november 2026: "bij de kampen aanklikken wie betaald heeft en
     wie nog moet betalen." Betaald geldt voor het hele gezin: alle kinderen
     met dezelfde mededeling gaan samen aan of uit (zie zetStapVoorGezin). */
  { sleutel: "betaald", naam: "Betaald" },
] as const;

export type Stap = (typeof STAPPEN)[number]["sleutel"];

export function isStap(waarde: string): waarde is Stap {
  return STAPPEN.some((s) => s.sleutel === waarde);
}

/* De nieuwe lijst stappen na een klik op een knop. */
export function wisselStap(huidig: string[], stap: Stap, aan: boolean) {
  const def = STAPPEN.find((s) => s.sleutel === stap);
  const tegenover = def && "tegenover" in def ? def.tegenover : null;
  const zonder = huidig.filter((s) => s !== stap && s !== tegenover);
  return aan ? [...zonder, stap] : zonder;
}
