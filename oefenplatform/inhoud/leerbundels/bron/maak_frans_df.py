# -*- coding: utf-8 -*-
"""De leerbundels voor Frans op 🚀 Boost dubbele finaliteit.

Gebaseerd op de vakfiche Frans van de 2de graad dubbele finaliteit, geldig van
1 januari 2027 tot en met 31 december 2027, voor bedrijf en organisatie en voor
maatschappij en welzijn. Het ERK-niveau is A2.

Let op: dit vak oefent **alleen het schriftelijke Frans**. Het examen bestaat
ook uit luisteren, spreken en een gesprek, en dat kan een oefenplatform met
tekstvragen niet nabootsen. Dat staat ook met zoveel woorden in de eerste
bundel, zodat niemand denkt dat dit het hele examen dekt.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. De bundel hoort dus bij
allebei de hoofdstukken; de titel van de bundel is de naam van het thema, en de
app laat "— deel 1" en "— deel 2" vallen voor ze zoekt.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-dubbele-finaliteit/frans.json`
doet daar het voorwerk voor; daarna gaat elke vraag nog één voor één naast de
tekst.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Frans"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
NIVEAU = "-boost-dubbele-finaliteit"
tabel = bundel.tabel

SCHRIFTELIJK = (
    "<strong>Dit oefenplatform oefent alleen het schriftelijke Frans.</strong> Je examen "
    "bestaat uit drie delen: een <strong>spreekopdracht</strong> die je thuis opneemt en "
    "indient tot drie dagen voor je digitale examen, het <strong>digitale examen</strong> van "
    "150 minuten in het examencentrum in Brussel, en een <strong>gesprek</strong> van tien "
    "minuten met vijftien minuten voorbereidingstijd voor twee opdrachten. De punten liggen "
    "zo: lezen 30 %, luisteren 30 %, schrijven 8 %, schriftelijke interactie 8 %, spreken "
    "8 %, en twee keer mondelinge interactie, elk 8 %. Luisteren, spreken en de gesprekken "
    "oefen je hier niet: daar heb je geluid en een gesprekspartner voor nodig. Wat je hier "
    "wél oefent — lezen, schrijven, woordenschat en grammatica — draagt de helft van je "
    "punten, en je hebt het ook nodig om te kunnen luisteren en spreken."
)
GEEN_GIS = (
    "<strong>Er is geen giscorrectie.</strong> Een fout antwoord kost je niets extra, dus "
    "vul altijd iets in, ook als je twijfelt."
)

BUNDELS = {}

# ---------------------------------------------------------------------------

BUNDELS["een-franse-tekst-begrijpen" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Een Franse tekst begrijpen",
    onder="Het onderwerp, de hoofdgedachte, de hoofdpunten en de gegevens die je nodig hebt.",
    secties=[
        dict(kop="Waarvoor dient dit vak hier?", blokken=[
            ("kader", SCHRIFTELIJK),
            ("p", "Lezen is met 30 % het zwaarste onderdeel dat je hier kan inoefenen, "
                  "evenveel als luisteren. En wie vlot leest, herkent dezelfde woorden ook "
                  "terug als hij ze hoort."),
            ("p", "Het ERK-niveau van dit jaar is <strong>A2</strong>. Dat betekent korte, "
                  "duidelijke teksten over het dagelijkse leven: een zoekertje, een bericht "
                  "van de school, een recept, een verslagje van een weekend, een affiche, een "
                  "beoordeling van een hotel. Reken er wel op dat er ook een tekst bij zit die "
                  "iets uitdagender is."),
        ]),
        dict(kop="Vier vragen bij elke tekst", blokken=[
            ("p", "Het <strong>onderwerp</strong> is waarover een tekst gaat. Je zegt het in "
                  "één of enkele <strong>woorden</strong>: 'iemand verkoopt zijn fiets', "
                  "'tweedehands kopen'. Niet in een volledige zin dus."),
            ("p", "De <strong>hoofdgedachte</strong> is de belangrijkste boodschap, in één "
                  "<strong>zin</strong>: 'Deze fiets is weinig gebruikt en kost 95 euro.' De "
                  "<strong>hoofdpunten</strong> zijn de inhoudelijke elementen die die "
                  "hoofdgedachte <strong>ondersteunen</strong>: de fiets is blauw, de "
                  "buitenbanden zijn nieuw, je moet hem zelf komen halen."),
            ("fig", svg.kernpiramide(),
             "Onderwerp in enkele woorden, hoofdgedachte in één zin, daaronder de punten die haar dragen."),
            ("p", "De vierde vraag is de praktische: <strong>informatie selecteren</strong>. "
                  "Dan hoef je de tekst niet helemaal te begrijpen, je moet er één gegeven uit "
                  "halen — een uur, een prijs, een dag, een aantal."),
            ("kader", "<strong>Doe het eens op een echte tekst.</strong> <em>À vendre : vélo de "
                      "ville bleu, taille moyenne. Je l'ai acheté il y a deux ans et je roule "
                      "très peu. Les pneus sont neufs. Prix : 95 euros. Je ne fais pas d'envoi : "
                      "il faut venir le chercher à Liège.</em><br>"
                      "<strong>Onderwerp:</strong> iemand verkoopt zijn fiets. "
                      "<strong>Hoofdgedachte:</strong> die fiets is weinig gebruikt en kost 95 "
                      "euro. <strong>Hoofdpunten:</strong> blauw, nieuwe buitenbanden, zelf "
                      "komen halen. <strong>Te selecteren:</strong> 95 euro."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["à vendre", "te koop"],
                ["un vélo, les pneus", "een fiets, de buitenbanden"],
                ["je roule très peu", "ik rijd er heel weinig mee"],
                ["le prix", "de prijs"],
                ["je ne fais pas d'envoi", "ik verstuur niet"],
                ["venir chercher", "komen halen"],
            ]), "Die woorden komen terug in elk zoekertje."),
        ]),
        dict(kop="Teksten uit het dagelijkse leven", blokken=[
            ("p", "Een <strong>bericht van de school</strong> zegt vooral wat er verandert: "
                  "<em>le lundi 12 octobre, les cours commencent à 10 h</em>, want <em>les "
                  "professeurs ont une réunion le matin</em>. De rest legt uit hoe het dan wél "
                  "loopt: <em>la garderie est ouverte à partir de 8 h</em> en <em>le repas de "
                  "midi se passe comme d'habitude</em>."),
            ("p", "Een <strong>recept</strong> zegt je in welke orde je iets doet: "
                  "<em>coupez deux oignons</em>, <em>ajoutez le riz</em>, <em>laissez cuire "
                  "vingt minutes sans couvercle</em>, <em>salez à la fin, pas avant</em>. "
                  "<em>Pour quatre personnes</em> staat bovenaan."),
            ("p", "Een <strong>verslagje</strong> vertelt wat er gebeurde: <em>samedi, je suis "
                  "allée à la mer</em>, <em>nous avons pris le train de 7 h 40 pour éviter le "
                  "monde</em>, <em>il faisait froid, mais le ciel était bleu</em>, <em>j'avais "
                  "mal aux jambes, mais j'étais contente</em>."),
            ("p", "Een <strong>affiche</strong> wil je overhalen: <em>viens essayer "
                  "l'escalade</em>, <em>inscris-toi avant le 30 septembre</em>, <em>le groupe "
                  "est limité à douze jeunes</em>. En een <strong>beoordeling</strong> geeft een "
                  "mening met een maar: <em>la chambre était propre</em>, <em>par contre, la "
                  "fenêtre donne sur la rue et j'ai mal dormi</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["une réunion, la garderie", "een vergadering, de opvang"],
                ["comme d'habitude", "zoals gewoonlijk"],
                ["un oignon, un couvercle", "een ui, een deksel"],
                ["éviter le monde", "de drukte vermijden"],
                ["avoir mal aux jambes", "pijn in de benen hebben"],
                ["par contre", "daarentegen"],
            ]), "Zes uitdrukkingen die je in zulke teksten voortdurend terugziet."),
        ]),
        dict(kop="Informatie opzoeken: uren, prijzen en berichten", blokken=[
            ("p", "Bij <strong>openingsuren</strong> zoek je alleen de regel die je nodig "
                  "hebt. <em>Lundi : fermé</em> betekent maandag gesloten; <em>mercredi : 14 h "
                  "– 19 h</em> is dus de namiddag; <em>samedi : 9 h – 13 h</em> betekent dat je "
                  "er in de namiddag niet meer binnen kan. <em>Fermée les jours fériés</em>: "
                  "gesloten op feestdagen."),
            ("p", "Bij een <strong>prijslijst</strong> let je op de voorwaarden. <em>Jeunes de "
                  "moins de 18 ans : 2,50 €</em> geldt voor wie jonger is dan achttien. "
                  "<em>Location d'une serviette : 2 €</em> is de huur van een handdoek, en "
                  "<em>le bonnet de bain est obligatoire et n'est pas en location</em> betekent "
                  "dat je je badmuts zelf moet meebrengen. Soms moet je even rekenen: twee "
                  "volwassenen plus één handdoek is 4,50 + 4,50 + 2 = 11 euro."),
            ("p", "In een <strong>gesprekje</strong> tussen twee mensen moet je volgen wie wat "
                  "zegt. <em>Je finis à 17 h, donc j'arrive vers 18 h 30</em>: <em>vers</em> "
                  "betekent rond. <em>Pas de souci</em> is geen probleem, <em>on mange à "
                  "19 h</em> zegt het uur, en <em>des fruits, il y a déjà un gâteau</em> zegt "
                  "waarom het fruit moet zijn."),
            ("p", "Een <strong>waslabel</strong> of een gebruiksaanwijzing zegt wat je moet en "
                  "niet mag doen: <em>lavez le vêtement seul, à 30 degrés</em>, <em>n'utilisez "
                  "pas de sèche-linge</em>, <em>repassez à l'envers</em>, <em>en cas de tache, "
                  "lavez tout de suite à l'eau froide</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["fermé, ouvert", "gesloten, open"],
                ["moins de 18 ans", "jonger dan achttien"],
                ["en location", "te huur"],
                ["vers 18 h 30", "rond half zeven"],
                ["pas de souci", "geen probleem"],
                ["une tache, tout de suite", "een vlek, onmiddellijk"],
            ]), "Woorden waarmee je een uurtabel, een prijslijst of een label kan lezen."),
        ]),
        dict(kop="Een artikel en een mail", blokken=[
            ("p", "Een <strong>krantenstukje</strong> heeft vaak een maatregel en een gevolg: "
                  "<em>les élèves laissent leur téléphone dans un casier pendant les cours</em>, "
                  "<em>les professeurs trouvent les classes plus calmes</em>, <em>certains "
                  "élèves se plaignent, mais la plupart disent qu'ils se concentrent mieux</em>, "
                  "<em>l'école va garder la règle jusqu'en juin</em>. Let op het verschil tussen "
                  "<em>certains</em> (sommige) en <em>la plupart</em> (de meeste): 'iedereen is "
                  "tevreden' staat er dus niet."),
            ("p", "Een <strong>mail om te solliciteren</strong> zegt waarom je schrijft en "
                  "wanneer je kan. <em>Je vous écris au sujet de votre annonce pour un job "
                  "d'été</em>: <em>au sujet de</em> betekent in verband met. <em>Je suis libre "
                  "du 1er au 31 juillet, sauf le week-end du 14</em>: <em>sauf</em> betekent "
                  "behalve."),
            ("weetje", "Je mag op het examen een <strong>online woordenboek</strong> gebruiken, "
                       "maar je hebt niet de tijd om elk woord op te zoeken. Zorg dus voor een "
                       "basiswoordenschat, en zoek alleen op wat je echt nodig hebt."),
            ("kader", GEEN_GIS),
        ]),
    ],
    onthoud=[
        "Onderwerp = enkele woorden. Hoofdgedachte = één zin. Hoofdpunten = wat haar draagt.",
        "Informatie selecteren: zoek alleen de regel die je nodig hebt.",
        "fermé = gesloten, ouvert = open; vers = rond; sauf = behalve.",
        "par contre zet twee dingen tegenover elkaar; déjà betekent al.",
        "certains = sommige, la plupart = de meeste. Dat is niet iedereen.",
        "Lezen telt voor 30 % van het examen, evenveel als luisteren.",
        "Er is geen giscorrectie, dus vul altijd iets in.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["tekstsoorten-tekstverbanden-en-leesstrategieen" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Tekstsoorten, tekstverbanden en leesstrategieën",
    onder="Zes soorten teksten, de woorden die ze aan elkaar houden, en wat je doet met een woord dat je niet kent.",
    secties=[
        dict(kop="Zes soorten teksten", blokken=[
            ("p", "Op het examen weet je nooit vooraf welke soort tekst je krijgt. Als je ziet "
                  "dat een tekst je wil <em>overtuigen</em>, lees je anders dan wanneer hij je "
                  "iets <em>uitlegt</em>. Daarom staan deze zes op een rij."),
            ("fig", tabel(["soort", "wat hij doet", "voorbeelden"], [
                ["informatief", "geeft je informatie over een onderwerp",
                 "krantenartikel, stukje uit een leerboek, interview, mail naar een klant"],
                ["persuasief", "wil je overtuigen of beïnvloeden",
                 "reclamefilmpje, campagne tegen te snel rijden, flyer van een fitnesszaal"],
                ["opiniërend", "iemand geeft zijn mening",
                 "recensie van een boek, hotelbeoordeling, reactie op sociale media"],
                ["prescriptief", "legt uit wat of hoe je iets moet doen",
                 "recept, instructiefilmpje, schoolreglement, veiligheidsvoorschriften"],
                ["narratief", "geeft gebeurtenissen verhalend weer",
                 "videoblog, reisverslag, podcast, getuigenis over een eerste werkdag"],
                ["literair", "heeft een esthetische waarde, speelt in op emoties",
                 "lied, gedicht, cartoon, strip, kortverhaal"],
            ]), "Een tekst kan er een beetje van twee zijn; je kijkt naar wat hij vooral wil."),
            ("kader", "<strong>Herken ze aan één zin.</strong> <em>Faites chauffer un litre de "
                      "bouillon</em> is prescriptief: het zegt je wat te doen. <em>Ramasse ce "
                      "que tu apportes</em> is persuasief: het wil je gedrag veranderen. <em>À "
                      "mon avis, deux heures c'est beaucoup trop long</em> is opiniërend. <em>À "
                      "partir du 15 décembre, le train partira cinq minutes plus tôt</em> is "
                      "informatief. <em>Ce matin-là, ma grand-mère a mis son chapeau rouge</em> "
                      "is narratief. <em>Apporte-moi le soleil</em> vraagt geen echte zon: dat "
                      "is literair."),
            ("p", "De vorm verklapt vaak al de soort. Een tekst die begint met <em>Chère Madame "
                  "Dupont,</em> is een brief of een mail aan één bepaalde persoon. Een titel als "
                  "<em>Trois bonnes raisons de prendre le vélo</em> belooft redenen, en dus een "
                  "tekst die je wil overhalen."),
        ]),
        dict(kop="Het communicatiemodel en de andere strategieën", blokken=[
            ("fig", svg.communicatiemodel(),
             "Van wie is de tekst, waarom is hij gemaakt, en voor wie?"),
            ("p", "Die drie vragen samen vormen het <strong>communicatiemodel</strong>. Stel "
                  "jezelf daarnaast vooraf: wat weet ik al over dit onderwerp, en waarover zou "
                  "de tekst kunnen gaan? Je <strong>voorkennis</strong> helpt je sneller "
                  "begrijpen wat er staat."),
            ("fig", svg.stappen([
                "Titel en beeld|Waarover gaat dit?",
                "Lezen in het geheel|Hoofdzaak of bijzaak?",
                "Pas dan opzoeken|Alleen wat je nodig hebt",
            ]), "Drie stappen, in die orde. Woord voor woord vertalen doe je nooit als eerste."),
            ("p", "Gebruik de <strong>visuele hulpmiddelen</strong> die een tekst biedt: de "
                  "titel en de tussentitels, benadrukte woorden, een foto, een tekening of een "
                  "grafiek bij een leestekst, of de beelden bij een videofragment."),
            ("p", "Maak <strong>onderscheid tussen hoofd- en bijzaken</strong>: je ziet welke "
                  "zinnen de boodschap dragen en welke alleen een voorbeeld of een detail "
                  "geven. En als je halfweg niets meer snapt, lees dan eerst verder tot het "
                  "einde: een tekst legt zichzelf vaak verder uit."),
            ("kader", "Je mag een <strong>online woordenboek</strong> gebruiken, maar niet voor "
                      "elk woord. Beslis eerst of de betekenis van dat woord écht nodig is om "
                      "de tekst te begrijpen. Alleen dan zoek je het op."),
        ]),
        dict(kop="Signaalwoorden: de gedachtegang van de tekst", blokken=[
            ("p", "<strong>Structuuraanduiders</strong> zijn de woorden waarmee een tekst zijn "
                  "gedachtegang vasthoudt. Ze zeggen je hoe de stukken zich tot elkaar "
                  "verhouden."),
            ("fig", tabel(["wat het woord doet", "Frans"], [
                ["orde van de stappen", "d'abord, ensuite, puis, enfin"],
                ["tegenstelling", "mais, par contre, cependant, pourtant"],
                ["reden", "parce que, car, comme"],
                ["gevolg", "donc, alors"],
                ["toevoeging", "et, aussi, en plus"],
                ["voorwaarde", "si"],
            ]), "Zes groepen. Hun plaats in de zin zegt niets, hun betekenis alles."),
            ("kader", "<strong>In een echte tekst.</strong> <em>Le marché est moins cher que le "
                      "supermarché, <strong>par contre</strong> il n'ouvre que le mercredi. "
                      "<strong>Comme</strong> je travaille ce jour-là, j'y vais rarement. "
                      "<strong>Donc</strong> j'achète mes légumes au magasin du coin.</em><br>"
                      "<em>Par contre</em> zet de twee kanten tegenover elkaar, <em>comme</em> "
                      "geeft de reden (omdat ik die dag werk), <em>donc</em> het gevolg."),
            ("p", "Let op twee die je snel verwart: <em>cependant</em> betekent nochtans of toch "
                  "en zet een tegenstelling, <em>car</em> betekent want en geeft een reden. "
                  "<em>Attention</em> is geen signaalwoord maar een waarschuwing, en "
                  "<em>beaucoup</em> betekent gewoon veel."),
        ]),
        dict(kop="Verwijswoorden: waarnaar wijst dit woord?", blokken=[
            ("p", "Een <strong>verwijswoord</strong> vervangt een persoon, een voorwerp, een "
                  "begrip of een plaats uit een <strong>vorige</strong> zin. Als je niet weet "
                  "waarnaar het verwijst, verlies je de draad. Een verwijswoord wijst dus altijd "
                  "terug, nooit vooruit."),
            ("kader", "<strong>Vier verwijzingen in drie zinnen.</strong> <em>Nos voisins ont un "
                      "grand jardin. <strong>Ils y</strong> cultivent des tomates et des "
                      "haricots. L'été dernier, ils nous <strong>en</strong> ont donné un plein "
                      "panier. Nous <strong>les</strong> avons remerciés avec une tarte.</em><br>"
                      "<em>Ils</em> = de buren. <em>Y</em> = in de tuin. <em>En</em> = van de "
                      "tomaten en de bonen. <em>Les</em> = de buren; daarom staat er een s aan "
                      "<em>remerciés</em>. Je bedankt mensen, geen bonen."),
            ("fig", tabel(["verwijswoord", "vervangt"], [
                ["il, elle, ils, elles", "het onderwerp van de vorige zin"],
                ["le, la, l', les", "een lijdend voorwerp"],
                ["lui, leur", "een meewerkend voorwerp: aan hem, aan hen"],
                ["y", "een plaats: à, dans, chez …"],
                ["en", "een onbepaalde hoeveelheid: du, de la, des of een getal"],
            ]), "Vijf soorten. Een schrijver gebruikt ze om niet te moeten herhalen."),
        ]),
        dict(kop="Een onbekend woord: raden in plaats van opzoeken", blokken=[
            ("p", "Drie bronnen gebruik je om te raden. De <strong>context</strong>: <em>il a "
                  "oublié son parapluie, donc il est rentré tout <strong>mouillé</strong></em> — "
                  "nat dus. Je <strong>kennis van andere talen</strong>: <em>dangereux</em> lijkt "
                  "op het Engelse <em>dangerous</em>. En de <strong>bouw van het woord</strong>: "
                  "<em>im-praticable</em> is niet begaanbaar, want <em>im-</em> maakt negatief."),
            ("p", "Beslis daarna of dat woord echt belangrijk is. Soms kan je er gewoon over en "
                  "blijft de tekst duidelijk."),
            ("weetje", "Niet elk woord dat op Nederlands of Engels lijkt, betekent hetzelfde, "
                       "maar in de meeste gevallen helpt die gok je wel vooruit. Probeer het dus "
                       "eerst, en zoek daarna pas op."),
        ]),
    ],
    onthoud=[
        "Zes soorten: informatief, persuasief, opiniërend, prescriptief, narratief, literair.",
        "Communicatiemodel: van wie, waarom, voor wie?",
        "d'abord – ensuite – enfin = orde. par contre, cependant = tegenstelling.",
        "parce que, car, comme = reden. donc, alors = gevolg.",
        "y = een plaats, en = een hoeveelheid, les = een lijdend voorwerp in het meervoud.",
        "Een verwijswoord wijst terug, nooit vooruit.",
        "Raad uit de context, uit een andere taal of uit de bouw van het woord.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["de-franstalige-wereld-omgangsvormen-en-gewoontes" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="De Franstalige wereld: omgangsvormen en gewoontes",
    onder="Begroeten, aanspreken, tu of vous, en wat een tekst je over gewoontes vertelt.",
    secties=[
        dict(kop="Waarom cultuur bij een taalexamen hoort", blokken=[
            ("p", "Je leert een taal omdat je ze wil gebruiken, en een taal gebruik je met "
                  "mensen. Daarom krijg je op het examen teksten waarin "
                  "<strong>socioculturele aspecten</strong> belicht worden, en moet je eruit "
                  "kunnen halen wat ze zeggen over het leven van Franstaligen."),
            ("fig", tabel(["aspect", "voorbeeld uit een tekst"], [
                ["het dagelijkse leven", "hoe laat men eet, wanneer de winkels sluiten"],
                ["leefomstandigheden", "wonen, werken, school"],
                ["gewoontes", "de kaas komt vóór het dessert"],
                ["sociale verhoudingen", "wanneer je tu zegt en wanneer vous"],
                ["waarden en normen", "wat men hoffelijk vindt"],
                ["lichaamstaal", "la bise, een hand geven"],
                ["sociale conventies", "eerst bonjour, dan je vraag"],
            ]), "Zeven dingen. Je moet ze niet opsommen, je moet ze in een tekst herkennen."),
            ("weetje", "De opdracht vraagt niet dat je het land kent. Een tekst over het leven "
                       "van een jongere in Senegal vraagt alleen dat je eruit haalt wat díe "
                       "tekst over het dagelijkse leven daar zegt."),
        ]),
        dict(kop="Begroeten en aanspreken", blokken=[
            ("kader", "<strong>Eerst bonjour.</strong> <em>Quand tu entres dans une boulangerie "
                      "en France, tu dis « Bonjour » avant de demander ton pain. Si tu commences "
                      "par « Je voudrais une baguette », la vendeuse te répondra peut-être "
                      "« Bonjour » d'abord. Ce n'est pas de la mauvaise humeur : c'est l'ordre "
                      "normal.</em><br>De begroeting komt dus vóór de vraag. Ook bij een "
                      "politieagent of een verkoper."),
            ("fig", tabel(["situatie", "wat je zegt"], [
                ["een onbekende, met vous", "Bonjour, madame. / Bonjour, monsieur."],
                ["een vriend", "Salut ! / Coucou, ça va ?"],
                ["'s avonds, formeel", "Bonsoir, madame."],
                ["afscheid tot morgen", "À demain !"],
                ["afscheid, informeel", "À plus ! / Bisous !"],
                ["een eerste kennismaking", "Enchanté !"],
            ]), "Salut en coucou zijn voor vrienden; madame en monsieur maken het formeel."),
            ("p", "In een <strong>mail</strong> aan een vrouw van wie je de naam niet kent, "
                  "schrijf je <em>Madame,</em> — ken je de naam wel, dan <em>Madame "
                  "Dupont,</em>. Afsluiten doe je met <em>Cordialement,</em> of <em>Je vous "
                  "remercie d'avance.</em> <em>Bisous</em> en <em>À plus</em> horen daar niet."),
            ("p", "In <strong>Franstalig België</strong> begroeten mensen elkaar met een kus op "
                  "de wang, <em>la bise</em>, en dat doen ook mannen onder elkaar. Wie dat niet "
                  "gewoon is, kijkt daar even van op."),
        ]),
        dict(kop="Tu of vous", blokken=[
            ("fig", svg.registerschaal(zinnen=("Salut, tu viens ?", "Tu viens aussi ?",
                                               "Pourriez-vous venir ?")),
             "Dezelfde vraag, drie registers. Je kiest naar wie je spreekt."),
            ("p", "<em>Tu</em> gebruik je tegen een vriend of een klasgenoot. <em>Vous</em> is "
                  "zowel het meervoud als de <strong>hoffelijke vorm voor één persoon</strong>: "
                  "een volwassene die je niet kent, een klant, een leraar."),
            ("kader", "<strong>Het hangt niet van de leeftijd af.</strong> <em>Au travail, "
                      "j'appelle mes collègues par leur prénom et on se dit tu. Mais quand un "
                      "client entre, je passe au vous, même s'il a mon âge. Et je recommence à "
                      "dire vous à un collègue que je ne connais pas encore.</em><br>"
                      "<em>Même s'il a mon âge</em>: zelfs als hij mijn leeftijd heeft. Wat "
                      "telt, is de <strong>verhouding</strong>, niet het aantal jaren."),
            ("p", "Kies ook het bijhorende woordje: <em>s'il vous plaît</em> bij vous, <em>s'il "
                  "te plaît</em> bij tu. En in een mail aan een onbekende hoort de "
                  "<strong>conditionnel de politesse</strong>: <em>Pourriez-vous me dire quand "
                  "je peux venir ?</em> klinkt heel anders dan <em>Je viens demain, d'accord ?</em>"),
        ]),
        dict(kop="Alledaagse sociale contacten", blokken=[
            ("fig", tabel(["wat je doet", "Frans"], [
                ["bedanken", "Merci. / Merci beaucoup. / Je te remercie."],
                ["je verontschuldigen", "Pardon. / Excusez-moi. / Je suis désolé."],
                ["reageren op een verontschuldiging", "Ce n'est pas grave."],
                ["uitnodigen", "Tu viens manger chez moi samedi ?"],
                ["aan tafel", "Bon appétit !"],
                ["iemand goede reis wensen", "Bonne route !"],
            ]), "Zes dingen die je in elk gesprek nodig hebt."),
            ("p", "Een <strong>uitnodiging</strong> is een vraag aan de ander: <em>Tu viens "
                  "manger chez moi samedi ?</em> <em>Je mange chez toi samedi</em> is geen "
                  "uitnodiging maar een mededeling over jezelf."),
            ("p", "Pas je <strong>toon</strong> aan de ontvanger aan. Aan een leraar schrijf je "
                  "vous en een nette groet, aan je beste vriend tu en salut. Wie de verkeerde "
                  "toon kiest, klinkt onbedoeld onvriendelijk, ook als elk woord juist gespeld "
                  "is: <em>register en beleefdheidsconventies</em> is een eigen rij waarop je "
                  "beoordeeld wordt."),
            ("p", "<strong>Lichaamstaal</strong> hoort erbij: je gebruikt ze zelf om je "
                  "boodschap over te brengen, en je schat die van je gesprekspartner in om er "
                  "goed op te reageren."),
        ]),
        dict(kop="Frans in België en in de wereld", blokken=[
            ("kader", "<em>En Belgique, trois langues sont officielles : le néerlandais, le "
                      "français et l'allemand. Le français est la langue de la Wallonie et, avec "
                      "le néerlandais, de Bruxelles. Un Belge francophone dit septante et "
                      "nonante, là où un Français dit soixante-dix et quatre-vingt-dix.</em>"),
            ("p", "Het is dus <strong>dezelfde taal</strong>, met hier en daar een ander woord. "
                  "Een taal kan van streek tot streek verschillen zonder een andere taal te "
                  "worden. Frans wordt ook gesproken in <strong>Zwitserland</strong>, "
                  "<strong>Luxemburg</strong>, <strong>Québec</strong> en in veel landen van "
                  "<strong>Afrika</strong>: de woorden en het accent zijn niet overal gelijk, "
                  "maar men begrijpt elkaar."),
            ("fig", tabel(["België", "Frankrijk"], [
                ["septante (70)", "soixante-dix"],
                ["nonante (90)", "quatre-vingt-dix"],
                ["fête nationale: 21 juli", "fête nationale: 14 juli"],
            ]), "Twee getallen en twee feestdagen, allebei juist Frans."),
            ("p", "Een paar <strong>gewoontes</strong> die in een examentekst kunnen opduiken: "
                  "in veel Franse steden sluiten de winkels tussen de middag en twee uur, en op "
                  "zondag is vaak alleen de bakker open, meestal enkel in de voormiddag. En aan "
                  "tafel is <em>le repas principal</em> doorgaans 's avonds, met het brood naast "
                  "het bord en de kaas vóór het dessert."),
        ]),
    ],
    onthoud=[
        "Eerst bonjour, dan je vraag. Ook bij een verkoper of een agent.",
        "tu bij een vriend, vous bij een onbekende volwassene of een klant.",
        "Vous is ook de hoffelijke vorm voor één persoon.",
        "s'il vous plaît bij vous, s'il te plaît bij tu.",
        "la bise: in Franstalig België ook tussen mannen.",
        "België: septante en nonante, en de nationale feestdag op 21 juli.",
        "Frans is officieel in België, en wordt ook in Zwitserland, Québec en Afrika gesproken.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["schrijven-schriftelijke-interactie-en-leesbeleving" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Schrijven, schriftelijke interactie en leesbeleving",
    onder="Vijf schrijfopdrachten, de strategieën eromheen, en de rijen waarop je beoordeeld wordt.",
    secties=[
        dict(kop="Wat je moet kunnen schrijven", blokken=[
            ("p", "Schrijven en schriftelijke interactie zijn samen <strong>16 %</strong> van je "
                  "examen. Vijf dingen worden van je gevraagd, elk met een gewone situatie."),
            ("fig", tabel(["wat je doet", "een voorbeeld"], [
                ["alledaagse sociale contacten leggen",
                 "begroeten, bedanken, uitnodigen, je verontschuldigen"],
                ["informatie geven en vragen",
                 "een zoekertje opstellen, een mail over een vakantiejob"],
                ["je mening geven", "reageren op een discussie op sociale media"],
                ["iets vertellen", "verslag uitbrengen over je stage"],
                ["iemand iets uitleggen", "een gerecht, de weg, tips om gezonder te eten"],
            ]), "Vijf opdrachten. Bij elk daarvan telt eerst of je doel bereikt is."),
            ("p", "Een <strong>zoekertje</strong> is volledig als er drie dingen in staan: wat "
                  "je verkoopt en in welke staat, de prijs, en hoe men je kan bereiken. Een "
                  "<strong>mail om te solliciteren</strong> begint met <em>Madame, Monsieur,</em> "
                  "en zegt wie je bent, wanneer je kan werken en waarom je die job wil. Je punten "
                  "op school horen daar niet in."),
            ("p", "Om iets te <strong>vragen</strong> gebruik je de hoffelijke vorm: <em>je "
                  "voudrais</em> in plaats van <em>je veux</em>, en <em>Pourriez-vous me dire "
                  "quand je peux venir me présenter ?</em> in plaats van <em>Je passe demain "
                  "matin.</em>"),
        ]),
        dict(kop="Je mening, een verhaal, een uitleg", blokken=[
            ("fig", tabel(["wat je wil zeggen", "Frans"], [
                ["je mening inleiden", "À mon avis, … / Je pense que … / Pour moi, …"],
                ["het eens zijn", "Je suis d'accord avec toi."],
                ["hoffelijk oneens zijn", "Je ne suis pas d'accord, mais je comprends ton point de vue."],
                ["een reden geven", "… parce que …"],
            ]), "Een mening zonder reden blijft een kreet; zet er parce que achter."),
            ("p", "Wie iets <strong>vertelt</strong> over een afgelopen gebeurtenis, schrijft in "
                  "de verleden tijd: de gebeurtenissen in de <em>passé composé</em>, de "
                  "omstandigheden in de <em>imparfait</em>. En je maakt de orde duidelijk met "
                  "<em>d'abord, ensuite, puis, enfin</em>. Een tekst heeft best een inleiding, "
                  "een midden en een slot."),
            ("fig", svg.tekstopbouw([
                ("inleiding", "waarover je gaat schrijven", 1),
                ("midden", "je punten, met d'abord, ensuite, puis, enfin", 1.6),
                ("slot", "je besluit of een vraag aan de lezer", 1),
            ]),
             "Drie delen, met signaalwoorden ertussen: zo kan een lezer je volgen."),
            ("p", "Wie iets <strong>uitlegt</strong>, gebruikt de <em>impératif</em>: "
                  "<em>coupez</em>, <em>ajoutez</em>, <em>tournez à droite</em>, <em>allez tout "
                  "droit</em>, <em>prenez la deuxième rue</em>. En je slaat geen stappen over: "
                  "een uitleg die de helft weglaat, bereikt zijn doel niet."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["à droite / à gauche", "naar rechts / naar links"],
                ["tout droit", "rechtdoor"],
                ["prenez la deuxième rue", "neem de tweede straat"],
                ["au bout de la rue", "op het einde van de straat"],
            ]), "Vier uitdrukkingen waarmee je iemand de weg kan uitleggen."),
        ]),
        dict(kop="De strategieën bij het schrijven", blokken=[
            ("fig", svg.stappen([
                "Plan|Kernwoorden in orde",
                "Schrijf|Met de woorden die je kent",
                "Lees na|Is het helder en gepast?",
            ]), "Drie stappen. De laatste wordt het vaakst overgeslagen en kost het meest."),
            ("p", "Begin met het <strong>communicatiemodel</strong>: waarom schrijf je, voor wie "
                  "is je boodschap, met wie communiceer je, wat wil je precies vertellen, en "
                  "welk kanaal gebruik je — een mail, een blogbericht, een bericht in een app?"),
            ("p", "Maak dan een <strong>schrijfplan met kernwoorden</strong>: een lijstje van de "
                  "punten die je wil zeggen, in de orde waarin je ze zal schrijven. Zo vergeet "
                  "je niets en staat je tekst meteen logisch."),
            ("p", "Zit je vast? Laat je niet ontmoedigen, maar <strong>zeg het met de woorden en "
                  "structuren die je al kent</strong>. Een omweg die aankomt, is beter dan een "
                  "perfecte zin die er niet komt. Je mag daarbij het online woordenboek en de "
                  "spellingcontrole gebruiken die in je examen staan."),
            ("kader", "<strong>Lees je tekst grondig na.</strong> Is de communicatie helder, "
                      "gepast en vlot? Een spellingcontrole ziet niet dat je <em>a</em> schreef "
                      "waar <em>à</em> moest staan, of <em>ou</em> waar <em>où</em> hoorde. Die "
                      "keuzes blijven jouw werk."),
        ]),
        dict(kop="Waarop je beoordeeld wordt", blokken=[
            ("fig", tabel(["rij", "wat ze nakijkt"], [
                ["taakvoltooiing", "het doel is bereikt, je boodschap is volledig en ter zake, en je respecteert de opgegeven lengte"],
                ["woordenschat", "je gebruikt frequente woorden en vaste uitdrukkingen correct"],
                ["grammatica en zinsbouw", "eenvoudige correcte zinnen; fouten verstoren de communicatie niet"],
                ["tekststructuur en samenhang", "inleiding, midden en slot, met herkenbare tekstverbanden"],
                ["register en beleefdheidsconventies", "een gepaste toon en gepaste omgangsvormen"],
                ["tekstopbouw en lay-out", "alleen bij schrijven: een duidelijke vorm die bij de tekstsoort past"],
                ["spelling en leestekengebruik", "alleen bij schrijven: fouten staan het begrip niet in de weg"],
            ]), "Zeven rijen. De laatste twee gelden niet bij spreken; daar komen lichaamstaal, tempo en uitspraak in de plaats."),
            ("p", "Twee dingen die leerlingen punten kosten zonder dat ze één fout Frans "
                  "schrijven: de <strong>lengte</strong> niet respecteren — 150 woorden waar er "
                  "80 gevraagd worden — en de <strong>aanspreking en de slotformule</strong> "
                  "weglaten om kort te blijven."),
            ("kader", GEEN_GIS),
        ]),
        dict(kop="Je leesbeleving in het Frans verwoorden", blokken=[
            ("p", "Bij een <strong>literaire tekst</strong> vraagt het examen iets anders dan "
                  "begrijpen: je verwoordt schriftelijk in het Frans je eigen ervaring en "
                  "gevoelens. Je krijgt daarvoor een <strong>schrijfkader</strong>, "
                  "sleutelwoorden of een voorbeeld, zodat je niet voor een wit blad begint."),
            ("kader", "<strong>Een tekst en een reactie.</strong> <em>Je t'écris d'une ville où "
                      "il pleut tous les jours, où les trains ne s'arrêtent plus. Si tu passes "
                      "un dimanche, apporte-moi le soleil.</em><br><em>Ce texte me touche parce "
                      "que je connais ce sentiment. Moi aussi, j'ai déjà attendu quelqu'un "
                      "pendant tout un hiver. J'aime la dernière phrase : apporte-moi le soleil, "
                      "ça veut dire apporte-moi un peu de joie.</em><br>"
                      "Die reactie doet drie dingen goed: ze zegt wat de tekst oproept, ze legt "
                      "uit waarom met iets uit haar eigen leven, en ze verwijst naar een zin uit "
                      "de tekst."),
            ("fig", tabel(["wat je zegt", "Frans"], [
                ["dit raakt me", "Ce texte me touche."],
                ["het doet me denken aan", "Ce passage me fait penser à mon enfance."],
                ["ik vereenzelvig me met", "Je m'identifie au personnage principal."],
                ["ik vind de stijl mooi", "J'aime la façon dont c'est écrit."],
            ]), "Vier zinnen om mee te beginnen. Een samenvatting van de tekst is geen beleving."),
            ("p", "Er bestaat geen juist gevoel. Je mag ook schrijven dat een tekst je niets "
                  "doet, zolang je uitlegt waarom. Wat beoordeeld wordt, is of je je ervaring in "
                  "het Frans duidelijk kan verwoorden en met de tekst kan verbinden."),
        ]),
    ],
    onthoud=[
        "Vijf opdrachten: contact leggen, informatie geven en vragen, je mening, vertellen, uitleggen.",
        "je voudrais en pourriez-vous zijn hoffelijker dan je veux en tu peux.",
        "Een mening krijgt een reden met parce que.",
        "Vertellen = passé composé en imparfait. Uitleggen = impératif.",
        "Plan met kernwoorden, dan schrijven, dan grondig nalezen.",
        "Taakvoltooiing telt ook de opgegeven lengte.",
        "Bij een literaire tekst schrijf je je eigen gevoel, met een reden erbij.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["spreken-gesprekken-klank-en-spelling" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Spreken, gesprekken, klank en spelling",
    onder="Hoe het examen verloopt, wat je in een gesprek zegt, en hoe het Frans klinkt dat je ziet staan.",
    secties=[
        dict(kop="Zo ziet je examen eruit", blokken=[
            ("kader", SCHRIFTELIJK),
            ("fig", tabel(["onderdeel", "waar en hoelang"], [
                ["spreekopdracht", "thuis opnemen, indienen tot drie dagen voor je digitale examen"],
                ["digitaal examen", "150 minuten in het examencentrum in Brussel: lezen, luisteren en schrijven"],
                ["voorbereiding mondeling", "15 minuten voor twee opdrachten"],
                ["gesprek", "10 minuten met de examinator"],
            ]), "Dien je spreekopdracht tijdig in: anders mag je niet deelnemen aan het examen in het centrum."),
            ("p", "Je krijgt ter plaatse een <strong>balpen en kladpapier</strong>, een "
                  "<strong>hoofdtelefoon</strong>, en in je examen staan <strong>links</strong> "
                  "naar het digitale woordenboek en de spellingcontrole. Een eigen laptop breng "
                  "je niet mee."),
            ("p", "Je persoonlijke spullen laat je in een <strong>locker</strong> in de "
                  "onthaalruimte: je jas, je tas en je gsm. Een gsm, een smartwatch, "
                  "cursusmateriaal of een samenvatting bij je hebben in de examenruimte wordt "
                  "als <strong>examenfraude</strong> beschouwd."),
            ("weetje", "Je krijgt voorbereidingstijd voor de mondelinge opdrachten, maar je moet "
                       "in het gesprek zelf ook <strong>spontaan</strong> kunnen reageren. Een "
                       "uitgeschreven tekst voorlezen werkt daar dus niet."),
        ]),
        dict(kop="Een gesprek beginnen, gaande houden en beëindigen", blokken=[
            ("p", "Bij een <strong>spreekopdracht</strong> ben je alleen aan het woord. Bij een "
                  "<strong>gesprek</strong> moet je reageren op je gesprekspartner: je begint "
                  "een eenvoudig gesprek, je houdt het gaande en je beëindigt het."),
            ("fig", svg.spreekballonnen([
                ("beginnen", "Bonjour, je peux vous poser une question ?", True),
                ("gaande houden", "Et vous, qu'en pensez-vous ?", False),
                ("beëindigen", "Merci beaucoup, bonne journée !", True),
            ]), "Beginnen, de ander erbij halen, afsluiten: drie verschillende dingen."),
            ("fig", tabel(["als …", "dan zeg je"], [
                ["je iets niet begrepen hebt", "Vous pouvez répéter, s'il vous plaît ?"],
                ["het te snel gaat", "Pouvez-vous parler plus lentement ?"],
                ["de ander jou niet begrijpt", "je herhaalt, of je zegt het op een andere manier"],
                ["je een woord niet vindt", "je zegt het met de woorden die je wél kent"],
            ]), "Dat vragen is een strategie, geen zwakte. Luider spreken helpt zelden."),
            ("p", "Speel in op wat je gesprekspartner zegt, toon interesse en toon respect. Een "
                  "gesprek gaande houden is net dát: niet je eigen verhaal afmaken, maar ingaan "
                  "op de ander."),
        ]),
        dict(kop="Waarop je bij spreken beoordeeld wordt", blokken=[
            ("fig", tabel(["rij", "wat ze nakijkt"], [
                ["lichaamstaal", "je gebruikt een gepaste lichaamstaal"],
                ["spreektempo en vlotheid", "onderbrekingen, valse starts en herformuleringen zijn aanvaardbaar"],
                ["uitspraak en intonatie", "je uitspraak is voldoende helder en belemmert het begrip niet"],
            ]), "Drie rijen die alleen bij spreken gelden. Klinken als een moedertaalspreker hoeft niet."),
            ("p", "De vier rijen die je ook bij schrijven hebt, blijven gelden: "
                  "taakvoltooiing, woordenschat, grammatica en zinsbouw, tekststructuur en "
                  "samenhang, en register en beleefdheidsconventies. <em>Spelling en "
                  "leestekengebruik</em> en <em>tekstopbouw en lay-out</em> gelden hier niet: "
                  "die kan je al sprekend niet laten zien."),
            ("p", "Bereid een spreekopdracht voor met een <strong>plan met kernwoorden</strong> "
                  "en oefen <strong>luidop</strong>. Dat helpt je tempo en je uitspraak meer dan "
                  "een tekst uit het hoofd leren."),
        ]),
        dict(kop="Klanken en klankencombinaties", blokken=[
            ("fig", tabel(["schrift", "klank", "voorbeeld"], [
                ["ou", "oe", "bouche, rouge, tout"],
                ["oi", "ongeveer wa", "moi, trois, voiture"],
                ["ai", "è", "maison, français"],
                ["eu", "eu", "deux, heureux"],
                ["an, en", "nasaal an", "dans, prendre"],
                ["on", "nasaal on", "bonjour, maison"],
                ["in, ain", "nasaal in", "matin, pain"],
                ["ch", "sj", "chercher, chambre"],
            ]), "Acht combinaties. Wie ze kent, leest een onbekend woord meteen juist."),
            ("p", "Een paar letters <strong>schrijf je wel en hoor je niet</strong>. De slot-t "
                  "van <em>petit</em> blijft stil, de uitgang <em>-ent</em> van <em>ils "
                  "parlent</em> hoor je niet (<em>ils parlent</em> klinkt als <em>il "
                  "parle</em>), en de <strong>h</strong> aan het begin is altijd stil: daarom "
                  "zeg je <em>l'heure</em> en niet <em>la heure</em>, en <em>l'hôtel</em>."),
            ("p", "De <strong>c</strong> en de <strong>g</strong> hangen af van de letter erna: "
                  "voor <em>e</em> en <em>i</em> klinkt de c als een s (<em>cent</em>, "
                  "<em>ciel</em>), voor <em>a</em>, <em>o</em> en <em>u</em> als een k "
                  "(<em>car</em>, <em>couleur</em>). Dezelfde regel bij de g: <em>gentil</em> "
                  "tegenover <em>gare</em>. Wil je toch een s-klank voor een a of een o, dan zet "
                  "je een <strong>cédille</strong> onder de c: <em>ça</em>, <em>garçon</em>, "
                  "<em>français</em>."),
        ]),
        dict(kop="Accenten, klemtoon en intonatie", blokken=[
            ("fig", tabel(["paar", "verschil"], [
                ["a / à", "il a = hij heeft; à Bruxelles = in Brussel"],
                ["ou / où", "of / waar"],
                ["la / là", "het lidwoord / daar"],
                ["é / è", "été (gesloten, zoals in beek) / père (open, zoals in bed)"],
                ["aller / allé", "infinitief / voltooid deelwoord"],
            ]), "Eén accent maakt er een ander woord van. Dat is geen versiering."),
            ("p", "Het <strong>accent aigu</strong> helt naar rechts (<em>été</em>, "
                  "<em>élève</em>), het <strong>accent grave</strong> naar links (<em>père</em>, "
                  "<em>très</em>). En het verschil tussen <em>aller</em> (infinitief), "
                  "<em>allez</em> (persoonsvorm) en <em>allé</em> (voltooid deelwoord) zie je "
                  "alleen in het schrift: ze klinken bijna gelijk."),
            ("p", "De <strong>klemtoon</strong> van een Frans woord of woordgroep valt meestal "
                  "op de <strong>laatste</strong> lettergreep: vergelijk het Nederlandse "
                  "TE-le-foon met het Franse té-lé-PHONE. Dat is een van de dingen die Frans "
                  "Frans doet klinken."),
            ("p", "Met je <strong>intonatie</strong> alleen kan je van een mededeling een vraag "
                  "maken: <em>Tu viens.</em> wordt <em>Tu viens ?</em> door je stem op het einde "
                  "omhoog te laten gaan. En duidelijk <strong>articuleren</strong> betekent dat "
                  "je elke klank goed vormt, ook aan het einde van een woord."),
            ("p", "Tot slot vraagt het examen de <strong>spelling van frequente woorden</strong>. "
                  "Een spellingcontrole helpt je daar niet volledig: ze ziet niet dat je "
                  "<em>a</em> schreef waar <em>à</em> moest staan."),
        ]),
    ],
    onthoud=[
        "Drie delen: spreekopdracht thuis, digitaal examen van 150 minuten, gesprek van 10 minuten.",
        "Gsm, smartwatch en samenvattingen in de locker; anders is het examenfraude.",
        "Vous pouvez répéter ? en Pouvez-vous parler plus lentement ? mag je altijd vragen.",
        "ou = oe, oi = wa, ch = sj, en de h aan het begin hoor je nooit.",
        "c en g klinken zacht voor e en i; de cédille maakt ç zacht voor a, o en u.",
        "a / à, ou / où, la / là: één accent, een ander woord.",
        "De klemtoon valt in het Frans op de laatste lettergreep.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordvelden-mens-familie-gevoelens-en-gezondheid" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Woordvelden: mens, familie, gevoelens en gezondheid",
    onder="Jezelf en je gezin, wat je voelt, en wat je zegt als je je niet goed voelt.",
    secties=[
        dict(kop="Waarom woordenschat nooit een doel op zich is", blokken=[
            ("p", "Je hebt woorden nodig om teksten te begrijpen en om zelf te schrijven of te "
                  "spreken. Daarom staan ze hier niet in een kale lijst, maar in zinnen waarin "
                  "ze iets doen. Hoe rijker je woordenschat, hoe vlotter het gaat — en hoe "
                  "minder je moet opzoeken op een examen waar je daar de tijd niet voor hebt."),
            ("p", "De woordvelden van dit thema: <strong>familie</strong>, "
                  "<strong>gevoelens</strong>, <strong>gezondheid en lichaamsdelen</strong>, "
                  "<strong>persoonlijke gegevens</strong>, en de "
                  "<strong>instructietaal</strong> die je op een examen nodig hebt."),
        ]),
        dict(kop="De familie en je persoonlijke gegevens", blokken=[
            ("fig", svg.stamboom(),
             "Dezelfde namen als in het Nederlands, maar elk met zijn eigen lidwoord."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["les parents, le père, la mère", "de ouders, de vader, de moeder"],
                ["le frère, la sœur", "de broer, de zus"],
                ["les grands-parents", "de grootouders"],
                ["l'oncle, la tante", "de oom, de tante"],
                ["le cousin, la cousine", "de neef, de nicht"],
                ["l'aîné, le cadet", "de oudste, de jongste"],
            ]), "Le voisin, de buur, hoort niet bij de familie maar bij het woordveld wonen."),
            ("p", "Om iemand te <strong>vergelijken</strong> gebruik je <em>plus … que</em>: "
                  "<em>J'ai un frère plus jeune que moi.</em> En let op: <em>sœur</em> schrijf je "
                  "met een œ, maar <em>soeur</em> mag ook als je dat teken niet vindt."),
            ("fig", tabel(["op een formulier", "Nederlands"], [
                ["nom / prénom", "familienaam / voornaam"],
                ["date de naissance", "geboortedatum"],
                ["lieu de naissance", "geboorteplaats"],
                ["nationalité", "nationaliteit"],
                ["adresse", "adres"],
                ["numéro de téléphone", "telefoonnummer"],
            ]), "In het Frans staat de familienaam eerst: nom, dan prénom."),
            ("p", "Op de vraag <em>Quelle est votre nationalité ?</em> antwoord je <em>Je suis "
                  "belge</em> — met een <strong>kleine letter</strong>, want een nationaliteit "
                  "is in het Frans een bijvoeglijk naamwoord. Het land krijgt wel een "
                  "hoofdletter: <em>la Belgique</em>."),
        ]),
        dict(kop="Gevoelens", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["content, contente", "tevreden, blij"],
                ["triste", "verdrietig"],
                ["fatigué, fatiguée", "moe"],
                ["être en colère / fâché", "boos zijn, kwaad zijn"],
                ["avoir peur", "bang zijn"],
                ["heureux, heureuse", "gelukkig"],
            ]), "Een gevoel verandert mee met wie het zegt: fatigué of fatiguée."),
            ("p", "Twee dingen om op te letten. <em>Je suis fatigué</em> en <em>je suis "
                  "fatiguée</em> klinken <strong>gelijk</strong>: die extra e schrijf je omdat "
                  "een meisje het zegt. En het Frans gebruikt <strong>avoir</strong> waar wij "
                  "'zijn' zeggen: <em>j'ai faim</em> (ik heb honger), <em>j'ai soif</em>, "
                  "<em>j'ai froid</em>, <em>j'ai chaud</em>, <em>j'ai peur</em> — telkens zonder "
                  "lidwoord."),
            ("kader", "<strong>In een tekstje.</strong> <em>Hier, j'étais vraiment fatiguée, et "
                      "un peu triste aussi. Ce matin, ça va beaucoup mieux : j'ai reçu une bonne "
                      "nouvelle et je suis contente. Mon frère, lui, est en colère parce que son "
                      "équipe a perdu.</em><br>Drie gevoelens, drie personen, en twee tijden: "
                      "<em>j'étais</em> voor gisteren, <em>je suis</em> voor vandaag."),
        ]),
        dict(kop="Het lichaam en de gezondheid", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la tête, la gorge", "het hoofd, de keel of hals"],
                ["le ventre, le dos", "de buik, de rug"],
                ["la main, le pied", "de hand, de voet"],
                ["la jambe, le bras", "het been, de arm"],
                ["l'épaule, le coude, le genou", "de schouder, de elleboog, de knie"],
                ["un œil, les yeux; une dent", "een oog, de ogen; een tand"],
            ]), "Les yeux is een onregelmatig meervoud: dat moet je kennen."),
            ("p", "Pijn zeg je met <strong>avoir mal à</strong>: <em>j'ai mal à la tête</em>, "
                  "<em>j'ai mal au ventre</em> (want à + le wordt au), <em>j'ai mal aux "
                  "dents</em> (à + les wordt aux). Verwar <em>aux dents</em> (tandpijn) niet met "
                  "<em>aux oreilles</em> (oorpijn)."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["Je ne me sens pas bien.", "Ik voel me niet goed."],
                ["Je suis malade.", "Ik ben ziek."],
                ["avoir de la fièvre", "koorts hebben"],
                ["une ordonnance", "een voorschrift"],
                ["un comprimé, un médicament", "een tablet, een geneesmiddel"],
                ["la pharmacie, le pharmacien", "de apotheek, de apotheker"],
            ]), "Se sentir is wederkerend: je me sens, tu te sens, il se sent."),
            ("kader", "<strong>Bij de dokter.</strong> <em>— Bonjour, qu'est-ce qui ne va pas ? "
                      "— J'ai mal au ventre depuis deux jours, docteur. — Vous avez de la "
                      "fièvre ? — Non, mais je dors mal. — Je vous donne une ordonnance. Prenez "
                      "un comprimé matin et soir, pendant cinq jours.</em><br>"
                      "<em>Qu'est-ce qui ne va pas ?</em> is de gewone openingsvraag van een "
                      "dokter, en <em>depuis</em> betekent sinds."),
            ("p", "Een <strong>afspraak</strong> maak je met <em>Je voudrais prendre un "
                  "rendez-vous, s'il vous plaît.</em> In de <strong>apotheek</strong> krijg je "
                  "paracetamol <em>sans ordonnance</em>, maar voor een antibioticum heb je er "
                  "wel een nodig; vraag advies met <em>Demandez conseil au pharmacien.</em> En "
                  "zoek je een dokter in een vreemde stad: <em>Excusez-moi, où est le médecin le "
                  "plus proche ?</em>"),
        ]),
        dict(kop="Instructietaal: de opdracht zelf begrijpen", blokken=[
            ("fig", tabel(["Frans", "wat je moet doen"], [
                ["Complétez le texte avec les mots suivants.", "vul de tekst aan met de woorden die erbij staan"],
                ["Cochez la bonne réponse.", "kruis het juiste antwoord aan"],
                ["Reliez.", "verbind met elkaar"],
                ["Mettez dans le bon ordre.", "zet in de juiste orde"],
                ["Répondez en français.", "antwoord in het Frans"],
                ["Justifiez votre réponse.", "verantwoord je antwoord"],
            ]), "Wie de opdracht niet begrijpt, verliest punten zonder één taalfout te maken."),
            ("p", "Twee woorden om te onthouden: <em>une question</em> is de vraag, <em>une "
                  "réponse</em> het antwoord. En <em>suivant</em> betekent volgend."),
        ]),
    ],
    onthoud=[
        "Het lidwoord hoort bij het woord: la sœur, le frère, l'oncle, la tante.",
        "nom = familienaam, prénom = voornaam. Nationaliteit met een kleine letter.",
        "Het Frans zegt avoir waar wij zijn zeggen: j'ai faim, j'ai peur, j'ai quinze ans.",
        "avoir mal à la tête, au ventre, aux dents.",
        "un œil wordt les yeux.",
        "ordonnance = voorschrift; sans ordonnance = zonder voorschrift.",
        "Lees de instructietaal: cochez, complétez, reliez, justifiez.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordvelden-eten-kleding-wonen-en-winkelen" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Woordvelden: eten, kleding, wonen en winkelen",
    onder="De woorden van een gewone dag: een menu, een boodschappenlijst, een kassa, een zoekertje voor een woning.",
    secties=[
        dict(kop="Eten en drinken", blokken=[
            ("p", "De woordvelden van dit thema: <strong>eten en drinken</strong>; "
                  "<strong>winkels en diensten</strong>; <strong>cijfers, gewichten, maten en "
                  "hoeveelheden</strong>; <strong>kleding en accessoires</strong>; "
                  "<strong>kleuren, vormen en materialen</strong>; de "
                  "<strong>woning</strong> met haar meubels en uitrusting; "
                  "<strong>dagelijkse bezigheden</strong>; en <strong>dagelijkse of "
                  "persoonlijke voorwerpen</strong>."),
            ("kader", "<strong>Een menu lezen.</strong> <em>Menu du jour — Entrée : soupe de "
                      "légumes ou salade de tomates. Plat : poulet et frites, ou pâtes aux "
                      "champignons (plat végétarien). Dessert : glace, fruits de saison ou crêpe "
                      "au sucre. Boisson comprise : eau, jus d'orange ou limonade. 14 "
                      "euros.</em><br>Drie gangen: <em>entrée</em>, <em>plat</em>, "
                      "<em>dessert</em>. <em>Boisson comprise</em> betekent drank inbegrepen, en "
                      "koffie staat er niet bij."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["le poulet, le poisson, le porc", "kip, vis, varkensvlees"],
                ["le pain, le fromage", "brood, kaas"],
                ["les légumes, les fruits", "de groenten, het fruit"],
                ["l'eau, le jus d'orange", "water, sinaasappelsap"],
                ["une entrée, un plat, un dessert", "een voorgerecht, een hoofdgerecht, een nagerecht"],
                ["végétarien", "vegetarisch"],
            ]), "Vier woorden met een p die je niet mag verwarren: poulet, poisson, porc, pain."),
        ]),
        dict(kop="Hoeveelheden, maten en de kassa", blokken=[
            ("p", "Na een <strong>hoeveelheid</strong> komt in het Frans alleen <em>de</em>: "
                  "<em>un kilo de pommes de terre</em>, <em>500 grammes de carottes</em>, <em>une "
                  "bouteille de lait</em>, <em>un paquet de pâtes</em>, <em>un litre d'eau</em>, "
                  "<em>beaucoup de monde</em>, <em>un peu de sel</em>, <em>trop de bruit</em>, "
                  "<em>assez de places</em> — nooit <em>des</em> of <em>du</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un kilo, un gramme, un litre", "een kilo, een gram, een liter"],
                ["une bouteille, un paquet", "een fles, een pak"],
                ["six œufs", "zes eieren"],
                ["un billet, une pièce", "een biljet, een muntstuk"],
                ["payer par carte / en espèces", "met de kaart / met cash geld betalen"],
                ["un ticket", "een kassabon"],
            ]), "Un billet kan ook een ticket zijn, bijvoorbeeld voor de trein."),
            ("kader", "<strong>Aan de kassa.</strong> <em>— Bonjour, ce sera tout ? — Oui, et je "
                      "voudrais un sac, s'il vous plaît. — Ça fait 23,40 euros. Vous payez par "
                      "carte ou en espèces ? — Par carte. — Voilà votre ticket, bonne "
                      "journée !</em><br><em>Ce sera tout ?</em> betekent: is dat alles? Vragen "
                      "wat iets kost doe je met <em>Ça coûte combien ?</em>"),
            ("fig", tabel(["winkel of dienst", "wat je er vindt"], [
                ["la boulangerie", "brood, une baguette"],
                ["la boucherie", "vlees"],
                ["la pharmacie", "geneesmiddelen"],
                ["la librairie", "boeken (geen bibliotheek!)"],
                ["la poste, la banque", "post, bank"],
                ["le magasin, le marché", "de winkel, de markt"],
            ]), "La librairie is een boekhandel; een bibliotheek is une bibliothèque."),
        ]),
        dict(kop="Kleding, kleuren, vormen en materialen", blokken=[
            ("kader", "<em>Pour l'entretien, mets un pantalon noir et une chemise blanche. Pas "
                      "de baskets : des chaussures fermées. S'il fait froid, prends ta veste "
                      "grise, mais laisse ton bonnet dans ton sac.</em><br>"
                      "<em>Pas de baskets</em> betekent geen sportschoenen; <em>des chaussures "
                      "fermées</em> zijn gesloten schoenen."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un pantalon, une chemise", "een broek, een hemd"],
                ["une veste, un pull", "een vest, een trui"],
                ["une jupe, une robe", "een rok, een kleed"],
                ["des chaussures, des baskets", "schoenen, sportschoenen"],
                ["un bonnet, un sac", "een muts, een zak of tas"],
            ]), "Un bonnet de bain is een badmuts, verplicht in veel Franse zwembaden."),
            ("fig", svg.kleurstalen([
                ("noir / noire", "zwart", "#1f2328"),
                ("blanc / blanche", "wit", "#f7f5ee"),
                ("gris / grise", "grijs", "#8d9298"),
                ("rouge", "rood", "#c0392b"),
                ("vert / verte", "groen", "#2f5d50"),
                ("bleu / bleue", "blauw", "#2c5f8a"),
                ("jaune", "geel", "#e0b43a"),
                ("brun / marron", "bruin", "#7a5230"),
            ]), "Een kleur past zich aan het naamwoord aan, en staat erachter: une voiture rouge."),
            ("p", "<strong>Vormen</strong> en <strong>materialen</strong> horen bij hetzelfde "
                  "woordveld maar zijn geen kleuren: <em>rond</em>, <em>carré</em> (vierkant), "
                  "<em>rectangulaire</em> (rechthoekig) zijn vormen; <em>le bois</em> (hout), "
                  "<em>le verre</em> (glas), <em>le coton</em> (katoen), <em>le métal</em>, "
                  "<em>le plastique</em> zijn materialen."),
        ]),
        dict(kop="De woning", blokken=[
            ("kader", "<strong>Een zoekertje.</strong> <em>L'appartement a deux chambres, une "
                      "cuisine équipée et une petite salle de bains. Le salon donne sur un "
                      "balcon. Il y a un lave-linge dans la cave. Le loyer est de 650 euros par "
                      "mois, charges comprises.</em><br>"
                      "<em>Une chambre</em> is een slaapkamer, <em>une cave</em> een kelder, "
                      "<em>le loyer</em> de huurprijs, en <em>charges comprises</em> betekent "
                      "kosten inbegrepen."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la cuisine, le salon", "de keuken, de woonkamer"],
                ["la chambre, la salle de bains", "de slaapkamer, de badkamer"],
                ["la cave, le grenier", "de kelder, de zolder"],
                ["le balcon, le jardin", "het balkon, de tuin"],
                ["une table, une chaise, un lit", "een tafel, een stoel, een bed"],
                ["un frigo, un lave-linge", "een koelkast, een wasmachine"],
            ]), "Le loyer is geen voorwerp maar de prijs die je elke maand betaalt."),
        ]),
        dict(kop="Een dag thuis", blokken=[
            ("kader", "<em>En semaine, je me lève à six heures et demie. Je me douche, je prends "
                      "mon petit-déjeuner et je pars à sept heures et quart. L'après-midi, je "
                      "fais mes devoirs avant de sortir. Le soir, c'est moi qui mets la table et "
                      "mon frère qui fait la vaisselle.</em>"),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["se lever, se doucher", "opstaan, zich douchen"],
                ["se raser, s'habiller", "zich scheren, zich kleden"],
                ["mettre la table", "de tafel dekken"],
                ["faire la vaisselle", "de vaat doen"],
                ["ranger sa chambre", "zijn kamer opruimen"],
                ["sortir la poubelle", "het vuilnis buitenzetten"],
            ]), "De eerste vier zijn wederkerend of met faire; de laatste twee zijn gewone werkwoorden."),
            ("p", "En de dingen die je op zak hebt: <em>les clés</em> (de sleutels), <em>le "
                  "portefeuille</em> (de portefeuille), <em>le parapluie</em> (de paraplu), "
                  "<em>le téléphone</em>. Een <em>balcon</em> hoort bij de woning en gaat niet "
                  "mee in je zak."),
        ]),
    ],
    onthoud=[
        "Entrée – plat – dessert. Boisson comprise = drank inbegrepen.",
        "Na een hoeveelheid komt de: un kilo de pommes, beaucoup de monde.",
        "payer par carte of en espèces; ce sera tout ? = is dat alles?",
        "La librairie is een boekhandel, la bibliothèque een bibliotheek.",
        "Een kleur staat achter het naamwoord en past zich aan: une veste grise.",
        "le loyer = de huur; charges comprises = kosten inbegrepen.",
        "mettre la table, faire la vaisselle, ranger sa chambre.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordvelden-school-werk-en-de-professionele-wereld" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Woordvelden: school, werk en de professionele wereld",
    onder="Onderwijs, beroepen, solliciteren, multimedia, sport en vrije tijd.",
    secties=[
        dict(kop="Op school", blokken=[
            ("p", "De woordvelden van dit thema: <strong>onderwijs en vorming</strong>; de "
                  "<strong>professionele wereld</strong> met de beroepen; "
                  "<strong>communicatie en multimedia</strong>; en <strong>sport en "
                  "ontspanning</strong>. Dit zijn de woorden waarmee je over jezelf en je "
                  "toekomst spreekt, en net daarom komen ze op het examen terug in een mail over "
                  "een vakantiejob of in een verslag over je stage."),
            ("kader", "<em>Je suis en quatrième année. Mes cours préférés sont le français et "
                      "les sciences. Les maths, c'est plus difficile pour moi, mais j'ai un bon "
                      "professeur. Nous avons cours de huit heures vingt à quatre heures, avec "
                      "une heure de midi. Le mercredi, on finit à midi.</em><br>"
                      "<em>Être en quatrième année</em>: in het vierde jaar zitten, met een "
                      "rangtelwoord. <em>Midi</em> is twaalf uur 's middags; "
                      "<em>minuit</em> is middernacht."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un cours, une heure de cours", "een les, een lesuur"],
                ["un devoir, une interrogation", "een taak, een overhoring"],
                ["un examen, un bulletin", "een examen, een rapport"],
                ["un trimestre, un semestre", "een trimester, een halfjaar"],
                ["le professeur, le titulaire", "de leraar, de klastitularis"],
                ["une année scolaire", "een schooljaar"],
                ["une remarque, une note", "een opmerking, een cijfer"],
            ]), "Une remarque is een opmerking; een cijfer is une note."),
            ("kader", "<strong>Een rapport lezen.</strong> <em>Bulletin du premier trimestre — "
                      "Français : 14/20. Mathématiques : 11/20. Sciences : 16/20. Éducation "
                      "physique : 15/20. Remarque du titulaire : élève attentif, mais doit "
                      "rendre ses devoirs à temps.</em><br>"
                      "<em>Doit rendre ses devoirs à temps</em>: moet zijn taken op tijd "
                      "inleveren. Attentief is hij juist wél."),
        ]),
        dict(kop="Beroepen", blokken=[
            ("kader", "<em>Dans ma famille, tout le monde travaille avec les mains. Mon père est "
                      "électricien, ma mère est infirmière et mon oncle est boulanger. Moi, je "
                      "voudrais devenir éducateur.</em>"),
            ("fig", tabel(["mannelijk", "vrouwelijk", "Nederlands"], [
                ["un vendeur", "une vendeuse", "verkoper"],
                ["un coiffeur", "une coiffeuse", "kapper"],
                ["un infirmier", "une infirmière", "verpleegkundige"],
                ["un boulanger", "une boulangère", "bakker"],
                ["un cuisinier", "une cuisinière", "kok"],
                ["un ouvrier", "une ouvrière", "arbeider"],
                ["un médecin", "un médecin", "dokter"],
            ]), "De meeste beroepsnamen veranderen mee met het geslacht; een paar blijven gelijk."),
            ("p", "Na <strong>être</strong> en <strong>devenir</strong> komt een beroepsnaam "
                  "<strong>zonder lidwoord</strong>: <em>ma mère est infirmière</em>, <em>je "
                  "voudrais devenir cuisinier</em>. En <em>être au chômage</em> betekent werkloos "
                  "zijn — dat is geen beroep."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["le travail, travailler", "het werk, werken"],
                ["un salaire", "een loon"],
                ["un contrat", "een contract"],
                ["un horaire", "een uurregeling"],
                ["un bureau", "een bureau of kantoor"],
            ]), "Le travail wordt in het meervoud les travaux."),
        ]),
        dict(kop="Stage en solliciteren", blokken=[
            ("kader", "<strong>Een verslag over een stage.</strong> <em>Mon stage s'est bien "
                      "passé. Le premier jour, j'avais peur de mal faire, mais l'équipe m'a "
                      "aidé. J'ai appris à répondre au téléphone et à classer des documents. Ce "
                      "que j'ai trouvé difficile, c'est de rester assis toute la journée. Je "
                      "recommencerais quand même.</em><br>"
                      "<em>Apprendre à</em> betekent leren om, <em>rester assis</em> blijven "
                      "zitten, en <em>quand même</em> toch."),
            ("kader", "<strong>Een zoekertje.</strong> <em>Magasin de sport cherche étudiant "
                      "pour les samedis. Tâches : accueillir les clients, ranger les rayons, "
                      "aider à la caisse. Expérience non exigée. Envoyez votre CV par mail avant "
                      "le 15 du mois.</em><br>"
                      "<em>Une tâche</em> is een taak, <em>un rayon</em> een rek, en "
                      "<em>expérience non exigée</em> betekent: ervaring is niet vereist."),
            ("p", "In je eigen <strong>sollicitatiemail</strong> zet je wie je bent en in welk "
                  "jaar je zit, wanneer je kan werken, en waarom je net die job wil. <em>Envoyer</em> "
                  "is sturen (niet invullen: dat is <em>remplir</em>)."),
        ]),
        dict(kop="Communicatie en multimedia", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un ordinateur, un écran", "een computer, een scherm"],
                ["une application", "een app"],
                ["un compte, un mot de passe", "een account, een wachtwoord"],
                ["se connecter / se déconnecter", "inloggen / uitloggen"],
                ["un mail, un courriel", "een mail"],
                ["un appel", "een telefoongesprek"],
                ["les courriers indésirables", "de ongewenste berichten, de spam"],
            ]), "Se connecter is wederkerend: je me connecte, tu te connectes."),
            ("kader", "<em>Pour vous inscrire, créez un compte avec votre adresse mail. Vous "
                      "recevrez un message avec un lien. Si le message n'arrive pas, regardez "
                      "dans les courriers indésirables. N'envoyez jamais votre mot de passe par "
                      "mail.</em><br>Dat laatste is geen taalregel maar een goede raad: je "
                      "wachtwoord stuur je nooit met een mail."),
        ]),
        dict(kop="Sport en ontspanning", blokken=[
            ("p", "Hier zit één vaste valkuil. Bij een <strong>sport of een spel</strong> hoort "
                  "<em>jouer à</em>: <em>jouer au basket</em>, <em>jouer au football</em>. Bij "
                  "een <strong>instrument</strong> hoort <em>jouer de</em>: <em>jouer du "
                  "piano</em>, <em>jouer de la guitare</em>. En voor veel sporten gebruik je "
                  "<em>faire de</em>: <em>faire du vélo</em>, <em>faire de la danse</em>. "
                  "<em>Jouer du tennis</em> bestaat niet."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un match, une équipe", "een wedstrijd, een ploeg"],
                ["un joueur, un entraîneur", "een speler, een trainer"],
                ["nager, courir", "zwemmen, lopen"],
                ["un film, une série, un livre", "een film, een reeks, een boek"],
                ["deux fois par semaine", "twee keer per week"],
            ]), "Na aimer komt een infinitief: j'aime nager, j'aime lire."),
        ]),
    ],
    onthoud=[
        "Je suis en quatrième année. Midi = 12 u 's middags, minuit = middernacht.",
        "Een beroepsnaam na être of devenir staat zonder lidwoord.",
        "Beroepen veranderen mee: un vendeur, une vendeuse.",
        "expérience non exigée = ervaring niet vereist; envoyer = sturen.",
        "mot de passe = wachtwoord; se connecter = inloggen.",
        "jouer au basket, jouer du piano, faire du vélo.",
        "deux fois par semaine = twee keer per week.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordvelden-tijd-weer-reizen-en-vervoer" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Woordvelden: tijd, weer, reizen en vervoer",
    onder="Wanneer en waar iets gebeurt: dagen, uren, het weer, de trein en de landen.",
    secties=[
        dict(kop="Dagen, maanden en seizoenen", blokken=[
            ("p", "De woordvelden van dit thema: <strong>dagen, maanden, seizoenen en "
                  "feesten</strong>; <strong>uur en plaats</strong>; het "
                  "<strong>weer</strong>; <strong>vakantie en reizen</strong>; "
                  "<strong>transportmiddelen</strong>; en <strong>landen en "
                  "nationaliteiten</strong>. Dit zijn de woorden waarmee een tekst zegt wanneer "
                  "en waar iets gebeurt."),
            ("fig", tabel(["dagen", "maanden"], [
                ["lundi, mardi, mercredi", "janvier, février, mars, avril"],
                ["jeudi, vendredi", "mai, juin, juillet, août"],
                ["samedi, dimanche", "septembre, octobre, novembre, décembre"],
            ]), "Allemaal met een kleine letter, anders dan in het Engels."),
            ("fig", svg.seizoenen(),
             "le printemps (maart), l'été (juni), l'automne, l'hiver: vier seizoenen, elk met hun lidwoord."),
            ("p", "<em>L'hiver</em> en <em>l'automne</em> krijgen <em>l'</em>, want ze beginnen "
                  "met een klinker of een stille h. En <em>les vacances</em> staat in het Frans "
                  "altijd in het <strong>meervoud</strong>: <em>les grandes vacances durent de "
                  "juillet à fin août</em>."),
            ("fig", tabel(["feest", "wanneer"], [
                ["Noël", "25 december"],
                ["le Nouvel An", "1 januari (le 1er janvier)"],
                ["la fête nationale (België)", "21 juli"],
                ["la fête nationale (Frankrijk)", "14 juli"],
                ["un anniversaire", "een verjaardag: bon anniversaire !"],
            ]), "Alleen de eerste van de maand krijgt een rangtelwoord: le 1er janvier, maar le 2 janvier."),
        ]),
        dict(kop="Het uur", blokken=[
            ("fig", svg.naast_elkaar([svg.klok(8, 45), svg.klok(15, 30)]),
             "Links: neuf heures moins le quart. Rechts: trois heures et demie."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["il est huit heures", "het is acht uur"],
                ["huit heures et quart", "kwart na acht"],
                ["huit heures et demie", "half negen"],
                ["neuf heures moins le quart", "kwart voor negen"],
                ["midi / minuit", "twaalf uur 's middags / middernacht"],
                ["dix-sept heures trente", "17.30 u, dus half zes"],
            ]), "Demie met een e, want une heure is vrouwelijk. In een agenda gebruikt het Frans de klok van 24 uur."),
            ("p", "Een <strong>agenda</strong> lezen is informatie selecteren: <em>Mardi : "
                  "dentiste à dix-sept heures trente</em>, <em>Jeudi : entraînement de "
                  "basket</em>, <em>Dimanche : rien</em>. Let op het verschil tussen "
                  "<em>mercredi</em> en <em>mercredi après-midi</em>: vrij in de namiddag is "
                  "niet vrij de hele dag."),
        ]),
        dict(kop="Waar iets ligt", blokken=[
            ("fig", svg.plattegrond(),
             "Dezelfde woorden als in een uitleg over de weg: devant, derrière, en face de, entre."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["devant / derrière", "voor / achter"],
                ["en face de", "tegenover"],
                ["entre … et …", "tussen … en …"],
                ["à côté de", "naast"],
                ["sur / sous", "op / onder"],
                ["tout droit", "rechtdoor"],
                ["au bout de la rue", "op het einde van de straat"],
            ]), "Tout droit is rechtdoor, à droite is naar rechts: één letter, een ander antwoord."),
            ("p", "<em>Pendant</em> hoort niet in die rij: dat betekent tijdens en zegt "
                  "<strong>wanneer</strong>, niet waar."),
        ]),
        dict(kop="Het weer", blokken=[
            ("kader", "<strong>Een weerbericht.</strong> <em>Demain, le temps restera gris dans "
                      "tout le pays. Il pleuvra le matin en Wallonie, avec un vent assez fort "
                      "venant de l'ouest. Les températures ne dépasseront pas douze degrés. En "
                      "fin de journée, quelques éclaircies à la côte.</em><br>"
                      "Een weerbericht staat bijna helemaal in de <strong>futur simple</strong>: "
                      "<em>restera</em>, <em>pleuvra</em>, <em>dépasseront</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["il fait beau / mauvais", "het is mooi / slecht weer"],
                ["il fait chaud / froid", "het is warm / koud"],
                ["il pleut, il neige", "het regent, het sneeuwt"],
                ["il y a du vent", "het waait"],
                ["une éclaircie", "een opklaring"],
                ["une température, un degré", "een temperatuur, een graad"],
            ]), "Pleuvoir en neiger bestaan alleen als il pleut en il neige: onpersoonlijke werkwoorden."),
            ("fig", svg.windroos(),
             "le nord, le sud, l'est, l'ouest: de wind komt venant de l'ouest, uit het westen."),
        ]),
        dict(kop="Reizen en vervoer", blokken=[
            ("kader", "<strong>Een bericht in de stationshal.</strong> <em>Le train de 14 h 05 "
                      "vers Namur a un retard de vingt minutes. Les voyageurs pour Charleroi "
                      "doivent changer à Ottignies. Le train suivant part à 14 h 35, voie "
                      "3.</em><br><em>Un retard</em> is een vertraging, <em>changer</em> is hier "
                      "overstappen, en <em>une voie</em> is een spoor."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["le train, le bus, le tram", "de trein, de bus, de tram"],
                ["l'avion, le bateau", "het vliegtuig, de boot"],
                ["la gare, le quai, la voie", "het station, het perron, het spoor"],
                ["un retard, changer", "een vertraging, overstappen"],
                ["un billet", "een ticket"],
            ]), "Je zegt prendre le train en prendre le bus, nooit aller le bus."),
            ("p", "Het voorzetsel hangt af van het vervoermiddel: <strong>en</strong> als je "
                  "erin zit (<em>en train</em>, <em>en voiture</em>, <em>en bus</em>, <em>en "
                  "avion</em>), <strong>à</strong> als dat niet zo is (<em>à vélo</em>, <em>à "
                  "pied</em>)."),
            ("kader", "<strong>Een reisverslag.</strong> <em>L'été dernier, nous sommes partis "
                      "dix jours en Espagne. Nous avons pris l'avion jusqu'à Barcelone, puis le "
                      "train jusqu'à la côte. L'hôtel était simple mais propre, et la mer était à "
                      "deux cents mètres.</em><br><em>Jusqu'à</em> betekent tot aan."),
        ]),
        dict(kop="Landen en nationaliteiten", blokken=[
            ("fig", tabel(["land", "nationaliteit", "waar je woont"], [
                ["la Belgique", "belge", "en Belgique"],
                ["la France", "français, française", "en France"],
                ["l'Italie", "italien, italienne", "en Italie"],
                ["l'Allemagne", "allemand, allemande", "en Allemagne"],
                ["le Portugal", "portugais, portugaise", "au Portugal"],
                ["le Maroc", "marocain, marocaine", "au Maroc"],
                ["les Pays-Bas", "néerlandais, néerlandaise", "aux Pays-Bas"],
            ]), "Een vrouwelijk land krijgt en, een mannelijk au, een meervoud aux. Bij een stad: à Paris."),
            ("p", "Een <strong>nationaliteit</strong> schrijf je met een <strong>kleine "
                  "letter</strong>: <em>je suis belge</em>, <em>Lena est allemande</em>. Het land "
                  "zelf krijgt wel een hoofdletter. En <em>venir de</em> wordt <em>venir d'</em> "
                  "voor een klinker: <em>Mateo vient d'Italie</em>."),
        ]),
    ],
    onthoud=[
        "Dagen, maanden en nationaliteiten: kleine letter. Landen: hoofdletter.",
        "les vacances staat altijd in het meervoud.",
        "et quart, et demie, moins le quart. Midi is 12 u, minuit middernacht.",
        "tout droit = rechtdoor, à droite = naar rechts, en face de = tegenover.",
        "il pleut, il neige, il fait froid: onpersoonlijke vormen.",
        "en train, en voiture, maar à vélo en à pied.",
        "en France, au Portugal, aux Pays-Bas, à Paris.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["zelfstandige-naamwoorden-lidwoorden-en-determinanten" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Zelfstandige naamwoorden, lidwoorden en determinanten",
    onder="Mannelijk of vrouwelijk, enkelvoud of meervoud, en welk woordje er dan voor komt.",
    secties=[
        dict(kop="Mannelijk, vrouwelijk, enkelvoud, meervoud", blokken=[
            ("p", "Elk Frans zelfstandig naamwoord is <strong>mannelijk of vrouwelijk</strong>, "
                  "ook een tafel of een trein. Je kan dat niet aan het woord zelf zien, dus leer "
                  "een naamwoord <strong>altijd met zijn lidwoord</strong>: <em>la table</em>, "
                  "<em>le train</em>. Dat ene woordje spaart je later tien fouten uit, want het "
                  "bijvoeglijk naamwoord en het voltooid deelwoord volgen het."),
            ("fig", tabel(["enkelvoud", "meervoud", "regel"], [
                ["un ami", "des amis", "gewoon een s erbij (die je niet hoort)"],
                ["un journal", "des journaux", "woorden op -al krijgen -aux"],
                ["un gâteau", "des gâteaux", "woorden op -eau krijgen een x"],
                ["un œil", "les yeux", "helemaal onregelmatig"],
            ]), "Un animal wordt des animaux, un bureau wordt des bureaux."),
            ("p", "De meervouds-s <strong>hoor je niet</strong>. Of er één of meer zijn, hoor je "
                  "dus aan het lidwoord: <em>le livre</em> tegenover <em>les livres</em>, "
                  "<em>un ami</em> tegenover <em>des amis</em>."),
        ]),
        dict(kop="Bepaald, onbepaald en samengetrokken", blokken=[
            ("fig", tabel(["soort", "vormen", "wanneer"], [
                ["bepaald (défini)", "le, la, l', les", "een bepaald iets, of iets in het algemeen"],
                ["onbepaald (indéfini)", "un, une, des", "om het even welk, één exemplaar"],
                ["samengetrokken (contracté)", "au, aux, du, des", "à of de plus le of les"],
                ["deelaanduidend (partitif)", "du, de la, de l', des", "een onbepaalde hoeveelheid"],
            ]), "Vier soorten lidwoorden. De vormen du en des staan in twee rijen: de betekenis verschilt."),
            ("p", "<strong>Samentrekken</strong> gebeurt alleen bij <em>le</em> en <em>les</em>: "
                  "à + le = <strong>au</strong>, à + les = <strong>aux</strong>, de + le = "
                  "<strong>du</strong>, de + les = <strong>des</strong>. Bij <em>la</em> en "
                  "<em>l'</em> blijft het gewoon staan: <em>à la maison</em>, <em>à l'école</em>. "
                  "<em>À le parc</em> bestaat dus niet: dat wordt <em>au parc</em>."),
            ("p", "Voor een <strong>klinker of een stille h</strong> worden <em>le</em> en "
                  "<em>la</em> samen <em>l'</em>: <em>l'ami</em>, <em>l'école</em>, "
                  "<em>l'heure</em>."),
        ]),
        dict(kop="Een deel van iets: du, de la, des", blokken=[
            ("p", "Het <strong>deelaanduidend lidwoord</strong> zegt dat je over een "
                  "<strong>onbepaalde hoeveelheid</strong> spreekt: <em>du café</em> (wat "
                  "koffie), <em>de la soupe</em>, <em>de l'eau</em>, <em>des légumes</em>. Het "
                  "verandert de betekenis van je zin: <em>j'aime le chocolat</em> is chocolade in "
                  "het algemeen, <em>je mange du chocolat</em> is er een beetje van."),
            ("fig", tabel(["voor een …", "vorm", "voorbeeld"], [
                ["mannelijk woord", "du", "du pain, du café"],
                ["vrouwelijk woord", "de la", "de la soupe, de la viande"],
                ["klinker of stille h", "de l'", "de l'eau, de l'huile"],
                ["meervoud", "des", "des pommes, des frites"],
            ]), "Vier vormen van hetzelfde lidwoord."),
            ("kader", "<strong>Twee plaatsen waar het de wordt.</strong> Na een "
                      "<strong>hoeveelheid</strong>: <em>un kilo <strong>de</strong> pommes</em>, "
                      "<em>beaucoup <strong>de</strong> monde</em>, <em>un peu "
                      "<strong>de</strong> sel</em>, <em>trop <strong>de</strong> bruit</em>, "
                      "<em>assez <strong>de</strong> places</em>, <em>un litre "
                      "<strong>d'</strong>eau</em>. En na een <strong>ontkenning</strong>: "
                      "<em>je ne mange pas <strong>de</strong> pain</em>, <em>il n'y a pas "
                      "<strong>de</strong> problème</em>, <em>pas <strong>d'</strong>amis</em>."),
            ("p", "Let op: na een ontkenning blijft het <strong>bepaald</strong> lidwoord wel "
                  "staan. <em>Je n'aime pas le café</em> — want hier gaat het over koffie in het "
                  "algemeen, niet over een hoeveelheid."),
        ]),
        dict(kop="Aanwijzen, bezitten, vragen", blokken=[
            ("fig", tabel(["soort", "mannelijk", "vrouwelijk", "meervoud"], [
                ["aanwijzend", "ce (cet voor klinker)", "cette", "ces"],
                ["bezittelijk (ik)", "mon", "ma (mon voor klinker)", "mes"],
                ["bezittelijk (jij)", "ton", "ta", "tes"],
                ["bezittelijk (hij/zij)", "son", "sa", "ses"],
                ["bezittelijk (zij, meervoud)", "leur", "leur", "leurs"],
                ["vragend", "quel", "quelle", "quels / quelles"],
            ]), "Ces is de enige meervoudsvorm van het aanwijzend woord: voor allebei de geslachten."),
            ("p", "<em>Ce</em> wordt <em>cet</em> voor een klinker of een stille h: <em>cet "
                  "homme</em>, <em>cet ami</em>, <em>cet hôtel</em> — dan hoor je de t."),
            ("kader", "<strong>Het bezittelijk woord volgt het bezit, niet de bezitter.</strong> "
                      "Een jongen én een meisje zeggen <em>ma voiture</em>, want <em>voiture</em> "
                      "is vrouwelijk. En <em>son frère</em> / <em>sa sœur</em> kunnen allebei "
                      "'zijn' of 'haar' betekenen: in het Engels worden dat <em>his</em> en "
                      "<em>her</em>, in het Frans niet. Wie de bezitter is, moet uit de rest van "
                      "de tekst blijken."),
            ("p", "Ook hier speelt de klinker: <em>ma amie</em> wordt <em>mon amie</em>, "
                  "<em>mon école</em>, <em>mon histoire</em> — dat klinkt vlotter."),
            ("p", "Het <strong>vragend</strong> woord heeft vier vormen en past zich aan, net "
                  "als een bijvoeglijk naamwoord: <em>Quelle heure est-il ?</em>, <em>Quel est "
                  "ton numéro de téléphone ?</em>, <em>Quelles couleurs ?</em>"),
        ]),
        dict(kop="De telwoorden", blokken=[
            ("fig", tabel(["getal", "Frans", "let op"], [
                ["11 tot 16", "onze, douze, treize, quatorze, quinze, seize", "zes aparte woorden"],
                ["70", "septante (B) / soixante-dix (F)", "allebei juist Frans"],
                ["80", "quatre-vingts", "met s, maar quatre-vingt-deux zonder"],
                ["90", "nonante (B) / quatre-vingt-dix (F)", ""],
                ["100", "cent", "zonder lidwoord; deux cents met s"],
            ]), "In België hoor je septante en nonante, in Frankrijk soixante-dix en quatre-vingt-dix."),
            ("p", "<strong>Rangtelwoorden</strong> zeggen welke plaats in een rij: "
                  "<em>premier</em> (eerste), <em>deuxième</em>, <em>troisième</em>, "
                  "<em>dernier</em> (laatste). Op <em>premier</em> na krijgen ze allemaal "
                  "<strong>-ième</strong>. En in een datum gebruik je er maar één: <em>le premier "
                  "mai</em>, maar <em>le deux mai</em> en <em>le trois mai</em>."),
        ]),
    ],
    onthoud=[
        "Leer een naamwoord met zijn lidwoord: la table, le train.",
        "à + le = au, à + les = aux, de + le = du, de + les = des. À la blijft à la.",
        "du, de la, de l', des = een onbepaalde hoeveelheid.",
        "Na een hoeveelheid en na een ontkenning wordt het de: un kilo de, pas de.",
        "ce / cet / cette / ces, en mon / ma / mes volgen het bezit, niet de bezitter.",
        "quel, quelle, quels, quelles: vier vormen van hetzelfde vraagwoord.",
        "quinze (15), quatre-vingts (80), cent (100), troisième, dernier.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["voornaamwoorden-sujet-cod-coi-en-de-wederkerende" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Voornaamwoorden: sujet, COD, COI en de wederkerende",
    onder="Wie doet het, wat ondergaat het, aan wie gebeurt het — en waar dat woordje dan staat.",
    secties=[
        dict(kop="Waarom dit bij lezen én bij schrijven telt", blokken=[
            ("p", "Een voornaamwoord <strong>verwijst</strong> naar een persoon, een voorwerp, "
                  "een begrip of een plaats uit een vorige zin. Als je niet weet waarnaar het "
                  "verwijst, verlies je de draad van de tekst. En als je zelf schrijft, gebruik "
                  "je ze om niet elke keer hetzelfde woord te moeten herhalen."),
            ("fig", svg.voornaamwoordplaats(),
             "Het grote verschil met het Nederlands: in het Frans staat het voorwerp vóór het werkwoord."),
        ]),
        dict(kop="Het onderwerp", blokken=[
            ("fig", tabel(["wie", "vorm", "let op"], [
                ["ik", "je (j' voor een klinker)", "j'aime, j'ai"],
                ["jij", "tu", "bij een vriend of klasgenoot"],
                ["hij / zij", "il / elle", ""],
                ["men, de mensen", "on", "krijgt dezelfde vorm als il: on parle"],
                ["wij", "nous", "iemand én ik: Marie et moi = nous"],
                ["jullie / u", "vous", "Marie et toi = vous; ook de hoffelijke vorm"],
                ["zij (meervoud)", "ils / elles", "één mannelijk woord erbij = ils"],
            ]), "Mon frère et ma sœur worden ils; deux filles worden elles."),
            ("p", "Het onderwerp valt in het Frans <strong>nooit</strong> weg: je zegt <em>je "
                  "parle</em>, nooit <em>parle</em> alleen. Alleen in de <em>impératif</em> "
                  "gebeurt dat: <em>parle !</em>"),
            ("p", "En <em>moi</em> is géén onderwerp. Dat staat alleen, of na een voorzetsel: "
                  "<em>avec moi</em>, <em>chez moi</em>, <em>plus grand que moi</em>. <em>Moi "
                  "parle</em> bestaat niet."),
        ]),
        dict(kop="COD en COI: het verschil", blokken=[
            ("fig", svg.zinsdelen([
                ("Je", "onderwerp", svg.DIM),
                ("donne", "persoonsvorm", svg.DARK),
                ("mon numéro", "COD", svg.AMBER),
                ("à Lila", "COI", svg.FOREST),
            ]), "Eén zin, vier delen. Wat geef ik? Mon numéro. Aan wie? À Lila."),
            ("p", "Het <strong>lijdend voorwerp (COD)</strong> antwoordt op <em>wie of wat "
                  "ondergaat de handeling?</em> en staat <strong>zonder voorzetsel</strong>: "
                  "<em>je regarde la télévision</em>, <em>je lis un livre</em>."),
            ("p", "Het <strong>meewerkend voorwerp (COI)</strong> antwoordt op <em>aan wie?</em> "
                  "en staat met <strong>à</strong>: <em>j'écris à ma grand-mère</em>, <em>il "
                  "parle à ses parents</em>. Werkwoorden die dat vragen: <em>parler à</em>, "
                  "<em>écrire à</em>, <em>téléphoner à</em>, <em>répondre à</em>, <em>demander "
                  "à</em>, <em>donner à</em>."),
            ("fig", tabel(["wie", "COD", "COI"], [
                ["mij / jou", "me, te", "me, te"],
                ["hem / haar", "le, la (l')", "lui"],
                ["ons / jullie", "nous, vous", "nous, vous"],
                ["hen", "les", "leur"],
            ]), "Alleen in de derde persoon zie je het verschil: le/la/les tegenover lui/leur."),
            ("p", "Dus: <em>Je regarde la télévision</em> wordt <em>je <strong>la</strong> "
                  "regarde</em>; <em>tu connais mon frère ?</em> wordt <em>tu <strong>le</strong> "
                  "connais ?</em>; <em>j'écris à ma grand-mère</em> wordt <em>je "
                  "<strong>lui</strong> écris</em>; <em>il parle à ses parents</em> wordt <em>il "
                  "<strong>leur</strong> parle</em>. <em>Leur</em> krijgt hier geen s, ook al "
                  "gaat het over meerdere mensen."),
            ("p", "<em>Lui</em> kan 'aan hem' én 'aan haar' betekenen; dat moet uit de rest van "
                  "de tekst blijken. En een zin kan allebei hebben: <em>je donne le livre à "
                  "Lila</em> wordt <em>je le lui donne</em>."),
        ]),
        dict(kop="Waar het voornaamwoord staat", blokken=[
            ("fig", tabel(["soort zin", "plaats", "voorbeeld"], [
                ["gewone zin", "vóór het vervoegde werkwoord", "je la vois, il me parle"],
                ["ontkenning", "binnen de ne … pas, bij het werkwoord", "je ne le connais pas"],
                ["met een infinitief", "vóór die infinitief", "tu peux m'aider ?"],
                ["bevel zonder ontkenning", "erachter, met een koppelteken", "regarde-moi, donne-le-moi"],
                ["bevel met ontkenning", "weer ervoor", "ne me regarde pas"],
            ]), "In een bevel wordt me moi: appelle-moi, lève-toi."),
            ("p", "Bij <strong>twee voornaamwoorden samen</strong> komt in de derde persoon het "
                  "COD eerst: <em>je <strong>le lui</strong> donne</em>. Bij <em>me, te, nous, "
                  "vous</em> is het omgekeerd: <em>il <strong>me le</strong> donne</em>."),
        ]),
        dict(kop="De wederkerende werkwoorden", blokken=[
            ("p", "Een <strong>wederkerend</strong> werkwoord heeft een <em>se</em> bij zich in "
                  "de infinitief: <em>se lever</em>, <em>se laver</em>, <em>s'appeler</em>, "
                  "<em>se doucher</em>, <em>se sentir</em>. Dat woordje verandert mee met de "
                  "persoon."),
            ("fig", svg.persoonsvormen([
                ("je|tu|il, elle, on", "me lave, te laves, se lave", svg.FOREST),
                ("nous|vous|ils, elles", "nous lavons, vous lavez, se lavent", svg.AMBER),
            ]), "In de wij- en jullie-vorm staat het woordje twee keer: nous nous lavons."),
            ("p", "Het zegt dat de handeling op het onderwerp zelf terugslaat: <em>il lave la "
                  "voiture</em> (hij wast iets anders) tegenover <em>il se lave</em> (hij wast "
                  "zich). Hetzelfde werkwoord kan dus allebei."),
            ("p", "Het kan ook <strong>elkaar</strong> betekenen: <em>on se voit demain</em> (we "
                  "zien elkaar morgen), <em>ils se parlent</em>. En voor een klinker wordt "
                  "<em>te</em> <em>t'</em>: <em>Comment tu t'appelles ?</em>"),
        ]),
        dict(kop="Y en en", blokken=[
            ("fig", tabel(["woord", "vervangt", "voorbeeld"], [
                ["y", "een plaats met à, dans of chez", "Tu vas à la poste ? → Tu y vas ?"],
                ["en", "een onbepaalde hoeveelheid of een getal", "Tu as des frères ? → J'en ai deux."],
            ]), "Allebei staan ze, net als de andere voornaamwoorden, vóór het werkwoord."),
            ("p", "<em>J'y vais demain</em> betekent: ik ga er morgen heen. <em>Il y est</em>: "
                  "hij is daar. Let op de samentrekking: <em>je y vais</em> bestaat niet, het "
                  "wordt <em>j'y vais</em>, en <em>j'en ai deux</em>."),
            ("p", "Twee vaste uitdrukkingen om te onthouden: <em>j'en ai assez</em> (ik heb er "
                  "genoeg van) en <em>on y va !</em> (we gaan!)."),
        ]),
    ],
    onthoud=[
        "In het Frans staat het voorwerp vóór het werkwoord: je la vois.",
        "COD = zonder voorzetsel (le, la, les). COI = met à (lui, leur).",
        "leur krijgt geen s als voornaamwoord: il leur parle.",
        "In een bevel komt het erachter met een streepje: donne-le-moi.",
        "Een wederkerend werkwoord verandert mee: je me lève, nous nous levons.",
        "y = een plaats, en = een hoeveelheid. j'y vais, j'en ai deux.",
        "Een voornaamwoord verwijst altijd terug, nooit vooruit.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Bijvoeglijke naamwoorden, bijwoorden en de trappen",
    onder="Vorm, plaats en vergelijking, plus de bijwoorden en de voorzetsels.",
    secties=[
        dict(kop="De vorm: mee met het naamwoord", blokken=[
            ("p", "Je gebruikt bijvoeglijke naamwoorden om je tekst <strong>rijker</strong> te "
                  "maken. Daarvoor moet je twee dingen in orde hebben: de vorm en de plaats."),
            ("fig", tabel(["mannelijk", "vrouwelijk", "regel"], [
                ["petit", "petite", "gewoon een e erbij"],
                ["difficile", "difficile", "eindigt al op een e: niets verandert"],
                ["heureux", "heureuse", "woorden op -eux worden -euse"],
                ["sportif", "sportive", "woorden op -if worden -ive"],
                ["blanc", "blanche", "onregelmatig"],
                ["bon / beau / vieux", "bonne / belle / vieille", "onregelmatig"],
            ]), "In het meervoud komt er nog een s bij: petites, heureuses, sportives."),
            ("p", "Die uitgangen <strong>hoor</strong> je soms wel (<em>petit</em> tegenover "
                  "<em>petite</em>) en soms niet (<em>jeune</em>, <em>difficiles</em>). "
                  "Schrijven moet je ze altijd."),
        ]),
        dict(kop="De plaats: meestal erachter", blokken=[
            ("fig", svg.woordvolgorde([
                ("lidwoord", "une", svg.DIM),
                ("naamwoord", "voiture", svg.DARK),
                ("bijvoeglijk nw.", "rouge", svg.AMBER),
            ]), "In het Frans komt het bijvoeglijk naamwoord meestal ná het naamwoord."),
            ("p", "Dat is net omgekeerd aan het Nederlands: <em>un film intéressant</em>, "
                  "<em>un livre intéressant</em>, <em>une voiture rouge</em>. <em>Une rouge "
                  "voiture</em> bestaat niet, en een <strong>kleur</strong> staat altijd "
                  "erachter."),
            ("p", "Eén kleine groep gaat wél <strong>vooraan</strong>: <em>grand</em>, "
                  "<em>petit</em>, <em>bon</em>, <em>mauvais</em>, <em>beau</em>, <em>joli</em>, "
                  "<em>jeune</em>, <em>vieux</em>, <em>nouveau</em>. Vandaar <em>c'est une belle "
                  "journée</em>, met <em>belle</em> vooraan én in de vrouwelijke vorm."),
        ]),
        dict(kop="Vergelijken: de drie trappen", blokken=[
            ("fig", tabel(["wat je zegt", "Frans", "voorbeeld"], [
                ["meer dan", "plus … que", "plus grand que moi"],
                ["minder dan", "moins … que", "moins cher que l'autre"],
                ["even als", "aussi … que", "aussi grande que son frère"],
                ["de meeste / de minste", "le, la, les plus / moins … de", "la plus grande maison de la rue"],
            ]), "In een vergelijking hoort que; bij de overtreffende trap hoort de."),
            ("p", "Het bijvoeglijk naamwoord blijft ook in een vergelijking <strong>meegaan</strong> "
                  "met het woord waarbij het hoort: <em>ma sœur est plus âgé<strong>e</strong> que "
                  "moi</em>. En een lang bijvoeglijk naamwoord verandert in het Frans niet van "
                  "vorm zoals bij ons: het blijft <em>plus intéressant que</em>."),
            ("kader", "<strong>Twee onregelmatige.</strong> <em>bon</em> → <em>meilleur</em> → "
                      "<em>le meilleur</em> (goed, beter, de beste). <em>Plus bon</em> bestaat "
                      "niet. Bij het bijwoord gaat het net zo: <em>bien</em> → <em>mieux</em> → "
                      "<em>le mieux</em>."),
        ]),
        dict(kop="De bijwoorden", blokken=[
            ("p", "Een <strong>bijwoord</strong> hoort bij een werkwoord en verandert "
                  "<strong>nooit</strong> van vorm: <em>elle parle lentement</em>, <em>ils "
                  "parlent lentement</em> — geen e en geen s. Dat is het grote verschil met een "
                  "bijvoeglijk naamwoord: <em>elle est rapide</em> zegt iets over haar, <em>elle "
                  "parle rapidement</em> over hoe ze spreekt."),
            ("p", "Je maakt er een van een bijvoeglijk naamwoord door "
                  "<strong>-ment</strong> achter de <strong>vrouwelijke</strong> vorm te zetten: "
                  "lent → lente → <em>lentement</em>; heureux → heureuse → "
                  "<em>heureusement</em>; normal → normale → <em>normalement</em>; facile → "
                  "<em>facilement</em>; rapide → <em>rapidement</em>."),
            ("fig", tabel(["hoe vaak", "Frans"], [
                ["altijd", "toujours"],
                ["vaak", "souvent"],
                ["soms", "parfois, quelquefois"],
                ["zelden", "rarement"],
                ["nooit", "ne … jamais"],
                ["nog niet", "pas encore"],
            ]), "Ne … jamais staat in twee stukken rond het werkwoord, net als ne … pas."),
            ("p", "Zo'n bijwoord staat meestal <strong>achter</strong> het vervoegde werkwoord: "
                  "<em>je vais souvent à la piscine</em>. In de passé composé komt het tussen "
                  "het hulpwerkwoord en het deelwoord: <em>j'ai souvent mangé là</em>."),
            ("p", "<em>Beaucoup</em> is ook een bijwoord, van hoeveelheid: <em>j'ai beaucoup "
                  "travaillé</em>. Voor een naamwoord komt er <em>de</em> bij: <em>beaucoup de "
                  "travail</em>."),
        ]),
        dict(kop="De voorzetsels", blokken=[
            ("fig", tabel(["Frans", "wanneer", "voorbeeld"], [
                ["à", "bij een stad, en bij te voet of per fiets", "à Bruxelles, à pied, à vélo"],
                ["en", "bij een vrouwelijk land en bij een vervoermiddel waar je in zit", "en France, en train, en voiture"],
                ["au / aux", "bij een mannelijk land of een meervoud", "au Portugal, aux Pays-Bas"],
                ["chez", "bij een persoon of een beroep", "chez Lila, chez le médecin"],
                ["depuis", "sinds — met een présent erbij!", "j'habite ici depuis trois ans"],
                ["pendant", "tijdens", "pendant les vacances"],
                ["avant / après", "voor / na", "avant midi, après l'école"],
                ["avec / sans", "met / zonder", "avec sucre, sans sucre"],
                ["sur / sous", "op / onder", "sur la table, sous la table"],
            ]), "Depuis staat in het Frans bij een tegenwoordige tijd, waar wij 'ik woon hier al' zeggen."),
            ("p", "<em>De</em> wordt <em>d'</em> voor een klinker of een stille h: <em>un verre "
                  "d'eau</em>, <em>beaucoup d'amis</em>, <em>pas d'histoire</em>."),
        ]),
    ],
    onthoud=[
        "Het bijvoeglijk naamwoord gaat mee met het naamwoord: une petite maison, des exercices difficiles.",
        "Het staat meestal erachter; grand, petit, bon, beau en jeune gaan vooraan.",
        "Een kleur staat altijd erachter: une voiture rouge.",
        "plus / moins / aussi … que. Overtreffend: le plus … de.",
        "bon → meilleur → le meilleur. Plus bon bestaat niet.",
        "Een bijwoord verandert nooit van vorm; -ment komt achter de vrouwelijke vorm.",
        "en France, au Portugal, à Paris, chez le médecin, en train maar à vélo.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["present-imperatif-en-de-wederkerende-werkwoorden" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Présent, impératif en de wederkerende werkwoorden",
    onder="De tegenwoordige tijd, het bevel, de infinitief, en de werkwoorden zonder persoon.",
    secties=[
        dict(kop="Drie vormen die bijna gelijk klinken", blokken=[
            ("kader", "<strong>Dit is de belangrijkste regel van het hele vak.</strong> Je moet "
                      "het verschil kennen tussen een <strong>infinitief</strong> "
                      "(<em>aller</em>), een <strong>persoonsvorm</strong> (<em>allez</em>) en "
                      "een <strong>voltooid deelwoord</strong> (<em>allé</em>). Ze klinken bijna "
                      "gelijk, maar ze doen iets anders in de zin. Wie dat verschil kent, leest "
                      "een Franse zin juist én schrijft ze juist."),
            ("fig", tabel(["vorm", "voorbeeld", "wat ze doet"], [
                ["infinitief", "aller, parler, finir", "staat na een ander werkwoord of in een woordenboek"],
                ["persoonsvorm", "vous allez, je parle", "is vervoegd en hoort bij een onderwerp"],
                ["voltooid deelwoord", "allé, parlé, fini", "staat bij avoir of être"],
            ]), "parler, parlez en parlé klinken hetzelfde en schrijf je anders."),
        ]),
        dict(kop="De présent: de drie regelmatige groepen", blokken=[
            ("fig", tabel(["-er: parler", "-ir: finir", "-re: vendre"], [
                ["je parle", "je finis", "je vends"],
                ["tu parles", "tu finis", "tu vends"],
                ["il parle", "il finit", "il vend"],
                ["nous parlons", "nous finissons", "nous vendons"],
                ["vous parlez", "vous finissez", "vous vendez"],
                ["ils parlent", "ils finissent", "ils vendent"],
            ]), "Let bij finir op de dubbele s in het meervoud: finissons, finissez, finissent."),
            ("p", "Bij een werkwoord op <strong>-er</strong> klinken <em>je parle</em>, <em>tu "
                  "parles</em>, <em>il parle</em> en <em>ils parlent</em> <strong>allemaal "
                  "hetzelfde</strong>. Vier vormen, één klank: het verschil zie je alleen in het "
                  "schrift. Daarom moet je die uitgangen kennen, ook al hoor je ze niet."),
            ("p", "Niet alle werkwoorden op -ir doen het zoals <em>finir</em>: <em>venir</em>, "
                  "<em>partir</em>, <em>sortir</em> en <em>dormir</em> gaan hun eigen weg. "
                  "<em>Finir</em> en <em>choisir</em> volgen wel hetzelfde patroon."),
        ]),
        dict(kop="De onregelmatige die je echt nodig hebt", blokken=[
            ("fig", tabel(["werkwoord", "je", "tu", "il", "nous", "vous", "ils"], [
                ["être", "suis", "es", "est", "sommes", "êtes", "sont"],
                ["avoir", "ai", "as", "a", "avons", "avez", "ont"],
                ["aller", "vais", "vas", "va", "allons", "allez", "vont"],
                ["faire", "fais", "fais", "fait", "faisons", "faites", "font"],
                ["prendre", "prends", "prends", "prend", "prenons", "prenez", "prennent"],
                ["pouvoir", "peux", "peux", "peut", "pouvons", "pouvez", "peuvent"],
                ["vouloir", "veux", "veux", "veut", "voulons", "voulez", "veulent"],
                ["devoir", "dois", "dois", "doit", "devons", "devez", "doivent"],
                ["venir", "viens", "viens", "vient", "venons", "venez", "viennent"],
                ["savoir", "sais", "sais", "sait", "savons", "savez", "savent"],
            ]), "Verwar ils ont (avoir) niet met ils sont (être). Vous faites en vous êtes eindigen niet op -ez."),
            ("p", "Twee dingen waar het Frans <strong>avoir</strong> gebruikt en wij 'zijn': "
                  "<em>j'ai quinze ans</em> (leeftijd) en <em>j'ai faim</em>, <em>j'ai froid</em>, "
                  "<em>j'ai peur</em> (gevoelens en behoeften)."),
        ]),
        dict(kop="De impératif: een bevel, een raad, een instructie", blokken=[
            ("fig", tabel(["vorm", "parler", "finir", "être / avoir"], [
                ["tu", "parle ! (zonder s)", "finis !", "sois ! / aie !"],
                ["nous", "parlons !", "finissons !", "soyons ! / ayons !"],
                ["vous", "parlez !", "finissez !", "soyez ! / ayez !"],
            ]), "Drie vormen, en het onderwerp valt weg. Bij -er verliest de tu-vorm zijn s."),
            ("p", "Een bevel geven aan 'hij' kan niet: er zijn alleen deze drie. De "
                  "<strong>nous-vorm</strong> betekent 'laten we': <em>allons !</em>"),
            ("p", "Je komt de impératif overal tegen in een <strong>prescriptieve tekst</strong>: "
                  "<em>coupez deux oignons</em>, <em>ajoutez le riz</em>, <em>n'utilisez pas de "
                  "sèche-linge</em>, <em>inscris-toi avant le 30 septembre</em>. Daarom staat er "
                  "in een recept <em>ajoutez le riz</em> en niet <em>vous ajoutez le riz</em>."),
            ("p", "Bij een <strong>wederkerend</strong> werkwoord komt het voornaamwoord "
                  "erachter met een koppelteken, en wordt <em>te</em> <em>toi</em>: <em>lève-toi "
                  "!</em>, <em>assieds-toi !</em> Ook <em>me</em> wordt <em>moi</em>: "
                  "<em>appelle-moi !</em>, <em>regarde-moi !</em>"),
        ]),
        dict(kop="De infinitief na een ander werkwoord", blokken=[
            ("p", "Na <em>aimer</em>, <em>vouloir</em>, <em>pouvoir</em>, <em>devoir</em>, "
                  "<em>aller</em> en <em>il faut</em> komt een <strong>infinitief</strong>, geen "
                  "tweede persoonsvorm: <em>j'aime jouer au basket</em>, <em>je veux partir</em>, "
                  "<em>tu peux venir ?</em>, <em>je dois travailler</em>, <em>je vais manger</em>, "
                  "<em>il faut partir</em>."),
            ("p", "<em>Je veux je mange</em> bestaat dus niet. En het voornaamwoord hoort bij de "
                  "infinitief die het aanvult: <em>tu peux <strong>m'</strong>aider ?</em>"),
        ]),
        dict(kop="De onpersoonlijke werkwoorden", blokken=[
            ("p", "Een paar werkwoorden bestaan <strong>alleen in de derde persoon "
                  "enkelvoud</strong>, want er is geen echte persoon die de handeling doet. "
                  "<em>Nous pleuvons</em> bestaat niet."),
            ("fig", tabel(["vorm", "betekenis"], [
                ["il pleut", "het regent (pleuvoir)"],
                ["il neige", "het sneeuwt (neiger)"],
                ["il faut", "het is nodig, men moet (falloir)"],
                ["il y a", "er is, er zijn"],
                ["il fait beau / froid", "het is mooi / koud weer"],
            ]), "Die il verwijst naar niets of niemand; hij houdt alleen de plaats van het onderwerp bezet."),
            ("p", "<em>Il y a</em> blijft hetzelfde in het enkelvoud en het meervoud: <em>il y a "
                  "un problème</em>, <em>il y a trois chaises</em>. En over het weer zegt het "
                  "Frans <em>il fait</em>: <em>il fait beau aujourd'hui</em>, <em>il fait vingt "
                  "degrés</em>."),
        ]),
    ],
    onthoud=[
        "aller (infinitief), allez (persoonsvorm), allé (deelwoord): dezelfde klank, ander werk.",
        "-er: e, es, e, ons, ez, ent. -ir: is, is, it, issons, issez, issent.",
        "être, avoir, aller, faire, prendre, pouvoir, vouloir en venir ken je uit het hoofd.",
        "j'ai quinze ans, j'ai faim: het Frans zegt avoir waar wij zijn zeggen.",
        "De impératif heeft drie vormen en geen onderwerp; bij -er valt de s weg.",
        "Na aimer, vouloir, pouvoir, devoir, aller en il faut komt een infinitief.",
        "il pleut, il neige, il faut, il y a: alleen in de derde persoon enkelvoud.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["passe-compose-imparfait-en-passe-recent" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Passé composé, imparfait en passé récent",
    onder="Drie manieren om over het verleden te spreken, en wanneer je welke neemt.",
    secties=[
        dict(kop="Waarvoor je ze nodig hebt", blokken=[
            ("p", "Moet je een <strong>verslag</strong> schrijven over een afgelopen gebeurtenis "
                  "— je stage, je weekend, een uitstap — dan gebruik je de verleden tijd: de "
                  "<em>passé composé</em> en de <em>imparfait</em>, door elkaar. Daarnaast is er "
                  "de <em>passé récent</em> voor iets dat net gebeurd is."),
            ("fig", svg.franse_tijden(),
             "Imparfait en passé composé kijken terug, passé récent net achter je, futur proche vooruit."),
        ]),
        dict(kop="De passé composé met avoir", blokken=[
            ("p", "De passé composé is <strong>twee delen</strong>: een hulpwerkwoord in de "
                  "présent plus een <strong>voltooid deelwoord</strong>. Bij de meeste "
                  "werkwoorden is dat hulpwerkwoord <em>avoir</em>."),
            ("fig", tabel(["groep", "deelwoord", "voorbeeld"], [
                ["-er", "-é", "regarder → j'ai regardé"],
                ["-ir", "-i", "finir → j'ai fini"],
                ["-re", "vaak -u", "vendre → j'ai vendu, attendre → j'ai attendu"],
                ["onregelmatig", "", "faire → fait, prendre → pris, voir → vu, avoir → eu, être → été"],
            ]), "Avoir eu en avoir été: ook die twee gaan met avoir."),
            ("p", "Met <strong>avoir</strong> verandert het deelwoord <strong>niet</strong> van "
                  "vorm: <em>elle a mangé</em>, <em>ils ont mangé</em>, <em>nous avons fait</em> "
                  "— geen e en geen s."),
            ("p", "De <strong>ontkenning</strong> gaat rond het hulpwerkwoord, niet rond het "
                  "deelwoord: <em>je n'ai pas mangé</em>, <em>il n'est pas venu</em>."),
        ]),
        dict(kop="De passé composé met être", blokken=[
            ("p", "Een kleine groep werkwoorden van <strong>komen, gaan en blijven</strong> "
                  "gebruikt <em>être</em>: <em>aller</em>, <em>venir</em>, <em>partir</em>, "
                  "<em>sortir</em>, <em>arriver</em>, <em>rester</em>, <em>entrer</em>, "
                  "<em>monter</em>, <em>descendre</em>, <em>tomber</em>, <em>naître</em>, "
                  "<em>mourir</em>, <em>devenir</em>. En daarbij <strong>alle wederkerende "
                  "werkwoorden</strong>: <em>je me suis levé</em>, <em>elle s'est lavée</em>, "
                  "<em>nous nous sommes vus</em>."),
            ("kader", "<strong>Met être past het deelwoord zich aan het onderwerp aan.</strong> "
                      "<em>Il est parti</em> — <em>elle est parti<strong>e</strong></em> — "
                      "<em>ils sont parti<strong>s</strong></em> — <em>elles sont "
                      "parti<strong>es</strong></em>. Vandaar <em>nous sommes restés</em>, "
                      "<em>les filles sont sorties</em>, <em>ils sont arrivés</em>, en <em>je "
                      "suis né</em> of <em>je suis née</em>, naargelang wie het zegt."),
            ("fig", tabel(["met avoir", "met être"], [
                ["nous avons mangé (geen s)", "nous sommes partis (met s)"],
                ["elle a fait", "elle est allée"],
                ["ils ont pris", "ils sont descendus"],
            ]), "Eén regel, twee uitkomsten: alleen met être verandert het deelwoord mee."),
        ]),
        dict(kop="De imparfait", blokken=[
            ("p", "De imparfait maak je uit de stam van de <strong>nous-vorm van de "
                  "présent</strong> plus de uitgangen <strong>-ais, -ais, -ait, -ions, -iez, "
                  "-aient</strong>. Nous parlons → <em>je parlais</em>; nous faisons → <em>je "
                  "faisais</em>; nous prenons → <em>je prenais</em>; nous habitons → <em>nous "
                  "habitions</em>."),
            ("p", "Eén werkwoord doet het anders: <strong>être</strong> → <em>j'étais, tu étais, "
                  "il était, nous étions, vous étiez, ils étaient</em>."),
            ("p", "<em>Il parlait</em> en <em>ils parlaient</em> klinken "
                  "<strong>hetzelfde</strong>: twee spellingen, één klank. Het verschil tussen "
                  "enkelvoud en meervoud zie je, je hoort het niet."),
            ("fig", tabel(["imparfait", "passé composé"], [
                ["de achtergrond, de omstandigheden", "één gebeurtenis, afgesloten"],
                ["il faisait froid, le ciel était bleu", "nous avons marché deux heures"],
                ["een gewoonte: quand j'étais petit, j'allais souvent …", "één keer: hier, je suis allé …"],
                ["wat bezig was: je dormais …", "… quand il est arrivé"],
            ]), "In één zin komen ze voortdurend samen voor: de ene geeft de achtergrond, de andere de gebeurtenis."),
            ("p", "In een verslag over je stage betekent dat: wat je <strong>elke dag</strong> "
                  "deed, komt in de imparfait (<em>je commençais à huit heures</em>), en wat op "
                  "<strong>één bepaalde dag</strong> gebeurde, in de passé composé (<em>le "
                  "premier jour, l'équipe m'a aidé</em>)."),
        ]),
        dict(kop="De passé récent: venir de", blokken=[
            ("p", "<strong>Venir de + infinitief</strong> betekent dat iets <strong>net</strong> "
                  "gebeurd is: <em>je viens de manger</em> (ik heb net gegeten), <em>elle vient "
                  "d'arriver</em>, <em>nous venons de partir</em>, <em>il vient de "
                  "téléphoner</em>."),
            ("p", "Alleen <em>venir</em> wordt vervoegd: <em>je viens, tu viens, il vient, nous "
                  "venons, vous venez, ils viennent</em>. En <em>de</em> wordt <em>d'</em> voor "
                  "een klinker."),
            ("p", "Het verschil met de gewone verleden tijd: <em>j'ai mangé</em> kan vanmorgen of "
                  "vorig jaar zijn, <em>je viens de manger</em> is daarnet. Zet je <em>venir</em> "
                  "in de imparfait, dan betekent het 'was net': <em>je venais de rentrer quand "
                  "il a sonné</em>."),
            ("weetje", "Verwar het niet met <strong>aller</strong> + infinitief: dat is net het "
                       "omgekeerde. <em>Je vais manger</em> = ik ga eten. <em>Je viens de "
                       "manger</em> = ik heb net gegeten."),
        ]),
    ],
    onthoud=[
        "Passé composé = avoir of être + voltooid deelwoord.",
        "Met avoir verandert het deelwoord niet; met être gaat het mee met het onderwerp.",
        "Met être: aller, venir, partir, sortir, arriver, rester, naître … en alle wederkerende.",
        "Deelwoorden: -é, -i, -u, en fait, pris, vu, eu, été.",
        "Imparfait = stam van de nous-vorm + -ais, -ait, -ions, -aient. être → j'étais.",
        "Imparfait = achtergrond of gewoonte; passé composé = één afgeronde gebeurtenis.",
        "venir de + infinitief = net gebeurd; aller + infinitief = gaat gebeuren.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["futur-proche-futur-simple-en-de-conditionnel-de-politesse" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Futur proche, futur simple en de conditionnel de politesse",
    onder="Twee manieren om vooruit te kijken, en de vorm waarmee je hoffelijk iets vraagt.",
    secties=[
        dict(kop="De futur proche: aller + infinitief", blokken=[
            ("p", "De eenvoudigste toekomst van het Frans is <strong>aller in de présent plus "
                  "een infinitief</strong>. Je vervoegt alleen <em>aller</em>; het tweede "
                  "werkwoord blijft onveranderd."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["je vais manger", "ik ga eten"],
                ["tu vas partir", "je gaat vertrekken"],
                ["il va pleuvoir", "het gaat regenen"],
                ["nous allons voir", "we gaan zien"],
                ["vous allez travailler", "jullie gaan werken"],
                ["ils vont arriver", "ze gaan aankomen"],
            ]), "Alleen aller verandert mee; de infinitief blijft staan zoals hij is."),
            ("p", "De ontkenning gaat rond <em>aller</em>, niet rond de infinitief: <em>je ne "
                  "vais pas manger</em>. En een voornaamwoord hoort bij de infinitief: <em>je "
                  "vais <strong>t'</strong>appeler</em>."),
            ("weetje", "<em>Je vais à Paris</em> betekent gewoon 'ik ga naar Parijs': dat is "
                       "<em>aller</em> als volwaardig werkwoord. Pas als er een "
                       "<strong>infinitief</strong> op volgt, is het een toekomende tijd."),
        ]),
        dict(kop="De futur simple", blokken=[
            ("p", "De futur simple is <strong>één woord</strong>. Je neemt de infinitief en "
                  "plakt de uitgangen <strong>-ai, -as, -a, -ons, -ez, -ont</strong> eraan. Bij "
                  "een werkwoord op <strong>-re</strong> valt de e weg."),
            ("fig", tabel(["parler", "finir", "prendre"], [
                ["je parlerai", "je finirai", "je prendrai"],
                ["tu parleras", "tu finiras", "tu prendras"],
                ["il parlera", "il finira", "il prendra"],
                ["nous parlerons", "nous finirons", "nous prendrons"],
                ["vous parlerez", "vous finirez", "vous prendrez"],
                ["ils parleront", "ils finiront", "ils prendront"],
            ]), "De uitgangen zijn de vormen van avoir: ai, as, a, ons, ez, ont."),
            ("p", "Tussen de stam en de uitgang zit <strong>altijd een r</strong>. Dat is het "
                  "kenmerk van deze tijd: hoor of zie je een r voor de uitgang, dan kijkt de "
                  "zin vooruit."),
            ("fig", tabel(["werkwoord", "stam", "je-vorm"], [
                ["être", "ser-", "je serai"],
                ["avoir", "aur-", "j'aurai"],
                ["aller", "ir-", "j'irai"],
                ["faire", "fer-", "je ferai"],
                ["pouvoir", "pourr-", "je pourrai"],
                ["vouloir", "voudr-", "je voudrai"],
                ["venir", "viendr-", "je viendrai"],
                ["voir", "verr-", "je verrai"],
                ["devoir", "devr-", "je devrai"],
            ]), "Deze stammen moet je kennen; de uitgangen blijven dezelfde."),
            ("p", "Verwar <em>j'irai</em> (futur simple van aller) niet met <em>je vais "
                  "aller</em> (futur proche). Beide betekenen dat je zal gaan."),
        ]),
        dict(kop="Welke van de twee neem je?", blokken=[
            ("fig", tabel(["futur proche", "futur simple"], [
                ["spreektaal, dagelijks", "schrijftaal, formeler"],
                ["dichtbij of al geregeld", "verder weg, een plan, een voorspelling"],
                ["je vais appeler le médecin", "l'année prochaine, je ferai un stage"],
            ]), "In een mail of een verslag staat vaker de futur simple, in een gesprekje de futur proche."),
            ("p", "Ze zijn niet streng gescheiden: in een gewone zin kunnen ze meestal beide. "
                  "Maar in een <strong>sollicitatiemail</strong> of een geschreven verslag kiest "
                  "het Frans vaker de futur simple, en in een berichtje of een gesprek de futur "
                  "proche."),
            ("p", "Een <strong>tijdsbepaling</strong> verraadt wat er moet staan: "
                  "<em>demain</em>, <em>la semaine prochaine</em>, <em>l'année prochaine</em> en "
                  "<em>dans trois jours</em> kijken vooruit en vragen een toekomende tijd. "
                  "<em>Hier</em> en <em>la semaine dernière</em> kijken terug, "
                  "<em>maintenant</em> blijft in het nu."),
        ]),
        dict(kop="De conditionnel de politesse", blokken=[
            ("kader", "Van de conditionnel heb je hier <strong>alleen de hoffelijke vorm</strong> "
                      "nodig. Je gebruikt ze om iets te <strong>vragen of te wensen zonder "
                      "bruusk te klinken</strong>. Je hoeft de conditionnel niet als volledige "
                      "tijd te kennen."),
            ("fig", tabel(["hoffelijk", "letterlijk", "wanneer"], [
                ["je voudrais un café", "ik zou een koffie willen", "iets vragen in een winkel of café"],
                ["j'aimerais travailler ici", "ik zou hier graag werken", "een wens in een mail"],
                ["pourriez-vous m'aider ?", "zou u me kunnen helpen?", "een vraag aan iemand die u is"],
                ["pourrais-tu venir ?", "zou je kunnen komen?", "een vraag aan iemand die tu is"],
            ]), "Je veux un café klinkt eisend; je voudrais un café is wat je in een café zegt."),
            ("p", "De vormen die je nodig hebt: <em>je voudrais</em>, <em>j'aimerais</em>, "
                  "<em>je pourrais</em>, <em>pourriez-vous</em>, <em>pourrais-tu</em>, "
                  "<em>est-ce que vous pourriez…</em> Ze eindigen op <strong>-ais</strong> of "
                  "<strong>-iez</strong> en hebben, net als de futur simple, een "
                  "<strong>r</strong> voor de uitgang."),
            ("p", "Dat laatste leidt tot één verraderlijk paar: <em>j'aurai</em> is de toekomst "
                  "('ik zal hebben'), <em>j'aurais</em> met een <strong>s</strong> is de "
                  "hoffelijke of voorwaardelijke vorm ('ik zou hebben'). Zo ook <em>je "
                  "serai</em> tegenover <em>je serais</em>, en <em>je pourrai</em> tegenover "
                  "<em>je pourrais</em>. Eén letter verschil, een andere betekenis."),
            ("p", "In een <strong>mail aan iemand die u is</strong> gaat die hoffelijke vorm "
                  "samen met de rest van de vous-vorm: <em>Madame, j'aimerais poser ma "
                  "candidature. Pourriez-vous me donner plus d'informations ?</em>"),
        ]),
    ],
    onthoud=[
        "Futur proche = aller (vervoegd) + infinitief: je vais manger.",
        "Futur simple = infinitief + ai, as, a, ons, ez, ont; bij -re valt de e weg.",
        "Er zit altijd een r voor de uitgang van de futur simple.",
        "Stammen uit het hoofd: ser-, aur-, ir-, fer-, pourr-, voudr-, viendr-, verr-.",
        "Futur proche in spreektaal en dichtbij; futur simple in schrijftaal en verder weg.",
        "Demain en la semaine prochaine vragen een toekomende tijd; hier kijkt terug.",
        "je voudrais, j'aimerais, pourriez-vous: zo vraag je hoffelijk iets.",
        "j'aurai = ik zal hebben; j'aurais met s = ik zou hebben.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["zinsbouw-zinsdelen-voegwoorden-en-de-overeenkomst" + NIVEAU] = dict(
    vak=VAK, niveau=DF, titel="Zinsbouw, zinsdelen, voegwoorden en de overeenkomst",
    onder="Hoe een Franse zin in elkaar zit, hoe je ze vraagt of ontkent, en wat met wat moet kloppen.",
    secties=[
        dict(kop="Zes soorten zinnen", blokken=[
            ("fig", tabel(["soort", "waarvoor", "voorbeeld"], [
                ["mededelend", "iets vertellen", "Il travaille à Bruxelles."],
                ["vragend", "iets vragen", "Où travaille-t-il ?"],
                ["bevelend", "een bevel of een raad", "Travaillez plus vite !"],
                ["uitroepend", "verbazing of gevoel", "Quel beau jardin !"],
                ["ontkennend", "iets tegenspreken", "Il ne travaille pas."],
                ["wensend", "een wens of een hoop", "J'aimerais travailler ici."],
            ]), "Aan het teken achteraan zie je er al veel: een punt, een vraagteken of een uitroepteken."),
            ("p", "De gewone woordorde van het Frans is <strong>onderwerp – persoonsvorm – de "
                  "rest</strong>. Anders dan bij ons komt er na een woord vooraan "
                  "<strong>geen</strong> omkering: <em>Demain je vais à Bruxelles</em>, niet "
                  "<em>demain vais je</em>."),
            ("fig", svg.woordvolgorde([
                ("onderwerp", "Marie", svg.FOREST),
                ("persoonsvorm", "mange", svg.AMBER),
                ("rest", "une pomme à midi", svg.DIM),
            ]), "Marie mange une pomme à midi."),
        ]),
        dict(kop="Drie manieren om een vraag te stellen", blokken=[
            ("fig", tabel(["vorm", "voorbeeld", "register"], [
                ["intonatie", "Tu viens ?", "spreektaal, heel gewoon"],
                ["est-ce que", "Est-ce que tu viens ?", "neutraal, overal goed"],
                ["omkering", "Viens-tu ? / Travaille-t-il ?", "formeler, schrijftaal"],
            ]), "Alle drie vragen hetzelfde; ze klinken alleen anders."),
            ("p", "Bij de omkering komt er een <strong>-t-</strong> tussen als er twee klinkers "
                  "tegen elkaar zouden komen: <em>travaille-t-il</em>, <em>a-t-elle</em>, "
                  "<em>va-t-on</em>."),
            ("p", "Vraagwoorden: <em>qui</em> (wie), <em>que / qu'est-ce que</em> (wat), "
                  "<em>où</em> (waar), <em>quand</em> (wanneer), <em>comment</em> (hoe), "
                  "<em>pourquoi</em> (waarom), <em>combien</em> (hoeveel), <em>quel / quelle</em> "
                  "(welke). Ze staan vooraan: <em>Pourquoi est-ce que tu pleures ?</em>"),
        ]),
        dict(kop="De ontkenning: twee delen", blokken=[
            ("p", "Een Franse ontkenning is bijna altijd <strong>twee woorden rond de "
                  "persoonsvorm</strong>: <em>ne … pas</em>. Voor een klinker wordt <em>ne</em> "
                  "<em>n'</em>: <em>je n'aime pas</em>."),
            ("fig", tabel(["ontkenning", "betekenis", "voorbeeld"], [
                ["ne … pas", "niet", "Je ne comprends pas."],
                ["ne … jamais", "nooit", "Il ne vient jamais."],
                ["ne … plus", "niet meer", "Elle ne fume plus."],
                ["ne … rien", "niets", "Je ne vois rien."],
                ["ne … personne", "niemand", "Je ne connais personne."],
                ["ne … pas encore", "nog niet", "Il n'est pas encore là."],
            ]), "Het eerste deel staat voor de persoonsvorm, het tweede erachter."),
            ("p", "In de <strong>passé composé</strong> en de <strong>futur proche</strong> gaat "
                  "de ontkenning rond het <strong>hulpwerkwoord</strong>: <em>je n'ai pas "
                  "mangé</em>, <em>je ne vais pas manger</em>. En na een ontkenning wordt "
                  "<em>un, une, du, de la, des</em> meestal <strong>de</strong>: <em>je n'ai pas "
                  "de voiture</em>."),
        ]),
        dict(kop="Enkelvoudig of samengesteld, en de voegwoorden", blokken=[
            ("p", "Een <strong>enkelvoudige zin</strong> heeft één persoonsvorm: <em>Il "
                  "travaille à Bruxelles.</em> Een <strong>samengestelde zin</strong> heeft er "
                  "twee of meer, en dan zit er een <strong>voegwoord</strong> tussen: <em>Il "
                  "travaille à Bruxelles <strong>parce qu'</strong>il aime la ville.</em>"),
            ("p", "Tel dus de <strong>persoonsvormen</strong>, niet de werkwoorden: <em>je veux "
                  "partir</em> is één persoonsvorm plus een infinitief, en dus een enkelvoudige "
                  "zin."),
            ("fig", tabel(["nevenschikkend (gelijkwaardig)", "onderschikkend (ondergeschikt)"], [
                ["et (en)", "parce que (omdat)"],
                ["ou (of)", "quand (wanneer)"],
                ["mais (maar)", "si (als)"],
                ["donc (dus)", "comme (zoals, aangezien)"],
                ["car (want)", "pendant que (terwijl)"],
                ["ni … ni (noch … noch)", "que (dat)"],
            ]), "Car en parce que betekenen allebei 'want of omdat'; car is nevenschikkend, parce que niet."),
            ("p", "Dezelfde woorden zijn ook de <strong>signaalwoorden</strong> waarmee je het "
                  "tekstverband ziet: <em>mais</em> kondigt een tegenstelling aan, <em>donc</em> "
                  "een gevolg, <em>parce que</em> een reden."),
        ]),
        dict(kop="De zinsdelen", blokken=[
            ("p", "Vier zinsdelen moet je kunnen benoemen: het <strong>sujet</strong> "
                  "(onderwerp), de <strong>verbe conjugué</strong> (persoonsvorm), het "
                  "<strong>COD</strong> (lijdend voorwerp, zonder voorzetsel) en het "
                  "<strong>COI</strong> (meewerkend voorwerp, met <em>à</em>)."),
            ("fig", svg.zinsdelen([
                ("Marie", "sujet", svg.FOREST),
                ("donne", "verbe", svg.AMBER),
                ("un livre", "COD", svg.DARK),
                ("à Paul", "COI", svg.DIM),
            ]), "Marie donne un livre à Paul."),
            ("p", "Zoek het <strong>sujet</strong> met de vraag 'wie of wat doet het?', het "
                  "<strong>COD</strong> met <em>qui ?</em> of <em>quoi ?</em> na het werkwoord, "
                  "en het <strong>COI</strong> met <em>à qui ?</em> Dat onderscheid heb je nodig "
                  "om het juiste voornaamwoord te kiezen: een COD wordt <em>le, la, les</em>, een "
                  "COI wordt <em>lui, leur</em>."),
        ]),
        dict(kop="Drie soorten overeenkomst", blokken=[
            ("fig", tabel(["wat met wat", "regel", "voorbeeld"], [
                ["sujet en persoonsvorm", "de persoonsvorm volgt het onderwerp",
                 "les enfants jouent, mon frère joue"],
                ["naamwoord en adjectief", "het adjectief volgt in geslacht en getal",
                 "une petite maison, des livres verts"],
                ["être en deelwoord", "het deelwoord volgt het onderwerp",
                 "elle est partie, ils sont partis"],
            ]), "Met avoir verandert het deelwoord niet: elle a mangé, ils ont mangé."),
            ("p", "Let bij de eerste op een <strong>onderwerp dat verder weg staat</strong>: in "
                  "<em>les élèves de ma classe travaillent bien</em> hoort de persoonsvorm bij "
                  "<em>les élèves</em>, niet bij <em>ma classe</em>."),
            ("p", "En let op het <strong>samengestelde onderwerp</strong>: <em>Marie et Paul "
                  "sont partis</em> — twee namen samen zijn een meervoud."),
            ("kader", "Dit is in het schrift veel belangrijker dan in de klank. <em>Il "
                      "joue</em> en <em>ils jouent</em> klinken gelijk, net als <em>une maison "
                      "verte</em> en <em>des maisons vertes</em> op de laatste klank na. Bij een "
                      "<strong>schrijfopdracht</strong> wordt juist dat nagekeken."),
        ]),
    ],
    onthoud=[
        "Zes soorten zinnen: mededelend, vragend, bevelend, uitroepend, ontkennend, wensend.",
        "De woordorde blijft onderwerp, persoonsvorm, rest: demain je vais, geen omkering.",
        "Een vraag stellen: intonatie, est-ce que, of omkering met -t- ertussen.",
        "De ontkenning is twee delen rond de persoonsvorm: ne … pas, jamais, plus, rien.",
        "Na een ontkenning wordt un, du of des meestal de: je n'ai pas de voiture.",
        "Tel de persoonsvormen om enkelvoudig van samengesteld te onderscheiden.",
        "Sujet, verbe conjugué, COD (zonder à), COI (met à).",
        "Drie overeenkomsten: onderwerp met persoonsvorm, naamwoord met adjectief, être met deelwoord.",
    ],
)
