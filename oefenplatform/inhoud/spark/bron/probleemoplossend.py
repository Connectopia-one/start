# -*- coding: utf-8 -*-
"""De vragen voor "Probleemoplossend denken" (✨ Spark, wiskunde).

De vakfiche zegt over dit onderdeel: je lost opgaven op door een strategie te
kiezen, je zet een probleem om in wiskundetaal en terug, en je kijkt achteraf
na of je antwoord kan kloppen. De vier stappen die de fiche noemt zijn: begrijp
het probleem, maak een plan, voer het plan uit, reflecteer.

Daarom staan hier vooral echte vraagstukken, en gaat maar een handvol vragen
over de strategie zelf. Een kind leert dit door het te doen, niet door de
namen van de heuristieken op te zeggen.

Deel 1 blijft bij opgaven van één of twee stappen. Deel 2 vraagt terugrekenen,
alle mogelijkheden overlopen, patronen zien en volhouden over meer stappen.

De wiskundige notatie staat in de vragen zelf: \\(7 \\cdot 1{,}20 = 8{,}40\\)
in plaats van dezelfde som in woorden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Een fles water kost € \(1{,}20\). Hoeveel kosten er zeven?",
        opties=[r"€ \(8{,}40\)", r"€ \(7{,}20\)", r"€ \(84\)"],
        antwoord=0,
        uitleg=r"\(7 \cdot 1{,}20 = 8{,}40\). Reken even na of het kan kloppen: zeven flessen van "
               r"iets meer dan een euro moet iets meer dan zeven euro zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een opgave en je snapt niet meteen wat er gevraagd wordt. Wat doe je het best eerst?",
        opties=[
            "De opgave nog eens lezen en opschrijven wat je weet en wat je zoekt",
            "Alle getallen die je ziet bij elkaar optellen",
            "Naar de volgende vraag gaan",
        ],
        antwoord=0,
        uitleg="De eerste stap is altijd: begrijp het probleem. Pas als je weet wat gegeven is en wat "
               "gevraagd wordt, kan je een plan maken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een klas van \(24\) leerlingen is een derde afwezig. Hoeveel leerlingen zijn er aanwezig?",
        opties=[r"\(16\)", r"\(8\)", r"\(21\)"],
        antwoord=0,
        uitleg=r"Een derde van \(24\) is \(8\), dus er zijn er \(8\) afwezig. Aanwezig: "
               r"\(24 - 8 = 16\). Let op dat er naar de aanwezigen gevraagd wordt, niet naar de "
               r"afwezigen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rechthoekige tuin is \(12\) m lang en \(8\) m breed. Hoeveel meter draad heb je "
              r"nodig om er een hek rond te zetten?",
        opties=[r"\(40\) m", r"\(96\) m", r"\(20\) m"],
        antwoord=0,
        uitleg=r"Rond de tuin is de omtrek: \(2 \cdot (12 + 8) = 40\) m. Met \(12 \cdot 8\) zou je de "
               r"oppervlakte krijgen, en die staat in \(\text{m}^{2}\), niet in m.",
    ),
    dict(
        type="invultekst",
        vraag="Een trein vertrekt om 9.45 u en rijdt 2 uur en 20 minuten. Hoe laat komt hij aan? (bijvoorbeeld 14.05)",
        antwoord="12.05",
        uitleg="9.45 u + 2 u = 11.45 u, en daar nog 20 minuten bij. 11.45 u + 15 min is 12.00 u, en "
               "nog 5 minuten geeft 12.05 u.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Drie vrienden delen € \(45\) eerlijk. Daarna geeft ieder € \(2\) aan een goed doel. "
              r"Hoeveel houdt ieder over?",
        opties=[r"€ \(13\)", r"€ \(15\)", r"€ \(39\)"],
        antwoord=0,
        uitleg=r"Eerst delen: \(45 : 3 = 15\) euro per persoon. Dan elk € \(2\) af: \(15 - 2 = 13\). "
               r"Doe de stappen in de volgorde waarin ze gebeuren.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een pak van \(500\) g koekjes kost € \(3\). Wat betaal je voor een kilo?",
        opties=[r"€ \(6\)", r"€ \(1{,}50\)", r"€ \(3\)"],
        antwoord=0,
        uitleg=r"Een kilo is \(1000\) g, dus twee pakken: \(2 \cdot 3 = 6\) euro. Hier helpt een "
               r"verhoudingstabel: \(500\) g ↔ € \(3\), dus \(1000\) g ↔ € \(6\).",
    ),
    dict(
        type="waarofniet",
        vraag="Als je antwoord op een vraagstuk onmogelijk is (bijvoorbeeld een leeftijd van 200 jaar), mag je het toch opschrijven zolang je berekening netjes is.",
        antwoord=False,
        uitleg="Nee. De laatste stap is reflecteren: kan dit antwoord kloppen? Een onmogelijk antwoord "
               "betekent dat er iets misging, en dan zoek je de fout.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een film duurt \(105\) minuten. Hoe lang is dat in uren en minuten?",
        opties=[r"\(1\) u \(45\) min", r"\(1\) u \(5\) min", r"\(2\) u \(5\) min"],
        antwoord=0,
        uitleg=r"\(105 : 60 = 1\), met \(45\) over. Dus \(1\) uur en \(45\) minuten. Een uur heeft "
               r"\(60\) minuten, geen \(100\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je koopt vier broodjes van € \(2{,}50\) en betaalt met € \(20\). Hoeveel krijg je terug?",
        opties=[r"€ \(10\)", r"€ \(17{,}50\)", r"€ \(12\)"],
        antwoord=0,
        uitleg=r"Vier broodjes: \(4 \cdot 2{,}50 = 10\) euro. Terug: \(20 - 10 = 10\) euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een handige eerste stap bij een vraagstuk met veel gegevens door elkaar?",
        opties=[
            "De gegevens in een tabel of schema zetten",
            "Beginnen met het grootste getal",
            "Meteen een formule opschrijven",
        ],
        antwoord=0,
        uitleg="Gegevens ordenen in een tabel of schema maakt zichtbaar wat bij wat hoort. Dat is een "
               "van de strategieën die de vakfiche noemt.",
    ),
    dict(
        type="invultekst",
        vraag=r"Een zwembad van \(25\) meter lang: hoeveel volledige lengtes zwem je als je \(1\) kilometer zwemt?",
        antwoord="40",
        uitleg=r"Een kilometer is \(1000\) m. \(1000 : 25 = 40\) lengtes.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een fietser rijdt \(15\) km per uur. Hoe lang doet hij over \(45\) km?",
        opties=[r"\(3\) uur", r"\(30\) minuten", r"\(60\) uur"],
        antwoord=0,
        uitleg=r"\(45 : 15 = 3\) uur. Controleer het omgekeerd: \(3\) uur aan \(15\) km per uur is "
               r"\(45\) km.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een doos zitten \(6\) rijen van \(8\) chocolaatjes. Er zijn er al \(12\) op. Hoeveel blijven er over?",
        opties=[r"\(36\)", r"\(48\)", r"\(26\)"],
        antwoord=0,
        uitleg=r"Eerst het totaal: \(6 \cdot 8 = 48\). Dan eraf: \(48 - 12 = 36\).",
    ),
    dict(
        type="waarofniet",
        vraag="Schatten voor je rekent, is tijdverlies.",
        antwoord=False,
        uitleg="Schatten kost weinig tijd en laat je meteen zien of je uitkomst in de buurt ligt. Het "
               "is een van de strategieën uit de vakfiche.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een recept voor \(4\) personen vraagt \(300\) g rijst. Hoeveel heb je nodig voor \(6\) personen?",
        opties=[r"\(450\) g", r"\(500\) g", r"\(400\) g"],
        antwoord=0,
        uitleg=r"Ga eerst naar één persoon: \(300 : 4 = 75\) g. Dan maal zes: \(6 \cdot 75 = 450\) g.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een boek heeft \(240\) bladzijden. Je leest er elke dag \(30\). Op welke dag ben je klaar?",
        opties=["De achtste dag", "De zevende dag", "De tiende dag"],
        antwoord=0,
        uitleg=r"\(240 : 30 = 8\), dus na acht dagen ben je rond.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een gsm kost € \(240\). Je spaart € \(15\) per week. Na hoeveel weken heb je genoeg?",
        opties=[r"\(16\) weken", r"\(15\) weken", r"\(24\) weken"],
        antwoord=0,
        uitleg=r"\(240 : 15 = 16\) weken. Controleer: \(16 \cdot 15 = 240\).",
    ),
    dict(
        type="invultekst",
        vraag="Je hebt drie truien en twee broeken. Hoeveel verschillende combinaties kan je aantrekken?",
        antwoord="6",
        uitleg=r"Bij elke trui passen twee broeken: \(3 \cdot 2 = 6\). Je kan ze ook alle zes "
               r"opschrijven, dat is ook een strategie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je rekent uit dat een klas van \(25\) leerlingen samen \(3\) potloden heeft. Wat doe je?",
        opties=[
            "Je berekening opnieuw nakijken, want dit klinkt onwaarschijnlijk",
            "Het antwoord opschrijven, want je hebt netjes gerekend",
            r"Het getal afronden naar \(25\)",
        ],
        antwoord=0,
        uitleg="Reflecteren hoort bij het oplossen. Een antwoord dat niet plausibel is, is een teken "
               "dat er ergens een stap misliep.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Ik denk aan een getal, tel er \(7\) bij op en vermenigvuldig het resultaat met \(3\). "
              r"Ik krijg \(36\). Aan welk getal dacht ik?",
        opties=[r"\(5\)", r"\(12\)", r"\(9\)"],
        antwoord=0,
        uitleg=r"Reken terug, van achter naar voor: \(36 : 3 = 12\), en \(12 - 7 = 5\). Controleer "
               r"vooruit: \((5 + 7) \cdot 3 = 36\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een rij begint met \(2,\ 5,\ 11,\ 23,\ \ldots\) Welk getal komt er daarna?",
        opties=[r"\(47\)", r"\(35\)", r"\(46\)"],
        antwoord=0,
        uitleg=r"Elk getal is het vorige maal \(2\) plus \(1\): \(2 \to 5 \to 11 \to 23 \to 47\). "
               r"Zoek bij een rij altijd eerst naar het verband tussen twee opeenvolgende getallen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Op een parking staan auto's en motors: samen \(20\) voertuigen en \(70\) wielen. Hoeveel motors staan er?",
        opties=[r"\(5\)", r"\(10\)", r"\(15\)"],
        antwoord=0,
        uitleg=r"Stel dat het allemaal auto's waren: \(20 \cdot 4 = 80\) wielen, dat is er \(10\) te "
               r"veel. Elke motor scheelt \(2\) wielen, dus \(10 : 2 = 5\) motors. Controleer: \(5\) "
               r"motors (\(10\) wielen) en \(15\) auto's (\(60\) wielen) is \(70\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoeveel getallen van twee cijfers kan je maken met de cijfers \(1\), \(2\) en \(3\) "
              r"als elk cijfer maar één keer gebruikt mag worden?",
        opties=[r"\(6\)", r"\(9\)", r"\(3\)"],
        antwoord=0,
        uitleg=r"Schrijf ze allemaal op: \(12,\ 13,\ 21,\ 23,\ 31,\ 32\). Dat zijn er \(6\). Drie "
               r"keuzes voor het eerste cijfer, en dan nog twee over voor het tweede: "
               r"\(3 \cdot 2 = 6\).",
    ),
    dict(
        type="invultekst",
        vraag=r"Een kaars van \(20\) cm brandt \(3\) cm per uur op. Na hoeveel uur is ze nog \(5\) cm lang?",
        antwoord="5",
        uitleg=r"Er moet \(20 - 5 = 15\) cm wegbranden, en dat gaat \(3\) cm per uur: \(15 : 3 = 5\) "
               r"uur. Let op dat er niet gevraagd wordt hoe lang ze helemaal opbrandt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie vrienden zitten aan een tafel. Ieder geeft ieder ander een hand. Hoeveel handdrukken zijn er?",
        opties=[r"\(3\)", r"\(6\)", r"\(9\)"],
        antwoord=0,
        uitleg=r"Noem ze A, B en C: AB, AC en BC. Dat zijn er \(3\). AB en BA is dezelfde handdruk, "
               r"dus je mag niet gewoon \(3 \cdot 2\) doen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een trui kost na \(20\,\%\) korting € \(32\). Wat was de oude prijs?",
        opties=[r"€ \(40\)", r"€ \(38{,}40\)", r"€ \(52\)"],
        antwoord=0,
        uitleg=r"€ \(32\) is \(80\,\%\) van de oude prijs. Dus de oude prijs is "
               r"\(32 : 0{,}80 = 40\) euro. Controleer: \(20\,\%\) van \(40\) is \(8\), en "
               r"\(40 - 8 = 32\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een kraan vult een vat in \(6\) uur, een tweede kraan doet er \(12\) uur over. Hoe lang duurt het als ze samen lopen?",
        opties=[r"\(4\) uur", r"\(9\) uur", r"\(18\) uur"],
        antwoord=0,
        uitleg=r"Kijk naar \(12\) uur: de eerste kraan vult in die tijd \(2\) vaten, de tweede \(1\) "
               r"vat. Samen \(3\) vaten in \(12\) uur, dus \(1\) vat in \(4\) uur. Samen gaat het "
               r"altijd sneller dan de snelste alleen, dus \(9\) of \(18\) uur kon al niet.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel keer schrijf je het cijfer \(1\) als je alle getallen van \(1\) tot en met \(20\) opschrijft?",
        antwoord="12",
        uitleg=r"\(1\) en \(10\) tot \(19\) geven elk één \(1\) op de plaats van de tientallen of de "
               r"eenheden: \(1,\ 10,\ 11\) (twee keer), \(12,\ 13,\ 14,\ 15,\ 16,\ 17,\ 18,\ 19\). "
               r"Samen \(12\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een tuin van \(20\) m lang krijgt om de \(4\) meter een paal, ook aan het begin en aan het einde. Hoeveel palen zijn er?",
        opties=[r"\(6\)", r"\(5\)", r"\(4\)"],
        antwoord=0,
        uitleg=r"\(20 : 4 = 5\) tussenruimtes, maar palen staan op de grenzen: \(5 + 1 = 6\). Dit "
               r"heet de paalfout; maak bij twijfel een tekening.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een som van drie opeenvolgende getallen is \(48\). Wat is het kleinste?",
        opties=[r"\(15\)", r"\(16\)", r"\(14\)"],
        antwoord=0,
        uitleg=r"Het middelste is \(48 : 3 = 16\), dus de getallen zijn \(15,\ 16\) en \(17\). "
               r"Controleer: \(15 + 16 + 17 = 48\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je koopt \(3\) kg appels en \(2\) kg peren voor € \(11\). Appels kosten € \(2\) per kilo. Wat kost een kilo peren?",
        opties=[r"€ \(2{,}50\)", r"€ \(2\)", r"€ \(5\)"],
        antwoord=0,
        uitleg=r"De appels kosten \(3 \cdot 2 = 6\) euro. Blijft over voor de peren: \(11 - 6 = 5\) "
               r"euro, voor \(2\) kilo. Dus \(5 : 2 = 2{,}50\) euro per kilo.",
    ),
    dict(
        type="waarofniet",
        vraag="Als een strategie niet werkt, is het slim om een andere te proberen in plaats van dezelfde weg te blijven gaan.",
        antwoord=True,
        uitleg="Juist. Terugkijken op je aanpak en die bijstellen hoort bij het oplossen. Een schets, "
               "een tabel of terugrekenen kan opeens wel werken.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een zaal heeft rijen van \(14\) stoelen. Er komen \(100\) mensen. Hoeveel rijen zijn er nodig?",
        opties=[r"\(8\)", r"\(7\)", r"\(14\)"],
        antwoord=0,
        uitleg=r"\(100 : 14 = 7\), met \(2\) over. Die \(2\) mensen hebben ook een stoel nodig, dus "
               r"\(8\) rijen. Bij zo'n vraag rond je altijd naar boven af.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het is nu 14.00 u. Hoe laat is het over \(100\) uur?",
        opties=["18.00 u", "16.00 u", "20.00 u"],
        antwoord=0,
        uitleg=r"\(100 : 24 = 4\) volle dagen met \(4\) uur over. Vier dagen later is het weer "
               r"14.00 u, plus \(4\) uur is 18.00 u.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoeveel kleine kubusjes zitten er in een kubus van \(3\) bij \(3\) bij \(3\)?",
        antwoord="27",
        uitleg=r"\(3 \cdot 3 \cdot 3 = 27\). Een laag is \(3 \cdot 3 = 9\) kubusjes, en er zijn drie "
               r"lagen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Anna is nu \(12\) en haar mama \(40\). Over hoeveel jaar is haar mama precies dubbel zo oud als Anna?",
        opties=[r"\(16\) jaar", r"\(14\) jaar", r"\(28\) jaar"],
        antwoord=0,
        uitleg=r"Het verschil blijft altijd \(28\) jaar. Als mama dubbel zo oud is, is dat verschil "
               r"gelijk aan Anna's leeftijd, dus Anna is dan \(28\) en mama \(56\). Dat is over "
               r"\(28 - 12 = 16\) jaar.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een winkel verkoopt \(4\) flessen voor de prijs van \(3\). Eén fles kost € \(2\). "
              r"Hoeveel procent korting krijg je op de vier samen?",
        opties=[r"\(25\,\%\)", r"\(33\,\%\)", r"\(20\,\%\)"],
        antwoord=0,
        uitleg=r"Vier flessen kosten normaal € \(8\), nu betaal je € \(6\). De korting is € \(2\) op "
               r"€ \(8\), en \(2 : 8 = 0{,}25\), dus \(25\,\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je verdeelt \(100\) snoepjes over een aantal kinderen, elk evenveel, en er blijven er \(4\) over. Hoeveel kinderen kunnen er zijn?",
        opties=[r"\(8\)", r"\(7\)", r"\(9\)"],
        antwoord=0,
        uitleg=r"Er zijn \(100 - 4 = 96\) snoepjes eerlijk verdeeld, dus het aantal kinderen is een "
               r"deler van \(96\). Van de drie is enkel \(8\) dat. En er moeten meer dan \(4\) "
               r"kinderen zijn, anders kon je de rest nog verdelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de laatste stap bij het oplossen van een vraagstuk?",
        opties=[
            "Nakijken of je antwoord de gestelde vraag beantwoordt",
            "De berekening netjes overschrijven",
            "Het grootste getal onderstrepen",
        ],
        antwoord=0,
        uitleg="Reflecteren: klopt het antwoord, is het mogelijk, en geeft het écht antwoord op wat er "
               "gevraagd werd? Een juist getal bij de verkeerde vraag is nog altijd fout.",
    ),
]
