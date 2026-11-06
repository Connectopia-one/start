/*
  Lijkt een ingevuld formulier op reclame van een robot?

  Kim op 6 november 2026: "er komen veel van deze irritante spam dingen in de
  verzoeken". Een voorbeeld: een terugbelverzoek met een lange Engelse
  verkooptekst en twee links, gsm-nummer 3627903985, en "Gerber" als naam
  van het kind, naam van de ouders én leeftijd. Het lokvakje hield dat niet
  tegen, want die robot vult enkel vakjes in die je kan zien.

  Er gaat hier NOOIT iets verloren. Wat verdacht is, komt in de databank met
  als soort "spam: <de gewone soort>" en een zin die zegt waarom. Het
  beheerscherm van het ouderportaal toont dat op een eigen tabblad Spam, met
  een knop om het terug te zetten als het toch een echte aanvraag was.

  Eén vreemd ding is nog geen spam: een ouder kan in het Engels schrijven, of
  een link naar zijn praktijk meesturen. Pas vanaf twee tekens samen zetten
  we het apart. Het verborgen vakje "website" (dat een mens niet ziet) is
  wel genoeg op zich.
*/

export const SPAM_VOORVOEGSEL = "spam: ";
export const SPAM_REDEN = "Waarom bij spam";

/* Engelse woordjes die in een Nederlandse tekst bijna nooit voorkomen. */
const ENGELS = new Set(
  (
    "the you your our are this that with for and to it if will would " +
    "free click here visit please customer customers call calls lead " +
    "leads offer price ranking unsubscribe hello cheers regards thanks " +
    "best just don't i'm it's what who they them"
  ).split(" "),
);

/* En Nederlandse, om te vergelijken. */
const NEDERLANDS = new Set(
  (
    "de het een en van ik je jij u wij we ons onze is zijn met voor " +
    "op in dat die niet wel ook maar graag kind kinderen zoon dochter " +
    "mijn hij zij er om bij hallo dag dank groeten vraag kan kunnen"
  ).split(" "),
);

/* Een getal in woorden, voor wie de leeftijd uitschrijft. */
const GETALWOORDEN =
  /\b(een|twee|drie|vier|vijf|zes|zeven|acht|negen|tien|elf|twaalf|dertien|veertien|vijftien|zestien|zeventien|achttien|maand|maanden|jaar|jaren|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|years?|months?)\b/i;

const LINK = /(https?:\/\/|www\.|\b[a-z0-9-]+\.(com|net|org|io|co|info|biz|xyz)\b)/i;

function telWoorden(tekst: string, lijst: Set<string>) {
  return (tekst.toLowerCase().match(/[a-z']+/g) ?? []).filter((w) =>
    lijst.has(w),
  ).length;
}

/*
  Een gsm- of telefoonnummer zoals een Belgische ouder het intypt:
  0468 35 74 96, 468357496 (de 0 vergeten), +32 468 ..., 0032 ..., of een
  buitenlands nummer met + of 00 ervoor. 3627903985 is geen van die.
*/
function lijktOpTelefoon(waarde: string) {
  const schoon = waarde.replace(/[\s./()-]/g, "");
  if (/^(\+|00)\d{8,15}$/.test(schoon)) return true;
  if (/^0\d{8,9}$/.test(schoon)) return true;
  if (/^4\d{8}$/.test(schoon)) return true;
  if (/^32\d{8,9}$/.test(schoon)) return true;
  return false;
}

export function spamRedenen(
  gegevens: Record<string, string>,
  lokvakjeWebsite: string,
): string[] {
  if (lokvakjeWebsite.trim()) {
    return ["het verborgen vakje dat enkel robots zien, was ingevuld"];
  }

  const redenen: string[] = [];
  const vakjes = Object.entries(gegevens);
  const vrijeTekst = vakjes
    /* Een mailadres zoals jan@telenet.be is geen link, en een vakje dat
       naar een website vraagt mag er een hebben. */
    .filter(([vraag]) => !/mail|website|webadres|site/i.test(vraag))
    .map(([, antwoord]) => antwoord)
    .join(" \n ");

  if (LINK.test(vrijeTekst)) redenen.push("er staat een link in");

  const engels = telWoorden(vrijeTekst, ENGELS);
  const nederlands = telWoorden(vrijeTekst, NEDERLANDS);
  if (engels >= 6 && engels > nederlands * 2) {
    redenen.push("de tekst is in het Engels");
  }

  const telefoon = vakjes.find(([vraag]) => /gsm|telefoon/i.test(vraag))?.[1];
  if (telefoon && !lijktOpTelefoon(telefoon)) {
    redenen.push(`${telefoon} is geen gewoon telefoonnummer`);
  }

  /* Dezelfde naam in drie of meer vakjes, zoals "Gerber" overal. */
  const perAntwoord = new Map<string, number>();
  for (const [, antwoord] of vakjes) {
    const a = antwoord.trim().toLowerCase();
    if (!a || a === "ja" || a === "nee") continue;
    perAntwoord.set(a, (perAntwoord.get(a) ?? 0) + 1);
  }
  const herhaald = [...perAntwoord.entries()].find(([, n]) => n >= 3);
  if (herhaald) {
    redenen.push(`"${herhaald[0]}" staat in ${herhaald[1]} vakjes`);
  }

  const leeftijd = vakjes.find(([vraag]) => /leeftijd/i.test(vraag))?.[1];
  if (leeftijd && !/\d/.test(leeftijd) && !GETALWOORDEN.test(leeftijd)) {
    redenen.push("bij de leeftijd staat geen getal");
  }

  return redenen.length >= 2 ? redenen : [];
}
