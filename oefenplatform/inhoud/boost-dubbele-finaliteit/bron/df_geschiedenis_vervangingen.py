# -*- coding: utf-8 -*-
"""De dertien vragen die bij dubbele finaliteit anders moeten dan bij doorstroom.

De sleutel is de vráág van de doorstroomversie, woord voor woord. `bouw_geschiedenis.py`
zoekt ze op en zet er deze vraag voor in de plaats; staat een sleutel niet (meer)
in de doorstroombestanden, dan stopt het script met een foutmelding. Zo kan een
aanpassing aan de doorstroomvragen hier nooit stil voorbijgaan.

Elke vervanging heeft hetzelfde type als de vraag die ze vervangt, en bij waar
of niet waar dezelfde waarheidswaarde, zodat het evenwicht per hoofdstuk blijft
kloppen. Bij een meerkeuzevraag met meerdere juiste antwoorden blijven het er
meerdere, zodat het aandeel van 20 à 30 % niet verschuift.

De inhoud komt uit de DF-fiche zelf: de lokale en langeafstandshandel, de
verwevenheid van stad en platteland, ambachten en gilden, Bagdad als kruispunt
van internationale handel, de driehoekshandel, de organisatievormen van de
commerciële revolutie, de nieuwe betaalmiddelen, de landbouwvernieuwingen, het
standpunt over slavenhandel in verschillende bronnen, de David van Michelangelo
en de aard van het interculturele contact tussen moslims en christenen.
"""

VERVANGINGEN = {
    # ── Standen, domein en stad — deel 1
    "Wat betekent het dat het domein zelfvoorzienend was?": dict(
        type="meerkeuze",
        vraag="Welk product hoort bij de langeafstandshandel en niet bij de lokale handel?",
        opties=[
            "specerijen die van heel ver uit Azië worden aangevoerd",
            "brood dat de bakker in de straat zelf gebakken heeft",
            "groenten die de boer uit het dorp op de markt brengt",
            "brandhout dat men in het bos naast de stad gaat halen",
        ],
        antwoord=0,
        uitleg="Lokale handel gaat over dagelijkse waren van dichtbij. Langeafstandshandel "
               "brengt dure, lichte goederen die de lange reis waard zijn.",
    ),
    # ── Standen, domein en stad — deel 2
    "Wat betekent het ontstaan van een geldeconomie?": dict(
        type="meerkeuze",
        vraag="Hoe zijn de stad en het platteland in de middeleeuwen met elkaar verweven?",
        opties=[
            "het platteland levert het voedsel, de stad levert gereedschap en laken",
            "de stad en het platteland hebben in die tijd niets met elkaar te maken",
            "het platteland koopt alles in de stad en levert er zelf helemaal niets",
            "de stad verbouwt haar eigen graan en heeft het platteland niet nodig",
        ],
        antwoord=0,
        uitleg="Zonder de boeren eromheen kan een stad niet eten; zonder de stad heeft de boer "
               "geen markt en geen gereedschap.",
    ),
    "Met de geldeconomie komen er ook wisselaars, kredietvormen en boekhouding op.": dict(
        type="waarofniet",
        vraag="Ambachten en gilden bepaalden mee wie in de stad een beroep mocht uitoefenen.",
        antwoord=True,
        uitleg="Een gilde legde vast wie meester kon worden, hoeveel leerjongens je mocht "
               "hebben en welke kwaliteit je werk moest halen.",
    ),
    "In welk maatschappelijk domein hoort het ontstaan van de geldeconomie in de eerste plaats thuis?": dict(
        type="meerkeuze",
        vraag="In welk maatschappelijk domein horen de ambachten en gilden in de eerste plaats thuis?",
        opties=[
            "het economische domein",
            "het militaire domein",
            "het culturele domein",
            "het religieuze domein",
        ],
        antwoord=0,
        uitleg="Het gaat over werken, produceren en verkopen. Dat een gilde ook een altaar in "
               "de kerk onderhield, maakt haar daarnaast ook cultureel.",
    ),
    # ── Geloof, kunst en macht in de middeleeuwen — deel 1
    "De organisatie van de katholieke Kerk situeer je vooral in welk maatschappelijk domein?": dict(
        type="meerkeuze",
        vraag="Waarom was Bagdad in de middeleeuwen een kruispunt van internationale handel?",
        opties=[
            "de stad lag waar de routes tussen Azië, Afrika en Europa samenkwamen",
            "de stad lag aan de Atlantische Oceaan en beheerste de zeeroutes",
            "de stad lag midden in Europa en was er de grootste van allemaal",
            "de stad lag naast de zilvermijnen waar alle munten gemaakt werden",
        ],
        antwoord=0,
        uitleg="Op een kaart zie je het meteen: de zijderoutes uit het oosten en de wegen naar "
               "de Middellandse Zee komen er samen.",
    ),
    # ── De 'Nieuwe' Wereld en de driehoekshandel — deel 1
    "De demografische inzinking, het encomiendasysteem en de Afrikaanse slavenhandel hangen met elkaar samen.": dict(
        type="waarofniet",
        vraag="De demografische inzinking van de precolumbiaanse bevolking, de Afro-Amerikaanse "
              "slavenhandel en de driehoekshandel hangen met elkaar samen.",
        antwoord=True,
        uitleg="Stierf de inheemse bevolking weg, dan viel de arbeidskracht in de kolonies weg. "
               "Die werd gehaald in Afrika, en zo draaide de driehoekshandel.",
    ),
    # ── De 'Nieuwe' Wereld en de driehoekshandel — deel 2
    "Wat zijn kenmerken van het handelskapitalisme?": dict(
        type="meerkeuze",
        vraag="Welke organisatievormen van ondernemingen horen bij de commerciële revolutie?",
        opties=[
            "de handelscompagnie",
            "de manufactuur",
            "de huisnijverheid",
            "de staatsfabriek die volledig van de koning is",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie horen bij de commerciële revolutie. Een fabriek die volledig van "
               "de staat is, hoort bij een veel latere tijd.",
    ),
    "Wat houdt mercantilisme in?": dict(
        type="meerkeuze",
        vraag="Hoe ontstaan er nieuwe betaalmiddelen als gevolg van de commerciële revolutie?",
        opties=[
            "handelaars gebruiken een wisselbrief in plaats van munten mee te zeulen",
            "iedere koopman mag vanaf dan zijn eigen gouden munten laten slaan",
            "de vorst schaft alle munten af en laat enkel nog ruilhandel toe",
            "men betaalt voortaan uitsluitend met goederen en nooit meer met geld",
        ],
        antwoord=0,
        uitleg="Met een wisselbrief betaal je in de ene stad en haal je het geld in de andere. "
               "Daaruit groeit het bankwezen.",
    ),
    "Volgens het mercantilisme is vrije handel met alle landen het beste voor een vorst.": dict(
        type="waarofniet",
        vraag="Bij huisnijverheid werken de arbeiders samen in één grote fabriek van de ondernemer.",
        antwoord=False,
        uitleg="Bij huisnijverheid werkt men thuis, met materiaal dat de ondernemer brengt en "
               "ophaalt. In één werkplaats samenwerken is de manufactuur.",
    ),
    "Wat is het verband tussen landbouwproductiviteit en bevolkingsgroei?": dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de landbouwproductiviteit en de technische vernieuwingen?",
        opties=[
            "betere werktuigen en methodes laten dezelfde grond meer opbrengen",
            "nieuwe werktuigen maken de grond na een paar jaar juist onvruchtbaar",
            "de twee hebben niets met elkaar te maken en verlopen los van elkaar",
            "meer opbrengst zorgt ervoor dat men geen werktuigen meer nodig heeft",
        ],
        antwoord=0,
        uitleg="Een betere ploeg, een ander vruchtwisselstelsel of een nieuw gewas: telkens "
               "haalt dezelfde akker meer voedsel op.",
    ),
    "Wat is het verband tussen de ontdekkingsreizen en het handelskapitalisme?": dict(
        type="meerkeuze",
        vraag="Twee bronnen geven een heel ander standpunt over de slavenhandel. Wat doe je dan?",
        opties=[
            "nagaan wie elke bron maakte en met welke bedoeling, en de twee afwegen",
            "de bron kiezen die het kortst is, want die is het makkelijkst te lezen",
            "allebei de bronnen weggooien, want een van de twee moet wel liegen",
            "de bron geloven die het oudst is, want die stond er het dichtst bij",
        ],
        antwoord=0,
        uitleg="Een slavenhandelaar en een tot slaaf gemaakte schrijven allebei de waarheid van "
               "hun kant. Wie ze naast elkaar legt, ziet net daarom meer.",
    ),
    # ── Humanisme, Reformatie, renaissance en barok — deel 1
    "Wat veranderde er aan de wetenschappelijke methode?": dict(
        type="meerkeuze",
        vraag="Waarom behoort het beeld David van Michelangelo tot de renaissance?",
        opties=[
            "het toont de mens zelf, naakt en in klassieke verhoudingen",
            "het is helemaal van goud gemaakt en hoort daarom in een kerkschat",
            "het toont enkel heiligen met een gouden achtergrond, zoals gebruikelijk",
            "het werd geschilderd op het plafond van een kapel in plaats van gehouwen",
        ],
        antwoord=0,
        uitleg="De renaissancekunst zet de mens centraal en kijkt naar Grieken en Romeinen. De "
               "gouden achtergrond hoort bij de middeleeuwse kunst.",
    ),
    # ── Het Ottomaanse Rijk en samenlevingen vergelijken — deel 2
    "Welke economische systemen kan je met elkaar vergelijken?": dict(
        type="meerkeuze",
        vraag="Langs welke wegen liepen de contacten tussen moslims en christenen?",
        opties=[
            "de zijderoutes",
            "de Arabische cultuur en de cultuur van christelijk Europa",
            "de kruistochten",
            "de ontdekkingsreizen naar Amerika",
        ],
        antwoord=[0, 1, 2],
        uitleg="Langs die drie wegen liep het interculturele contact. De ontdekkingsreizen naar "
               "Amerika horen bij de vroegmoderne tijd en bij een heel andere ontmoeting.",
    ),
    # ── De 'Nieuwe' Wereld en de driehoekshandel — deel 1 (invulvraag)
    "Hoe heet het Spaanse systeem waarbij een kolonist arbeid mocht opeisen van de inheemse bevolking?": dict(
        type="invultekst",
        vraag="Hoe heet de oversteek van Afrika naar Amerika, het tweede been van de driehoekshandel?",
        antwoord=["de middenpassage", "middenpassage"],
        uitleg="Op dat been werden tot slaaf gemaakte mensen vervoerd, in omstandigheden die velen "
               "niet overleefden.",
    ),
    # ── Humanisme, Reformatie, renaissance en barok — deel 1
    "Wat bereikte de westerse geneeskunde níét langs de Arabische wereld?": dict(
        type="meerkeuze",
        vraag="Welke stroming hoort níét bij de Reformatie?",
        opties=[
            "de Contrareformatie",
            "het lutheranisme",
            "het anglicanisme",
            "het calvinisme",
        ],
        antwoord=0,
        uitleg="De Contrareformatie is juist het antwoord van de katholieke Kerk op de Reformatie, "
               "geen stroming erbinnen.",
    ),
    "Vesalius toonde aan dat de oude Griekse geneeskundige teksten niet in alles gelijk hadden.": dict(
        type="waarofniet",
        vraag="De renaissancekunst kijkt voor haar voorbeeld terug naar de klassieke oudheid.",
        antwoord=True,
        uitleg="Evenwicht, rust en heldere verhoudingen komen rechtstreeks van de Grieken en de "
               "Romeinen.",
    ),
}
