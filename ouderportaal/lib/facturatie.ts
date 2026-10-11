import {
  euro,
  factuurLabel,
  langeDatum,
  type Activiteit,
} from "@/lib/activiteiten";

/*
  Van de aanwezigheden van een maand naar de regels van een factuur.

  Kim op 11 oktober 2026: "als ik dan in billit gewoon kan ingeven bijvoorbeeld
  5 x les young engineer, of 4 x plusklas of 4 x pluswerking zou dat makkelijk
  zijn. Zo kan ik maandelijks aangeven wat hun factuur is."

  Al het rekenwerk staat hier, zonder databank en zonder opmaak, zodat het
  apart na te rekenen is. Het scherm in app/beheer/facturatie gaat enkel nog
  over hoe het eruitziet.

  De regel die hier geldt: een kind dat ingeschreven staat, telt mee. Enkel een
  uitdrukkelijke "afwezig" valt eraf. Zo staat er na een maand waarin niemand
  iets aanduidde geen lege factuur, en is een vergeten vinkje niet meteen een
  vergeten inkomst. Hoeveel er nog niet aangeduid is, staat er wel bij, want
  een cijfer zonder dat erbij leest als zekerheid.
*/

export type DeelnameRij = {
  activiteit_id: string;
  kind_id: string;
  aanwezig: boolean | null;
};

export type KindRij = { id: string; naam: string; profile_id: string };

export type GezinRij = { id: string; full_name: string | null };

export type Ontvangst = {
  id: string;
  profile_id: string | null;
  datum: string;
  bedrag: number;
  wijze: string;
  opmerking: string | null;
  gestort_op: string | null;
};

export type Regel = {
  label: string;
  aantal: number;
  /* Hoeveel van die keren nog niemand aanduidde. */
  nietAangeduid: number;
  /* De prijs per keer, als die bij elke dag van deze regel dezelfde is. */
  prijs: number | null;
  /* De som van de prijzen die ingevuld zijn. */
  totaal: number;
  /* Bij hoeveel keren er geen prijs staat. */
  zonderPrijs: number;
  perKind: { naam: string; aantal: number }[];
};

export type GezinFactuur = {
  gezin: GezinRij;
  regels: Regel[];
  totaal: number;
  zonderPrijs: number;
  nietAangeduid: number;
  betaald: number;
  ontvangsten: Ontvangst[];
};

function bedrag(waarde: unknown): number | null {
  if (waarde === null || waarde === undefined || waarde === "") return null;
  const getal = Number(waarde);
  return Number.isFinite(getal) ? getal : null;
}

/* Telt mee op de factuur zolang er geen "afwezig" staat. */
export function teltMee(deelname: DeelnameRij) {
  return deelname.aanwezig !== false;
}

export function maakFacturen({
  activiteiten,
  deelnames,
  kinderen,
  gezinnen,
  ontvangsten = [],
}: {
  activiteiten: Activiteit[];
  deelnames: DeelnameRij[];
  kinderen: KindRij[];
  gezinnen: GezinRij[];
  ontvangsten?: Ontvangst[];
}): GezinFactuur[] {
  const activiteitVan = new Map(activiteiten.map((a) => [a.id, a]));
  const kindVan = new Map(kinderen.map((k) => [k.id, k]));
  const gezinVan = new Map(gezinnen.map((g) => [g.id, g]));

  /* gezin -> regel -> de tellingen van die regel */
  const perGezin = new Map<string, Map<string, Regel>>();

  for (const deelname of deelnames) {
    const activiteit = activiteitVan.get(deelname.activiteit_id);
    const kind = kindVan.get(deelname.kind_id);
    if (!activiteit || !kind || !teltMee(deelname)) continue;

    const label = factuurLabel(activiteit);
    const regels = perGezin.get(kind.profile_id) ?? new Map<string, Regel>();
    perGezin.set(kind.profile_id, regels);

    const regel: Regel = regels.get(label) ?? {
      label,
      aantal: 0,
      nietAangeduid: 0,
      prijs: null,
      totaal: 0,
      zonderPrijs: 0,
      perKind: [],
    };

    regel.aantal += 1;
    if (deelname.aanwezig === null) regel.nietAangeduid += 1;

    const prijs = bedrag(activiteit.prijs);
    if (prijs === null) regel.zonderPrijs += 1;
    else regel.totaal += prijs;

    /* De prijs per keer tonen we enkel als elke dag van deze regel hetzelfde
       kost; anders staat er een bedrag op het scherm dat nergens op klopt. */
    if (regel.aantal === 1) regel.prijs = prijs;
    else if (regel.prijs !== prijs) regel.prijs = null;

    const bestaand = regel.perKind.find((r) => r.naam === kind.naam);
    if (bestaand) bestaand.aantal += 1;
    else regel.perKind.push({ naam: kind.naam, aantal: 1 });

    regels.set(label, regel);
  }

  const betaaldPerGezin = new Map<string, Ontvangst[]>();
  for (const rij of ontvangsten) {
    if (!rij.profile_id) continue;
    const lijst = betaaldPerGezin.get(rij.profile_id) ?? [];
    lijst.push(rij);
    betaaldPerGezin.set(rij.profile_id, lijst);
  }

  const facturen: GezinFactuur[] = [];
  for (const [gezinId, regels] of perGezin) {
    const lijst = [...regels.values()].sort((a, b) =>
      a.label.localeCompare(b.label, "nl"),
    );
    for (const regel of lijst) {
      regel.perKind.sort((a, b) => a.naam.localeCompare(b.naam, "nl"));
    }
    const eigen = betaaldPerGezin.get(gezinId) ?? [];
    facturen.push({
      gezin: gezinVan.get(gezinId) ?? { id: gezinId, full_name: null },
      regels: lijst,
      totaal: lijst.reduce((som, r) => som + r.totaal, 0),
      zonderPrijs: lijst.reduce((som, r) => som + r.zonderPrijs, 0),
      nietAangeduid: lijst.reduce((som, r) => som + r.nietAangeduid, 0),
      betaald: eigen.reduce((som, r) => som + (bedrag(r.bedrag) ?? 0), 0),
      ontvangsten: eigen,
    });
  }

  return facturen.sort((a, b) =>
    (a.gezin.full_name ?? "").localeCompare(b.gezin.full_name ?? "", "nl"),
  );
}

export function gezinNaam(gezin: GezinRij) {
  return (gezin.full_name ?? "").trim() || "Gezin zonder naam";
}

/*
  De regels als tekst met tabs ertussen: beschrijving, aantal, prijs per keer.
  Zo staat elke kolom apart zodra je het in een rekenblad of in Billit plakt.
*/
export function alsRegels(factuur: GezinFactuur) {
  return factuur.regels
    .map((regel) =>
      [
        regel.label,
        regel.aantal,
        regel.prijs === null ? "" : regel.prijs.toFixed(2).replace(".", ","),
      ].join("\t"),
    )
    .join("\n");
}

/* Hetzelfde voor alle gezinnen samen, met het gezin als eerste kolom. */
export function allesAlsTabel(facturen: GezinFactuur[]) {
  const regels = [["Gezin", "Omschrijving", "Aantal", "Prijs per keer"].join("\t")];
  for (const factuur of facturen) {
    for (const regel of factuur.regels) {
      regels.push(
        [
          gezinNaam(factuur.gezin),
          regel.label,
          regel.aantal,
          regel.prijs === null ? "" : regel.prijs.toFixed(2).replace(".", ","),
        ].join("\t"),
      );
    }
  }
  return regels.join("\n");
}

/*
  Het zinnetje voor een factuur die al betaald is. Kim: "of als ouders al
  betaald hebben dat ik achteraf een voldaan factuur kan sturen."
*/
export function voldaanTekst(factuur: GezinFactuur, maand: string) {
  if (factuur.ontvangsten.length === 0) return null;
  const wijzen = [...new Set(factuur.ontvangsten.map((o) => o.wijze))].join(" en ");
  const datums = factuur.ontvangsten.map((o) => o.datum).sort();
  const laatste = datums[datums.length - 1];
  return (
    `Reeds betaald: ${euro(factuur.betaald)} (${wijzen}), ` +
    `laatste betaling op ${langeDatum(laatste)}. Deze factuur voor ${maand} ` +
    `is voldaan ` +
    `en dient enkel als bewijs.`
  );
}
