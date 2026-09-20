/*
  Algemene gegevens van de site.
  Alles wat je hier aanpast, verandert overal mee: in het menu, in de voettekst
  en in de blokken op de startpagina.
*/

export const site = {
  naam: "connectopia.one",
  vzw: "vzw",
  baseline: "Ruimte voor nieuwsgierigheid, talent en uitdaging",
  omschrijving:
    "Connectopia vzw verbindt kinderen aan peers en ouders aan de juiste experts. Plusklas, pluswerkingen, Young Engineers en kampen voor nieuwsgierige kinderen.",
  afsluiter: "Samen bouwen we aan een toekomst vol mogelijkheden",
  socials: "@connectopia.one",
  /* Het mailadres uit al onze communicatie, van de MATM groep. */
  email: "info@matmgroep.com",
};

/*
  De acht onderdelen van de site.
  De volgorde hier is de volgorde op de startpagina.

  groep:  "watwedoen"  = het blok "Wat we doen"
          "uitgelicht" = het grote uitgelichte blok eronder
          "platform"   = het blok "Direct naar jouw plek"
          "kennis"     = het blok "Lezen en bijleren"
  kleur:  "green" | "orange" | "purple" | "blue"
  extern: zet een volledige https-link als het onderdeel op een andere site staat
  inMenu: false als je het onderdeel niet bovenaan in het menu wil
*/

export type Kleur = "green" | "orange" | "purple" | "blue";

export type Onderdeel = {
  slug: string;
  titel: string;
  menuTitel: string;
  icoon: string;
  omschrijving: string;
  groep: "watwedoen" | "uitgelicht" | "platform" | "kennis";
  kleur: Kleur;
  label?: string;
  extern?: string;
  inMenu?: boolean;
};

export const onderdelen: Onderdeel[] = [
  {
    slug: "/over-ons",
    titel: "Wie is Connectopia",
    menuTitel: "Over ons",
    icoon: "🌱",
    omschrijving:
      "Ons verhaal, onze kernwaarden en het team achter de werking. Ervaringsdeskundigen met een netwerk van wél-specialisten.",
    groep: "watwedoen",
    kleur: "green",
  },
  {
    slug: "/aanbod",
    titel: "Ons aanbod",
    menuTitel: "Aanbod",
    icoon: "🎒",
    omschrijving:
      "Alles wat we zelf organiseren, met data, locaties, leeftijden en inschrijving op één pagina.",
    groep: "watwedoen",
    kleur: "orange",
    label: "Gratis proefles",
  },
  {
    slug: "/wegwijzer",
    titel: "Wegwijzer voor ouders",
    menuTitel: "Wegwijzer",
    icoon: "🗺️",
    omschrijving:
      "Een echte roadmap bij ASS, ADHD, HB en UHB. Van het eerste vermoeden tot ver na de diagnose.",
    groep: "uitgelicht",
    kleur: "blue",
  },
  {
    slug: "/waar-kan-je-terecht",
    titel: "Waar kan je terecht",
    menuTitel: "Waar kan je terecht",
    icoon: "🧭",
    omschrijving:
      "Diensten en organisaties die we kennen en vertrouwen: van psycholoog en logopedist tot bijlesleerkracht met kennis van hoogbegaafdheid, ook bij dubbele diagnoses.",
    groep: "watwedoen",
    kleur: "purple",
  },
  {
    slug: "/ouderportaal",
    titel: "Ouderportaal",
    menuTitel: "Ouderportaal",
    icoon: "🏠",
    omschrijving:
      "Je gezin, de kalender, het materiaal en de foto's van de klasjes waar je kind bij zit.",
    groep: "platform",
    kleur: "green",
    label: "Inloggen",
    inMenu: false,
    extern: "https://ouders.connectopia.one",
  },
  {
    slug: "/oefenplatform",
    titel: "Oefenplatform",
    menuTitel: "Oefenplatform",
    icoon: "✏️",
    omschrijving:
      "Interactieve oefeningen per categorie, met voortgang per kind. Je kiest wat past bij wat je kind al kan.",
    groep: "platform",
    kleur: "orange",
    label: "Inloggen",
    inMenu: false,
    extern: "https://oefenplatform.connectopia.one",
  },
  {
    slug: "/blog",
    titel: "Blog, tips en meer",
    menuTitel: "Blog",
    icoon: "📰",
    omschrijving:
      "Artikels van ons team en van externe partners, over opvoeden, school, diagnoses en alles wat ouders bezighoudt.",
    groep: "kennis",
    kleur: "green",
  },
  {
    slug: "/prikbord",
    titel: "Prikbord voor ouders",
    menuTitel: "Prikbord",
    icoon: "📌",
    omschrijving:
      "Een vraag stellen, een tip delen, ervaringen uitwisselen. Het online prikbord van de Connectopia-ouders.",
    groep: "platform",
    kleur: "purple",
    label: "Binnenkort",
  },
];

export const menu = onderdelen.filter((o) => o.inMenu !== false);

export function onderdeelPerGroep(groep: Onderdeel["groep"]) {
  return onderdelen.filter((o) => o.groep === groep);
}

/*
  Zet een link uit de teksten om naar het echte adres.
  Verwijst een link naar een onderdeel dat op een ander webadres staat
  (het veld "extern"), dan gebruikt de site dat adres.
*/
export function echteLink(link: string) {
  return onderdelen.find((o) => o.slug === link)?.extern ?? link;
}
