# -*- coding: utf-8 -*-
"""Rekenkundige en meetkundige rijen.

Wiskunde basis, derde graad. De fiche vraagt: rij, rekenkundige en
meetkundige rij, recursief en expliciet voorschrift, grafische voorstelling,
stijgen en dalen, toenemende en afnemende stijging of daling, het verband met
lineaire en exponentiële groei en met eerstegraadsfuncties en exponentiële
functies, en de somformules s_n uit het formularium. Contexten zoals
enkelvoudige en samengestelde intrest. Limieten van rijen en oneindige
reeksen vraagt deze fiche niet.

Deel 1: rekenkundige rijen. Deel 2: meetkundige rijen en vergelijken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Wat is een rekenkundige rij?",
        opties=[
            r"een rij waarin je telkens hetzelfde getal \(v\) optelt: \(u_{n+1} = u_{n} + v\)",
            r"een rij waarin je telkens met hetzelfde getal \(q\) vermenigvuldigt: \(u_{n+1} = u_{n} \cdot q\)",
            r"een rij waarin elke term het kwadraat is van de vorige: \(u_{n+1} = u_{n}^{2}\)",
            r"een rij waarin elke term de som is van de twee vorige termen",
        ],
        antwoord=0,
        uitleg=r"Dat vaste getal heet het verschil van de rij. Een vaste vermenigvuldiger hoort bij een meetkundige rij.",
    ),
    dict(
        type="invultekst",
        vraag=r"Wat is het verschil van de rij \(12, 9, 6, 3, \dots\)? Schrijf het getal.",
        antwoord=["-3", "−3", "min 3"],
        uitleg=r"Elke term is \(3\) minder: \(9 - 12 = -3\). Een negatief verschil geeft een dalende rij.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het recursief voorschrift van de rij \(5, 8, 11, 14, \dots\)?",
        opties=[
            r"\(u_{1} = 5\) en \(u_{n+1} = u_{n} + 3\)",
            r"\(u_{n+1} = u_{n} + 3\) zonder beginterm",
            r"\(u_{1} = 5\) en \(u_{n+1} = 3u_{n}\)",
            r"\(u_{n} = 5 + 3n\)",
        ],
        antwoord=0,
        uitleg=r"Een recursief voorschrift geeft de volgende term uit de vorige, en heeft altijd een beginterm nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het expliciet voorschrift van de rij \(5, 8, 11, 14, \dots\)?",
        opties=[r"\(u_{n} = 5 + (n - 1) \cdot 3\)", r"\(u_{n} = 5 + 3n\)", r"\(u_{n} = 5 \cdot 3^{n-1}\)", r"\(u_{n} = 3 + 5n\)"],
        antwoord=0,
        uitleg=r"\(u_{n} = u_{1} + (n - 1) v\). Controle: \(u_{1} = 5\), \(u_{2} = 8\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(u_{20}\) van de rij \(5, 8, 11, 14, \dots\). Schrijf het getal.",
        antwoord=["62", "tweeënzestig"],
        uitleg=r"\(u_{20} = 5 + 19 \cdot 3 = 62\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"De grafische voorstelling van een rekenkundige rij bestaat uit losse punten op een rechte.",
        antwoord=True,
        uitleg=r"\(u_{n} = u_{1} + (n - 1) v\) is lineair in \(n\). Het zijn losse punten omdat \(n\) enkel natuurlijke waarden aanneemt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij welke groei past een rekenkundige rij?",
        opties=[r"lineaire groei", r"exponentiële groei", r"kwadratische groei", r"periodieke groei"],
        antwoord=0,
        uitleg=r"Er komt telkens evenveel bij: een constante stijging of daling, zoals bij een eerstegraadsfunctie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met welke formule bereken je de som \(s_{n}\) van de eerste \(n\) termen van een rekenkundige rij?",
        opties=[r"\(s_{n} = n \cdot \dfrac{u_{1} + u_{n}}{2}\)", r"\(s_{n} = \dfrac{u_{1} + u_{n}}{n}\)", r"\(s_{n} = u_{1} \cdot \dfrac{1 - q^{n}}{1 - q}\)", r"\(s_{n} = n \cdot u_{n}\)"],
        antwoord=0,
        uitleg=r"Het aantal termen maal het gemiddelde van de eerste en de laatste term. De formule met \(q\) is voor een meetkundige rij.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken de som van de getallen \(1 + 2 + 3 + \dots + 100\). Schrijf het getal.",
        antwoord=["5050", "5 050", "5.050"],
        uitleg=r"\(s_{100} = 100 \cdot \dfrac{1 + 100}{2} = 5050\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken de som van de eerste \(10\) termen van de rij \(5, 8, 11, \dots\). Schrijf het getal.",
        antwoord=["185", "honderdvijfentachtig"],
        uitleg=r"\(u_{10} = 5 + 9 \cdot 3 = 32\), dus \(s_{10} = 10 \cdot \dfrac{5 + 32}{2} = 185\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een rekenkundige rij met een negatief verschil is stijgend.",
        antwoord=False,
        uitleg=r"Bij een negatief verschil wordt elke term kleiner: de rij daalt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rij heeft \(u_{1} = 4\) en \(u_{6} = 29\) en is rekenkundig. Wat is het verschil?",
        opties=[r"\(5\)", r"\(25\)", r"\(\dfrac{29}{6}\)", r"\(4\)"],
        antwoord=0,
        uitleg=r"Van \(u_{1}\) naar \(u_{6}\) zijn vijf stappen: \(\dfrac{29 - 4}{5} = 5\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een zaal heeft \(15\) stoelen op de eerste rij en telkens \(2\) stoelen meer op de volgende rij. Hoeveel stoelen staan er op rij \(12\)?",
        opties=[r"\(37\)", r"\(39\)", r"\(24\)", r"\(27\)"],
        antwoord=0,
        uitleg=r"\(u_{12} = 15 + 11 \cdot 2 = 37\). Wie \(12 \cdot 2\) optelt, telt één stap te veel.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel stoelen zijn er in totaal op de eerste \(12\) rijen van die zaal (\(15, 17, 19, \dots\))? Schrijf het getal.",
        antwoord=["312", "driehonderdtwaalf"],
        uitleg=r"\(s_{12} = 12 \cdot \dfrac{15 + 37}{2} = 12 \cdot 26 = 312\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je zet \(1000\) euro op een rekening met \(2\%\) enkelvoudige intrest per jaar. Welke rij geeft het bedrag na elk jaar?",
        opties=[r"een rekenkundige rij met verschil \(20\)", r"een meetkundige rij met reden \(1{,}02\)", r"een rekenkundige rij met verschil \(1{,}02\)", r"een meetkundige rij met reden \(20\)"],
        antwoord=0,
        uitleg=r"Bij enkelvoudige intrest krijg je elk jaar \(2\%\) van het beginbedrag: telkens \(20\) euro.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een rekenkundige rij met \(v = 0\) zijn alle termen gelijk.",
        antwoord=True,
        uitleg=r"Er komt telkens \(0\) bij. Zo'n rij is constant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke rij is rekenkundig?",
        opties=[r"\(2{,}5;\ 4;\ 5{,}5;\ 7\)", r"\(2;\ 4;\ 8;\ 16\)", r"\(1;\ 4;\ 9;\ 16\)", r"\(1;\ 2;\ 4;\ 7\)"],
        antwoord=0,
        uitleg=r"Telkens \(+1{,}5\). De andere rijen hebben geen vast verschil.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een rekenkundige rij is elke term het gemiddelde van de term ervoor en de term erna.",
        antwoord=True,
        uitleg=r"\(u_{n-1} = u_{n} - v\) en \(u_{n+1} = u_{n} + v\). Het gemiddelde daarvan is \(u_{n}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Het expliciet voorschrift \(u_{n} = 7 - 2n\) hoort bij een stijgende rij.",
        antwoord=False,
        uitleg=r"\(u_{1} = 5\), \(u_{2} = 3\), \(u_{3} = 1\): de rij daalt met verschil \(-2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rekenkundige rij heeft \(u_{1} = 100\) en \(v = -7\). Wat is de eerste negatieve term?",
        opties=[r"\(u_{16} = -5\)", r"\(u_{15} = 2\)", r"\(u_{15} = -5\)", r"\(u_{14} = 9\)"],
        antwoord=0,
        uitleg=r"\(u_{n} = 100 - 7(n - 1)\). \(u_{15} = 100 - 98 = 2\), \(u_{16} = 100 - 105 = -5\).",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag=r"Wat is de reden \(q\) van de rij \(3, 6, 12, 24, \dots\)? Schrijf het getal.",
        antwoord=["2", "twee"],
        uitleg=r"\(q = \dfrac{u_{2}}{u_{1}} = \dfrac{6}{3} = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het expliciet voorschrift van een meetkundige rij?",
        opties=[r"\(u_{n} = u_{1} \cdot q^{n-1}\)", r"\(u_{n} = u_{1} \cdot q^{n}\)", r"\(u_{n} = u_{1} + (n - 1) q\)", r"\(u_{n} = (u_{1} \cdot q)^{n}\)"],
        antwoord=0,
        uitleg=r"Om bij \(u_{n}\) te komen, vermenigvuldig je \(n - 1\) keer met \(q\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(u_{8}\) van de rij \(3, 6, 12, 24, \dots\). Schrijf het getal.",
        antwoord=["384", "driehonderdvierentachtig"],
        uitleg=r"\(u_{8} = 3 \cdot 2^{7} = 3 \cdot 128 = 384\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is het recursief voorschrift van de rij \(80, 40, 20, 10, \dots\)?",
        opties=[r"\(u_{1} = 80\) en \(u_{n+1} = \tfrac{1}{2} u_{n}\)", r"\(u_{1} = 80\) en \(u_{n+1} = u_{n} - 40\)", r"\(u_{1} = 80\) en \(u_{n+1} = 2u_{n}\)", r"\(u_{n} = 80 \cdot \left(\tfrac{1}{2}\right)^{n}\)"],
        antwoord=0,
        uitleg=r"Telkens de helft: reden \(\tfrac{1}{2}\). Het laatste voorschrift is expliciet en klopt bovendien niet voor \(u_{1}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij welke groei past een meetkundige rij met \(q > 1\)?",
        opties=[r"exponentiële groei", r"lineaire groei", r"kwadratische groei", r"periodieke groei"],
        antwoord=0,
        uitleg=r"Telkens met hetzelfde getal vermenigvuldigen is exponentiële groei, zoals bij \(a^{x}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Met welke formule bereken je \(s_{n}\) van een meetkundige rij met \(q \neq 1\)?",
        opties=[r"\(s_{n} = u_{1} \cdot \dfrac{1 - q^{n}}{1 - q}\)", r"\(s_{n} = n \cdot \dfrac{u_{1} + u_{n}}{2}\)", r"\(s_{n} = u_{1} \cdot q^{n}\)", r"\(s_{n} = \dfrac{u_{1}}{1 - q}\)"],
        antwoord=0,
        uitleg=r"Die formule staat in het formularium. De formule zonder macht van q hoort bij een oneindige reeks, en die vraagt deze leerstof niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Bereken \(1 + 2 + 4 + 8 + \dots + 512\) (tien termen). Schrijf het getal.",
        antwoord=["1023", "1 023", "1.023"],
        uitleg=r"\(s_{10} = 1 \cdot \dfrac{1 - 2^{10}}{1 - 2} = \dfrac{1 - 1024}{-1} = 1023\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een meetkundige rij met \(u_{1} = 5\) en \(q = 0{,}8\) is dalend.",
        antwoord=True,
        uitleg=r"Een positieve beginterm maal een reden tussen \(0\) en \(1\) wordt steeds kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe verloopt de rij \(u_{n} = 5 \cdot 0{,}8^{n-1}\)?",
        opties=[r"afnemende daling", r"toenemende daling", r"afnemende stijging", r"constante daling"],
        antwoord=0,
        uitleg=r"\(5;\ 4;\ 3{,}2;\ 2{,}56\): de dalingen \(1;\ 0{,}8;\ 0{,}64\) worden kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je zet \(1000\) euro op een rekening met \(2\%\) samengestelde intrest per jaar. Welke rij geeft het bedrag na elk jaar?",
        opties=[r"een meetkundige rij met reden \(1{,}02\)", r"een rekenkundige rij met verschil \(20\)", r"een meetkundige rij met reden \(0{,}02\)", r"een rekenkundige rij met verschil \(1{,}02\)"],
        antwoord=0,
        uitleg=r"Elk jaar wordt het bedrag maal \(1{,}02\), ook de intrest van vorige jaren.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel staat er na \(5\) jaar op die rekening (\(1000\) euro aan \(2\%\) samengestelde intrest), afgerond op een cent?",
        opties=[r"\(1104{,}08\) euro", r"\(1100{,}00\) euro", r"\(1082{,}43\) euro", r"\(1126{,}16\) euro"],
        antwoord=0,
        uitleg=r"\(1000 \cdot 1{,}02^{5} \approx 1104{,}08\). Bij enkelvoudige intrest was het \(1100\) euro.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De rij \(2, 6, 18, 54, \dots\) is rekenkundig.",
        antwoord=False,
        uitleg=r"De verschillen \(4, 12, 36\) zijn niet gelijk, maar de quotiënten wel: reden \(3\). Ze is meetkundig.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een meetkundige rij heeft \(u_{1} = 2\) en \(u_{4} = 54\). Wat is de reden?",
        opties=[r"\(3\)", r"\(27\)", r"\(\dfrac{52}{3}\)", r"\(9\)"],
        antwoord=0,
        uitleg=r"\(u_{4} = u_{1} \cdot q^{3}\), dus \(q^{3} = 27\) en \(q = 3\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"In een meetkundige rij is het quotiënt van twee opeenvolgende termen altijd hetzelfde.",
        antwoord=True,
        uitleg=r"Dat quotiënt is de reden \(q\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bal valt van \(4\) m hoogte en botst telkens terug tot \(75\%\) van de vorige hoogte. Hoe hoog komt hij na de derde bots?",
        opties=[r"\(1{,}6875\) m", r"\(2{,}25\) m", r"\(1{,}75\) m", r"\(3\) m"],
        antwoord=0,
        uitleg=r"\(4 \cdot 0{,}75^{3} = 4 \cdot 0{,}421875 = 1{,}6875\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke rij is meetkundig?",
        opties=[r"\(81;\ 27;\ 9;\ 3\)", r"\(81;\ 72;\ 63;\ 54\)", r"\(1;\ 3;\ 6;\ 10\)", r"\(2;\ 3;\ 5;\ 8\)"],
        antwoord=0,
        uitleg=r"Telkens gedeeld door \(3\), reden \(\tfrac{1}{3}\). De tweede rij is rekenkundig.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een meetkundige rij met reden \(q = 1\) is een rij met allemaal dezelfde termen.",
        antwoord=True,
        uitleg=r"Telkens maal \(1\) verandert niets. Daarom geldt de somformule enkel voor \(q \neq 1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een rekenkundige rij met een positief verschil groeit op lange termijn sneller dan een meetkundige rij met reden \(1{,}1\) en positieve beginterm.",
        antwoord=False,
        uitleg=r"Exponentiële groei haalt lineaire groei altijd in, hoe groot het verschil ook is.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een virusbericht wordt door elke ontvanger naar \(3\) nieuwe mensen gestuurd. Ronde \(1\) bereikt \(3\) mensen. Hoeveel mensen bereikt ronde \(5\)? Schrijf het getal.",
        antwoord=["243", "tweehonderddrieënveertig"],
        uitleg=r"\(u_{5} = 3 \cdot 3^{4} = 3^{5} = 243\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel mensen zijn er dan samen bereikt na \(5\) rondes (\(3 + 9 + 27 + 81 + 243\))? Schrijf het getal.",
        antwoord=["363", "driehonderddrieënzestig"],
        uitleg=r"\(s_{5} = 3 \cdot \dfrac{1 - 3^{5}}{1 - 3} = 3 \cdot \dfrac{-242}{-2} = 363\).",
    ),
]
