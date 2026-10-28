import { kampRegels, kampen, type Kamp } from "@/content/kampen";

/*
  De prijs van een kampinschrijving. Dezelfde berekening draait in de browser
  (om de prijs mee te tonen) en op de server (om te bewaren), zodat de ouder
  en het ouderportaal hetzelfde bedrag zien.

  Per dag: elk kind betaalt de dagprijs, en elk volgend kind uit hetzelfde
  gezin krijgt de broer-of-zuskorting. Met een verhoogde tegemoetkoming wordt
  het totaal daarna gehalveerd. Dagen van een volzet kamp tellen niet mee:
  daar staat het kind op de wachtlijst.
*/

export type KindKeuze = { dagen: string[] };

export function kampVanDag(dag: string): Kamp | undefined {
  return kampen.find((k) => k.dagen.some((d) => d.naam === dag));
}

export function berekenPrijs(kinderen: KindKeuze[], vt: boolean) {
  const perDag = new Map<string, number>();
  for (const kind of kinderen) {
    for (const dag of new Set(kind.dagen)) {
      if (kampVanDag(dag)?.volzet) continue;
      perDag.set(dag, (perDag.get(dag) ?? 0) + 1);
    }
  }

  let dagen = 0;
  let korting = 0;
  for (const aantal of perDag.values()) {
    dagen += aantal;
    korting += Math.max(0, aantal - 1) * kampRegels.broerZusKorting;
  }
  const subtotaal = dagen * kampRegels.prijsPerDag;
  const naKorting = subtotaal - korting;
  const totaal = vt ? Math.round(naKorting * 50) / 100 : naKorting;
  return { dagen, subtotaal, korting, vtKorting: naKorting - totaal, totaal };
}

export function euro(bedrag: number) {
  return `€${bedrag.toFixed(2).replace(".", ",").replace(",00", "")}`;
}
