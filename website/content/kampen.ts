/*
  De vakantiekampen waarvoor je online kan inschrijven, op /kampen/inschrijven.

  Kim op 28 oktober 2026: "de inschrijving zoals ze gebeurt via het young
  engineers website is handiger. Kunnen we het ook op die manier bouwen? En het
  wel nog steeds in het beheer laten toekomen van ouderportaal zoals nu?"
  Dus: kaartjes met "Kies dit", één formulier eronder, de prijs rekent mee, en
  elke inschrijving komt in Beheer → Aanvragen terecht. Betalen gebeurt met een
  overschrijving, zoals bij Young Engineers (Kims keuze, 28 oktober 2026).

  EEN KAMP TOEVOEGEN
  Kopieer een blok in de lijst `kampen` en pas het aan. Let op de `naam` van
  elke dag: dat is de naam van de lijst in het ouderportaal (Beheer →
  Lijsten). Gebruik dus altijd dezelfde vorm, "Plaats weekdag dag maand".
  Een kamp waarvan alle dagen voorbij zijn, verdwijnt vanzelf van de pagina.

  VOLZET
  Zet `volzet: true`. Het kaartje blijft staan, maar wie dan inschrijft, komt
  op de wachtlijst en moet nog niets betalen.

  NOG NIET ZEKER
  Zet `bevestigen: true` voor een kamp dat pas doorgaat als er genoeg
  inschrijvingen zijn. Ouders schrijven in, maar betalen pas als jij het kamp
  bevestigt.
*/

export const kampRegels = {
  prijsPerDag: 40,
  /* Korting per dag voor elk volgend kind uit hetzelfde gezin, zoals bij
     Young Engineers. Zet op 0 om ze weg te laten. */
  broerZusKorting: 5,
  uren: "Elke dag van 9u tot 15u",
  leeftijd: "6 tot 15 jaar",
  rekening: "BE61 0689 6047 3617",
  rekeninghouder: "Connectopia vzw",
  /* Hetzelfde onderwerp als het oude inschrijfformulier, zodat oude en nieuwe
     inschrijvingen in het ouderportaal samen gefilterd worden. */
  onderwerp: "Inschrijving via de website — Vakantiekampen",
  /* Hoeveel dagen een ouder heeft om te betalen. */
  betaaltermijn: "binnen de 7 dagen",
};

export type KampDag = {
  /* De naam van de lijst in het ouderportaal. */
  naam: string;
  /* Zoals de ouder het leest. */
  label: string;
  /* jjjj-mm-dd, om voorbije dagen weg te laten. */
  datum: string;
};

export type Kamp = {
  id: string;
  titel: string;
  thema: string;
  plaats: "Hasselt" | "Genk";
  adres: string;
  wanneer: string;
  foto: string;
  fotoBeschrijving: string;
  dagen: KampDag[];
  volzet?: boolean;
  bevestigen?: boolean;
  opmerking?: string;
};

export const kampen: Kamp[] = [
  {
    id: "herfst-hasselt",
    titel: "Herfstkamp Hasselt",
    thema: "Young Engineer Held",
    plaats: "Hasselt",
    adres: "Level X 28, Vilderstraat 28, Hasselt",
    wanneer: "Maandag 2 en dinsdag 3 november 2026",
    foto: "young-engineers.jpg",
    fotoBeschrijving: "Kinderen bouwen samen met lego en techniek.",
    dagen: [
      { naam: "Hasselt maandag 2 november", label: "Maandag 2 november", datum: "2026-11-02" },
      { naam: "Hasselt dinsdag 3 november", label: "Dinsdag 3 november", datum: "2026-11-03" },
    ],
  },
  {
    id: "herfst-genk",
    titel: "Herfstkamp Genk",
    thema: "Creatieve duizendpoot: van techniek tot design",
    plaats: "Genk",
    adres: "T2 Campus, Thor Park 8040, Genk",
    wanneer: "Woensdag 4 en donderdag 5 november 2026",
    foto: "vakantiekampen.jpg",
    fotoBeschrijving:
      "Een kind drukt op een knop bij een proefopstelling met een gele onderzeeër in een waterbak.",
    dagen: [
      { naam: "Genk woensdag 4 november", label: "Woensdag 4 november", datum: "2026-11-04" },
      { naam: "Genk donderdag 5 november", label: "Donderdag 5 november", datum: "2026-11-05" },
    ],
  },
  {
    id: "kerst-hasselt",
    titel: "Kerstkamp Hasselt",
    thema: "Kies zelf je dagen",
    plaats: "Hasselt",
    adres: "Vilderstraat 28, Hasselt",
    wanneer: "21 tot 23 december en 28 tot 30 december 2026",
    foto: "vakantiekampen.jpg",
    fotoBeschrijving:
      "Een kind drukt op een knop bij een proefopstelling met een gele onderzeeër in een waterbak.",
    bevestigen: true,
    opmerking:
      "Dit kamp gaat door als er genoeg inschrijvingen zijn. Je betaalt pas als we het bevestigen.",
    dagen: [
      { naam: "Kerst maandag 21 december", label: "Maandag 21 december", datum: "2026-12-21" },
      { naam: "Kerst dinsdag 22 december", label: "Dinsdag 22 december", datum: "2026-12-22" },
      { naam: "Kerst woensdag 23 december", label: "Woensdag 23 december", datum: "2026-12-23" },
      { naam: "Kerst maandag 28 december", label: "Maandag 28 december", datum: "2026-12-28" },
      { naam: "Kerst dinsdag 29 december", label: "Dinsdag 29 december", datum: "2026-12-29" },
      { naam: "Kerst woensdag 30 december", label: "Woensdag 30 december", datum: "2026-12-30" },
    ],
  },
];
