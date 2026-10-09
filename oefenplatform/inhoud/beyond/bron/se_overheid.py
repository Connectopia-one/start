# -*- coding: utf-8 -*-
"""De inkomsten en de uitgaven van de overheid.

Het eerste van twee thema's uit "ik maak deel uit van een sociaal
rechtvaardige samenleving", dat tien procent weegt.

De fiche geeft vier soorten inkomsten en vier soorten uitgaven, met telkens
voorbeelden. Die voorbeelden staan hier letterlijk, want ze zijn de
herkenningspunten op het examen:

    inkomsten
      directe belastingen            bedrijfsvoorheffing, onroerende voorheffing
      indirecte belastingen          btw, milieubelasting
      diverse inkomsten              boetes, vergoedingen voor diensten
      inkomsten uit overheidskapitaal  verkoop of verhuur van gronden en gebouwen

    uitgaven
      collectieve behoeften          veiligheid, onderwijs, openbaar vervoer
      economische groei              handel en transport, digitale infrastructuur,
                                     duurzaamheid
      maatschappelijk leven          cultuur en sport, sociale ontwikkeling van
                                     jongeren, infocampagnes
      sociale uitgaven               sociale zekerheid, sociale woningen,
                                     projecten tegen armoede

Het verschil tussen een directe en een indirecte belasting is wat kinderen
hier het vaakst verwarren: een directe belasting gaat rechtstreeks van jou naar
de overheid, een indirecte zit verstopt in de prijs van wat je koopt.

Deel 1 is de inkomsten van de overheid.
Deel 2 is de uitgaven van de overheid en hun invloed op de samenleving.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een directe belasting?",
        opties=[
            "een belasting die rechtstreeks van jou naar de overheid gaat",
            "een belasting die in de prijs van een product zit",
            "een belasting die je enkel bij een aankoop betaalt",
            "een belasting die je in één keer per jaar betaalt",
        ],
        antwoord=0,
        uitleg="Direct wil zeggen zonder tussenstap: de overheid heft ze op jouw inkomen of bezit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een indirecte belasting?",
        opties=[
            "een belasting die in de prijs van een product of dienst zit",
            "een belasting die de overheid op je loon inhoudt",
            "een belasting op de grond die je bezit",
            "een belasting die je enkel als zelfstandige betaalt",
        ],
        antwoord=0,
        uitleg="Jij betaalt ze aan de verkoper, die ze doorstort. Daarom indirect.",
    ),
    dict(
        type="meerkeuze",
        vraag="De btw op je nieuwe gsm. Welke soort inkomst is dat voor de overheid?",
        opties=[
            "een indirecte belasting",
            "een directe belasting",
            "een diverse inkomst",
            "een inkomst uit het kapitaal dat de overheid zelf bezit",
        ],
        antwoord=0,
        uitleg="Btw zit in de prijs en komt bij de overheid via de verkoper.",
    ),
    dict(
        type="meerkeuze",
        vraag="De bedrijfsvoorheffing op je loon. Welke soort inkomst is dat?",
        opties=[
            "een directe belasting",
            "een indirecte belasting",
            "een diverse inkomst",
            "een sociale uitgave",
        ],
        antwoord=0,
        uitleg="Ze wordt op jouw inkomen geheven, dus rechtstreeks. De fiche noemt ze als voorbeeld van een directe belasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="De onroerende voorheffing op een huis. Welke soort inkomst is dat?",
        opties=[
            "een directe belasting",
            "een indirecte belasting",
            "een inkomst uit het kapitaal dat de overheid zelf bezit",
            "een vergoeding voor een dienst",
        ],
        antwoord=0,
        uitleg="Ze wordt rechtstreeks op je bezit geheven, net als de belasting op je inkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een boete voor te snel rijden. Welke soort inkomst is dat volgens de fiche?",
        opties=[
            "een diverse inkomst",
            "een directe belasting",
            "een indirecte belasting",
            "een inkomst uit het kapitaal dat de overheid zelf bezit",
        ],
        antwoord=0,
        uitleg="Boetes en vergoedingen voor diensten staan in de fiche bij de diverse inkomsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="De stad verhuurt een gebouw aan een vereniging. Welke soort inkomst is dat?",
        opties=[
            "een inkomst uit het kapitaal dat de overheid zelf bezit",
            "een diverse inkomst",
            "een directe belasting",
            "een indirecte belasting",
        ],
        antwoord=0,
        uitleg="Verkoop of verhuur van gronden en gebouwen staat letterlijk in de fiche bij deze soort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een milieubelasting op een vervuilend product. Welke soort inkomst is dat?",
        opties=[
            "een indirecte belasting",
            "een directe belasting",
            "een diverse inkomst",
            "een inkomst uit het kapitaal dat de overheid zelf bezit",
        ],
        antwoord=0,
        uitleg="Ze zit in de prijs van het product. De fiche noemt ze naast de btw als voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel soorten inkomsten van de overheid noemt de fiche?",
        opties=["vier", "twee", "drie", "vijf"],
        antwoord=0,
        uitleg="Directe belastingen, indirecte belastingen, diverse inkomsten en inkomsten uit overheidskapitaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je betaalt om een paspoort aan te vragen bij de gemeente. Welke soort inkomst is dat?",
        opties=[
            "een vergoeding voor een dienst, dus een diverse inkomst",
            "een directe belasting op je persoon, zoals de personenbelasting",
            "een indirecte belasting die in de prijs verrekend zit",
            "een inkomst uit het kapitaal dat de overheid zelf bezit",
        ],
        antwoord=0,
        uitleg="De fiche noemt vergoedingen voor diensten bij de diverse inkomsten, naast boetes.",
    ),
    dict(
        type="waarofniet",
        vraag="De btw is een indirecte belasting.",
        antwoord=True,
        uitleg="Ze zit in de prijs en de verkoper stort ze door.",
    ),
    dict(
        type="waarofniet",
        vraag="De bedrijfsvoorheffing is een indirecte belasting.",
        antwoord=False,
        uitleg="Ze wordt rechtstreeks op je loon geheven, dus ze is direct.",
    ),
    dict(
        type="waarofniet",
        vraag="Boetes horen volgens de fiche bij de diverse inkomsten van de overheid.",
        antwoord=True,
        uitleg="Ze staan er samen met de vergoedingen voor diensten.",
    ),
    dict(
        type="waarofniet",
        vraag="De verkoop van een stuk grond door de overheid is een belasting.",
        antwoord=False,
        uitleg="Dat is een inkomst uit overheidskapitaal, geen belasting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze noemt de fiche als soort inkomst van de overheid?",
        opties=[
            "directe belastingen",
            "indirecte belastingen",
            "inkomsten uit overheidskapitaal",
            "giften van burgers",
        ],
        antwoord=[0, 1, 2],
        uitleg="Giften staan niet in de fiche. De vierde soort is de diverse inkomsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden geeft de fiche bij de indirecte belastingen?",
        opties=["de btw", "de milieubelasting", "de accijnzen op brandstof", "de onroerende voorheffing"],
        antwoord=[0, 1, 2],
        uitleg="De onroerende voorheffing is direct. Accijnzen zitten net als btw in de prijs.",
    ),
    dict(
        type="invultekst",
        vraag="Welke indirecte belasting zit in de prijs van bijna alles wat je koopt? Antwoord met de afkorting.",
        antwoord=["btw", "BTW"],
        uitleg="De btw is het voorbeeld dat de fiche vooraan zet bij de indirecte belastingen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke directe belasting houdt je werkgever op je loon in? Antwoord met één woord.",
        antwoord=["bedrijfsvoorheffing", "de bedrijfsvoorheffing"],
        uitleg="Ze staat in de fiche als voorbeeld van een directe belasting.",
    ),
    dict(
        type="invultekst",
        vraag="Welke directe belasting betaal je op een huis of een stuk grond dat je bezit?",
        antwoord=["onroerende voorheffing", "de onroerende voorheffing"],
        uitleg="Onroerend betekent vastgoed: grond en gebouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heft een overheid volgens de fiche belastingen?",
        opties=[
            "om haar uitgaven voor de samenleving te kunnen betalen",
            "om de prijzen op de markt zo laag mogelijk te houden",
            "om de winst van de bedrijven in het land te verhogen",
            "om geld opzij te zetten voor economisch moeilijke jaren",
        ],
        antwoord=0,
        uitleg="De fiche koppelt de inkomsten meteen aan de vier soorten uitgaven.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zijn collectieve behoeften?",
        opties=[
            "behoeften waar de hele samenleving van gebruikmaakt",
            "behoeften die alleen voor grote gezinnen gelden",
            "behoeften die mensen samen aankopen in groep",
            "behoeften van verenigingen in plaats van personen",
        ],
        antwoord=0,
        uitleg="Veiligheid, onderwijs en openbaar vervoer zijn de voorbeelden uit de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden geeft de fiche bij het voorzien in collectieve behoeften?",
        opties=[
            "veiligheid, onderwijs en openbaar vervoer",
            "cultuur, sport en infocampagnes",
            "handel, transport en digitale infrastructuur",
            "sociale woningen en projecten tegen armoede",
        ],
        antwoord=0,
        uitleg="De andere drie rijtjes horen bij de andere soorten uitgaven.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid legt glasvezel aan in een industriezone. Bij welke soort uitgave hoort dat?",
        opties=[
            "investeren in economische groei en ontwikkeling",
            "voorzien in de collectieve behoeften van de bevolking",
            "bijdragen aan het maatschappelijk en culturele leven",
            "sociale uitgaven en uitkeringen voor wie het nodig heeft",
        ],
        antwoord=0,
        uitleg="Digitale infrastructuur staat in de fiche als voorbeeld bij economische groei.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid betaalt een festival en een sporthal. Bij welke soort uitgave hoort dat?",
        opties=[
            "bijdragen aan het maatschappelijk en culturele leven",
            "voorzien in de collectieve behoeften van de bevolking",
            "investeren in economische groei",
            "sociale uitgaven en uitkeringen voor wie het nodig heeft",
        ],
        antwoord=0,
        uitleg="Cultuur en sport staan in de fiche bij het maatschappelijk leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid bouwt sociale woningen. Bij welke soort uitgave hoort dat?",
        opties=[
            "sociale uitgaven en uitkeringen voor wie het nodig heeft",
            "voorzien in de collectieve behoeften van de bevolking",
            "bijdragen aan het maatschappelijk en culturele leven",
            "investeren in economische groei",
        ],
        antwoord=0,
        uitleg="Sociale woningen staan in de fiche naast de sociale zekerheid en de projecten tegen armoede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een infocampagne over gezond eten. Bij welke soort uitgave hoort dat?",
        opties=[
            "bijdragen aan het maatschappelijk en culturele leven",
            "sociale uitgaven en uitkeringen voor wie het nodig heeft",
            "voorzien in de collectieve behoeften van de bevolking",
            "investeren in economische groei",
        ],
        antwoord=0,
        uitleg="Infocampagnes staan in de fiche bij het maatschappelijk leven, naast cultuur en sport.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid investeert in duurzaamheid. Bij welke soort uitgave hoort dat volgens de fiche?",
        opties=[
            "investeren in economische groei en ontwikkeling",
            "sociale uitgaven en uitkeringen voor wie het nodig heeft",
            "voorzien in de collectieve behoeften van de bevolking",
            "bijdragen aan het maatschappelijk en culturele leven",
        ],
        antwoord=0,
        uitleg="Duurzaamheid staat er naast handel, transport en digitale infrastructuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="De overheid financiert de sociale zekerheid. Bij welke soort uitgave hoort dat?",
        opties=[
            "sociale uitgaven en uitkeringen voor wie het nodig heeft",
            "investeren in economische groei",
            "voorzien in de collectieve behoeften van de bevolking",
            "bijdragen aan het maatschappelijk en culturele leven",
        ],
        antwoord=0,
        uitleg="De financiering van de sociale zekerheid staat vooraan bij de sociale uitgaven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel soorten uitgaven van de overheid noemt de fiche?",
        opties=["vier", "drie", "vijf", "zes"],
        antwoord=0,
        uitleg="Collectieve behoeften, economische groei, maatschappelijk leven en sociale uitgaven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de invloed van de uitgaven van de overheid op de samenleving?",
        opties=[
            "ze bepalen mee wat er voor iedereen beschikbaar is",
            "ze hebben enkel effect op wie een uitkering krijgt",
            "ze veranderen vooral de prijzen in de winkel",
            "ze raken enkel de bedrijven en niet de gezinnen",
        ],
        antwoord=0,
        uitleg="Van scholen tot bussen tot sociale woningen: de uitgaven bepalen mee hoe een samenleving eruitziet.",
    ),
    dict(
        type="waarofniet",
        vraag="Onderwijs staat volgens de fiche bij de collectieve behoeften.",
        antwoord=True,
        uitleg="Samen met veiligheid en openbaar vervoer.",
    ),
    dict(
        type="waarofniet",
        vraag="De financiering van de sociale zekerheid is een inkomst van de overheid.",
        antwoord=False,
        uitleg="Het is een uitgave, en ze staat in het rijtje van de sociale uitgaven.",
    ),
    dict(
        type="waarofniet",
        vraag="Investeren in digitale infrastructuur hoort volgens de fiche bij de economische groei.",
        antwoord=True,
        uitleg="Ze staat er naast handel en transport en duurzaamheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Cultuur en sport zijn volgens de fiche sociale uitgaven.",
        antwoord=False,
        uitleg="Ze horen bij het bijdragen aan het maatschappelijk leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze noemt de fiche als soort uitgave van de overheid?",
        opties=[
            "voorzien in de collectieve behoeften van de bevolking",
            "investeren in economische groei en ontwikkeling",
            "sociale uitgaven en uitkeringen voor wie het nodig heeft",
            "het terugbetalen van belastingen aan bedrijven",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vierde soort is bijdragen aan het maatschappelijk leven. Terugbetalingen aan bedrijven staan er niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voorbeelden geeft de fiche bij de sociale uitgaven?",
        opties=[
            "de financiering van de sociale zekerheid",
            "sociale woningen",
            "projecten tegen armoede",
            "de bouw van een nieuwe rechtbank",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een rechtbank hoort eerder bij veiligheid, en dat is een collectieve behoefte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt de fiche behoeften waar de hele samenleving van gebruikmaakt? Vul aan: ... behoeften.",
        antwoord=["collectieve", "collectief"],
        uitleg="Veiligheid, onderwijs en openbaar vervoer zijn de voorbeelden.",
    ),
    dict(
        type="invultekst",
        vraag="Bij welke soort uitgave horen sociale woningen en projecten tegen armoede? Vul aan: ... uitgaven.",
        antwoord=["sociale"],
        uitleg="Daar staat ook de financiering van de sociale zekerheid bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente kiest tussen een nieuwe bibliotheek en een nieuwe fietsbrug. Welke twee soorten uitgaven staan hier tegenover elkaar?",
        opties=[
            "het maatschappelijk leven en een collectieve behoefte",
            "een sociale uitgave en een collectieve behoefte",
            "economische groei en een sociale uitgave",
            "een diverse inkomst en een sociale uitgave",
        ],
        antwoord=0,
        uitleg="Een bibliotheek hoort bij cultuur, een fietsbrug bij het openbaar vervoer en de mobiliteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche naar de invloed van inkomsten én uitgaven samen?",
        opties=[
            "omdat de overheid met die twee de ongelijkheid probeert te beperken",
            "omdat de inkomsten en de uitgaven altijd exact gelijk moeten zijn",
            "omdat de uitgaven van een overheid altijd hoger liggen dan haar inkomsten",
            "omdat de burger enkel de inkomsten voelt en nooit de uitgaven",
        ],
        antwoord=0,
        uitleg="Dat staat zo in het leerdoel: via inkomsten en uitgaven heeft de overheid impact en probeert ze ongelijkheid te beperken.",
    ),
]
