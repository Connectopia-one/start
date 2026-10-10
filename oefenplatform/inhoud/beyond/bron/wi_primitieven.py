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
        vraag=r"Wat is een primitieve functie \(F\) van \(f\)?",
        opties=[
            r"een functie met \(F'(x) = f(x)\)",
            r"de afgeleide \(f'(x)\) van \(f\)",
            r"de oppervlakte onder de grafiek van \(f\)",
            r"de inverse functie \(f^{-1}\)",
        ],
        antwoord=0,
        uitleg="Primitiveren is afleiden in omgekeerde richting. De oppervlakte komt pas met de hoofdstelling in beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Waarom schrijf je bij een onbepaalde integraal altijd \(+\,C\)?",
        opties=[
            "omdat elke constante bij het afleiden verdwijnt",
            "omdat de integraal anders niet bestaat",
            r"omdat \(C\) de oppervlakte onder de grafiek is",
            r"omdat \(C\) de ondergrens van de integraal is",
        ],
        antwoord=0,
        uitleg=r"De afgeleide van een constante is nul, dus er zijn oneindig veel primitieven die één constante van elkaar verschillen.",
    ),
    dict(
        type="invultekst",
        vraag=r"Je leidt een primitieve \(F\) van \(f\) af. Wat krijg je dan? Schrijf het antwoord.",
        antwoord=["f"],
        uitleg=r"Dat is net de definitie: \(F'(x) = f(x)\), dus afleiden brengt je terug bij \(f\).",
    ),
    dict(
        type="waarofniet",
        vraag="Primitiveren is de omgekeerde bewerking van afleiden.",
        antwoord=True,
        uitleg="Dat is ook de beste controle op je werk: leid je antwoord af en je moet de integrand terugkrijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\int x^{n}\,dx\)?",
        opties=[
            r"\(\dfrac{x^{\,n+1}}{n+1} + C\)",
            r"\(\dfrac{x^{\,n-1}}{n-1} + C\)",
            r"\(n\,x^{\,n-1} + C\)",
            r"\(\dfrac{x^{\,n}}{n} + C\)",
        ],
        antwoord=0,
        uitleg="De exponent gaat met één omhoog en je deelt door die nieuwe exponent. Het derde antwoord is net de afgeleide.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Voor welke exponent werkt \(\int x^{n}\,dx = \dfrac{x^{\,n+1}}{n+1} + C\) niet?",
        opties=[
            r"\(n = -1\)",
            r"\(n = 0\)",
            r"\(n = 1\)",
            r"elke \(n < 0\)",
        ],
        antwoord=0,
        uitleg=r"Dan zou je door nul delen. Die ene integraal geeft net \(\ln|x| + C\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\int \dfrac{1}{x}\,dx = \ln|x| + C\).",
        antwoord=True,
        uitleg=r"De absolute waarde zorgt dat de formule ook werkt voor \(x < 0\), waar \(\ln x\) zelf niet bestaat.",
    ),
    dict(
        type="invultekst",
        vraag="Een functie heeft één primitieve. Hoeveel heeft ze er dan in totaal? Schrijf het antwoord in twee woorden.",
        antwoord=["oneindig veel"],
        uitleg=r"Bij elke primitieve mag je om het even welke constante \(C\) optellen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\int \cos x\,dx\)?",
        opties=[
            r"\(\sin x + C\)",
            r"\(-\sin x + C\)",
            r"\(-\cos x + C\)",
            r"\(\tan x + C\)",
        ],
        antwoord=0,
        uitleg=r"Afleiden brengt je van \(\sin x\) naar \(\cos x\), dus primitiveren gaat net de andere kant op.",
    ),
    dict(
        type="waarofniet",
        vraag=r"\(\int \sin x\,dx = \cos x + C\).",
        antwoord=False,
        uitleg=r"Er hoort een minteken bij: \(\int \sin x\,dx = -\cos x + C\). Je controleert het door af te leiden.",
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
        uitleg=r"\(\int \left(f + g\right)dx = \int f\,dx + \int g\,dx\) en \(\int k\,f\,dx = k\int f\,dx\). Voor een product of een quotiënt gaat dat niet op, en daar bestaan net de andere methodes voor.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\int_{0}^{2} x\,dx\)? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"De primitieve is \(\dfrac{x^{2}}{2}\), dus \(\dfrac{4}{2} - 0 = 2\). Het is ook de oppervlakte van een driehoek met basis \(2\) en hoogte \(2\).",
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
        uitleg=r"\(\int f(x)\,dx\) is een familie van functies, \(\int_{a}^{b} f(x)\,dx\) is een getal.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Twee primitieven van dezelfde functie \(f\) kunnen een verschillende afgeleide hebben.",
        antwoord=False,
        uitleg=r"Allebei hebben ze \(f\) als afgeleide. Ze verschillen alleen een constante.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\int k\,dx\), met \(k\) een constante?",
        opties=[
            r"\(k\,x + C\)",
            r"\(\dfrac{k}{x} + C\)",
            r"\(0 + C\)",
            r"\(k^{2} + C\)",
        ],
        antwoord=0,
        uitleg=r"Afleiden van \(k\,x\) geeft \(k\). De grafiek van de primitieve is dus een rechte met helling \(k\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\int e^{x}\,dx\)?",
        opties=[
            r"\(e^{x} + C\)",
            r"\(x\,e^{x} + C\)",
            r"\(\dfrac{e^{\,x+1}}{x+1} + C\)",
            r"\(\ln x + C\)",
        ],
        antwoord=0,
        uitleg=r"\(e^{x}\) is haar eigen afgeleide, dus ook haar eigen primitieve.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke continue functie heeft een primitieve.",
        antwoord=True,
        uitleg="Dat volgt uit de hoofdstelling van de integraalrekening. Of je die primitieve ook in een formule kan schrijven, is een andere vraag.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\int_{0}^{1} x^{2}\,dx\)? Schrijf het antwoord als breuk.",
        antwoord=["1/3"],
        uitleg=r"De primitieve is \(\dfrac{x^{3}}{3}\), en invullen geeft \(\dfrac{1}{3}\).",
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
        uitleg=r"De integrand staat tussen \(\int\) en \(dx\).",
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
        uitleg=r"Zonder grenzen ligt \(C\) niet vast. Met grenzen valt ze bij het aftrekken weg.",
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
        uitleg=r"Soms moet je de integrand eerst wat herschrijven voor je ze herkent, bijvoorbeeld \(\sqrt{x} = x^{1/2}\).",
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
        vraag=r"Je splitst \(\int (2x + 3)\,dx\). In hoeveel aparte integralen valt ze uiteen? Schrijf het cijfer.",
        antwoord=["2", "twee"],
        uitleg=r"Eén voor \(2x\) en één voor \(3\). De factor \(2\) mag je buiten de eerste integraal halen.",
    ),
    dict(
        type="waarofniet",
        vraag="Integratie door substitutie is de kettingregel in omgekeerde richting.",
        antwoord=True,
        uitleg=r"Je herkent een binnenste functie met haar afgeleide ernaast, en noemt die binnenste functie \(u\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat kies je als nieuwe veranderlijke \(u\) bij een substitutie?",
        opties=[
            "een binnenste functie waarvan de afgeleide ook in de integrand staat",
            "altijd de term met de hoogste graad uit de integrand",
            "de hele integrand, zodat er alleen nog een u overblijft",
            "de ondergrens van de integraal, want dat is veruit het eenvoudigst",
        ],
        antwoord=0,
        uitleg=r"Zonder die afgeleide erbij kan je \(dx\) niet omzetten naar \(du\) en loopt de substitutie vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe luidt de formule voor partiële integratie?",
        opties=[
            r"\(\int u\,v'\,dx = u\,v - \int v\,u'\,dx\)",
            r"\(\int u\,v'\,dx = u\,v + \int v\,u'\,dx\)",
            r"\(\int u\,v'\,dx = \int u\,dx \cdot \int v'\,dx\)",
            r"\(\int u\,v'\,dx = u'\,v - u\,v'\)",
        ],
        antwoord=0,
        uitleg="Dat minteken vergeten is de meest gemaakte fout bij deze methode.",
    ),
    dict(
        type="waarofniet",
        vraag="Partiële integratie volgt uit de productregel voor afgeleiden.",
        antwoord=True,
        uitleg=r"Je integreert \(\left(u\,v\right)' = u'v + u\,v'\) langs beide kanten en brengt één term naar de andere kant.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\int_{0}^{\pi} \sin x\,dx\)? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"De primitieve is \(-\cos x\). In \(\pi\) geeft dat \(1\), in \(0\) geeft dat \(-1\), en het verschil is \(2\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke integraal pak je met partiële integratie aan?",
        opties=[
            r"\(\int x\,e^{x}\,dx\)",
            r"\(\int (2x + 3)\,dx\)",
            r"\(\int (x^{2} - 5)\,dx\)",
            r"\(\int \dfrac{1}{x}\,dx\)",
        ],
        antwoord=0,
        uitleg="Een product van twee heel verschillende soorten functies is het typische geval. De drie andere gaan onmiddellijk of met splitsing.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een bepaalde integraal mag je na een substitutie de oude grenzen gewoon laten staan.",
        antwoord=False,
        uitleg=r"De grenzen horen bij \(x\), niet bij \(u\). Je zet ze mee om, of je gaat na de integratie eerst terug naar \(x\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel is \(\int \dfrac{f'(x)}{f(x)}\,dx\)?",
        opties=[
            r"\(\ln|f(x)| + C\)",
            r"\(f(x) + C\)",
            r"\(\dfrac{1}{f(x)} + C\)",
            r"\(\dfrac{f(x)^{2}}{2} + C\)",
        ],
        antwoord=0,
        uitleg=r"Dat is een substitutie met \(u = f(x)\). Je herkent dit patroon aan de afgeleide van de noemer die in de teller staat.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel is \(\int_{1}^{3} 2x\,dx\)? Schrijf het getal.",
        antwoord=["8", "acht"],
        uitleg=r"De primitieve is \(x^{2}\), dus \(9 - 1 = 8\).",
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
        uitleg=r"Daarmee herschrijf je bijvoorbeeld \(\sin^{2}x = \dfrac{1 - \cos 2x}{2}\), en dát kan je wel integreren.",
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
        vraag=r"Een constante factor mag je voor het integraalteken zetten: \(\int k\,f(x)\,dx = k\int f(x)\,dx\).",
        antwoord=True,
        uitleg=r"Dat is een deel van de lineariteit. Een factor met een \(x\) erin mag dat niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"\(\int 5\,dx = 5x\) plus een wat? Schrijf het woord.",
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
        vraag=r"Waarom schrijf je bij een bepaalde integraal geen \(+\,C\)?",
        opties=[
            "omdat ze bij het aftrekken van de twee grenzen wegvalt",
            "omdat een bepaalde integraal geen primitieve gebruikt",
            "omdat de constante daar altijd gelijk is aan nul",
            "omdat de grenzen de constante zelf voorstellen",
        ],
        antwoord=0,
        uitleg=r"\(\left(F(b) + C\right) - \left(F(a) + C\right) = F(b) - F(a)\).",
    ),
]
