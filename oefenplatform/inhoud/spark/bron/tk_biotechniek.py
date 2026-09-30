# -*- coding: utf-8 -*-
"""De vragen voor "Biotechnische systemen" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Technische systemen —
biotechnisch systeem": biochemische processen in de voedingsindustrie, de taken
van het FAVV, de conservering van voedingsmiddelen, het etiket, de verpakkingen
en hun duurzaamheid.

Deel 1 gaat over micro-organismen in de voedingsproductie, over het FAVV, en
over de bewaartechnieken van de fiche en wat ze doen met de groei van bacteriën
en schimmels.
Deel 2 gaat over het etiket, de functies en de eigenschappen van verpakkingen,
de pictogrammen van bijlage 1, en duurzaam omgaan met voedsel en verpakkingen.

Twee dingen die de fiche uit elkaar houdt en die hier elk hun eigen vraag
krijgen: "ten minste houdbaar tot" gaat over kwaliteit, "te gebruiken tot" over
veiligheid. En koelen remt bacteriën af, invriezen legt ze zo goed als stil;
geen van beide doodt ze.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke micro-organismen noemt de vakfiche?",
        opties=["Bacteriën", "Schimmels", "Gisten", "Insecten", "Regenwormen"],
        antwoord=[0, 1, 2],
        uitleg="Micro-organismen zijn zo klein dat je ze niet met het blote oog ziet. Insecten en wormen zijn gewoon kleine dieren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk micro-organisme zorgt ervoor dat brooddeeg rijst?",
        opties=[
            "Gist",
            "Een schimmel op de korst",
            "Een bacterie uit verse melk",
            "Een virus dat in het meel zit",
        ],
        antwoord=0,
        uitleg="Gist eet de suikers in het deeg op en maakt daarbij koolstofdioxide. Die gasbelletjes doen het deeg rijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wordt melk yoghurt?",
        opties=[
            "Bacteriën zetten de melksuiker om",
            "Schimmels eten het vet uit de melk op",
            "De melk wordt gekookt en daarna gezeefd",
            "De melk wordt met veel suiker geklopt",
        ],
        antwoord=0,
        uitleg="Melkzuurbacteriën maken van de melksuiker melkzuur. Daardoor wordt de melk zuur en dik.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het maken van kaas komt er geen enkel micro-organisme aan te pas.",
        antwoord=False,
        uitleg="Kaas wordt juist gemaakt met bacteriën, en bij sommige soorten ook met schimmels. Denk aan de blauwe aders in blauwe kaas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij het maken van zuurkool?",
        opties=[
            "Bacteriën fermenteren de kool",
            "De kool wordt in de zon gedroogd",
            "De kool wordt met stralen behandeld",
            "De kool wordt diep ingevroren bewaard",
        ],
        antwoord=0,
        uitleg="Melkzuurbacteriën zetten de suikers in de kool om in melkzuur. Dat maakt de kool zuur, en zuur houdt bederf tegen.",
    ),
    dict(
        type="invultekst",
        vraag="De afkorting van het Federaal Agentschap voor de veiligheid van de voedselketen is ___.",
        antwoord="FAVV",
        uitleg="Het FAVV waakt over alles wat met ons voedsel gebeurt, van het veld tot in de winkel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van het FAVV?",
        opties=[
            "Waken over de veiligheid van ons voedsel",
            "De prijzen in de winkel vastleggen",
            "Recepten bedenken voor de fabrikanten",
            "Landbouwers hun subsidies uitbetalen",
        ],
        antwoord=0,
        uitleg="Het FAVV controleert, waarschuwt en kan producten uit de handel halen. Over prijzen en recepten gaat het niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het FAVV controleert winkels, restaurants en voedingsbedrijven.",
        antwoord=True,
        uitleg="De hele voedselketen valt eronder: de boerderij, de fabriek, de winkel en de keuken van een restaurant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn bewaartechnieken?",
        opties=["Pekelen", "Roken", "Invriezen", "Schuren", "Lakken"],
        antwoord=[0, 1, 2],
        uitleg="Schuren en lakken zijn afwerkingstechnieken voor een werkstuk. Met voedsel hebben ze niets te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet invriezen met bacteriën?",
        opties=[
            "Het legt hun groei zo goed als stil",
            "Het doodt ze allemaal in één keer",
            "Het laat ze juist sneller groeien",
            "Het verandert ze in gewone gisten",
        ],
        antwoord=0,
        uitleg="Bij vriestemperatuur kunnen bacteriën zich niet meer vermenigvuldigen. Ze zijn niet dood: na het ontdooien gaan ze weer verder.",
    ),
    dict(
        type="waarofniet",
        vraag="Pasteuriseren en steriliseren zijn allebei bewaartechnieken met warmte.",
        antwoord=True,
        uitleg="Pasteuriseren verhit korter en minder heet, steriliseren langer en heter. Hoe heter, hoe langer het product houdbaar blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent UHT op een pak melk?",
        opties=[
            "De melk is heel kort heel sterk verhit",
            "De melk is een tijd diepgevroren geweest",
            "De melk is met veel zout bewaard gebleven",
            "De melk is boven een houtvuur gerookt",
        ],
        antwoord=0,
        uitleg="UHT staat voor ultrahoge temperatuur. Daardoor blijft het pak maanden goed zonder koelkast, tot je het opent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft gedroogd fruit lang goed?",
        opties=[
            "Zonder water kunnen bacteriën niet groeien",
            "Droog fruit is te hard geworden voor bacteriën",
            "Bij het drogen gaan alle bacteriën meteen dood",
            "Droog fruit wordt vanzelf zuur en dus veilig",
        ],
        antwoord=0,
        uitleg="Bacteriën en schimmels hebben vocht nodig. Haal je het water weg, dan valt hun groei stil.",
    ),
    dict(
        type="waarofniet",
        vraag="Vacuüm verpakken voegt juist lucht toe aan de verpakking.",
        antwoord=False,
        uitleg="Vacuüm verpakken zuigt de lucht er net uit. Zonder zuurstof kunnen veel bacteriën en schimmels niet groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is pekelen?",
        opties=[
            "Voedsel bewaren in een zoute oplossing",
            "Voedsel bewaren in de diepvriezer",
            "Voedsel bewaren boven een houtvuur",
            "Voedsel bewaren in een hete oven",
        ],
        antwoord=0,
        uitleg="Zout onttrekt water aan het voedsel én aan de bacteriën. Daardoor kunnen die niet meer groeien.",
    ),
    dict(
        type="waarofniet",
        vraag="Fermenteren is een bewaartechniek waarbij micro-organismen het werk doen.",
        antwoord=True,
        uitleg="Bij zuurkool, yoghurt en kaas laten we bacteriën of gisten met opzet hun gang gaan. Zij maken het product zuur, en zuur houdt bederf tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij wecken?",
        opties=[
            "Voedsel wordt in een gesloten pot verhit",
            "Voedsel wordt aan de open lucht gedroogd",
            "Voedsel wordt met sterke stralen behandeld",
            "Voedsel wordt met wat alcohol besprenkeld",
        ],
        antwoord=0,
        uitleg="De pot gaat dicht en dan de warmte in. De micro-organismen gaan dood en er kan niets nieuws bij, want de pot blijft gesloten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bewaartechnieken werken met warmte?",
        opties=["Pasteuriseren", "Steriliseren", "UHT", "Invriezen", "Koelen"],
        antwoord=[0, 1, 2],
        uitleg="Die drie verhitten het product. Koelen en invriezen doen net het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Koelen en invriezen zijn precies hetzelfde.",
        antwoord=False,
        uitleg="Koelen remt bacteriën af, invriezen legt ze zo goed als stil. Daarom blijft iets in de diepvries veel langer goed dan in de koelkast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt vlees gerookt?",
        opties=[
            "De rook remt bacteriën en geeft smaak",
            "De rook maakt het vlees veel zachter",
            "De rook maakt het vlees een stuk zwaarder",
            "De rook vervangt het zout in de bereiding",
        ],
        antwoord=0,
        uitleg="In rook zitten stoffen die bacteriën tegenhouden, en het vlees droogt er ook wat door uit. Roken en zouten gaan trouwens vaak samen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat moet er op het etiket van een voedingsmiddel staan?",
        opties=[
            "De ingrediëntenlijst",
            "De allergenen",
            "De houdbaarheidsdatum",
            "De naam van de winkel",
            "De naam van wie het koopt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt ook de voedingswaarde, het nettogewicht, de bewaarvoorschriften en de naam van de fabrikant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'ten minste houdbaar tot' op een verpakking?",
        opties=[
            "Daarna kan de kwaliteit minder worden",
            "Daarna is het product altijd gevaarlijk",
            "Daarna moet je het meteen weggooien",
            "Daarvoor mag je het nog niet opeten",
        ],
        antwoord=0,
        uitleg="Het gaat over kwaliteit, niet over veiligheid. Koekjes van een dag over datum zijn misschien wat minder krokant, meer niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'te gebruiken tot' op een verpakking?",
        opties=[
            "Na die datum kan het product onveilig zijn",
            "Na die datum smaakt het alleen wat minder",
            "Voor die datum is het nog niet helemaal klaar",
            "Die datum zegt wanneer het gemaakt werd",
        ],
        antwoord=0,
        uitleg="Dat staat op verse producten zoals vlees en vis. Daar gaat het wél over veiligheid, dus die datum respecteer je.",
    ),
    dict(
        type="waarofniet",
        vraag="Ten minste houdbaar tot en te gebruiken tot betekenen precies hetzelfde.",
        antwoord=False,
        uitleg="De eerste gaat over kwaliteit, de tweede over veiligheid. Juist door dat verschil te kennen, gooi je minder eten weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een allergeen?",
        opties=[
            "Een stof waar sommige mensen op reageren",
            "Een kleurstof die de smaak wat versterkt",
            "Een bewaarmiddel dat schimmels tegenhoudt",
            "Een vitamine die in verse groenten zit",
        ],
        antwoord=0,
        uitleg="Noten, melk, gluten en ei zijn bekende allergenen. Ze moeten op het etiket opvallen, vaak in het vet gedrukt.",
    ),
    dict(
        type="invultekst",
        vraag="De lijst op een verpakking die alle bestanddelen opsomt, heet de ___.",
        antwoord=["ingrediëntenlijst", "ingredientenlijst"],
        uitleg="Die lijst staat in volgorde van hoeveelheid: waar het meeste van in zit, staat vooraan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een verpakking?",
        opties=[
            "Het product beschermen bij het vervoer",
            "Het product langer houdbaar maken",
            "Informatie doorgeven aan de klant",
            "De prijs van het product doen dalen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt gebruiksgemak, hygiënische bewaring, informatie voor de klant en bescherming tegen breken, bederf en licht. Goedkoper wordt een product er niet van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zit rode wijn in een donkere fles?",
        opties=[
            "Om een reactie met licht tegen te gaan",
            "Om de fles steviger te maken bij vervoer",
            "Om de wijn binnenin wat koeler te houden",
            "Om de wijn sneller te laten rijpen in de kelder",
        ],
        antwoord=0,
        uitleg="Licht brengt in de wijn een chemische reactie op gang waardoor hij bederft. Het donkere glas houdt dat licht tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Vacuüm verpakken beschermt voedsel tegen bederf.",
        antwoord=True,
        uitleg="Zonder zuurstof groeien veel bacteriën en schimmels niet. Daarom blijft vacuüm verpakt vlees veel langer goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voordeel van een plastic fles boven een glazen fles?",
        opties=[
            "Ze weegt minder, dus het vervoer kost minder",
            "Ze is in elk geval goedkoper om te maken",
            "Ze is in alle opzichten beter voor het milieu",
            "Ze houdt het licht veel beter tegen dan glas",
        ],
        antwoord=0,
        uitleg="Dat voorbeeld staat in de fiche: lichter vervoeren kost minder energie. Maar plastic zorgt wel voor meer afval in het milieu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een nadeel van plastic flessen?",
        opties=[
            "Ze zorgen voor meer afval in het milieu",
            "Ze breken een stuk makkelijker dan glas",
            "Ze wegen een flink stuk meer dan glas",
            "Ze kunnen op geen enkele manier hergebruikt",
        ],
        antwoord=0,
        uitleg="Duurzaamheid is altijd een afweging: lichter vervoeren staat tegenover meer afval. Daarom gaat de fiche over voor- én nadelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pictogram met de pijlen die een driehoek vormen, betekent dat de verpakking recycleerbaar is.",
        antwoord=True,
        uitleg="Dat is het recyclageteken. Soms staat er een percentage bij: dat zegt hoeveel gerecycleerd materiaal er al in zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het pictogram met een cijfer van 1 tot 7 in het midden?",
        opties=[
            "Het zegt om welke soort kunststof het gaat",
            "Het zegt hoeveel het product in totaal weegt",
            "Het zegt hoeveel dagen het nog houdbaar is",
            "Het zegt vanaf welke leeftijd het geschikt is",
        ],
        antwoord=0,
        uitleg="Elke kunststof krijgt een eigen nummer. Zo weet de recyclagefabriek welke soorten bij elkaar horen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Groenpuntlogo betekent dat de verpakking van gerecycleerd materiaal gemaakt is.",
        antwoord=False,
        uitleg="Het zegt niets over de verpakking zelf. Het betekent dat de fabrikant meebetaalt aan het ophalen en recycleren van verpakkingsafval, via het Fost Plus-systeem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het pictogram met een glas en een vork?",
        opties=[
            "Het product is veilig voor voedsel",
            "Het product mag in de vaatwasser",
            "Het product mag in een hete oven",
            "Het product is breekbaar bij vervoer",
        ],
        antwoord=0,
        uitleg="Dat teken staat op doosjes en bekers om te zeggen dat er zonder gevaar eten of drinken in mag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je duurzaam met voedsel en verpakkingen omgaan?",
        opties=[
            "Kopen wat je echt nodig hebt",
            "Herbruikbare verpakkingen gebruiken",
            "Je afval goed sorteren",
            "Alles in kleine porties apart verpakken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles apart verpakken levert juist een berg extra afval op. Minder kopen dan je weggooit, scheelt het meest.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verpakking met statiegeld breng je terug naar de winkel.",
        antwoord=True,
        uitleg="Je betaalt bij de aankoop een bedrag dat je terugkrijgt als je de verpakking inlevert. Zo wordt ze hergebruikt of gerecycleerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent composteerbaar?",
        opties=[
            "De verpakking kan vergaan tot compost",
            "De verpakking mag in de microgolfoven",
            "De verpakking is helemaal van glas gemaakt",
            "De verpakking kan nooit opnieuw gebruikt",
        ],
        antwoord=0,
        uitleg="Composteerbaar materiaal wordt door micro-organismen afgebroken tot aarde. Het hoort dus bij het gft en niet bij het restafval.",
    ),
    dict(
        type="waarofniet",
        vraag="Het pictogram met de doorstreepte vuilnisbak betekent dat het product gewoon bij het huisvuil mag.",
        antwoord=False,
        uitleg="Het betekent net het omgekeerde: dit hoort bij de selectieve ophaling en mag níét bij het huishoudelijk afval.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat de voedingswaarde op een etiket?",
        opties=[
            "Zodat je weet hoeveel energie en stoffen erin zitten",
            "Zodat je weet wie het product precies gemaakt heeft",
            "Zodat je weet hoe je het product moet klaarmaken",
            "Zodat je weet uit welk land het product komt",
        ],
        antwoord=0,
        uitleg="De voedingswaarde geeft per honderd gram de energie, de vetten, de suikers, de eiwitten en het zout. Zo kan je twee producten met elkaar vergelijken.",
    ),
]
