/*
  Knop "Begrippenarena" op elke vakpagina — /niveaus/<niveau>/<vak>

  Kim, 12 november 2026: bij elk vak een knop naar de begrippenarena die
  erbij hoort. De knop opent het spel meteen op het juiste niveau.

  Per vak: welk spel (de slug uit `spellen` in inhoud/extras.ts) en welk
  niveau binnen dat spel (dezelfde naam als `niveauInSpel` bij de kaarten
  in extras.ts). Staat een vak hier niet in, dan komt er geen knop.

  De sleutel is "<niveau>/<vak>", zoals in het webadres.
*/

export const arenaKnopTekst = "Oefen de begrippen in de begrippenarena";
export const woordenKnopTekst = "Oefen de woorden in de woordenarena";

type Arena = { spel: string; niveau?: string };

const a = (spel: string, niveau?: string): Arena => ({ spel, niveau });

const NAT = "begrippenarena-natuur";
const WIS = "begrippenarena-wiskunde";
const AK = "begrippenarena-aardrijkskunde";
const NL = "begrippenarena-nederlands";
const GES = "begrippenarena";
const ECO = "begrippenarena-economie";
const MENS = "begrippenarena-mens";
const TECH = "begrippenarena-techniek";
const EN = "woordenarena-engels";
const FR = "woordenarena-frans";
const HOEK = "begrippenarena-uitdagingshoek";

export const arenaPerVak: Record<string, Arena> = {
  /* 🧱 Basis */
  "basis/frans": a(FR, "lager"),
  "basis/nederlands": a(NL, "lager"),
  "basis/wiskunde": a(WIS, "lager"),

  /* 🌱 Start */
  "start/aardrijkskunde": a(AK, "start"),
  "start/engels": a(EN, "start"),
  "start/frans": a(FR, "lager"),
  "start/geschiedenis": a(GES, "start"),
  "start/nederlands": a(NL, "lager"),
  "start/wetenschap-en-techniek": a(TECH, "lager"),
  "start/wiskunde": a(WIS, "lager"),

  /* ✨ Spark */
  "spark/aardrijkskunde": a(AK, "spark"),
  "spark/engels": a(EN, "spark"),
  "spark/frans": a(FR, "spark"),
  "spark/geschiedenis": a(GES, "spark"),
  "spark/natuurwetenschappen": a(NAT, "spark"),
  "spark/nederlands": a(NL, "spark"),
  "spark/samenleving-en-economie": a(MENS, "se_spark"),
  "spark/techniek": a(TECH, "spark"),
  "spark/wiskunde": a(WIS, "spark"),

  /* 🚀 Boost doorstroom */
  "boost-doorstroom/aardrijkskunde": a(AK, "boost"),
  "boost-doorstroom/biologie": a(NAT, "boost"),
  "boost-doorstroom/chemie": a(NAT, "boost"),
  "boost-doorstroom/economie": a(ECO, "boost"),
  "boost-doorstroom/engels": a(EN, "boost"),
  "boost-doorstroom/frans": a(FR, "boost"),
  "boost-doorstroom/fysica": a(NAT, "boost"),
  "boost-doorstroom/geschiedenis": a(GES, "boost"),
  "boost-doorstroom/kunstbeschouwing-en-filosofie": a(MENS, "kf_boost"),
  "boost-doorstroom/natuurwetenschappen": a(NAT, "boost"),
  "boost-doorstroom/nederlands": a(NL, "boost"),
  "boost-doorstroom/sociale-en-gedragswetenschappen": a(MENS, "sgw_boost"),
  "boost-doorstroom/wiskunde": a(WIS, "boost"),
  "boost-doorstroom/wiskunde-basis": a(WIS, "boost"),

  /* 🚀 Boost dubbele finaliteit */
  "boost-dubbele-finaliteit/aardrijkskunde": a(AK, "boost"),
  "boost-dubbele-finaliteit/economie-en-bedrijfswetenschappen": a(ECO, "boost"),
  "boost-dubbele-finaliteit/engels": a(EN, "boost"),
  "boost-dubbele-finaliteit/frans": a(FR, "boost"),
  "boost-dubbele-finaliteit/geschiedenis": a(GES, "boost"),
  "boost-dubbele-finaliteit/gezondheid-zorg-en-welzijn": a(MENS, "gzw"),
  "boost-dubbele-finaliteit/natuurwetenschappen": a(NAT, "boost"),
  "boost-dubbele-finaliteit/nederlands": a(NL, "boost"),
  "boost-dubbele-finaliteit/ontwikkeling-en-pedagogisch-handelen": a(MENS, "oph"),
  "boost-dubbele-finaliteit/toegepaste-economie": a(ECO, "toegepast"),
  "boost-dubbele-finaliteit/wiskunde": a(WIS, "boost"),

  /* 🌍 Beyond doorstroom */
  "beyond-doorstroom/aardrijkskunde": a(AK, "beyond"),
  "beyond-doorstroom/bedrijfswetenschappen-en-recht": a(ECO, "bedrijf"),
  "beyond-doorstroom/biologie": a(NAT, "beyond"),
  "beyond-doorstroom/chemie": a(NAT, "beyond"),
  "beyond-doorstroom/economie": a(ECO, "beyond"),
  "beyond-doorstroom/engels": a(EN, "beyond"),
  "beyond-doorstroom/filosofie-en-recht": a(MENS, "filorecht"),
  "beyond-doorstroom/frans": a(FR, "beyond"),
  "beyond-doorstroom/fysica": a(NAT, "beyond"),
  "beyond-doorstroom/geschiedenis": a(GES, "beyond"),
  "beyond-doorstroom/natuurwetenschappen": a(NAT, "beyond"),
  "beyond-doorstroom/nederlands": a(NL, "beyond"),
  "beyond-doorstroom/samenleving-en-economie": a(MENS, "se_beyond"),
  "beyond-doorstroom/sociale-en-gedragswetenschappen": a(MENS, "sgw_beyond"),
  "beyond-doorstroom/statistiek": a(WIS, "statistiek"),
  "beyond-doorstroom/wiskunde": a(WIS, "beyond"),
  "beyond-doorstroom/wiskunde-basis": a(WIS, "basis"),

  /* 🌍 Beyond dubbele finaliteit */
  "beyond-dubbele-finaliteit/aardrijkskunde": a(AK, "beyond"),
  "beyond-dubbele-finaliteit/engels": a(EN, "beyond"),
  "beyond-dubbele-finaliteit/frans": a(FR, "beyond"),
  "beyond-dubbele-finaliteit/geschiedenis": a(GES, "beyond"),
  "beyond-dubbele-finaliteit/natuurwetenschappen": a(NAT, "beyond"),
  "beyond-dubbele-finaliteit/nederlands": a(NL, "beyond"),
  "beyond-dubbele-finaliteit/wiskunde": a(WIS, "beyond"),

  /* 🔭 Uitdagingshoek */
  "hoekje/coderen-en-computers": a(HOEK, "code"),
  "hoekje/de-ruimte": a(HOEK, "ruimte"),
  "hoekje/geschiedenis-van-belgie": a(HOEK, "belgie"),
  "hoekje/paradoxen-en-weetjes": a(HOEK, "paradox"),
};

/* Het webadres en het opschrift van de knop, of null als er geen arena is. */
export function arenaKnop(niveau: string, vak: string) {
  const arena = arenaPerVak[`${niveau}/${vak}`];
  if (!arena) return null;
  return {
    href: `/extras/${arena.spel}${arena.niveau ? `?niveau=${arena.niveau}` : ""}`,
    tekst: arena.spel.startsWith("woordenarena") ? woordenKnopTekst : arenaKnopTekst,
    icoon: arena.spel.startsWith("woordenarena") ? "🗣️" : "🎲",
  };
}
