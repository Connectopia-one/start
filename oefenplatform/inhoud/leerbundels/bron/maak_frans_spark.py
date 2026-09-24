# -*- coding: utf-8 -*-
"""De leerbundels voor Frans op ✨ Spark-niveau.

Gebaseerd op de vakfiche Frans 1ste graad A-stroom die Kim aanleverde.

Let op: dit vak oefent **alleen het schriftelijke Frans**. Het examen van de
Examencommissie bestaat ook uit luisteren, spreken en een gesprek, en dat kan
een oefenplatform met tekstvragen niet nabootsen. Dat staat ook met zoveel
woorden in de eerste bundel, zodat niemand denkt dat dit het hele examen dekt.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met moeilijkere vragen. De bundel wordt
dus twee keer geüpload, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../spark/frans.json` doet daar het
voorwerk voor; daarna gaat elke vraag nog één voor één naast de tekst.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Frans"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
tabel = bundel.tabel

SCHRIFTELIJK = (
    "<strong>Dit oefenplatform oefent alleen het schriftelijke Frans.</strong> Het examen "
    "van de Examencommissie telt vijf onderdelen: luisteren (30 %), lezen (30 %), schrijven "
    "(2 x 8 %), spreken (8 %) en twee gesprekken (2 x 8 %). Luisteren, spreken en de "
    "gesprekken oefen je hier niet: daar heb je geluid en een gesprekspartner voor nodig. "
    "Wat je hier wél oefent — lezen, schrijven, woordenschat en grammatica — is samen goed "
    "voor 46 % van je punten, en je hebt het ook nodig om te kunnen luisteren en spreken."
)

BUNDELS = {}

# ---------------------------------------------------------------------------

BUNDELS["een-franse-tekst-lezen"] = dict(
    vak=VAK, niveau=SPARK, titel="Een Franse tekst lezen",
    onder="Het onderwerp, de hoofdgedachte en de hoofdpunten vinden, ook als je niet elk woord kent.",
    secties=[
        dict(kop="Waarvoor dient dit vak hier?", blokken=[
            ("kader", SCHRIFTELIJK),
            ("p", "Lezen is met 30 % het zwaarste onderdeel dat je hier kan inoefenen, "
                  "evenveel als luisteren. En wie vlot leest, herkent dezelfde woorden ook "
                  "terug als hij ze hoort."),
        ]),
        dict(kop="Drie lagen in elke tekst", blokken=[
            ("p", "Het <strong>onderwerp</strong> is waarover een tekst gaat. Je zegt het in "
                  "één of enkele <strong>woorden</strong>, bijvoorbeeld 'dieren'. Je schrijft "
                  "het dus niet op in een volledige zin."),
            ("p", "De <strong>hoofdgedachte</strong> is de belangrijkste boodschap, in "
                  "één <strong>zin</strong>: 'Dieren horen niet thuis in de zoo.' De "
                  "<strong>hoofdpunten</strong> zijn de inhoudelijke elementen die die "
                  "hoofdgedachte <strong>ondersteunen</strong>: dieren moeten in de vrije "
                  "natuur kunnen bewegen, ze zijn gevoelig voor stress, ze gedragen zich "
                  "anders."),
            ("fig", svg.kernpiramide(),
             "Onderwerp in enkele woorden, hoofdgedachte in één zin, daaronder de punten die haar dragen."),
            ("p", "Een tekst kondigt zijn onderwerp vaak zelf aan met "
                  "<strong>il s'agit de…</strong> (het gaat over…). En 'Kavaan, un éléphant, "
                  "a quitté le zoo pour un parc naturel au Cambodge' zegt je de kern: de "
                  "olifant Kavaan verhuisde van de zoo naar een natuurpark in Cambodja "
                  "(<em>quitter</em> = verlaten)."),
        ]),
        dict(kop="Wat je doet vóór en tijdens het lezen: de strategieën", blokken=[
            ("p", "De vakfiche noemt ze met die naam: <strong>strategieën</strong>, manieren van aanpakken die je helpen om een tekst te begrijpen ook als hij moeilijker is dan je aankan. Je hoeft ze niet uit het hoofd te kennen, je moet ze gebruiken."),
            ("fig", svg.stappen([
                "Titel en foto&#39;s|Waarover gaat dit?",
                "Lezen en zoeken|Uur, prijs, datum",
                "Pas dan opzoeken|Welk woord echt nodig is",
            ]), "Drie stappen, in die volgorde. Vertalen doe je nooit als eerste."),
            ("p", "Stel jezelf vooraf enkele vragen: wat weet ik al over dit onderwerp, en "
                  "waarover zou de tekst kunnen gaan? Gebruik daarbij de "
                  "<strong>visuele hulpmiddelen</strong> die de tekst biedt: de titel en de "
                  "tussentitels, <strong>benadrukte woorden</strong>, een foto, een tekening "
                  "of een grafiek. Hoeveel bladzijden de tekst telt, zegt je niets."),
            ("p", "Moet je <strong>informatie selecteren</strong> — het uur van een activiteit, "
                  "de prijs, de datum — dan lees je gericht: je zoekt naar cijfers en "
                  "tijdsaanduidingen in plaats van de hele tekst woord voor woord te lezen. "
                  "In een <strong>uitnodiging</strong> of op een affiche zoek je net die drie "
                  "gegevens: de <strong>datum</strong>, het <strong>uur</strong> en de "
                  "<strong>plaats</strong>. Wie de affiche gedrukt heeft, zelden."),
            ("kader", "<strong>Je moet niet elk woord kennen.</strong> Leid de betekenis af uit "
                      "de zin eromheen, uit wat je al weet, of uit de manier waarop het woord "
                      "gevormd is. Beslis daarna of dat woord echt nodig is om de tekst te "
                      "begrijpen. Alleen dan zoek je het op. Je mag op het examen een online "
                      "woordenboek gebruiken, maar je hebt geen tijd om elk woord op te zoeken, "
                      "dus zorg voor een basiswoordenschat."),
            ("p", "Je kennis van het Nederlands en van andere vreemde talen, zoals het "
                  "<strong>Engels</strong>, helpt je zulke woorden te <strong>raden</strong>: "
                  "<em>la musique</em>, <em>le téléphone</em>, <em>la télévision</em>, "
                  "<em>une information</em>, <em>un restaurant</em> en <em>un animal</em> raad "
                  "je zo. Maar <em>le pain</em> (het brood) en <em>la nourriture</em> (het "
                  "eten) lijken nergens op; die moet je leren."),
            ("p", "Drie bronnen gebruik je dus om te raden: de <strong>context</strong> (de zin eromheen), je <strong>voorkennis</strong> (wat je al over het onderwerp weet) en je <strong>moedertaal</strong> of een andere taal die je kent. Dat staat zo in de fiche."),
        ]),
        dict(kop="Het communicatiemodel bij een tekst", blokken=[
            ("fig", svg.communicatiemodel(),
             "Van wie is de tekst, waarom is hij geschreven, en voor wie?"),
            ("p", "Die drie vragen vormen samen het <strong>communicatiemodel</strong>. Ze "
                  "zeggen je meer over een tekst dan om het even welk los woord."),
            ("p", "Let ook op de <strong>structuuraanduiders</strong>. Dat is het woord waarmee de fiche twee soorten wegwijzers samen benoemt: <strong>verwijswoorden</strong> (voornaamwoorden zoals <em>ils</em> en <em>y</em>) en <strong>signaalwoorden</strong> (zoals <em>d'abord</em>, <em>puis</em>, <em>parce que</em>). Samen laten ze je de gedachtegang van de tekst volgen. Ze krijgen een eigen bundel: die over tekstsoorten, signaalwoorden en verwijswoorden."),
        ]),
        dict(kop="Woorden die vaak in een leestekst staan", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["il s'agit de", "het gaat over"],
                ["selon / d'après l'auteur", "volgens / volgens de auteur (een mening, geen feit)"],
                ["une enquête, une étude récente", "een onderzoek, een recent onderzoek"],
                ["environ, la plupart, la moitié, plus de", "ongeveer, de meeste, de helft, meer dan"],
                ["malgré, cependant, en revanche", "ondanks, nochtans, daarentegen"],
                ["il est interdit de, gratuit", "het is verboden te, gratis"],
                ["à partir de, jusqu'à", "vanaf, tot"],
                ["la vie quotidienne, les habitudes alimentaires", "het dagelijkse leven, de eetgewoonten"],
                ["un article de journal, le titre", "een krantenartikel, de titel"],
                ["courir, la piscine, les jeunes, un écran", "lopen, het zwembad, de jongeren, een scherm"],
                ["passer du temps, devant, dormir, bouger", "tijd doorbrengen, voor, slapen, bewegen"],
            ]), "Environ, la moitié en plus de gaan over een hoeveelheid; 'la plupart des élèves' (de meeste leerlingen) is niet hetzelfde als 'tous les élèves' (alle leerlingen)."),
            ("weetje", "Op het examen krijg je teksten over het dagelijkse leven, de "
                       "samenleving en het schoolleven, én over landen en streken waar Frans "
                       "gesproken wordt. Je haalt er bijvoorbeeld de eetgewoonten uit, of je "
                       "merkt op dat in Franstalig België iedereen elkaar met een kus begroet, "
                       "ook mannen onder elkaar."),
            ("p", "De fiche noemt dat: je <strong>identificeert aspecten van maatschappijen en culturen waarin Frans gesproken wordt</strong>. Het gaat om het dagelijkse leven, de leefomstandigheden, gewoontes, sociale verhoudingen, waarden en normen, <strong>lichaamstaal</strong> en <strong>sociale conventies</strong>. Je moet die dingen niet van buiten leren: je moet ze uit een tekst kunnen halen als ze erin staan."),
        ]),
    ],
    onthoud=[
        "Onderwerp = enkele woorden. Hoofdgedachte = één zin. Hoofdpunten = wat haar draagt.",
        "Kijk eerst naar titel, tussentitels, benadrukte woorden en beeld.",
        "Raad een onbekend woord uit de context; zoek het pas op als het echt nodig is.",
        "Zoek gericht als je een uur, een prijs of een datum moet vinden.",
        "'Selon' en 'd'après l'auteur' kondigen een mening aan, geen feit.",
        "Lezen telt voor 30 % van het examen.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["tekstsoorten-signaalwoorden-en-verwijswoorden"] = dict(
    vak=VAK, niveau=SPARK, titel="Tekstsoorten, signaalwoorden en verwijswoorden",
    onder="Vijf soorten teksten, en de kleine woordjes die de weg wijzen.",
    secties=[
        dict(kop="Vijf soorten teksten", blokken=[
            ("fig", tabel(["soort tekst", "wat ze doet", "voorbeelden"], [
                ["informatief — een informatieve tekst", "geeft je informatie over een onderwerp", "een krantenartikel, een stukje uit een leerboek, een interview"],
                ["opiniërend — een opiniërende tekst", "iemand geeft zijn mening", "een gesprek over een boek, een reactie op sociale media"],
                ["prescriptief — een prescriptieve tekst", "legt uit wat of hoe je iets moet doen", "een recept, een instructiefilmpje op YouTube, een schoolreglement"],
                ["narratief — een narratieve tekst", "geeft feiten en gebeurtenissen verhalend weer", "een videoblog, een reisverslag, een podcast"],
                ["literair — een literaire tekst", "heeft een esthetische waarde, speelt in op emoties", "een lied, een gedicht, een cartoon, een strip, een kortverhaal"],
            ]), "Prescriptief komt van 'voorschrijven', narratief van 'narrer' (vertellen), opinie van 'mening'."),
            ("p", "Aan de woorden zie je vaak meteen welk soort je voor je hebt. "
                  "<em>'Mélangez la farine et les œufs, puis ajoutez le lait'</em> geeft "
                  "bevelen: meng en voeg toe. Dat is een recept, dus prescriptief. "
                  "<em>'Ce film est vraiment ennuyeux, je ne le conseille à personne'</em> is "
                  "een mening (<em>ennuyeux</em> = saai, <em>conseiller</em> = aanraden). "
                  "<em>'Bonjour à tous ! Aujourd'hui je vous emmène à Marseille'</em> is een "
                  "videoblog of reisverslag."),
            ("p", "Eén tekst kan <strong>meer dan één doel</strong> hebben: een reisverslag "
                  "dat ook informatie geeft, een videoblog waarin iemand ook zijn mening geeft, "
                  "een strip die ook iets uitlegt."),
            ("p", "Weten met welk soort je te maken hebt, is geen etiket plakken. Het zegt je "
                  "waarop je moet letten: bij een recept op de <strong>volgorde van de "
                  "stappen</strong>, bij een opiniestuk op de <strong>argumenten</strong>, bij "
                  "een verhaal op de <strong>gebeurtenissen</strong>."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", "<strong>Signaalwoorden</strong> zeggen vooraf wat er komt. Ze helpen je om "
                  "de gedachtegang van een tekst te reconstrueren."),
            ("fig", tabel(["verband", "Frans", "Nederlands"], [
                ["volgorde en opsomming", "d'abord, ensuite, puis, enfin", "eerst, daarna, vervolgens, ten slotte (enfin sluit de opsomming af)"],
                ["reden", "parce que, car", "omdat, want"],
                ["gevolg", "donc, alors", "dus, dan"],
                ["tegenstelling", "mais, pourtant, cependant, en revanche", "maar, nochtans, echter, daarentegen"],
                ["toevoeging", "de plus, en plus, aussi", "bovendien, daarbij, ook"],
                ["voorbeeld", "par exemple", "bijvoorbeeld"],
                ["toegeving", "bien que, malgré", "hoewel, ondanks"],
            ]), "'Je reste à la maison parce qu'il pleut': parce que geeft de reden."),
        ]),
        dict(kop="Verwijswoorden", blokken=[
            ("p", "Een <strong>verwijswoord</strong> grijpt terug naar iets dat al genoemd is. "
                  "Vind je niet terug naar wie of wat het verwijst, dan is de tekst op dat punt "
                  "onduidelijk — en moet de schrijver het naamwoord gewoon opnieuw schrijven. "
                  "Omgekeerd gebruik je ze zelf ook, om niet steeds hetzelfde woord te moeten "
                  "herhalen."),
            ("fig", tabel(["zin", "het verwijswoord", "waarnaar"], [
                ["Les élèves sont en classe. <strong>Ils</strong> écoutent le professeur.", "ils", "de leerlingen"],
                ["Je vais à Paris. J'<strong>y</strong> vais en train.", "y", "naar Parijs (een plaats)"],
                ["Ma sœur adore les chats. Elle <strong>en</strong> a trois.", "en", "katten (een hoeveelheid)"],
                ["Marie parle à Paul. Elle <strong>lui</strong> explique le problème.", "lui", "aan Paul"],
                ["Les enfants jouent dehors. Leurs parents <strong>les</strong> regardent.", "les", "de kinderen"],
            ]), "'Y' vervangt meestal een plaats, 'en' meestal een hoeveelheid."),
        ]),
    ],
    onthoud=[
        "Vijf soorten: informatief, opiniërend, prescriptief, narratief, literair.",
        "Eén tekst kan meer dan één doel hebben.",
        "d'abord, ensuite, enfin = volgorde. parce que = reden. donc, alors = gevolg.",
        "mais, pourtant, cependant, en revanche = tegenstelling.",
        "y = een plaats, en = een hoeveelheid, lui = aan wie.",
        "Signaalwoorden helpen je de gedachtegang van een tekst te volgen.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["schrijven-berichten-uitnodigingen-en-mails"] = dict(
    vak=VAK, niveau=SPARK, titel="Schrijven: berichten, uitnodigingen en mails",
    onder="Wat je schrijft, voor wie, en in welke toon. Plus waarop je beoordeeld wordt.",
    secties=[
        dict(kop="Wat je moet kunnen schrijven", blokken=[
            ("p", "De vakfiche noemt vijf dingen. Je legt <strong>alledaagse sociale "
                  "contacten</strong>: begroeten, aanspreken, afscheid nemen, iets voorstellen, "
                  "bedanken, feliciteren, uitnodigen, je verontschuldigen en reageren op "
                  "verontschuldigingen. Je <strong>geeft en vraagt informatie</strong> (een "
                  "uitnodiging voor een feestje schrijven). Je <strong>geeft je mening</strong> "
                  "(reageren op een discussie op sociale media). Je <strong>vertelt "
                  "iets</strong> (wat je in het weekend gedaan hebt). En je <strong>legt iemand "
                  "iets uit</strong>, bijvoorbeeld hoe je een gerecht klaarmaakt op basis van "
                  "foto's."),
            ("kader", "Bij een schrijfopdracht krijg je een <strong>schrijfkader</strong> dat je "
                      "ondersteunt. Volg de onderdelen die het vraagt, punt per punt: dan haal "
                      "je de taakvoltooiing binnen."),
        ]),
        dict(kop="Vaste zinnen die je altijd kan gebruiken", blokken=[
            ("fig", tabel(["waarvoor", "Frans"], [
                ["groeten (informeel / formeel)", "Salut ! / Bonjour, Madame, Monsieur,"],
                ["bedanken", "Merci beaucoup (hartelijk dank). Je vous remercie (ik dank u). Merci d'avance (alvast bedankt)."],
                ["antwoorden op dank", "De rien. Je vous en prie."],
                ["je verontschuldigen (sorry)", "Je suis désolé. Je vous prie de m'excuser."],
                ["feliciteren en wensen", "Félicitations ! Bon anniversaire ! Bonne chance !"],
                ["uitnodigen", "Tu viens à ma fête samedi ? (kom je zaterdag naar mijn feestje?)"],
                ["aanvaarden", "Avec plaisir ! D'accord, je viens. Oui, merci, à samedi !"],
                ["weigeren", "Désolé, je ne peux pas venir."],
                ["iets vragen", "Peux-tu m'aider ? Pouvez-vous m'aider ? Je voudrais savoir…"],
                ["een mail openen", "Je vous écris pour…"],
                ["afsluiten (informeel)", "À bientôt ! (tot binnenkort) Salut ! Bisous ! À plus !"],
                ["afsluiten (formeel)", "Cordialement, / Veuillez agréer mes salutations distinguées."],
                ["beleefd blijven", "s'il te plaît / s'il vous plaît"],
                ["te laat zijn", "Je serai en retard."],
            ]), "Une fête = een feest. 'À plus !' is heel informeel; 'Cordialement' past bij een leerkracht."),
            ("kader", "In een <strong>uitnodiging</strong> horen zeker drie gegevens: <strong>wanneer</strong> (de datum), <strong>hoe laat</strong> (het uur) en <strong>waar</strong> (de plaats). <em>Tu viens à ma fête samedi, à 15 heures, chez moi ?</em> Wie het feestje organiseert of hoeveel het kost, hoeft er niet in; die drie wel, anders weet je gast niet waar hij moet zijn."),
        ]),
        dict(kop="Tu of vous: het register", blokken=[
            ("fig", svg.registerschaal(),
             "Tegen een klasgenoot 'tu', tegen een onbekende volwassene 'vous'."),
            ("p", "De fiche verwacht van jou een <strong>neutraal of informeel register</strong> "
                  "met <strong>gepaste beleefdheidsconventies</strong>. Een daarvan is heel "
                  "concreet: spreek je in het Frans een politieagent of een verkoper aan, dan "
                  "zeg je altijd eerst <strong>bonjour</strong>."),
            ("p", "Beleefd word je vooral met de <strong>conditionnel de politesse</strong>: "
                  "<em>je voudrais</em> in plaats van <em>je veux</em>, en "
                  "<em>pourriez-vous m'envoyer le programme ?</em> in plaats van "
                  "<em>envoyez le programme</em>. 'Je voudrais' betekent 'ik zou graag…'."),
            ("weetje", "In een WhatsAppgesprek met vrienden kan een emoji je boodschap "
                       "ondersteunen. In een formele mail is hij ongepast. Dezelfde inhoud, "
                       "een andere ontvanger, een andere vorm."),
        ]),
        dict(kop="Waarop je beoordeeld wordt", blokken=[
            ("fig", tabel(["vereiste", "wat men nakijkt"], [
                ["taakvoltooiing", "het doel is bereikt, je boodschap komt over, is volledig, helder, correct en ter zake, en je respecteert de opgegeven lengte"],
                ["woordenschat", "frequente woorden, woordcombinaties en vaste uitdrukkingen correct gebruikt"],
                ["grammatica en zinsbouw", "eenvoudige correcte zinnen; fouten verstoren de communicatie niet"],
                ["tekststructuur en samenhang", "inleiding, midden en slot, met herkenbare tekstverbanden"],
                ["register en beleefdheidsconventies", "neutraal of informeel, passend bij je ontvanger"],
                ["tekstopbouw en lay-out", "de opbouw is duidelijk herkenbaar, de lay-out gepast"],
                ["spelling en leestekens", "je spelt redelijk correct, met spellingcontrole en woordenboek"],
            ]), "Perfect hoef je niet te zijn: fouten mogen, zolang ze je boodschap niet in de weg staan."),
            ("p", "Een formele mail heeft drie vaste onderdelen: een <strong>aanhef</strong> "
                  "('Madame, Monsieur,'), de <strong>reden waarom je schrijft</strong> ('Je vous "
                  "écris pour…') en een <strong>slotgroet</strong> ('Cordialement,'). Emoji's "
                  "horen daar niet bij."),
            ("p", "Een goed opgebouwde tekst heeft een <strong>inleiding</strong>, een "
                  "<strong>midden</strong> en een <strong>slot</strong>, met signaalwoorden "
                  "ertussen: <em>d'abord, ensuite, enfin</em>. Wil je een mening geven, zet er "
                  "dan een reden bij met <em>parce que</em>: "
                  "<em>'J'aime ce film parce que l'histoire est surprenante.'</em>"),
            ("p", "Vertel je wat je in het weekend gedaan hebt, dan staat dat in de "
                  "<strong>verleden tijd</strong>: <em>j'ai joué au foot</em>, "
                  "<em>je suis allé au cinéma</em>."),
        ]),
        dict(kop="Als je vastzit", blokken=[
            ("p", "Laat je niet ontmoedigen: probeer je doel te bereiken met de woorden en "
                  "structuren die je wél al kent. Ken je een woord niet, dan "
                  "<strong>omschrijf</strong> je het. Je mag ook een online woordenboek en een "
                  "spellingcontrole gebruiken; oefen daar thuis mee."),
            ("p", "En als allerlaatste stap: <strong>lees je tekst grondig na</strong>. Is de "
                  "communicatie helder, gepast en vlot? Moet je schrappen omdat je tekst te lang "
                  "is, laat dan losse details vallen, niet de kern."),
        ]),
    ],
    onthoud=[
        "Volg het schrijfkader: elk onderdeel dat het vraagt, komt in je tekst.",
        "Tu bij vrienden, vous bij een onbekende volwassene. Begin met bonjour.",
        "Je voudrais en pourriez-vous zijn de beleefde vormen.",
        "Inleiding, midden en slot, met d'abord, ensuite en enfin ertussen.",
        "Een mening krijgt een reden met 'parce que'.",
        "Fouten mogen, zolang ze de boodschap niet verstoren. Lees altijd na.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["een-foto-of-afbeelding-beschrijven"] = dict(
    vak=VAK, niveau=SPARK, titel="Een foto of afbeelding beschrijven",
    onder="Er is, er zijn, en waar het staat: de bouwstenen van een beschrijving in het Frans.",
    secties=[
        dict(kop="Waarom dit apart staat", blokken=[
            ("p", "De vakfiche vraagt bij schrijven dat je <strong>iemand iets uitlegt</strong>, "
                  "met als voorbeeld: uitleggen hoe je een gerecht moet klaarmaken "
                  "<em>op basis van foto's of afbeeldingen</em>. En bij literatuur dat je "
                  "<strong>schriftelijk je eigen beleving verwoordt</strong>. Een beeld "
                  "beschrijven komt dus twee keer van pas, en het is iets wat je kan oefenen "
                  "met een vaste set zinnen."),
            ("kader", "Krijg je bij de foto een <strong>schrijfkader</strong>, dan zegt dat kader wat je beschrijving moet bevatten. Volg het punt per punt: elk onderdeel dat het vraagt, komt in je tekst. Zo haal je de <strong>taakvoltooiing</strong> binnen, en dat is de eerste vereiste van de fiche."),
        ]),
        dict(kop="Begin met wat er is", blokken=[
            ("p", "Bijna elke beschrijving begint met <strong>il y a</strong>, 'er is' of 'er "
                  "zijn'. Die vorm verandert nooit: <em>il y a un chien</em>, <em>il y a trois "
                  "enfants</em>. Daarnaast kan je <em>je vois</em> (ik zie) of <em>on voit</em> "
                  "(men ziet) gebruiken."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["Sur la photo, il y a une famille à table.", "Op de foto is er een gezin aan tafel."],
                ["Je vois trois enfants.", "Ik zie drie kinderen."],
                ["On voit une église.", "Men ziet een kerk."],
                ["La scène se passe à la plage.", "Het tafereel speelt zich af op het strand."],
            ]), "'Se passer' betekent zich afspelen: zo zeg je in één zin waar het beeld genomen is."),
        ]),
        dict(kop="Zeg waar het staat", blokken=[
            ("fig", svg.fotokader(),
             "Links, midden, rechts, voorgrond en achtergrond: vijf plaatsen om je beschrijving aan op te hangen."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["à gauche / à droite / au milieu", "links / rechts / in het midden"],
                ["au premier plan", "op de voorgrond"],
                ["à l'arrière-plan / au fond", "op de achtergrond / achteraan"],
                ["devant / derrière / dans / à côté de", "voor / achter / in / naast"],
            ]), "'Devant la maison' is voor het huis, 'dans le jardin' in de tuin."),
            ("p", "'À gauche, il y a une femme avec un enfant' zegt veel meer dan 'la femme est "
                  "là'. Wie je beschrijving leest, ziet het beeld niet; 'daar' helpt hem niet."),
        ]),
        dict(kop="Beschrijf de mensen", blokken=[
            ("fig", tabel(["waarover", "Frans"], [
                ["gestalte", "Il est grand et mince."],
                ["haar", "Elle a les cheveux longs et bruns. / Elle a les cheveux courts."],
                ["ogen", "Elle a les yeux bleus."],
                ["kleren", "Elle porte un manteau rouge. Il porte un jean et des baskets. Il porte des lunettes."],
                ["hoe iemand eruitziet", "Elle a l'air fatiguée (moe). Elle a l'air triste (verdrietig). Ils ont l'air de s'amuser."],
                ["gevoel", "Ils sont contents (ze zijn blij). Elle est heureuse."],
            ]), "Porter = dragen. De kleur staat achter het naamwoord: un manteau rouge, une robe bleue."),
            ("p", "Let op de vorm: <em>manteau</em> is mannelijk (<em>un</em> manteau), en "
                  "<em>porter</em> vervoeg je gewoon: <em>elle porte</em>, niet 'elle port'. "
                  "'<strong>Avoir l'air</strong>' + bijvoeglijk naamwoord betekent 'eruitzien "
                  "als', en met een infinitief erachter 'lijken te': <em>ils ont l'air de "
                  "s'amuser</em>, ze lijken zich te amuseren."),
            ("p", "Waar je niet aan kan zien wat iemand doet of voelt, zeg je het voorzichtig: "
                  "<strong>je pense que…</strong> (ik denk dat), <strong>il me semble que…</strong> "
                  "(het lijkt me dat), <strong>peut-être que…</strong> (misschien). Zet nooit "
                  "iets als feit neer dat je niet ziet: dan beschrijf je de foto niet meer en "
                  "klopt je uitleg niet."),
        ]),
        dict(kop="Beschrijf wat er gebeurt en hoe het aanvoelt", blokken=[
            ("p", "Een foto toont <strong>één moment</strong>, dus beschrijf je hem in de "
                  "<strong>tegenwoordige tijd</strong>: <em>un homme lit un journal</em> (een "
                  "man leest een krant), <em>les enfants jouent dans le jardin</em>. Wil je "
                  "benadrukken dat iets nét bezig is, gebruik dan <strong>être en train "
                  "de</strong> + infinitief: <em>ils sont en train de préparer le repas</em>, "
                  "ze zijn de maaltijd aan het klaarmaken."),
            ("fig", tabel(["waarover", "Frans"], [
                ["sfeer", "L'ambiance est joyeuse. La scène est calme. Tout le monde sourit."],
                ["weer", "Il fait beau sur la photo. Il y a du soleil."],
                ["je mening", "Cette photo me plaît parce qu'elle est joyeuse."],
            ]), "'Il fait beau' gaat over het weer; 'la photo est belle' over de foto zelf."),
            ("p", "Moet je met foto's uitleggen hoe iets gemaakt wordt, zet de stappen dan op "
                  "een rij met <strong>d'abord</strong> (eerst), <strong>ensuite</strong> "
                  "(daarna) en <strong>enfin</strong> (ten slotte)."),
        ]),
        dict(kop="De volgorde van je beschrijving", blokken=[
            ("fig", svg.stappen([
                "Het geheel|Sur la photo, il y a…",
                "De details|À gauche… au premier plan…",
                "Je mening|Cette photo me plaît…",
            ]), "Eerst waar de foto over gaat, dan wat je precies ziet, pas daarna wat je ervan vindt."),
            ("p", "Dat is dezelfde inleiding-midden-slot die de fiche ook bij de tekststructuur "
                  "vraagt. Heb je maar een beperkte lengte gekregen, laat dan losse details "
                  "vallen — elke kleur apart hoeft niet. Het onderwerp, de plaats en je mening "
                  "met een reden zijn de kern."),
        ]),
        dict(kop="Je beleving bij een literaire tekst", blokken=[
            ("p", "Dezelfde zinnen heb je nodig bij de tweede opdracht waar de fiche om vraagt: "
                  "je <strong>verwoordt schriftelijk je eigen beleving en interpretatie</strong> "
                  "bij een <strong>literaire tekst</strong> — een gedicht, een verhaal, een lied, "
                  "een strip. Ook daar krijg je hulp: een <strong>schrijfkader</strong>, "
                  "<strong>sleutelwoorden</strong> of een voorbeeld."),
            ("fig", tabel(["wat men kan vragen", "hoe je begint"], [
                ["waarom iets je aanspreekt", "J'aime ce poème parce que…"],
                ["waarom je je herkent in een personage", "Je m'identifie à ce personnage parce que…"],
                ["of je zoiets al hebt meegemaakt", "Moi aussi, j'ai vécu quelque chose comme ça."],
                ["welk gevoel de tekst oproept", "Ce texte me rend triste / heureux."],
                ["wat je van de stijl of de vorm vindt", "J'aime le style / les rimes."],
                ["zelf een einde verzinnen", "À la fin, je pense que…"],
            ]), "Een personage is een figuur in het verhaal. Verzin je zelf een einde, dan moet het geloofwaardig zijn: het moet bij het verhaal passen."),
            ("p", "Je <strong>beleving</strong> is wat de tekst bij jou doet; je "
                  "<strong>interpretatie</strong> is hoe jij hem begrijpt. Geef altijd een "
                  "<strong>reden</strong> met <em>parce que</em>: 'mooi' alleen is geen antwoord."),
        ]),
    ],
    onthoud=[
        "Il y a verandert nooit: il y a un chien, il y a trois enfants.",
        "à gauche, au milieu, à droite; au premier plan, à l'arrière-plan.",
        "Elle porte… / Elle a les cheveux… / Elle a l'air… beschrijven een persoon.",
        "Een foto beschrijf je in de tegenwoordige tijd.",
        "Wat je niet zeker weet: je pense que, il me semble que, peut-être que.",
        "Eerst het geheel, dan de details, dan je mening met parce que.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordenschat-mensen-familie-gevoelens-en-gezondheid"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: mensen, familie, gevoelens en gezondheid",
    onder="Jezelf en anderen voorstellen, beschrijven en zeggen hoe je je voelt.",
    secties=[
        dict(kop="Jezelf voorstellen", blokken=[
            ("fig", tabel(["vraag", "antwoord"], [
                ["Comment tu t'appelles ?", "Je m'appelle Lotte. (s'appeler is wederkerend: je m'appelle, tu t'appelles, il s'appelle)"],
                ["Quel âge as-tu ?", "J'ai quatorze ans. (ik ben veertien jaar)"],
                ["Où habites-tu ?", "J'habite à Hasselt. (habiter = wonen)"],
                ["Quelle est ta nationalité ?", "Je suis belge. / Je suis française."],
            ]), "Naam, leeftijd, woonplaats en nationaliteit: dat zijn je persoonlijke gegevens."),
            ("kader", "In het Frans <strong>heb</strong> je je leeftijd: <em>j'ai quatorze "
                      "ans</em>, met <strong>avoir</strong> en niet met être. 'Je suis "
                      "quatorze ans' bestaat niet. Datzelfde geldt voor <em>j'ai faim</em> "
                      "(honger), <em>j'ai soif</em> (dorst), <em>j'ai peur</em> (bang) en "
                      "<em>j'ai mal</em> (pijn)."),
            ("weetje", "Nationaliteiten krijgen in het Frans een <strong>kleine letter</strong>: "
                       "<em>je suis belge</em>. Het land krijgt er wel een: <em>la "
                       "Belgique</em>, <em>la France</em>. En let op: <em>la France</em> is het "
                       "land, <em>le français</em> de taal, <em>une Française</em> een vrouw."),
        ]),
        dict(kop="De familie", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["le père / la mère", "de vader / de moeder"],
                ["les parents", "de ouders"],
                ["le frère / la sœur", "de broer / de zus"],
                ["les grands-parents", "de grootouders"],
                ["un oncle / une tante", "een oom / een tante"],
                ["un cousin / une cousine", "een kozijn / een nicht (kind van je oom of tante)"],
                ["un neveu / une nièce", "een neef / een nicht (kind van je broer of zus)"],
                ["la belle-mère, le beau-père, la belle-sœur", "de schoonmoeder of stiefmoeder, de schoonvader, de schoonzus"],
                ["un ami / une amie, un voisin / une voisine", "een vriend / een vriendin, een buur / een buurvrouw"],
            ]), "Beau- en belle- voor een familielid betekent 'schoon-' of 'stief-'."),
            ("p", "<em>La mère</em> (de moeder) en <em>la mer</em> (de zee) klinken bijna "
                  "hetzelfde. Kijk naar de zin om te weten welk woord er staat."),
        ]),
        dict(kop="Gevoelens", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["content / contente", "blij, tevreden"],
                ["triste", "verdrietig"],
                ["fatigué", "moe"],
                ["heureux", "gelukkig"],
                ["inquiet / inquiète", "ongerust, bezorgd"],
                ["fier / fière", "trots"],
                ["déçu", "ontgoocheld"],
                ["surpris", "verrast"],
                ["sympa (sympathique)", "aardig, leuk"],
            ]), "Bij een meisje krijgt het woord vaak een -e erbij: content wordt contente."),
            ("p", "Over jezelf zeg je <em>je suis content</em>, of <em>je me sens mieux</em> "
                  "(ik voel me beter). <em>Se sentir</em> is wederkerend: je me sens, tu te "
                  "sens. En <em>j'ai peur</em> betekent 'ik ben bang' — opnieuw met avoir."),
        ]),
        dict(kop="Het lichaam en de gezondheid", blokken=[
            ("p", "De <strong>lichaamsdelen</strong> heb je nodig om te zeggen waar het pijn "
                  "doet, en om iemand te beschrijven: <em>elle a les yeux bleus</em> (ze heeft "
                  "blauwe ogen)."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la tête, la gorge, le ventre, le dos", "het hoofd, de keel, de buik, de rug"],
                ["la main, le pied, les yeux (un œil), les dents", "de hand, de voet, de ogen (een oog), de tanden"],
                ["les cheveux", "het haar (altijd meervoud)"],
                ["malade, une maladie", "ziek, een ziekte"],
                ["enrhumé, un rhume", "verkouden, een verkoudheid"],
                ["un médecin, une infirmière", "een arts of dokter, een verpleegster"],
                ["un médicament, une pharmacie, un hôpital", "een geneesmiddel, een apotheek, een ziekenhuis"],
            ]), "Les cheveux (het haar) tegenover les chevaux (de paarden): één letter verschil."),
            ("p", "Pijn zeg je met <strong>avoir mal à</strong>: <em>j'ai mal à la tête</em> "
                  "(hoofdpijn), <em>j'ai mal au ventre</em> (buikpijn), <em>j'ai mal à la "
                  "gorge</em> (keelpijn), <em>j'ai mal aux dents</em>, <em>j'ai mal au dos</em>. "
                  "Let op het lidwoord: à + le wordt <strong>au</strong>, à + les wordt "
                  "<strong>aux</strong>."),
        ]),
        dict(kop="Iemand beschrijven", blokken=[
            ("p", "<em>Il est grand.</em> <em>Elle a les cheveux blonds.</em> <em>Il est "
                  "sympathique.</em> Gestalte, haar en karakter: daarmee kan je iemand in een "
                  "tekst volgen én iemand op een foto beschrijven. Dezelfde woorden komen dus "
                  "twee keer van pas."),
            ("p", "Verder duiken in teksten vaak op: <em>il est marié</em> (hij is getrouwd, van "
                  "<em>se marier</em>), <em>elle est née en 2012</em> (ze is geboren in 2012, "
                  "van <em>naître</em>; het deelwoord krijgt een -e omdat het met être gaat)."),
        ]),
    ],
    onthoud=[
        "Je m'appelle… j'ai … ans… j'habite à… je suis belge.",
        "Leeftijd, honger, dorst, angst en pijn gaan met avoir, niet met être.",
        "le frère, la sœur, les parents, les grands-parents, un oncle, une tante.",
        "avoir mal à la tête / au ventre / à la gorge / aux dents.",
        "Nationaliteiten met een kleine letter, landen met een hoofdletter.",
        "Les cheveux = het haar. Les yeux = de ogen.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordenschat-eten-wonen-kleding-en-dagelijkse-dingen"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: eten, wonen, kleding en dagelijkse dingen",
    onder="De woorden van een gewone dag: aan tafel, in huis, aan de kleerkast en in de winkel.",
    secties=[
        dict(kop="Eten en drinken", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["le petit déjeuner / le déjeuner / le dîner", "het ontbijt / het middagmaal / het avondmaal"],
                ["le pain, une baguette", "het brood, een stokbrood"],
                ["une pomme, une pomme de terre", "een appel, een aardappel"],
                ["le fromage, la viande", "de kaas, het vlees"],
                ["l'eau, le lait, le jus d'orange", "het water, de melk, het sinaasappelsap"],
                ["la nourriture", "het voedsel, het eten"],
                ["C'est délicieux !", "Het is heerlijk!"],
            ]), "In Frankrijk is 'le déjeuner' het middagmaal, niet het ontbijt."),
            ("p", "Bestellen doe je beleefd: <em>Je voudrais une baguette, s'il vous plaît.</em> "
                  "En vragen wat iets kost: <em>Ça coûte combien ?</em> of <em>C'est combien "
                  "?</em> (<em>coûter</em> = kosten, <em>combien</em> = hoeveel)."),
        ]),
        dict(kop="Het huis: de kamers en delen van een woning", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la maison, un appartement", "het huis, een appartement"],
                ["la cuisine", "de keuken (en ook: het koken)"],
                ["la chambre", "de slaapkamer"],
                ["la salle de bains", "de badkamer"],
                ["la salle de séjour, le salon", "de woonkamer"],
                ["la salle à manger", "de eetkamer"],
                ["le jardin, un escalier, une fenêtre", "de tuin, een trap, een raam"],
                ["une table, une chaise, un lit, une armoire, un canapé", "een tafel, een stoel, een bed, een kast, een zetel"],
                ["le frigo (le réfrigérateur)", "de koelkast"],
            ]), "Un escalier is een trap: dat hoort bij het gebouw, niet bij de meubels."),
            ("p", "<strong>Faire la cuisine</strong> betekent koken, <strong>faire les "
                  "courses</strong> betekent boodschappen doen. Dat zijn vaste uitdrukkingen: "
                  "<em>une course</em> op zich is een wedloop."),
        ]),
        dict(kop="Kleding, kleuren, vormen en materialen", blokken=[
            ("fig", svg.kleurstalen([
                ("rouge", "rood", "#c0392b"), ("bleu", "blauw", "#2f6fa8"),
                ("vert", "groen", "#3f7d4f"), ("jaune", "geel", "#d8a92b"),
                ("noir", "zwart", "#23291f"), ("gris", "grijs", "#8a8f80"),
            ]), "De kleur staat in het Frans achter het naamwoord: une robe bleue, un pull bleu."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un pantalon, un jean, une robe, un pull", "een broek, een jeans, een jurk, een trui"],
                ["un manteau", "een jas of mantel"],
                ["des chaussures, des baskets, une chaussette", "schoenen, sportschoenen, een sok"],
                ["rond / carré", "rond / vierkant"],
                ["en bois, en verre, en métal, en plastique", "van hout, van glas, van metaal, van plastic"],
            ]), "'Il est en bois' betekent: hij is van hout. 'En' + materiaal zegt waarvan iets gemaakt is."),
            ("p", "Let op <em>le verre</em> (het glas) tegenover <em>le vert</em> (het groen): "
                  "ze klinken hetzelfde."),
        ]),
        dict(kop="Dagelijkse bezigheden", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["se lever", "opstaan — Je me lève à sept heures."],
                ["se laver, s'habiller", "zich wassen, zich aankleden"],
                ["se brosser les dents", "zijn tanden poetsen"],
                ["prendre le bus", "de bus nemen"],
                ["faire ses devoirs", "zijn huiswerk maken"],
                ["ranger sa chambre", "zijn kamer opruimen"],
            ]), "Die werkwoorden met 'se' zijn wederkerend: je me lève, tu te lèves, il se lève."),
        ]),
        dict(kop="Winkels en voorwerpen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la boulangerie, le boulanger", "de bakkerij, de bakker"],
                ["le marché, le supermarché", "de markt, de supermarkt"],
                ["la caisse, un client, le prix", "de kassa, een klant, de prijs"],
                ["un sac, un sac à dos", "een tas, een rugzak"],
                ["la clé (la clef)", "de sleutel"],
                ["un portefeuille, un porte-monnaie", "een portefeuille, een portemonnee"],
            ]), "Le pain koop je bij le boulanger, in la boulangerie."),
            ("weetje", "<em>Porte-monnaie</em> bestaat uit <em>porter</em> (dragen) en "
                       "<em>monnaie</em> (geld): iets dat geld draagt, dus een portemonnee. Wie "
                       "de delen van een samenstelling herkent, raadt de betekenis. Dat is "
                       "precies de leesstrategie die de vakfiche noemt."),
        ]),
    ],
    onthoud=[
        "le petit déjeuner = ontbijt, le déjeuner = middagmaal, le dîner = avondmaal.",
        "la cuisine, la chambre, la salle de bains, la salle de séjour.",
        "De kleur staat achter het naamwoord en past zich aan: une robe bleue.",
        "faire la cuisine = koken, faire les courses = boodschappen doen.",
        "Je me lève, je me lave, je m'habille, je me brosse les dents.",
        "'En' + materiaal: en bois, en verre, en métal.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordenschat-school-beroepen-sport-en-vrije-tijd"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: school, beroepen, sport en vrije tijd",
    onder="De woorden van de schooldag, van de opdracht zelf, en van wat je daarna doet.",
    secties=[
        dict(kop="Op school", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["l'école, une classe, un cours", "de school, een klas, een les"],
                ["un élève, un professeur (un prof)", "een leerling, een leerkracht"],
                ["un cahier, un livre, un cartable", "een schrift, een boek, een boekentas"],
                ["les devoirs, faire ses devoirs", "het huiswerk, zijn huiswerk maken"],
                ["la récréation", "de speeltijd"],
                ["un emploi du temps", "een lessenrooster"],
                ["une matière", "een vak (ook: stof, materie)"],
                ["la note, une bonne note", "het punt of cijfer, een goed punt"],
            ]), "Un livre (mannelijk) is een boek; une livre (vrouwelijk) is een pond."),
        ]),
        dict(kop="Instructietaal: de taal van de opdracht", blokken=[
            ("kader", "Dit is de woordenschat waar je het snelst punten mee verliest. Wie "
                      "<em>cochez</em> of <em>reliez</em> niet begrijpt, doet de verkeerde "
                      "oefening, hoe goed hij de leerstof ook kent. Daarom zet de vakfiche "
                      "instructietaal bij de woordvelden die je moet kennen."),
            ("fig", tabel(["opdracht", "wat je moet doen"], [
                ["Cochez la bonne réponse.", "Kruis het juiste antwoord aan. (cocher = aankruisen)"],
                ["Cochez la bonne case.", "Kruis het juiste vakje aan."],
                ["Complétez la phrase.", "Vul de zin aan."],
                ["Soulignez…", "Onderlijn…"],
                ["Entourez…", "Omcirkel…"],
                ["Reliez…", "Verbind wat bij elkaar hoort."],
                ["Répondez aux questions.", "Beantwoord de vragen."],
                ["Répondez en français.", "Antwoord in het Frans."],
                ["Rédigez un court texte.", "Stel een korte tekst op."],
                ["Justifiez votre réponse.", "Verantwoord je antwoord (leg uit waarom)."],
                ["Vrai ou faux ?", "Waar of niet waar?"],
            ]), "'Répondez en français': een antwoord in het Nederlands levert geen punten op, hoe juist het ook is."),
        ]),
        dict(kop="Beroepen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un métier", "een beroep — Quel est ton métier ?"],
                ["un boulanger", "een bakker"],
                ["une infirmière / un infirmier", "een verpleegster / een verpleger"],
                ["un facteur", "een postbode"],
                ["un vendeur / une vendeuse", "een verkoper / een verkoopster"],
                ["un médecin, un pharmacien", "een arts, een apotheker"],
                ["travailler dans un bureau", "op een kantoor werken"],
            ]), "Un bureau is zowel het kantoor als het meubel; de zin eromheen beslist."),
        ]),
        dict(kop="Sport en vrije tijd", blokken=[
            ("kader", "<strong>Jouer à</strong> bij een sport, <strong>jouer de</strong> bij een "
                      "muziekinstrument: <em>je joue au football</em>, <em>je joue au tennis</em>, "
                      "maar <em>je joue du piano</em>. Dat verschil is een klassieke valkuil."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["la natation, nager", "het zwemmen, zwemmen"],
                ["le vélo, le basket, le football", "het fietsen, het basketbal, het voetbal"],
                ["la marche, la lecture", "het wandelen, het lezen"],
                ["une équipe, un match, l'entraînement, s'entraîner", "een ploeg, een wedstrijd, de training, trainen"],
                ["gagner / perdre", "winnen / verliezen"],
                ["faire partie d'un club", "lid zijn van een club"],
                ["mon temps libre, un passe-temps", "mijn vrije tijd, een hobby"],
                ["un spectacle", "een voorstelling"],
                ["s'intéresser à", "zich interesseren voor — Je m'intéresse à la musique."],
            ]), "'J'ai perdu mes clés' betekent dat je je sleutels kwijt bent: perdre is ook 'kwijtraken'."),
            ("p", "<em>Quel est ton passe-temps préféré ?</em> is 'wat is je favoriete "
                  "tijdverdrijf?'. <em>Préféré</em> betekent favoriet, en dat woord komt ook "
                  "terug in <em>ma matière préférée</em>, mijn lievelingsvak."),
        ]),
        dict(kop="Communicatie en multimedia", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un ordinateur, un portable", "een computer, een gsm of een laptop"],
                ["un écran, une application", "een scherm, een app"],
                ["un mot de passe", "een wachtwoord"],
                ["envoyer un message", "een bericht sturen"],
                ["télécharger", "downloaden"],
                ["un réseau social", "een sociaal netwerk"],
            ]), "Op een réseau social reageer je op een discussie: dat is een van de schrijfopdrachten uit de fiche."),
        ]),
    ],
    onthoud=[
        "Cochez, complétez, soulignez, entourez, reliez, justifiez: lees de opdracht.",
        "Répondez en français — anders krijg je geen punten.",
        "l'école, un élève, un cahier, les devoirs, la récréation.",
        "un métier: boulanger, infirmière, facteur, vendeur, médecin.",
        "jouer au football, maar jouer du piano.",
        "gagner = winnen, perdre = verliezen (en ook kwijtraken).",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordenschat-getallen-tijd-weer-reizen-en-landen"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordenschat: getallen, tijd, weer, reizen en landen",
    onder="De gegevens waar leesvragen het vaakst naar vragen: hoeveel, wanneer en waar.",
    secties=[
        dict(kop="De getallen", blokken=[
            ("p", "Het Franse telsysteem doet boven de zestig iets bijzonders. "
                  "<strong>Soixante-dix</strong> is 60 + 10 = 70. <strong>Quatre-vingts</strong> "
                  "is letterlijk 'vier twintigen', dus 4 x 20 = 80. En "
                  "<strong>quatre-vingt-dix-sept</strong> is 80 + 10 + 7 = 97. In België hoor "
                  "je ook <em>septante</em> en <em>nonante</em>, maar op het examen staat de "
                  "Franse vorm."),
            ("fig", tabel(["Frans", "getal"], [
                ["douze", "12"],
                ["quinze", "15"],
                ["soixante", "60"],
                ["soixante-dix", "70"],
                ["quatre-vingts", "80"],
                ["quatre-vingt-dix-sept", "97"],
                ["cent", "100"],
                ["mille", "1000"],
            ]), "De vakfiche noemt 15, 80 en 100 uitdrukkelijk als voorbeelden."),
            ("p", "Naast die <strong>hoofdtelwoorden</strong> heb je de "
                  "<strong>rangtelwoorden</strong>: <em>premier</em> (de eerste), "
                  "<em>deuxième</em> (de tweede), <em>troisième</em> (de derde), "
                  "<em>dernier</em> (de laatste). <em>La deuxième fois</em> is 'de tweede keer'; "
                  "<em>deux fois</em> zou 'twee keer' betekenen."),
        ]),
        dict(kop="Hoeveelheden en maten", blokken=[
            ("kader", "Na een hoeveelheid staat in het Frans alleen <strong>de</strong>, zonder "
                      "lidwoord: <em>un kilo de pommes</em>, <em>un litre de lait</em>, "
                      "<em>beaucoup de travail</em>, <em>un peu de sucre</em>, <em>assez de "
                      "temps</em>."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["un kilo de pommes, un litre de lait", "een kilo appels, een liter melk"],
                ["beaucoup de, un peu de, assez de", "veel, een beetje, genoeg"],
                ["environ", "ongeveer"],
                ["la moitié, la plupart", "de helft, de meeste"],
                ["plus de, moins de", "meer dan, minder dan"],
            ]), "'La plupart des élèves' is niet 'tous les élèves'."),
        ]),
        dict(kop="Dagen, maanden, seizoenen en feesten", blokken=[
            ("fig", tabel(["soort", "Frans"], [
                ["dagen", "lundi (maandag), mardi, mercredi, jeudi, vendredi, samedi, dimanche (zondag)"],
                ["maanden", "janvier, février, mars, avril, mai, juin, juillet, août, septembre, octobre, novembre, décembre"],
                ["seizoenen", "le printemps (lente), l'été (zomer), l'automne (herfst), l'hiver (winter)"],
                ["feesten", "Noël (Kerstmis), Pâques (Pasen), le Nouvel An (Nieuwjaar)"],
            ]), "Juin en juillet lijken sterk op elkaar: juni en juli."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["hier, aujourd'hui, demain, après-demain", "gisteren, vandaag, morgen, overmorgen"],
                ["la semaine prochaine", "volgende week"],
            ]), "'Là-bas' betekent daarginds: dat is een plaats, geen tijd."),
        ]),
        dict(kop="Hoe laat is het?", blokken=[
            ("fig", svg.klok(8, 30),
             "Il est huit heures et demie — en dat is in het Nederlands halfnegen."),
            ("kader", "Hier gaat het vaak mis. Het Frans telt <strong>door vanaf het voorbije "
                      "uur</strong>, het Nederlands telt <strong>naar het volgende toe</strong>. "
                      "<em>Huit heures et demie</em> is dus halfnegen, niet halfacht."),
            ("fig", tabel(["Frans", "Nederlands"], [
                ["Il est huit heures.", "Het is acht uur."],
                ["Il est huit heures et quart.", "Het is kwart over acht."],
                ["Il est huit heures et demie.", "Het is halfnegen."],
                ["Il est sept heures moins le quart.", "Het is kwart voor zeven."],
                ["Il est midi / minuit.", "Het is twaalf uur 's middags / middernacht."],
                ["à partir de 14 h / jusqu'à 14 h", "vanaf 14 uur / tot 14 uur"],
            ]), "Voor het uur gebruik je 'il est', voor het weer 'il fait'."),
        ]),
        dict(kop="Het weer", blokken=[
            ("p", "Over het weer zeg je <strong>il fait</strong>, niet 'il est': <em>il fait "
                  "beau</em>, <em>il fait chaud</em>, <em>il fait froid</em>, <em>il fait du "
                  "vent</em>. Daarnaast: <em>il pleut</em> (het regent), <em>il neige</em> (het "
                  "sneeuwt), <em>il y a du soleil</em> (het is zonnig), <em>il y a des "
                  "nuages</em> (het is bewolkt)."),
            ("weetje", "<em>Le temps</em> betekent zowel 'het weer' als 'de tijd'. "
                       "<em>Quel temps fait-il ?</em> gaat over het weer, <em>je n'ai pas le "
                       "temps</em> over tijd. De zin eromheen beslist."),
        ]),
        dict(kop="Reizen en landen", blokken=[
            ("fig", tabel(["Frans", "Nederlands"], [
                ["les vacances", "de vakantie (altijd meervoud)"],
                ["le train, l'avion, le vélo, la voiture", "de trein, het vliegtuig, de fiets, de auto"],
                ["la gare, le quai, un billet, l'horaire", "het station, het perron, een ticket, de dienstregeling"],
                ["un aller-retour / un aller simple", "een heen-en-terugticket / een enkele reis"],
                ["la plage", "het strand"],
                ["la France, la Belgique", "Frankrijk, België — le français is de taal, une Française een Française"],
            ]), "La gare is de plaats waar je op de trein stapt, niet het vervoermiddel zelf."),
            ("kader", "<strong>En</strong> + vervoermiddel: <em>en train</em>, <em>en "
                      "voiture</em>, <em>en avion</em> — maar te voet is <em>à pied</em>. "
                      "<strong>À</strong> + stad: <em>à Bruxelles</em>, <em>à Paris</em>. "
                      "<strong>En</strong> + vrouwelijk land: <em>en France</em>, <em>en "
                      "Belgique</em>; <strong>au</strong> + mannelijk land: <em>au Canada</em>. "
                      "En <em>venir de</em> betekent 'afkomstig zijn uit': <em>je viens de "
                      "Belgique</em>."),
        ]),
    ],
    onthoud=[
        "quinze = 15, soixante-dix = 70, quatre-vingts = 80, cent = 100.",
        "Na een hoeveelheid staat alleen 'de': un kilo de pommes.",
        "Il est … heures voor het uur, il fait … voor het weer.",
        "Huit heures et demie is halfnegen, niet halfacht.",
        "en train, à pied, à Bruxelles, en France, au Canada.",
        "Leesvragen gaan vaak net over een uur, een prijs of een datum.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["grammatica-lidwoorden-naamwoorden-en-voornaamwoorden"] = dict(
    vak=VAK, niveau=SPARK, titel="Grammatica: lidwoorden, naamwoorden en voornaamwoorden",
    onder="Le, la, les, du, mon, ce en lui: de kleine woordjes waar alles van afhangt.",
    secties=[
        dict(kop="Elk naamwoord heeft een geslacht", blokken=[
            ("p", "In het Frans is elk <strong>zelfstandig naamwoord</strong> (un <em>substantif</em>) "
                  "<strong>mannelijk</strong> (<em>masculin</em>) of <strong>vrouwelijk</strong> "
                  "(<em>féminin</em>), en dat moet je meeleren met het woord. Het "
                  "bepaalt het <strong>lidwoord</strong> én de vorm van het "
                  "<strong>bijvoeglijk naamwoord</strong>: <em>un petit livre</em> tegenover "
                  "<em>une petite table</em>."),
            ("fig", tabel(["soort lidwoord (article)", "mannelijk", "vrouwelijk", "meervoud"], [
                ["bepaald (défini) — de, het", "le livre", "la table", "les livres"],
                ["onbepaald (indéfini) — een", "un livre", "une table", "des livres"],
                ["deelaanduidend (partitif) — een deel van", "du pain", "de la soupe", "des légumes"],
            ]), "La table is de tafel, le livre het boek. Voor een klinker wordt le of la gewoon l': l'école, l'eau."),
            ("p", "Het <strong>deelaanduidend</strong> lidwoord gebruik je voor een onbepaalde "
                  "hoeveelheid: <em>je bois de l'eau</em> (ik drink water), <em>je mange du "
                  "pain</em>. 'Je bois l'eau' zou over één bepaald glas water gaan."),
            ("kader", "In het Nederlands zeg je gewoon 'boeken'; in het Frans <strong>moet</strong> "
                      "daar <em>des livres</em> staan. Dat lidwoord vergeten is een van de "
                      "meestgemaakte fouten."),
            ("p", "Enkelvoud heet in het Frans <em>singulier</em>, meervoud <em>pluriel</em>. "
                  "Het <strong>meervoud</strong> krijgt een -s, maar die hoor je meestal niet: "
                  "<em>livre</em> en <em>livres</em> klinken hetzelfde. Je hoort het meervoud "
                  "aan het lidwoord: <em>le</em> tegenover <em>les</em>."),
        ]),
        dict(kop="Samengetrokken lidwoorden (articles contractés)", blokken=[
            ("fig", svg.woordvolgorde([
                ("à + le", "au", svg.FOREST),
                ("à + les", "aux", svg.FOREST),
                ("de + le", "du", svg.AMBER),
                ("de + les", "des", svg.AMBER),
            ]), "Bij la en l' verandert er niets: à la gare, de la soupe, de l'eau."),
            ("p", "Daarom is het <em>j'ai mal <strong>au</strong> ventre</em> en <em>j'ai mal "
                  "<strong>aux</strong> dents</em>. 'De le' en 'à le' bestaan niet."),
        ]),
        dict(kop="Wanneer het lidwoord 'de' wordt", blokken=[
            ("fig", tabel(["situatie", "voorbeeld"], [
                ["na een hoeveelheid", "beaucoup <strong>de</strong> travail, un litre <strong>de</strong> lait, un kilo <strong>de</strong> pommes"],
                ["na een ontkenning", "Je n'ai pas <strong>de</strong> frère. Je ne bois pas <strong>de</strong> lait. Je ne mange plus <strong>de</strong> viande."],
            ]), "Je bois du lait wordt je ne bois pas de lait: un, une, du, de la en des worden allemaal 'de'."),
        ]),
        dict(kop="Déterminants: mijn, deze, welke", blokken=[
            ("fig", tabel(["soort", "vormen", "voorbeeld"], [
                ["bezittelijk (possessif)", "mon, ma, mes / ton, ta, tes / son, sa, ses", "mon livre, ma sœur (mijn zus), ma sœur s'appelle Léa, mes parents"],
                ["aanwijzend (démonstratif)", "ce, cet, cette, ces", "ce livre (dit boek), cette table, ces enfants"],
                ["vragend (interrogatif)", "quel, quelle, quels, quelles", "Quel livre ? Quelle heure est-il ?"],
            ]), "Sœur is vrouwelijk enkelvoud, dus ma sœur; heure is vrouwelijk, dus quelle heure."),
            ("weetje", "Begint een vrouwelijk woord met een klinker, dan schrijf je toch "
                       "<em>mon</em>: <em>mon amie</em>, <em>mon école</em>. Dat is alleen voor "
                       "de klank. Staat er een bijvoeglijk naamwoord tussen dat met een "
                       "medeklinker begint, dan is het weer <em>ma</em>: <em>ma meilleure "
                       "amie</em>."),
        ]),
        dict(kop="De bijvoeglijke naamwoorden (adjectifs)", blokken=[
            ("p", "Ze passen zich aan in <strong>geslacht</strong> en <strong>getal</strong>: "
                  "<em>une robe verte</em> (een groene jurk), <em>des robes vertes</em>, <em>un pull vert</em>, "
                  "<em>des pulls verts</em>. En anders dan in het Nederlands staan ze "
                  "<strong>achter</strong> het naamwoord: <em>une voiture rouge</em>."),
            ("p", "Een kleine groep korte, veelgebruikte woorden staat wél <strong>vóór</strong> "
                  "het naamwoord: <em>petit</em>, <em>grand</em>, <em>jeune</em>, <em>beau</em>, "
                  "<em>bon</em> — <em>un petit garçon</em>, <em>une grande maison</em>, <em>un "
                  "jeune homme</em>. Kleuren staan altijd achteraan."),
            ("fig", tabel(["trap", "vorm", "voorbeeld"], [
                ["vergrotende trap (comparatif)", "plus … que / moins … que", "Il est plus grand que moi. (groter dan ik)"],
                ["overtreffende trap (superlatif)", "le / la / les plus …", "C'est le plus grand de la classe."],
                ["onregelmatig", "bon → meilleur → le meilleur", "C'est ma meilleure amie. (mijn beste vriendin)"],
            ]), "'Plus bon' bestaat niet: dat is meilleur. Let op de vorm: les belles maisons, les beaux livres."),
        ]),
        dict(kop="De telwoorden", blokken=[
            ("p", "De fiche vraagt de frequente <strong>hoofdtelwoorden</strong> (<em>nombres "
                  "cardinaux</em>: quinze, quatre-vingts, cent) en <strong>rangtelwoorden</strong> "
                  "(<em>nombres ordinaux</em>): <em>premier</em> "
                  "(de eerste), <em>deuxième</em> (de tweede), <em>troisième</em> (de derde), "
                  "<em>dernier</em> (de laatste). <em>La deuxième fois</em> is 'de tweede "
                  "keer'; <em>deux fois</em> zou 'twee keer' betekenen. De getallen zelf staan "
                  "in de bundel over getallen, tijd en weer."),
        ]),
        dict(kop="De voornaamwoorden (pronoms)", blokken=[
            ("p", "Een <strong>persoonlijk voornaamwoord</strong> heet in het Frans een "
                  "<em>pronom personnel</em>. Het kan onderwerp zijn, lijdend voorwerp of "
                  "meewerkend voorwerp, en elk van die drie heeft zijn eigen rijtje."),
            ("fig", tabel(["soort", "vormen", "voorbeeld"], [
                ["onderwerp (sujet)", "je, tu, il, elle, nous, vous, ils, elles", "Nous regardons la télé."],
                ["lijdend voorwerp (COD)", "me, te, le, la, nous, vous, les", "Je vois Marie → Je <strong>la</strong> vois."],
                ["meewerkend voorwerp (COI)", "me, te, lui, nous, vous, leur", "Je parle à Paul → Je <strong>lui</strong> parle."],
                ["wederkerend (réfléchi)", "me, te, se, nous, vous, se", "Je <strong>me</strong> lave les mains. (ik was mijn handen)"],
            ]), "Staat er 'à' voor de persoon, dan is het een COI: lui of leur."),
            ("fig", svg.voornaamwoordplaats(),
             "In het Frans staat het voorwerp vóór het werkwoord: je la vois, je te parle, il nous aide."),
            ("p", "Bij een <strong>wederkerend werkwoord</strong> (<em>verbe pronominal</em>) verwijst het voornaamwoord "
                  "naar het onderwerp zelf: <em>je me lève</em>, <em>tu te couches</em>, "
                  "<em>elle s'habille</em>. Bij <em>je te vois</em> gaat het net om iemand "
                  "anders."),
            ("p", "En je moet altijd <strong>weten waarnaar een voornaamwoord verwijst</strong>. "
                  "Dat staat zo in de vakfiche: anders begrijp je de samenhang tussen de zinnen "
                  "niet, en dus de tekst niet."),
        ]),
    ],
    onthoud=[
        "le / la / les — un / une / des — du / de la / des.",
        "à + le = au, à + les = aux, de + le = du, de + les = des.",
        "Na een hoeveelheid en na een ontkenning: alleen 'de'.",
        "mon, ma, mes / ce, cette, ces / quel, quelle.",
        "Bijvoeglijke naamwoorden staan meestal achter het naamwoord en passen zich aan.",
        "Het voorwerp staat vóór het werkwoord: je la vois, je lui parle.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["grammatica-werkwoorden-tijden-en-zinsbouw"] = dict(
    vak=VAK, niveau=SPARK, titel="Grammatica: werkwoorden, tijden en zinsbouw",
    onder="Aller, allez of allé? En hoe je van een zin een vraag of een ontkenning maakt.",
    secties=[
        dict(kop="Drie vormen die hetzelfde klinken", blokken=[
            ("fig", svg.woordvolgorde([
                ("infinitief", "aller", svg.FOREST),
                ("persoonsvorm", "allez", svg.AMBER),
                ("voltooid deelwoord", "allé", svg.DARK),
            ]), "Ze klinken hetzelfde en zien er anders uit. Je moet aan de zin zien welke je nodig hebt."),
            ("p", "De <strong>infinitief</strong> (<em>infinitif</em>) is het hele werkwoord: <em>aller</em>. De "
                  "<strong>persoonsvorm</strong> hoort bij een onderwerp: <em>vous allez</em>. "
                  "Het <strong>voltooid deelwoord</strong> hoort bij hebben of zijn: <em>je "
                  "suis allé</em>. De vakfiche noemt precies dit voorbeeld: je moet het "
                  "onderscheid kennen om te weten hoe je de werkwoordsvorm correct moet "
                  "interpreteren of schrijven."),
        ]),
        dict(kop="De tegenwoordige tijd", blokken=[
            ("fig", svg.persoonsvormen([
                ("je", "parle", svg.FOREST),
                ("tu", "parles", svg.FOREST),
                ("il|elle|on", "parle", svg.FOREST),
                ("nous", "parlons", svg.AMBER),
                ("vous", "parlez", svg.AMBER),
                ("ils|elles", "parlent", svg.AMBER),
            ]), "Parler betekent spreken. Werkwoorden op -er krijgen -e, -es, -e, -ons, -ez, -ent; nous krijgt bijna altijd -ons."),
            ("fig", tabel(["être (zijn)", "avoir (hebben)", "aller (gaan)"], [
                ["je suis", "j'ai", "je vais"],
                ["tu es", "tu as", "tu vas"],
                ["il est", "il a", "il va"],
                ["nous sommes", "nous avons", "nous allons"],
                ["vous êtes", "vous avez", "vous allez"],
                ["ils sont", "ils ont", "ils vont"],
            ]), "Deze drie onregelmatige werkwoorden heb je overal nodig: leer ze uit het hoofd."),
            ("p", "De fiche maakt het onderscheid tussen <strong>regelmatige</strong> en <strong>frequente onregelmatige werkwoorden</strong> (<em>verbes réguliers et irréguliers</em>). Regelmatig zijn de werkwoorden op -er, zoals <em>parler</em>: die volgen allemaal hetzelfde rijtje. Onregelmatig zijn <em>être</em>, <em>avoir</em>, <em>aller</em>, <em>venir</em> en <em>faire</em>: die leer je één voor één."),
        ]),
        dict(kop="De tijden op een rij", blokken=[
            ("fig", svg.franse_tijden(),
             "Vier tijden rond het nu, plus het présent in het midden."),
            ("fig", tabel(["tijd", "hoe je ze maakt", "voorbeeld"], [
                ["indicatif présent", "de vervoegde vorm", "je mange"],
                ["passé composé", "het hulpwerkwoord avoir of être + voltooid deelwoord", "j'ai mangé, je suis allé, elle est allée au cinéma (naar de film)"],
                ["imparfait", "de stam + -ais, -ais, -ait, -ions, -iez, -aient", "je mangeais"],
                ["futur proche", "aller + infinitief", "je vais manger"],
                ["passé récent", "venir de + infinitief", "je viens de manger (ik heb net gegeten)"],
                ["impératif — de gebiedende wijs", "het werkwoord zonder onderwerp", "Ferme la porte ! (doe de deur dicht) Écoutez ! Viens ici ! Regardons ensemble !"],
                ["conditionnel de politesse", "de beleefde vorm", "je voudrais, pourriez-vous (beleefder dan pouvez-vous)"],
            ]), "'Je voudrais' met -s is beleefd; 'je voudrai' zonder -s is de toekomende tijd."),
            ("p", "Het verschil tussen <strong>imparfait</strong> en <strong>passé "
                  "composé</strong>: de imparfait beschrijft een <em>gewoonte of een "
                  "toestand</em> die een tijd duurde — <em>'Quand j'étais petit, j'habitais à "
                  "Liège'</em> — en de passé composé <em>één afgeronde gebeurtenis</em>: "
                  "<em>'Hier, j'ai mangé une pizza.'</em>"),
        ]),
        dict(kop="Avoir of être in de verleden tijd", blokken=[
            ("kader", "Werkwoorden van <strong>beweging en verandering</strong> — aller, venir, "
                      "partir, arriver, naître — gaan met <strong>être</strong>. En dan past het "
                      "voltooid deelwoord zich aan het <strong>onderwerp</strong> aan: "
                      "<em>il est parti</em>, <em>elle est partie</em>, <em>ils sont partis</em>, "
                      "<em>elles sont parties</em>. Met <strong>avoir</strong> gebeurt dat niet: "
                      "<em>j'ai mangé</em>, <em>elle a mangé</em>."),
            ("p", "<strong>Wederkerende werkwoorden</strong> (<em>verbes pronominaux</em>) gaan altijd met être, en het "
                  "wederkerend voornaamwoord blijft staan: <em>nous nous sommes levés tôt</em>, "
                  "<em>elle s'est lavée</em>."),
        ]),
        dict(kop="Soorten zinnen", blokken=[
            ("fig", tabel(["zinssoort", "voorbeeld"], [
                ["mededelend (déclarative)", "Tu viens."],
                ["vragend (interrogative)", "Est-ce que tu viens ? / Viens-tu ?"],
                ["bevelend (impérative)", "Viens ici !"],
                ["uitroepend (exclamative)", "Quelle belle journée ! (wat een mooie dag)"],
                ["ontkennend (négative)", "Je ne viens pas."],
                ["bevestigend (affirmative)", "Oui, je viens."],
            ]), "Van een gewone zin maak je een vraagzin door om te draaien (de inversie): je zet de persoonsvorm voorop met een streepje. Viens-tu ? Parlez-vous français ?"),
            ("p", "De <strong>ontkenning</strong> bestaat uit twee delen rond het werkwoord: "
                  "<strong>ne … pas</strong>. Voor een klinker wordt ne → n': <em>je n'aime "
                  "pas</em>. Er zijn varianten: <strong>ne … jamais</strong> (nooit) en "
                  "<strong>ne … plus</strong> (niet meer). <em>Je ne mange plus de viande</em> "
                  "betekent 'ik eet geen vlees meer' — en let ook daar op het lidwoord: 'de la "
                  "viande' wordt 'de viande'."),
            ("p", "Een <strong>enkelvoudige zin</strong> heeft één persoonsvorm: <em>je mange "
                  "une pomme</em>, <em>je bois du café</em>. Een <strong>samengestelde "
                  "zin</strong> heeft er twee of meer: <em>il pleut, donc je reste ici</em>, "
                  "<em>je sais que tu viens</em>, <em>elle chante et il danse</em>, <em>quand il "
                  "pleut, je reste à la maison</em>."),
            ("p", "Variëren tussen soorten zinnen maakt je tekst <strong>levendig</strong>. "
                  "Dat vraagt de vakfiche uitdrukkelijk."),
        ]),
        dict(kop="Voegwoorden, voorzetsels en congruentie", blokken=[
            ("fig", tabel(["soort", "voorbeelden"], [
                ["nevenschikkende voegwoorden (conjonctions)", "et, mais, ou, donc, alors, ensuite"],
                ["onderschikkende voegwoorden", "parce que, que, quand, bien que"],
                ["frequente voorzetsels (prépositions)", "à (à Bruxelles), en (en train, il travaille en Belgique), de, sur, dans, avec"],
            ]), "Een nevenschikkend voegwoord verbindt gelijkwaardige delen; een onderschikkend maakt er een bijzin van."),
            ("fig", tabel(["wat het voegwoord aangeeft", "voorbeelden"], [
                ["chronologisch verloop", "d'abord, ensuite, puis, enfin, alors"],
                ["opsomming", "et, aussi, en plus"],
                ["oorzaak", "parce que, car, donc"],
                ["tegenstelling", "mais, pourtant"],
            ]), "De fiche noemt precies die vier: chronologisch verloop, opsomming, oorzaak en tegenstelling."),
            ("p", "De <strong>overeenkomst</strong> (accord) tussen onderwerp en persoonsvorm is "
                  "vooral een <em>schrijfregel</em>: <em>il joue</em> en <em>ils jouent</em> "
                  "klinken hetzelfde, maar je schrijft ze anders. <em>Les enfants "
                  "<strong>jouent</strong> dans le jardin</em> — derde persoon meervoud, dus "
                  "-ent."),
            ("p", "Diezelfde overeenkomst geldt tussen een <strong>zelfstandig naamwoord of voornaamwoord en het bijvoeglijk naamwoord</strong> — <em>une robe verte</em>, <em>des robes vertes</em> — en bij het <strong>voltooid deelwoord met être</strong>: <em>elle est partie</em>. Ook die twee staan in de fiche."),
        ]),
        dict(kop="Klank en schriftbeeld", blokken=[
            ("p", "De fiche vraagt ook dat je de <strong>relatie tussen klank- en schriftbeeld</strong> kent en de <strong>spelling van frequente woorden</strong> beheerst. Dat merk je vooral bij het schrijven: <em>il joue</em>, <em>ils jouent</em>, <em>parler</em>, <em>parlez</em> en <em>parlé</em> klinken hetzelfde en schrijf je anders. Wie alleen op zijn oor afgaat, schrijft de verkeerde vorm."),
            ("p", "Let bij het schrijven op de <strong>accenten</strong>: <em>é</em> (é fermé, zoals in <em>parlé</em>), <em>è</em> (zoals in <em>père</em>), <em>ê</em> (zoals in <em>être</em>) en de cédille in <em>ça</em> en <em>français</em>. Een accent vergeten is een spelfout, net zoals een vergeten -s."),
            ("weetje", "De <strong>uitspraak</strong> zelf — klanken, woordklemtoon, articulatie en intonatie — hoort bij de onderdelen luisteren en spreken van het examen. Die oefen je hier niet: daar heb je geluid en een gesprekspartner voor nodig."),
        ]),
    ],
    onthoud=[
        "aller (infinitief), allez (persoonsvorm), allé (deelwoord): dezelfde klank.",
        "être, avoir en aller ken je uit het hoofd.",
        "Passé composé = avoir of être + deelwoord. Met être past het deelwoord zich aan.",
        "futur proche = aller + infinitief. passé récent = venir de + infinitief.",
        "Imparfait = gewoonte of toestand; passé composé = één afgeronde gebeurtenis.",
        "Ontkennen doe je met ne … pas rond het werkwoord.",
    ],
)
