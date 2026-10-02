export type NiveauSlug =
  | "basis"
  | "start"
  | "spark"
  | "boost-doorstroom"
  | "boost-dubbele-finaliteit"
  | "beyond-doorstroom"
  | "beyond-dubbele-finaliteit"
  | "hoekje";

export type Niveau = {
  slug: NiveauSlug;
  emoji: string;
  naam: string;
  omschrijving: string;
  /* Hoort deze categorie onder een knop op de startpagina samen met een
     andere? Zie GROEPEN hieronder. */
  groep?: GroepSlug;
  /* De korte naam die op de knop staat als de categorie onder een groep
     hangt. "Doorstroom" leest beter dan "Boost doorstroom" wanneer je net op
     de knop Boost geduwd hebt. */
  kort?: string;
};

/*
  🧱 Basis is geen leerjaar maar herhaling: de bouwstenen (komma verschuiven,
  maten omzetten, breuken, de namen van de bewerkingen, ggd en kgv) voor een
  kind dat die nog niet vlot beheerst, in welke categorie het ook zit. Daarom
  staat het op de startpagina apart, onder de leerjaarknoppen.

  🔭 De uitdagingshoek is dat andere uiterste: geen leerstof van een leerjaar,
  maar vragen die er net naast liggen (de ruimte, hoe een computer denkt, de
  geschiedenis van ons land, paradoxen). Voor wie klaar is met de gewone
  hoofdstukken en gewoon verder wil denken. Niet te verwarren met het
  hoofdstuk "Uitdaging — alles door elkaar", dat bij elk vak staat en wél
  binnen de leerstof van dat vak blijft.

  🚀 Boost is vanaf de tweede graad geen één categorie meer. De examencommissie
  splitst daar in doorstroomfinaliteit en dubbele finaliteit, met eigen
  vakfiches: doorstroom heeft Nederlands 1 en Nederlands 2 en kiest tussen
  wiskunde gevorderd en wiskunde basis, dubbele finaliteit heeft gewoon
  Nederlands en gewoon wiskunde. Dat zijn andere vakken met andere leerstof, dus
  twee categorieën. Op de startpagina blijft het wel één knop; de keuze tussen
  de twee komt een stap later.

  🌍 Beyond splitst op dezelfde manier, sinds 2 oktober 2026. De examencommissie
  zet de derde graad in vier lijsten, maar die vallen bij ons in twee
  categorieën uiteen. De doorstroomfiches noemen bovenaan zelf zowel de
  domeinoverschrijdende richtingen (economie-wiskunde, humane wetenschappen,
  Latijn, moderne talen, wetenschappen-wiskunde) als de domeingebonden
  (bedrijfswetenschappen, welzijnswetenschappen), dus die horen samen in één
  categorie. De basisvorming van de dubbele finaliteit en commerciële
  organisatie vormen de tweede.
*/
export const NIVEAUS: Niveau[] = [
  {
    slug: "basis",
    emoji: "🧱",
    naam: "Basis",
    omschrijving: "De bouwstenen herhalen, voor elk niveau",
  },
  {
    slug: "start",
    emoji: "🌱",
    naam: "Start",
    omschrijving: "5de & 6de leerjaar",
  },
  {
    slug: "spark",
    emoji: "✨",
    naam: "Spark",
    omschrijving: "1ste & 2de middelbaar",
  },
  {
    slug: "boost-doorstroom",
    emoji: "🚀",
    naam: "Boost doorstroom",
    kort: "Doorstroom",
    omschrijving:
      "Economische wetenschappen, humane wetenschappen, Latijn, moderne talen, natuurwetenschappen",
    groep: "boost",
  },
  {
    slug: "boost-dubbele-finaliteit",
    emoji: "🚀",
    naam: "Boost dubbele finaliteit",
    kort: "Dubbele finaliteit",
    omschrijving: "Bedrijf en organisatie, maatschappij en welzijn",
    groep: "boost",
  },
  {
    slug: "beyond-doorstroom",
    emoji: "🌍",
    naam: "Beyond doorstroom",
    kort: "Doorstroom",
    omschrijving:
      "Economie-wiskunde, humane wetenschappen, Latijn, moderne talen, wetenschappen-wiskunde, bedrijfs- en welzijnswetenschappen",
    groep: "beyond",
  },
  {
    slug: "beyond-dubbele-finaliteit",
    emoji: "🌍",
    naam: "Beyond dubbele finaliteit",
    kort: "Dubbele finaliteit",
    omschrijving: "Basisvorming en commerciële organisatie",
    groep: "beyond",
  },
  {
    slug: "hoekje",
    emoji: "🔭",
    naam: "Uitdagingshoek",
    omschrijving: "Verder dan de leerstof, voor wie graag ver doordenkt",
  },
];

export type GroepSlug = "boost" | "beyond";

export type Groep = {
  slug: GroepSlug;
  emoji: string;
  naam: string;
  omschrijving: string;
};

/*
  Een groep is géén categorie: er hangt geen enkel hoofdstuk aan. Het is enkel
  de knop op de startpagina die naar de twee categorieën eronder leidt.
*/
export const GROEPEN: Groep[] = [
  {
    slug: "boost",
    emoji: "🚀",
    naam: "Boost",
    omschrijving: "3de & 4de middelbaar",
  },
  {
    slug: "beyond",
    emoji: "🌍",
    naam: "Beyond",
    omschrijving: "5de & 6de middelbaar",
  },
];

export function vindNiveau(slug: string): Niveau | undefined {
  return NIVEAUS.find((n) => n.slug === slug);
}

export function vindGroep(slug: string): Groep | undefined {
  return GROEPEN.find((g) => g.slug === slug);
}

/** De categorieën die onder deze groep hangen, in de volgorde van NIVEAUS. */
export function niveausVanGroep(groep: string): Niveau[] {
  return NIVEAUS.filter((n) => n.groep === groep);
}

/**
 * Krijgt het eerste hoofdstuk van deze categorie bij een import vanzelf
 * "gratis" mee, als proefhoofdstuk?
 *
 * Ja voor de leerjaren en voor 🧱 Basis: daar moet een ouder iets kunnen
 * uitproberen vóór hij betaalt. Niet voor 🔭 de uitdagingshoek: dat is geen
 * leerweg maar een extraatje bij een account.
 */
export function heeftProefhoofdstuk(slug: string): boolean {
  return slug !== "hoekje";
}

/**
 * De knoppen op de startpagina, zonder 🧱 Basis en 🔭 de hoek: die staan daar
 * apart onder. Een groep telt als één knop, en de categorieën eronder komen
 * dus niet apart in de lijst.
 */
export type Startknop = {
  slug: string;
  emoji: string;
  naam: string;
  omschrijving: string;
  /* De categorieën achter deze knop. Bij een gewone categorie is dat ze zelf;
     bij een groep zijn dat de categorieën eronder. Daarmee weet de startpagina
     of er al inhoud achter de knop staat. */
  categorieen: NiveauSlug[];
};

export const STARTKNOPPEN: Startknop[] = NIVEAUS.reduce<Startknop[]>(
  (knoppen, n) => {
    if (n.slug === "basis" || n.slug === "hoekje") return knoppen;
    if (!n.groep) {
      knoppen.push({
        slug: n.slug,
        emoji: n.emoji,
        naam: n.naam,
        omschrijving: n.omschrijving,
        categorieen: [n.slug],
      });
      return knoppen;
    }
    const bestaat = knoppen.find((k) => k.slug === n.groep);
    if (bestaat) {
      bestaat.categorieen.push(n.slug);
      return knoppen;
    }
    const groep = vindGroep(n.groep);
    if (groep) {
      knoppen.push({
        slug: groep.slug,
        emoji: groep.emoji,
        naam: groep.naam,
        omschrijving: groep.omschrijving,
        categorieen: [n.slug],
      });
    }
    return knoppen;
  },
  [],
);
