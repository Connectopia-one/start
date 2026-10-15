# -*- coding: utf-8 -*-
"""Pittige vragen bij "Biotechnische systemen" (✨ Spark, techniek).

Bewaartechnieken, etiket en pictogrammen toegepast op situaties uit de keuken en
de winkel, met de misvattingen die de leerbundel zelf aanwijst.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag="Je oma doet groenten in een glazen bokaal, sluit die goed af en verhit de gesloten bokaal. Zolang de bokaal dicht blijft, blijven de groenten maanden goed. Welke bewaartechniek gebruikt ze?",
        opties=["Wecken", "Pekelen", "Koelen", "Fermenteren"],
        antwoord=0,
        uitleg="Voedsel in een gesloten pot verhitten heet wecken. Pekelen gebeurt in een zoute oplossing zonder verhitten, en bij fermenteren laat je juist micro-organismen het werk doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ontdooit kipfilet die drie maanden in de diepvries lag. Wat klopt er?",
        opties=[
            "De bacteriën gaan weer groeien, dus de kip kan weer bederven",
            "De vrieskou heeft alle bacteriën gedood, dus de kip blijft goed",
            "Ontdooide kip kan niet meer bederven door de kou van daarvoor",
            "Alleen de schimmels overleven het invriezen, de bacteriën niet",
        ],
        antwoord=0,
        uitleg="Invriezen legt de groei van bacteriën zo goed als stil, maar het doodt ze niet. Na het ontdooien gaan ze gewoon verder, dus ontdooid voedsel bederft weer zoals vers voedsel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een allergeen is een stof waar iedereen ziek van wordt als hij ze eet.",
        antwoord=False,
        uitleg="Een allergeen is een stof waar sommige mensen op reageren. De meeste mensen eten ze zonder probleem; daarom moeten de allergenen apart op het etiket staan, voor wie er wel op reageert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een pak koekjes staat 'ten minste houdbaar tot' de datum van gisteren. Op een pak gehakt staat 'te gebruiken tot' dezelfde datum. Wat doe je best?",
        opties=[
            "De koekjes mag je nog eten, het gehakt eet je niet meer",
            "Het gehakt mag je nog eten, de koekjes gooi je weg",
            "Je gooit allebei weg, want de datum is voorbij",
            "Je eet allebei op, want één dag te laat is niet erg",
        ],
        antwoord=0,
        uitleg="'Ten minste houdbaar tot' gaat over kwaliteit: de koekjes zijn misschien minder lekker, maar je mag ze nog eten. 'Te gebruiken tot' gaat over veiligheid: na die datum kan het gehakt onveilig zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze bewaartechnieken werken zonder koude en zonder warmte? (meerdere antwoorden mogelijk)",
        opties=["Drogen", "Pekelen", "Vacuüm verpakken", "Fermenteren", "Wecken"],
        antwoord=[0, 1, 2, 3],
        uitleg="Drogen haalt het water weg, pekelen gebruikt een zoute oplossing, vacuüm verpakken haalt de lucht eruit en bij fermenteren doen micro-organismen het werk. Bij wecken wordt de gesloten pot verhit, dus daar komt wel warmte aan te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke van deze bewerkingen laat je micro-organismen met opzet hun werk doen? (meerdere antwoorden mogelijk)",
        opties=[
            "Zuurkool maken",
            "Brooddeeg laten rijzen",
            "Melk pasteuriseren",
            "Vlees invriezen",
            "Fruit drogen",
        ],
        antwoord=[0, 1],
        uitleg="Bij zuurkool fermenteren bacteriën de kool, en bij brooddeeg doet gist het werk. Pasteuriseren, invriezen en drogen doen net het omgekeerde: die moeten de micro-organismen tegenhouden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over koelen en invriezen klopt?",
        opties=[
            "In de diepvries ligt de groei van bacteriën zo goed als stil",
            "In de koelkast ligt de groei van bacteriën helemaal stil",
            "Koelen en invriezen doden allebei de bacteriën in het voedsel",
            "Koelen legt de groei stil, invriezen remt ze alleen een beetje af",
        ],
        antwoord=0,
        uitleg="Koelen remt de groei af, invriezen legt ze zo goed als stil. Geen van beide doodt de bacteriën. Wie de twee verwisselt, denkt dat de koelkast meer doet dan de diepvries.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gesloten pak UHT-melk hoeft niet in de koelkast, maar een geopend pak wel.",
        antwoord=True,
        uitleg="UHT-melk is heel kort heel sterk verhit en blijft daardoor maanden goed zonder koelkast. Dat geldt wel maar tot je het pak opent: daarna gaat het in de koelkast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een meisje met een notenallergie wil een koek kopen. Waar op de verpakking kijkt ze best?",
        opties=[
            "Bij de allergenen en in de ingrediëntenlijst",
            "Bij de voedingswaarde en de hoeveelheid energie",
            "Bij de houdbaarheidsdatum op de achterkant",
            "Bij het pictogram met een glas en een vork",
        ],
        antwoord=0,
        uitleg="De ingrediëntenlijst somt alle bestanddelen op, en de allergenen moeten apart vermeld zijn. De voedingswaarde zegt hoeveel energie en stoffen erin zitten, niet of er noten in zitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op een plastic bakje staat het Groenpuntlogo. Wat mag je daaruit besluiten?",
        opties=[
            "Het bedrijf betaalt mee voor de inzameling en verwerking",
            "Het bakje is van gerecycleerd materiaal gemaakt",
            "Het bakje is van een materiaal dat veilig is voor voedsel",
            "Het bakje mag niet bij het huisvuil, je levert het apart in",
        ],
        antwoord=0,
        uitleg="Het Groenpuntlogo zegt dat het bedrijf meebetaalt voor de inzameling en verwerking van verpakkingen. Het zegt niet dat de verpakking van gerecycleerd materiaal is; dat is net de misvatting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt een bakje voor je boterhammen dat je daarna ook kunt laten recycleren. Welke pictogrammen wil je daarvoor op het bakje zien? (meerdere antwoorden mogelijk)",
        opties=[
            "Een glas en een vork",
            "Pijlen die een driehoek vormen",
            "Het Groenpuntlogo",
            "Een doorstreepte vuilnisbak",
        ],
        antwoord=[0, 1],
        uitleg="Het glas en de vork zeggen dat het materiaal veilig is voor voedsel, en de driehoek van pijlen dat de verpakking recycleerbaar is. Het Groenpuntlogo gaat over wie meebetaalt, en de doorstreepte vuilnisbak zegt alleen dat iets niet bij het huisvuil mag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een winkel twijfelt tussen glazen en plastic flessen voor water. Welke uitspraken kloppen? (meerdere antwoorden mogelijk)",
        opties=[
            "Plastic weegt minder, dus het vervoer kost minder",
            "Plastic flessen geven meer afval in het milieu",
            "Een fles met statiegeld breng je terug naar de winkel",
            "Plastic is in alle opzichten beter voor het milieu",
            "Glazen flessen zijn lichter om te vervoeren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Plastic is lichter en dus goedkoper te vervoeren, maar het geeft meer afval in het milieu. Je moet dus afwegen; geen van beide is in alle opzichten beter.",
    ),
    dict(
        type="waarofniet",
        vraag="Zuurkool is tegelijk een product van micro-organismen en een manier om kool langer te bewaren.",
        antwoord=True,
        uitleg="Bacteriën fermenteren de kool tot zuurkool, en fermenteren is meteen ook een bewaartechniek. De micro-organismen doen het werk en maken het product tegelijk langer houdbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bakje met het pictogram van een glas en een vork is daardoor ook recycleerbaar.",
        antwoord=False,
        uitleg="Het glas en de vork zeggen alleen dat het materiaal veilig is voor voedsel. Of het recycleerbaar is, zegt een ander pictogram: de pijlen die een driehoek vormen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Op een beker yoghurt staat bij de voedingswaarde: \(5\) gram suiker per \(100\) gram. De beker bevat \(300\) gram yoghurt. Hoeveel gram suiker zit er in de hele beker? Antwoord met een getal.",
        antwoord="15",
        reken="5 * 300 / 100",
        uitleg=r"In de beker zit drie keer \(100\) gram yoghurt. Dan zit er ook drie keer zoveel suiker in: \(3\) maal \(5\) gram is \(15\) gram. Met de voedingswaarde kun je zo uitrekenen wat je echt binnenkrijgt.",
    ),
    dict(
        type="invultekst",
        vraag="Een fabrikant verhit melk heel kort heel sterk, zodat een gesloten pak maanden goed blijft zonder koelkast. Welke drie letters staan dan op het pak? Antwoord met één woord.",
        antwoord="UHT",
        uitleg="UHT betekent dat de melk heel kort heel sterk verhit is. Gewoon pasteuriseren verhit tot onder het kookpunt; zo'n melk blijft niet maanden goed buiten de koelkast.",
    ),
    dict(
        type="invultekst",
        vraag="Een inspecteur komt onaangekondigd de keuken van een frituur controleren op voedselveiligheid. Voor welke instelling werkt hij? Geef de afkorting.",
        antwoord="FAVV",
        uitleg="Het FAVV waakt over de veiligheid van ons voedsel en controleert daarvoor winkels, restaurants en voedingsbedrijven. Een frituur hoort daar ook bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakker merkt dat zijn brooddeeg helemaal niet gerezen is. Wat is hij waarschijnlijk vergeten toe te voegen?",
        opties=["Gist", "Schimmel", "Melkzuurbacteriën", "Een zoute pekel"],
        antwoord=0,
        uitleg="Gist is het micro-organisme dat brooddeeg doet rijzen. Bacteriën zorgen voor yoghurt en zuurkool, niet voor gerezen deeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Eieren worden verkocht in een kartonnen doos met een apart vakje voor elk ei. Welke taak van een verpakking staat daar vooral voorop?",
        opties=[
            "Het product beschermen bij het vervoer",
            "Het product langer houdbaar maken door koude",
            "De klant informeren over de allergenen in het ei",
            "Het product laten fermenteren tijdens het vervoer",
        ],
        antwoord=0,
        uitleg="De vakjes houden de eieren apart, zodat ze niet tegen elkaar botsen en breken onderweg. Een kartonnen doos koelt niet, en informatie geven doet het etiket.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke manier van boodschappen doen is het duurzaamst?",
        opties=[
            "Kopen wat je echt nodig hebt, in herbruikbare zakken",
            "Elke koek apart verpakt kopen, dat is netter en hygiënischer",
            "Veel meer kopen dan nodig, dan hoef je minder vaak te gaan",
            "Alles in plastic kopen, want plastic is lichter om te dragen",
        ],
        antwoord=0,
        uitleg="Kopen wat je echt nodig hebt en herbruikbare verpakkingen gebruiken zijn twee manieren om duurzaam met voedsel en verpakkingen om te gaan. Alles apart verpakken of te veel kopen levert juist extra afval op.",
    ),
]
