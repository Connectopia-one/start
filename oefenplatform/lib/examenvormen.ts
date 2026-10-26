/**
 * De overige vraagvormen van het examen van de Examencommissie.
 *
 * Na de tabel en de keuzelijst (zie lib/vraagvorm.ts) vroeg Kim op 26 oktober
 * 2026 om alle vormen van dat examen te bouwen, "en dan in 1 keer tegoei
 * aanpakken". Het verslag van wat dat examen vraagt, staat in
 * examencommissie/vraagstelling-examencommissie.md in de projectmap.
 *
 * Hoe elke vorm in de databank staat. Aan de kolommen verandert niets, enkel
 * aan het lijstje toegelaten types; een casus krijgt een eigen kolom (zie
 * supabase/examenvormen.sql).
 *
 *   volgorde   opties   de stappen, zoals ze bewaard zijn
 *              antwoord [2, 0, 1]: de nummers van de stappen in de juiste volgorde
 *
 *   koppelen   opties   wat links staat, één per rij
 *              antwoord {"kolommen": [wat rechts staat], "juist": [per rij het nummer rechts]}
 *              Rechts staat er meestal één meer dan links, zoals op het examen.
 *
 *   sorteren   opties   de kaartjes die in een kolom moeten
 *              antwoord {"kolommen": [de kolommen], "juist": [per kaartje het nummer van zijn kolom]}
 *              Een kolom mag leeg blijven.
 *
 *   sleepzin   vraag    de zin, met elk leeg vak als [[_]]
 *              opties   de woorden om te slepen, ook de woorden die nergens horen
 *              antwoord [per leeg vak het nummer van het woord]
 *
 *   hotspot    antwoord {"zones": [[x, y, breedte, hoogte], ...]} in procent van de prent
 *              De prent is de afbeelding van de vraag. Een klik in één zone is juist.
 *
 *   open       antwoord het voorbeeldantwoord, als tekst
 *              opties   eventueel de regels die al in het tekstvak staan ("Stap 1:")
 *
 *   tekenen    antwoord het voorbeeldantwoord, als tekst
 *              De afbeelding van de vraag, als die er is, ligt onder het tekenvak.
 *
 * Open en tekenen kan een computer niet nakijken; op het examen doet een mens
 * dat. Hier ziet het kind na het antwoorden een voorbeeldantwoord en zegt het
 * zelf of het juist was. Dat oordeel is wat telt.
 *
 * Wat een kind antwoordt: bij volgorde de nummers in de volgorde die het
 * koos; bij koppelen, sorteren en sleepzin per plaats een nummer (-1 is: nog
 * niets); bij hotspot [x, y] in procent; bij open de tekst; bij tekenen het
 * woord "getekend" (de tekening zelf bewaren we niet).
 */

import { leesTabel, lijstVolgorde, type Tabel } from "@/lib/vraagvorm";

export const NIEUWE_VORMEN = ["volgorde", "koppelen", "sorteren", "sleepzin", "hotspot", "open", "tekenen"] as const;

/** De vormen die het kind zelf nakijkt met een voorbeeldantwoord. */
export function zelfNakijken(type: string): boolean {
  return type === "open" || type === "tekenen";
}

// ---------------------------------------------------------------------------
// Volgorde

export function volgordeJuist(opties: unknown, antwoord: unknown): number[] {
  const n = Array.isArray(opties) ? opties.length : 0;
  if (Array.isArray(antwoord) && antwoord.length === n) return antwoord.map(Number);
  return Array.from({ length: n }, (_, i) => i);
}

/**
 * De volgorde waarin het kind de stappen eerst ziet. Geschud, maar nooit al
 * juist: anders klikt een kind dat niets verschuift op Controleer en heeft het
 * punten voor niets.
 */
export function beginVolgorde(vraagId: string, juist: number[]): number[] {
  const n = juist.length;
  const geschud = lijstVolgorde(vraagId, 0, n).map((i) => juist[i]);
  if (n > 1 && geschud.every((k, i) => k === juist[i])) {
    return [...geschud.slice(1), geschud[0]];
  }
  return geschud;
}

// ---------------------------------------------------------------------------
// Koppelen en sorteren: dezelfde vorm als de tabel, dus ook dezelfde lezer.

export type Koppeling = Tabel;
export function leesKoppeling(opties: unknown, antwoord: unknown): Koppeling | null {
  return leesTabel(opties, antwoord);
}

// ---------------------------------------------------------------------------
// Een zin met lege vakken om woorden in te slepen

const VAK = /\[\[([^\]]*?)\]\]/g;

export type SleepStuk = { soort: "tekst"; tekst: string } | { soort: "vak"; nummer: number };

export function leesSleepzin(vraag: string): SleepStuk[] {
  const stukken: SleepStuk[] = [];
  let vorige = 0;
  let nummer = 0;
  for (const m of vraag.matchAll(VAK)) {
    if (m.index > vorige) stukken.push({ soort: "tekst", tekst: vraag.slice(vorige, m.index) });
    vorige = m.index + m[0].length;
    stukken.push({ soort: "vak", nummer: nummer++ });
  }
  if (vorige < vraag.length) stukken.push({ soort: "tekst", tekst: vraag.slice(vorige) });
  return stukken;
}

export function aantalVakken(vraag: string): number {
  return [...vraag.matchAll(VAK)].length;
}

/** De zin met in elk vak het woord dat het kind (of het antwoord) erin zette. */
export function sleepzinAlsTekst(vraag: string, woorden: string[] | null, lijst?: number[]): string {
  return leesSleepzin(vraag)
    .map((s) => {
      if (s.soort === "tekst") return s.tekst;
      const k = lijst?.[s.nummer];
      return k !== undefined && k >= 0 && woorden?.[k] ? woorden[k] : "____";
    })
    .join("");
}

// ---------------------------------------------------------------------------
// Klikken op de prent

export type Zone = [number, number, number, number];

export function leesZones(antwoord: unknown): Zone[] {
  const ruw = (antwoord as { zones?: unknown })?.zones;
  if (!Array.isArray(ruw)) return [];
  return ruw
    .map((z) => (Array.isArray(z) ? z.map(Number) : []))
    .filter((z): z is Zone => z.length === 4 && z.every((n) => Number.isFinite(n)));
}

export function inZone(punt: unknown, zones: Zone[]): boolean {
  if (!Array.isArray(punt) || punt.length !== 2) return false;
  const [x, y] = punt.map(Number);
  return zones.some(([zx, zy, b, h]) => x >= zx && x <= zx + b && y >= zy && y <= zy + h);
}

// ---------------------------------------------------------------------------
// Nakijken

/** Juist of fout bij de vormen die een computer kan nakijken. */
export function isJuistNieuw(
  vraag: { type: string; vraag: string; opties: unknown; antwoord: unknown },
  gegeven: unknown,
): boolean | null {
  const lijst = Array.isArray(gegeven) ? gegeven.map(Number) : null;
  const gelijk = (juist: number[]) =>
    Boolean(lijst) && lijst!.length === juist.length && juist.length > 0 && juist.every((k, i) => lijst![i] === k);
  switch (vraag.type) {
    case "volgorde":
      return gelijk(volgordeJuist(vraag.opties, vraag.antwoord));
    case "koppelen":
    case "sorteren": {
      const t = leesKoppeling(vraag.opties, vraag.antwoord);
      return Boolean(t) && gelijk(t!.juist);
    }
    case "sleepzin":
      return gelijk(Array.isArray(vraag.antwoord) ? vraag.antwoord.map(Number) : []);
    case "hotspot":
      return inZone(gegeven, leesZones(vraag.antwoord));
    default:
      return null;
  }
}

/** Is er bij deze vorm al iets aangeduid? null: geen nieuwe vorm. */
export function isIngevuldNieuw(type: string, gegeven: unknown): boolean | null {
  if (!(NIEUWE_VORMEN as readonly string[]).includes(type)) return null;
  if (gegeven === null || gegeven === undefined) return false;
  if (type === "open" || type === "tekenen") return String(gegeven).trim() !== "";
  if (type === "volgorde" || type === "hotspot") return Array.isArray(gegeven);
  return Array.isArray(gegeven) && gegeven.some((n) => Number(n) >= 0);
}

// ---------------------------------------------------------------------------
// Uitschrijven, voor het rapport van de ouder, de begeleiding en de pdf

export function schrijfNieuw(
  vraag: { type: string; vraag: string; opties: string[] | null; antwoord: unknown },
  waarde: unknown,
): string | null {
  // Het juiste antwoord komt soms binnen zoals het bewaard staat.
  const binnen = waarde as { juist?: unknown } | null;
  const lijst = Array.isArray(waarde)
    ? waarde.map(Number)
    : Array.isArray(binnen?.juist)
      ? binnen.juist.map(Number)
      : [];
  const opties = vraag.opties ?? [];
  switch (vraag.type) {
    case "volgorde":
      return lijst.map((k) => opties[k] ?? "?").join(" → ");
    case "koppelen":
    case "sorteren": {
      const t = leesKoppeling(vraag.opties, vraag.antwoord);
      if (!t) return "—";
      return t.rijen.map((rij, i) => `${rij}: ${t.kolommen[lijst[i]] ?? "niets"}`).join(" · ");
    }
    case "sleepzin":
      return sleepzinAlsTekst(vraag.vraag, vraag.opties, lijst);
    case "hotspot": {
      if ((waarde as { zones?: unknown })?.zones) return "een plaats op de prent";
      return inZone(waarde, leesZones(vraag.antwoord)) ? "op de juiste plaats geklikt" : "naast de juiste plaats geklikt";
    }
    case "open":
    case "tekenen":
      return String(waarde ?? "—");
    default:
      return null;
  }
}

/** Hoe de vraagtekst op papier of in een lijst staat. */
export function vraagAlsTekst(vraag: { type: string; vraag: string }): string {
  if (vraag.type === "sleepzin") return sleepzinAlsTekst(vraag.vraag, null);
  return vraag.vraag;
}

// ---------------------------------------------------------------------------
// De vaste zin boven de vraag, zoals op het examen

const ALLES_OF_NIETS = "Je krijgt alleen punten als je deze vraag volledig juist beantwoordt.";

export function instructieNieuw(
  type: string,
  vraag: { opties: unknown; antwoord: unknown },
): { zin: string; punten: string | null } | null {
  switch (type) {
    case "volgorde":
      return { zin: "Zet de onderdelen in de juiste volgorde.", punten: ALLES_OF_NIETS };
    case "koppelen": {
      const t = leesKoppeling(vraag.opties, vraag.antwoord);
      const teVeel = t ? t.kolommen.length - t.rijen.length : 0;
      return {
        zin:
          "Koppel elk onderdeel aan het juiste antwoord." +
          (teVeel === 1 ? " Er is één antwoord te veel." : teVeel > 1 ? ` Er zijn ${teVeel} antwoorden te veel.` : ""),
        punten: ALLES_OF_NIETS,
      };
    }
    case "sorteren":
      return { zin: "Sleep elk onderdeel in de juiste kolom. Een kolom mag leeg blijven.", punten: ALLES_OF_NIETS };
    case "sleepzin":
      return { zin: "Sleep het juiste woord in elk leeg vak. Niet alle woorden moeten gebruikt worden.", punten: ALLES_OF_NIETS };
    case "hotspot":
      return { zin: "Klik op de afbeelding.", punten: null };
    case "open":
      return { zin: "Typ je antwoord in het tekstvak.", punten: "Daarna zie je een voorbeeldantwoord en kijk je jezelf na." };
    case "tekenen":
      return { zin: "Teken je antwoord in het vak.", punten: "Daarna zie je een voorbeeldantwoord en kijk je jezelf na." };
    default:
      return null;
  }
}

// ---------------------------------------------------------------------------
// Inlezen, voor de import en voor het formulier in Beheer

function tekst(x: unknown) {
  return String(x ?? "").trim();
}

/**
 * Eén vraag van een nieuwe vorm klaarmaken om te bewaren. Wat er in een
 * importbestand mag staan:
 *
 *   volgorde  "opties": de stappen in de juiste volgorde
 *   koppelen  "paren": [["links", "rechts"], ...], "extra": ["te veel"]
 *   sorteren  "kolommen": ["A", "B"], "items": [["kaartje", "A"], ...]
 *   sleepzin  "vraag": "De hoofdstad is [[Brussel]].", "extra": ["Antwerpen"]
 *   hotspot   "zones": [[x, y, breedte, hoogte]], en "afbeelding_url"
 *   open      "antwoord": het voorbeeldantwoord, eventueel "opties": ["Stap 1:"]
 *   tekenen   "antwoord": het voorbeeldantwoord
 *
 * Gooit een fout met een zin die Kim begrijpt; zo komt er nooit een halve
 * vraag in de databank.
 */
export function zetNieuweVormKlaar(v: Record<string, unknown>): Record<string, unknown> {
  const { paren, extra, items, zones, kolommen, ...rest } = v;
  switch (v.type) {
    case "volgorde": {
      const opties = Array.isArray(v.opties) ? v.opties.map(tekst).filter(Boolean) : [];
      if (opties.length < 2) throw new Error("Een volgordevraag heeft minstens twee stappen nodig.");
      const antwoord = Array.isArray(v.antwoord) && v.antwoord.length === opties.length
        ? v.antwoord.map(Number)
        : opties.map((_, i) => i);
      const gesorteerd = [...antwoord].sort((a, b) => a - b);
      if (!gesorteerd.every((k, i) => k === i)) throw new Error("Het antwoord van een volgordevraag noemt elke stap precies één keer.");
      return { ...rest, opties, antwoord };
    }
    case "koppelen": {
      if (Array.isArray(paren)) {
        const lijst = paren.map((p) => (Array.isArray(p) ? p.map(tekst) : []));
        if (lijst.some((p) => p.length !== 2 || !p[0] || !p[1])) {
          throw new Error('Elk paar staat als ["links", "rechts"].');
        }
        const rechts: string[] = [];
        for (const [, r] of lijst) if (!rechts.includes(r)) rechts.push(r);
        for (const e of Array.isArray(extra) ? extra.map(tekst).filter(Boolean) : []) {
          if (!rechts.includes(e)) rechts.push(e);
        }
        return {
          ...rest,
          opties: lijst.map(([l]) => l),
          antwoord: { kolommen: rechts, juist: lijst.map(([, r]) => rechts.indexOf(r)) },
        };
      }
      return { ...rest, ...controleerKoppeling(v.opties, v.antwoord, "koppelvraag") };
    }
    case "sorteren": {
      if (Array.isArray(items)) {
        const lijst = items.map((p) => (Array.isArray(p) ? p.map(tekst) : []));
        if (lijst.some((p) => p.length !== 2 || !p[0] || !p[1])) {
          throw new Error('Elk kaartje staat als ["kaartje", "kolom"].');
        }
        const kols = Array.isArray(kolommen) ? kolommen.map(tekst).filter(Boolean) : [];
        for (const [, k] of lijst) if (!kols.includes(k)) kols.push(k);
        if (kols.length < 2) throw new Error("Een sorteervraag heeft minstens twee kolommen nodig.");
        return {
          ...rest,
          opties: lijst.map(([i]) => i),
          antwoord: { kolommen: kols, juist: lijst.map(([, k]) => kols.indexOf(k)) },
        };
      }
      return { ...rest, ...controleerKoppeling(v.opties, v.antwoord, "sorteervraag") };
    }
    case "sleepzin":
      return { ...rest, ...maakSleepzin(tekst(v.vraag), Array.isArray(extra) ? extra.map(tekst) : Array.isArray(v.opties) && !Array.isArray(v.antwoord) ? v.opties.map(tekst) : [], v) };
    case "hotspot": {
      const z = Array.isArray(zones) ? { zones } : v.antwoord;
      const lijst = leesZones(z);
      if (!lijst.length) throw new Error("Een klikvraag heeft minstens één zone nodig: [x, y, breedte, hoogte] in procent.");
      if (lijst.some(([x, y, b, h]) => x < 0 || y < 0 || b <= 0 || h <= 0 || x + b > 100.5 || y + h > 100.5)) {
        throw new Error("Een zone ligt (deels) buiten de prent. Alles staat in procent, van 0 tot 100.");
      }
      return { ...rest, opties: null, antwoord: { zones: lijst } };
    }
    case "open":
    case "tekenen": {
      const antwoord = tekst(v.antwoord);
      if (!antwoord) throw new Error("Geef een voorbeeldantwoord, zodat het kind zichzelf kan nakijken.");
      const opties = v.type === "open" && Array.isArray(v.opties) ? v.opties.map(tekst).filter(Boolean) : null;
      return { ...rest, opties: opties?.length ? opties : null, antwoord };
    }
    default:
      return v;
  }
}

/** Een koppel- of sorteervraag die al in de bewaarde vorm staat. */
function controleerKoppeling(opties: unknown, antwoord: unknown, naam: string) {
  const t = leesKoppeling(opties, antwoord);
  if (!t) throw new Error(`Deze ${naam} klopt niet: geef per rij één antwoord dat bestaat.`);
  return { opties: t.rijen, antwoord: { kolommen: t.kolommen, juist: t.juist } };
}

/**
 * Een zin met de juiste woorden tussen dubbele haken: "De hoofdstad is
 * [[Brussel]]." Wordt bewaard met lege vakken [[_]] en de woorden apart.
 * Een zin die al lege vakken heeft, komt met zijn woorden en antwoord binnen.
 */
function maakSleepzin(vraagIn: string, extraIn: string[], v: Record<string, unknown>) {
  const vakken = [...vraagIn.matchAll(VAK)].map((m) => m[1].trim());
  if (!vakken.length) throw new Error("Er staat geen leeg vak in de zin. Zet het juiste woord tussen dubbele haken: [[Brussel]].");
  if (vakken.every((w) => w === "_" || w === "")) {
    const woorden = Array.isArray(v.opties) ? v.opties.map(tekst) : [];
    const antwoord = Array.isArray(v.antwoord) ? v.antwoord.map(Number) : [];
    if (antwoord.length !== vakken.length || antwoord.some((k) => !(k >= 0 && k < woorden.length))) {
      throw new Error("Geef per leeg vak het nummer van het juiste woord.");
    }
    return { vraag: vraagIn, opties: woorden, antwoord };
  }
  if (vakken.some((w) => !w || w === "_")) throw new Error("Zet in elk leeg vak het juiste woord: [[Brussel]].");
  const woorden: string[] = [];
  for (const w of vakken) if (!woorden.includes(w)) woorden.push(w);
  for (const e of extraIn.filter(Boolean)) if (!woorden.includes(e)) woorden.push(e);
  return {
    vraag: vraagIn.replace(VAK, "[[_]]"),
    opties: woorden,
    antwoord: vakken.map((w) => woorden.indexOf(w)),
  };
}

/** De zin terug met de juiste woorden in de vakken, om aan te passen in Beheer. */
export function sleepzinMetWoorden(vraag: string, woorden: string[] | null, antwoord: unknown): string {
  const lijst = Array.isArray(antwoord) ? antwoord.map(Number) : [];
  let n = 0;
  return vraag.replace(VAK, () => `[[${woorden?.[lijst[n++]] ?? ""}]]`);
}

/** De woorden die in geen enkel vak horen. */
export function sleepzinExtra(woorden: string[] | null, antwoord: unknown): string[] {
  const lijst = Array.isArray(antwoord) ? antwoord.map(Number) : [];
  return (woorden ?? []).filter((_, i) => !lijst.includes(i));
}

// ---------------------------------------------------------------------------
// Het formulier in Beheer

/**
 * Wat er in de velden Vraag, Opties en Antwoord van het formulier staat,
 * omgezet naar wat een importbestand zou geven. Zo leest het formulier precies
 * zoals de import.
 *
 *   volgorde  Opties: de stappen in de juiste volgorde, één per regel.
 *   koppelen  Opties: "links = rechts", één paar per regel; een regel "= iets"
 *             is een antwoord te veel.
 *   sorteren  Opties: "kaartje = kolom", één per regel. Antwoord: eventueel de
 *             kolommen met | ertussen, zo komt ook een lege kolom erbij.
 *   sleepzin  Vraag: de zin met de juiste woorden in [[ ]]. Opties: de woorden
 *             te veel, één per regel.
 *   hotspot   Antwoord: de zones, "x, y, breedte, hoogte", met ; ertussen.
 *   open      Antwoord: het voorbeeldantwoord. Opties: de regels die al in het
 *             tekstvak staan.
 *   tekenen   Antwoord: het voorbeeldantwoord.
 */
export function vanFormulier(type: string, vraag: string, optiesRaw: string, antwoordRaw: string) {
  const regels = optiesRaw.split("\n").map((r) => r.trim()).filter(Boolean);
  const paar = (r: string) => {
    const i = r.indexOf("=");
    return i < 0 ? [r, ""] : [r.slice(0, i).trim(), r.slice(i + 1).trim()];
  };
  switch (type) {
    case "volgorde":
      return zetNieuweVormKlaar({ type, vraag, opties: regels });
    case "koppelen": {
      const lijst = regels.map(paar);
      if (lijst.some(([l, r]) => l && !r)) throw new Error('Schrijf elk paar als "links = rechts".');
      return zetNieuweVormKlaar({
        type,
        vraag,
        paren: lijst.filter(([l]) => l),
        extra: lijst.filter(([l]) => !l).map(([, r]) => r),
      });
    }
    case "sorteren": {
      const lijst = regels.map(paar);
      if (lijst.some(([i, k]) => !i || !k)) throw new Error('Schrijf elk kaartje als "kaartje = kolom".');
      return zetNieuweVormKlaar({
        type,
        vraag,
        items: lijst,
        kolommen: antwoordRaw ? antwoordRaw.split("|").map((k) => k.trim()) : [],
      });
    }
    case "sleepzin":
      return zetNieuweVormKlaar({ type, vraag, extra: regels });
    case "hotspot":
      return zetNieuweVormKlaar({
        type,
        vraag,
        zones: antwoordRaw.split(";").map((z) => z.split(",").map((n) => Number(n.trim().replace(",", ".")))).filter((z) => z.length === 4),
      });
    case "open":
    case "tekenen":
      return zetNieuweVormKlaar({ type, vraag, opties: regels, antwoord: antwoordRaw });
    default:
      return null;
  }
}

/** De weg terug: wat er in de drie velden staat als je een vraag aanpast. */
export function naarFormulier(v: { type: string; vraag: string; opties: string[] | null; antwoord: unknown }) {
  const t = v.type === "koppelen" || v.type === "sorteren" ? leesKoppeling(v.opties, v.antwoord) : null;
  switch (v.type) {
    case "volgorde": {
      const juist = volgordeJuist(v.opties, v.antwoord);
      return { vraag: v.vraag, opties: juist.map((k) => v.opties?.[k] ?? "").join("\n"), antwoord: "" };
    }
    case "koppelen": {
      if (!t) break;
      const gebruikt = new Set(t.juist);
      const extra = t.kolommen.filter((_, i) => !gebruikt.has(i)).map((r) => `= ${r}`);
      return { vraag: v.vraag, opties: [...t.rijen.map((l, i) => `${l} = ${t.kolommen[t.juist[i]]}`), ...extra].join("\n"), antwoord: "" };
    }
    case "sorteren":
      if (!t) break;
      return { vraag: v.vraag, opties: t.rijen.map((l, i) => `${l} = ${t.kolommen[t.juist[i]]}`).join("\n"), antwoord: t.kolommen.join(" | ") };
    case "sleepzin":
      return { vraag: sleepzinMetWoorden(v.vraag, v.opties, v.antwoord), opties: sleepzinExtra(v.opties, v.antwoord).join("\n"), antwoord: "" };
    case "hotspot":
      return { vraag: v.vraag, opties: "", antwoord: leesZones(v.antwoord).map((z) => z.map((n) => Math.round(n * 10) / 10).join(", ")).join("; ") };
    case "open":
    case "tekenen":
      return { vraag: v.vraag, opties: (v.opties ?? []).join("\n"), antwoord: String(v.antwoord ?? "") };
  }
  return null;
}

/** Schudt de volgorde van de woorden of de antwoorden rechts, vast per vraag. */
export function geschud(vraagId: string, nummer: number, aantal: number): number[] {
  return lijstVolgorde(vraagId, nummer, aantal);
}

// ---------------------------------------------------------------------------
// Een casus in een importbestand

/**
 * Een casus in een bestand: één situatie met de vragen die erbij horen.
 *
 *   {"casus": "Lien koopt ...", "vragen": [ {...}, {...} ]}
 *
 * Elke vraag krijgt de casus zelf mee, zodat ze ook op het examen, tussen
 * vragen van andere hoofdstukken, op zichzelf te beantwoorden is. Gewone
 * vragen komen ongewijzigd terug.
 */
export function pakCasussenUit(lijst: unknown[]): unknown[] {
  return lijst.flatMap((v) => {
    const groep = v as { casus?: unknown; vragen?: unknown; type?: unknown };
    if (!groep.type && typeof groep.casus === "string" && Array.isArray(groep.vragen)) {
      return groep.vragen.map((w) => ({ casus: groep.casus, ...(w as object) }));
    }
    return [v];
  });
}
