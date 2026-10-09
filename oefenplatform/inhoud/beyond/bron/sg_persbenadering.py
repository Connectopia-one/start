# -*- coding: utf-8 -*-
"""Persoonlijkheid: van Freud over Bandura naar Rogers.

Drie benaderingen van persoonlijkheid in één thema: de psychodynamische, de
cognitieve en de humanistische. Ze staan samen omdat ze dezelfde vraag anders
beantwoorden: wat houdt een persoonlijkheid in beweging?

De begrippen staan letterlijk in de fiche:

    psychodynamische benadering: de psychoanalyse van Sigmund Freud
        bewustzijnsniveaus: het onbewuste (met verdringing), het onder- of
            voorbewuste, het bewuste
        persoonlijkheidsstructuur: het Es of Id (eros of levensdrift,
            thanatos of doodsdrift, lustprincipe), het Ich of Ego
            (realiteitsprincipe), het Über-ich of Superego
            (moraliteitsprincipe)
    cognitieve benadering
        sociaal-cognitieve leertheorie: Albert Bandura - wederzijds
            determinisme (cognities en eigenschappen, omgeving, gedrag),
            zelfeffectiviteit
        locus of control theory: Julian Rotter - interne en externe locus of
            control
    humanistische benadering
        motivatietheorie: Abraham Maslow - behoeftepiramide, zelfactualisatie
        client-centered therapy: Carl Rogers - fenomenale veld, het actuele en
            het ideale zelf, zelfactualisatie, congruentie en incongruentie

Let op: de locus van controle bij Weiner (sociale psychologie) en de locus of
control bij Rotter (persoonlijkheid) lijken op elkaar, maar staan in de fiche
bij verschillende theorieën. Bij Weiner is het een dimensie van één attributie,
bij Rotter een vaste eigenschap van een persoon.

Deel 1 is de psychodynamische benadering.
Deel 2 is de cognitieve en de humanistische benadering.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel bewustzijnsniveaus onderscheidt Freud?",
        opties=[
            "drie",
            "twee",
            "vier",
            "vijf",
        ],
        antwoord=0,
        uitleg="Drie: het onbewuste, het onder- of voorbewuste en het bewuste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zit volgens Freud in het onbewuste?",
        opties=[
            "wat je niet kan oproepen maar wel doorwerkt",
            "wat je op dit moment aan het denken bent",
            "wat je met wat moeite kan oproepen",
            "wat je vandaag hebt meegemaakt",
        ],
        antwoord=0,
        uitleg="Het onbewuste is niet bereikbaar voor jezelf, en stuurt toch mee. Daar zit ook de verdringing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het voorbewuste bij Freud?",
        opties=[
            "wat je niet denkt maar wel kan oproepen",
            "wat je op dit moment denkt",
            "wat je nooit kan oproepen",
            "wat je nog moet leren",
        ],
        antwoord=0,
        uitleg="Het voorbewuste of onderbewuste is wat niet in je aandacht staat maar wel opgehaald kan worden, zoals je adres.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is verdringing bij Freud?",
        opties=[
            "iets te pijnlijks naar het onbewuste wegduwen",
            "iets uit het onbewuste naar het bewuste halen",
            "iets uitleggen met een oorzaak buiten jezelf",
            "iets herhalen tot het in het geheugen zit",
        ],
        antwoord=0,
        uitleg="Verdringing is een afweer: wat te pijnlijk is om te weten, verdwijnt uit het bewuste en blijft in het onbewuste werken.",
    ),
    dict(
        type="invultekst",
        vraag="Het wegduwen van iets te pijnlijks naar het onbewuste heet bij Freud ...",
        antwoord=["verdringing", "verdringen"],
        uitleg="Verdringing. De fiche zet dat begrip uitdrukkelijk bij het onbewuste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke drie delen bestaat de persoonlijkheid volgens Freud?",
        opties=[
            "het Es of Id",
            "het Ich of Ego",
            "het Über-ich of Superego",
            "het onbewuste",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie delen vormen de structuur. Het onbewuste is geen deel van de structuur maar een bewustzijnsniveau.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk principe volgt het Es of Id?",
        opties=[
            "het lustprincipe",
            "het realiteitsprincipe",
            "het moraliteitsprincipe",
            "het continuïteitsprincipe",
        ],
        antwoord=0,
        uitleg="Het Es wil nu wat het wil, zonder rekening te houden met de wereld. Dat is het lustprincipe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk principe volgt het Ich of Ego?",
        opties=[
            "het realiteitsprincipe",
            "het lustprincipe",
            "het moraliteitsprincipe",
            "het lustprincipe en het moraliteitsprincipe samen",
        ],
        antwoord=0,
        uitleg="Het Ich zoekt wat haalbaar is in de echte wereld, en bemiddelt tussen het Es en het Über-ich.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk principe volgt het Über-ich of Superego?",
        opties=[
            "het moraliteitsprincipe",
            "het realiteitsprincipe",
            "het lustprincipe",
            "het voorzichtigheidsprincipe",
        ],
        antwoord=0,
        uitleg="Het Über-ich is het gewetensdeel: het zegt wat hoort en wat niet, en geeft een schuldgevoel bij een overtreding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is eros bij Freud?",
        opties=[
            "de seks- of levensdrift",
            "de agressie- of doodsdrift",
            "het geweten in de persoon",
            "de band met de werkelijkheid",
        ],
        antwoord=0,
        uitleg="Eros is de levensdrift, thanatos de doodsdrift. Beide zitten volgens Freud in het Es.",
    ),
    dict(
        type="invultekst",
        vraag="De agressie- of doodsdrift heet bij Freud ...",
        antwoord=["thanatos"],
        uitleg="Thanatos. De tegenhanger, de seks- of levensdrift, heet eros.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Es, het Ich en het Über-ich kunnen volgens Freud met elkaar in conflict komen.",
        antwoord=True,
        uitleg="Waar. Dat conflict is de motor van de psychodynamische benadering: het Es wil, het Über-ich verbiedt, het Ich zoekt een weg.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Freud zit het Es volledig in het bewuste.",
        antwoord=False,
        uitleg="Niet waar. Het Es werkt grotendeels in het onbewuste. Dat is net waarom het volgens Freud zo moeilijk te beheersen is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand heeft enorme zin om een duur jasje mee te nemen zonder te betalen, maar doet het niet omdat het niet hoort. Welke twee delen van Freud strijden hier?",
        opties=[
            "het Es",
            "het Über-ich",
            "het voorbewuste",
            "het realiteitsprincipe",
        ],
        antwoord=[0, 1],
        uitleg="Het Es wil het jasje nu, het Über-ich zegt dat stelen niet hoort. Het Ich beslist wat er gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt honger in de les en besluit te wachten tot de pauze. Welk deel van Freud is hier aan het werk?",
        opties=[
            "het Ich, dat met de werkelijkheid rekent",
            "het Es, dat onmiddellijk bevrediging wil",
            "het Über-ich, dat een regel oplegt",
            "het onbewuste, dat de honger verdringt",
        ],
        antwoord=0,
        uitleg="Wachten tot een geschikt moment is het realiteitsprincipe van het Ich.",
    ),
    dict(
        type="invultekst",
        vraag="Het deel van de persoonlijkheid bij Freud dat tussen het Es en het Über-ich bemiddelt, is het ... of Ego.",
        antwoord=["Ich", "ich"],
        uitleg="Het Ich of Ego, dat volgens het realiteitsprincipe werkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Über-ich ontstaat volgens Freud onder andere door wat ouders en opvoeders meegeven.",
        antwoord=True,
        uitleg="Waar. Het geweten komt niet uit de lucht vallen: de normen van de opvoeders worden overgenomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het lustprincipe en het realiteitsprincipe horen volgens Freud bij hetzelfde deel van de persoonlijkheid.",
        antwoord=False,
        uitleg="Niet waar. Het lustprincipe hoort bij het Es, het realiteitsprincipe bij het Ich.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet deze benadering psychodynamisch?",
        opties=[
            "omdat er krachten in beweging zijn binnen de persoon",
            "omdat de persoonlijkheid elke dag verandert",
            "omdat ze met meetbare getallen werkt",
            "omdat ze de omgeving als motor ziet",
        ],
        antwoord=0,
        uitleg="Dynamiek is beweging. Het Es, het Ich en het Über-ich duwen en trekken, en daaruit komt het gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de bewustzijnsniveaus en de persoonlijkheidsstructuur bij Freud?",
        opties=[
            "de drie delen werken op verschillende niveaus van bewustzijn",
            "elk deel hoort bij precies één bewustzijnsniveau",
            "de niveaus en de delen hebben niets met elkaar te maken",
            "de drie delen zitten alle drie volledig in het bewuste",
        ],
        antwoord=0,
        uitleg="Het Es werkt vooral onbewust, het Ich en het Über-ich werken deels bewust en deels onbewust. Dat verband vraagt de fiche uitdrukkelijk.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is wederzijds determinisme bij Albert Bandura?",
        opties=[
            "persoon, omgeving en gedrag beïnvloeden elkaar alle drie",
            "de omgeving bepaalt het gedrag van de persoon",
            "de persoon bepaalt zijn omgeving volledig zelf",
            "het gedrag ligt vast bij de geboorte",
        ],
        antwoord=0,
        uitleg="Bandura zet drie pijlen in twee richtingen: wie je bent, waar je bent en wat je doet, werken op elkaar in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie zaken staan in het wederzijds determinisme van Bandura?",
        opties=[
            "de cognities en eigenschappen van het individu",
            "de omgeving van het individu",
            "het gedrag van het individu",
            "het onbewuste van het individu",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie. Het onbewuste is een begrip van Freud, niet van Bandura.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is zelfeffectiviteit bij Bandura?",
        opties=[
            "het geloof dat je iets zelf kan",
            "het beeld dat anderen van je hebben",
            "de inzet die je in een taak legt",
            "het resultaat dat je op een taak haalt",
        ],
        antwoord=0,
        uitleg="Zelfeffectiviteit is vertrouwen in je eigen kunnen voor een bepaalde taak. Het is geen algemeen zelfbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan zelfeffectiviteit tot een selffulfilling prophecy leiden?",
        opties=[
            "wie denkt dat hij het kan, probeert langer en slaagt vaker",
            "wie denkt dat hij het kan, hoeft niet meer te oefenen",
            "wie denkt dat hij het niet kan, wordt harder aangepakt",
            "wie denkt dat hij het niet kan, krijgt meer hulp",
        ],
        antwoord=0,
        uitleg="Het geloof stuurt het gedrag, en het gedrag maakt het geloof waar. Dat werkt in beide richtingen.",
    ),
    dict(
        type="invultekst",
        vraag="Het begrip van Bandura voor het geloof in je eigen kunnen bij een taak is ...",
        antwoord=["zelfeffectiviteit"],
        uitleg="Zelfeffectiviteit. Het andere begrip van Bandura in dit deel is het wederzijds determinisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de locus of control theory?",
        opties=[
            "Julian Rotter",
            "Albert Bandura",
            "Bernard Weiner",
            "Gordon Allport",
        ],
        antwoord=0,
        uitleg="Rotter. Hij onderscheidt een interne en een externe locus of control.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft iemand met een interne locus of control?",
        opties=[
            "het gevoel dat hij zijn leven zelf in handen heeft",
            "het gevoel dat geluk en anderen zijn leven bepalen",
            "het gevoel dat niets in zijn leven vastligt",
            "het gevoel dat zijn omgeving hem niet raakt",
        ],
        antwoord=0,
        uitleg="Intern betekent in de persoon zelf: mijn keuzes en mijn inzet bepalen wat er met mij gebeurt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Noa zegt na een geslaagd examen: ik had geluk met de vragen. Welke locus of control hoor je?",
        opties=[
            "een externe locus of control",
            "een interne locus of control",
            "een hoge zelfeffectiviteit",
            "een fenomenaal veld",
        ],
        antwoord=0,
        uitleg="Zij legt de oorzaak buiten zichzelf, bij het geluk. Dat is extern.",
    ),
    dict(
        type="waarofniet",
        vraag="Een interne locus of control gaat vaak samen met meer eigen initiatief nemen.",
        antwoord=True,
        uitleg="Waar. Wie denkt dat zijn inzet verschil maakt, zet ook eerder iets in gang.",
    ),
    dict(
        type="waarofniet",
        vraag="Een locus of control is bij Rotter een houding die van situatie tot situatie volledig wisselt.",
        antwoord=False,
        uitleg="Niet waar. Bij Rotter is het een vrij stabiele eigenschap van de persoon. Bij Weiner gaat het wel om één attributie per gebeurtenis.",
    ),
    dict(
        type="invultekst",
        vraag="Wie de oorzaak van wat hem overkomt bij geluk, toeval of anderen legt, heeft een ... locus of control.",
        antwoord=["externe", "extern"],
        uitleg="Een externe locus of control. De tegenhanger is de interne locus of control.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee namen staan in de fiche bij de humanistische benadering van persoonlijkheid?",
        opties=[
            "Abraham Maslow",
            "Carl Rogers",
            "Julian Rotter",
            "Sigmund Freud",
        ],
        antwoord=[0, 1],
        uitleg="Maslow met zijn motivatietheorie en Rogers met zijn client-centered therapy.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is zelfactualisatie bij Maslow en Rogers?",
        opties=[
            "worden wie je ten volle kan zijn",
            "doen wat de groep van je verwacht",
            "zorgen dat anderen je waarderen",
            "je gevoelens onder controle houden",
        ],
        antwoord=0,
        uitleg="Zelfactualisatie is je mogelijkheden waarmaken. Bij Maslow staat ze bovenaan de behoeftepiramide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het fenomenale veld bij Carl Rogers?",
        opties=[
            "de wereld zoals de persoon zelf die ervaart",
            "de wereld zoals ze objectief gemeten wordt",
            "het geheel van iemands onbewuste drijfveren",
            "de groep waar iemand zich bij rekent",
        ],
        antwoord=0,
        uitleg="Rogers vertrekt niet van hoe de wereld is, maar van hoe iemand hem beleeft. Daarin ligt volgens hem de verklaring van zijn gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee kanten van het zelf onderscheidt Rogers?",
        opties=[
            "het actuele zelf",
            "het ideale zelf",
            "het onbewuste zelf",
            "het sociale zelf",
        ],
        antwoord=[0, 1],
        uitleg="Het actuele zelf is wie je nu bent, het ideale zelf wie je zou willen zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is incongruentie bij Rogers?",
        opties=[
            "een grote afstand tussen het actuele en het ideale zelf",
            "een kleine afstand tussen het actuele en het ideale zelf",
            "een conflict tussen het Es en het Über-ich",
            "een verschil tussen twee bewustzijnsniveaus",
        ],
        antwoord=0,
        uitleg="Incongruentie betekent dat wie je bent en wie je wil zijn niet op elkaar vallen. Dat geeft spanning en ongemak.",
    ),
    dict(
        type="invultekst",
        vraag="Als het actuele zelf en het ideale zelf goed bij elkaar passen, spreekt Rogers van ...",
        antwoord=["congruentie"],
        uitleg="Congruentie. Het tegendeel is incongruentie, en die veroorzaakt spanning.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Rogers helpt onvoorwaardelijke aanvaarding iemand om dichter bij zijn actuele zelf te durven staan.",
        antwoord=True,
        uitleg="Waar. Wie zich aanvaard voelt zoals hij is, hoeft zich minder anders voor te doen, en dat verkleint de incongruentie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het fenomenale veld van Rogers is bij twee mensen in dezelfde kamer altijd hetzelfde.",
        antwoord=False,
        uitleg="Niet waar. Twee mensen in dezelfde kamer beleven iets heel anders. Juist dat verschil is het fenomenale veld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het grote verschil tussen de psychodynamische en de humanistische benadering van persoonlijkheid?",
        opties=[
            "de ene ziet een conflict, de andere een groei naar boven",
            "de ene ziet groei, de andere een conflict van krachten",
            "de ene werkt met het brein, de andere met de genen",
            "de ene geldt voor kinderen, de andere voor volwassenen",
        ],
        antwoord=0,
        uitleg="Bij Freud is persoonlijkheid het resultaat van strijd tussen delen. Bij Maslow en Rogers is ze een groei naar wie iemand kan worden.",
    ),
]
