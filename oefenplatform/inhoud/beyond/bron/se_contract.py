# -*- coding: utf-8 -*-
"""De arbeidsovereenkomst en het arbeidsreglement.

Het eerste van drie thema's uit "ik ga werken", dat vijftien procent weegt en
daarmee samen met de financiën het zwaarste blok van de fiche is na het
digitale.

De fiche deelt de arbeidsovereenkomsten op drie manieren in, en vraagt ze aan
die drie te herkennen:

    naar de aard van het werk     arbeider, bediende
    naar de duur                  bepaalde duur, onbepaalde duur,
                                  vervangingsduur, welomschreven werk
    naar de omvang                deeltijds, voltijds

Ze vraagt ook uitdrukkelijk om te kunnen bepalen of een recht of een plicht
in de arbeidsovereenkomst dan wel in het arbeidsreglement thuishoort. Het
verschil in één zin: de overeenkomst gaat over jouw afspraak met deze
werkgever, het reglement over de regels die voor iedereen in het bedrijf
gelden.

Op het examen krijg je bronmateriaal: een arbeidsovereenkomst, een
arbeidsreglement, een krantenartikel, een brochure, een loonfiche of een
wettekst. De arbeidssituaties die de fiche noemt, komen hier terug: de
beëindiging, de proefperiode bij studenten, de schorsing, het verbod op
nachtarbeid, de loonnormen en de uitbetaling, en overwerk met overloon.

Deel 1 is de soorten arbeidsovereenkomst.
Deel 2 is de overeenkomst tegenover het reglement, en de arbeidssituaties.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een arbeidsovereenkomst?",
        opties=[
            "de afspraak tussen één werknemer en zijn werkgever",
            "de regels die in het hele bedrijf gelden",
            "de wet over werken in België",
            "het document met je loon van vorige maand",
        ],
        antwoord=0,
        uitleg="Het reglement geldt voor iedereen, de overeenkomst is van jou alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke drie manieren deelt de fiche de arbeidsovereenkomsten in?",
        opties=[
            "naar de aard van het werk, de duur en de omvang van de prestaties",
            "naar het loon, de sector en de leeftijd",
            "naar het statuut, de werkgever en de woonplaats",
            "naar de opleiding, de ervaring en het contracttype",
        ],
        antwoord=0,
        uitleg="Die drie indelingen staan los van elkaar: elk contract valt in alle drie een vakje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee soorten onderscheidt de fiche naar de aard van het werk?",
        opties=[
            "arbeiders en bedienden",
            "voltijds en deeltijds",
            "bepaalde en onbepaalde duur",
            "vast en tijdelijk",
        ],
        antwoord=0,
        uitleg="Arbeider en bediende gaan over de aard van het werk, niet over de duur of de omvang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten onderscheidt de fiche naar de duur?",
        opties=[
            "bepaalde duur, onbepaalde duur, vervangingsduur en welomschreven werk",
            "bepaalde duur en onbepaalde duur",
            "voltijds, deeltijds en seizoenswerk",
            "proefperiode, vaste benoeming en interim",
        ],
        antwoord=0,
        uitleg="Vier soorten, en de vervangingsduur en het welomschreven werk worden vaak vergeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wordt aangeworven om een collega te vervangen die met ziekteverlof is. Welke duur heeft dat contract?",
        opties=[
            "een vervangingsduur",
            "een bepaalde duur",
            "een onbepaalde duur",
            "een welomschreven werk",
        ],
        antwoord=0,
        uitleg="Het contract loopt tot de afwezige terug is, en dat is geen vaste datum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wordt aangenomen om één dak te vernieuwen, en het contract eindigt als dat dak klaar is. Welke duur is dat?",
        opties=[
            "een welomschreven werk",
            "een bepaalde duur",
            "een vervangingsduur",
            "een onbepaalde duur",
        ],
        antwoord=0,
        uitleg="Niet de datum maar de opdracht bepaalt het einde. Dat is een duidelijk omschreven werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een contract loopt van 1 maart tot en met 31 augustus. Welke duur is dat?",
        opties=[
            "een bepaalde duur",
            "een onbepaalde duur",
            "een vervangingsduur",
            "een welomschreven werk",
        ],
        antwoord=0,
        uitleg="Er staat een einddatum in, dus de duur is bepaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een contract zonder einddatum. Welke duur is dat?",
        opties=[
            "een onbepaalde duur",
            "een bepaalde duur",
            "een welomschreven werk",
            "een vervangingsduur",
        ],
        antwoord=0,
        uitleg="Het loopt door tot een van de twee partijen het beëindigt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee soorten onderscheidt de fiche naar de omvang van de prestaties?",
        opties=[
            "deeltijds en voltijds",
            "arbeider en bediende",
            "bepaalde en onbepaalde duur",
            "vast en los",
        ],
        antwoord=0,
        uitleg="De omvang gaat over hoeveel uren je werkt, niet over wat voor werk het is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand werkt drie dagen per week, voor onbepaalde tijd, als bediende. Hoe noem je dat contract?",
        opties=[
            "een deeltijdse bediendenovereenkomst van onbepaalde duur",
            "een voltijdse arbeidersovereenkomst van bepaalde duur",
            "een vervangingsovereenkomst",
            "een overeenkomst voor een welomschreven werk",
        ],
        antwoord=0,
        uitleg="Alle drie de indelingen zitten in die ene naam: omvang, aard en duur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een contract van bepaalde duur heeft altijd een einddatum of een duidelijk eindpunt.",
        antwoord=True,
        uitleg="Daarom heet de duur bepaald. Bij een onbepaalde duur staat er geen einde in.",
    ),
    dict(
        type="waarofniet",
        vraag="Arbeider en bediende gaan volgens de fiche over de duur van het contract.",
        antwoord=False,
        uitleg="Ze gaan over de aard van het werk. De duur is een andere indeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vervangingsovereenkomst loopt tot de vervangen collega terug is.",
        antwoord=True,
        uitleg="Daarom valt er geen vaste einddatum op te schrijven.",
    ),
    dict(
        type="waarofniet",
        vraag="Deeltijds werken kan enkel met een contract van bepaalde duur.",
        antwoord=False,
        uitleg="De omvang en de duur staan los van elkaar. Deeltijds kan ook voor onbepaalde tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten naar de duur noemt de fiche?",
        opties=[
            "de bepaalde duur",
            "de vervangingsduur",
            "het welomschreven werk",
            "de proefduur",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vierde is de onbepaalde duur. Een proefduur staat niet als eigen soort in het rijtje.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet een contract dat loopt tot een afwezige collega terugkomt? Vul aan: een contract voor een ...",
        antwoord=["vervangingsduur", "vervanging"],
        uitleg="Een van de vier soorten naar de duur.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet een contract zonder einddatum? Vul aan: een contract van ... duur.",
        antwoord=["onbepaalde", "onbepaald"],
        uitleg="Het loopt door tot een van beide partijen het beëindigt.",
    ),
    dict(
        type="invultekst",
        vraag="Welke twee statuten onderscheidt de fiche naar de aard van het werk? Antwoord met het woord voor wie bureauwerk doet.",
        antwoord=["bediende", "bedienden"],
        uitleg="Arbeider en bediende zijn de twee soorten naar de aard van het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een arbeidsovereenkomst belangrijk voor de werknemer?",
        opties=[
            "ze legt zijn loon, uren en taken zwart op wit vast",
            "ze geeft hem recht op een uitkering bij werkloosheid",
            "ze bepaalt hoeveel belastingen hij betaalt",
            "ze vervangt het arbeidsreglement van het bedrijf",
        ],
        antwoord=0,
        uitleg="Wat afgesproken is, staat erin. Bij onenigheid is dat waar je op terugvalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een arbeidsovereenkomst belangrijk voor de werkgever?",
        opties=[
            "ze legt vast wat hij van de werknemer mag verwachten",
            "ze zorgt dat hij geen RSZ moet betalen",
            "ze vervangt de wet op de arbeidsovereenkomsten",
            "ze maakt ontslag onmogelijk",
        ],
        antwoord=0,
        uitleg="De fiche vraagt het belang voor beide partijen, niet alleen voor de werknemer.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een arbeidsreglement?",
        opties=[
            "de regels die voor iedereen in het bedrijf gelden",
            "de persoonlijke afspraak tussen werkgever en werknemer",
            "de wet op de arbeidsovereenkomsten",
            "het overzicht van je loon per maand",
        ],
        antwoord=0,
        uitleg="Het reglement is van het bedrijf, de overeenkomst is van jou.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het uurrooster dat voor de hele ploeg geldt. Waar hoort dat thuis?",
        opties=[
            "in het arbeidsreglement",
            "in de arbeidsovereenkomst",
            "op de loonfiche",
            "in de wettekst",
        ],
        antwoord=0,
        uitleg="Wat voor iedereen geldt, staat in het reglement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Jouw persoonlijke brutoloon. Waar hoort dat thuis?",
        opties=[
            "in de arbeidsovereenkomst",
            "in het arbeidsreglement",
            "in de wet",
            "in de brochure van de vakbond",
        ],
        antwoord=0,
        uitleg="Jouw loon is een afspraak tussen jou en je werkgever, geen regel voor iedereen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De regels over hoe je ziekte moet melden in het bedrijf. Waar hoort dat thuis?",
        opties=[
            "in het arbeidsreglement",
            "in de arbeidsovereenkomst",
            "op je loonfiche",
            "in je individuele rekening",
        ],
        antwoord=0,
        uitleg="Die procedure geldt voor alle werknemers, dus ze staat in het reglement.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is overloon?",
        opties=[
            "een toeslag bovenop het gewone loon voor overwerk",
            "het loon dat je te veel gekregen hebt",
            "het loon van een leidinggevende",
            "het deel van je loon dat belast wordt",
        ],
        antwoord=0,
        uitleg="Wie buiten zijn gewone uren werkt, krijgt daar een toeslag voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een schorsing van de arbeidsovereenkomst?",
        opties=[
            "het contract blijft bestaan maar het werk ligt tijdelijk stil",
            "het contract wordt definitief beëindigd",
            "de werknemer krijgt een officiële waarschuwing",
            "het loon wordt een maand ingehouden",
        ],
        antwoord=0,
        uitleg="Bij ziekte of zwangerschapsrust loopt het contract door terwijl je niet werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het verbod op nachtarbeid?",
        opties=[
            "werken tijdens de nacht mag in principe niet, met uitzonderingen",
            "nachtwerk mag altijd als je er een toeslag voor krijgt",
            "nachtwerk is overal verboden zonder uitzondering",
            "nachtwerk mag enkel voor bedienden",
        ],
        antwoord=0,
        uitleg="De fiche noemt het als arbeidssituatie. Er bestaan wettelijke uitzonderingen, bijvoorbeeld in de zorg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk bronmateriaal kan je volgens de fiche op het examen krijgen?",
        opties=[
            "een arbeidsovereenkomst, een arbeidsreglement of een loonfiche",
            "enkel een wettekst",
            "enkel de brochure van een vakbond",
            "een filmpje van je toekomstige werkgever",
        ],
        antwoord=0,
        uitleg="De fiche noemt daarnaast ook een krantenartikel en een brochure.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de rechten van de werknemer?",
        opties=[
            "op tijd zijn loon ontvangen",
            "het werk uitvoeren zoals afgesproken",
            "de instructies van de werkgever volgen",
            "zorgvuldig met het materiaal omgaan",
        ],
        antwoord=0,
        uitleg="De drie andere zijn plichten van de werknemer, geen rechten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de plichten van de werkgever?",
        opties=[
            "zorgen voor een veilige werkplek",
            "op tijd op het werk komen",
            "de instructies van de ploegbaas volgen",
            "het werk zorgvuldig uitvoeren",
        ],
        antwoord=0,
        uitleg="De andere drie zijn plichten van de werknemer.",
    ),
    dict(
        type="waarofniet",
        vraag="Het arbeidsreglement geldt voor alle werknemers van het bedrijf.",
        antwoord=True,
        uitleg="Daarom staat jouw persoonlijke loon er niet in.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een schorsing van de arbeidsovereenkomst is het contract beëindigd.",
        antwoord=False,
        uitleg="Het contract loopt door, alleen het werk ligt tijdelijk stil.",
    ),
    dict(
        type="waarofniet",
        vraag="Overwerk geeft recht op een toeslag, het overloon.",
        antwoord=True,
        uitleg="De fiche noemt overwerk en overloon samen als arbeidssituatie.",
    ),
    dict(
        type="waarofniet",
        vraag="Op het examen krijg je nooit bronmateriaal zoals een loonfiche te zien.",
        antwoord=False,
        uitleg="Een loonfiche staat juist in het rijtje bronnen, naast de overeenkomst, het reglement, een artikel, een brochure en een wettekst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke arbeidssituaties noemt de fiche?",
        opties=[
            "de beëindiging van de arbeidsovereenkomst",
            "de schorsing van de arbeidsovereenkomst",
            "overwerk en overloon",
            "de jaarlijkse evaluatie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een evaluatie staat niet in het rijtje. De proefperiode bij studenten, het verbod op nachtarbeid en de loonnormen wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in de arbeidsovereenkomst en niet in het arbeidsreglement?",
        opties=[
            "jouw functie",
            "jouw loon",
            "de duur van jouw contract",
            "de openingsuren van het bedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="De openingsuren gelden voor iedereen en staan dus in het reglement.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de toeslag die je krijgt voor uren buiten je gewone werktijd?",
        antwoord=["overloon", "het overloon"],
        uitleg="De fiche noemt overwerk en overloon samen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het tijdelijk stilvallen van het werk terwijl het contract blijft bestaan?",
        antwoord=["schorsing", "een schorsing"],
        uitleg="Bijvoorbeeld bij ziekte. Het contract wordt niet beëindigd.",
    ),
    dict(
        type="invultekst",
        vraag="In welk document staan de regels die voor alle werknemers van een bedrijf gelden?",
        antwoord=["arbeidsreglement", "het arbeidsreglement"],
        uitleg="De persoonlijke afspraken staan in de arbeidsovereenkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een student mag van zijn baas twee weken proberen voor beide beslissen of ze doorgaan. Welke arbeidssituatie is dat?",
        opties=[
            "de proefperiode bij studenten",
            "de schorsing van de arbeidsovereenkomst",
            "een contract voor een welomschreven werk",
            "het verbod op nachtarbeid",
        ],
        antwoord=0,
        uitleg="De fiche noemt de proefperiode bij studenten als aparte arbeidssituatie.",
    ),
]
