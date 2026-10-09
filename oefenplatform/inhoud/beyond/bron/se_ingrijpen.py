# -*- coding: utf-8 -*-
"""Verschuivingen op de markt en de overheid die ingrijpt.

Het tweede thema uit "ik begrijp de prijsvorming op de markt". Hier zit het
onderscheid dat de fiche letterlijk apart vraagt:

    een beweging óp de curve      de prijs van het product zelf verandert
    een verschuiving ván de curve iets anders verandert

Dat verschil is de moeilijkste van het hele blok, en het komt in beide delen
terug. Ezelsbruggetje: verandert de prijs, dan wandel je langs de curve;
verandert er iets anders, dan verhuist de hele curve.

De fiche vraagt ook de richting te bepalen, naar links of naar rechts, en
omgekeerd uit een verschuiving de mogelijke oorzaak af te leiden.

De drie overheidsmaatregelen staan er met zoveel woorden:
    btw en accijnzen heffen
    premies en subsidies uitkeren
    minimum- en maximumprijzen invoeren

Let op de twee prijzen, want ze worden vaak omgedraaid. Een minimumprijs ligt
bóven het evenwicht en geeft een overschot. Een maximumprijs ligt ónder het
evenwicht en geeft een tekort.

Deel 1 is bewegingen, verschuivingen en hun oorzaken.
Deel 2 is de overheid: belastingen, subsidies en vaste prijzen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer spreek je van een beweging op de vraagcurve?",
        opties=[
            "als de prijs van het product zelf verandert",
            "als het inkomen van de kopers verandert",
            "als er meer kopers bijkomen",
            "als een ander product goedkoper wordt",
        ],
        antwoord=0,
        uitleg="Verandert de prijs, dan schuif je langs dezelfde curve naar een ander punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer verschuift de vraagcurve zelf?",
        opties=[
            "als er iets anders verandert dan de prijs van het product",
            "als de prijs van het product daalt",
            "als de prijs van het product stijgt",
            "als de verkopers minder aanbieden",
        ],
        antwoord=0,
        uitleg="Inkomen, smaak, aantal kopers, de prijs van een ander product: dan verhuist de hele curve.",
    ),
    dict(
        type="meerkeuze",
        vraag="De lonen stijgen en mensen kopen meer van een product bij elke prijs. Wat gebeurt er?",
        opties=[
            "de vraagcurve verschuift naar rechts",
            "de vraagcurve verschuift naar links",
            "er is een beweging op de vraagcurve naar boven",
            "de aanbodcurve verschuift naar rechts",
        ],
        antwoord=0,
        uitleg="Bij elke prijs wordt er meer gevraagd, dus de hele curve gaat naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een product raakt uit de mode en mensen willen er bij elke prijs minder van. Wat gebeurt er?",
        opties=[
            "de vraagcurve verschuift naar links",
            "de vraagcurve verschuift naar rechts",
            "er is een beweging op de vraagcurve",
            "de aanbodcurve verschuift naar links",
        ],
        antwoord=0,
        uitleg="Minder vraag bij elke prijs betekent dat de curve naar links opschuift.",
    ),
    dict(
        type="meerkeuze",
        vraag="De grondstoffen voor een product worden duurder. Wat gebeurt er met het aanbod?",
        opties=[
            "de aanbodcurve verschuift naar links",
            "de aanbodcurve verschuift naar rechts",
            "er is enkel een beweging op de aanbodcurve",
            "er verandert niets aan het aanbod",
        ],
        antwoord=0,
        uitleg="Produceren wordt duurder, dus bij elke prijs wordt er minder aangeboden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nieuwe machine maakt het goedkoper om een product te maken. Wat gebeurt er?",
        opties=[
            "de aanbodcurve verschuift naar rechts",
            "de aanbodcurve verschuift naar links",
            "de vraagcurve verschuift naar rechts",
            "er is een beweging op de aanbodcurve",
        ],
        antwoord=0,
        uitleg="Goedkoper produceren betekent meer aanbod bij elke prijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraagcurve verschuift naar rechts en het aanbod blijft gelijk. Wat gebeurt er met het evenwicht?",
        opties=[
            "de prijs stijgt en de hoeveelheid stijgt",
            "de prijs daalt en de hoeveelheid stijgt",
            "de prijs stijgt en de hoeveelheid daalt",
            "de prijs en de hoeveelheid blijven gelijk",
        ],
        antwoord=0,
        uitleg="Meer kopers bij hetzelfde aanbod duwen zowel de prijs als de verhandelde hoeveelheid omhoog.",
    ),
    dict(
        type="meerkeuze",
        vraag="De aanbodcurve verschuift naar rechts en de vraag blijft gelijk. Wat gebeurt er met het evenwicht?",
        opties=[
            "de prijs daalt en de hoeveelheid stijgt",
            "de prijs stijgt en de hoeveelheid stijgt",
            "de prijs daalt en de hoeveelheid daalt",
            "er verandert niets",
        ],
        antwoord=0,
        uitleg="Meer aanbod bij dezelfde vraag drukt de prijs en verhoogt de verhandelde hoeveelheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet op een grafiek dat de aanbodcurve naar links verschoven is. Wat kan de oorzaak zijn?",
        opties=[
            "de grondstoffen zijn duurder geworden",
            "de kopers hebben meer geld te besteden",
            "het product is in de mode geraakt",
            "er zijn meer kopers bijgekomen",
        ],
        antwoord=0,
        uitleg="De andere drie raken de vraag, niet het aanbod.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet dat de vraagcurve naar links verschoven is. Wat kan de oorzaak zijn?",
        opties=[
            "een vergelijkbaar product is veel goedkoper geworden",
            "de productiekosten zijn gedaald",
            "er zijn meer verkopers op de markt",
            "de fabriek heeft een nieuwe machine",
        ],
        antwoord=0,
        uitleg="De andere drie verschuiven het aanbod. Een goedkoper alternatief trekt kopers weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prijsdaling van het product zelf verschuift de vraagcurve naar rechts.",
        antwoord=False,
        uitleg="Nee, dan beweeg je langs dezelfde curve naar een ander punt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stijging van het inkomen van de kopers verschuift de vraagcurve.",
        antwoord=True,
        uitleg="Het inkomen is niet de prijs van het product, dus de hele curve verhuist.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de vraagcurve naar rechts verschuift, daalt de evenwichtsprijs.",
        antwoord=False,
        uitleg="Ze stijgt: er zijn meer kopers voor hetzelfde aanbod.",
    ),
    dict(
        type="waarofniet",
        vraag="Duurdere grondstoffen verschuiven de aanbodcurve naar links.",
        antwoord=True,
        uitleg="Produceren kost meer, dus bij elke prijs komt er minder op de markt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze verschuiven de vraagcurve?",
        opties=[
            "het inkomen van de kopers verandert",
            "de smaak van de kopers verandert",
            "er komen kopers bij of vallen er weg",
            "de prijs van het product zelf verandert",
        ],
        antwoord=[0, 1, 2],
        uitleg="De prijs van het product zelf geeft een beweging óp de curve, geen verschuiving ervan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze verschuiven de aanbodcurve?",
        opties=[
            "de productiekosten veranderen",
            "er komt een betere techniek",
            "er komen verkopers bij",
            "de prijs van het product zelf verandert",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ook hier: de prijs van het product zelf laat je langs de curve bewegen.",
    ),
    dict(
        type="invultekst",
        vraag="Verandert de prijs van het product zelf, dan is er een beweging ... de curve. Vul aan met één woord.",
        antwoord=["op"],
        uitleg="Verandert er iets anders, dan is er een verschuiving van de curve.",
    ),
    dict(
        type="invultekst",
        vraag="Naar welke kant verschuift de vraagcurve als er meer kopers bijkomen? Antwoord met links of rechts.",
        antwoord=["rechts", "naar rechts"],
        uitleg="Meer vraag bij elke prijs betekent naar rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraagcurve verschuift naar links en het aanbod blijft gelijk. Wat gebeurt er met het evenwicht?",
        opties=[
            "de prijs daalt en de hoeveelheid daalt",
            "de prijs stijgt en de hoeveelheid daalt",
            "de prijs daalt en de hoeveelheid stijgt",
            "er verandert niets",
        ],
        antwoord=0,
        uitleg="Minder kopers bij hetzelfde aanbod drukken allebei omlaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een zomer met slecht weer bederft een groot deel van de oogst. Wat gebeurt er met de prijs van die groente?",
        opties=[
            "het aanbod verschuift naar links en de prijs stijgt",
            "de vraag verschuift naar links en de prijs daalt",
            "het aanbod verschuift naar rechts en de prijs daalt",
            "er is enkel een beweging op de aanbodcurve",
        ],
        antwoord=0,
        uitleg="Minder aanbod bij dezelfde vraag duwt de prijs omhoog.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie soorten overheidsmaatregelen noemt de fiche?",
        opties=[
            "btw en accijnzen, premies en subsidies, en minimum- en maximumprijzen",
            "belastingen, boetes en vergunningen",
            "invoerrechten, exportsteun en quota",
            "rentevoeten, leningen en spaarpremies",
        ],
        antwoord=0,
        uitleg="Precies die drie staan in de fiche bij het ingrijpen op de markt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een accijns?",
        opties=[
            "een extra belasting op bepaalde producten, zoals brandstof of alcohol",
            "een korting die de overheid aan producenten geeft",
            "de laagste prijs waartegen verkocht mag worden",
            "een vergoeding voor een dienst van de gemeente",
        ],
        antwoord=0,
        uitleg="Ze komt bovenop de btw en maakt die producten bewust duurder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een belasting op een product met het aanbod?",
        opties=[
            "het aanbod verschuift naar links en de prijs stijgt",
            "het aanbod verschuift naar rechts en de prijs daalt",
            "de vraag verschuift naar rechts",
            "er verandert niets aan prijs of hoeveelheid",
        ],
        antwoord=0,
        uitleg="Verkopen wordt duurder voor de aanbieder, dus hij biedt bij elke prijs minder aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een subsidie aan producenten met het aanbod?",
        opties=[
            "het aanbod verschuift naar rechts en de prijs daalt",
            "het aanbod verschuift naar links en de prijs stijgt",
            "de vraag verschuift naar links",
            "de evenwichtshoeveelheid daalt",
        ],
        antwoord=0,
        uitleg="Produceren wordt goedkoper, dus er komt meer op de markt en de prijs zakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt een minimumprijs die iets uithaalt?",
        opties=[
            "boven de evenwichtsprijs",
            "onder de evenwichtsprijs",
            "precies op de evenwichtsprijs",
            "dat maakt niet uit",
        ],
        antwoord=0,
        uitleg="Een minimumprijs onder het evenwicht verandert niets, want de markt zit er al boven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er door een minimumprijs boven het evenwicht?",
        opties=["een overschot", "een tekort", "een nieuw evenwicht", "niets"],
        antwoord=0,
        uitleg="De prijs ligt te hoog voor de kopers, dus er blijft aanbod over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt een maximumprijs die iets uithaalt?",
        opties=[
            "onder de evenwichtsprijs",
            "boven de evenwichtsprijs",
            "precies op de evenwichtsprijs",
            "dat maakt niet uit",
        ],
        antwoord=0,
        uitleg="Een maximumprijs boven het evenwicht verandert niets, want de markt zit er al onder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er door een maximumprijs onder het evenwicht?",
        opties=["een tekort", "een overschot", "een nieuw evenwicht", "niets"],
        antwoord=0,
        uitleg="Veel mensen willen kopen tegen die lage prijs, maar de verkopers bieden te weinig aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zou een overheid een maximumprijs invoeren?",
        opties=[
            "om een noodzakelijk product betaalbaar te houden",
            "om de producenten een eerlijk inkomen te geven",
            "om meer belastingen te kunnen innen",
            "om het aanbod te vergroten",
        ],
        antwoord=0,
        uitleg="Denk aan energie of huur: de overheid wil vermijden dat het onbetaalbaar wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zou een overheid een minimumprijs invoeren?",
        opties=[
            "om de producenten een leefbaar inkomen te garanderen",
            "om het product goedkoper te maken voor de kopers",
            "om een tekort op te lossen",
            "om minder belastingen te moeten innen",
        ],
        antwoord=0,
        uitleg="Een bekend voorbeeld is een bodemprijs voor landbouwproducten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een maximumprijs geeft een tekort.",
        antwoord=True,
        uitleg="De prijs ligt onder het evenwicht, dus de vraag is groter dan het aanbod.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minimumprijs geeft een tekort.",
        antwoord=False,
        uitleg="Een minimumprijs geeft een overschot: de prijs ligt boven het evenwicht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een subsidie aan producenten doet de prijs voor de koper dalen.",
        antwoord=True,
        uitleg="Het aanbod verschuift naar rechts en dat drukt de evenwichtsprijs.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de fiche grijpt de overheid enkel in door prijzen vast te leggen.",
        antwoord=False,
        uitleg="Het rijtje van de fiche heeft drie manieren: btw en accijnzen heffen, subsidies geven en prijzen vastleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen van de overheid noemt de fiche?",
        opties=[
            "btw en accijnzen heffen",
            "premies en subsidies uitkeren",
            "minimum- en maximumprijzen invoeren",
            "de productie zelf overnemen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De productie overnemen staat niet in dit rijtje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is waar over een maximumprijs?",
        opties=[
            "ze ligt onder de evenwichtsprijs",
            "ze geeft een tekort",
            "ze wordt ingevoerd om iets betaalbaar te houden",
            "ze geeft een overschot",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een overschot hoort bij een minimumprijs, niet bij een maximumprijs.",
    ),
    dict(
        type="invultekst",
        vraag="Welke vaste prijs van de overheid geeft een overschot? Antwoord met één woord.",
        antwoord=["minimumprijs", "een minimumprijs"],
        uitleg="Ze ligt boven het evenwicht, dus er blijft aanbod over.",
    ),
    dict(
        type="invultekst",
        vraag="Welke vaste prijs van de overheid geeft een tekort? Antwoord met één woord.",
        antwoord=["maximumprijs", "een maximumprijs"],
        uitleg="Ze ligt onder het evenwicht, dus de vraag is groter dan het aanbod.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de extra belasting op producten zoals brandstof, tabak en alcohol?",
        antwoord=["accijns", "accijnzen", "de accijnzen"],
        uitleg="Ze komt bovenop de btw en staat in het rijtje van overheidsmaatregelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid geeft een premie voor zonnepanelen. Wat verwacht je op die markt?",
        opties=[
            "meer vraag, dus een hogere prijs en meer verkochte panelen",
            "minder vraag, dus een lagere prijs",
            "minder aanbod, dus een hogere prijs",
            "niets, een premie raakt de markt niet",
        ],
        antwoord=0,
        uitleg="Een premie aan de koper verschuift de vraag naar rechts: meer mensen willen kopen bij elke prijs.",
    ),
]
