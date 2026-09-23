/**
 * De volgorde waarin hoofdstukken in een lijst horen te staan.
 *
 * Normaal is dat gewoon het volgnummer. Eén geval vraagt meer: sinds we een
 * thema opsplitsen in een "— deel 1" en een "— deel 2", krijgt dat deel 2 het
 * eerstvolgende vrije nummer, en dat is zelden het nummer naast deel 1. Zonder
 * ingreep staan dan éérst alle delen 1 onder elkaar en daarna pas alle delen 2,
 * en moet een kind dat net deel 1 afwerkte helemaal naar beneden scrollen.
 *
 * Daarom sorteren we op het thema (de titel vóór "— deel"), op de plaats van
 * het vroegste deel van dat thema, en pas daarbinnen op deelnummer. Wie geen
 * deel in zijn titel heeft, houdt gewoon zijn eigen plaats.
 *
 * Dit is enkel de weergave. In de databank verandert er niets, dus webadressen
 * en voortgang blijven kloppen.
 */

export type TeSorteren = { titel: string; volgnummer: number };

const DEEL = /\s*[—–-]\s*deel\s+(\d+)\s*$/i;

/** "Getallenleer — deel 2" → { thema: "getallenleer", deel: 2 } */
export function splitsDeel(titel: string): { thema: string; deel: number } {
  const treffer = titel.match(DEEL);
  if (!treffer) return { thema: titel.trim().toLowerCase(), deel: 0 };
  return {
    thema: titel.slice(0, treffer.index).trim().toLowerCase(),
    deel: Number(treffer[1]),
  };
}

export function sorteerHoofdstukken<T extends TeSorteren>(hoofdstukken: T[]): T[] {
  // Per thema het laagste volgnummer: daar komt de hele groep te staan.
  const plaatsVanThema = new Map<string, number>();
  for (const h of hoofdstukken) {
    const { thema } = splitsDeel(h.titel);
    const huidige = plaatsVanThema.get(thema);
    if (huidige === undefined || h.volgnummer < huidige) {
      plaatsVanThema.set(thema, h.volgnummer);
    }
  }

  return [...hoofdstukken].sort((a, b) => {
    const da = splitsDeel(a.titel);
    const db = splitsDeel(b.titel);
    const pa = plaatsVanThema.get(da.thema) ?? a.volgnummer;
    const pb = plaatsVanThema.get(db.thema) ?? b.volgnummer;
    if (pa !== pb) return pa - pb;
    if (da.deel !== db.deel) return da.deel - db.deel;
    return a.volgnummer - b.volgnummer;
  });
}
