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
    { soort: "afbeelding", bestand: "naam.jpg", beschrijving: "...", bijschrift: "..." }
    { soort: "knop",    tekst: "...", link: "https://..." }

  Bij "titel" in een lijstpunt: laat het weg als je alleen een zin wil.
  Bij een afbeelding: zet het bestand in de map  public/blog/
  en vul alleen de bestandsnaam in.
    beschrijving  vertelt wat er te zien is, voor wie de foto niet kan zien
    bijschrift    komt onder de foto te staan, bv. de naam van de fotograaf
    link          maakt de foto klikbaar
    klein: true   toont de foto op halve breedte, handig bij een kleine foto
*/

export type Blok =
  | { soort: "tekst"; tekst: string }
  | { soort: "kop"; tekst: string }
  | { soort: "lijst"; punten: { titel?: string; tekst: string }[] }
  | {
      soort: "afbeelding";
      bestand: string;
      beschrijving: string;
      bijschrift?: string;
      link?: string;
      klein?: boolean;
    }
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
    slug: "tranen-van-herkenning-op-het-forum",
    titel:
      "Tranen van herkenning: het forum De kracht van hoogbegaafdheid, en waarom Connectopia geen luxe is",
    datum: "2026-05-18",
    auteur: "Kim",
    labels: ["persoonlijk", "KU Leuven"],
    samenvatting:
      "Afgelopen maart was ik op het forum De kracht van hoogbegaafdheid bij KU Leuven. De zaal zat bomvol, en dat zegt alles over hoe groot de nood is.",
    blokken: [
      {
        soort: "tekst",
        tekst:
          "Afgelopen maart was ik op het forum “De kracht van hoogbegaafdheid” (KU Leuven). Ik had gehoopt op een interessante avond. Wat ik kreeg was veel meer: tranen van herkenning, een zaal die bomvol zat, en een vuur dat zegt: wij moeten verder.",
      },
      {
        soort: "afbeelding",
        bestand: "forum-zaal.jpg",
        beschrijving: "Een volle collegezaal tijdens de forumavond over hoogbegaafdheid.",
        bijschrift: "Forumavond rond hoogbegaafdheid bij KU Leuven. Foto: Joren De Weerdt",
      },
      {
        soort: "tekst",
        tekst:
          "Toen Kim Kiekens haar voordracht hield, schoot het bij mij helemaal vol. Ze verwoordde precies wat ik zo vaak niet kon zeggen: de eenzaamheid van een snel denkend brein, de vermoeidheid van jezelf steeds aanpassen, het verdriet als niemand ziet hoeveel moeite het kost om “normaal” te doen. Ik zat daar met kippenvel en een brok in mijn keel, en om me heen zag ik knikkende hoofden en ook natte ogen. Herkenning is geen theorie. Het is een lichamelijke ervaring.",
      },
      {
        soort: "afbeelding",
        bestand: "forum-spreker.jpg",
        beschrijving: "Een spreekster aan de lessenaar van KU Leuven tijdens de forumavond.",
        bijschrift: "Forumavond rond hoogbegaafdheid bij KU Leuven. Foto: Joren De Weerdt",
      },
      {
        soort: "tekst",
        tekst:
          "Wat me nóg meer raakte? De opkomst. De zaal was afgeladen vol. Ouders, leerkrachten, psychologen, coaches, en ook hoogbegaafde volwassenen die eindelijk antwoorden zochten. Die enorme opkomst benadrukt precies één ding: de nood is schrijnend. Mensen staan niet voor hun plezier in de file om naar een forum te gaan. Ze komen omdat ze ergens anders niet gehoord worden.",
      },
      { soort: "kop", tekst: "Hoogbegaafdheid mag geen taboe meer zijn" },
      {
        soort: "tekst",
        tekst:
          "We weten het al langer: hoogbegaafdheid wordt óf verheerlijkt, óf weggewuifd. “Ach wat erg, je kind kan zo goed leren.” Maar de valkuilen, perfectionisme, overprikkeling, sociale mismatch en faalangst, blijven te vaak onbesproken. Alsof je alleen maar dankbaar mag zijn. Alsof je geen recht hebt op steun.",
      },
      {
        soort: "tekst",
        tekst:
          "Kim Kiekens brak dat taboe met haar verhaal. En de zaal liet zien: wij willen hier wél over praten. Zonder schaamte. Zonder bagatellisering.",
      },
      {
        soort: "afbeelding",
        bestand: "forum-applaus.jpg",
        beschrijving: "Een zaal vol mensen die applaudisseren na de voordracht.",
        bijschrift: "Forumavond rond hoogbegaafdheid bij KU Leuven. Foto: Joren De Weerdt",
      },
      {
        soort: "kop",
        tekst: "Waarom Connectopia geen platform “erbij” is, maar een noodzaak",
      },
      {
        soort: "tekst",
        tekst:
          "Precies dáárom ben ik begonnen met Connectopia. Geen vrijblijvend initiatief, maar een antwoord op wat ik die avond voelde en zag:",
      },
      {
        soort: "lijst",
        punten: [
          { tekst: "Herkenning bieden waar die nu ontbreekt." },
          { tekst: "Valkuilen bespreekbaar maken zonder oordeel." },
          {
            tekst:
              "Lotgenoten en experts samenbrengen, omdat een school of gezin het vaak niet alleen kan trekken.",
          },
          {
            tekst:
              "Van taboe naar tool gaan: hoe herken je overprikkeling? Hoe praat je met een kind dat alles al snapt maar nog niet kan dragen?",
          },
        ],
      },
      {
        soort: "tekst",
        tekst:
          "De energie van die volle zaal heeft mij bevestigd: Connectopia is geen leuke extra, het is broodnodig. Er is een leegte in het hulplandschap voor cognitief sterke kinderen én hun omgeving. Die leegte willen we mee helpen vullen.",
      },
      { soort: "kop", tekst: "Laten we doorgaan" },
      {
        soort: "tekst",
        tekst:
          "Het forum was een prachtige start, maar geen eindpunt. Want morgen zitten diezelfde kinderen weer in een klas waar niemand begrijpt waarom ze zo intens reageren. Zitten ouders weer alleen met hun vragen. Zitten volwassen hoogbegaafden zich weer aan te passen tot ze knappen.",
      },
      { soort: "tekst", tekst: "Daarom mijn oproep:" },
      {
        soort: "lijst",
        punten: [
          {
            titel: "Praat verder",
            tekst: "Deel dit bericht, vertel over jouw traan van herkenning.",
          },
          {
            titel: "Volg Connectopia",
            tekst: "Hoe meer mensen meebouwen, hoe sneller we een écht vangnet hebben.",
          },
          {
            titel: "Maak hoogbegaafdheid bespreekbaar",
            tekst:
              "Op school, aan de keukentafel, op de werkvloer. Zowel de krachten als de kwetsbaarheden.",
          },
        ],
      },
      {
        soort: "tekst",
        tekst:
          "Samen zorgen we dat niemand meer in stilte huilt van onbegrip, maar dat tranen van herkenning altijd gevolgd worden door: “Wij gaan je helpen.”",
      },
      {
        soort: "tekst",
        tekst:
          "Met heel lieve groetjes en een welgemeend applaus, en ik hoop dat er nog veel forums mogen komen.",
      },
    ],
  },
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
        klein: true,
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
        klein: true,
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
