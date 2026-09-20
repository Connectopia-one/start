/*
  Blogberichten.

  Een nieuw bericht schrijven? Voeg onderaan in de lijst een blok toe.
  Het bericht met de nieuwste datum komt vanzelf bovenaan.

  datum:  schrijf als "2026-06-18" (jaar-maand-dag)
  auteur: "Connectopia" of de naam van de partner die het schreef
  labels: korte woorden waar het bericht over gaat, bv. ["kampen", "zorgen"]

  De tekst bouw je op uit blokken. Er zijn er vijf:
    { soort: "tekst",   tekst: "..." }                     een gewone alinea
    { soort: "kop",     tekst: "..." }                     een tussentitel
    { soort: "lijst",   punten: [{ titel: "...", tekst: "..." }] }
    { soort: "afbeelding", bestand: "naam.png", beschrijving: "...", link: "..." }
    { soort: "knop",    tekst: "...", link: "https://..." }

  Bij "titel" in een lijstpunt: laat het weg als je alleen een zin wil.
  Bij een afbeelding: zet het bestand in de map  public/blog/
  en vul alleen de bestandsnaam in. "link" is optioneel; vul je die in,
  dan is de afbeelding klikbaar.
*/

export type Blok =
  | { soort: "tekst"; tekst: string }
  | { soort: "kop"; tekst: string }
  | { soort: "lijst"; punten: { titel?: string; tekst: string }[] }
  | { soort: "afbeelding"; bestand: string; beschrijving: string; link?: string }
  | { soort: "knop"; tekst: string; link: string };

export type Bericht = {
  slug: string;
  titel: string;
  datum: string;
  auteur: string;
  labels?: string[];
  samenvatting: string;
  blokken: Blok[];
};

export const blogTekst = {
  label: "Blog, tips en meer",
  titel: "Wat we leren, delen we",
  tekst:
    "Artikels van ons team en van externe partners, over opvoeden, school, diagnoses en alles wat ouders bezighoudt.",
  leegTekst: "Het eerste bericht staat er binnenkort aan te komen.",
};

export const berichten: Bericht[] = [
  {
    slug: "de-zomer-vreugde-of-stress",
    titel: "De zomer: een tijd van vreugde, of een bron van stress?",
    datum: "2026-06-18",
    auteur: "Kim",
    labels: ["zorgen", "kampen", "persoonlijk"],
    samenvatting:
      "Voor veel kinderen is de zomervakantie vrijheid en avontuur. Voor menig ouder is het een periode van intensieve logistieke en emotionele puzzels.",
    blokken: [
      {
        soort: "tekst",
        tekst:
          "De zomervakantie. Voor veel kinderen een periode van vrijheid en avontuur, maar voor menig ouder is het een periode van intensieve logistieke en emotionele puzzels. Terwijl de wereld spreekt over vakantieplannen en uitstapjes, zitten veel ouders van kinderen die net dat beetje extra ondersteuning nodig hebben in de zenuwspanning.",
      },
      { soort: "kop", tekst: "De zoektocht naar “gewoon”" },
      {
        soort: "tekst",
        tekst:
          "Voor ouders van een kind met een label of extra zorgbehoefte is een kamp zoeken geen kwestie van een snelle klik op een inschrijfformulier. Het is een zoektocht door een mijnenveld van onzekerheid. Waar het ene kind moeiteloos aansluit bij een voetbal- of chirokamp, is dat voor een kind met een andere gebruiksaanwijzing vaak niet weggelegd. Het gemis van die toegankelijkheid creëert ook een diepe kloof in gezinnen: broers en zussen moeten vaak gescheiden worden, waardoor ouders zich in bochten moeten wringen om alle opvang rond te krijgen.",
      },
      { soort: "kop", tekst: "De onzichtbare laag van angst" },
      {
        soort: "tekst",
        tekst:
          "Er is een laag van bezorgdheid waar zelden hardop over wordt gesproken. Het is de angst om je kind, dat extra zorg nodig heeft, achter te laten bij “vreemden”.",
      },
      {
        soort: "lijst",
        punten: [
          {
            titel: "Het wachten",
            tekst:
              "De telefoon die in je broekzak trilt, zorgt voor een direct verhoogde hartslag. Is het de begeleider? Gaat het mis?",
          },
          {
            titel: "De emotionele tol",
            tekst:
              "Het ophalen aan het einde van de dag voelt als een spannend examen. Hoeveel traantjes zijn er gevloeid? Hoeveel energie heeft dit gekost?",
          },
          {
            titel: "De euforie",
            tekst:
              "Maar dan is er dat zeldzame, gouden moment: het lukt. Het kind heeft genoten, het heeft gewerkt. De euforie die je dan als ouder voelt, is onbeschrijfelijk, een gevoel waar “normale” ouders vaak nooit bij stil hoeven te staan.",
          },
        ],
      },
      {
        soort: "afbeelding",
        bestand: "zomer-begeleiding.png",
        beschrijving: "Een begeleidster en een ouder kijken samen met een kind naar een tekening.",
      },
      { soort: "kop", tekst: "Waarom prikkelarm geen luxe is, maar noodzaak" },
      {
        soort: "tekst",
        tekst:
          "We geloven dat ieder kind recht heeft op een zorgeloze vakantie. Prikkelarme kampen zijn voor veel kinderen niet alleen een fijne extra, maar de enige manier om tot rust te komen en te groeien. Door structuur te bieden zonder de overprikkeling van grote groepen, creëren we een omgeving waar elk kind op zijn eigen tempo kan ontdekken en creëren.",
      },
      { soort: "kop", tekst: "Samen bouwen aan vertrouwen" },
      {
        soort: "tekst",
        tekst: "Wij geloven in een nieuwe aanpak. Een aanpak waarbij communicatie centraal staat:",
      },
      {
        soort: "lijst",
        punten: [
          {
            titel: "Transparantie",
            tekst: "Ouders moeten zich op elk moment kunnen verzekeren dat het goed gaat.",
          },
          {
            titel: "Betrokkenheid",
            tekst:
              "Door ouders echt te betrekken, halen we de angst weg en bouwen we samen aan een veilige haven.",
          },
          {
            titel: "Inclusiviteit",
            tekst:
              "Zorgen dat broers en zussen samen kunnen genieten, waardoor de druk op het gezin als geheel afneemt.",
          },
        ],
      },
      {
        soort: "tekst",
        tekst:
          "Wij willen een plek zijn waar de “angst voor het telefoontje” plaatsmaakt voor het vertrouwen in een fijne dag. Omdat elk kind, met of zonder label, de zomer van zijn leven verdient.",
      },
      {
        soort: "tekst",
        tekst:
          "Onze droom blijft dat elk kind zichzelf mag zijn, en dat prikkelarm en inclusief geen luxe zijn maar voor iedereen een mogelijke optie worden.",
      },
      { soort: "kop", tekst: "Een facebookgroep voor iedereen" },
      {
        soort: "tekst",
        tekst:
          "Wij hebben alvast een facebookgroep gemaakt om kamporganisatoren en ouders die kampen zoeken samen te brengen. Niet enkel van onze organisatie, maar gratis en open voor iedereen die kampen organiseert voor kinderen met extra noden in België. Ouders die leuke kampen willen aanbevelen, en zo samen een mooie verzameling kampjes op maat verzamelen. Alles is welkom!",
      },
      {
        soort: "afbeelding",
        bestand: "zomer-samen-spelen.png",
        beschrijving: "Vier kinderen spelen samen een gezelschapsspel op de grond.",
        link: "https://www.facebook.com/groups/2075601083022326/",
      },
      {
        soort: "knop",
        tekst: "Naar de facebookgroep",
        link: "https://www.facebook.com/groups/2075601083022326/",
      },
      {
        soort: "tekst",
        tekst:
          "Zo kunnen we allemaal ons steentje bijdragen en mee helpen in deze zoektocht. Met lieve groetjes, Kim",
      },
    ],
  },
  {
    slug: "officieel-een-vzw",
    titel: "Officieel een vzw, en dat vieren we samen met jullie",
    datum: "2026-09-04",
    auteur: "Connectopia",
    labels: ["nieuws", "tarieven"],
    samenvatting:
      "Vanaf schooljaar 2026–2027 zijn we niet alleen officieel een vzw, we verlagen ook onze prijzen.",
    blokken: [
      {
        soort: "tekst",
        tekst:
          "Vanaf schooljaar 2026–2027 zijn we niet alleen officieel een vzw, we verlagen ook onze prijzen. Zo maken we plaats voor nog meer nieuwsgierige kinderen die net dat beetje extra uitdaging, begrip of ruimte nodig hebben.",
      },
      {
        soort: "tekst",
        tekst:
          "De plusklas kost voortaan 50 euro per dag in plaats van 60, een pluswerking 25 euro per drie uur in plaats van 30, en een les Young Engineers 20 euro in plaats van 25.",
      },
      {
        soort: "tekst",
        tekst:
          "Bedankt aan iedereen die dit mee mogelijk maakt. Samen bouwen we aan een toekomst vol mogelijkheden.",
      },
    ],
  },
];

export const berichtenOpDatum = [...berichten].sort((a, b) =>
  b.datum.localeCompare(a.datum),
);
