# -*- coding: utf-8 -*-
"""Primitieven, de onbepaalde integraal en de integratiemethoden.

Het eerste stuk van het onderdeel "Analyse: integralen" van fiche G2, dat daar
achtendertig procent van het examen weegt.

Deel 1 is het begrip primitieve functie en de basisprimitieven.
Deel 2 zijn de vier integratiemethoden die de fiche noemt: onmiddellijke
integratie, integratie door splitsing, door substitutie en partiële
integratie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een primitieve functie van f?",
        opties=[
            "een functie waarvan de afgeleide f is",
            "de afgeleide van de functie f zelf",
            "de oppervlakte onder de grafiek van f",
            "de inverse functie van de functie f",
        ],
        antwoord=0,
        uitleg="Primitiveren is afleiden in omgekeerde richting. De oppervlakte komt pas met de hoofdstelling in beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je bij een onbepaalde integraal altijd plus C?",
        opties=[
            "omdat elke constante bij het afleiden verdwijnt",
            "omdat de integraal anders niet bestaat",
            "omdat C de oppervlakte onder de grafiek is",
            "omdat C de ondergrens van de integraal is",
        ],
        antwoord=0,
        uitleg="De afgeleide van een constante is nul, dus er zijn oneindig veel primitieven die één constante van elkaar verschillen.",
    ),
    dict(
        type="invultekst",
        vraag="Je leidt een primitieve van f af. Wat krijg je? Schrijf het antwoord.",
        antwoord=["f"],
        uitleg="Dat is net de definitie van een primitieve: afleiden brengt je terug bij f.",
    ),
    dict(
        type="waarofniet",
        vraag="Primitiveren is de omgekeerde bewerking van afleiden.",
        antwoord=True,
        uitleg="Dat is ook de beste controle op je werk: leid je antwoord af en je moet de integrand terugkrijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de primitieve van x tot de macht n?",
        opties=[
            "x tot de macht n plus één, gedeeld door n plus één",
            "x tot de macht n min één, gedeeld door n min één",
            "n maal x tot de macht n min één, plus een constante",
            "x tot de macht n, gedeeld door het getal n zelf",
        ],
        antwoord=0,
        uitleg="De exponent gaat met één omhoog en je deelt door die nieuwe exponent. Het derde antwoord is net de afgeleide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor welke exponent werkt die regel niet?",
        opties=[
            "voor n gelijk aan min één",
            "voor n gelijk aan nul",
            "voor n gelijk aan één",
            "voor elke negatieve n",
        ],
        antwoord=0,
        uitleg="Dan zou je door nul delen. Die ene integraal geeft net de natuurlijke logaritme.",
    ),
    dict(
        type="waarofniet",
        vraag="De primitieve van één gedeeld door x is de natuurlijke logaritme van de absolute waarde van x.",
        antwoord=True,
        uitleg="De absolute waarde zorgt dat de formule ook werkt voor negatieve x, waar de logaritme zelf niet bestaat.",
    ),
    dict(
        type="invultekst",
        vraag="Een functie heeft één primitieve. Hoeveel heeft ze er dan in totaal? Schrijf het antwoord in twee woorden.",
        antwoord=["oneindig veel"],
        uitleg="Bij elke primitieve mag je om het even welke constante optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de primitieve van de cosinus van x?",
        opties=[
            "de sinus van x, plus een constante",
            "min de sinus van x, plus een constante",
            "min de cosinus van x, plus een constante",
            "de tangens van x, plus een constante",
        ],
        antwoord=0,
        uitleg="Afleiden brengt je van sinus naar cosinus, dus primitiveren gaat net de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="De primitieve van de sinus van x is de cosinus van x, plus een constante.",
        antwoord=False,
        uitleg="Er hoort een minteken bij: min de cosinus van x. Je controleert het door af te leiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de lineariteit van de integraal?",
        opties=[
            "je mag termsgewijs integreren en constanten buiten halen",
            "je mag een product term voor term integreren",
            "je mag een breuk teller en noemer apart integreren",
            "je mag de grenzen van plaats verwisselen zonder gevolg",
        ],
        antwoord=0,
        uitleg="Voor een som en voor een veelvoud werkt het. Voor een product of een quotiënt niet, en daar bestaan net de andere methodes voor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van nul tot twee van x? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg="De primitieve is x kwadraat gedeeld door twee. Invullen geeft vier op twee min nul, dus twee. Het is ook de oppervlakte van een driehoek met basis twee en hoogte twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een onbepaalde en een bepaalde integraal?",
        opties=[
            "een bepaalde integraal heeft grenzen en levert een getal op",
            "een bepaalde integraal heeft geen integratieconstante nodig omdat ze altijd nul is",
            "een onbepaalde integraal bestaat alleen voor continue functies",
            "een onbepaalde integraal levert een getal op en een bepaalde een functie",
        ],
        antwoord=0,
        uitleg="De onbepaalde integraal is een familie van functies, de bepaalde een getal.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee primitieven van dezelfde functie kunnen een verschillende afgeleide hebben.",
        antwoord=False,
        uitleg="Allebei hebben ze dezelfde afgeleide, namelijk de oorspronkelijke functie. Ze verschillen alleen een constante.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de primitieve van een constante k?",
        opties=[
            "k maal x, plus een constante",
            "k gedeeld door x, plus een constante",
            "nul, plus een constante",
            "k in het kwadraat, plus een constante",
        ],
        antwoord=0,
        uitleg="Afleiden van k maal x geeft k. De grafiek van de primitieve is dus een rechte met helling k.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de primitieve van e tot de macht x?",
        opties=[
            "e tot de macht x, plus een constante",
            "x maal e tot de macht x, plus een constante",
            "e tot de macht x plus één, gedeeld door x plus één",
            "de natuurlijke logaritme van x, plus een constante",
        ],
        antwoord=0,
        uitleg="Die functie is haar eigen afgeleide, dus ook haar eigen primitieve.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke continue functie heeft een primitieve.",
        antwoord=True,
        uitleg="Dat volgt uit de hoofdstelling van de integraalrekening. Of je die primitieve ook in een formule kan schrijven, is een andere vraag.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van nul tot één van x kwadraat? Schrijf het antwoord als breuk.",
        antwoord=["1/3"],
        uitleg="De primitieve is x tot de derde gedeeld door drie, en in één geeft dat een derde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de integrand in een integraal?",
        opties=[
            "de functie die je integreert",
            "de grens waartussen je integreert",
            "het getal dat de integraal oplevert",
            "de constante die je achteraan bijschrijft",
        ],
        antwoord=0,
        uitleg="De integrand staat tussen het integraalteken en de dx.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet de integraal zonder grenzen de onbepaalde integraal?",
        opties=[
            "omdat de uitkomst op een constante na onbepaald blijft",
            "omdat je nooit zeker weet of de gevonden uitkomst klopt",
            "omdat de functie er niet continu hoeft te zijn",
            "omdat je het resultaat niet kan controleren",
        ],
        antwoord=0,
        uitleg="Zonder grenzen ligt die constante niet vast. Met grenzen valt ze bij het aftrekken weg.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer spreek je van onmiddellijke integratie?",
        opties=[
            "als de integrand meteen in de tabel van basisprimitieven staat",
            "als je de integraal in je hoofd kan uitrekenen zonder schrijven",
            "als de integraal grenzen heeft en dus een getal oplevert",
            "als je de integrand eerst in twee stukken moet splitsen",
        ],
        antwoord=0,
        uitleg="Soms moet je de integrand eerst wat herschrijven voor je ze herkent, bijvoorbeeld een wortel als een macht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij integratie door splitsing?",
        opties=[
            "je schrijft de integrand als een som en integreert elke term apart",
            "je splitst het integratie-interval op in twee kleinere stukken",
            "je splitst de integrand in een teller en een noemer",
            "je splitst de integratieconstante in twee delen op",
        ],
        antwoord=0,
        uitleg="Dat mag dankzij de lineariteit van de integraal.",
    ),
    dict(
        type="invultekst",
        vraag="Je splitst de integraal van twee x plus drie. In hoeveel aparte integralen valt ze uiteen? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg="Eén voor twee x en één voor drie. De twee mag je buiten de eerste integraal halen.",
    ),
    dict(
        type="waarofniet",
        vraag="Integratie door substitutie is de kettingregel in omgekeerde richting.",
        antwoord=True,
        uitleg="Je herkent een binnenste functie met haar afgeleide ernaast, en noemt die binnenste functie u.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kies je als nieuwe veranderlijke bij een substitutie?",
        opties=[
            "een binnenste functie waarvan de afgeleide ook in de integrand staat",
            "altijd de term met de hoogste graad uit de integrand",
            "de hele integrand, zodat er alleen nog een u overblijft",
            "de ondergrens van de integraal, want dat is veruit het eenvoudigst",
        ],
        antwoord=0,
        uitleg="Zonder die afgeleide erbij kan je de dx niet omzetten en loopt de substitutie vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de formule voor partiële integratie?",
        opties=[
            "u maal v, min de integraal van v maal de afgeleide van u",
            "u maal v, plus de integraal van v maal de afgeleide van u",
            "de integraal van u, maal de integraal van v, zonder meer",
            "u maal de afgeleide van v, min v maal de afgeleide van u",
        ],
        antwoord=0,
        uitleg="Dat minteken vergeten is de meest gemaakte fout bij deze methode.",
    ),
    dict(
        type="waarofniet",
        vraag="Partiële integratie volgt uit de productregel voor afgeleiden.",
        antwoord=True,
        uitleg="Je integreert de productregel langs beide kanten en brengt één term naar de andere kant.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van nul tot pi van de sinus van x? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg="De primitieve is min de cosinus. In pi geeft dat één, in nul min één, en het verschil is twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke integraal pak je met partiële integratie aan?",
        opties=[
            "x maal e tot de macht x",
            "twee x plus drie",
            "x kwadraat min vijf",
            "één gedeeld door x",
        ],
        antwoord=0,
        uitleg="Een product van twee heel verschillende soorten functies is het typische geval. De drie andere gaan onmiddellijk of met splitsing.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een bepaalde integraal mag je na een substitutie de oude grenzen gewoon laten staan.",
        antwoord=False,
        uitleg="De grenzen horen bij de oude veranderlijke. Je zet ze mee om, of je gaat na de integratie eerst terug naar x.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de primitieve van de afgeleide van f, gedeeld door f?",
        opties=[
            "de natuurlijke logaritme van de absolute waarde van f",
            "de functie f zelf, plus een constante erbij",
            "één gedeeld door f, plus een constante erbij",
            "de functie f in het kwadraat, gedeeld door het getal twee",
        ],
        antwoord=0,
        uitleg="Dat is een substitutie met u gelijk aan f. Je herkent dit patroon aan de afgeleide van de noemer die in de teller staat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de integraal van één tot drie van twee x? Schrijf het getal.",
        antwoord=["8", "acht"],
        uitleg="De primitieve is x kwadraat. Negen min één is acht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer voer je eerst een euclidische deling uit voor je integreert?",
        opties=[
            "bij een breuk waarvan de teller een hogere graad heeft dan de noemer",
            "bij elke breuk met ergens een x in de noemer, zonder uitzondering",
            "bij een integrand met een wortel in de noemer",
            "bij een product van twee veeltermfuncties",
        ],
        antwoord=0,
        uitleg="Na de deling houd je een veelterm over plus een eenvoudige rest, en die twee stukken integreer je apart.",
    ),
    dict(
        type="waarofniet",
        vraag="Een integraal met een wortel erin kan je nooit met substitutie oplossen.",
        antwoord=False,
        uitleg="Net wel: substitutie is een van de vaste methodes voor een integrand met een wortel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke goniometrische formules heb je soms nodig bij het integreren?",
        opties=[
            "de grondformule en de formule voor de dubbele hoek",
            "de sinusregel en de cosinusregel in een driehoek",
            "de formules van Simpson en de verwante hoeken",
            "de omzetting van graden naar radialen en terug",
        ],
        antwoord=0,
        uitleg="Daarmee herschrijf je bijvoorbeeld de sinus in het kwadraat tot iets wat je wel kan integreren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe controleer je het resultaat van een onbepaalde integraal?",
        opties=[
            "door je antwoord af te leiden en met de integrand te vergelijken",
            "door een getal in te vullen en het resultaat te bekijken",
            "door de integraal nog een tweede keer te berekenen",
            "door de grenzen van plaats te verwisselen en te vergelijken",
        ],
        antwoord=0,
        uitleg="Dat is een echte controle, want afleiden is eenduidig. Opnieuw rekenen herhaalt vaak dezelfde fout.",
    ),
    dict(
        type="waarofniet",
        vraag="Een constante factor mag je voor het integraalteken zetten.",
        antwoord=True,
        uitleg="Dat is een deel van de lineariteit. Een factor met een x erin mag dat niet.",
    ),
    dict(
        type="invultekst",
        vraag="De integraal van vijf dx is vijf x plus een wat? Schrijf het woord.",
        antwoord=["constante", "integratieconstante"],
        uitleg="Bij elke onbepaalde integraal hoort die constante erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als één methode niet volstaat voor een integraal?",
        opties=[
            "je combineert methodes, bijvoorbeeld eerst splitsen en dan substitueren",
            "je besluit dat de integraal niet te berekenen valt",
            "je vervangt de integraal door een benadering met smalle rechthoeken",
            "je deelt de integraal door het aantal gebruikte methodes",
        ],
        antwoord=0,
        uitleg="Bij een moeilijkere integraal heb je vaak meerdere technieken na elkaar nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je bij een bepaalde integraal geen plus C?",
        opties=[
            "omdat ze bij het aftrekken van de twee grenzen wegvalt",
            "omdat een bepaalde integraal geen primitieve gebruikt",
            "omdat de constante daar altijd gelijk is aan nul",
            "omdat de grenzen de constante zelf voorstellen",
        ],
        antwoord=0,
        uitleg="Je telt dezelfde constante er in de bovengrens bij en in de ondergrens weer af.",
    ),
]
