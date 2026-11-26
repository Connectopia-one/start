# -*- coding: utf-8 -*-
"""Humane wetenschappen: participatie, het kiesstelsel en het kiesrecht.

Het vierde van zes thema's over politieke wetenschappen, enkel voor humane
wetenschappen (fiche 3DDO, onderdeel "Participatie: inspraak van de burger").

De fiche vraagt:

    hoe burgers via verkiezingen deel uitmaken van een representatieve
        democratie
    het kiesstelsel van België: evenredige vertegenwoordiging
    de evolutie van het kiesrecht in België
    vormen van politieke participatie: conventionele en niet-conventionele
    participeren via burgerinitiatieven, referenda en volksraadplegingen,
        belangengroepen, sociale bewegingen
    factoren die participatie beïnvloeden: urbanisatie, gezinssituatie,
        scholingsgraad, leeftijd, gender, digitalisering
    het Belgisch kiesstelsel vergelijken met een ander gegeven kiesstelsel,
        en de invloed van een kiesstelsel op representatie en besluitvorming
    argumenten voor of tegen het afschaffen van de opkomstplicht

De jaartallen van het kiesrecht: cijnskiesrecht (1831), algemeen meervoudig
stemrecht voor mannen met opkomstplicht (1893), algemeen enkelvoudig
stemrecht voor mannen (1919), stemrecht voor vrouwen bij de
parlementsverkiezingen (1948), stemrecht vanaf 18 jaar (1981).

Deel 1 zijn verkiezingen, kiesstelsel en kiesrecht.
Deel 2 zijn de vormen van participatie, de factoren en de opkomstplicht.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe nemen burgers in een representatieve democratie vooral deel aan de politiek?",
        opties=[
            "door bij verkiezingen vertegenwoordigers te kiezen die in hun naam beslissen",
            "door zelf elke week over alle nieuwe wetten te stemmen in het parlement",
            "door de ministers rechtstreeks te benoemen via een brief aan de koning",
            "door als rechter te zetelen in een rechtbank van hun eigen gemeente",
        ],
        antwoord=0,
        uitleg="In een representatieve democratie geven burgers via verkiezingen een mandaat aan vertegenwoordigers. Die beslissen dan in hun naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent evenredige vertegenwoordiging?",
        opties=[
            "een partij krijgt ongeveer hetzelfde deel van de zetels als van de stemmen",
            "de partij met de meeste stemmen in een kieskring krijgt alle zetels van die kieskring",
            "elke partij krijgt evenveel zetels, hoeveel stemmen ze ook haalt",
            "de zetels worden verdeeld volgens het aantal leden van elke partij",
        ],
        antwoord=0,
        uitleg="Wie 20 procent van de stemmen haalt, krijgt ongeveer 20 procent van de zetels. Zo komen ook kleinere partijen in het parlement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk kiesstelsel gebruikt België voor de verkiezingen van het parlement?",
        opties=[
            "evenredige vertegenwoordiging",
            "een meerderheidsstelsel met één winnaar per kieskring",
            "een stelsel waarbij de koning de parlementsleden kiest",
            "een stelsel waarbij enkel de grootste partij zetels krijgt",
        ],
        antwoord=0,
        uitleg="België werkt met evenredige vertegenwoordiging. Daardoor zitten er veel partijen in het parlement en zijn er bijna altijd coalities.",
    ),
    dict(
        type="meerkeuze",
        vraag="In het Verenigd Koninkrijk krijgt per kiesdistrict enkel de kandidaat met de meeste stemmen een zetel. Wat is een gevolg van dat meerderheidsstelsel?",
        opties=[
            "grote partijen krijgen meer zetels dan hun deel van de stemmen",
            "elke partij krijgt precies zoveel procent van de zetels als van de stemmen",
            "er zijn na de verkiezingen altijd coalities van vijf of zes partijen nodig",
            "kleine partijen krijgen meer zetels dan ze stemmen haalden in het land",
        ],
        antwoord=0,
        uitleg="Bij een meerderheidsstelsel gaan de stemmen voor verliezers in een district verloren. Dat bevoordeelt grote partijen en geeft vaak een regering van één partij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voordeel van evenredige vertegenwoordiging?",
        opties=[
            "de zetels weerspiegelen goed hoe de kiezers gestemd hebben",
            "er is na de verkiezingen meestal meteen een regering van één partij",
            "de grootste partij kan beslissen zonder rekening te houden met anderen",
            "er hoeven veel minder kiezers te gaan stemmen",
        ],
        antwoord=0,
        uitleg="Meer stromingen krijgen een stem in het parlement. Het nadeel is dat regeringsvorming moeilijker is, omdat er coalities nodig zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat was het cijnskiesrecht van 1831?",
        opties=[
            "enkel mannen die genoeg belastingen betaalden, mochten stemmen",
            "alle mannen en vrouwen vanaf 21 jaar mochten één stem uitbrengen",
            "alle mannen vanaf 25 jaar mochten stemmen, sommigen meer dan één keer",
            "iedereen mocht stemmen, maar enkel voor de gemeenteraad",
        ],
        antwoord=0,
        uitleg="Cijns betekent belasting. In 1831 mocht maar een klein deel van de mannen stemmen: wie rijk genoeg was om voldoende belasting te betalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat veranderde er in 1893 aan het kiesrecht in België?",
        opties=[
            "algemeen meervoudig stemrecht voor mannen, met opkomstplicht",
            "het stemrecht voor vrouwen bij de verkiezingen van het parlement",
            "het verlagen van de stemleeftijd naar 18 jaar voor alle Belgen",
            "het afschaffen van de opkomstplicht voor alle verkiezingen",
        ],
        antwoord=0,
        uitleg="Vanaf 1893 mochten alle mannen vanaf 25 jaar stemmen, maar wie rijk was, een diploma had of een gezin had, kreeg extra stemmen. Tegelijk kwam de opkomstplicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet deze stappen in de evolutie van het kiesrecht in de juiste volgorde.",
        opties=[
            "cijnskiesrecht, meervoudig stemrecht, enkelvoudig stemrecht voor mannen, stemrecht voor vrouwen",
            "meervoudig stemrecht, cijnskiesrecht, stemrecht voor vrouwen, enkelvoudig stemrecht voor mannen",
            "enkelvoudig stemrecht voor mannen, cijnskiesrecht, stemrecht voor vrouwen, meervoudig stemrecht",
            "cijnskiesrecht, stemrecht voor vrouwen, meervoudig stemrecht, enkelvoudig stemrecht voor mannen",
        ],
        antwoord=0,
        uitleg="1831 cijnskiesrecht, 1893 algemeen meervoudig stemrecht, 1919 algemeen enkelvoudig stemrecht voor mannen, 1948 stemrecht voor vrouwen bij de parlementsverkiezingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Sinds wanneer mogen vrouwen in België stemmen voor het parlement?",
        opties=["sinds 1948", "sinds 1831", "sinds 1893", "sinds 1981"],
        antwoord=0,
        uitleg="Vrouwen mochten al vanaf 1921 stemmen voor de gemeenteraad, maar pas vanaf 1948 voor het parlement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat veranderde er in 1981 aan het stemrecht?",
        opties=[
            "de leeftijd om te mogen stemmen werd verlaagd naar 18 jaar",
            "vrouwen mochten voor het eerst stemmen voor de gemeenteraad",
            "het cijnskiesrecht werd ingevoerd voor de rijkste mannen",
            "rijke mannen kregen voortaan twee of drie stemmen in plaats van één",
        ],
        antwoord=0,
        uitleg="Vroeger moest je 21 jaar zijn om te stemmen. Sinds 1981 is dat 18 jaar.",
    ),
    dict(
        type="invultekst",
        vraag="Het kiesstelsel waarbij partijen ongeveer evenveel procent zetels krijgen als procent stemmen, heet ... vertegenwoordiging.",
        antwoord=["evenredige"],
        uitleg="Evenredig betekent in verhouding. België gebruikt dit stelsel.",
    ),
    dict(
        type="invultekst",
        vraag="Het kiesrecht van 1831, waarbij enkel wie genoeg belasting betaalde mocht stemmen, heet het ...kiesrecht.",
        antwoord=["cijns", "cijnskiesrecht"],
        uitleg="Cijns is een oud woord voor belasting.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het meervoudig stemrecht van 1893 hadden sommige mannen meer stemmen dan andere.",
        antwoord=True,
        uitleg="Wie een diploma, eigendom of een gezin had, kreeg één of twee extra stemmen. Pas in 1919 kreeg elke man één stem.",
    ),
    dict(
        type="waarofniet",
        vraag="In een meerderheidsstelsel krijgen kleine partijen gewoonlijk meer zetels dan bij evenredige vertegenwoordiging.",
        antwoord=False,
        uitleg="Het omgekeerde klopt: een meerderheidsstelsel bevoordeelt grote partijen. Kleine partijen halen zelden een district.",
    ),
    dict(
        type="waarofniet",
        vraag="Het kiesstelsel heeft invloed op hoeveel partijen er in het parlement zitten en hoe een regering gevormd wordt.",
        antwoord=True,
        uitleg="Evenredige vertegenwoordiging geeft veel partijen en coalities. Een meerderheidsstelsel geeft minder partijen en vaker een regering van één partij.",
    ),
    dict(
        type="waarofniet",
        vraag="Vanaf 1831 mochten alle volwassen Belgen stemmen.",
        antwoord=False,
        uitleg="In 1831 mocht maar een kleine groep rijke mannen stemmen. Het stemrecht werd daarna in stappen uitgebreid.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een land met evenredige vertegenwoordiging haalt partij Z 10 procent van de stemmen. Hoeveel van de 150 zetels krijgt ze ongeveer?",
        opties=["ongeveer 15", "ongeveer 10", "geen enkele", "ongeveer 75"],
        antwoord=0,
        uitleg="10 procent van 150 zetels is 15 zetels. Bij evenredige vertegenwoordiging komen de zetels ongeveer overeen met het deel van de stemmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk nadeel hoort vaak bij een meerderheidsstelsel?",
        opties=[
            "stemmen voor de verliezers in een district tellen niet mee",
            "er zijn altijd lange onderhandelingen tussen veel partijen nodig",
            "kleine partijen krijgen meer macht dan hun aantal kiezers",
            "er is geen enkele partij die na de verkiezingen kan regeren",
        ],
        antwoord=0,
        uitleg="Wie op een verliezer stemde, ziet zijn stem niet terug in het parlement. Daardoor kan de verdeling van de zetels ver afwijken van die van de stemmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Sinds 1893 geldt in België een opkomstplicht. Wat houdt die in?",
        opties=[
            "wie stemrecht heeft, moet naar het stembureau gaan",
            "wie stemrecht heeft, moet op een bepaalde partij stemmen",
            "wie kandidaat is, moet in zijn eigen gemeente wonen",
            "wie kiest, moet een geldig stembiljet invullen voor iemand",
        ],
        antwoord=0,
        uitleg="Je moet aanwezig zijn, maar je mag blanco of ongeldig stemmen. Daarom spreek je beter van opkomstplicht dan van stemplicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vroegen arbeiders aan het einde van de 19de eeuw om algemeen stemrecht?",
        opties=[
            "omdat ze door het cijnskiesrecht niet mochten stemmen",
            "omdat ze al meerdere stemmen hadden en er nog meer wilden",
            "omdat vrouwen toen al mochten stemmen en mannen nog niet",
            "omdat de koning de verkiezingen wilde afschaffen",
        ],
        antwoord=0,
        uitleg="Wie weinig verdiende, betaalde te weinig belasting om te mogen stemmen. Na stakingen en acties kwam er in 1893 algemeen meervoudig stemrecht.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is conventionele politieke participatie?",
        opties=[
            "deelnemen via de gewone kanalen, zoals stemmen of lid worden van een partij",
            "deelnemen via acties buiten de gewone kanalen, zoals een betoging of een boycot",
            "niet gaan stemmen en helemaal geen interesse tonen in de politiek van het land",
            "de politiek volgen via sociale media zonder er ooit zelf iets aan te doen",
        ],
        antwoord=0,
        uitleg="Stemmen, kandidaat zijn, lid worden van een partij of een politicus contacteren zijn conventionele vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vormen van niet-conventionele participatie?",
        opties=[
            "deelnemen aan een betoging",
            "een product boycotten om een boodschap te geven",
            "een online petitie ondertekenen",
            "gaan stemmen bij de verkiezingen",
            "lid worden van een politieke partij",
        ],
        antwoord=[0, 1, 2],
        uitleg="Betogingen, boycots en petities gaan buiten de gewone politieke kanalen om. Stemmen en lid worden van een partij zijn conventioneel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een referendum of volksraadpleging?",
        opties=[
            "een stemming waarbij de burgers zelf beslissen over één vraag",
            "een vergadering van het parlement waarin de begroting besproken wordt",
            "een peiling bij duizend kiezers over hun voorkeur voor een partij",
            "een betoging van burgers tegen een beslissing van de regering",
        ],
        antwoord=0,
        uitleg="Bij een referendum of volksraadpleging stemmen de burgers over één vraag. In België gebeurt een volksraadpleging vooral in gemeenten, en het resultaat is niet bindend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een belangengroep?",
        opties=[
            "een organisatie die de belangen van een groep verdedigt bij de politiek",
            "een politieke partij die deelneemt aan de verkiezingen van het parlement",
            "een rechtbank die beslist over conflicten tussen burgers en bedrijven",
            "een groep ministers die samen een nieuw regeerakkoord schrijven",
        ],
        antwoord=0,
        uitleg="Vakbonden, werkgeversorganisaties, boerenbonden en consumentenorganisaties zijn belangengroepen. Ze nemen niet deel aan verkiezingen, maar oefenen druk uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een sociale beweging?",
        opties=[
            "een brede groep mensen die samen actievoert voor een maatschappelijke zaak",
            "een partij die na de verkiezingen samen met andere in de regering stapt",
            "een officieel orgaan dat alle stemmen telt na de verkiezingen",
            "een afdeling van de federale regering die sociale uitkeringen betaalt",
        ],
        antwoord=0,
        uitleg="De klimaatbeweging, de vrouwenbeweging en de vredesbeweging zijn voorbeelden. Ze zijn losser georganiseerd dan een belangengroep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bewoners van een wijk verzamelen handtekeningen om een speelpleintje te laten heraanleggen en brengen hun voorstel op de gemeenteraad. Welke vorm van participatie is dit?",
        opties=["een burgerinitiatief", "een referendum", "een belangengroep", "een verkiezing"],
        antwoord=0,
        uitleg="Burgers nemen zelf het initiatief en brengen een voorstel bij de politiek. Dat is een burgerinitiatief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Duizenden jongeren spijbelen op donderdag om in Brussel te betogen voor een strenger klimaatbeleid. Welke vorm van participatie herken je?",
        opties=[
            "een sociale beweging met niet-conventionele participatie",
            "een belangengroep met conventionele participatie",
            "een referendum georganiseerd door de gemeente",
            "een verkiezing van vertegenwoordigers voor het parlement",
        ],
        antwoord=0,
        uitleg="Een brede groep voert actie buiten de gewone kanalen om. Dat is een sociale beweging die niet-conventioneel participeert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vakbond overlegt met de minister van Werk over een nieuwe regeling voor de pensioenen. Welke vorm van participatie is dit?",
        opties=["een belangengroep die druk uitoefent", "een burgerinitiatief", "een volksraadpleging", "een sociale beweging zonder organisatie"],
        antwoord=0,
        uitleg="Een vakbond verdedigt de belangen van werknemers. Overleg met de regering is een typische manier waarop belangengroepen invloed uitoefenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn factoren die de mate van politieke participatie beïnvloeden?",
        opties=["scholingsgraad", "leeftijd", "gender", "digitalisering", "lichaamslengte", "lievelingskleur"],
        antwoord=[0, 1, 2, 3],
        uitleg="Ook urbanisatie en gezinssituatie spelen een rol. Lichaamslengte en lievelingskleur hebben er niets mee te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit onderzoek blijkt vaak dat hoger opgeleiden meer politiek participeren. Welke factor speelt hier?",
        opties=["de scholingsgraad", "de urbanisatie", "de gezinssituatie", "de gender"],
        antwoord=0,
        uitleg="Wie langer naar school ging, heeft vaak meer kennis en vertrouwen om aan politiek deel te nemen. Dat is de factor scholingsgraad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Jongeren tekenen sneller een online petitie of delen een politiek bericht op sociale media dan dat ze lid worden van een partij. Welke twee factoren zie je hier vooral?",
        opties=[
            "leeftijd en digitalisering",
            "gender en urbanisatie",
            "gezinssituatie en scholingsgraad",
            "urbanisatie en gezinssituatie",
        ],
        antwoord=0,
        uitleg="Jongere mensen participeren vaker op andere manieren, en het internet maakt nieuwe vormen van participatie mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een alleenstaande ouder met drie jonge kinderen heeft weinig tijd om naar politieke vergaderingen te gaan. Welke factor speelt hier?",
        opties=["de gezinssituatie", "de scholingsgraad", "de digitalisering", "de urbanisatie"],
        antwoord=0,
        uitleg="Zorg voor een gezin kost tijd en energie. De gezinssituatie beïnvloedt dus hoeveel iemand politiek kan participeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een argument vóór het afschaffen van de opkomstplicht?",
        opties=[
            "wie stemt, doet dat dan uit eigen overtuiging en niet omdat het moet",
            "zonder opkomstplicht zijn er altijd meer kiezers in elk stembureau van het land",
            "zonder opkomstplicht krijgt elke kiezer in het land meer dan één stem",
            "zonder opkomstplicht hoeft er geen grondwet meer te bestaan",
        ],
        antwoord=0,
        uitleg="Voorstanders vinden stemmen een recht en geen plicht. Ze vinden dat een stem uit vrije wil meer waard is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een argument tegen het afschaffen van de opkomstplicht?",
        opties=[
            "dan stemmen vooral bepaalde groepen en is de uitslag minder representatief",
            "dan mogen vrouwen en jongeren niet meer stemmen bij de verkiezingen",
            "dan verdwijnt het systeem van evenredige vertegenwoordiging voorgoed",
            "dan moet de koning zelf de regering samenstellen zonder het parlement",
        ],
        antwoord=0,
        uitleg="Als vooral sommige groepen gaan stemmen, krijgen hun belangen meer gewicht. Tegenstanders van de afschaffing vrezen dat zwakkere groepen minder gehoord worden.",
    ),
    dict(
        type="invultekst",
        vraag="Een organisatie zoals een vakbond, die de belangen van een groep verdedigt bij de politiek, heet een ...",
        antwoord=["belangengroep", "drukkingsgroep", "belangenorganisatie"],
        uitleg="Belangengroepen of drukkingsgroepen nemen niet deel aan verkiezingen, maar proberen beslissingen te beïnvloeden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een betoging is een vorm van niet-conventionele politieke participatie.",
        antwoord=True,
        uitleg="Een betoging gaat buiten de gewone kanalen zoals verkiezingen of partijen om. Daarom is ze niet-conventioneel, ook al is ze wettelijk toegelaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Belangengroepen nemen deel aan de verkiezingen met hun eigen kandidatenlijsten.",
        antwoord=False,
        uitleg="Dat doen politieke partijen. Belangengroepen oefenen druk uit, maar komen niet op bij verkiezingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Waar je woont, in een stad of op het platteland, kan invloed hebben op hoe je politiek participeert.",
        antwoord=True,
        uitleg="Dat is de factor urbanisatie. In een stad zijn er bijvoorbeeld meer acties en verenigingen, op het platteland kent men de lokale politici vaak beter.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de opkomstplicht ben je verplicht om op een partij of kandidaat te stemmen.",
        antwoord=False,
        uitleg="Je moet enkel naar het stembureau gaan. Wat je daar doet, ook blanco stemmen, is geheim en vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vergelijk je de mate van politieke participatie in een democratie en in een dictatuur?",
        opties=[
            "omdat burgers in een dictatuur veel minder vrij deelnemen aan de politiek",
            "omdat burgers in een dictatuur meer referenda hebben dan in een democratie",
            "omdat er in een democratie geen verkiezingen georganiseerd worden",
            "omdat in een dictatuur iedereen lid moet zijn van een belangengroep",
        ],
        antwoord=0,
        uitleg="In een dictatuur zijn verkiezingen niet vrij en worden betogingen of kritische groepen vaak verboden. De staatsvorm bepaalt dus mee hoeveel burgers kunnen participeren.",
    ),
]
