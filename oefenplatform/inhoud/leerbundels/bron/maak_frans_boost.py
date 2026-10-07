# -*- coding: utf-8 -*-
"""De leerbundels voor Frans op 🚀 Boost doorstroom-niveau.

Gebaseerd op de twee vakfiches Frans van de 2de graad doorstroomfinaliteit,
geldig vanaf 1 januari 2027. Frans 1 is een digitaal examen van 120 minuten
over lezen en luisteren; Frans 2 bestaat uit een spreekopdracht die je thuis
opneemt, twee schrijfopdrachten op het digitale examen, en een gesprek van tien
minuten. Allebei de fiches gelden voor dezelfde vier richtingen: economische
wetenschappen, humane wetenschappen, natuurwetenschappen en Latijn. Het
ERK-niveau is B1.

De woordvelden en de grammaticalijst achter de twee examens zijn woord voor
woord dezelfde, dus staan ze hier één keer. Wat hier níét in zit, is luisteren,
spreken en het gesprek: die vragen geluid en een gesprekspartner. Achteraan
elke bundel staat daarom hetzelfde kader met een opdracht die je buiten het
scherm doet, telkens een andere en telkens bij het thema van de bundel.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/frans.json`
doet daar het voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie. Dat is nodig: Frans van Boost dubbele finaliteit heeft bundels met
bijna dezelfde titels, en Beheer → Leerstof leest de categorie uit de
bestandsnaam.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Frans"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
NIVEAU = "-boost-doorstroom"
tabel = bundel.tabel

BUNDELS = {}


def buiten(opdracht):
    """Het vaste slotkader: wat je niet achter een scherm leert."""
    return dict(kop="Oefen dit ook buiten het scherm", blokken=[
        ("p", "Hier oefen je lezen, schrijven, woordenschat en grammatica. Maar het examen "
              "<strong>Frans 1</strong> is voor de helft <strong>luisteren</strong>, en "
              "<strong>Frans 2</strong> bestaat naast de twee schrijfopdrachten uit een "
              "<strong>spreekopdracht</strong> die je thuis opneemt en een "
              "<strong>gesprek van tien minuten</strong>. Die drie leer je niet achter een "
              "scherm, maar door Frans te horen en zelf Frans te praten, ook als het hakkelt."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer en let daarna "
                  "op wat je miste of niet gezegd kreeg. Dat is precies je volgende oefening."),
    ])


# ───────────────────────── 1. Een Franse tekst analyseren
BUNDELS["een-franse-tekst-analyseren" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Een Franse tekst analyseren",
    onder="Het onderwerp en de hoofdgedachte vinden, gegevens uit een tekst halen, en horen wat de schrijver bedoelt.",
    secties=[
        dict(kop="Wat vraagt dit examen van je?", blokken=[
            ("p", "Het examen <strong>Frans 1</strong> duurt 120 minuten en bestaat volledig uit "
                  "<strong>lezen</strong> en <strong>luisteren</strong>. Lezen is dus het zwaarste "
                  "onderdeel dat je hier kan inoefenen, en wie vlot leest, herkent dezelfde woorden "
                  "ook terug als hij ze hoort."),
            ("p", "Het ERK-niveau is <strong>B1</strong>, een stap boven de eerste graad. Begrijpen "
                  "wat er staat is niet genoeg meer: je moet ook <strong>verbanden leggen</strong> "
                  "tussen delen van een tekst, en informatie halen uit wat er <strong>niet "
                  "letterlijk</strong> staat."),
            ("kader", "Elke leesvraag hieronder staat op een echt Frans tekstje. Een vraag over "
                      "lezen zonder tekst is geen leesvraag. Lees het tekstje dus eerst helemaal, "
                      "ook als de vraag maar naar één cijfer vraagt."),
        ]),
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Drie dingen die op elkaar lijken en die je uit elkaar moet houden. Het "
                  "<strong>onderwerp</strong> is waarover de tekst gaat, en dat zeg je in "
                  "<strong>enkele woorden</strong>: 'over het uitlenen van elektrische fietsen'. De "
                  "<strong>hoofdgedachte</strong> is de belangrijkste boodschap, en die zeg je in "
                  "<strong>een hele zin</strong>: 'Wie een fiets mag proberen, koopt er vaak zelf "
                  "een.' De <strong>hoofdpunten</strong> zijn de elementen die die hoofdgedachte "
                  "<strong>ondersteunen</strong>."),
            ("fig", svg.kernpiramide(),
             "Bovenaan het onderwerp in enkele woorden, daaronder de hoofdgedachte in één zin, onderaan de punten die haar dragen."),
            ("p", "Antwoord op een vraag naar de hoofdgedachte dus nooit met een los woord, en op een "
                  "vraag naar het onderwerp nooit met een heel verhaal. Vind je de hoofdgedachte niet "
                  "meteen, lees dan de <strong>titel</strong> en de <strong>laatste zin</strong> "
                  "opnieuw: heel vaak werkt een tekst naar zijn slotzin toe."),
            ("kader", "<strong>Doe het eens op een echte tekst.</strong> <em>Depuis trois ans, la "
                      "ville de Namur prête des vélos électriques aux habitants qui travaillent à "
                      "plus de cinq kilomètres de chez eux. Le prêt dure six semaines et ne coûte "
                      "rien. L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les "
                      "gens essayer. Après l'essai, un habitant sur trois achète son propre "
                      "vélo.</em><br>"
                      "<strong>Onderwerp:</strong> het uitlenen van elektrische fietsen. "
                      "<strong>Hoofdgedachte:</strong> wie zo'n fiets zes weken mag proberen, koopt "
                      "er vaak zelf een. <strong>Hoofdpunten:</strong> het leent al drie jaar, het "
                      "geldt voor wie verder dan vijf kilometer van zijn werk woont, het kost niets, "
                      "en een inwoner op drie koopt er daarna zelf een."),
        ]),
        dict(kop="De teksten waarop je dit oefent", blokken=[
            ("p", "De vragen van dit hoofdstuk staan op zes korte teksten. Lees ze hier eerst "
                  "rustig, dan herken je ze straks meteen terug."),
            ("kader", "<strong>Een nieuwsbericht.</strong> <em>Hier soir, un orage violent a traversé "
                      "le sud du pays. Plusieurs routes ont été fermées pendant deux heures. Il n'y a "
                      "pas de blessés, mais une centaine de maisons sont restées sans électricité "
                      "jusqu'à ce matin.</em><br>Gisteravond trok een hevig onweer over het zuiden van "
                      "het land. Verschillende wegen waren twee uur lang afgesloten. Er vielen geen "
                      "gewonden, maar een honderdtal huizen zat tot vanochtend zonder stroom."),
            ("kader", "<strong>Een stukje over een schoolkantine.</strong> <em>Notre école a changé le "
                      "menu de la cantine en septembre. Il y a maintenant un plat végétarien tous les "
                      "jours et moins de viande. Au début, beaucoup d'élèves se sont plaints. Trois "
                      "mois plus tard, la cantine sert deux fois plus de repas qu'avant. Le cuisinier "
                      "explique que le secret n'est pas le menu, mais le goût.</em><br>Onze school "
                      "veranderde in september het menu van de kantine: elke dag een vegetarisch "
                      "gerecht en minder vlees. In het begin klaagden veel leerlingen. Drie maanden "
                      "later serveert de kantine dubbel zoveel maaltijden als voordien. De kok legt "
                      "uit dat het geheim niet het menu is maar de smaak."),
            ("kader", "<strong>Een stagebrief.</strong> <em>Madame, Monsieur, Je suis élève en "
                      "quatrième année et je cherche un stage de deux semaines au mois de février. Je "
                      "m'intéresse beaucoup au travail de votre laboratoire. Je suis libre tous les "
                      "jours et je peux venir me présenter quand vous voulez. Je vous remercie "
                      "d'avance pour votre réponse.</em><br>De schrijver zit in het vierde jaar, zoekt "
                      "een stage van twee weken in februari, is elke dag vrij en wil zich komen "
                      "voorstellen wanneer het past."),
            ("kader", "<strong>Een stukje over een markt.</strong> <em>Le samedi matin, la place est "
                      "pleine. On y vend des légumes, du fromage et des fleurs. Les prix sont plus "
                      "élevés qu'au supermarché, mais les clients reviennent chaque semaine. « Ici, je "
                      "sais qui a cultivé mes tomates », dit une dame de soixante ans.</em><br>Op "
                      "zaterdagochtend is het plein vol. Er worden groenten, kaas en bloemen verkocht. "
                      "De prijzen liggen hoger dan in de supermarkt, en toch komen de klanten elke "
                      "week terug."),
            ("kader", "<strong>Een stukje van een forum.</strong> <em>Marie : J'ai acheté ce casque il "
                      "y a deux mois et le son est déjà mauvais d'un côté. Quelqu'un a le même "
                      "problème ? — Yacine : Chez moi, c'était le câble. Je l'ai remplacé pour douze "
                      "euros et tout fonctionne. — Lila : Moi, j'ai renvoyé le mien. La garantie dure "
                      "deux ans, profites-en.</em><br>Marie heeft een koptelefoon die aan één kant "
                      "slecht klinkt. Yacine verving bij hem de kabel voor twaalf euro, Lila stuurde "
                      "de hare terug met een beroep op de garantie van twee jaar."),
        ]),
        dict(kop="Gegevens uit de tekst halen", blokken=[
            ("p", "De praktische vraag bij elke tekst is: <strong>informatie selecteren</strong>. Dan "
                  "hoef je de tekst niet helemaal te begrijpen, je moet er één gegeven uit halen — "
                  "een aantal weken, een maand, een aantal huizen, een prijs. Zoek dan naar de "
                  "<strong>vorm</strong> die je nodig hebt, en niet naar alle woorden."),
            ("p", "Let op de Franse <strong>getalwoorden</strong>, want die staan er voluit: "
                  "<em>six semaines</em> is zes weken, <em>trois mois plus tard</em> is drie maanden "
                  "later, <em>deux heures</em> is twee uur, <em>une dame de soixante ans</em> is een "
                  "dame van zestig. En <em>une centaine de maisons</em> is een honderdtal huizen: "
                  "ongeveer honderd, niet precies honderd."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["prêter, le prêt dure", "uitlenen, het uitlenen duurt"],
                ["ne coûte rien", "kost niets"],
                ["un habitant sur trois", "een inwoner op drie"],
                ["une centaine de", "een honderdtal, ongeveer honderd"],
                ["deux fois plus que", "dubbel zoveel als"],
                ["plus élevé que", "hoger dan"],
            ]), "Zes manieren waarop een Franse tekst een hoeveelheid uitdrukt."),
        ]),
        dict(kop="Tussen de regels lezen", blokken=[
            ("p", "Op B1-niveau staat het antwoord vaak niet letterlijk in de tekst. Wat je "
                  "<strong>afleidt</strong>, moet er wel uit volgen. <em>Un habitant sur trois "
                  "achète son propre vélo</em>: als één op de drie er een koopt, kopen de andere "
                  "<strong>twee op de drie</strong> er dus geen. Dat staat er niet, en toch is het "
                  "juist."),
            ("p", "Pas op voor <strong>ontkenningen</strong>, want die draaien een hele zin om. "
                  "<em>Il n'y a pas de blessés</em> betekent dat er juist <strong>géén</strong> "
                  "gewonden zijn. <em>Je ne fais pas d'envoi</em> betekent dat de verkoper niet "
                  "verstuurt. Lees <em>ne … pas</em> dus altijd mee."),
            ("p", "En let op <strong>wie wat zegt</strong>. In een forumgesprek komen drie mensen aan "
                  "het woord: <em>Marie</em> heeft een koptelefoon waarvan het geluid aan één kant "
                  "slecht is, <em>Yacine</em> verving bij hem de kabel voor twaalf euro, en "
                  "<em>Lila</em> stuurde de hare terug met een beroep op de garantie van twee jaar. "
                  "Wie dat door elkaar haalt, antwoordt fout op een vraag die hij nochtans begreep."),
            ("weetje", "In <em>« Ici, je sais qui a cultivé mes tomates »</em> zegt de dame dat ze "
                       "weet wie haar tomaten gekweekt heeft. Ze kweekt ze dus niet zelf: "
                       "<em>cultiver</em> staat in de verleden tijd en gaat over iemand anders."),
        ]),
        dict(kop="De bedoeling en de toon van de schrijver", blokken=[
            ("p", "Twee vragen die er bij elke tekst bij kunnen komen. De eerste is de "
                  "<strong>bedoeling</strong>: waarom is deze tekst geschreven? Een stad die haar "
                  "proef afsluit met een cijfer dat goed nieuws is, wil je <strong>overtuigen</strong> "
                  "om die fiets eens te proberen. Dat cijfer staat niet toevallig als laatste."),
            ("p", "De tweede is de <strong>toon</strong>. Een tekst die alleen op een rij zet wat er "
                  "veranderde en wat het opbracht, is <strong>rustig vaststellend</strong>: er staat "
                  "geen enkel oordeel in. Vergelijk dat met <strong>boos</strong>, "
                  "<strong>bezorgd</strong> of <strong>spottend</strong>, waar je telkens de woorden "
                  "van het oordeel zelf kan aanwijzen. Kan je ze niet aanwijzen, dan is de toon "
                  "neutraal."),
            ("fig", svg.registerschaal(zinnen=("Salut, tu m'aides ?", "Tu peux m'aider ?",
                                            "Pourriez-vous m'aider ?")),
             "Van heel formeel tot heel familiair; de aanspreking verraadt meteen waar een tekst zit."),
            ("p", "De toon hangt ook samen met het <strong>register</strong>. "
                  "<em>Madame, Monsieur</em> als aanhef, <em>vous</em> als aanspreking en <em>je vous "
                  "remercie d'avance pour votre réponse</em> als slot: dat is een "
                  "<strong>formele brief</strong>. Dezelfde brief met <em>tu</em> zou ineens veel te "
                  "familiair klinken."),
        ]),
        dict(kop="Verbanden tussen de zinnen", blokken=[
            ("p", "Een tekst is geen stapel losse zinnen. De kleine woordjes leggen de verbanden, en "
                  "op dit niveau wordt daar uitdrukkelijk naar gevraagd."),
            ("fig", tabel(["Signaal", "Welk verband"], [
                ["ne … pas …, mais …", "een tegenstelling tussen twee dingen: niet dit, maar dat"],
                ["mais", "een maar: het zwakt af wat er net gezegd is"],
                ["donc, c'est pourquoi", "een gevolg"],
                ["parce que, car", "een oorzaak of een reden"],
                ["par exemple, ainsi", "een voorbeeld bij de vorige zin"],
                ["en septembre, au début, trois mois plus tard", "een tijdsverloop: de gebeurtenissen na elkaar"],
            ]), "Zes signalen en het verband dat ze aankondigen."),
            ("p", "<em>L'idée n'est pas de donner un vélo à tout le monde, mais de laisser les gens "
                  "essayer</em> zet dus twee <strong>bedoelingen</strong> tegenover elkaar. En "
                  "<em>Il n'y a pas de blessés, mais une centaine de maisons sont restées sans "
                  "électricité</em> begint geruststellend en komt met dat ene <em>mais</em> toch bij "
                  "een nadeel uit."),
            ("p", "Ook een <strong>zin met een cijfer</strong> of een <strong>citaat</strong> heeft "
                  "een taak in de tekst. <em>Trois mois plus tard, la cantine sert deux fois plus de "
                  "repas qu'avant</em> komt na de klachten, en laat dus zien dat de verandering "
                  "<strong>gelukt</strong> is. Het citaat van de dame van zestig komt meteen na de "
                  "zin over de hogere prijzen, en legt dus uit <strong>waarom</strong> de klanten die "
                  "prijs toch betalen. Vraag je bij zo'n zin altijd af: wat zou er wegvallen als ze "
                  "er niet stond?"),
        ]),
        dict(kop="Tekstsoorten herkennen, en twee teksten vergelijken", blokken=[
            ("p", "Je hoeft de soort niet te raden: elke tekstsoort heeft haar eigen vorm. Een "
                  "<strong>kort nieuwsbericht</strong> opent met een tijdsbepaling (<em>hier "
                  "soir</em>), geeft feiten en cijfers, en heeft geen mening en geen aanspreking. Een "
                  "<strong>formele brief</strong> heeft een aanhef en een beleefdheidsformule. Een "
                  "<strong>forum</strong> is een vraag met antwoorden van verschillende mensen. Een "
                  "<strong>reclameboodschap</strong> wil je overhalen en een "
                  "<strong>handleiding</strong> zegt in welke orde je iets doet."),
            ("p", "Twee teksten over hetzelfde <strong>vergelijken</strong> hoort er op dit niveau "
                  "ook bij. Een stukje over een markt en een stukje van een forum gaan allebei over "
                  "kopen, maar het ene <strong>beschrijft</strong> wat er te zien is, en op het "
                  "andere <strong>geven</strong> mensen elkaar <strong>raad</strong>. Zoek bij zo'n "
                  "vraag dus niet het verschil in onderwerp, maar het verschil in wat de tekst "
                  "<em>doet</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["essayer, l'essai", "proberen, de proef"],
                ["se plaindre, une plainte", "klagen, een klacht"],
                ["un blessé, blesser", "een gewonde, verwonden"],
                ["profiter de", "gebruikmaken van, profiteren van"],
                ["un stage, être libre", "een stage, vrij zijn"],
                ["la garantie, renvoyer", "de garantie, terugsturen"],
            ]), "Zes woorden uit de teksten van dit hoofdstuk, met hun familie erbij."),
            ("weetje", "<em>Profites-en</em> is <em>profiter</em> in de gebiedende wijs met een "
                       "<em>en</em> erachter. Dat <em>en</em> verwijst naar waar je van profiteert — "
                       "hier naar de garantie van twee jaar."),
        ]),
        buiten("zoek een kort Frans nieuwsbericht op de radio of in een podcast, en vat het in twee "
               "Nederlandse zinnen samen: het onderwerp en de hoofdgedachte."),
    ],
)


# ───────────────────────── 2. Tekstsoorten, tekstverbanden en verwijswoorden
BUNDELS["tekstsoorten-tekstverbanden-en-verwijswoorden" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Tekstsoorten, tekstverbanden en verwijswoorden",
    onder="Zes soorten teksten en waaraan je ze herkent, de signaalwoorden die de draad van een tekst zichtbaar maken, en waarnaar ils, y en en verwijzen.",
    secties=[
        dict(kop="Zes soorten teksten", blokken=[
            ("p", "De vakfiche zet zes soorten teksten op een rij. Je herkent ze niet aan hun "
                  "onderwerp maar aan wat ze <strong>doen</strong>, en dat zie je meestal al aan de "
                  "eerste zinnen."),
            ("fig", tabel(["Soort", "Wat de tekst doet", "Voorbeelden"], [
                ["informatief", "informeren, uitleggen hoe iets werkt",
                 "een krantenartikel over de nieuwe treinkaart, een interview in een tijdschrift"],
                ["persuasief", "overtuigen of beïnvloeden", "een affiche, een reclameboodschap"],
                ["opiniërend", "een mening geven", "een hotelbeoordeling, een lezersbrief"],
                ["prescriptief", "zeggen wat je moet doen", "een recept, een bijsluiter, een schoolreglement"],
                ["narratief", "vertellen wat er gebeurd is", "een reisverslag, een getuigenis, een videoblog"],
                ["literair", "iets laten voelen met taal", "een gedicht, een lied, een strip, een kortverhaal"],
            ]), "De zes soorten uit de vakfiche, met de voorbeelden die de fiche zelf noemt."),
            ("p", "<strong>Persuasief</strong> is het woord dat je moet kennen voor een tekst die je "
                  "probeert te <strong>overtuigen of te beïnvloeden</strong>, en "
                  "<strong>prescriptief</strong> voor een tekst die je <strong>voorschrijft</strong> "
                  "wat je moet doen."),
            ("weetje", "Een opiniërende tekst mag wél feiten bevatten. <em>La chambre était propre et "
                       "le petit déjeuner correct</em> zijn feiten, maar <em>pour ce prix, je "
                       "m'attendais à mieux</em> en <em>je n'y retournerai pas</em> maken er een "
                       "mening van. Het gaat erom waarvoor de feiten dienen."),
        ]),
        dict(kop="Waaraan je de soort ziet", blokken=[
            ("p", "Een <strong>prescriptieve</strong> tekst staat in de "
                  "<strong>gebiedende wijs</strong>: <em>Épluchez quatre pommes de terre et "
                  "coupez-les en morceaux. Faites-les cuire vingt minutes dans l'eau bouillante. "
                  "Égouttez, puis écrasez-les avec un peu de lait chaud. Salez et servez tout de "
                  "suite.</em> Die bevelende vormen <em>épluchez, coupez, salez</em> zijn het "
                  "signaal, niet het onderwerp."),
            ("p", "Een <strong>persuasieve</strong> tekst gebruikt middelen om je over de streep te "
                  "trekken: <em>Ne jetez plus vos piles à la poubelle !</em> is een rechtstreeks "
                  "<strong>bevel aan de lezer</strong> met een <strong>uitroepteken</strong>, "
                  "<em>une seule pile pollue des milliers de litres d'eau</em> is een "
                  "<strong>groot getal</strong> dat de schade zichtbaar maakt, <em>Déposez-les "
                  "gratuitement dans le bac vert de votre magasin</em> zegt wat je dan wél moet "
                  "doen (breng ze gratis naar de groene bak van je winkel), en <em>un geste de "
                  "trois secondes, un fleuve sauvé</em> is een <strong>kort slotzinnetje met een "
                  "sterk beeld</strong> erin. Een opsomming van wetenschappelijke bronnen hoort er "
                  "net niet bij: dat is wat een informatieve tekst doet."),
            ("p", "Een <strong>opiniërende</strong> tekst heeft een <strong>ik</strong> met een "
                  "oordeel: <em>J'ai passé deux nuits dans cet hôtel. La chambre était propre et le "
                  "petit déjeuner correct, mais le bruit de la rue m'a réveillé chaque matin à cinq "
                  "heures. Pour ce prix, je m'attendais à mieux. Je n'y retournerai pas.</em>"),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["éplucher, couper en morceaux", "schillen, in stukken snijden"],
                ["l'eau bouillante, égoutter", "het kokende water, afgieten"],
                ["écraser, saler", "pletten, zouten"],
                ["jeter, une pile, le bac vert", "weggooien, een batterij, de groene bak"],
                ["polluer, un fleuve sauvé", "vervuilen, een gespaarde rivier"],
                ["le bruit de la rue, réveiller", "het straatlawaai, wekken"],
            ]), "Woorden uit het recept, de affiche en de beoordeling van dit hoofdstuk."),
        ]),
        dict(kop="Voor je de eerste zin leest", blokken=[
            ("p", "Drie hulpmiddelen brengen je volgens de fiche al vooruit nog vóór je begint: de "
                  "<strong>titel en de tussentitels</strong>, een <strong>foto of een tekening</strong> "
                  "erbij, en de woorden die <strong>vetgedrukt</strong> staan. De lengte van de laatste "
                  "alinea zegt je niets."),
            ("p", "Daarna helpt het <strong>communicatiemodel</strong>: van wie is deze tekst, waarom "
                  "is hij geschreven, en voor wie? Wie zich die drie vragen stelt, leest meteen "
                  "gerichter."),
            ("fig", svg.communicatiemodel(),
             "Zender, boodschap en ontvanger, met het kanaal, de context en het doel eromheen."),
            ("p", "Staat er een <strong>onbekend Frans woord</strong> in, dan leid je de betekenis "
                  "eerst <strong>af uit de context of uit de woordvorm</strong>. Het woordenboek komt "
                  "pas daarna: op een examen van 120 minuten heb je de tijd niet om elk woord op te "
                  "zoeken."),
        ]),
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Deze drie komen bij elke tekst terug. Het <strong>onderwerp</strong> bepalen "
                  "betekent: in <strong>één of enkele woorden</strong> zeggen waarover de tekst gaat. "
                  "De <strong>hoofdgedachte</strong> is de boodschap zelf, in een hele zin, en de "
                  "<strong>hoofdpunten</strong> zijn de elementen die ze <strong>dragen</strong>. Het "
                  "verschil zit dus niet in waar ze staan of in kort tegenover lang."),
            ("p", "<strong>Analyseren</strong> is meer dan letterlijk aanwijzen. Wat je afleidt, moet "
                  "uit de tekst volgen, maar het hoeft er niet woord voor woord in te staan. Dat is "
                  "precies wat B1 van je vraagt."),
        ]),
        dict(kop="Tekstverbanden: wat doet een alinea tegenover een andere?", blokken=[
            ("p", "Een <strong>tekstverband</strong> is de <strong>functie</strong> van een alinea "
                  "tegenover een andere alinea. Niet hoeveel zinnen ze telt, en niet in welke orde ze "
                  "op papier staat: wat ze <em>doet</em>. Geeft alinea 3 de "
                  "<strong>oorzaak</strong> van alinea 2, het <strong>gevolg</strong>, een "
                  "<strong>toelichting</strong>, een <strong>tegenstelling</strong>, of een "
                  "<strong>weerlegging</strong>?"),
            ("fig", svg.tekstopbouw([
                ("alinea 1", "de vaststelling: de bibliotheek sluit om achttien uur", 1.0),
                ("alinea 2", "de oorzaak: er is te weinig personeel 's avonds", 1.0),
                ("alinea 3", "de tegenstelling: op woensdag blijft ze wel open", 1.0),
                ("alinea 4", "het besluit: wie later wil, komt op woensdag", 1.0),
            ]), "Vier alinea's over hetzelfde onderwerp, elk met een andere functie."),
            ("weetje", "<strong>Alfabetische volgorde</strong> staat niet in de lijst van "
                       "tekstverbanden, en kan er ook niet in staan: dat zegt iets over de letters, "
                       "niet over de gedachtegang."),
        ]),
        dict(kop="Signaalwoorden: de draad zichtbaar maken", blokken=[
            ("p", "Signaalwoorden zijn de woordjes waarmee je de <strong>gedachtegang</strong> van een "
                  "tekst kan <strong>reconstrueren</strong>. Lees in een moeilijke tekst eerst alleen "
                  "die woorden, en je ziet de structuur al voor je de rest begrijpt."),
            ("fig", tabel(["Verband", "Frans"], [
                ["gevolg", "donc, alors, c'est pourquoi"],
                ["oorzaak of reden", "parce que, car"],
                ["tegenstelling", "mais, pourtant, par contre, en revanche, cependant — il fait froid mais le soleil brille"],
                ["volgorde", "d'abord, ensuite, puis, enfin"],
                ["voorbeeld", "par exemple, ainsi"],
                ["toevoeging of opsomming", "de plus, en outre, aussi"],
            ]), "Zes verbanden met de Franse woorden die ze aankondigen."),
            ("p", "<em>Il pleuvait, <strong>donc</strong> nous sommes restés à la maison</em> geeft "
                  "een <strong>gevolg</strong>; <em>Le train était en retard <strong>parce "
                  "qu'</strong>un arbre bloquait la voie</em> geeft een <strong>oorzaak</strong>. En "
                  "de volgorde van een uitleg is <em>d'abord, ensuite, enfin</em>: <em>D'abord, on "
                  "coupe les légumes. Ensuite, on les fait cuire.</em>"),
            ("p", "Twee valkuilen. <em>En revanche</em> lijkt op <em>par exemple</em> maar betekent "
                  "iets heel anders: het is <strong>daarentegen</strong>, net als <em>par contre</em>, "
                  "dus een tegenstelling. En <em>cependant</em> kondigt vaak een "
                  "<strong>uitzondering</strong> aan: <em>La bibliothèque ferme à dix-huit heures. "
                  "Cependant, le mercredi, elle reste ouverte jusqu'à vingt heures.</em>"),
            ("kader", "<strong>Grâce à of à cause de?</strong> Allebei geven ze een oorzaak, maar "
                      "<em>grâce à</em> noemt een <strong>goede</strong> oorzaak en <em>à cause "
                      "de</em> een <strong>slechte</strong>. <em>Grâce à son entraîneur, elle a "
                      "gagné</em> tegenover <em>À cause de la pluie, le match est annulé</em>. Bij een "
                      "staking is het dus <em>à cause de la grève</em>."),
        ]),
        dict(kop="Verwijswoorden: waarnaar wijst dat woordje terug?", blokken=[
            ("p", "Een tekst herhaalt niet graag. In de plaats daarvan verwijst hij terug, en jij moet "
                  "weten waarnaar. <em>Les élèves ont protesté. <strong>Ils</strong> voulaient garder "
                  "leur local.</em> <em>Ils</em> zijn <em>les élèves</em>."),
            ("fig", tabel(["Verwijswoord", "Waarnaar het verwijst", "Voorbeeld"], [
                ["il, elle, ils, elles", "naar wie of wat al genoemd is", "Les élèves ont protesté. Ils voulaient…"],
                ["y", "naar een plaats die al genoemd is", "J'aime cette ville. J'y habite depuis dix ans."],
                ["en", "naar een hoeveelheid van iets dat al genoemd is", "Tu as des frères ? — Oui, j'en ai deux."],
                ["celui-ci", "het laatstgenoemde", "Le chien et le chat : celui-ci dort."],
                ["celui-là", "het eerstgenoemde", "Le chien et le chat : celui-là aboie."],
                ["ce dernier", "de laatstgenoemde persoon of zaak", "Le directeur a reçu le journaliste; ce dernier posait des questions."],
            ]), "Zes verwijswoorden met waarnaar ze terugwijzen."),
            ("weetje", "<em>Elle</em> verwijst niet altijd naar een persoon. Een Frans woord heeft "
                       "een geslacht, dus <em>la bibliothèque</em> wordt ook <em>elle</em>: "
                       "<em>elle reste ouverte jusqu'à vingt heures</em>."),
        ]),
        buiten("lees een Franse recensie of een Frans opiniestukje en zoek er de signaalwoorden in; "
               "zeg daarna in het Frans in twee zinnen of je het eens bent."),
    ],
)


# ───────────────────────── 3. De Franstalige wereld: omgangsvormen en gewoontes
BUNDELS["de-franstalige-wereld-omgangsvormen-en-gewoontes" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="De Franstalige wereld: omgangsvormen en gewoontes",
    onder="Waar Frans gesproken wordt, hoe het van streek tot streek verschilt, en wat je zegt en doet om niet onbeleefd over te komen.",
    secties=[
        dict(kop="Waar wordt er Frans gesproken?", blokken=[
            ("p", "Frans is een officiële landstaal in <strong>België</strong>, "
                  "<strong>Zwitserland</strong> en <strong>Luxemburg</strong>, en in "
                  "<strong>Canada</strong> zelfs op het niveau van het hele land. De provincie waar "
                  "het grootste deel van de bevolking Frans spreekt, is <strong>Québec</strong>."),
            ("p", "De <strong>meeste</strong> landen met Frans als officiële taal liggen echter in "
                  "<strong>Afrika</strong>: <em>le Sénégal</em>, <em>la Côte d'Ivoire</em> en "
                  "<em>la République démocratique du Congo</em> zijn er drie van. De gemeenschap van "
                  "al die landen en gebieden samen heet <strong>la Francophonie</strong>."),
            ("fig", tabel(["Hoofdstad", "Land", "Frans officieel?"], [
                ["Paris", "la France", "ja"],
                ["Bruxelles", "la Belgique", "ja"],
                ["Dakar", "le Sénégal", "ja"],
                ["Lisbonne", "le Portugal", "neen, daar is het Portugees"],
            ]), "Drie hoofdsteden van Franstalige landen, en één die er niet bij hoort."),
        ]),
        dict(kop="Hetzelfde Frans, andere woorden", blokken=[
            ("p", "Frans is niet overal hetzelfde, en het examen kan een tekst uit België, Frankrijk "
                  "of Québec voorleggen. Het bekendste verschil zijn de "
                  "<strong>getalwoorden</strong>: een Belg zegt <em>septante</em> en "
                  "<em>nonante</em>, een Fransman <em>soixante-dix</em> en <em>quatre-vingt-dix</em>. "
                  "<em>Octante</em> hoor je bij ons nooit; tachtig is <em>quatre-vingts</em>, overal."),
            ("fig", tabel(["België of Québec", "Frankrijk", "Nederlands"], [
                ["septante, nonante", "soixante-dix, quatre-vingt-dix", "zeventig, negentig"],
                ["le dîner (België)", "le déjeuner", "het middagmaal"],
                ["un GSM (België)", "un portable", "een mobiele telefoon"],
                ["un courriel (Québec)", "un mail", "een e-mail"],
                ["une fin de semaine (Québec)", "un week-end", "een weekend"],
                ["un cégep (Québec)", "—", "een school tussen secundair en universiteit"],
            ]), "Woorden die van streek tot streek verschillen."),
            ("weetje", "<em>Quinze jours</em> betekent in het Frans <strong>twee weken</strong>, geen "
                       "vijftien dagen. Men rekent de eerste en de laatste dag mee. Zo is "
                       "<em>huit jours</em> een week."),
        ]),
        dict(kop="Het schooljaar, de feestdag en de datum", blokken=[
            ("p", "<strong>La rentrée</strong> is het <strong>begin van het schooljaar na de "
                  "zomer</strong>, en het is in Frankrijk een begrip: de winkels, de kranten en de "
                  "politiek praten erover. Het is dus niet de terugkeer van een reis en ook niet de "
                  "ingang van een gebouw."),
            ("fig", svg.ladder([
                ("l'université", "pas na het secundair"),
                ("le bac", "het eindexamen van het secundair"),
                ("le lycée", "de laatste jaren secundair"),
                ("le collège", "de eerste jaren secundair"),
                ("l'école primaire", "het lager onderwijs"),
            ], bovenaan="het laatst", onderaan="het eerst"),
             "De Franse schoolloopbaan, van onder naar boven in de orde waarin je ze doorloopt."),
            ("p", "De <strong>nationale feestdag</strong> van Frankrijk is <strong>14 juli</strong>; "
                  "21 juli is de onze. En een <strong>datum</strong> schrijf je in het Frans met een "
                  "lidwoord en zonder hoofdletter: <strong>le 3 septembre</strong>. Namen van maanden "
                  "en dagen krijgen in het Frans <strong>geen hoofdletter</strong>, anders dan in het "
                  "Engels: <em>lundi</em>, <em>mars</em>, <em>septembre</em>."),
        ]),
        dict(kop="Bonjour, tu of vous, en la bise", blokken=[
            ("p", "Stap je in Frankrijk een bakkerij binnen, dan zeg je <strong>eerst "
                  "<em>bonjour</em></strong> en pas daarna wat je komt halen. Met de deur in huis "
                  "vallen klinkt er onbeschoft, ook als je vraag netjes is."),
            ("p", "<strong>Tutoyer</strong> is iemand met <em>tu</em> aanspreken, "
                  "<strong>vouvoyer</strong> met <em>vous</em>. Je gebruikt <em>vous</em> bij een "
                  "volwassene met wie je <strong>geen nauwe band</strong> hebt: een winkelier, een "
                  "leerkracht die je niet kent, een onbekende op straat. <em>Tu</em> tegen een "
                  "onbekende volwassene komt in Frankrijk meestal <strong>te familiair of zelfs "
                  "onbeleefd</strong> over."),
            ("fig", tabel(["Situatie", "Wat je zegt"], [
                ["je ontmoet iemand voor het eerst", "Enchanté."],
                ["je verontschuldigt je", "Je suis désolé. / Excusez-moi. / Pardon."],
                ["iemand bedankt je", "De rien."],
                ["je neemt afscheid", "Au revoir. / À bientôt. / Bonne journée."],
                ["je nodigt een vriend uit", "Ça te dit d'aller au cinéma ?"],
                ["je gaat eten", "Bon appétit."],
            ]), "Zes vaste momenten, met wat er dan gezegd wordt."),
            ("p", "<strong>La bise</strong> is de begroeting met <strong>kussen op de wang</strong> — "
                  "geen handdruk en geen buiging. Hoeveel kussen het zijn, verschilt zelfs van streek "
                  "tot streek. En <em>bon appétit</em> zeg je <strong>vóór</strong> de maaltijd, niet "
                  "achteraf als dank."),
            ("weetje", "Een <strong>fooi</strong> is in een Franse winkel of restaurant niet "
                       "verplicht: <em>le service est compris</em> staat meestal op de rekening. Wie "
                       "tevreden is, laat wat kleingeld liggen, maar niemand verwacht het."),
        ]),
        dict(kop="Een klassieke maaltijd", blokken=[
            ("p", "De gangen van een klassieke Franse maaltijd komen in deze orde: "
                  "<strong>l'entrée</strong>, <strong>le plat</strong>, <strong>le fromage</strong> "
                  "en pas daarna <strong>le dessert</strong>. Die kaas vóór het nagerecht is het stuk "
                  "dat bij ons vaak omgewisseld wordt."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["l'entrée", "het voorgerecht"],
                ["le plat (principal)", "het hoofdgerecht"],
                ["le fromage", "de kaas"],
                ["le dessert", "het nagerecht"],
                ["l'addition", "de rekening"],
                ["le service est compris", "de dienst is inbegrepen"],
            ]), "De woorden die je aan tafel en bij het afrekenen nodig hebt."),
        ]),
        dict(kop="Beleefd schrijven: de aanhef, de slotformule en de conditionnel", blokken=[
            ("p", "Schrijf je naar een dienst of een gemeente en ken je de <strong>naam van de "
                  "ontvanger niet</strong>, dan begin je met <strong><em>Madame, "
                  "Monsieur,</em></strong>. <em>Salut</em>, <em>Cher ami</em> of <em>Bonjour toi</em> "
                  "kan daar niet."),
            ("fig", tabel(["Slotformule", "Hoe formeel"], [
                ["Veuillez agréer mes salutations distinguées", "heel formeel, voor een brief aan een dienst"],
                ["Bien à vous", "formeel en toch vriendelijk"],
                ["Cordialement", "de gewone formule in een mail"],
                ["Bisous", "enkel voor familie en goede vrienden"],
            ]), "Vier slotformules, van de meest formele tot de meest familiare."),
            ("p", "De <strong>conditionnel de politesse</strong> is de truc om een vraag beleefd te "
                  "maken: je vraagt iets met <strong><em>je voudrais</em></strong> in plaats van "
                  "<em>je veux</em>, en met <strong><em>pourriez-vous</em></strong> in plaats van "
                  "<em>pouvez-vous</em>. <em>Pourriez-vous m'aider, s'il vous plaît ?</em> klinkt "
                  "meteen een toon vriendelijker."),
            ("p", "Schrijf je een <strong>blogbericht voor leeftijdsgenoten</strong>, dan mag je hen "
                  "met <em>tu</em> of <em>vous</em> aanspreken, maar wel <strong>verzorgd en zonder "
                  "sms-taal</strong>. De plechtige formules van een officiële brief horen daar niet, "
                  "en losse opsommingen zonder volledige zinnen ook niet."),
            ("weetje", "<strong>Lichaamstaal</strong> hoort bij de socioculturele aspecten die de "
                       "fiche noemt: hoe dicht je bij iemand staat, of je de hand geeft of de bise, "
                       "of je iemand in de ogen kijkt. Het hoort er dus bij, ook al kan je het niet "
                       "achter een scherm oefenen."),
        ]),
        buiten("zoek een Frans gesprekje op (in een film of een reeks), let op wanneer de mensen "
               "elkaar met tu of vous aanspreken, en zeg daarna zelf hardop dezelfde vraag eerst met "
               "tu en dan met vous."),
    ],
)


# ───────────────────────── 4. Schrijven, schriftelijke interactie en leesbeleving
BUNDELS["schrijven-schriftelijke-interactie-en-leesbeleving" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Schrijven, schriftelijke interactie en leesbeleving",
    onder="De taalhandelingen van het examen, de opbouw van een verzorgde mail, antwoorden op een bericht, en in het Frans zeggen wat een verhaal met je deed.",
    secties=[
        dict(kop="Wat vraagt een schrijfopdracht?", blokken=[
            ("p", "Op het examen <strong>Frans 2</strong> staan twee schrijfopdrachten. Elke opdracht "
                  "heeft een <strong>taalhandeling</strong>: wat je met je tekst wil doen. Dat is het "
                  "eerste dat je moet vaststellen, want het bepaalt alles wat daarna komt."),
            ("fig", tabel(["Taalhandeling", "Wanneer", "Franse zinnen"], [
                ["informatie vragen", "een mail naar de gemeente over vrijwilligerswerk",
                 "Pourriez-vous me dire si… / Je voudrais savoir… / J'aimerais avoir des renseignements sur…"],
                ["je mening geven", "een reactie onder een discussie op sociale media",
                 "À mon avis… / Je trouve que… / Selon moi…"],
                ["iets vertellen", "in een mail beschrijven hoe een ongeval gebeurd is",
                 "D'abord… puis… finalement…"],
                ["iets uitleggen", "een blogbericht met tips om vlotter in te slapen",
                 "Je vais vous expliquer comment ça marche."],
                ["iemand overtuigen", "een castingbureau vragen je inschrijving te aanvaarden",
                 "D'abord… De plus… Enfin…"],
                ["sociale contacten", "begroeten, bedanken, uitnodigen, je verontschuldigen, je waardering uiten",
                 "Je vous remercie de votre réponse."],
            ]), "De taalhandelingen van de vakfiche, met waar je ze tegenkomt."),
            ("p", "<em>Des renseignements</em> zijn <strong>inlichtingen</strong>: <em>je voudrais "
                  "des renseignements sur le stage</em>. En <em>expliquer</em> is "
                  "<strong>uitleggen</strong>, <em>remercier</em> is <strong>bedanken</strong>."),
            ("weetje", "Een schrijfopdracht beoordeelt <strong>niet alleen</strong> je grammatica. Of "
                       "je de taalhandeling uitvoert, of je toon bij de ontvanger past en of je tekst "
                       "een duidelijke opbouw heeft, telt even goed mee."),
        ]),
        dict(kop="Voor je de eerste zin schrijft", blokken=[
            ("p", "Een <strong>schrijfplan</strong> is een <strong>lijstje kernwoorden</strong> dat je "
                  "vooraf maakt. Niet de hele tekst eerst in het Nederlands schrijven — dan krijg je "
                  "een vertaling in plaats van een Franse tekst — en ook geen woordentelling."),
            ("p", "Stel je daarna de drie vragen van het <strong>communicatiemodel</strong>: "
                  "<strong>waarom</strong> schrijf ik, <strong>voor wie</strong> is mijn boodschap, en "
                  "<strong>welk kanaal</strong> gebruik ik? Hoeveel tijd je nog hebt, hoort daar niet "
                  "bij: dat verandert je tekst niet."),
            ("kader", "<strong>Zit je vast, bereik dan je doel met de woorden die je wél kent.</strong> "
                      "Je kent <em>une perceuse</em> niet? Omschrijf het: <em>un outil pour faire des "
                      "trous</em>. Dat is beter dan de zin weglaten, een Nederlands woord in je Franse "
                      "tekst zetten of een woord gebruiken dat iets anders betekent."),
        ]),
        dict(kop="De opbouw van een verzorgde mail", blokken=[
            ("p", "Een verzorgde Franse mail heeft vier delen, en altijd in deze orde."),
            ("fig", svg.tekstopbouw([
                ("de aanhef", "Madame, Monsieur, / Salut Léa,", 1.0),
                ("de reden van je bericht", "Je vous écris au sujet de votre annonce.", 1.0),
                ("de inhoud", "je vraag, je verhaal, je argumenten", 1.3),
                ("de slotformule", "Cordialement, / Bien à vous,", 1.0),
            ]), "De vier delen van een mail, van boven naar onder."),
            ("p", "De <strong>reden</strong> zeg je meteen in de eerste zin: <em>Je vous écris au "
                  "<strong>sujet</strong> de votre annonce</em>, <em>Je me permets de vous contacter "
                  "pour…</em>, <em>Suite à votre annonce, …</em>. <em>Je vous remercie d'avance</em> "
                  "hoort daar net niet: dat is een slotzin."),
            ("fig", tabel(["Aanhef", "Wanneer"], [
                ["Salut Léa,", "aan een vriendin"],
                ["Madame, / Monsieur,", "aan iemand die je niet kent"],
                ["Cher Monsieur, / Chère Madame,", "aan iemand die je al kent"],
                ["Monsieur le Directeur,", "aan iemand met een functie, heel formeel"],
            ]), "Vier aanhefvormen, met de situatie waarin ze passen."),
            ("p", "Let op twee dingen. <em>Je vous prie d'agréer, Madame, mes salutations "
                  "distinguées</em> is een <strong>slotformule</strong>, geen aanhef. En een formele "
                  "mail hou je <strong>helemaal</strong> in de <strong>vous-vorm</strong>, ook in de "
                  "werkwoorden van de laatste zin: wie halverwege naar <em>tu</em> overschakelt, "
                  "verliest zijn toon."),
        ]),
        dict(kop="Vertellen, uitleggen en overtuigen", blokken=[
            ("p", "<strong>Vertellen</strong> wat er gebeurd is, doe je in het Frans met de "
                  "<strong>passé composé</strong> voor de gebeurtenissen en de "
                  "<strong>imparfait</strong> voor de achtergrond: <em>Il pleuvait (achtergrond) et "
                  "la voiture a glissé (gebeurtenis)</em>."),
            ("p", "<strong>Overtuigen</strong> doe je met <strong>argumenten</strong>, en dan het "
                  "best met argumenten waarom de ontvanger er zelf beter van wordt. Zet ze op een rij "
                  "met <em>d'abord</em>, <em>de plus</em> en <em>enfin</em>. Een opsomming van je "
                  "gevoelens of een verhaal over je vakantie overtuigt een castingbureau niet."),
            ("p", "<strong>Uitnodigen</strong> kan formeel en informeel: <em>Nous serions heureux de "
                  "vous accueillir le 12 mai</em> tegenover <em>Viens donc, ça va être génial !</em> "
                  "De eerste is een conditionnel met <em>vous</em>, de tweede een gebiedende wijs met "
                  "<em>tu</em>."),
            ("weetje", "Na <em>je pense que</em> in een <strong>bevestigende</strong> zin komt "
                       "gewoon de <strong>indicatif</strong>: <em>je pense qu'il est malade</em>. De "
                       "subjonctif komt pas als je het ontkent of er een vraag van maakt: <em>je ne "
                       "pense pas qu'il soit malade</em>."),
        ]),
        dict(kop="Schriftelijke interactie: antwoorden op een bericht", blokken=[
            ("p", "Een opdracht waarbij je <strong>op een bericht van iemand anders antwoordt</strong>, "
                  "heet <strong>schriftelijke interactie</strong>. Daar zit een valkuil in: het bericht "
                  "stelt vaak meer dan één vraag."),
            ("p", "De veiligste aanpak is <strong>alle vragen beantwoorden, in dezelfde "
                  "volgorde</strong> als ze gesteld zijn. Eén vraag kiezen levert punten in, en alles "
                  "samenvatten in één algemene zin ook. De vragen woord voor woord herhalen hoeft "
                  "niet: je antwoord mag gewoon duidelijk zijn."),
            ("fig", tabel(["Situatie", "Wat je schrijft"], [
                ["je verontschuldigt je voor een gemiste afspraak",
                 "Je suis vraiment désolé de ne pas avoir pu venir."],
                ["iemand verontschuldigt zich bij jou",
                 "Ce n'est pas grave, ne vous inquiétez pas."],
                ["je bedankt voor een antwoord", "Je vous remercie de votre réponse."],
                ["je vraagt om inlichtingen", "J'aimerais avoir des renseignements sur…"],
            ]), "Vier reacties die in een mailgesprek telkens terugkomen."),
        ]),
        dict(kop="Leesbeleving: zeggen wat een tekst met je deed", blokken=[
            ("p", "Bij <strong>leesbeleving</strong> vraagt de fiche iets anders dan begrijpen: dat je "
                  "in het <strong>Frans je eigen ervaring en je gevoelens verwoordt</strong>. Je hoeft "
                  "het gedicht dus niet woord voor woord te vertalen, de dichter niet te dateren en "
                  "het rijmschema niet te benoemen."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["Cette histoire m'a beaucoup touché.", "Dat verhaal heeft me erg geraakt."],
                ["Ce personnage me ressemble beaucoup.", "Dat personage lijkt veel op mij."],
                ["La fin m'a surpris parce que…", "Het einde verraste me omdat…"],
                ["Je me suis reconnu dans…", "Ik herkende mezelf in…"],
                ["Ce passage m'a fait rire.", "Die passage deed me lachen."],
                ["Je n'ai pas aimé, car…", "Ik vond het niet goed, want…"],
            ]), "Zes zinnen om je beleving bij een tekst te verwoorden."),
            ("p", "<em>Le livre compte deux cent dix pages</em> is géén beleving maar een feit. Zeg "
                  "dus wat het boek <strong>met jou</strong> deed, en geef er telkens een "
                  "<strong>reden</strong> bij met <em>parce que</em> of <em>car</em>."),
        ]),
        dict(kop="Nalezen, en wat een spellingcontrole niet ziet", blokken=[
            ("p", "De fiche vraagt uitdrukkelijk dat je je tekst <strong>grondig naleest</strong> voor "
                  "je hem indient. Let daarbij op drie dingen: of de <strong>werkwoorden "
                  "overeenkomen</strong> met hun onderwerp, of de <strong>bijvoeglijke "
                  "naamwoorden</strong> het juiste geslacht en getal hebben, en of je "
                  "<strong>overal dezelfde aanspreekvorm</strong> hebt aangehouden."),
            ("p", "Een <strong>spellingcontrole</strong> helpt je met een vergeten letter, een "
                  "ontbrekend accent of een dubbele medeklinker te veel. Wat ze <strong>niet</strong> "
                  "vindt, is een woord dat <strong>juist gespeld is maar niet past</strong>: "
                  "<em>le père</em> in plaats van <em>la paire</em> ziet geen enkele controle."),
            ("kader", "<strong>Geen sms-taal.</strong> Ook aan een leeftijdsgenoot schrijf je in een "
                      "schrijfopdracht geen afkortingen. Je taal <strong>aanpassen aan de "
                      "ontvanger</strong> betekent een gepaste toon kiezen, zodat je boodschap beter "
                      "aankomt — niet de regels laten vallen."),
        ]),
        buiten("schrijf een korte Franse mail aan een echte plek waar je stage of vrijwilligerswerk "
               "zou willen doen, en lees hem daarna luidop voor: wat je niet kan voorlezen, is meestal "
               "ook niet goed geschreven."),
    ],
)


# ───────────────────────── 5. Woordvelden: mens, gezondheid en het dagelijkse leven
BUNDELS["woordvelden-mens-gezondheid-en-het-dagelijkse-leven" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Woordvelden: mens, gezondheid en het dagelijkse leven",
    onder="De familie, de gevoelens, het lichaam en de dokter, eten, kleren, het huis en de gang van een gewone dag.",
    secties=[
        dict(kop="De familie", blokken=[
            ("p", "De familiewoorden lijken op elkaar, en net daarom worden ze verward. "
                  "<em>Un <strong>beau</strong>-père</em> is een <strong>schoonvader of een "
                  "stiefvader</strong> — niet een grootvader en niet een peter. Dezelfde "
                  "<em>beau-</em> komt terug in <em>une belle-mère</em>, <em>un beau-frère</em> en "
                  "<em>une belle-sœur</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["les grands-parents, ma grand-mère", "de grootouders, mijn grootmoeder"],
                ["un oncle, une tante", "een oom, een tante"],
                ["un cousin, une cousine", "een neef, een nicht (kind van je oom of tante)"],
                ["un neveu, une nièce", "een neef, een nicht (kind van je broer of zus)"],
                ["un beau-père, une belle-mère", "een schoonvader of stiefvader, een schoonmoeder of stiefmoeder"],
                ["un voisin, une voisine", "een buur — géén familie"],
            ]), "De familiewoorden die in teksten het vaakst terugkomen."),
            ("weetje", "<em>Les parents</em> betekent in het Frans niet altijd alleen de vader en de "
                       "moeder: het kan ook <strong>de familie in het algemeen</strong> zijn, zoals "
                       "ons woord 'verwanten'. <em>J'ai des parents en France</em> betekent dus dat "
                       "je daar familie hebt."),
        ]),
        dict(kop="Gevoelens", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["triste", "verdrietig"],
                ["en colère", "boos"],
                ["déçu(e)", "ontgoocheld"],
                ["inquiet, inquiète", "ongerust"],
                ["content(e), heureux", "tevreden, gelukkig"],
                ["avoir peur, avoir honte", "bang zijn, zich schamen"],
            ]), "Gevoelswoorden; mince (slank) staat er bewust niet bij, dat beschrijft een lichaam."),
            ("p", "<em>Être inquiet</em> is <strong>ongerust</strong> zijn, niet boos en niet "
                  "verveeld. <em>J'ai <strong>peur</strong> des araignées</em> is: ik ben bang van "
                  "spinnen. En <em>avoir honte</em> is <strong>zich schamen</strong>."),
        ]),
        dict(kop="Het lichaam, ziek zijn en de dokter", blokken=[
            ("p", "Pijn uitdrukken gaat in het Frans altijd met <strong><em>avoir mal à</em></strong> "
                  "plus het lichaamsdeel, met het lidwoord erbij: <em>j'ai mal à la "
                  "<strong>tête</strong></em> is hoofdpijn, <em>j'ai mal à la <strong>gorge</strong></em> "
                  "is keelpijn. <em>Au cou</em> zou je nek zijn, <em>à la bouche</em> je mond en "
                  "<em>à la langue</em> je tong."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la tête, la gorge, le cou", "het hoofd, de keel, de nek"],
                ["l'épaule, le genou, la cheville", "de schouder, de knie, de enkel"],
                ["se casser le bras", "zijn arm breken"],
                ["une ordonnance", "een voorschrift van de dokter"],
                ["un médecin, une infirmière", "een arts, een verpleegkundige"],
                ["être en pleine forme", "in topvorm zijn"],
            ]), "Het lichaam en de woorden van bij de dokter."),
            ("p", "<em>Il est malade</em>, <em>elle ne se sent pas bien</em> en <em>il a de la "
                  "fièvre</em> zeggen allemaal dat iemand zich niet goed voelt. <em>Elle est en "
                  "pleine forme</em> zegt net het <strong>omgekeerde</strong>. En <em>être "
                  "fatigué</em> is <strong>moe</strong> zijn, niet ziek, niet verkouden en niet "
                  "gewond."),
            ("weetje", "<em>Les cheveux</em> zijn de <strong>haren</strong>, <em>les chevaux</em> zijn "
                       "de <strong>paarden</strong>. Eén letter verschil, en een zin die ineens iets "
                       "heel anders zegt."),
        ]),
        dict(kop="Avoir waar wij 'zijn' zeggen", blokken=[
            ("p", "Een vaste valstrik. Het Frans gebruikt <strong>avoir</strong> op plaatsen waar wij "
                  "'zijn' zeggen. <em>J'ai <strong>soif</strong></em> is 'ik heb dorst', en <em>il "
                  "<strong>a</strong> quinze ans</em> betekent <strong>hij is vijftien jaar</strong> "
                  "— niet dat hij vijftien broers heeft of er vijftien jaar woont."),
            ("fig", tabel(["Met avoir", "Nederlands", "Met être"], [
                ["avoir faim, avoir soif", "honger hebben, dorst hebben", "être content, blij zijn"],
                ["avoir froid, avoir chaud", "koud hebben, warm hebben", "être fatigué, moe zijn"],
                ["avoir peur, avoir honte", "bang zijn, zich schamen", "être triste, verdrietig zijn"],
                ["avoir … ans", "… jaar zijn", "être malade, ziek zijn"],
            ]), "Links de uitdrukkingen met avoir, rechts die met être."),
        ]),
        dict(kop="Eten en drinken", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un repas", "een maaltijd"],
                ["le pain, la confiture, le café", "het brood, de confituur, de koffie"],
                ["les légumes, les fruits", "de groenten, het fruit"],
                ["la viande, le poulet, le poisson", "het vlees, de kip, de vis"],
                ["une entrée, un plat, un dessert", "een voorgerecht, een gerecht, een nagerecht"],
                ["être au régime", "op dieet zijn"],
            ]), "Het woordveld eten, met de drie gangen erbij."),
            ("p", "<em>Un repas</em> is de <strong>maaltijd</strong> zelf; een recept is <em>une "
                  "recette</em>, een restaurant <em>un restaurant</em> en een bord <em>une "
                  "assiette</em>. Let ook op <em>le poulet</em> (de kip) tegenover <em>le pain</em> "
                  "(het brood): bij het ontbijt hoort het tweede."),
        ]),
        dict(kop="Kleren, kleuren en materialen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["une chemise, un pantalon", "een hemd, een broek"],
                ["une jupe, une robe", "een rok, een kleed"],
                ["des chaussures noires, des chaussettes", "zwarte schoenen, sokken"],
                ["une ceinture", "een gordel — een accessoire, geen kledingstuk"],
                ["porter", "dragen, zowel in je handen als aan je lijf"],
                ["le verre, le bois, le cuir", "het glas, het hout, het leer"],
            ]), "Kleren, een accessoire en drie materialen."),
            ("p", "Bij de <strong>kleuren</strong> zit een regel die je moet kennen: de meeste kleuren "
                  "passen zich aan (<em>une robe verte</em>, <em>des robes vertes</em>), maar een "
                  "paar kleuren die eigenlijk de naam van een <strong>ding</strong> zijn, veranderen "
                  "<strong>nooit</strong> van vorm."),
            ("fig", svg.kleurstalen([
                ("marron", "kastanjebruin", "#8b5a2b"),
                ("orange", "oranje", "#e07b1f"),
                ("kaki", "kaki", "#8a8f4a"),
                ("vert", "groen", "#2f7d3a"),
            ]), "De eerste drie blijven onveranderlijk; vert is een gewone kleur om naast te leggen."),
            ("p", "<em>Des chaussures <strong>marron</strong></em> dus, maar <em>des chaussures "
                  "<strong>vertes</strong></em>. <em>Marron</em> is immers een kastanje, "
                  "<em>orange</em> een sinaasappel en <em>kaki</em> een vrucht."),
        ]),
        dict(kop="Het huis", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la cuisine", "de keuken"],
                ["la salle de bains, une serviette", "de badkamer, een handdoek"],
                ["la chambre", "de slaapkamer"],
                ["le rez-de-chaussée", "het gelijkvloers"],
                ["un immeuble, un appartement", "een gebouw, een appartement"],
                ["un canapé, un portefeuille, des clés", "een zetel, een portefeuille, sleutels"],
            ]), "De kamers van een huis, en wat er in staat of in je zak zit."),
            ("p", "<em>L'immeuble</em> is géén kamer maar het <strong>gebouw</strong> waarin de "
                  "appartementen zitten. En <em>le rez-de-chaussée</em> is het "
                  "<strong>gelijkvloers</strong>: de eerste verdieping is in het Frans al één trap "
                  "hoger dan bij ons gevoel."),
            ("weetje", "<em>Un a<strong>pp</strong>artement</em> schrijf je in het Frans met "
                       "<strong>twee p's</strong>, anders dan het Engelse <em>apartment</em>. "
                       "Zulke kleine verschillen tussen Frans en Engels kosten op een examen punten."),
        ]),
        dict(kop="De gang van een gewone dag", blokken=[
            ("p", "Wat je dagelijks doet, staat in het Frans vaak in een "
                  "<strong>wederkerend</strong> werkwoord: <em>je <strong>me</strong> lève</em>, "
                  "<em>je <strong>me</strong> lave</em>, <em>je <strong>m'</strong>habille</em>. "
                  "<em>Je me <strong>lève</strong> à sept heures</em> is: ik sta om zeven uur op."),
            ("fig", svg.stappen([
                "se lever|opstaan",
                "se laver|je wassen",
                "s'habiller|je kleden",
                "se coucher|gaan slapen",
            ]), "Vier wederkerende werkwoorden in de orde van een dag; alleen het laatste hoort bij de avond."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["faire la vaisselle", "de vaat doen, afwassen"],
                ["faire la lessive", "de was doen in de wasmachine"],
                ["ranger sa chambre", "zijn kamer opruimen"],
                ["faire les courses", "boodschappen doen"],
                ["mettre la table", "de tafel dekken"],
                ["sortir la poubelle", "de vuilnisbak buitenzetten"],
            ]), "De huishoudelijke klussen die in teksten en opdrachten terugkomen."),
            ("p", "Twee die op elkaar lijken: <em>faire la <strong>vaisselle</strong></em> is "
                  "<strong>afwassen</strong>, <em>faire la <strong>lessive</strong></em> is de was "
                  "doen in de wasmachine. En <em>ranger sa chambre</em> is zijn kamer "
                  "<strong>opruimen</strong>, niet schilderen, huren of verlaten."),
        ]),
        buiten("vertel in het Frans aan iemand hoe jouw dag van vandaag verliep, van het opstaan tot "
               "nu, en gebruik daarbij minstens drie wederkerende werkwoorden."),
    ],
)


# ───────────────────────── 6. Woordvelden: school, werk, reizen en de samenleving
BUNDELS["woordvelden-school-werk-reizen-en-de-samenleving" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Woordvelden: school, werk, reizen en de samenleving",
    onder="De school en de beroepen, het vervoer en het verblijf, de instructietaal van de opdrachten, de cijfers, het uur en het weer.",
    secties=[
        dict(kop="De school", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["une matière", "een vak"],
                ["un horaire, un bulletin", "een uurrooster, een rapport"],
                ["une interrogation", "een toets"],
                ["un examen, réussir un examen", "een examen, slagen voor een examen"],
                ["un stage", "een stage of een cursus van enkele dagen"],
                ["la récréation", "de pauze op school"],
            ]), "Het woordveld school; un chantier (een werf) hoort er niet bij."),
            ("p", "Eén woord vraagt opletten: <em><strong>passer</strong> un examen</em> betekent "
                  "alleen dat je het examen <strong>aflegt</strong>, niet dat je geslaagd bent. "
                  "Geslaagd zijn is <em><strong>réussir</strong></em>: <em>j'ai réussi mon "
                  "<strong>examen</strong></em>."),
        ]),
        dict(kop="Werk en beroepen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un boulanger, une boulangère", "een bakker, een bakkerin"],
                ["un plombier, un électricien", "een loodgieter, een elektricien"],
                ["un avocat, une avocate", "een advocaat, een advocate"],
                ["une enseignante, une institutrice, une professeure", "een leerkracht, een onderwijzeres, een lerares"],
                ["un emploi, un travail", "werk — de twee woorden betekenen hetzelfde"],
                ["un entretien d'embauche", "een sollicitatiegesprek"],
            ]), "Beroepen en de woorden rond werk zoeken; un bâtiment (een gebouw) is geen beroep."),
            ("p", "<em>Elle travaille comme <strong>enseignante</strong> dans une école</em>: let op "
                  "de <strong>vrouwelijke vorm</strong>, die het Frans voor bijna elk beroep heeft. "
                  "En een <em>agence pour l'emploi</em> is een <strong>arbeidsbureau</strong> — dat "
                  "hoort bij werk en niet bij reizen."),
        ]),
        dict(kop="Vervoer, reizen en verblijf", blokken=[
            ("p", "Bij een vervoermiddel waarin je <strong>in</strong> zit, staat <em>en</em>: "
                  "<em><strong>en</strong> train</em>, <em>en voiture</em>, <em>en avion</em>. Bij "
                  "een vervoermiddel waarop je <strong>zit</strong>, staat <em>à</em>: <em>à "
                  "<strong>vélo</strong></em>, <em>à moto</em>, <em>à pied</em> (te voet)."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un car", "een autocar of een reisbus — géén personenwagen"],
                ["un camion, un avion", "een vrachtwagen, een vliegtuig"],
                ["un aller-retour", "een heen-en-terugticket"],
                ["une auberge de jeunesse", "een jeugdherberg"],
                ["une chambre d'hôte", "een gastenkamer, een bed and breakfast"],
                ["un camping", "een camping"],
            ]), "Vervoermiddelen en soorten verblijf; un carnet is een boekje."),
        ]),
        dict(kop="Landen en nationaliteiten", blokken=[
            ("p", "Welk voorzetsel je bij een land zet, hangt af van zijn geslacht. Bij een "
                  "<strong>vrouwelijk</strong> land staat <em>en</em>: <em>j'habite "
                  "<strong>en</strong> Belgique</em>, <em>en France</em>. Bij een "
                  "<strong>mannelijk</strong> land staat <em>au</em>: <em>au Portugal</em>, "
                  "<em>au Canada</em>. Bij een <strong>meervoud</strong> staat <em>aux</em>: "
                  "<em>aux Pays-Bas</em>."),
            ("fig", tabel(["Vraag", "Juist", "Fout"], [
                ["waar woon je?", "j'habite en Belgique", "j'habite dans la Belgique"],
                ["waar kom je uit?", "il vient de France", "il vient de la France"],
                ["waar ga je naartoe?", "je vais au Portugal", "je vais à Portugal"],
                ["en bij een meervoud?", "aux Pays-Bas", "à les Pays-Bas"],
            ]), "De vormen die het vaakst fout gaan, met de juiste ernaast."),
            ("weetje", "Namen van nationaliteiten krijgen in het Frans een "
                       "<strong>kleine</strong> letter als ze een <strong>bijvoeglijk "
                       "naamwoord</strong> zijn: <em>un film <strong>f</strong>rançais</em>. Staan ze "
                       "als zelfstandig naamwoord voor de persoon, dan krijgen ze een hoofdletter: "
                       "<em>un <strong>F</strong>rançais</em>."),
        ]),
        dict(kop="Winkels, diensten en multimedia", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la caisse", "de kassa"],
                ["une réduction", "een korting"],
                ["la livraison", "de levering"],
                ["un portable", "een gsm of een draagbare computer"],
                ["un écran, un mot de passe", "een scherm, een wachtwoord"],
                ["une pièce jointe", "een bijlage bij een mail"],
            ]), "Winkelwoorden en de woorden van het scherm; une étagère is een rek."),
        ]),
        dict(kop="De instructietaal: het Frans van de opdrachten", blokken=[
            ("p", "Dit is het woordveld dat het makkelijkst vergeten wordt en het meeste punten kost. "
                  "Wie niet weet wat <em>cochez</em> of <em>soulignez</em> betekent, verliest punten "
                  "op een vraag waarvan hij het antwoord <strong>kende</strong>."),
            ("fig", tabel(["Opdracht", "Wat je moet doen"], [
                ["cochez la bonne réponse", "het juiste antwoord aankruisen"],
                ["soulignez le verbe", "het werkwoord onderlijnen"],
                ["entourez, barrez", "omcirkelen, doorstrepen"],
                ["reliez", "twee dingen met elkaar verbinden"],
                ["complétez, rédigez, décrivez", "aanvullen, schrijven, beschrijven — je schrijft zelf"],
                ["justifiez votre réponse", "uitleggen waarom je dat antwoord geeft"],
            ]), "De opdrachtwoorden die op een Frans examen terugkomen."),
        ]),
        dict(kop="Cijfers, maten en hoeveelheden", blokken=[
            ("p", "In Frankrijk zegt men <em>soixante-dix</em> (70), <em>quatre-vingts</em> (80) en "
                  "<em>quatre-vingt-dix</em> (90). <em>Septante-cinq</em> bestaat in Frankrijk niet; "
                  "dat is Belgisch Frans. Let ook op de <strong>s</strong> van "
                  "<em>quatre-ving<strong>ts</strong></em>, die wegvalt zodra er nog een getal volgt: "
                  "<em>quatre-vingt-un</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["trois virgule cinq (3,5)", "drie komma vijf — met een komma, niet met een punt"],
                ["une livre", "een pond, ongeveer een halve kilo"],
                ["un kilo, un gramme, une tonne", "een kilo, een gram, een ton"],
                ["beaucoup de, un peu de, assez de", "veel, een beetje, genoeg"],
                ["trop de, moins de, plus de", "te veel, minder, meer"],
                ["une centaine, une dizaine", "een honderdtal, een tiental"],
            ]), "Maten en hoeveelheden; parce que (omdat) hoort bij de verbanden."),
            ("p", "Na een hoeveelheid komt <strong><em>de</em></strong> zonder lidwoord: <em>il y a "
                  "beaucoup <strong>de</strong> travail</em>, <em>un peu <strong>de</strong> "
                  "lait</em>, <em>assez <strong>d'</strong>argent</em>. Dus niet <em>beaucoup du "
                  "travail</em>."),
        ]),
        dict(kop="Het uur en de plaats", blokken=[
            ("p", "Het uur zeg je in het gewone gesprek met <em>et quart</em>, <em>et demie</em> en "
                  "<em>moins le quart</em>: <em>trois heures <strong>et quart</strong></em> is kwart "
                  "over drie, <em>trois heures moins le quart</em> is kwart voor drie."),
            ("fig", svg.naast_elkaar([svg.klok(3, 15), svg.klok(14, 30)]),
             "Links trois heures et quart, rechts quatorze heures trente."),
            ("p", "Officieel — in uurroosters, op tickets en in berichten — gebruikt het Frans de "
                  "<strong>24-urenklok</strong>: <em>quatorze heures trente</em> is "
                  "<strong>14.30 uur</strong>, dus half drie in de namiddag. En <em>à huit heures "
                  "moins dix</em> is tien voor acht."),
            ("fig", tabel(["Frans", "Wat het aangeeft"], [
                ["à côté de", "een plaats: naast"],
                ["en face de", "een plaats: tegenover"],
                ["au milieu de", "een plaats: midden in"],
                ["au-dessus de, en dessous de", "een plaats: boven, onder"],
                ["à cause de", "géén plaats maar een oorzaak"],
            ]), "Plaatsbepalingen, met de uitdrukking die er niet bij hoort."),
        ]),
        dict(kop="Het weer", blokken=[
            ("p", "Het weer staat in het Frans bijna altijd in een zin met "
                  "<strong><em>il fait</em></strong> of met een eigen werkwoord. <em>Il "
                  "<strong>fait</strong> doux</em> betekent dat het <strong>zacht</strong> weer is — "
                  "niet zonnig en warm, en ook niet dat het lichtjes regent."),
            ("fig", tabel(["Juist", "Nederlands"], [
                ["Il pleut. / Il va pleuvoir.", "Het regent. / Het gaat regenen."],
                ["Il neige.", "Het sneeuwt."],
                ["Il fait du vent.", "Het waait."],
                ["Il fait froid. / Il fait doux.", "Het is koud. / Het is zacht."],
                ["Il fait beau. / Il y a du soleil.", "Het is mooi weer. / Het is zonnig."],
                ["une prévision", "een voorspelling"],
            ]), "De vaste weerzinnen; il est froid bestaat niet, dat is altijd il fait froid."),
            ("weetje", "<em>Le temps</em> betekent in het Frans zowel <strong>het weer</strong> als "
                       "<strong>de tijd</strong>. <em>Quel temps fait-il ?</em> vraagt naar het weer, "
                       "<em>je n'ai pas le temps</em> gaat over tijd."),
        ]),
        buiten("lees of beluister een Frans weerbericht van vandaag en vertel het daarna in het Frans "
               "na in drie zinnen, met minstens één zin in de toekomst (il va…)."),
    ],
)


# ───────────────────────── 7. Zelfstandige naamwoorden, lidwoorden en determinanten
BUNDELS["zelfstandige-naamwoorden-lidwoorden-en-determinanten" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Zelfstandige naamwoorden, lidwoorden en determinanten",
    onder="De vier soorten lidwoorden, de samentrekkingen, het geslacht en het meervoud, en alles wat er nog voor een naamwoord kan staan.",
    secties=[
        dict(kop="Vier soorten lidwoorden", blokken=[
            ("fig", tabel(["Soort", "Vormen", "Wanneer"], [
                ["bepaald", "le, la, l', les", "iets dat bekend is: le livre que j'ai lu"],
                ["onbepaald", "un, une, des", "iets dat nieuw is: un livre, des livres"],
                ["deelaanduidend", "du, de la, de l', des", "een onbepaalde hoeveelheid: du pain"],
                ["na ontkenning of hoeveelheid", "de, d'", "pas de pain, beaucoup de pain"],
            ]), "De vier rijen die je uit elkaar moet houden."),
            ("p", "<em>L'</em> komt in de plaats van <em>le</em> of <em>la</em> voor een woord dat met "
                  "een <strong>klinker of een stomme h</strong> begint: <em><strong>L'</strong>hôtel "
                  "est fermé</em>, <em>l'eau</em>, <em>l'arbre</em>. Dat heeft niets met het geslacht "
                  "of met het aantal lettergrepen te maken."),
            ("weetje", "Het onbepaald lidwoord <strong>verdwijnt niet</strong> in het meervoud, zoals "
                       "bij ons: <em>un livre</em> wordt <em><strong>des</strong> livres</em>. "
                       "Nederlands 'boeken' zonder lidwoord bestaat in het Frans niet."),
        ]),
        dict(kop="Het deelaanduidend lidwoord", blokken=[
            ("p", "<em>Je mange <strong>du</strong> pain</em> betekent: ik eet brood, een "
                  "<strong>onbepaalde hoeveelheid</strong> ervan. Dat <em>du</em> is dus geen "
                  "samentrekking van <em>de</em> en <em>les</em>, geen bezittelijk voornaamwoord en "
                  "geen meervoud van <em>le</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["Je bois de l'eau.", "Ik drink water."],
                ["Il prend de la soupe.", "Hij neemt soep."],
                ["Elle achète du fromage.", "Zij koopt kaas."],
                ["Nous mangeons le riz chaque soir.", "Wij eten élke avond de rijst — bepaald, dus le."],
            ]), "Drie keer een onbepaalde hoeveelheid, en één bepaalde zin om naast te leggen."),
            ("p", "Na een <strong>ontkenning</strong> wordt dat lidwoord <strong><em>de</em></strong>: "
                  "<em>je mange du pain</em> wordt <em>je ne mange pas <strong>de</strong> pain</em>, "
                  "en <em>il a des frères</em> wordt <em>il n'a pas <strong>de</strong> frères</em>. "
                  "Na een <strong>hoeveelheid</strong> gebeurt hetzelfde: <em>trop "
                  "<strong>de</strong> travail</em>, <em>assez <strong>d'</strong>argent</em>."),
            ("kader", "<strong>Nog één geval:</strong> staat er een bijvoeglijk naamwoord vóór het "
                      "naamwoord in het meervoud, dan wordt <em>des</em> ook <em>de</em>. "
                      "<em>J'ai <strong>de</strong> belles chaussures</em>, niet <em>des belles "
                      "chaussures</em>."),
        ]),
        dict(kop="De samentrekkingen", blokken=[
            ("fig", tabel(["Samentrekking", "Wordt", "Voorbeeld"], [
                ["à + le", "au", "je vais au cinéma"],
                ["à + les", "aux", "je parle aux voisins"],
                ["de + le", "du", "je viens du magasin"],
                ["de + les", "des", "la clé des voitures"],
                ["à + la, de + la", "blijven staan", "à la gare, de la maison"],
            ]), "De vier samentrekkingen die bestaan, en de twee vormen die blijven."),
            ("p", "<em>Je vais <strong>au</strong> cinéma</em> dus, nooit <em>à le cinéma</em>. En "
                  "<em>dela</em> bestaat niet: dat blijft altijd <em>de la</em>."),
        ]),
        dict(kop="Het lidwoord bij lichaamsdelen", blokken=[
            ("p", "Hier doet het Frans iets anders dan het Nederlands. Bij een "
                  "<strong>lichaamsdeel</strong> staat meestal het <strong>bepaald lidwoord</strong>, "
                  "waar wij een bezittelijk voornaamwoord zetten."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["J'ai mal à la tête.", "Ik heb hoofdpijn (mijn hoofd doet pijn)."],
                ["Il se lave les mains.", "Hij wast zijn handen."],
                ["Elle s'est cassé le bras.", "Zij heeft haar arm gebroken."],
                ["Ouvrez les yeux.", "Open je ogen."],
            ]), "Vier zinnen met le of la waar het Nederlands mijn, zijn of haar zet."),
        ]),
        dict(kop="Geslacht en meervoud", blokken=[
            ("p", "Het <strong>geslacht</strong> van een Frans naamwoord moet je weten, want het "
                  "<strong>lidwoord en het bijvoeglijk naamwoord passen zich eraan aan</strong>. Bij "
                  "het lezen is dat zelfs een hulp: aan <em>la</em> of <em>une</em> zie je al dat het "
                  "woord vrouwelijk is, en aan <em>grande</em> dat het bij een vrouwelijk woord "
                  "hoort."),
            ("p", "De landen volgen dezelfde regel: <em><strong>la</strong> France</em>, <em>la "
                  "Belgique</em> en <em>la Suisse</em> zijn vrouwelijk, maar <em><strong>le</strong> "
                  "Canada</em> is mannelijk, net als <em>le Portugal</em> en <em>le Maroc</em>."),
            ("fig", tabel(["Uitgang", "Meervoud", "Voorbeeld"], [
                ["-al", "-aux", "un journal → des journaux"],
                ["-ail (soms)", "-aux", "un travail → des travaux"],
                ["-eau", "-eaux", "un gâteau → des gâteaux"],
                ["-eu", "-eux", "un cheveu → des cheveux"],
                ["onregelmatig", "—", "un œil → des yeux"],
            ]), "De meervoudsvormen die niet gewoon een -s krijgen."),
            ("weetje", "<em>Des oeils</em> bestaat niet: het meervoud van <em>un œil</em> is "
                       "<em>des <strong>yeux</strong></em>. En <strong>niet elk woord op een -e is "
                       "vrouwelijk</strong>: <em>le livre</em>, <em>un problème</em> en <em>un "
                       "musée</em> zijn mannelijk. <em>Un livre de poche</em> is dus mannelijk, al "
                       "eindigt het op een -e; <em>une livre</em> met <em>une</em> is iets heel "
                       "anders, namelijk een pond."),
        ]),
        dict(kop="Determinanten: alles wat nog voor een naamwoord kan staan", blokken=[
            ("p", "Een <strong>determinant</strong> is het woordje dat voor een naamwoord staat en "
                  "zegt over welk exemplaar het gaat. Het lidwoord is er één van; er zijn nog vier "
                  "soorten."),
            ("fig", tabel(["Soort", "Vormen", "Voorbeeld"], [
                ["aanwijzend", "ce, cet, cette, ces", "cet arbre est très vieux"],
                ["bezittelijk, één eigenaar", "mon, ton, son / ma, ta, sa / mes, tes, ses", "mon amie"],
                ["bezittelijk, meerdere eigenaars", "notre, votre, leur / nos, vos, leurs", "leurs cahiers"],
                ["vragend", "quel, quelle, quels, quelles", "quelle heure est-il ?"],
                ["onbepaald", "chaque, quelques, plusieurs, certains, tout", "chaque jour"],
            ]), "De vijf soorten determinanten met hun vormen."),
            ("p", "<em>Cet</em> gebruik je voor een mannelijk woord dat met een klinker begint: "
                  "<em><strong>Cet</strong> arbre</em>, <em>cet hôtel</em>. Wil je er nadruk op "
                  "leggen, dan hang je <strong>-ci</strong> of <strong>-là</strong> achter het "
                  "naamwoord: <em>ce livre-<strong>ci</strong></em> is <strong>dit boek hier</strong>, "
                  "<em>ce livre-là</em> dat boek daar."),
        ]),
        dict(kop="Het bezittelijk determinant: let op waarnaar het kijkt", blokken=[
            ("p", "Dit is de grootste valkuil van het hele hoofdstuk. Het Franse bezittelijk "
                  "determinant richt zich naar het <strong>ding dat bezeten wordt</strong>, niet naar "
                  "de <strong>eigenaar</strong>. Daarom betekent <em>sa maison</em> even goed "
                  "<strong>zijn huis</strong> als <strong>haar huis</strong>: <em>maison</em> is "
                  "vrouwelijk, dus <em>sa</em>, wie de eigenaar ook is."),
            ("p", "Om dezelfde reden is het <em><strong>mon</strong> amie</em> en niet <em>ma "
                  "amie</em>: voor een klinker neemt het Frans de mannelijke vorm, omdat <em>ma "
                  "amie</em> niet vlot klinkt. En bij meerdere eigenaars met meerdere dingen staat "
                  "<em>leurs</em>: <em>les élèves ont oublié <strong>leurs</strong> cahiers</em>."),
            ("weetje", "<em>Leur</em> bestaat twee keer. Vóór een <strong>naamwoord</strong> is het "
                       "een bezittelijk determinant (<em>leur maison</em>, hun huis); vóór een "
                       "<strong>werkwoord</strong> is het een voornaamwoord dat <em>aan hen</em> "
                       "betekent (<em>je leur parle</em>, ik praat met hen). Dat tweede krijgt nooit "
                       "een -s."),
        ]),
        dict(kop="Chaque, tout en de rangtelwoorden", blokken=[
            ("p", "<em>Chaque</em> betekent <strong>elk of ieder</strong> en staat "
                  "<strong>altijd</strong> bij een <strong>enkelvoud</strong>: <em>chaque jour</em>, "
                  "<em>chaque élève</em>. <em>Quelques</em> (enkele), <em>plusieurs</em> "
                  "(verschillende) en <em>certains</em> (sommige) staan bij een meervoud."),
            ("fig", tabel(["Vorm van tout", "Wanneer", "Voorbeeld"], [
                ["tout", "mannelijk enkelvoud", "tout le jour"],
                ["toute", "vrouwelijk enkelvoud", "toute la journée"],
                ["tous", "mannelijk meervoud", "tous les jours, je prends le bus"],
                ["toutes", "vrouwelijk meervoud", "toutes les semaines"],
            ]), "De vier vormen van tout; touts bestaat niet."),
            ("p", "<em>Tout le monde</em> betekent 'iedereen' en is in het Frans een "
                  "<strong>enkelvoud</strong>: <em>tout le monde <strong>est</strong> là</em>, niet "
                  "<em>sont</em>."),
            ("fig", tabel(["Getal", "Rangtelwoord", "Let op"], [
                ["un", "premier, première", "niet unième"],
                ["cinq", "cinquième", "met een u erbij"],
                ["neuf", "neuvième", "de f wordt een v"],
                ["onze", "onzième", "de e valt weg"],
                ["trois", "troisième", "la troisième fois, de derde keer"],
            ]), "De rangtelwoorden die het vaakst fout gespeld worden."),
            ("weetje", "Een <strong>datum</strong> krijgt in het Frans géén rangtelwoord: <em>le 2 "
                       "mai</em>, <em>le 15 août</em>. De enige uitzondering is de eerste van de "
                       "maand: <em>le 1<sup>er</sup> mai</em>."),
        ]),
        buiten("vertel in het Frans wat er bij jou thuis in de keuken staat, en gebruik daarbij "
               "minstens één keer du of de la, één keer ce of cette, en één keer leur of leurs."),
    ],
)


# ───────────────────────── 8. Voornaamwoorden: COD, COI, y en en
BUNDELS["voornaamwoorden-cod-coi-y-en-en" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Voornaamwoorden: COD, COI, y en en",
    onder="Wat le, lui, y en en vervangen, waar ze in de zin staan, en de betrekkelijke voornaamwoorden qui, que, dont en où.",
    secties=[
        dict(kop="De onderwerpsvormen", blokken=[
            ("p", "De rij waarmee alles begint: <strong>je, tu, il, elle, on, nous, vous, ils, "
                  "elles</strong>. Dat zijn de vormen die <strong>onderwerp</strong> van de zin zijn."),
            ("weetje", "<em>On</em> en <em>nous</em> betekenen in het gesproken Frans vaak hetzelfde, "
                       "maar <em>on</em> wordt <strong>als een enkelvoud vervoegd</strong>: <em>on "
                       "<strong>va</strong> au cinéma</em> tegenover <em>nous <strong>allons</strong> "
                       "au cinéma</em>."),
        ]),
        dict(kop="Het lijdend voorwerp (COD)", blokken=[
            ("p", "Het <strong>lijdend voorwerp</strong> is waarop de handeling valt. In <em>Marie "
                  "achète <strong>le livre</strong></em> is <em>le livre</em> het COD. Vervang je het "
                  "door een voornaamwoord, dan wordt het <em>le</em>, <em>la</em>, <em>l'</em> of "
                  "<em>les</em>, en het schuift <strong>vóór het vervoegde werkwoord</strong>: "
                  "<em>Marie <strong>l'</strong>achète</em>."),
            ("fig", svg.voornaamwoordplaats(),
             "Dezelfde zin in de twee talen, met het voorwerp in het geel."),
            ("fig", tabel(["Soort", "Vormen"], [
                ["onderwerp", "je, tu, il, elle, on, nous, vous, ils, elles"],
                ["lijdend voorwerp (COD)", "me, te, le, la, l', nous, vous, les"],
                ["meewerkend voorwerp (COI)", "me, te, lui, nous, vous, leur"],
                ["tonisch (na een voorzetsel)", "moi, toi, lui, elle, nous, vous, eux, elles"],
            ]), "De vier rijen persoonlijke voornaamwoorden."),
        ]),
        dict(kop="Het meewerkend voorwerp (COI)", blokken=[
            ("p", "Een <strong>meewerkend voorwerp</strong> herken je aan de "
                  "<strong><em>à</em></strong> die in de volle zin vóór de persoon staat: <em>je "
                  "téléphone <strong>à</strong> mes parents</em>. Dan gebruik je <em>lui</em> "
                  "(enkelvoud) of <em>leur</em> (meervoud): <em>je <strong>leur</strong> "
                  "téléphone</em>."),
            ("fig", tabel(["Juist", "Waarom"], [
                ["Je lui parle tous les jours.", "parler à quelqu'un, dus een COI"],
                ["Elle leur a répondu hier.", "répondre à quelqu'un, dus een COI"],
                ["Nous lui téléphonons ce soir.", "téléphoner à quelqu'un, dus een COI"],
                ["Je le vois à l'école.", "voir quelqu'un, zonder à, dus een COD — niet je lui vois"],
            ]), "Drie werkwoorden met à en één zonder."),
            ("p", "Het loont dus om bij een werkwoord te onthouden <strong>of er een à bij "
                  "hoort</strong>. <em>Parler à</em>, <em>répondre à</em>, <em>téléphoner à</em>, "
                  "<em>écrire à</em>, <em>donner à</em> nemen <em>lui</em> of <em>leur</em>; "
                  "<em>voir</em>, <em>regarder</em>, <em>aimer</em> en <em>acheter</em> nemen "
                  "<em>le</em>, <em>la</em> of <em>les</em>."),
        ]),
        dict(kop="Y en en", blokken=[
            ("p", "<strong><em>Y</em></strong> vervangt een <strong>plaats</strong>, of een groep met "
                  "<em>à</em> die <strong>geen persoon</strong> is: <em>je vais à Paris</em> wordt "
                  "<em>j'<strong>y</strong> vais</em>, <em>je pense à mon examen</em> wordt <em>j'y "
                  "pense</em>."),
            ("p", "<strong><em>En</em></strong> vervangt een groep die met <strong><em>de, du, de la "
                  "of des</em></strong> begint, en dus ook een <strong>hoeveelheid</strong>: "
                  "<em>j'ai trois frères</em> wordt <em>j'<strong>en</strong> ai trois</em>, <em>je "
                  "mange du pain</em> wordt <em>j'en mange</em>."),
            ("p", "Allebei staan ze, net als de andere voornaamwoorden, <strong>vóór</strong> het "
                  "vervoegde werkwoord. Alleen in de <strong>bevelende zin</strong> springen ze "
                  "erachter: <em>Vas-<strong>y</strong> !</em>, <em>Prends-<strong>en</strong> !</em>"),
        ]),
        dict(kop="Twee voornaamwoorden in één zin", blokken=[
            ("p", "Staan er twee samen, dan ligt de volgorde vast. <em>Il <strong>me le</strong> "
                  "donne</em>: <em>me</em> komt vóór <em>le</em>."),
            ("fig", svg.stappen([
                "me, te|nous, vous, se",
                "le, la|les",
                "lui|leur",
                "y",
                "en",
            ]), "De vaste volgorde van de voornaamwoorden vóór het werkwoord."),
            ("fig", tabel(["Juist", "Fout"], [
                ["Je te le dis.", "Je le te dis."],
                ["Il le lui a donné.", "Je lui le donne."],
                ["Elle nous en parle.", "Elle en nous parle."],
                ["Il m'y emmène.", "Il y me emmène."],
            ]), "Vier zinnen in de juiste volgorde, met de fout ernaast."),
            ("weetje", "In de <strong>bevelende zin</strong> staan de voornaamwoorden "
                       "<strong>achter</strong> het werkwoord, met streepjes ertussen, en wordt "
                       "<em>me</em> dan <em>moi</em>: <em>Donne-<strong>le-moi</strong> !</em>"),
        ]),
        dict(kop="Na een voorzetsel: de tonische vormen", blokken=[
            ("p", "Na een voorzetsel zoals <em>avec</em>, <em>chez</em>, <em>pour</em> of <em>sans</em> "
                  "kan je <strong>niet</strong> <em>je</em>, <em>tu</em> of <em>il</em> gebruiken. Daar "
                  "staan de <strong>tonische</strong> vormen: <strong>moi, toi, lui, elle, nous, "
                  "vous, eux, elles</strong>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["Je viens avec toi.", "Ik kom met jou."],
                ["On va chez eux.", "We gaan bij hen thuis."],
                ["C'est pour moi ?", "Is dat voor mij?"],
                ["Elle part sans lui.", "Zij vertrekt zonder hem."],
            ]), "Vier zinnen waarin het voorzetsel de tonische vorm oplegt."),
        ]),
        dict(kop="De wederkerende voornaamwoorden", blokken=[
            ("p", "<em>Je <strong>me</strong> lève tôt</em>, <em>nous <strong>nous</strong> "
                  "dépêchons</em>, <em>tu <strong>te</strong> souviens de lui ?</em> — het "
                  "wederkerend voornaamwoord verandert mee met het onderwerp en staat vóór het "
                  "werkwoord."),
            ("p", "Soms betekent dat <em>se</em> niet 'zichzelf' maar <strong>elkaar</strong>: "
                  "<em>Les élèves <strong>se</strong> sont écrit toute l'année</em> betekent dat ze "
                  "<strong>aan elkaar</strong> schreven, niet aan zichzelf. Het verband in de zin "
                  "zegt je welke van de twee het is."),
        ]),
        dict(kop="De betrekkelijke voornaamwoorden: qui, que, dont, où", blokken=[
            ("p", "Deze vier noemt de vakfiche met name, en ze zijn niet uitwisselbaar. Welk je kiest, "
                  "hangt af van de <strong>rol</strong> die het woord in de <strong>bijzin</strong> "
                  "speelt."),
            ("fig", tabel(["Voornaamwoord", "Rol in de bijzin", "Voorbeeld"], [
                ["qui", "onderwerp", "la femme qui parle"],
                ["que", "lijdend voorwerp", "le livre que je lis est passionnant"],
                ["dont", "er hoort een de bij het werkwoord of het naamwoord", "le livre dont j'ai besoin"],
                ["où", "een plaats of een tijdstip", "c'est le jour où tout a changé"],
            ]), "De vier betrekkelijke voornaamwoorden met hun rol."),
            ("p", "<em>Que</em> verkort voor een klinker tot <em>qu'</em>, maar <em>qui</em> "
                  "<strong>nooit</strong>: <em>la femme <strong>qui</strong> arrive</em>, niet "
                  "<em>qu'arrive</em>."),
            ("p", "<em>Dont</em> gebruik je zodra er in de bijzin een <em>de</em> bij hoort: <em>avoir "
                  "besoin <strong>de</strong></em> geeft <em>le livre dont j'ai besoin</em>, "
                  "<em>parler <strong>de</strong></em> geeft <em>l'ami dont je t'ai parlé</em>, en "
                  "<em>venir <strong>de</strong></em> geeft <em>la ville dont il vient</em>. Maar "
                  "<em>habiter</em> heeft geen <em>de</em>: dat wordt <em>la maison <strong>où</strong> "
                  "j'habite</em>."),
            ("weetje", "<em>Ce qui</em> en <em>ce que</em> verwijzen niet naar één naamwoord maar naar "
                       "een <strong>heel idee</strong>: <em>Je ne comprends pas <strong>ce qui</strong> "
                       "s'est passé</em> — ik begrijp niet wat er gebeurd is."),
        ]),
        dict(kop="Voornaamwoorden die alleen kunnen staan", blokken=[
            ("fig", tabel(["Soort", "Vormen", "Voorbeeld"], [
                ["bezittelijk", "le mien, la tienne, le sien, les leurs",
                 "C'est ta voiture ? — Oui, c'est la mienne."],
                ["aanwijzend", "celui, celle, ceux, celles",
                 "Ton livre préféré ? — Celui de Camus."],
                ["neutraal aanwijzend", "ce, ceci, cela, ça", "Cela m'étonne."],
                ["onbepaald", "quelqu'un, personne, rien, tout",
                 "Il n'y a personne dans la salle."],
                ["vragend", "qui, que, quoi, lequel, laquelle, lesquels, lesquelles",
                 "Qui a téléphoné ?"],
            ]), "Vijf soorten voornaamwoorden die zonder naamwoord naast zich staan."),
            ("p", "Het <strong>bezittelijke</strong> voornaamwoord past zich aan het "
                  "<strong>bezeten ding</strong> aan: een auto is vrouwelijk, dus <em>c'est "
                  "<strong>la mienne</strong></em>. En <em>ce sac n'est pas le mien, c'est "
                  "<strong>le sien</strong></em>: een zak is mannelijk."),
            ("p", "<em>Celui</em> vervangt een naamwoord dat al genoemd is: <em>Quel est ton livre "
                  "préféré ? — <strong>Celui</strong> de Camus</em> betekent 'dat van Camus', waarbij "
                  "<em>celui</em> het woord <em>livre</em> vervangt. <em>Cette</em> hoort daar niet "
                  "bij: dat staat altijd vóór een naamwoord."),
            ("weetje", "<em>Cela</em> is de <strong>verzorgde</strong> vorm en <em>ça</em> de "
                       "<strong>spreektaal</strong> — net omgekeerd aan wat veel mensen denken. In een "
                       "schrijfopdracht schrijf je dus liever <em>cela</em>."),
            ("p", "<em>Lequel</em> is het enige <strong>vragende</strong> woord in dat rijtje, en het "
                  "past zich aan in geslacht en getal: <em>laquelle</em>, <em>lesquels</em>, "
                  "<em>lesquelles</em>. <em>Quelqu'un</em>, <em>personne</em> en <em>rien</em> zijn "
                  "onbepaald."),
        ]),
        dict(kop="Bij het lezen: wie doet wat aan wie?", blokken=[
            ("p", "De voornaamwoorden zijn niet alleen grammatica, ze beslissen wat een zin betekent. "
                  "<em>Sophie a rencontré Paul. <strong>Elle lui</strong> a tout raconté.</em> "
                  "<em>Elle</em> is het onderwerp en dus Sophie; <em>lui</em> is het meewerkend "
                  "voorwerp en dus Paul. <strong>Sophie vertelde alles aan Paul</strong>, en niet "
                  "omgekeerd."),
            ("kader", "<strong>Doe dit bij elke moeilijke zin.</strong> Zoek eerst het onderwerp, dan "
                      "het werkwoord, en vraag je daarna af waar elk voornaamwoord naar terugwijst. "
                      "Negen van de tien keer zit de moeilijkheid daar, en niet in de woordenschat."),
        ]),
        buiten("vertel in het Frans aan iemand over een cadeau: wie gaf het aan wie, en gebruik "
               "daarbij minstens één keer lui of leur en één keer en."),
    ],
)


# ───────────────────────── 9. Bijvoeglijke naamwoorden, bijwoorden en de trappen
BUNDELS["bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Bijvoeglijke naamwoorden, bijwoorden en de trappen",
    onder="De vrouwelijke en meervoudsvormen, waar het bijvoeglijk naamwoord staat, hoe je er een bijwoord van maakt en hoe je vergelijkt.",
    secties=[
        dict(kop="De vrouwelijke vorm", blokken=[
            ("p", "De gewone regel is eenvoudig: je zet er een <strong>-e</strong> achter. "
                  "<em>grand</em> wordt <em>grand<strong>e</strong></em>, <em>ouvert</em> wordt "
                  "<em>ouvert<strong>e</strong></em>: <em>la porte est <strong>ouverte</strong></em>."),
            ("fig", tabel(["Uitgang", "Vrouwelijk", "Voorbeeld"], [
                ["-eux", "-euse", "heureux → heureuse"],
                ["-if", "-ive", "sportif → sportive"],
                ["-c", "-che", "blanc → blanche"],
                ["-er", "-ère", "cher → chère"],
                ["-el, -eil", "-elle, -eille", "nouvel → nouvelle"],
                ["al een -e", "blijft gelijk", "jeune → jeune, facile → facile"],
            ]), "De uitgangen die niet gewoon een -e krijgen."),
            ("p", "<em>Une histoire <strong>heureuse</strong></em> dus, en <em>une fille "
                  "sportive</em>. Een bijvoeglijk naamwoord dat al op een <strong>-e</strong> "
                  "eindigt, krijgt er <strong>geen tweede</strong> bij: <em>un jeune homme</em>, "
                  "<em>une jeune femme</em>."),
        ]),
        dict(kop="Drie woorden met een extra vorm", blokken=[
            ("p", "<em>Beau</em>, <em>nouveau</em> en <em>vieux</em> hebben een "
                  "<strong>aparte mannelijke vorm</strong> voor een woord dat met een "
                  "<strong>klinker</strong> begint, omdat de gewone vorm daar niet vlot klinkt."),
            ("fig", tabel(["Mannelijk", "Voor een klinker", "Vrouwelijk", "Mannelijk meervoud"], [
                ["beau", "bel (un bel homme)", "belle", "beaux"],
                ["nouveau", "nouvel (un nouvel ami)", "nouvelle", "nouveaux"],
                ["vieux", "vieil (un vieil arbre)", "vieille", "vieux"],
            ]), "De drie woorden met vier vormen elk."),
            ("p", "<em>Les <strong>nouvelles</strong> maisons</em> is dus juist: <em>maison</em> is "
                  "vrouwelijk, dus het meervoud is <em>nouvelles</em>. En <em>petit</em> doet hier "
                  "niet aan mee: <em>petil</em> bestaat niet."),
        ]),
        dict(kop="Het meervoud", blokken=[
            ("fig", tabel(["Uitgang", "Meervoud", "Voorbeeld"], [
                ["gewoon", "+ s", "gentil → gentils"],
                ["-eau", "-eaux", "beau → beaux"],
                ["-al", "-aux", "national → nationaux"],
                ["-x of -s", "blijft gelijk", "heureux → heureux, gris → gris"],
            ]), "De meervoudsvormen van het bijvoeglijk naamwoord."),
            ("p", "<em>Heureuxs</em> bestaat dus niet: een woord dat al op een <strong>-x</strong> "
                  "eindigt, verandert niet. In het vrouwelijk meervoud komt er wel gewoon een -s bij: "
                  "<em>des fêtes <strong>nationales</strong></em>."),
        ]),
        dict(kop="Waar staat het bijvoeglijk naamwoord?", blokken=[
            ("p", "In het Frans staat het bijvoeglijk naamwoord <strong>meestal achter</strong> het "
                  "naamwoord: <em>une voiture rouge</em>, <em>un film intéressant</em>. Dat is net "
                  "omgekeerd aan het Nederlands, en het is de eerste gewoonte die je moet afleren."),
            ("p", "Een klein groepje korte, veelgebruikte woorden staat er wél <strong>voor</strong>: "
                  "<strong>grand, petit, jeune, vieux, beau, bon, nouveau, joli, gros</strong>. "
                  "<em>Intéressant</em> hoort daar niet bij."),
            ("kader", "<strong>Soms verandert de plaats de betekenis.</strong> <em>Un homme "
                      "<strong>grand</strong></em> is een man die groot van gestalte is; <em>un "
                      "<strong>grand</strong> homme</em> is een groot man in de zin van belangrijk. "
                      "Hetzelfde woord, twee betekenissen, en alleen de plaats zegt welke."),
            ("weetje", "Staat zo'n woord vóór een naamwoord in het meervoud, dan wordt <em>des</em> "
                       "ook <em>de</em>: <em><strong>de</strong> vieux livres</em>, <em>de belles "
                       "chaussures</em>."),
        ]),
        dict(kop="De overeenkomst", blokken=[
            ("p", "Een bijvoeglijk naamwoord na <em>être</em>, <em>sembler</em> of <em>paraître</em> "
                  "komt overeen met het <strong>onderwerp</strong> van de zin: <em>Les filles sont "
                  "heureus<strong>es</strong></em>, <em>Marie semble fatigué<strong>e</strong></em>, "
                  "<em>Les garçons sont grand<strong>s</strong></em>. <em>Elles sont content</em> is "
                  "dus fout: dat moet <em>content<strong>es</strong></em> zijn."),
            ("p", "Bij een <strong>gemengde groep</strong> wint het mannelijk meervoud, ook als er "
                  "maar één jongen bij is: één jongen en drie meisjes geeft <em><strong>Ils</strong> "
                  "sont parti<strong>s</strong></em>."),
            ("p", "Die uitgangen zijn bij het <strong>lezen</strong> een hulp: ze "
                  "<strong>verraden bij welk naamwoord</strong> het woord hoort. Staat er "
                  "<em>grandes</em> in een lange zin, dan weet je dat het bij een vrouwelijk meervoud "
                  "hoort, en dat scheelt zoeken."),
        ]),
        dict(kop="Van bijvoeglijk naamwoord naar bijwoord", blokken=[
            ("p", "Een <strong>bijwoord</strong> zegt hoe iets gebeurt. In het Frans maak je het "
                  "meestal door <strong>-ment</strong> achter de <strong>vrouwelijke</strong> vorm te "
                  "zetten."),
            ("fig", svg.stappen([
                "doux|mannelijk",
                "douce|vrouwelijk",
                "doucement|bijwoord",
            ]), "De drie stappen van bijvoeglijk naamwoord naar bijwoord."),
            ("fig", tabel(["Bijvoeglijk naamwoord", "Bijwoord"], [
                ["rapide", "rapidement"],
                ["facile", "facilement"],
                ["vrai", "vraiment"],
                ["doux, douce", "doucement — elle parle doucement"],
                ["bon", "bien (niet bonment)"],
                ["mauvais", "mal"],
            ]), "Zes bijwoorden, met de twee onregelmatige onderaan."),
            ("p", "Een bijwoord is <strong>onveranderlijk</strong>: het verandert nooit mee met het "
                  "geslacht of het getal van het onderwerp. <em>Elles parlent doucement</em>, zonder "
                  "-s."),
            ("fig", tabel(["Bijwoord", "Nederlands"], [
                ["toujours", "altijd"],
                ["souvent", "vaak"],
                ["parfois, quelquefois", "soms"],
                ["rarement", "zelden"],
                ["jamais", "nooit"],
                ["lentement", "traag — dat zegt hoe, niet hoe vaak"],
            ]), "Bijwoorden van frequentie, met één van wijze erbij."),
            ("weetje", "In een <strong>samengestelde tijd</strong> staat een kort bijwoord "
                       "<strong>tussen het hulpwerkwoord en het deelwoord</strong>: <em>j'ai "
                       "<strong>souvent</strong> mangé ici</em>, niet <em>j'ai mangé souvent ici</em>."),
        ]),
        dict(kop="Vergelijken: de trappen", blokken=[
            ("fig", tabel(["Trap", "Vorm", "Voorbeeld"], [
                ["meer", "plus … que", "Il est plus rapide que moi."],
                ["minder", "moins … que", "Ce film est moins intéressant que l'autre."],
                ["even", "aussi … que", "Tu es aussi fort que ton frère."],
                ["de meeste", "le/la/les plus …", "la plus belle ville"],
                ["de minste", "le/la/les moins …", "le moins cher"],
            ]), "De vijf vormen om te vergelijken."),
            ("p", "Bij de <strong>overtreffende</strong> trap past het <strong>lidwoord</strong> zich "
                  "aan het naamwoord aan: <em><strong>la</strong> plus belle ville</em>, "
                  "<em><strong>le</strong> plus intéressant</em>. <em>Très intéressant</em> is geen "
                  "overtreffende trap maar gewoon 'heel interessant'."),
            ("fig", tabel(["Woord", "Vergrotende trap", "Let op"], [
                ["bon (goed, bij een naamwoord)", "meilleur", "c'est le meilleur restaurant de la ville"],
                ["bien (goed, bij een werkwoord)", "mieux", "elle chante mieux que sa sœur"],
                ["mauvais (slecht)", "pire", "c'est pire que je pensais"],
            ]), "De drie onregelmatige trappen."),
            ("p", "<em>Plus bon</em> en <em>plus mieux</em> bestaan niet, net zoals wij geen 'goeder' "
                  "zeggen. En hou <em>meilleur</em> en <em>mieux</em> uit elkaar: "
                  "<strong>meilleur</strong> hoort bij een <strong>naamwoord</strong> (<em>une "
                  "meilleure voix</em>), <strong>mieux</strong> bij een <strong>werkwoord</strong> "
                  "(<em>chanter mieux</em>). <em>Pire</em> hoort bij <em>mauvais</em>, niet bij "
                  "<em>bon</em>."),
        ]),
        dict(kop="Hoeveelheden vergelijken", blokken=[
            ("p", "Vergelijk je een <strong>hoeveelheid</strong>, dan komt er een <strong><em>de</em> "
                  "zonder lidwoord</strong> bij: <em>J'ai <strong>plus de</strong> livres que "
                  "toi</em>, niet <em>plus livres</em> en niet <em>plus des livres</em>."),
            ("fig", tabel(["Uitdrukking", "Wat ze vergelijkt"], [
                ["plus de … que", "een hoeveelheid: meer"],
                ["moins de … que", "een hoeveelheid: minder"],
                ["autant de … que", "een hoeveelheid: evenveel"],
                ["aussi … que", "een eigenschap: even — dus zonder de"],
            ]), "Drie uitdrukkingen voor hoeveelheden, en één voor een eigenschap."),
            ("p", "Staat er geen naamwoord bij, dan vergelijk je hoe <strong>sterk</strong> iets "
                  "gebeurt: <em>Elle travaille <strong>le plus</strong> de toute la classe</em> "
                  "betekent dat zij <strong>het hardst werkt van de hele klas</strong>."),
        ]),
        buiten("vergelijk in het Frans twee plaatsen die je kent, hardop en in vier zinnen, met één "
               "keer plus, één keer moins, één keer aussi en één keer meilleur of mieux."),
    ],
)


# ───────────────────────── 10. Présent, impératif en de wederkerende werkwoorden
BUNDELS["present-imperatif-en-de-wederkerende-werkwoorden" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Présent, impératif en de wederkerende werkwoorden",
    onder="De tegenwoordige tijd van de drie groepen, de bevelende vorm, de werkwoorden met se, en de twee tijden vlak voor en vlak na nu.",
    secties=[
        dict(kop="De présent van de regelmatige werkwoorden", blokken=[
            ("fig", tabel(["Persoon", "-er: parler", "-ir: finir", "-re: vendre"], [
                ["je", "parle", "finis", "vends"],
                ["tu", "parles", "finis", "vends"],
                ["il, elle, on", "parle", "finit", "vend"],
                ["nous", "parlons", "finissons", "vendons"],
                ["vous", "parlez", "finissez", "vendez"],
                ["ils, elles", "parlent", "finissent", "vendent"],
            ]), "De drie groepen regelmatige werkwoorden naast elkaar."),
            ("p", "De uitgangen van de <strong>-er</strong>-werkwoorden zijn "
                  "<strong>-e, -es, -e, -ons, -ez, -ent</strong>. <em>Nous "
                  "<strong>parlons</strong> français à la maison.</em> Werkwoorden op "
                  "<strong>-ir</strong> zoals <em>finir</em> schuiven in het meervoud een "
                  "<strong>-iss-</strong> in hun stam: <em>nous finissons</em>."),
            ("weetje", "<em>Je parle</em>, <em>tu parles</em> en <em>ils parlent</em> klinken in het "
                       "Frans <strong>precies hetzelfde</strong>: de uitgang <strong>-ent</strong> "
                       "van <em>ils</em> en <em>elles</em> <strong>hoor je niet</strong>. Alleen "
                       "<em>nous parlons</em> en <em>vous parlez</em> klinken anders. Bij het "
                       "luisteren moet je dus uit de zin halen wie er bedoeld wordt."),
        ]),
        dict(kop="De onregelmatige werkwoorden", blokken=[
            ("fig", tabel(["Werkwoord", "Présent"], [
                ["être", "suis, es, est, sommes, êtes, sont"],
                ["avoir", "ai, as, a, avons, avez, ont"],
                ["aller", "vais, vas, va, allons, allez, vont"],
                ["faire", "fais, fais, fait, faisons, faites, font"],
                ["dire", "dis, dis, dit, disons, dites, disent"],
                ["prendre", "prends, prends, prend, prenons, prenez, prennent"],
            ]), "De zes werkwoorden die in elke tekst terugkomen."),
            ("p", "<em>Vous <strong>êtes</strong> en retard</em>: let op die vorm. Drie werkwoorden "
                  "hebben bij <em>vous</em> de uitgang <strong>-tes</strong> in plaats van "
                  "<em>-ez</em>: <em><strong>êtes</strong></em>, <em><strong>faites</strong></em> en "
                  "<em><strong>dites</strong></em>. <em>Avoir</em> doet daar niet aan mee: dat is "
                  "gewoon <em>avez</em>."),
            ("p", "Sommige werkwoorden veranderen van <strong>stam</strong>: <em>prendre</em> geeft "
                  "<em>ils <strong>prennent</strong> le bus tous les jours</em>, <em>venir</em> geeft "
                  "<em>ils viennent</em>, <em>pouvoir</em> geeft <em>ils peuvent</em>. <em>Chanter</em> "
                  "is dan weer kurkdroog regelmatig."),
            ("weetje", "Het Frans heeft <strong>geen</strong> aparte vorm voor 'ik ben aan het lezen', "
                       "zoals het Engels met <em>I am reading</em>. <em>Je lis</em> dekt allebei. Wil "
                       "je toch benadrukken dat je ermee bezig bent, dan zeg je <em>je suis en train "
                       "de lire</em>."),
        ]),
        dict(kop="Vervoegd of infinitief?", blokken=[
            ("p", "<em>Il parle</em> is <strong>vervoegd</strong> (het hoort bij <em>il</em>), "
                  "<em>parler</em> is de <strong>infinitief</strong>, de vorm die in het woordenboek "
                  "staat. Welke van de twee je nodig hebt, hangt af van wat ervoor staat."),
            ("fig", tabel(["Na dit woord", "Komt", "Voorbeeld"], [
                ["pour, sans, avant de", "een infinitief", "pour partir, sans manger"],
                ["il faut", "een infinitief", "il faut partir maintenant"],
                ["pouvoir, vouloir, devoir, aimer", "een infinitief, rechtstreeks", "je veux lire un livre"],
                ["essayer de, oublier de, décider de", "de + infinitief", "j'essaie de comprendre"],
                ["commencer à, apprendre à, réussir à", "à + infinitief", "je commence à comprendre"],
                ["que", "een vervoegd werkwoord", "je pense que tu as raison"],
            ]), "Wat er na elk woord volgt."),
            ("p", "<em>Je veux <strong>lire</strong> un livre</em> dus, en niet <em>je veux de "
                  "partir</em>: na <em>vouloir</em> komt de infinitief <strong>rechtstreeks</strong>. "
                  "Na <em>que</em> komt er daarentegen altijd een <strong>vervoegd</strong> werkwoord."),
        ]),
        dict(kop="Moeten: il faut of devoir?", blokken=[
            ("p", "<em>Il faut partir maintenant</em> drukt een <strong>verplichting</strong> uit, "
                  "maar laat <strong>open wie</strong> moet. <em>Il <strong>doit</strong> partir</em> "
                  "zegt wel wie: hij. Dat is het hele verschil."),
            ("p", "<em>Il faut</em> is een <strong>onpersoonlijk</strong> werkwoord: die <em>il</em> "
                  "verwijst naar niemand. Dat geldt ook voor <em>il pleut</em> en <em>il neige</em>. "
                  "In <em>il part</em> is die <em>il</em> wel een echte persoon."),
        ]),
        dict(kop="De impératif: de bevelende vorm", blokken=[
            ("p", "De impératif heeft in het Frans maar <strong>drie</strong> vormen, en je laat het "
                  "onderwerp weg: <em>parle</em> (tu), <em>parlons</em> (nous), <em>parlez</em> "
                  "(vous). Bij een <strong>-er</strong>-werkwoord valt de <strong>-s</strong> van "
                  "<em>tu</em> weg: <em><strong>Regarde</strong> ce film !</em>"),
            ("fig", tabel(["Werkwoord", "tu", "nous", "vous"], [
                ["parler", "parle", "parlons", "parlez"],
                ["finir", "finis", "finissons", "finissez"],
                ["être", "sois", "soyons", "soyez"],
                ["avoir", "aie", "ayons", "ayez"],
                ["savoir", "sache", "sachons", "sachez"],
            ]), "De regelmatige vormen bovenaan, de drie onregelmatige eronder."),
            ("p", "Een <strong>ontkennend</strong> bevel zet <em>ne</em> en <em>pas</em> gewoon rond "
                  "het werkwoord: <em><strong>Ne</strong> parlez <strong>pas</strong>.</em> En een "
                  "<strong>voornaamwoord</strong> staat in een <strong>bevestigend</strong> bevel "
                  "<strong>achter</strong> het werkwoord, met een streepje: <em>Donne-le-moi !</em>, "
                  "<em><strong>Lève-toi</strong> !</em>"),
        ]),
        dict(kop="De wederkerende werkwoorden", blokken=[
            ("p", "Een wederkerend werkwoord heeft <strong>altijd</strong> een voornaamwoord bij zich "
                  "dat naar het <strong>onderwerp</strong> verwijst: <em>je <strong>me</strong> "
                  "lève</em>, <em>tu <strong>te</strong> lèves</em>, <em>il <strong>se</strong> "
                  "lève</em>, <em>nous <strong>nous</strong> dépêchons</em>, <em>vous <strong>vous</strong> "
                  "levez</em>, <em>elles <strong>s'</strong>habillent vite le matin</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["se lever", "opstaan — bij ons zonder 'zich'"],
                ["se promener", "wandelen — bij ons zonder 'zich'"],
                ["se souvenir de", "zich herinneren"],
                ["se dépêcher", "zich haasten"],
                ["s'habiller", "zich aankleden"],
                ["regarder", "kijken — niet wederkerend"],
            ]), "Werkwoorden die in het Frans wederkerend zijn en in het Nederlands vaak niet."),
            ("p", "<em>Nous dépêchons</em> of <em>nous se dépêchons</em> bestaat dus niet: het "
                  "voornaamwoord moet mee veranderen met het onderwerp. En in de <strong>passé "
                  "composé</strong> gaat een wederkerend werkwoord <strong>altijd met "
                  "<em>être</em></strong>: <em>je me suis levé</em>, nooit <em>j'ai me levé</em>."),
        ]),
        dict(kop="Vlak voor nu en vlak na nu", blokken=[
            ("p", "Twee tijden die je met een hulpwerkwoord in de présent maakt, en die je dus nu al "
                  "kan gebruiken."),
            ("fig", svg.franse_tijden(),
             "De tijden van de vakfiche op één lijn, met maintenant in het midden."),
            ("p", "De <strong>futur proche</strong> is <em>aller</em> in de présent plus een "
                  "<strong>infinitief</strong>: <em>nous <strong>allons</strong> manger</em>, "
                  "<em>je vais partir</em>. Het gaat over iets dat <strong>zo meteen</strong> "
                  "gebeurt."),
            ("p", "De <strong>passé récent</strong> is <em>venir <strong>de</strong></em> plus een "
                  "infinitief, en gaat over iets dat <strong>net gebeurd</strong> is: <em>je viens de "
                  "finir</em>, <em>elle vient de partir</em>, <em>nous venons d'arriver</em>. Die "
                  "<em>de</em> mag je niet laten vallen: <em>il vient finir</em> betekent iets anders. "
                  "En <em>je viens de manger</em> betekent dus <strong>ik heb net gegeten</strong>, "
                  "niet dat ik zo meteen ga eten."),
        ]),
        dict(kop="Wijzen en tijden", blokken=[
            ("p", "De vakfiche spreekt over <strong>wijzen</strong> en <strong>tijden</strong>, en "
                  "dat is niet hetzelfde. Een <strong>wijze</strong> zegt <strong>hoe</strong> je "
                  "iets voorstelt: als een bevel (<em>l'impératif</em>), als iets onzekers "
                  "(<em>le subjonctif</em>), als een voorwaarde (<em>le conditionnel</em>). Een "
                  "<strong>tijd</strong> zegt <strong>wanneer</strong> het gebeurt: <em>le "
                  "présent</em>, <em>l'imparfait</em>, <em>le futur</em>."),
            ("kader", "<strong>Bij het lezen helpt de vorm je meteen vooruit.</strong> Zie je "
                      "<em>allez</em> staan, dan weet je zeker dat het werkwoord "
                      "<strong>vervoegd</strong> is — bij <em>vous</em>, of als een bevel. Een "
                      "infinitief ziet er anders uit (<em>aller</em>), en een verleden tijd ook."),
        ]),
        buiten("vertel in het Frans wat je straks nog gaat doen en wat je net gedaan hebt, met één "
               "keer je vais en één keer je viens de."),
    ],
)


# ───────────────────────── 11. Passé composé, imparfait en plus-que-parfait
BUNDELS["passe-compose-imparfait-en-plus-que-parfait" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Passé composé, imparfait en plus-que-parfait",
    onder="De drie verleden tijden: welke gebeurtenis, welk decor en wat er daarvóór al gebeurd was.",
    secties=[
        dict(kop="De passé composé", blokken=[
            ("p", "De passé composé bestaat uit <strong>twee delen</strong>: een "
                  "<strong>hulpwerkwoord in de présent</strong> (<em>avoir</em> of <em>être</em>) plus "
                  "een <strong>voltooid deelwoord</strong>. <em>Hier, j'<strong>ai</strong> mangé au "
                  "restaurant.</em>"),
            ("fig", tabel(["Soort werkwoord", "Deelwoord", "Voorbeeld"], [
                ["-er", "-é", "manger → mangé, parler → parlé"],
                ["-ir", "-i", "finir → fini"],
                ["-re", "-u", "vendre → vendu"],
                ["onregelmatig", "—", "prendre → pris, voir → vu, faire → fait"],
                ["onregelmatig", "—", "avoir → eu, être → été, mettre → mis"],
                ["onregelmatig", "—", "écrire → écrit, dire → dit, lire → lu"],
            ]), "De drie regelmatige vormen en de deelwoorden die je uit het hoofd moet kennen."),
            ("p", "<em>Faisé</em> bestaat dus niet: <em>faire</em> geeft <em><strong>fait</strong></em>. "
                  "En het deelwoord van <em>être</em> is <em><strong>été</strong></em>, niet "
                  "<em>eu</em> — dat laatste is het deelwoord van <em>avoir</em>."),
            ("p", "De <strong>ontkenning</strong> zet <em>ne</em> en <em>pas</em> rond het "
                  "<strong>hulpwerkwoord</strong>, niet rond het deelwoord: <em>Je <strong>n'</strong>ai "
                  "<strong>pas</strong> mangé.</em>"),
        ]),
        dict(kop="Avoir of être?", blokken=[
            ("p", "De meeste werkwoorden nemen <strong>avoir</strong>. Een kleine groep "
                  "<strong>bewegingswerkwoorden</strong> neemt <strong>être</strong>, en die groep "
                  "zit vol tegengestelde paren."),
            ("fig", tabel(["Paar", "Betekenis"], [
                ["aller — venir", "gaan — komen"],
                ["entrer — sortir", "binnengaan — buitengaan"],
                ["monter — descendre", "naar boven — naar beneden"],
                ["arriver — partir", "aankomen — vertrekken"],
                ["naître — mourir", "geboren worden — sterven"],
                ["rester, tomber, rentrer", "blijven, vallen, terugkeren — zonder tegenhanger"],
            ]), "De être-groep; naître en rester vormen géén paar."),
            ("p", "Daarbovenop gaan <strong>alle wederkerende werkwoorden</strong> met <em>être</em>: "
                  "<em>je me suis levé</em>, <em>ils s'étaient levés</em>. Dat is zonder "
                  "uitzondering."),
            ("weetje", "Krijgt zo'n bewegingswerkwoord een <strong>lijdend voorwerp</strong>, dan "
                       "schakelt het over op <em>avoir</em>. <em>Il <strong>est</strong> monté</em> "
                       "(hij is naar boven gegaan) tegenover <em>Il <strong>a</strong> monté les "
                       "valises</em> (hij heeft de koffers naar boven gedragen). Zo ook <em>elle est descendue</em> tegenover "
                       "<em>elle a descendu la poubelle</em>. Allebei juist, maar "
                       "ze betekenen iets anders."),
        ]),
        dict(kop="De overeenkomst van het deelwoord", blokken=[
            ("p", "Dit is de regel die op een examen het vaakst punten kost. Met "
                  "<strong>être</strong> komt het deelwoord overeen met het "
                  "<strong>onderwerp</strong>; met <strong>avoir</strong> "
                  "<strong>niet</strong>."),
            ("fig", tabel(["Juist", "Waarom"], [
                ["Elle est partie.", "être, vrouwelijk enkelvoud, dus -e"],
                ["Elles sont arrivées.", "être, vrouwelijk meervoud, dus -es"],
                ["Ils sont venus hier.", "être, mannelijk meervoud, dus -s"],
                ["Nous sommes restés une heure.", "être, meervoud, dus -s"],
                ["Elle est née en 2008.", "être, vrouwelijk, dus née"],
                ["Elles ont parlé longtemps.", "avoir, dus géén overeenkomst"],
            ]), "Vijf keer être met overeenkomst, en één keer avoir zonder."),
            ("p", "<em>Elles ont parties</em> is dus dubbel fout: <em>partir</em> gaat met "
                  "<em>être</em>, en na <em>avoir</em> zou er geen -s staan. Juist is <em>elles sont "
                  "<strong>parties</strong></em>. En <em>nous <strong>sommes</strong> rentrés tard "
                  "hier soir</em>, met <em>sommes</em>."),
        ]),
        dict(kop="De imparfait", blokken=[
            ("p", "De imparfait maak je uit de <strong>nous-vorm van de présent</strong>, zonder "
                  "<strong>-ons</strong>, plus de uitgangen <strong>-ais, -ais, -ait, -ions, -iez, "
                  "-aient</strong>. <em>nous parl<strike>ons</strike></em> geeft <em>je parlais</em>, "
                  "<em>nous fais<strike>ons</strike></em> geeft <em>il <strong>faisait</strong> beau "
                  "ce jour-là</em>."),
            ("p", "<em>Quand j'étais petit, je <strong>jouais</strong> dehors.</em> "
                  "<strong>Être</strong> is het <strong>enige</strong> werkwoord met een "
                  "onregelmatige stam in de imparfait: <em>j'étais</em>. <em>Avoir</em> "
                  "(<em>j'avais</em>), <em>aller</em> (<em>j'allais</em>) en <em>faire</em> "
                  "(<em>je faisais</em>) volgen gewoon de regel."),
        ]),
        dict(kop="Welke van de twee kies je?", blokken=[
            ("p", "De <strong>passé composé</strong> is voor <strong>afgelopen "
                  "gebeurtenissen</strong> die het verhaal <strong>vooruitduwen</strong>. De "
                  "<strong>imparfait</strong> is voor het <strong>decor</strong>, een "
                  "<strong>gewoonte</strong> of een <strong>toestand</strong> die bleef duren."),
            ("fig", tabel(["Kondigt passé composé aan", "Kondigt imparfait aan"], [
                ["hier", "souvent"],
                ["soudain, tout à coup", "tous les jours"],
                ["l'année dernière", "chaque été"],
                ["à huit heures", "d'habitude"],
            ]), "De tijdsbepalingen die je al verklappen welke tijd er komt."),
            ("p", "In één zin samen zie je het mooiste: <em>Je <strong>lisais</strong> quand le "
                  "téléphone <strong>a sonné</strong>.</em> Lezen was aan de gang, de telefoon ging "
                  "op één bepaald moment. En: <em>Il <strong>pleuvait</strong>. Soudain, une voiture "
                  "<strong>a freiné</strong>.</em> De regen is het decor, het remmen de gebeurtenis."),
            ("weetje", "Het Nederlandse <strong>'ik las'</strong> kan in het Frans allebei zijn: "
                       "<em>je lisais</em> (ik was aan het lezen, elke avond) of <em>j'ai lu</em> (ik "
                       "heb het gelezen, af). Je kan dus niet op het Nederlands voortgaan; je moet "
                       "kijken wat de zin bedoelt."),
            ("fig", tabel(["Nederlandse zin", "Welke tijd"], [
                ["Elke zomer gingen we naar zee.", "imparfait, een gewoonte"],
                ["Hij was tien jaar toen hij verhuisde.", "imparfait, een toestand"],
                ["Het regende de hele dag.", "imparfait, het decor"],
                ["Gisteren ben ik naar de tandarts geweest.", "passé composé, één gebeurtenis"],
            ]), "Vier zinnen, met de tijd die het Frans hier kiest."),
        ]),
        dict(kop="De plus-que-parfait", blokken=[
            ("p", "De plus-que-parfait is het <strong>hulpwerkwoord in de imparfait</strong> plus het "
                  "<strong>voltooid deelwoord</strong>: <em>j'<strong>avais</strong> mangé</em>, "
                  "<em>il <strong>était</strong> parti</em>. Hij drukt uit dat iets <strong>al "
                  "gebeurd was vóór een ander moment in het verleden</strong>."),
            ("p", "<em>Quand je suis arrivé, il <strong>était</strong> déjà parti.</em> Eerst was hij "
                  "weg, pas daarna kwam ik aan. En <em>nous <strong>avions</strong> fini quand ils "
                  "sont arrivés.</em>"),
            ("fig", svg.stappen([
                "il avait perdu|ses clés",
                "il m'a dit|dat hij ze kwijt was",
                "maintenant|wij lezen het",
            ]), "Drie momenten na elkaar: wat het eerst gebeurde, staat in de plus-que-parfait."),
            ("p", "<em>Il m'a dit qu'il <strong>avait perdu</strong> ses clés</em>: eerst raakte hij "
                  "de sleutels kwijt, daarna vertelde hij het. De plus-que-parfait is dus het "
                  "<strong>vroegste</strong> van de twee."),
            ("p", "De regels van de passé composé blijven gewoon gelden: met <em>être</em> komt het "
                  "deelwoord nog altijd overeen met het onderwerp (<em>Nous étions déjà "
                  "<strong>sortis</strong></em>, <em>Ils s'étaient <strong>levés</strong> très tôt</em>), "
                  "en <em>j'ai avais mangé</em> met twee hulpwerkwoorden bestaat niet."),
            ("weetje", "<em>Avait</em> en <em>était</em> zijn <strong>imparfait</strong>-vormen, geen "
                       "futur. En let op het verschil tussen een deelwoord en een persoonsvorm: "
                       "<em>allé</em>, <em>fait</em> en <em>venu</em> zijn deelwoorden, maar "
                       "<em>allez</em> is een <strong>vervoegde</strong> vorm bij <em>vous</em>."),
        ]),
        buiten("vertel in het Frans wat er gisteren gebeurde, in minstens vier zinnen, en zorg dat er "
               "één zin met de imparfait bij zit die het decor zet."),
    ],
)


# ───────────────────────── 12. Futur, conditionnel en subjonctif
BUNDELS["futur-conditionnel-en-subjonctif" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Futur, conditionnel en subjonctif",
    onder="De toekomst, de beleefde en voorwaardelijke vorm, en de wijze die je na que nodig hebt.",
    secties=[
        dict(kop="De futur simple", blokken=[
            ("p", "De futur simple vertrekt van de <strong>infinitief</strong> en plakt daar de "
                  "uitgangen <strong>-ai, -as, -a, -ons, -ez, -ont</strong> achter. <em>Demain, je "
                  "<strong>partirai</strong> à huit heures.</em> Bij een werkwoord op "
                  "<strong>-re</strong> valt de <em>e</em> weg: <em>prendre</em> geeft <em>je "
                  "prendrai</em>."),
            ("p", "Je hoort die toekomst dus aan de <strong>r</strong> vlak voor de uitgang. In de "
                  "<strong>imparfait</strong> zit die r juist <strong>niet</strong>: vergelijk "
                  "<em>je parle<strong>r</strong>ai</em> met <em>je parlais</em>."),
            ("fig", tabel(["Werkwoord", "Stam in de futur", "Voorbeeld"], [
                ["aller", "ir-", "j'irai, nous irons"],
                ["avoir", "aur-", "tu auras"],
                ["être", "ser-", "nous serons là à midi"],
                ["faire", "fer-", "je ferai"],
                ["venir", "viendr-", "il viendra"],
                ["pouvoir, voir, courir", "pourr-, verr-, courr-", "met een dubbele r"],
            ]), "De onregelmatige stammen; parler houdt gewoon parl-."),
            ("weetje", "<em>Je vais partir</em> en <em>je partirai</em> betekenen allebei dat je gaat "
                       "vertrekken, maar de <strong>futur proche</strong> ligt "
                       "<strong>dichterbij</strong> en klinkt <strong>losser</strong>. In een "
                       "schrijfopdracht staat de futur simple netter."),
            ("kader", "<strong>Na <em>quand</em> staat in het Frans de futur</strong>, waar wij een "
                      "tegenwoordige tijd zeggen. <em>Quand il <strong>arrivera</strong>, nous "
                      "<strong>mangerons</strong>.</em> Wij zeggen 'wanneer hij aankomt', het Frans "
                      "zet er twee keer een toekomst."),
        ]),
        dict(kop="De conditionnel", blokken=[
            ("p", "De conditionnel présent is een kruising: je neemt de <strong>stam van de "
                  "futur</strong> en zet er de <strong>uitgangen van de imparfait</strong> achter."),
            ("fig", svg.stappen([
                "aimer|de infinitief",
                "aimer-|de stam van de futur",
                "j'aimerais|uitgang van de imparfait",
            ]), "De drie stappen van infinitief naar conditionnel."),
            ("p", "<em>J'<strong>aimerais</strong> aller en France</em>, <em>il "
                  "<strong>pourrait</strong> venir demain</em> (hij zou kunnen komen), <em>il "
                  "<strong>faudrait</strong> partir</em> (we zouden moeten vertrekken)."),
            ("p", "Gebruik de conditionnel om iets <strong>beleefd te vragen</strong> of iets "
                  "<strong>voorwaardelijks</strong> te zeggen. Dat eerste heet de "
                  "<strong>conditionnel de politesse</strong>: <em>Je voudrais réserver une "
                  "table</em>, <em>Pourriez-vous m'aider ?</em>, <em>J'aimerais vous poser une "
                  "question</em>. <em>Je veux une table</em> is dezelfde vraag zonder die beleefdheid, "
                  "en dat hoor je."),
            ("weetje", "<em>Je parlerai</em> (futur) en <em>je parlerais</em> (conditionnel) klinken "
                       "bijna <strong>hetzelfde</strong>, en toch betekenen ze iets anders: 'ik zal "
                       "spreken' tegenover 'ik zou spreken'. Bij het lezen zie je het verschil wel: "
                       "let op die <strong>-s</strong>."),
            ("p", "Nog een gebruik dat je in kranten tegenkomt: nieuws dat <strong>nog niet bevestigd "
                  "is</strong>, zet het Frans in de <strong>conditionnel</strong>, niet in de futur. "
                  "<em>Le train <strong>aurait</strong> du retard</em> betekent dat de trein naar "
                  "verluidt vertraging heeft."),
        ]),
        dict(kop="De subjonctif: de vorm", blokken=[
            ("p", "De subjonctif présent vertrekt van de <strong>ils-vorm van de présent</strong>, "
                  "zonder <strong>-ent</strong>, met de uitgangen <strong>-e, -es, -e, -ions, -iez, "
                  "-ent</strong>."),
            ("fig", svg.stappen([
                "ils prennent|de ils-vorm",
                "prenn-|zonder -ent",
                "que je prenne|uitgang erbij",
            ]), "De drie stappen naar de subjonctif."),
            ("fig", tabel(["Werkwoord", "Subjonctif", "Voorbeeld"], [
                ["être", "que je sois", "je suis content que tu sois là"],
                ["avoir", "que j'aie", "il faut que tu aies du courage"],
                ["faire", "que je fasse", "il faut que tu fasses attention"],
                ["aller", "que j'aille", "il faut que j'aille chez le médecin"],
                ["pouvoir", "que je puisse", "bien qu'il puisse venir"],
                ["savoir", "que je sache", "pour que tu saches la vérité"],
            ]), "De zes werkwoorden met een eigen subjonctif."),
            ("p", "Bij een regelmatig werkwoord zie je vaak <strong>geen</strong> verschil met de "
                  "présent: <em>que je parle</em> is dezelfde vorm. Juist daarom moet je de "
                  "<strong>uitdrukking</strong> herkennen die de subjonctif oproept."),
        ]),
        dict(kop="Wanneer komt er een subjonctif?", blokken=[
            ("p", "De subjonctif staat bijna altijd in een <strong>bijzin die met <em>que</em> "
                  "begint</strong>. Wat in de <strong>hoofdzin</strong> staat, beslist of je hem "
                  "nodig hebt."),
            ("fig", tabel(["De hoofdzin drukt uit", "Voorbeeld", "Wijze"], [
                ["een noodzaak", "il faut que tu fasses attention", "subjonctif"],
                ["een wil of een wens", "je veux que tu viennes, je voudrais que…", "subjonctif"],
                ["een gevoel", "je suis content que tu sois là", "subjonctif"],
                ["een twijfel of ontkenning", "je ne pense pas qu'il soit malade", "subjonctif"],
                ["een feit of een zekerheid", "je sais qu'il est là, il est sûr que tu as raison", "indicatif"],
                ["een mededeling", "elle dit qu'elle viendra, il m'a dit que…", "indicatif"],
            ]), "Wat er in de hoofdzin staat, bepaalt de wijze in de bijzin."),
            ("p", "Ook een paar <strong>voegwoorden</strong> trekken altijd een subjonctif aan: "
                  "<em><strong>pour que</strong></em> (opdat), <em><strong>bien que</strong></em> "
                  "(hoewel) en <em><strong>avant que</strong></em> (voordat). <em>Bien qu'il "
                  "<strong>soit</strong> fatigué, il continue</em> betekent: hoewel hij moe is, gaat "
                  "hij door. <em>Parce que</em> hoort daar níét bij: dat geeft een feit, dus een "
                  "indicatif."),
            ("p", "<em>Je pense que</em> bevestigend geeft de <strong>indicatif</strong> (<em>je pense "
                  "qu'il est malade</em>), maar in de <strong>ontkenning</strong> komt er twijfel bij "
                  "en vaak een subjonctif. En <em>il est certain qu'il pleuve</em> is fout: een "
                  "zekerheid vraagt <em>qu'il pleut</em>."),
            ("kader", "<strong>Hetzelfde onderwerp? Dan liever een infinitief.</strong> <em>Je suis "
                      "content <strong>de te voir</strong></em> klinkt natuurlijk; <em>je suis content "
                      "que je te voie</em> niet. Zo ook <em>je veux partir</em> in plaats van <em>je "
                      "veux que je parte</em>."),
            ("weetje", "De subjonctif is voor een Nederlandstalige zo lastig omdat ons eigen "
                       "<strong>taalgevoel er geen aanwijzing voor geeft</strong>: wij hebben die "
                       "wijze niet meer. Je moet hem dus leren aan de <strong>uitdrukkingen</strong> "
                       "die hem oproepen, niet aan je gehoor."),
        ]),
        dict(kop="Wijzen en tijden uit elkaar houden", blokken=[
            ("p", "<em>L'indicatif</em>, <em>l'impératif</em>, <em>le subjonctif</em> en <em>le "
                  "conditionnel</em> zijn <strong>wijzen</strong>; <em>l'imparfait</em>, <em>le "
                  "présent</em> en <em>le futur</em> zijn <strong>tijden</strong>. Een vraag die "
                  "'welke van deze is een tijd' luidt, gaat dus over dat onderscheid."),
            ("p", "Bij het lezen herken je de vormen aan hun uitgang: <em>nous irons</em>, <em>ils "
                  "seront</em> en <em>tu auras</em> staan in de <strong>futur</strong>, maar "
                  "<em>nous allions</em> is een <strong>imparfait</strong> — geen r voor de uitgang."),
        ]),
        buiten("vraag in het Frans beleefd iets aan iemand met je voudrais of pourriez-vous, en zeg "
               "daarna in één zin wat je volgend jaar zal doen, in de futur simple."),
    ],
)


# ───────────────────────── 13. Soorten zinnen, bijzinnen en si-zinnen
BUNDELS["soorten-zinnen-bijzinnen-en-si-zinnen" + NIVEAU] = dict(
    vak=VAK, niveau=BOOST, titel="Soorten zinnen, bijzinnen en si-zinnen",
    onder="Vragen stellen, ontkennen, uitroepen, de zinsdelen op hun plaats zetten, en de twee soorten si-zinnen.",
    secties=[
        dict(kop="De soorten zinnen", blokken=[
            ("p", "De vakfiche deelt de zinnen op drie manieren in, en die drie staan los van "
                  "elkaar. Naar wat je ermee doet: <strong>mededelend, vragend, bevelend</strong> en "
                  "<strong>uitroepend</strong>. Naar de vorm: <strong>bevestigend</strong> of "
                  "<strong>ontkennend</strong>. En naar de bouw: <strong>enkelvoudig</strong> of "
                  "<strong>samengesteld</strong>."),
            ("p", "Een <strong>samengestelde</strong> zin heeft <strong>meer dan één "
                  "persoonsvorm</strong>. Dat heeft niets met de lengte te maken: een zin van vier "
                  "woorden kan samengesteld zijn en een zin van twintig woorden enkelvoudig."),
        ]),
        dict(kop="Drie manieren om een vraag te stellen", blokken=[
            ("fig", tabel(["Manier", "Voorbeeld", "Wanneer"], [
                ["met de toon", "Tu viens ?", "spreektaal, de gewoonste vorm"],
                ["met est-ce que", "Est-ce que tu viens ?", "overal bruikbaar, ook geschreven"],
                ["met omkering", "Viens-tu ? / Partez-vous ?", "verzorgd, in een brief of een examen"],
            ]), "De drie vraagvormen van het Frans."),
            ("p", "Je mag ze niet mengen: <em>Est-ce que viens-tu ?</em> is fout, want dat zijn er "
                  "twee tegelijk. En bij de <strong>omkering</strong> komt er soms een extra "
                  "<strong>-t-</strong> tussen, als het werkwoord op een klinker eindigt: <em>A-<strong>t</strong>-il "
                  "le temps ?</em>, <em>Parle-<strong>t</strong>-elle français ?</em>"),
            ("fig", tabel(["Vraagwoord", "Vraagt naar"], [
                ["pourquoi", "een reden"],
                ["comment, de quelle façon", "een manier"],
                ["combien", "een aantal"],
                ["où, quand", "een plaats, een tijdstip"],
                ["qui, que, quoi", "een persoon, een zaak"],
            ]), "De vraagwoorden en wat ze opvragen."),
        ]),
        dict(kop="Ontkennen", blokken=[
            ("p", "De Franse ontkenning bestaat uit <strong>twee delen</strong> die rond het "
                  "<strong>vervoegde werkwoord</strong> staan: <em>Il <strong>ne</strong> parle "
                  "<strong>pas</strong>.</em> In een <strong>samengestelde tijd</strong> staan ze "
                  "rond het <strong>hulpwerkwoord</strong>: <em>Je n'ai pas mangé.</em>"),
            ("fig", tabel(["Ontkenning", "Nederlands", "Voorbeeld"], [
                ["ne … pas", "niet", "je ne mange pas"],
                ["ne … plus", "niet meer", "je ne mange plus de viande, ik eet geen vlees meer"],
                ["ne … jamais", "nooit", "il ne vient jamais"],
                ["ne … rien", "niets", "je ne vois rien"],
                ["ne … personne", "niemand", "je ne vois personne"],
                ["ne … que", "maar, slechts", "je n'ai que dix euros"],
            ]), "De ontkenningen; ne … toujours bestaat niet als ontkenning."),
            ("weetje", "Het tweede deel vervángt <em>pas</em>, het komt er niet bij. <em>Je ne vois "
                       "<strong>personne</strong></em> is juist; <em>je ne vois pas personne</em> is "
                       "fout, want dan staan er twee ontkenningen in dezelfde zin."),
        ]),
        dict(kop="Uitroepen", blokken=[
            ("fig", tabel(["Uitroepwoord", "Komt voor", "Voorbeeld"], [
                ["quel, quelle, quels, quelles", "een naamwoord", "Quelle belle maison !"],
                ["comme", "een hele zin", "Comme c'est beau !"],
                ["que", "een hele zin", "Que c'est gentil !"],
            ]), "De drie manieren om een uitroep te maken."),
            ("p", "Let bij een uitroep op de vorm van <em>quel</em>: die past zich aan het naamwoord "
                  "aan. <em><strong>Quelle</strong> belle maison !</em> met <em>maison</em> "
                  "vrouwelijk."),
            ("weetje", "In het Frans staat er een <strong>spatie vóór</strong> een uitroepteken en "
                       "een vraagteken: <em>Viens-tu ?</em> en <em>Quelle journée !</em> In het "
                       "Nederlands doen we dat niet, en op een examen valt het op."),
        ]),
        dict(kop="De zinsdelen en de woordvolgorde", blokken=[
            ("p", "De vakfiche noemt drie zinsdelen met name: het <strong>onderwerp</strong> "
                  "(<em>sujet</em>), de <strong>persoonsvorm</strong> (<em>verbe conjugué</em>) en "
                  "het <strong>lijdend voorwerp</strong> (<em>COD</em>). Een <strong>bijwoordelijke "
                  "bepaling</strong> van plaats hoort daar niet bij: die bestaat wel, maar de "
                  "fiche vraagt ze niet met name. De gewone woordvolgorde is "
                  "<strong>onderwerp, werkwoord, voorwerp</strong>."),
            ("fig", svg.zinsdelen([
                ("Les enfants", "sujet", svg.FOREST),
                ("jouent", "verbe conjugué", svg.AMBER),
                ("au ballon", "complément", svg.DARK),
            ]), "Dezelfde volgorde als in het Nederlands: eerst wie, dan wat hij doet."),
            ("p", "Het werkwoord komt <strong>overeen</strong> met het onderwerp: <em>Les enfants "
                  "<strong>jouent</strong> dans le jardin</em>, met een meervoud aan allebei de "
                  "kanten. <em>Les enfants joue</em> of <em>l'enfant jouent</em> loopt dus mis."),
            ("p", "Eén geval breekt de volgorde: een <strong>voornaamwoord</strong> als voorwerp komt "
                  "<strong>vóór</strong> het werkwoord. <em>Je vois le film</em> wordt <em>je "
                  "<strong>le</strong> vois</em>. Dat is geen uitzondering van dat ene werkwoord maar "
                  "een vaste regel."),
        ]),
        dict(kop="Nevenschikking en onderschikking", blokken=[
            ("p", "Een <strong>nevengeschikte</strong> zin kan <strong>alleen</strong> staan; een "
                  "<strong>ondergeschikte</strong> (onderschikkende) niet. <em>Il pleut, <strong>donc</strong> je "
                  "prends mon parapluie</em> bestaat uit twee zinnen die elk op zichzelf kunnen "
                  "staan: dat is <strong>nevenschikking</strong>, ook al legt <em>donc</em> een "
                  "verband."),
            ("fig", tabel(["Soort", "Voegwoorden"], [
                ["nevenschikkend", "et, mais, ou, donc, car"],
                ["reden", "parce que, comme"],
                ["tijd", "quand, dès que, pendant que"],
                ["doel", "pour que (+ subjonctif)"],
                ["toegeving", "bien que (+ subjonctif)"],
            ]), "De voegwoorden, naar wat ze doen."),
            ("p", "<em>Je reste <strong>parce qu'</strong>il pleut</em>: <em>parce que</em> betekent "
                  "omdat, en de bijzin kan niet alleen staan. <em>Comme</em> vooraan doet hetzelfde: "
                  "<em>Comme il pleut, je reste à la maison.</em>"),
            ("kader", "<strong>Pour of pour que?</strong> <em>Pour</em> gaat met een "
                      "<strong>infinitief</strong>: <em>je travaille <strong>pour</strong> gagner ma "
                      "vie</em>, om mijn brood te verdienen. <em>Pour que</em> gaat met een <strong>subjonctif</strong>, en "
                      "gebruik je als de twee delen een <strong>ander</strong> onderwerp hebben: "
                      "<em>je travaille pour que mes enfants puissent étudier</em>."),
        ]),
        dict(kop="Betrekkelijke bijzinnen", blokken=[
            ("fig", tabel(["Juist", "Waarom"], [
                ["la fille qui chante", "qui is het onderwerp van chante"],
                ["le film que j'ai vu", "que is het lijdend voorwerp van ai vu"],
                ["la ville où je suis né", "où voor een plaats"],
                ["voilà la maison où j'ai grandi", "où, want je grandis érgens"],
            ]), "Vier bijzinnen met het juiste voornaamwoord."),
            ("p", "<em>Le livre <strong>qui</strong> je lis</em> is fout: in die bijzin is "
                  "<em>je</em> het onderwerp, dus moet het <em><strong>que</strong> je lis</em> zijn. "
                  "Vraag je bij elke bijzin af welke rol het voornaamwoord speelt."),
        ]),
        dict(kop="De si-zinnen", blokken=[
            ("p", "Twee vaste patronen, en je moet ze allebei kennen. Welke je kiest, hangt af van "
                  "hoe <strong>echt</strong> de mogelijkheid is."),
            ("fig", tabel(["Soort", "Patroon", "Voorbeeld"], [
                ["een echte mogelijkheid", "si + présent → futur",
                 "Si tu veux, nous partirons."],
                ["een echte mogelijkheid", "si + présent → présent",
                 "S'il pleut, je reste à la maison."],
                ["iets onwerkelijks", "si + imparfait → conditionnel",
                 "Si j'avais de l'argent, j'achèterais une voiture."],
            ]), "De twee patronen van de si-zin."),
            ("p", "De regel die alles vasthoudt: <strong>na <em>si</em> staat nooit een futur en "
                  "nooit een conditionnel</strong>. <em>Si tu voudrais, nous partirions</em> is dus "
                  "fout; dat moet <em>Si tu <strong>voulais</strong>, nous partirions</em> zijn."),
        ]),
        dict(kop="Voorzetsels bij plaats en vervoer", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["en voiture, en train, en avion", "met de auto, de trein, het vliegtuig"],
                ["à pied, à vélo", "te voet, met de fiets"],
                ["au Portugal, en Belgique, aux Pays-Bas", "naar of in een land"],
                ["à Bruxelles, à Paris", "in een stad — altijd à, nooit en"],
                ["grâce à, à cause de", "dankzij, door toedoen van"],
                ["en face de, à côté de", "tegenover, naast"],
            ]), "Voorzetselgroepen die de fiche zelf als voorbeeld noemt."),
            ("p", "<em>Ils voyagent <strong>au</strong> Portugal cette année</em>, want "
                  "<em>Portugal</em> is mannelijk. Bij <strong>steden</strong> staat altijd "
                  "<em>à</em>: <em>j'habite <strong>à</strong> Bruxelles</em>, nooit <em>en "
                  "Bruxelles</em>."),
        ]),
        dict(kop="Bij het lezen: tel de persoonsvormen", blokken=[
            ("kader", "<strong>Loopt een Franse zin over drie regels?</strong> Tel dan de "
                      "<strong>persoonsvormen</strong>. Zo zie je meteen <strong>hoeveel delen</strong> "
                      "de zin heeft en <strong>waar elk deel begint</strong>. Zoek daarna bij elke "
                      "persoonsvorm haar eigen onderwerp, en de zin valt uiteen in stukken die je elk "
                      "apart begrijpt."),
        ]),
        buiten("stel in het Frans drie vragen aan iemand over zijn dag, elke keer op een andere "
               "manier: één met de toon, één met est-ce que en één met omkering."),
    ],
)
