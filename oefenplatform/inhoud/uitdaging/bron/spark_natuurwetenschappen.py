# -*- coding: utf-8 -*-
"""Uitdaging natuurwetenschappen ✨ Spark: de tien thema's door elkaar."""
NIVEAU = "spark"
VAK = "Natuurwetenschappen"
BESTAND = "spark-natuurwetenschappen-uitdaging.json"

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Een plant verbruikt zelf ook zuurstof, en toch geeft ze er overdag netto aan de lucht af. Hoe kan dat?",
        "opties": [
            "De fotosynthese levert meer zuurstof op dan de plant zelf verbruikt",
            "De plant stopt overdag met ademen en start daar 's nachts weer mee",
            "De bladgroenkorrels maken zuurstof zonder dat er licht voor nodig is",
            "De wortels nemen de zuurstof op die de bladeren nodig zouden hebben",
        ],
        "antwoord": 0,
        "uitleg": "Ademen doet een plant dag en nacht. Fotosynthese komt daar overdag bovenop en levert veel meer zuurstof op dan er verbruikt wordt, dus blijft er over.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een plant ademt enkel 's nachts en doet overdag alleen aan fotosynthese.",
        "antwoord": False,
        "uitleg": "Niet waar. Elke levende cel ademt onafgebroken, ook overdag. Alleen valt dat overdag niet op, omdat de fotosynthese er ruim bovenuit gaat.",
    },
    {
        "type": "invultekst",
        "vraag": "Een steen heeft een massa van 240 g en een volume van 80 cm³. Wat is zijn massadichtheid in g/cm³?",
        "antwoord": "3",
        "reken": "240 / 80",
        "uitleg": "Massadichtheid is massa gedeeld door volume: 240 : 80 = 3 g/cm³. Die steen is dus drie keer zo dicht als water.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een stuk hout heeft een massa van 60 g en een volume van 100 cm³. Water heeft een massadichtheid van 1 g/cm³. Wat gebeurt er?",
        "opties": [
            "Het hout drijft, want 0,6 g/cm³ is minder dicht dan water",
            "Het hout zinkt, want 60 gram is zwaarder dan honderd gram",
            "Het hout zweeft halverwege, want het verschil is maar klein",
            "Dat kan je niet weten zonder de vorm van het hout te kennen",
        ],
        "antwoord": 0,
        "uitleg": "60 : 100 = 0,6 g/cm³. Wat minder dicht is dan de vloeistof, drijft. De massa alleen zegt niets: je moet ze tegenover het volume zetten.",
    },
    {
        "type": "waarofniet",
        "vraag": "Of iets drijft of zinkt, hangt niet af van hoe groot het is maar van zijn massadichtheid.",
        "antwoord": True,
        "uitleg": "Waar. Een schip van duizenden ton drijft en een muntstuk zinkt. Wat telt, is de massa per cm³, vergeleken met die van de vloeistof.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een fietser remt, en de remblokjes worden warm. Welke energieomzetting gebeurt daar?",
        "opties": [
            "Bewegingsenergie wordt warmte",
            "Warmte wordt bewegingsenergie",
            "Chemische energie wordt licht",
            "Bewegingsenergie verdwijnt helemaal",
        ],
        "antwoord": 0,
        "uitleg": "Door de wrijving gaat de bewegingsenergie van de fiets over in warmte. Energie verdwijnt nooit, ze verandert alleen van vorm.",
    },
    {
        "type": "invultekst",
        "vraag": "Een auto legt 150 km af in 2 uur. Wat is de gemiddelde snelheid in km/h?",
        "antwoord": "75",
        "reken": "150 / 2",
        "uitleg": "Snelheid is afstand gedeeld door tijd: 150 : 2 = 75 km/h. Gemiddeld, want onderweg reed hij nu eens sneller en dan weer trager.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je onderzoekt of planten sneller groeien met meer licht. Wat doe je met water, grond en temperatuur?",
        "opties": [
            "Die houd je bij alle planten precies gelijk",
            "Die verander je mee, zodat de groei goed opvalt",
            "Die laat je bij elke plant toevallig anders zijn",
            "Die meet je niet, want ze doen hier niet ter zake",
        ],
        "antwoord": 0,
        "uitleg": "Je verandert één ding tegelijk. Verandert er meer, dan weet je achteraf niet waardóór de planten sneller groeiden.",
    },
    {
        "type": "waarofniet",
        "vraag": "Als je proef je hypothese weerlegt, is je onderzoek mislukt.",
        "antwoord": False,
        "uitleg": "Niet waar. Een weerlegde hypothese is een volwaardig resultaat: je weet nu iets wat je daarvoor niet wist. Mislukt is een proef pas als ze niets kan uitwijzen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom staan planten altijd aan het begin van een voedselketen?",
        "opties": [
            "Omdat ze als enige hun eigen voedsel maken uit licht",
            "Omdat ze zich niet kunnen verplaatsen om te ontsnappen",
            "Omdat er nu eenmaal veel meer planten zijn dan dieren",
            "Omdat elk dier in een keten uitsluitend planten eet",
        ],
        "antwoord": 0,
        "uitleg": "Planten zijn autotroof: ze maken met licht hun eigen voedsel. Alle andere schakels leven van wat een vorige schakel gemaakt heeft.",
    },
    {
        "type": "invultekst",
        "vraag": "Water heeft een massadichtheid van 1 g/cm³. Hoeveel gram weegt 2,5 liter water?",
        "antwoord": "2500",
        "reken": "2.5 * 1000",
        "uitleg": "1 liter is 1 000 cm³ en weegt dus 1 000 gram. 2,5 liter is 2 500 gram, of 2,5 kilogram.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Zet van klein naar groot: orgaan, cel, stelsel, weefsel.",
        "opties": [
            "Cel – weefsel – orgaan – stelsel",
            "Cel – orgaan – weefsel – stelsel",
            "Weefsel – cel – orgaan – stelsel",
            "Cel – weefsel – stelsel – orgaan",
        ],
        "antwoord": 0,
        "uitleg": "Cellen van dezelfde soort vormen een weefsel, weefsels samen een orgaan, en organen die samen één grote taak doen, een stelsel.",
    },
    {
        "type": "waarofniet",
        "vraag": "Elk orgaan bestaat uit weefsels, en elk weefsel uit cellen.",
        "antwoord": True,
        "uitleg": "Waar. Je hart bijvoorbeeld bestaat onder meer uit spierweefsel, en dat spierweefsel bestaat uit spiercellen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welk van deze is géén fysisch verschijnsel?",
        "opties": [
            "Hout dat verbrandt in de kachel",
            "Water dat kookt in een pan",
            "IJs dat smelt in een glas",
            "Suiker die oplost in thee",
        ],
        "antwoord": 0,
        "uitleg": "Bij verbranden ontstaan nieuwe stoffen, zoals as en koolstofdioxide: dat is chemisch. De drie andere veranderen alleen van toestand of verdelen zich.",
    },
    {
        "type": "waarofniet",
        "vraag": "Bij een fysisch verschijnsel ontstaat er een nieuwe stof.",
        "antwoord": False,
        "uitleg": "Niet waar, dat is net het verschil. Bij een fysisch verschijnsel blijft de stof dezelfde; bij een chemisch verschijnsel ontstaat er een andere.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je eet een boterham. Welke weg legt de suiker daaruit af naar je spieren?",
        "opties": [
            "Dunne darm, dan het bloed, dan de cellen van de spier",
            "Maag, dan de longen, dan het bloed naar de spier toe",
            "Dikke darm, dan de nieren, dan het bloed naar de spier",
            "Slokdarm, dan het bloed, dan rechtstreeks naar de spier",
        ],
        "antwoord": 0,
        "uitleg": "De vertering maakt de suikers vrij, de dunne darm laat ze in het bloed, en het hart stuwt dat bloed naar elke cel die energie nodig heeft.",
    },
    {
        "type": "invultekst",
        "vraag": "Een proef duurt anderhalf uur. Hoeveel minuten is dat?",
        "antwoord": "90",
        "reken": "1.5 * 60",
        "uitleg": "Anderhalf uur is 1,5 x 60 = 90 minuten. Bij tijd reken je met 60, niet met 100.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is in een bos een abiotische factor?",
        "opties": [
            "De temperatuur van de lucht",
            "De eiken die er groeien",
            "De reeën die er grazen",
            "De schimmels op het dode hout",
        ],
        "antwoord": 0,
        "uitleg": "Abiotisch betekent niet-levend: temperatuur, licht, vocht, bodem. De eiken, de reeën en de schimmels zijn biotische factoren.",
    },
    {
        "type": "waarofniet",
        "vraag": "Biodiversiteit gaat over hoeveel verschillende soorten er in een gebied leven, niet over hoeveel dieren er zijn.",
        "antwoord": True,
        "uitleg": "Waar. Een weide met duizend koeien en drie plantensoorten heeft een lage biodiversiteit; een hooiland met honderden soorten een hoge.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het grote verschil tussen knopvorming bij een gist en voortplanting bij een mens?",
        "opties": [
            "Bij de gist komt alles van één ouder, bij de mens van twee",
            "Bij de gist ontstaat er geen nieuw organisme, bij de mens wel",
            "Bij de gist gebeurt het zonder cellen, bij de mens met cellen",
            "Bij de gist duurt het langer dan bij de mens het geval is",
        ],
        "antwoord": 0,
        "uitleg": "Knopvorming is aseksueel: de nieuwe gist is een kopie van de ene ouder. Bij seksuele voortplanting mengt het erfelijk materiaal van twee ouders, en dat geeft variatie.",
    },
]
