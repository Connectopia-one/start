/**
 * Twee vraagvormen van het examen van de Examencommissie, en de vaste zin die
 * daar boven elke vraag staat.
 *
 * Waarom dit bestaat: op 26 oktober 2026 zijn het voorbeeldexamen en het
 * proefexamen van de Examencommissie vraag per vraag doorlopen (verslag in
 * examencommissie/vraagstelling-examencommissie.md in de projectmap). Twee
 * vormen kwamen daar telkens terug die het platform nog niet had:
 *
 *   - een tabel waarin je per rij aanduidt of een uitspraak juist of fout is.
 *     Waar of niet waar komt op dat examen nooit als losse vraag voor, enkel
 *     zo, met meerdere uitspraken onder elkaar;
 *   - een zin met een keuzelijst op de plaats van een ontbrekend woord, soms
 *     twee of drie keuzelijsten in dezelfde zin.
 *
 * Bij allebei krijg je alleen punten als alles juist is. Eén rij fout is de
 * hele vraag fout, net als bij meerkeuze met meerdere juiste antwoorden.
 *
 * In de databank verandert er niets aan de kolommen, enkel aan het lijstje
 * toegelaten types (zie supabase/vraagvormen.sql):
 *
 *   tabel       opties   de uitspraken, één per rij
 *               antwoord {"kolommen": ["Juist", "Fout"], "juist": [0, 1, 0]}
 *                        per rij het nummer van de juiste kolom
 *
 *   keuzelijst  vraag    de zin, met elke keuzelijst als [[stijgende|dalende]]
 *               antwoord [0, 2], per keuzelijst het nummer van de juiste optie
 *
 * Wat een kind antwoordt, wordt bij allebei bewaard als een lijstje nummers,
 * per rij of per keuzelijst. Wat het (nog) niet koos, staat er als -1.
 */

import { zaad } from "@/lib/optievolgorde";
import { instructieNieuw, schrijfNieuw, zetNieuweVormKlaar } from "@/lib/examenvormen";

/** Alle soorten vragen die het platform kent. Zie ook lib/examenvormen.ts. */
export const VRAAGTYPES = [
  "meerkeuze", "invultekst", "waarofniet", "tabel", "keuzelijst",
  "volgorde", "koppelen", "sorteren", "sleepzin", "hotspot", "open", "tekenen",
] as const;
export type VraagType = (typeof VRAAGTYPES)[number];

export const STANDAARD_KOLOMMEN = ["Juist", "Fout"];

// ---------------------------------------------------------------------------
// De tabel

export type Tabel = { rijen: string[]; kolommen: string[]; juist: number[] };

/** De tabel zoals ze in de databank staat, of null als er iets niet klopt. */
export function leesTabel(opties: unknown, antwoord: unknown): Tabel | null {
  if (!Array.isArray(opties) || !opties.length) return null;
  const a = (antwoord ?? {}) as { kolommen?: unknown; juist?: unknown };
  const kolommen = Array.isArray(a.kolommen) && a.kolommen.length >= 2
    ? a.kolommen.map(String)
    : STANDAARD_KOLOMMEN;
  const juist = Array.isArray(a.juist) ? a.juist.map(Number) : [];
  if (juist.length !== opties.length) return null;
  if (!juist.every((k) => Number.isInteger(k) && k >= 0 && k < kolommen.length)) return null;
  return { rijen: opties.map(String), kolommen, juist };
}

// ---------------------------------------------------------------------------
// De keuzelijst in een zin

const LIJST = /\[\[([^\]]+?)\]\]/g;

export type ZinStuk = { soort: "tekst"; tekst: string } | { soort: "lijst"; nummer: number; opties: string[] };

/** De zin in stukken: gewone tekst en keuzelijsten, in de volgorde van de zin. */
export function leesKeuzezin(vraag: string): ZinStuk[] {
  const stukken: ZinStuk[] = [];
  let vorige = 0;
  let nummer = 0;
  for (const m of vraag.matchAll(LIJST)) {
    if (m.index > vorige) stukken.push({ soort: "tekst", tekst: vraag.slice(vorige, m.index) });
    vorige = m.index + m[0].length;
    const opties = m[1].split("|").map((o) => o.trim()).filter(Boolean);
    stukken.push({ soort: "lijst", nummer: nummer++, opties });
  }
  if (vorige < vraag.length) stukken.push({ soort: "tekst", tekst: vraag.slice(vorige) });
  return stukken;
}

/** De opties van elke keuzelijst in de zin, in volgorde. */
export function keuzelijsten(vraag: string): string[][] {
  return leesKeuzezin(vraag)
    .filter((s): s is Extract<ZinStuk, { soort: "lijst" }> => s.soort === "lijst")
    .map((s) => s.opties);
}

/** Per keuzelijst het nummer van de juiste optie. */
export function keuzelijstJuist(antwoord: unknown): number[] {
  return Array.isArray(antwoord) ? antwoord.map(Number) : [];
}

/**
 * De volgorde waarin de opties van één keuzelijst getoond worden.
 *
 * Wie een zin schrijft, zet het juiste woord bijna vanzelf vooraan. Dat is
 * bij meerkeuze al eens gebleken (zie lib/optievolgorde.ts), dus schudden we
 * hier ook. De volgorde volgt uit het id van de vraag en het nummer van de
 * lijst, zodat ze vastligt: herladen geeft dezelfde volgorde.
 */
export function lijstVolgorde(vraagId: string, nummer: number, aantal: number): number[] {
  let t = zaad(`${vraagId}#${nummer}`);
  const volgend = () => {
    t = (Math.imul(t ^ (t >>> 15), 0x2c1b3c6d) + 0x9e3779b9) >>> 0;
    return t / 4294967296;
  };
  const volgorde = Array.from({ length: aantal }, (_, i) => i);
  for (let i = volgorde.length - 1; i > 0; i--) {
    const j = Math.floor(volgend() * (i + 1));
    [volgorde[i], volgorde[j]] = [volgorde[j], volgorde[i]];
  }
  return volgorde;
}

/**
 * De zin met de keuzelijsten uitgeschreven, voor plaatsen waar geen lijstje
 * kan staan: een rapport, een pdf, de lijst in Beheer. Met `juist` erbij staat
 * het juiste woord in de plaats van de lijst.
 */
export function keuzezinAlsTekst(vraag: string, juist?: number[]): string {
  return leesKeuzezin(vraag)
    .map((s) => {
      if (s.soort === "tekst") return s.tekst;
      if (juist) return s.opties[juist[s.nummer]] ?? "…";
      // Een leeg vak van een sleepzin (zie lib/examenvormen.ts).
      if (s.opties.length === 1 && s.opties[0] === "_") return "____";
      return `[${s.opties.join(" / ")}]`;
    })
    .join("");
}

/**
 * Een zin zoals je ze intikt, met een sterretje voor het juiste woord:
 * "een [[*stijgende|dalende]] rechte". Geeft de zin zonder sterretjes terug en
 * per keuzelijst het nummer van de optie met het sterretje. Staat er in een
 * lijst geen of meer dan één sterretje, dan is `juist` null.
 */
export function leesSterretjes(vraag: string): { vraag: string; juist: number[] | null } {
  const juist: number[] = [];
  let goed = true;
  const zonder = vraag.replace(LIJST, (_, binnen: string) => {
    const opties = binnen.split("|").map((o) => o.trim()).filter(Boolean);
    const met = opties.map((o, i) => (o.startsWith("*") ? i : -1)).filter((i) => i >= 0);
    if (met.length !== 1) goed = false;
    juist.push(met[0] ?? -1);
    return `[[${opties.map((o) => o.replace(/^\*\s*/, "")).join("|")}]]`;
  });
  return { vraag: zonder, juist: goed && juist.length ? juist : null };
}

/** De weg terug: het sterretje terug voor het juiste woord, om aan te passen. */
export function metSterretjes(vraag: string, juist: number[]): string {
  let nummer = 0;
  return vraag.replace(LIJST, (_, binnen: string) => {
    const k = juist[nummer++];
    const opties = binnen.split("|").map((o) => o.trim()).filter(Boolean);
    return `[[${opties.map((o, i) => (i === k ? `*${o}` : o)).join("|")}]]`;
  });
}

// ---------------------------------------------------------------------------
// Nakijken en uitschrijven, gedeeld door de quiz en de pagina's waar een ouder
// of begeleider meekijkt.

/** Alles of niets: elke rij of elke keuzelijst moet juist zijn. */
export function alleJuist(gegeven: unknown, juist: number[]): boolean {
  if (!Array.isArray(gegeven) || gegeven.length !== juist.length || !juist.length) return false;
  return juist.every((k, i) => Number(gegeven[i]) === k);
}

/**
 * Wat een kind aanduidde bij een tabel of een keuzelijst, in woorden.
 * Geeft null bij elk ander type, zodat de bestaande code verder kan.
 */
export function schrijfVorm(
  vraag: { type: string; vraag: string; opties: string[] | null; antwoord: unknown },
  waarde: unknown,
): string | null {
  if (vraag.type !== "tabel" && vraag.type !== "keuzelijst") return schrijfNieuw(vraag, waarde);
  // Het juiste antwoord van een tabel komt hier binnen zoals het bewaard
  // staat, met de kolommen erbij; wat een kind koos is een gewoon lijstje.
  const binnen = waarde as { juist?: unknown } | null;
  const lijst = Array.isArray(waarde)
    ? waarde.map(Number)
    : Array.isArray(binnen?.juist)
      ? binnen.juist.map(Number)
      : [];
  if (vraag.type === "tabel") {
    const tabel = leesTabel(vraag.opties, vraag.antwoord);
    if (!tabel) return "—";
    return tabel.rijen
      .map((rij, i) => `${rij}: ${tabel.kolommen[lijst[i]] ?? "niets"}`)
      .join(" · ");
  }
  return keuzelijsten(vraag.vraag)
    .map((opties, i) => opties[lijst[i]] ?? "niets")
    .join(" · ");
}

// ---------------------------------------------------------------------------
// De vaste zin boven de vraag

/**
 * Op het examen staat boven elke vraag een korte, vaste zin die zegt wat je
 * moet doen, en bij sommige vormen een tweede over de punten. Een kind dat
 * die zinnen hier al honderd keer las, hoeft er op het examen niet meer over
 * na te denken.
 *
 * `vakjes`: in dit hoofdstuk kan er bij meerkeuze meer dan één antwoord juist
 * zijn (zie lib/antwoord.ts). Dan staat er bij élke meerkeuzevraag "Duid alle
 * juiste antwoorden aan.", ook als er maar één juist is, net zoals op het
 * examen niet staat hoeveel het er zijn.
 *
 * `interactie`: een kleur- of sleepvraag (zie components/Figuren.tsx) zegt in
 * haar eigen tekst al wat je moet doen.
 */
export function instructie(
  type: string,
  {
    vakjes = false,
    interactie = false,
    vraag,
  }: { vakjes?: boolean; interactie?: boolean; vraag?: { opties: unknown; antwoord: unknown } } = {},
): { zin: string; punten: string | null } | null {
  const nieuw = instructieNieuw(type, vraag ?? { opties: null, antwoord: null });
  if (nieuw) return nieuw;
  if (type === "meerkeuze") {
    return vakjes
      ? { zin: "Duid alle juiste antwoorden aan.", punten: "Je krijgt alleen punten als je alle juiste antwoorden aanduidt." }
      : { zin: "Duid het enige juiste antwoord aan.", punten: null };
  }
  if (type === "waarofniet") return { zin: "Duid aan of de uitspraak waar of niet waar is.", punten: null };
  if (type === "invultekst") return interactie ? null : { zin: "Typ het antwoord in het lege vak.", punten: null };
  if (type === "tabel") {
    return {
      zin: "Duid per rij het enige juiste antwoord aan.",
      punten: "Je krijgt alleen punten als je deze vraag volledig juist beantwoordt.",
    };
  }
  if (type === "keuzelijst") {
    return {
      zin: "Kies het enige juiste antwoord in elke keuzelijst.",
      punten: "Je krijgt alleen punten als je deze vraag volledig juist beantwoordt.",
    };
  }
  return null;
}

// ---------------------------------------------------------------------------
// Inlezen, voor de import en voor het formulier in Beheer

/**
 * Maakt van wat er in een importbestand of een formulier staat het antwoord
 * zoals het bewaard wordt. Gooit een fout met een zin die Kim begrijpt als er
 * iets niet klopt; zo komt er nooit een halve vraag in de databank.
 *
 * Een tabel mag haar antwoord geven als
 *   - true en false per rij (true is de eerste kolom, standaard Juist),
 *   - het nummer van de juiste kolom per rij, vanaf 0,
 *   - of de naam van de kolom per rij ("juist", "fout", "ja").
 */
export function maakTabelAntwoord(rijen: string[], kolommenIn: unknown, antwoord: unknown) {
  const kolommen = Array.isArray(kolommenIn) && kolommenIn.length
    ? kolommenIn.map((k) => String(k).trim()).filter(Boolean)
    : STANDAARD_KOLOMMEN;
  if (kolommen.length < 2) throw new Error("Een tabel heeft minstens twee kolommen nodig.");
  if (!rijen.length) throw new Error("Een tabel heeft minstens één uitspraak nodig.");
  const lijst = Array.isArray(antwoord) ? antwoord : [];
  if (lijst.length !== rijen.length) {
    throw new Error(`De tabel heeft ${rijen.length} rijen maar ${lijst.length} antwoorden. Geef per rij één antwoord.`);
  }
  const juist = lijst.map((a, i) => {
    if (typeof a === "boolean") return a ? 0 : 1;
    if (typeof a === "number") return a;
    const tekst = String(a).trim().toLowerCase();
    if (/^\d+$/.test(tekst)) return Number(tekst);
    const k = kolommen.findIndex((naam) => naam.toLowerCase() === tekst);
    if (k < 0) throw new Error(`Rij ${i + 1}: "${a}" is geen kolom van deze tabel (${kolommen.join(", ")}).`);
    return k;
  });
  juist.forEach((k, i) => {
    if (!Number.isInteger(k) || k < 0 || k >= kolommen.length) {
      throw new Error(`Rij ${i + 1}: kolom ${k} bestaat niet.`);
    }
  });
  return { kolommen, juist };
}

/**
 * De zin en het antwoord van een keuzelijstvraag. Het juiste woord mag met
 * een sterretje in de zin staan ([[*stijgende|dalende]]); dan hoeft er geen
 * antwoord bij. Staat er toch een antwoord, dan mag dat per keuzelijst het
 * nummer van de optie zijn of het woord zelf.
 */
export function maakKeuzelijst(vraagIn: string, antwoord: unknown): { vraag: string; antwoord: number[] } {
  const { vraag, juist: uitSterretjes } = leesSterretjes(vraagIn);
  const lijsten = keuzelijsten(vraag);
  if (!lijsten.length) {
    throw new Error("Er staat geen keuzelijst in de zin. Schrijf ze als [[*juist|fout|ook fout]].");
  }
  lijsten.forEach((opties, i) => {
    if (opties.length < 2) throw new Error(`Keuzelijst ${i + 1} heeft maar één optie.`);
  });
  const heeftSterretje = /\[\[[^\]]*\*/.test(vraagIn);
  if (heeftSterretje) {
    if (!uitSterretjes) throw new Error("Zet in elke keuzelijst precies één sterretje, voor het juiste woord.");
    return { vraag, antwoord: uitSterretjes };
  }
  const lijst = Array.isArray(antwoord) ? antwoord : [];
  if (lijst.length !== lijsten.length) {
    throw new Error(`De zin heeft ${lijsten.length} keuzelijsten maar ${lijst.length} antwoorden. Zet een sterretje voor het juiste woord.`);
  }
  const juist = lijst.map((a, i) => {
    const opties = lijsten[i];
    if (typeof a === "number") return a;
    const k = opties.findIndex((o) => o.toLowerCase() === String(a).trim().toLowerCase());
    if (k >= 0) return k;
    if (/^\d+$/.test(String(a).trim())) return Number(a);
    throw new Error(`Keuzelijst ${i + 1}: "${a}" staat niet tussen de opties (${opties.join(", ")}).`);
  });
  juist.forEach((k, i) => {
    if (!Number.isInteger(k) || k < 0 || k >= lijsten[i].length) {
      throw new Error(`Keuzelijst ${i + 1}: optie ${k} bestaat niet.`);
    }
  });
  return { vraag, antwoord: juist };
}

/**
 * Eén vraag uit een importbestand klaarmaken om te bewaren. Bij een tabel of
 * een keuzelijst wordt het antwoord omgezet naar hoe het bewaard staat; elk
 * ander type komt ongewijzigd terug. Beide importvelden van Beheer gebruiken
 * dit, zodat een bestand op de twee plaatsen hetzelfde gelezen wordt.
 *
 * Een tabel in een bestand:
 *   {"type": "tabel", "vraag": "...", "rijen": ["...", "..."],
 *    "antwoord": [true, false]}
 * met eventueel "kolommen": ["Ja", "Nee"] en dan "antwoord": ["ja", "nee"].
 * "opties" mag in de plaats van "rijen".
 *
 * Een keuzelijst in een bestand:
 *   {"type": "keuzelijst", "vraag": "Een [[*stijgende|dalende]] rechte."}
 */
export function zetVormKlaar<
  T extends { type: string; vraag: string; opties?: unknown; antwoord?: unknown; rijen?: unknown; kolommen?: unknown },
>(v: T, waar: string): T {
  try {
    if (v.type === "tabel") {
      const bron = Array.isArray(v.rijen) ? v.rijen : v.opties;
      const rijen = Array.isArray(bron) ? bron.map((r) => String(r).trim()).filter(Boolean) : [];
      const antwoord = maakTabelAntwoord(rijen, v.kolommen, v.antwoord);
      const { rijen: _r, kolommen: _k, ...rest } = v;
      void _r;
      void _k;
      return { ...rest, opties: rijen, antwoord } as unknown as T;
    }
    if (v.type === "keuzelijst") {
      const { vraag, antwoord } = maakKeuzelijst(v.vraag, v.antwoord);
      return { ...v, vraag, opties: null, antwoord };
    }
    if (v.type !== "meerkeuze" && v.type !== "invultekst" && v.type !== "waarofniet") {
      if (!(VRAAGTYPES as readonly string[]).includes(v.type)) {
        throw new Error(`"${v.type}" is geen soort vraag die het platform kent.`);
      }
      return zetNieuweVormKlaar(v as unknown as Record<string, unknown>) as unknown as T;
    }
  } catch (e) {
    throw new Error(`${waar}: ${e instanceof Error ? e.message : String(e)}`);
  }
  return v;
}
