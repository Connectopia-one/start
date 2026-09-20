/*
  Blogberichten.

  Een nieuw bericht schrijven? Voeg onderaan in de lijst een blok toe.
  Het bericht met de nieuwste datum komt vanzelf bovenaan.

  datum:  schrijf als "2026-06-18" (jaar-maand-dag)
  auteur: "Connectopia" of de naam van de partner die het schreef
  labels: korte woorden waar het bericht over gaat, bv. ["kampen", "zorgen"]

  De tekst bouw je op uit blokken. Er zijn er zes:
    { soort: "tekst",   tekst: "..." }                     een gewone alinea
    { soort: "kop",     tekst: "..." }                     een tussentitel
    { soort: "citaat",  tekst: "..." }                     een uitgelichte quote
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
  | { soort: "citaat"; tekst: string }
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
    slug: "diep-gedacht-en-intens-gevoeld",
    titel: "Diep gedacht en intens gevoeld: verhalen van hoogbegaafde vrouwen",
    datum: "2026-03-20",
    auteur: "Tine Geysen",
    labels: ["boek", "Tine Geysen", "persoonlijk"],
    samenvatting:
      "Een boek van tien hoogbegaafde vrouwen die openhartig over hun leven vertellen, omkaderd door elf experts. Tine Geysen vertelt hoe het ontstond.",
    blokken: [
      {
        soort: "afbeelding",
        bestand: "boek-cover.jpg",
        beschrijving:
          "De cover van het boek Diep gedacht en intens gevoeld, met een lijntekening van een vrouw.",
        klein: true,
      },
      {
        soort: "tekst",
        tekst:
          "Het boek Diep gedacht en intens gevoeld is een samenwerking van 21 hoogbegaafde vrouwen. Tien vrouwen die elk hun eigen verhaal, hun eigen zoektocht en hun eigen moed hebben ingebracht. Deze ervaringen zijn omkaderd door 11 experts.",
      },
      {
        soort: "citaat",
        tekst:
          "Ik dacht dat ik te veel voelde, te diep dacht en te anders was. Maar ik besef nu dat dit net mijn kracht is, mijn superkracht.",
      },
      {
        soort: "tekst",
        tekst:
          "Ons boek is geen toeval. Het is het resultaat van een vuur dat in ons allemaal brandt. Dat maakt deze samenwerking bijzonder: we zijn verbonden door een gedeelde missie, hoogbegaafdheid beter zichtbaar maken, taboes doorbreken en de herkenning ervan bij vrouwen en meisjes omhoog brengen.",
      },
      { soort: "kop", tekst: "Een goed gelukte alien" },
      {
        soort: "tekst",
        tekst:
          "Voor mij persoonlijk begon dat vuur vanuit een gevoel waarmee ik lange tijd geworsteld heb: eenzaamheid. Ik voelde me vaak alsof ik een goed gelukte alien was die hier rondloopt. Met een missie, alleen waren ze me vergeten te vertellen welke missie dat precies was.",
      },
      {
        soort: "tekst",
        tekst:
          "Tijdens de coronaperiode besloot ik dat het misschien tijd was om aan mijn zelfvertrouwen te werken. Ik begon te lezen over hoogsensitiviteit en trauma, en plots kwam hoogbegaafdheid op mijn pad. Of ik daar ooit al bij stilgestaan had?",
      },
      {
        soort: "tekst",
        tekst:
          "Hoe meer ik las, hoe meer ik meende te herkennen. Maar tegelijk groeide mijn twijfel. Wie was ik eigenlijk? Iemand die zogezegd alles had, maar toch een leegte voelde, zo ergens ter hoogte van mijn borstkas. Ik voelde wel dat er meer inzat, maar wat was meer dan net?",
      },
      {
        soort: "tekst",
        tekst:
          "Kon het echt dat ik mezelf hierin herkende? Waarom hoorde ik bij de term hoogbegaafdheid zo vaak: “Slim, maar…”? Die betekenisvolle “maar”, waar nooit echt concrete handvatten bij kwamen.",
      },
      { soort: "kop", tekst: "Van een ik-verhaal naar een wij-verhaal" },
      {
        soort: "tekst",
        tekst:
          "Ik ging op zoek naar gelijkgestemden. Eerst andere mama’s, op zoek naar antwoorden voor hun kinderen. Hoe kunnen we hoogbegaafdheid positief benaderen? Wie ziet hier ook de kracht in? Wat betekent die “maar” voor jullie?",
      },
      {
        soort: "tekst",
        tekst:
          "Via sociale media vond ik andere vrouwen die hun intense zoektocht rond hoogbegaafdheid deelden. Hun eerlijkheid, hun kwetsbaarheid, hun verhalen brachten herkenning. En langzaam groeide een nieuwe vraag: herkenden zij ook iets bij zichzelf? Mocht hoogbegaafdheid wel? Maar diep vanbinnen voelde ik dat het klopte. We besloten dan ook om samen ons levensverhaal te brengen. Want wat als onze verhalen ook andere vrouwen zouden helpen? Wat als herkenning de eerste stap kon zijn naar groei, naar zelfvertrouwen, naar het ontwikkelen van talent en het begrijpen van valkuilen?",
      },
      {
        soort: "tekst",
        tekst:
          "Er kwam een WhatsApp-groep. Gesprekken. Herkenning. En steeds vaker die verwondering: hoe kan het dat vrouwen die kilometers van elkaar opgroeiden, zonder elkaar te kennen, zo gelijkaardige ervaringen delen? Vanaf dat moment was het geen individueel verhaal meer, maar een wij-verhaal.",
      },
      {
        soort: "afbeelding",
        bestand: "boek-voorstelling.jpg",
        beschrijving:
          "De vrouwen achter het boek staan samen op het podium bij de voorstelling in KU Leuven.",
        bijschrift:
          "De voorstelling van het boek bij KU Leuven, Campus Group T Leuven.",
      },
      {
        soort: "tekst",
        tekst:
          "Omdat onze groep zo divers is, wilden we ook verschillende experts samenbrengen. Niet één definitie van hoogbegaafdheid opleggen, maar de vele gezichten ervan laten zien. De rode draad in onze verhalen zichtbaar maken.",
      },
      {
        soort: "afbeelding",
        bestand: "boek-tekening.jpg",
        beschrijving:
          "Een lijntekening van een meisje in een kleedje met hartjes.",
        klein: true,
      },
      {
        soort: "tekst",
        tekst:
          "Dit boek is dan ook een ode aan elke vrouw die voelt dat er meer in haar zit. Dat ze hoogbegaafd is en dit talent omarmt. En dat ze dat wil voorleven. Je bent niet te veel en niet alleen, en je verdient zoveel liefde en begrip!",
      },
      { soort: "tekst", tekst: "— Tine Geysen" },
      {
        soort: "knop",
        tekst: "Meer over het boek",
        link: "https://www.projectdiepgedacht.be/",
      },
    ],
  },
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
        beschrijving:
          "Een volle collegezaal tijdens de forumavond over hoogbegaafdheid.",
        bijschrift:
          "Forumavond rond hoogbegaafdheid bij KU Leuven. Foto: Joren De Weerdt",
      },
      {
        soort: "tekst",
        tekst:
          "Toen Kim Kiekens haar voordracht hield, schoot het bij mij helemaal vol. Ze verwoordde precies wat ik zo vaak niet kon zeggen: de eenzaamheid van een snel denkend brein, de vermoeidheid van jezelf steeds aanpassen, het verdriet als niemand ziet hoeveel moeite het kost om “normaal” te doen. Ik zat daar met kippenvel en een brok in mijn keel, en om me heen zag ik knikkende hoofden en ook natte ogen. Herkenning is geen theorie. Het is een lichamelijke ervaring.",
      },
      {
        soort: "afbeelding",
        bestand: "forum-spreker.jpg",
        beschrijving:
          "Een spreekster aan de lessenaar van KU Leuven tijdens de forumavond.",
        bijschrift:
          "Forumavond rond hoogbegaafdheid bij KU Leuven. Foto: Joren De Weerdt",
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
        beschrijving:
          "Een zaal vol mensen die applaudisseren na de voordracht.",
        bijschrift:
          "Forumavond rond hoogbegaafdheid bij KU Leuven. Foto: Joren De Weerdt",
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
            tekst:
              "Hoe meer mensen meebouwen, hoe sneller we een écht vangnet hebben.",
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
        beschrijving:
          "Een begeleidster en een ouder kijken samen met een kind naar een tekening.",
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
        tekst:
          "Wij geloven in een nieuwe aanpak. Een aanpak waarbij communicatie centraal staat:",
      },
      {
        soort: "lijst",
        punten: [
          {
            titel: "Transparantie",
            tekst:
              "Ouders moeten zich op elk moment kunnen verzekeren dat het goed gaat.",
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
        beschrijving:
          "Vier kinderen spelen samen een gezelschapsspel op de grond.",
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
  {
    slug: "geen-kind-is-hetzelfde",
    titel:
      "Geen kind is hetzelfde: waarom we moeten stoppen met het hokje “hoogbegaafd”",
    datum: "2026-02-28",
    auteur: "Kim",
    labels: ["persoonlijk"],
    samenvatting:
      "De snelle rekenaar, de jonge schaker, het kind dat zich verveelt in de klas. Die bestaan. Maar er zijn net zoveel verschillen tussen hoogbegaafde kinderen als tussen alle andere kinderen.",
    blokken: [
      {
        soort: "tekst",
        tekst:
          "Wanneer mensen denken aan een hoogbegaafd kind, schieten er vaak een paar vaste plaatjes door hun hoofd: de snelle rekenaar, de jonge schaker, het meisje dat op haar vierde al zelfstandig leest, of de jongen die zijn tijd verveelt in de klas omdat hij alles al weet. En ja, die bestaan. Maar wat als ik je vertel dat het beeld dat we hebben van hoogbegaafdheid (HB) en uitzonderlijke hoogbegaafdheid (UHB) voor heel veel kinderen helemaal niet klopt? Dat er net zoveel verschillen zijn tussen hoogbegaafde kinderen als tussen alle andere kinderen op de wereld?",
      },
      {
        soort: "afbeelding",
        bestand: "hokje-dagdromen.jpg",
        beschrijving:
          "Tekening van een meisje dat in de klas voor zich uit droomt, met planeten, een boom, een vraagteken en een hart in een wolk boven haar hoofd.",
      },
      { soort: "kop", tekst: "De mythe van de universele HB'er" },
      {
        soort: "tekst",
        tekst:
          "De samenleving houdt van hokjes. Het geeft houvast. “Hoogbegaafd? Oh, dan ben je goed in wiskunde en schaken.” Maar de werkelijkheid is een stuk weerbarstiger en vooral een stuk kleurrijker.",
      },
      {
        soort: "tekst",
        tekst:
          "Ik wil graag een lans breken voor de kinderen die niet in dat standaardplaatje passen. Want de waarheid is: niet elke hoogbegaafde houdt van schaken. Sterker nog, er zijn er genoeg die een hekel hebben aan de stilte en de strategie van een schaakbord.",
      },
      {
        soort: "lijst",
        punten: [
          {
            titel: "De creatieveling",
            tekst:
              "Er zijn HB'ers die hun intelligentie uiten in kunst, muziek of verhalen verzinnen. Hun hoofd zit vol beelden en emoties, niet per se met getallen.",
          },
          {
            titel: "De doener",
            tekst:
              "Er zijn HB'ers die hun energie kwijt moeten in sport of bouwen. Hun slimheid zit in hun handelen, in het begrijpen van hoe dingen in elkaar steken door ze uit elkaar te halen.",
          },
          {
            titel: "De alleskunner",
            tekst:
              "En ja, er zijn er ook die van alles een beetje lusten. Die net zo goed een potje kunnen schaken als een schilderij kunnen maken, maar zich nergens volledig in thuis voelen omdat de wereld hen vraagt om te kiezen.",
          },
        ],
      },
      {
        soort: "afbeelding",
        bestand: "hokje-bouwen.jpg",
        beschrijving:
          "Tekening van een jongen die aan tafel een raket van karton in elkaar knutselt, tussen schetsen, een schaar en lijm.",
      },
      { soort: "kop", tekst: "Door de mazen van het net" },
      {
        soort: "tekst",
        tekst:
          "Het grootste probleem van die vastomlijnde verwachtingen? Dat kinderen er letterlijk doorheen vallen. De kinderen die niet voldoen aan het stereotype, worden simpelweg niet gezien.",
      },
      {
        soort: "tekst",
        tekst:
          "Denk aan het meisje dat stil is in de klas, niet voor haar beurt praat, maar thuis intense vragen stelt over het leven en de dood. Ze valt niet op, dus krijgt ze geen uitdaging.",
      },
      {
        soort: "tekst",
        tekst:
          "Denk aan de jongen die constant in conflict is omdat hij de waarom-vragen stelt waar de juf geen antwoord op heeft, en daardoor niet als slim, maar als lastig wordt bestempeld.",
      },
      {
        soort: "tekst",
        tekst:
          "En denk aan de kinderen die moeite hebben met rekenen vanwege dyscalculie, maar wel een uitzonderlijk taalgevoel hebben. Hun hoogbegaafdheid is niet “rendabel” voor de schoolprestaties, dus glippen ze door de mazen van het net. Ze voldoen niet aan de gekke verwachtingen die mensen hebben, en dat is ontzettend schadelijk. Het zorgt voor onbegrip, een laag zelfbeeld en het gevoel dat er iets mis is met jou, terwijl er juist iets mis is met de bril waardoor we kijken.",
      },
      {
        soort: "afbeelding",
        bestand: "hokje-muziek.jpg",
        beschrijving:
          "Tekening van een jongen die in een nis in een muur zit, terwijl noten, tandwielen, een potlood en een boek uit de opening tevoorschijn komen.",
      },
      { soort: "kop", tekst: "Waarom het ertoe doet" },
      {
        soort: "tekst",
        tekst:
          "Waarom is het zo belangrijk dat we dit beeld bijstellen? Omdat ieder kind de kans verdient om gezien te worden voor wie het werkelijk is. Een kind dat zich niet herkent in het hokje “hoogbegaafd”, zal dat label al snel afwijzen. “Als hoogbegaafd zijn betekent dat ik van rekenen moet houden, dan ben ik het niet.” En zo blijven ze rondlopen met een gevoel van anders zijn, zonder te weten waarom.",
      },
      { soort: "kop", tekst: "De schoonheid van diversiteit" },
      {
        soort: "tekst",
        tekst:
          "Laten we eerlijk zijn: wat zou de wereld ontzettend saai zijn als we allemaal hetzelfde waren. Stel je een wereld voor waarin iedereen hetzelfde denkt, dezelfde hobby's heeft en op dezelfde manier leert. Het zou een stille, grijze wereld zijn.",
      },
      {
        soort: "tekst",
        tekst:
          "De kracht van hoogbegaafdheid zit hem juist in de diversiteit. In de ene die later uitvinder wordt, de ander die maatschappelijke problemen oplost en de derde die ons raakt met muziek of schilderijen. Hoogbegaafdheid is geen sjabloon, het is een unieke manier van in de wereld staan, die er bij ieder mens weer anders uitziet.",
      },
      { soort: "kop", tekst: "Tot slot" },
      {
        soort: "tekst",
        tekst:
          "Dus laten we stoppen met het opleggen van verwachtingen. Laten we in plaats daarvan nieuwsgierig zijn. Niet vragen: “Speel je schaak?”, maar vragen: “Waar ga jij van gloeien? Waar ben jij nieuwsgierig naar?” Pas dan gaan we de rijkdom van hoogbegaafdheid echt zien. Pas dan zien we het kind, niet het label.",
      },
      {
        soort: "citaat",
        tekst:
          "Herken jij dit? Heb jij het gevoel dat je als kind, of nu, in een hokje werd gedrukt? Of heb je een kind dat niet in het plaatje past? Deel je ervaringen.",
      },
      { soort: "knop", tekst: "Deel je ervaring", link: "/contact" },
    ],
  },
  {
    slug: "leren-leren-lessen-uit-het-muziekonderwijs",
    titel: "Leren leren: lessen uit het muziekonderwijs",
    datum: "2026-02-28",
    auteur: "Lucas Dumoulin",
    labels: ["Lucas Dumoulin", "onderwijs", "ervaringen", "persoonlijk"],
    samenvatting:
      "Vaak ligt het probleem niet bij de leerstof, maar bij de studiemethode. Bijlesdocent en violist Lucas Dumoulin over wat het onderwijs kan leren van de muziekschool.",
    blokken: [
      {
        soort: "tekst",
        tekst:
          "Veel studenten kloppen aan bij een bijlesdocent met problemen voor een vak, maar vaak blijkt al snel dat hun probleem niet aan de leerstof ligt, wel aan hun studiemethode. Tegelijkertijd merk ik dat leerlingen wél academische vaardigheden leren, maar dan in de muziekschool. Om kort door de bocht te gaan: de muziekschool leert vaardigheden aan, het onderwijs biedt kennis aan. De truc is om ze ook in het onderwijs toe te passen.",
      },
      {
        soort: "afbeelding",
        bestand: "lucas-dumoulin.jpg",
        beschrijving:
          "Lucas Dumoulin in een muzieklokaal, met een piano en een rij gitaren aan de muur achter hem.",
        klein: true,
      },
      {
        soort: "tekst",
        tekst:
          "Ik ben Lucas, een bijlesdocent met een sterke focus op studiemethoden. Mijn werk is dus eigenlijk pas geslaagd als leerlingen niet meer moeten terugkomen. Daarnaast speel ik ook viool: vanuit deze combinatie wil ik in deze blog verkennen wat het reguliere onderwijs wel eens kan leren van de muziekschool.",
      },
      { soort: "kop", tekst: "1. Focus op de fundamenten" },
      {
        soort: "tekst",
        tekst:
          "Wie muziek studeert, ontdekt het snel: zonder stevige fundamenten wordt de volgende stap onnodig moeilijk. Dit begint zelfs voor je een instrument aanraakt: de taal van de muziek kunnen spreken is cruciaal. In de eerste jaren gaat er veel aandacht naar begrijpen wat muziek nu eigenlijk is. Begrippen zoals een toonaard, noten en akkoorden zijn belangrijke basisstukken om later een instrument te bespelen. Wanneer de basis onvoldoende wordt beheerst ben je eigenlijk niet meer bezig met je instrument, maar met het ontcijferen van de taal. Zonde, want zo wordt oefenen onnodig inefficiënt.",
      },
      {
        soort: "afbeelding",
        bestand: "leren-leren-viool.jpg",
        beschrijving:
          "Een viool met strijkstok op een houten tafel, naast een rode ringmap en opengeslagen studieboeken.",
        bijschrift: "Een greep uit mijn eigen leven",
      },
      {
        soort: "tekst",
        tekst:
          "Een parallel met wiskunde kan gemaakt worden: veel problemen die opduiken in het vierde en vijfde middelbaar hebben als oorzaak slechte fundamenten. Die problemen worden lang verscholen door intelligentie en patroonherkenning. Maar op een bepaald moment wordt verwacht dat alle regels gekend en toegepast worden, terwijl de oefeningen steeds complexer worden. Als die basisregels niet voldoende gekend zijn, gaat het mis en laat je steken vallen. “Domme fouten”. Harder studeren helpt niet wanneer het probleem ónder de leerstof zit. Op termijn concluderen dan veel studenten “ik ben gewoon niet goed in wiskunde of chemie”. Dat vind ik zonde.",
      },
      {
        soort: "tekst",
        tekst:
          "Ik heb deze les zelf ook ondervonden. Wanneer je viool leert spelen, spendeer je de eerste jaren aan de basishandelingen. Pas wanneer dat vlot gaat begin je met het echte werk: muziek interpreteren en maken. Zonder die basis ben je continu aan het nadenken over hoe je moet bewegen om geluid te maken. Je kan dus niet meer bezig zijn met de echte muziek. Dit was voor mij wel duidelijk voor viool, maar bij wiskunde helemaal niet.",
      },
      {
        soort: "tekst",
        tekst:
          "In het vijfde middelbaar kwam ik dan ook in de problemen met wiskunde. Ik ben met de hakken over de sloot door geraakt, en ik dacht lang dat ik gewoon niet goed in wiskunde was. Tot ik later de kans kreeg om bijles examencommissie te geven. Tijdens mijn voorbereiding ben ik met de pure fundamenten begonnen, en blijkt: wat vroeger zo moeilijk leek bleek wel mee te vallen zonder fundamentele gaten in mijn kennis.",
      },
      { soort: "kop", tekst: "2. Moeilijkheden verdragen" },
      {
        soort: "tekst",
        tekst:
          "Voor slimme of hoogbegaafde kinderen gaat school meestal vanzelf. Studeren is iets vreemd, falen nog meer. Muziek biedt een harde, maar eerlijke leerschool: een muur waar je keer op keer tegenaan botst. Niemand, ongeacht hun intelligentie, kan uit zichzelf een instrument. Dat vereist duizenden uren oefening, en falen. Heel veel falen. Tijdens het oefenen, in de les, op toonmomenten. Vooruitgang ontstaat alleen door continu tegen die muur aan te lopen, en nog liefst met je hoofd eerst.",
      },
      {
        soort: "afbeelding",
        bestand: "leren-leren-piano.jpg",
        klein: true,
        beschrijving:
          "Een pianist speelt op een vleugel op een groot podium, in het licht van een spot, voor een volle zaal.",
        bijschrift: "Erger dan een spreekbeurt?",
      },
      {
        soort: "tekst",
        tekst:
          "Dat is prachtig: falen is een vaardigheid die iedereen moet leren. Je leert niet alleen een instrument, maar ook vele soft skills: leren optreden vertaalt heel goed naar spreekbeurten of presentaties geven. En ook omgaan met het feit dat soms niet alles gaat zoals je zou willen, en dat dat oké is. En tegelijkertijd word je steeds beter in je instrument: de vruchten van je harde werk. Voor veel kinderen is muziek een ideale opstap om dé belangrijkste vaardigheid te leren: vallen en terug opstaan.",
      },
      {
        soort: "tekst",
        tekst:
          "Eén belangrijke kanttekening: doorzetten is belangrijk, maar weten wanneer te stoppen ook. Regelmatig herevalueren, bij de inschrijving voor volgend jaar bijvoorbeeld, en de vraag “is dit eigenlijk iets voor mij?” stellen is niet opgeven. Tijd is gelimiteerd, en dan kan je beter dingen doen die je graag doet.",
      },
      { soort: "kop", tekst: "3. (Gericht) herhalen, herhalen, herhalen" },
      {
        soort: "tekst",
        tekst:
          "Het meest herhaalde (ha!) devies van studiebegeleiding. Gevolgd door “ja, maar het is ook echt zo belangrijk!”. Absoluut, maar wat houdt herhalen nu eigenlijk in? En hoe herhaal ik nu goed? Als je methode aan deze eigenschappen voldoet, ben je al goed bezig:",
      },
      {
        soort: "lijst",
        punten: [
          {
            titel: "Gespreid",
            tekst: "Liefst over meerdere dagen, om te kunnen verwerken.",
          },
          {
            titel: "Gefocust",
            tekst:
              "Actief nadenken is veel effectiever. Na het herhalen moet je het gevoel hebben dat je hard gewerkt hebt.",
          },
          {
            titel: "Tijdsbesparend",
            tekst:
              "Als je je tijd optelt, ben je minder lang bezig dan alles in één studeersessie te doen.",
          },
        ],
      },
      {
        soort: "afbeelding",
        bestand: "leren-leren-herhalen.png",
        klein: true,
        beschrijving:
          "Grafiek met kennis op de verticale as en dagen op de horizontale as. Na elk moment van leren zakt de kennis, en elke herhaling brengt ze terug naar honderd procent, telkens minder steil.",
        bijschrift:
          "Gespreid herhalen is één van de meest gebruikte methodes. Met goede reden: het werkt",
      },
      {
        soort: "tekst",
        tekst:
          "Of het nu voetbal of viool is: een hobby oefen je ook niet één dag per week zes uur lang, maar liever gespreid. En als je iets wilt leren, dan gaat dat niet met je hersenen op automatische piloot. Herhaling werkt pas wanneer ze inspanning vraagt. Passieve herhaling heeft ook zijn plaats, maar dan als kers op de taart. Blootstelling is dé manier om uit te munten.",
      },
      { soort: "kop", tekst: "4. Leren door blootstelling" },
      {
        soort: "tekst",
        tekst:
          "Leren vereist niet altijd studeren. Ja, studeren is nodig, maar niet alles. Blootstelling kan helpen om met weinig extra inzet meer resultaten te boeken. Maar wat is dat?",
      },
      {
        soort: "tekst",
        tekst:
          "Een klassiek voorbeeld: een enthousiaste student legt de leerstof uit aan de keukentafel. Sommige delen gaan vlot, die zijn goed gekend. Andere gaan moeizamer, daar is nog werk aan. Ondertussen is alles nog een keer herhaald. Hetzelfde gaat voor uitleg geven aan medestudenten. Je test jezelf en herhaalt, zonder dat het als studeren aanvoelt.",
      },
      {
        soort: "tekst",
        tekst:
          "Ook YouTube-video's over het onderwerp, wetenschappelijke artikels, gesprekken met AI en dergelijke kunnen het leerproces versterken. Uiteraard gecombineerd met studeren, want anders blijf je te oppervlakkig. Minstens even belangrijk: deze zaken werken motiverend. Soms moet je alleen de toepassing van de leerstof zien om iets te willen leren, of tenminste beter begrijpen.",
      },
      {
        soort: "tekst",
        tekst:
          "Het is dus niet altijd nodig om nieuwe technieken te leren om beter te leren: we hebben al goede gewoontes die we elders al toepassen. De muziekschool begrijpt iets fundamenteels: vooruitgang is zelden spectaculair. Het is het resultaat van sterke fundamenten, gerichte herhaling en de bereidheid om moeilijkheden te confronteren.",
      },
      {
        soort: "tekst",
        tekst:
          "Heb je vragen of opmerkingen over dit artikel, of wil je graag eens babbelen? Aarzel niet om contact op te nemen. Lucas Dumoulin, telefoon +32 472 43 23 05.",
      },
      {
        soort: "knop",
        tekst: "Mail Lucas",
        link: "mailto:dmlnlucas@gmail.com",
      },
    ],
  },
  {
    slug: "de-wijsheid-van-de-zoektocht",
    titel:
      "De wijsheid van de zoektocht: waarom niemand de waarheid in pacht heeft (en dat oké is)",
    datum: "2026-02-19",
    auteur: "Kim",
    labels: ["ervaringen", "persoonlijk"],
    samenvatting:
      "Geen handleidingen, geen heilige graal. Waarom we bij Connectopia liever samen zoeken dan elkaar de les spellen.",
    blokken: [
      {
        soort: "tekst",
        tekst:
          "Welkom bij Connectopia. Een plek waar we geen handleidingen uitdelen, want die bestaan niet. Een plek waar we geen stempel van expert op iemand plakken alsof zij de heilige graal in handen hebben. Waarom niet? Omdat ieder mens, ieder kind, en zeker ieder hoogbegaafd (HB) of uitzonderlijk hoogbegaafd (UHB) kind, een uniek universum is.",
      },
      {
        soort: "tekst",
        tekst:
          "Wat voor de één een verademing is, kan voor de ander een absolute ramp betekenen. De ene leerling bloeit op bij een bepaalde methode, terwijl de andere er volledig door vastloopt. En dat is precies waarom wij hier op een andere manier met elkaar willen omgaan.",
      },
      { soort: "kop", tekst: "Een gemeenschappelijk hart" },
      {
        soort: "tekst",
        tekst:
          "Het eerste wat we willen benadrukken is dit: iedereen die op deze website terechtkomt, of je nu een professional bent met jarenlange studie of een ouder die zichzelf heeft ingelezen uit pure noodzaak, doet dit met een hart voor onze kinderen. Iedereen probeert bij te scholen, te leren en te begrijpen. Laten we dat nooit uit het oog verliezen.",
      },
      {
        soort: "tekst",
        tekst:
          "Want de harde waarheid is: niemand, zelfs de meest doorgewinterde expert niet, weet écht hoe alles zit. Het pad van een hoogbegaafd kind is niet lineair. Het is een kronkelend bospad dat constant verandert. Wat gisteren werkte, is vandaag achterhaald. De ontwikkeling van jouw kind is geen vaststaand gegeven, maar een dynamisch proces. En dat maakt het voor ons als ouders, maar zeker ook voor de kinderen zelf, soms ongelooflijk moeilijk.",
      },
      {
        soort: "afbeelding",
        bestand: "zoektocht-student.jpg",
        beschrijving:
          "Tekening van een jongere die met de handen aan het hoofd aan tafel zit, met een kluwen van gedachten boven het hoofd, een knuffel naast zich en een stapel boeken en papieren voor zich.",
      },
      {
        soort: "tekst",
        tekst:
          "Deze kinderen denken dieper, voelen intenser en dragen vaak veel meer zorgen met zich mee dan wij aan de oppervlakte zien. Het opvoeden van een HB-kind is dan ook geen evidentie. Het is een intense reis vol hoogte- en dieptepunten.",
      },
      { soort: "kop", tekst: "De kracht van vriendelijke feedback" },
      {
        soort: "tekst",
        tekst:
          "We zien op forums en in ouderraden vaak zoveel boosheid en frustratie. En terecht! Soms is een test volledig fout gegaan. Soms is er een advies gegeven dat niet alleen niet hielp, maar averechts werkte. Het is meer dan begrijpelijk dat je kwaad bent. Ventileren mag, het is zelfs nodig.",
      },
      {
        soort: "tekst",
        tekst:
          "Maar wat als we ons realiseren dat die frustratie, als we haar te lang vasthouden, vooral onszelf raakt? Wat als we in ons achterhoofd houden dat de persoon aan de andere kant van dat verkeerde advies, het waarschijnlijk wél goed bedoelde?",
      },
      {
        soort: "tekst",
        tekst:
          "In plaats van boosheid, kunnen we kiezen voor vriendelijkheid en respect. Dat betekent niet dat je je mond houdt. Integendeel. Wat mij helpt, is uit te leggen waarom iets voor ons niet werkte. Dat doe ik met respect, maar ook met duidelijkheid. En daarna ga ik verder met zoeken naar wat wel werkt. Want wie kent jouw kind, of wie ben jijzelf, nu het beste?",
      },
      { soort: "kop", tekst: "Fouten maken mag, ook voor professionals" },
      {
        soort: "tekst",
        tekst:
          "We leren onze kinderen toch ook dat fouten maken mag? Al hebben veel HB- en UHB-kinderen het daar zelf moeilijk mee, omdat ze zo streng zijn voor zichzelf. Waarom zou dat dan niet gelden voor de mensen die ons proberen te helpen?",
      },
      {
        soort: "tekst",
        tekst:
          "Professionals kunnen alleen maar beter worden in hun werk als ze eerlijke, maar respectvolle feedback krijgen. Als wij hen niet vertellen wat er bij ons thuis écht gebeurde met hun advies, missen zij een cruciaal stukje van de puzzel. Zo leren we samen.",
      },
      { soort: "kop", tekst: "Samen lichter worden" },
      {
        soort: "tekst",
        tekst:
          "Connectopia wil een community zijn waar we die zoektocht samen aangaan. Waar we elkaar steunen, in plaats van afbreken. Waar we elkaars expertise erkennen, maar ook de grenzen ervan. Waar we mogen zeggen dat het moeilijk is, maar waar we elkaar ook helpen om positief te blijven.",
      },
      {
        soort: "tekst",
        tekst:
          "Want door vriendelijk en lief te blijven, en door te onthouden dat we allemaal starten vanuit de juiste intenties, doen we iets bijzonders: we worden zelf ook lichter. En wie weet voelt de reis dan net iets minder eenzaam.",
      },
      {
        soort: "tekst",
        tekst:
          "Dus laten we met elkaar in gesprek gaan. Niet als expert en leek, maar als metgezellen op een gedeeld pad. Met vriendelijkheid, met respect, en met een open blik voor de unieke noden van ieder kind en ieder gezin.",
      },
      {
        soort: "citaat",
        tekst: "Welkom bij Connectopia. Laten we samen op weg gaan.",
      },
    ],
  },
  {
    slug: "autisme-bij-cognitief-begaafde-kinderen",
    titel: "Autisme bij cognitief begaafde kinderen",
    datum: "2026-02-19",
    auteur: "Katrien Volckaert",
    labels: ["Katrien Volckaert", "ervaringen"],
    samenvatting:
      "Slimme kinderen krijgen soms ten onrechte de diagnose autisme. Maar de omgekeerde fout bestaat ook: autisme dat onzichtbaar blijft achter een perfect gekopieerd maatpak.",
    blokken: [
      {
        soort: "afbeelding",
        bestand: "katrien-volckaert.jpg",
        beschrijving:
          "Katrien Volckaert, lachend, voor groen struikgewas met gele bloemen.",
      },
      {
        soort: "tekst",
        tekst:
          "Tijdens mijn opleiding tot experte in de hoogbegaafdheid leerde ik dat cognitief begaafde kinderen vaak ten onrechte de diagnose van autisme krijgen. Dit komt door hun soms weinig sociaal ogende gedrag. Ze vinden geen aansluiting bij hun leeftijdsgenootjes en zoeken jongere of net oudere kinderen op als speelkameraad. Wanneer dergelijk gedrag opgemerkt wordt, wordt er snel van uitgegaan dat deze kinderen sociaal nog niet rijp genoeg zijn. Dat ze wel heel intelligent zijn, maar dat ze sociaal-emotioneel nog niet op datzelfde niveau functioneren.",
      },
      {
        soort: "tekst",
        tekst:
          "Hierbij wordt vaak over het hoofd gezien dat er nog andere redenen bestaan die kunnen maken dat cognitief begaafde kinderen moeilijk aansluiting vinden bij leeftijdsgenootjes. Eén van die redenen wordt prachtig geïllustreerd in onderstaande cartoon.",
      },
      {
        soort: "afbeelding",
        bestand: "autisme-cartoon.jpg",
        beschrijving:
          "Cartoon in vijf beeldjes. Een kleuter vraagt aan een ander kind om het rode blokje, roept daarna luider, en krijgt van een volwassene te horen dat hij niet moet zeuren, hij kreeg toch een blokje. Twee volwassenen concluderen erna dat hij wel reuze slim is, maar emotioneel toch heel erg achter.",
      },
      {
        soort: "tekst",
        tekst:
          "Ik herinner me nog heel goed hoe mijn dochter, die zichzelf op driejarige leeftijd leerde lezen, in de tweede kleuterklas dagelijks naar huis kwam met verhalen over hoe dom haar klasgenootjes wel waren. In haar beleving, natuurlijk. “Mama, die kunnen nog niet eens de letter p lezen!” Je kunt je wel voorstellen dat zij op dat moment in een gans andere wereld vertoefde dan haar klasgenoten. Ook zij stelde ons meer dan eens de vraag: “Mama, hoe maak je vrienden?”, zelfs nadat ze een jaar was gesprongen.",
      },
      {
        soort: "tekst",
        tekst:
          "Een andere verklaring voor de soms moeilijk lopende contacten met leeftijdsgenoten kunnen we vinden bij de vriendschapsverwachtingen. Op dat gebied lopen cognitief begaafde kinderen namelijk vaak voor op hun leeftijdsgenoten. Ze hebben op jonge leeftijd al veel hogere verwachtingen van vriendschap. Zo verwachten ze van een vriend of vriendin bijvoorbeeld waarden als trouw, loyaliteit en intimiteit, terwijl de andere kinderen nog in de fase zitten van wederzijdsheid: als ik naar jouw verjaardagsfeestje mag komen, dan mag jij naar het mijne komen. Het groot rechtvaardigheidsgevoel van hoogintelligente kinderen kan dan ook heel erg opspelen wanneer niet aan hun onuitgesproken hoge verwachtingen wordt voldaan.",
      },
      {
        soort: "tekst",
        tekst:
          "Deze belangrijke inzichten in het sociaal functioneren van cognitief begaafde kinderen hebben veel ogen geopend. Een onterechte diagnose van autisme is natuurlijk ook niet niets.",
      },
      {
        soort: "tekst",
        tekst:
          "Toch dienen we op te letten om hierdoor niet te gaan overcompenseren naar de andere kant. De combinatie van een hoge intelligentie met autisme komt wel degelijk voor. En misschien net iets vaker dan we momenteel vermoeden.",
      },
      { soort: "kop", tekst: "Het maatpak-effect" },
      {
        soort: "tekst",
        tekst:
          "We stellen vast dat er zich bij de combinatie van autisme en cognitieve begaafdheid een interessant fenomeen voordoet. Laat het ons even het maatpak-effect noemen.",
      },
      {
        soort: "tekst",
        tekst:
          "Wat houdt dit fenomeen in? Wel, cognitief begaafde kinderen met autisme slagen er net dankzij hun grote intelligentie vaak in om toch op een aanvaardbare manier aan alle normen te voldoen. Zo meten ze zichzelf als het ware een maatpak aan om erbij te horen. Door goed te observeren en te kopiëren, én dankzij hun fenomenale geheugen, slagen deze kinderen er op een briljante manier in hun maatpak te perfectioneren en aldus hun autisme te camoufleren.",
      },
      {
        soort: "tekst",
        tekst:
          "Helaas lukt dit niet zonder hier enorm hard mee bezig te zijn en er heel veel energie in te investeren. Binnenin dat maatpak voelen deze kinderen zich echter vaak onzeker, angstig en anders. Meer en meer raken ze verwijderd van hun eigen ik. Hoe ouder het kind, hoe groter de eisen van de omgeving. Hoe groter de eisen van de omgeving, hoe meer energie deze kinderen in het onderhouden en aanpassen van hun maatpak moeten steken.",
      },
      {
        soort: "citaat",
        tekst:
          "Degenen die het meeste energie steken in hun maatpak, worden vaak het minste gezien, begrepen en dus ook het minste ondersteund.",
      },
      {
        soort: "tekst",
        tekst:
          "Nochtans hebben deze kinderen wel degelijk ondersteuning nodig. Door hun significant andere manier van prikkelverwerking en van denken in het algemeen, lopen deze leerlingen voortdurend tegen hun grenzen aan.",
      },
      {
        soort: "tekst",
        tekst:
          "Je krijgt aldus kinderen die, al dan niet zwaar, onderpresteren, doodmoe zijn, op de toppen van hun tenen lopen, thuis moeten ontladen of niet meer van hun scherm af te krijgen zijn, of zelfs kinderen die kampen met een burn-out en niet meer in staat zijn om naar school te gaan. Deze kinderen en hun ouders krijgen vaak nog een pakje schuld bovenop hun maatpak, want ze zijn toch intelligent genoeg? Daar kan het niet aan liggen!",
      },
      {
        soort: "tekst",
        tekst:
          "Autisme komt wel degelijk voor in combinatie met een hoge begaafdheid. En daar dienen we heel erg attent op te zijn. Misschien is het wel net binnen deze doelgroep van cognitief begaafde kinderen het meest noodzakelijk om autisme actief op te gaan sporen. Zodat we deze kinderen én hun omgeving kunnen ontschuldigen, en tegelijkertijd de hulp bieden die ze broodnodig hebben om zichzelf, met hun cognitieve begaafdheid, in de wereld te zetten.",
      },
      {
        soort: "kop",
        tekst: "Waarom autisme zo vaak verkeerd gediagnosticeerd wordt",
      },
      {
        soort: "tekst",
        tekst:
          "Wat maakt dat autisme nog zo vaak verkeerd gediagnosticeerd wordt, en dit langs beide kanten? Momenteel is de diagnose van autisme voornamelijk een gedragsdiagnose, een diagnose die gebaseerd wordt op hoe kinderen zich gedragen.",
      },
      {
        soort: "tekst",
        tekst:
          "Bij cognitief begaafde kinderen is het gedrag echter geen correcte graadmeter voor het al dan niet aanwezig zijn van autisme. Zoals hierboven beschreven werd, kan gedrag dat op autisme lijkt andere oorzaken hebben. Evengoed kan het zijn dat er autisme aanwezig is zonder dat er opvallend autistisch gedrag opgemerkt wordt. Integendeel, soms zijn het net de kinderen die het meest binnen de lijnen lijken te kleuren, die het meest worstelen met hun anders zijn en al hun moeilijkheden internaliseren.",
      },
      {
        soort: "tekst",
        tekst:
          "Beter dan naar het gedrag van kinderen te kijken, kan gekeken worden naar wat aan de basis ligt van autisme. Dat is enerzijds een sensorische over- en onderreactiviteit en anderzijds een andere informatieverwerking die we kunnen benoemen als autistisch denken. Door via gerichte testing op zoek te gaan naar eventuele tekortkomingen in de centrale coherentie, in de theory of mind én in de executieve functies krijg je niet enkel uitsluitsel over het al dan niet aanwezig zijn van autistisch denken, maar kun je ook gericht de moeilijkheden en de ondersteuningsnood van het individuele kind in kaart brengen.",
      },
      {
        soort: "tekst",
        tekst:
          "Autisme is wel degelijk een beperking binnen onze huidige, niet altijd autismevriendelijke maatschappij. Het is helaas ook een erg onzichtbare beperking, zeker bij personen die cognitief begaafd zijn en zichzelf een perfect gekopieerd maatpak aangemeten hebben.",
      },
      {
        soort: "tekst",
        tekst:
          "Op tijd herkenning, erkenning en gerichte ondersteuning krijgen, kan een wereld van verschil maken voor een kind. Tot zolang onze maatschappij er niet in slaagt op gebied van onderwijs onvoorwaardelijk naar de individuele noden van elk kind te kijken, zal de diagnose van autisme dan ook een belangrijke stap zijn voor de gezonde ontwikkeling van het kind met autisme. Zodat het aan de wereld ook zijn sterktes kan laten zien!",
      },
      { soort: "tekst", tekst: "Katrien Volckaert" },
      {
        soort: "knop",
        tekst: "Naar katrienvolckaert.be",
        link: "https://www.katrienvolckaert.be",
      },
    ],
  },
  {
    slug: "onze-wereld",
    titel:
      "Onze wereld: een verhaal van liefde, complexiteit en onzichtbare kracht",
    datum: "2026-02-09",
    auteur: "Kim",
    labels: ["persoonlijk"],
    samenvatting:
      "Hoogbegaafdheid, autisme en een lichaam dat zijn eigen weg gaat. Kim zet een raam open naar een wereld die vaak achter gesloten deuren blijft.",
    blokken: [
      {
        soort: "afbeelding",
        bestand: "onze-wereld-kim-en-mats.jpg",
        beschrijving:
          "Kim en haar zoon Mats, wang tegen wang, allebei lachend.",
      },
      {
        soort: "tekst",
        tekst:
          "Hallo lieve lezer, welkom in ons leven. Ik schrijf deze woorden niet als expert, maar als mens. Als moeder. Als partner. Als iemand die gelooft dat echte verbinding begint bij eerlijke verhalen. Dit is ons verhaal, een verhaal dat ik deel uit liefde en uit noodzaak. Uit liefde voor mijn gezin, en uit de noodzaak om te laten zien hoe het écht is. Om een raam open te zetten naar een wereld die vaak achter gesloten deuren blijft.",
      },
      {
        soort: "kop",
        tekst: "Wie wij zijn: HB, ASS en een lichaam dat zijn eigen weg gaat",
      },
      {
        soort: "tekst",
        tekst:
          "In ons gezin draait het om termen die meer zijn dan alleen labels. HB (hoogbegaafdheid) en ASS (autismespectrumstoornis) zijn geen beperkingen, maar wel sleutels tot begrip. Ze betekenen een intense manier van zijn: diep voelen, sterk nadenken, behoefte aan duidelijkheid, en breinen die zelden stoppen. Voor onze zoon Mats gaat dit nog een laag dieper: hij heeft het label UHB (uiterst hoogbegaafd) met een disharmonisch profiel. Zijn ontwikkeling loopt niet synchroon; op sommige vlakken denkt hij als een filosoof, op andere vlakken heeft hij de ondersteuning nodig die past bij zijn leeftijd en ASS. Het is een complexe, unieke combinatie.",
      },
      {
        soort: "tekst",
        tekst:
          "Maar ons verhaal heeft nog een andere, fysieke laag. Naast deze neurologische aspecten dragen wij lichamelijke uitdagingen met ons mee.",
      },
      {
        soort: "tekst",
        tekst:
          "Voor mij betekent dit een totale systeemziekte: hypermobiliteit, bindweefselaandoeningen, POTS (een vorm van dysautonomie) en DVN, wat staat voor dunnevezelneuropathie. Dit is een aandoening van de dunste zenuwvezels, die zorgt voor vaak hevige pijn, branderige sensaties en extreme vermoeidheid. Mijn gezondheid fluctueert van invaliderend tot bijna normaal, vaak zonder waarschuwing.",
      },
      {
        soort: "tekst",
        tekst:
          "Onze zoon Mats draagt zijn eigen zware last: een primaire immuundeficiëntie. Zijn lichaam kan niet zelf voldoende afweer opbouwen. Twee keer per week krijgt hij levensnoodzakelijke infusen, thuis gegeven. Door mij en door thuisverpleging. Onze woonkamer is daardoor soms een behandelkamer. Het is zorg verlenen met een moederhart, gedragen door een lichaam dat zelf ook vaak protesteert.",
      },
      { soort: "kop", tekst: "De onzichtbare, dubbele last" },
      {
        soort: "tekst",
        tekst:
          "De combinatie is wat ons leven intens maakt. Een hooggevoelig brein dat alles intens waarneemt, in een lichaam dat intense pijn of dysfunctie signaleert. Een brein dat behoefte heeft aan voorspelbaarheid, in een lichaam dat onvoorspelbaar is. De zorg voor een chronisch ziek kind, terwijl je zelf ook worstelt met je grenzen.",
      },
      {
        soort: "tekst",
        tekst:
          "De belasting is niet alleen mentaal, prikkels reguleren en overleven in een wereld die niet voor jou is ontworpen, maar ook puur fysiek: de uitputting van ziek zijn, pijn hebben, behandelingen geven, en herstellen. Het is een leven waarin vermoeidheid een te zwak woord is voor de diepe uitputting die soms komt aanwaaien.",
      },
      {
        soort: "kop",
        tekst: "En toch kiezen we voor lachen, verbinding en gelijkwaardigheid",
      },
      {
        soort: "tekst",
        tekst:
          "Maar, en dit is het belangrijkste, dit verhaal gaat niet alleen over last. Het gaat over veerkracht.",
      },
      {
        soort: "tekst",
        tekst:
          "Het gaat over hoe wij, te midden van ziekenhuismateriaal, infusen, pijnlijke dagen en overprikkelde momenten, nog steeds lachen. Hoe we samen op de bank een film kijken als alles even te veel is. Hoe Mats tijdens zijn infuusjes de grappigste vragen stelt over het universum. Hoe we de kleine overwinningen vieren: een dag zonder koorts, een goed gesprek, een moment van begrip zonder woorden.",
      },
      {
        soort: "tekst",
        tekst:
          "We blijven verbinden, met elkaar en met de wereld. We blijven gelijkwaardig. Ons leven is anders, maar niet minder waardevol. Onze ervaringen zijn intens, maar brengen een diep begrip van wat écht belangrijk is.",
      },
      { soort: "kop", tekst: "Waarom ik dit deel: omdat praten moet" },
      {
        soort: "tekst",
        tekst:
          "Dit is mijn diepste drijfveer: ik wil dat meer mensen kennismaken met de échte betekenis van leven met complexe uitdagingen. Niet de karikaturen, maar het echte, dagelijkse leven. Met zijn lichtpunten en zijn schaduwkanten.",
      },
      {
        soort: "tekst",
        tekst:
          "Ik schrijf omdat erover praten mag. Sterker nog: het moet. Niet om zielig gevonden te worden, maar om gezien te worden in je volledige mens-zijn. Om de last te delen, zodat je hem niet alleen hoeft te dragen. Om te laten zien dat het niet overal gemakkelijk is, en dat het oké is om dat te zeggen.",
      },
      {
        soort: "citaat",
        tekst:
          "De stilte rond complexe, chronische aandoeningen kan eenzaam maken. Ik breek die stilte, voor ons en voor iedereen die zich herkent.",
      },
      { soort: "kop", tekst: "Mijn visie en hoop" },
      { soort: "tekst", tekst: "Met dit verhaal hoop ik:" },
      {
        soort: "lijst",
        punten: [
          { tekst: "Een eerlijk en volledig beeld te schetsen." },
          { tekst: "Herkenning te bieden aan wie in eenzelfde bootje zit." },
          {
            tekst: "Begrip te kweken bij familie, vrienden en de samenleving.",
          },
          {
            tekst:
              "De kracht en veerkracht te tonen die schuilgaat achter de uitdagingen.",
          },
          {
            tekst: "Te bewijzen dat kwetsbaarheid en kracht hand in hand gaan.",
          },
        ],
      },
      {
        soort: "tekst",
        tekst:
          "Ik nodig je uit om met mildheid naar jezelf en anderen te kijken. Om te vragen: “Hoe is het vandaag echt met je?” En om te luisteren zonder meteen oplossingen aan te dragen. Soms is er alleen maar behoefte aan erkenning: “Dat klinkt zwaar. Ik hoor je.”",
      },
      { soort: "kop", tekst: "Tot slot" },
      {
        soort: "tekst",
        tekst:
          "Dankjewel dat je ons verhaal leest. Door het te delen, maak je het lichter. Jij maakt het mogelijk dat we ons minder alleen voelen. Voor iedereen die zelf een complexe weg bewandelt: je bent niet alleen. Deel je verhaal wanneer je kunt, in je eigen tempo.",
      },
      {
        soort: "tekst",
        tekst:
          "En vergeet niet: zelfs op de zwaarste dagen is er ruimte voor een lach, hoe klein ook. Dat is ons geheim. Dat is onze kracht.",
      },
      { soort: "tekst", tekst: "Met een hart vol realisme, moed en hoop, Kim" },
      {
        soort: "tekst",
        tekst:
          "PS: voel je vrij om te reageren, een vraag te stellen of je eigen ervaring te delen. Deze ruimte is er om te leren, te steunen en te groeien, samen.",
      },
      { soort: "knop", tekst: "Deel je verhaal", link: "/contact" },
    ],
  },
  {
    slug: "na-de-school-en-in-de-vakantie",
    titel: "Na de school en in de vakantie: dit doen we samen",
    datum: "2026-09-20",
    auteur: "Connectopia",
    labels: ["aanbod", "naschools", "kampen", "techniek"],
    samenvatting:
      "Een rondleiding door onze plusklas, de twee pluswerkingen, de Young Engineers-lessen en de vakantiekampen. Met foto's van wat er op zo'n dag gebeurt.",
    blokken: [
      {
        soort: "tekst",
        tekst:
          "Nieuwsgierigheid stopt niet als de schoolbel gaat. Bij heel wat kinderen begint ze dan pas: de vragen die ze de hele dag opgespaard hebben, het boek dat nog openligt, het ding dat ze willen bouwen. Daar maken wij tijd voor. Tijdens de week, op woensdag- en zaterdagvoormiddag, en in elke schoolvakantie.",
      },
      {
        soort: "afbeelding",
        bestand: "naschools-natuurkunde.jpg",
        beschrijving:
          "Een jongen houdt een visuele gids over natuurkunde open en kijkt over het boek heen.",
        bijschrift: "Nieuwsgierigheid houdt zich niet aan een uurrooster.",
        klein: true,
      },
      { soort: "kop", tekst: "De plusklas en de twee pluswerkingen" },
      {
        soort: "tekst",
        tekst:
          "Onze plusklas en pluswerkingen zijn er voor kinderen van 6 tot 12 jaar die net dat beetje extra uitdaging, begrip of ruimte nodig hebben. We werken in kleine groepjes, met aandacht voor het proces, de samenwerking en het plezier in leren.",
      },
      {
        soort: "lijst",
        punten: [
          {
            titel: "Externe plusklas",
            tekst:
              "Dinsdag van 9 tot 15 uur in Atheneum Hasselt, in drie trajecten van telkens tien dagen. Een veilige haven waar gelijkgestemde kinderen samen een diepgaand leertraject aangaan.",
          },
          {
            titel: "Pluswerking woensdag",
            tekst:
              "Woensdagvoormiddag van 9 tot 12 uur in Genk T2 Campus. Meer schoolse uitdaging en voorbereiding op de examencommissie, voor schoolgaande kinderen en voor kinderen in thuisonderwijs.",
          },
          {
            titel: "Pluswerking zaterdag",
            tekst:
              "Zaterdagvoormiddag van 9 tot 12 uur in de Vilderstraat 28 in Hasselt. Creativiteit en techniek laten samenkomen, met veel ruimte om te experimenteren.",
          },
        ],
      },
      {
        soort: "tekst",
        tekst:
          "Later instappen kan, ook in oktober is er nog plaats. En wie eerst wil proeven: je kind mag vrijblijvend een gratis proefles meedoen, zodat het zelf voelt of de groep past voor je iets vastlegt.",
      },
      {
        soort: "afbeelding",
        bestand: "naschools-knutselmateriaal.jpg",
        beschrijving:
          "Een tafel vol knutselmateriaal: blikken, eierdozen, klei, kartonnen rollen en bekertjes, onder een muur met handgeschreven tekst.",
        bijschrift:
          "“Wat zou jij hiermee creëren?” De vraag staat letterlijk op de muur.",
      },
      { soort: "kop", tekst: "Young Engineers, samen met ons" },
      {
        soort: "tekst",
        tekst:
          "Voor onze naschoolse activiteiten rond STEM en techniek werken we samen met Young Engineers. Ontdekken, experimenteren, bouwen en vooral plezier maken: met LEGO® echte uitdagingen aangaan, samenwerken en trots zijn op je werk.",
      },
      {
        soort: "lijst",
        punten: [
          {
            tekst: "Dinsdag van 15u20 tot 16u35 in Atheneum Hasselt.",
          },
          {
            tekst:
              "Woensdag van 13u tot 14u15 of van 14u15 tot 15u30 in Genk T2 Campus.",
          },
          {
            tekst:
              "Zaterdag van 13u tot 14u15 of van 14u15 tot 15u30 in de Vilderstraat 28 in Hasselt.",
          },
          { tekst: "Eén les duurt 1u15. Instappen kan het hele jaar door." },
        ],
      },
      {
        soort: "afbeelding",
        bestand: "naschools-bouwen.jpg",
        beschrijving:
          "Een kind bouwt aan tafel een wagentje met een motor, naast de bouwdoos en het werkboekje.",
        bijschrift: "Van het plan in het boekje naar iets dat echt rijdt.",
      },
      {
        soort: "afbeelding",
        bestand: "naschools-lego-doos.jpg",
        beschrijving:
          "Een geopende bouwdoos met blokken, wielen, assen, tandwielen en een motor.",
        bijschrift:
          "In elke doos zit een motor. Wat ermee gebeurt, kiest het kind zelf.",
        klein: true,
      },
      { soort: "kop", tekst: "En in elke schoolvakantie: de kampen" },
      {
        soort: "tekst",
        tekst:
          "Tijdens de herfst-, kerst-, krokus-, paas- en zomervakantie organiseren we kampen: een vakantie vol nieuwsgierigheid, creativiteit, techniek en uitdaging, in kleine groepen en met aandacht voor ieder kind.",
      },
      {
        soort: "lijst",
        punten: [
          { tekst: "Ontdekken: nieuwe dingen onderzoeken en vragen stellen" },
          {
            tekst:
              "Maken en experimenteren: van een idee naar iets dat écht werkt",
          },
          {
            tekst: "Creatief denken: eigen oplossingen bedenken en uitproberen",
          },
          {
            tekst:
              "Hun brein uitdagen: spelen, denken, bouwen en leren combineren",
          },
          {
            tekst:
              "Samen groeien: in kleine groepen en met aandacht voor ieder kind",
          },
        ],
      },
      {
        soort: "tekst",
        tekst:
          "De plaatsen zijn beperkt, dus reserveer tijdig. Nieuwe kampen en thema's maken we telkens bekend via de website en onze sociale media.",
      },
      { soort: "knop", tekst: "Bekijk het volledige aanbod", link: "/aanbod" },
    ],
  },
];

export const berichtenOpDatum = [...berichten].sort((a, b) =>
  b.datum.localeCompare(a.datum),
);
