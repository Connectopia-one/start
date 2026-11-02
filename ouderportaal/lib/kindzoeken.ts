/*
  Een kind van een inschrijvingslijst terugvinden in het ouderportaal.

  Kim op 2 november 2026, de ochtend van het herfstkamp: "kunnen de lijsten
  van de kampen dus herfstkampen en kerstkampen niet automatisch hier bij
  kampen komen te staan. nu moet ik alles nog met de hand daar in gaan
  zetten".

  Op het inschrijfformulier typt een ouder de naam zelf, dus die is zelden
  letter voor letter dezelfde als in het ouderportaal: "Ellena" tegen
  "Elena", "Mats" tegen "Mats Noben". We vergelijken daarom zonder
  hoofdletters en accenten, en laten één tikfout toe in de voornaam. Is er
  dan nog twijfel, dan beslist het gsm-nummer of het mailadres van de ouder.
  Blijft het onzeker, dan kiezen we niets: een verkeerde fiche op een
  kamplijst is erger dan een ontbrekende.
*/

export type PortaalKind = {
  id: string;
  naam: string;
  telefoon: string | null;
  mail: string | null;
};

function plat(tekst: string) {
  return tekst
    .normalize("NFD")
    .replace(/[̀-ͯ]/g, "")
    .toLowerCase()
    .replace(/[^a-z0-9 ]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function cijfers(tekst: string | null | undefined) {
  const c = (tekst ?? "").replace(/\D/g, "");
  /* 0468 en +32 468 zijn hetzelfde nummer. */
  return c.replace(/^0032/, "0").replace(/^32(?=4)/, "0");
}

/* Hoeveel letters verschillen twee woorden? Enkel nodig voor korte namen. */
function afstand(a: string, b: string) {
  const rij = Array.from({ length: b.length + 1 }, (_, i) => i);
  for (let i = 1; i <= a.length; i++) {
    let vorige = rij[0];
    rij[0] = i;
    for (let j = 1; j <= b.length; j++) {
      const nu = rij[j];
      rij[j] = Math.min(
        rij[j] + 1,
        rij[j - 1] + 1,
        vorige + (a[i - 1] === b[j - 1] ? 0 : 1),
      );
      vorige = nu;
    }
  }
  return rij[b.length];
}

export function zoekKind(
  naam: string,
  ouder: { gsm?: string | null; mail?: string | null },
  kinderen: PortaalKind[],
): PortaalKind | null {
  const gezocht = plat(naam);
  if (!gezocht) return null;

  const exact = kinderen.filter((k) => plat(k.naam) === gezocht);
  if (exact.length === 1) return exact[0];

  /* "Mats" tegen "Mats Noben", "Max-Emile" tegen "Max-Emile Cupers". */
  const langer = kinderen.filter((k) => plat(k.naam).startsWith(gezocht + " "));
  if (langer.length === 1) return langer[0];
  const korter = kinderen.filter((k) => gezocht.startsWith(plat(k.naam) + " "));
  if (langer.length === 0 && korter.length === 1) return korter[0];

  const voornaam = gezocht.split(" ")[0];
  const lijktOp = (exact.length ? exact : kinderen).filter((k) => {
    const andere = plat(k.naam).split(" ")[0];
    if (andere === voornaam) return true;
    return voornaam.length >= 4 && afstand(andere, voornaam) <= 1;
  });

  const gsm = cijfers(ouder.gsm);
  const mail = (ouder.mail ?? "").trim().toLowerCase();
  const vanGezin = (k: PortaalKind) =>
    (gsm.length >= 9 && cijfers(k.telefoon) === gsm) ||
    (!!mail && (k.mail ?? "").trim().toLowerCase() === mail);

  const zelfdeGezin = lijktOp.filter(vanGezin);
  if (zelfdeGezin.length === 1) return zelfdeGezin[0];
  if (lijktOp.length === 1) return lijktOp[0];

  /* De naam lijkt op niets, maar het gezin staat er wel, met hetzelfde
     mailadres of gsm-nummer. Kim op 2 november 2026: Jaxx, Kid, Lennert en
     Logan stonden als "zonder fiche" terwijl hun gezin een fiche in orde had;
     in het ouderportaal heet het kind anders dan op het formulier. Heeft dat
     gezin één kind, dan is het dat kind. Heeft het er meer, dan nemen we het
     enige wiens voornaam er nog wat op lijkt, anders niets. */
  const gezin = kinderen.filter(vanGezin);
  if (gezin.length === 1) return gezin[0];
  const bijna = gezin.filter((k) => {
    const andere = plat(k.naam).split(" ")[0];
    return andere.startsWith(voornaam) || voornaam.startsWith(andere) ||
      afstand(andere, voornaam) <= 2;
  });
  if (bijna.length === 1) return bijna[0];
  return null;
}

const MAANDEN = [
  "januari", "februari", "maart", "april", "mei", "juni",
  "juli", "augustus", "september", "oktober", "november", "december",
];

/* "Hasselt maandag 2 november" wordt 2026-11-02. Het jaar is dat van
   vandaag, of het volgende als die maand al lang voorbij is. */
export function datumUitNaam(naam: string, vandaag = new Date()): string | null {
  const tekst = naam.toLowerCase();
  const maand = MAANDEN.findIndex((m) => tekst.includes(m));
  const dag = Number(tekst.match(/\b(\d{1,2})\b/)?.[1] ?? 0);
  if (maand < 0 || dag < 1 || dag > 31) return null;
  let jaar = vandaag.getFullYear();
  if (maand < vandaag.getMonth() - 2) jaar++;
  return `${jaar}-${String(maand + 1).padStart(2, "0")}-${String(dag).padStart(2, "0")}`;
}

/* "Hasselt maandag 2 november" geeft "Hasselt"; zo kent Kampen en lessen ook
   de plaats. */
export function plaatsUitNaam(naam: string): string | null {
  const eerste = naam.trim().split(/\s+/)[0] ?? "";
  return /^(hasselt|genk)$/i.test(eerste) ? eerste : null;
}

/* Het gezin van een inschrijving, op mailadres of gsm-nummer. */
export function zoekGezin<G extends { telefoon: string | null; mail: string | null }>(
  ouder: { gsm?: string | null; mail?: string | null },
  gezinnen: G[],
): G | null {
  const gsm = cijfers(ouder.gsm);
  const mail = (ouder.mail ?? "").trim().toLowerCase();
  const op = gezinnen.filter(
    (g) =>
      (!!mail && (g.mail ?? "").trim().toLowerCase() === mail) ||
      (gsm.length >= 9 && cijfers(g.telefoon) === gsm),
  );
  return op.length === 1 ? op[0] : null;
}
