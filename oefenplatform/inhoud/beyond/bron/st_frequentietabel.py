# -*- coding: utf-8 -*-
"""Frequentietabellen en gegevens groeperen.

Het begin van het onderdeel "Werken met grote datasets", dat op het examen
veertig procent weegt. De fiche vraagt letterlijk twee dingen:
    "Je groepeert gegevens."
    "Je stelt een frequentietabel met absolute en relatieve frequenties op."
en allebei met ICT, op een aangeleverde grote dataset.

De fiche noemt uitdrukkelijk gegroepeerde én niet-gegroepeerde
frequentietabellen. Dat onderscheid is de kern van deel 2: wanneer groepeer
je, hoe kies je je klassen, en wat verlies je erbij. Want je verliest wel
iets: uit een gegroepeerde tabel kan je de oorspronkelijke waarden niet meer
terughalen, en het gemiddelde dat je eruit berekent is een benadering.

Deel 1 is de frequentietabel zelf: absoluut, relatief en cumulatief.
Deel 2 is groeperen in klassen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de absolute frequentie van een waarde?",
        opties=[
            "het aantal keer dat die waarde voorkomt",
            "het deel van het geheel dat die waarde inneemt",
            "het verschil tussen die waarde en het gemiddelde",
            "de plaats van die waarde in de gerangschikte lijst",
        ],
        antwoord=0,
        uitleg="Gewoon tellen. Komt het cijfer zeven elf keer voor, dan is de absolute frequentie elf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de relatieve frequentie van een waarde?",
        opties=[
            "de absolute frequentie gedeeld door het totale aantal",
            "de absolute frequentie vermenigvuldigd met het totale aantal",
            "het aantal keer dat die waarde voorkomt in de steekproef",
            "het verschil tussen de grootste en de kleinste frequentie",
        ],
        antwoord=0,
        uitleg="Ze zegt welk deel van het geheel die waarde inneemt, en wordt vaak als percentage geschreven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een waarde komt acht keer voor in een dataset van veertig. Wat is de relatieve frequentie?",
        opties=["twintig procent", "acht procent", "veertig procent", "vijf procent"],
        antwoord=0,
        uitleg="Acht gedeeld door veertig is nul komma twee, dus twintig procent.",
    ),
    dict(
        type="waarofniet",
        vraag="De som van alle relatieve frequenties in een tabel is gelijk aan één.",
        antwoord=True,
        uitleg="Of honderd procent. Dat is de snelste controle op een rekenfout in je tabel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de cumulatieve frequentie bij een bepaalde waarde?",
        opties=[
            "het aantal gegevens tot en met die waarde",
            "het aantal gegevens dat precies die waarde heeft",
            "het aantal gegevens boven die waarde",
            "het gemiddelde van alle waarden tot die waarde",
        ],
        antwoord=0,
        uitleg="Je telt de frequenties op terwijl je de tabel doorloopt. Bij de laatste rij kom je aan het totaal.",
    ),
    dict(
        type="invultekst",
        vraag="Een waarde komt twaalf keer voor in een dataset van vijftig. Wat is de relatieve frequentie in procent? Geef het getal in cijfers.",
        antwoord=["24", "24 procent"],
        uitleg="Twaalf gedeeld door vijftig is nul komma vierentwintig, dus vierentwintig procent.",
    ),
    dict(
        type="waarofniet",
        vraag="Een absolute frequentie kan een kommagetal zijn.",
        antwoord=False,
        uitleg="Het is een aantal, dus altijd een geheel getal. De relatieve frequentie mag wel een kommagetal zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men relatieve frequenties om twee datasets te vergelijken?",
        opties=[
            "omdat datasets van verschillende grootte zo vergelijkbaar worden",
            "omdat relatieve frequenties altijd grotere getallen geven",
            "omdat absolute frequenties niet met ICT berekend kunnen worden",
            "omdat relatieve frequenties geen eenheid nodig hebben",
        ],
        antwoord=0,
        uitleg="Veertig van de tweehonderd en twee van de tien zijn allebei twintig procent. In absolute getallen lijken ze niets op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tabel bevat de frequenties 12, 18, 25 en 5. Hoe groot is het totale aantal?",
        opties=["zestig", "vijfenvijftig", "vijftig", "vijfenzestig"],
        antwoord=0,
        uitleg="Twaalf plus achttien plus vijfentwintig plus vijf is zestig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een frequentietabel kan je ook voor een niet-numerieke variabele opstellen.",
        antwoord=True,
        uitleg="Haarkleur, studierichting of woonplaats: je telt gewoon hoeveel keer elke categorie voorkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een frequentietabel staat bij de derde rij een cumulatieve frequentie van 45 en bij de vierde rij 62. Wat is de absolute frequentie van de vierde rij?",
        opties=["zeventien", "tweeënzestig", "vijfenveertig", "honderdzeven"],
        antwoord=0,
        uitleg="Tweeënzestig min vijfenveertig is zeventien. Een cumulatieve kolom lees je altijd als een verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe stel je volgens de fiche een frequentietabel op bij een grote dataset?",
        opties=[
            "met ICT, dus met de rekenapps van de examencommissie",
            "met de hand, want tellen kan een rekenapp niet",
            "door enkel de tien meest voorkomende waarden te tellen",
            "door de dataset eerst te standaardiseren met de formule",
        ],
        antwoord=0,
        uitleg="Bij duizenden gegevens is tellen met de hand onbegonnen werk. De fiche vraagt het dan ook met ICT.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel is de som van alle relatieve frequenties in procent? Geef het getal in cijfers.",
        antwoord=["100", "100 procent"],
        uitleg="Honderd procent, of één als je met decimalen rekent.",
    ),
    dict(
        type="waarofniet",
        vraag="De laatste cumulatieve frequentie in een tabel is gelijk aan de grootste absolute frequentie.",
        antwoord=False,
        uitleg="Ze is gelijk aan het totale aantal gegevens, want je hebt dan alles opgeteld. Dat is een goede controle.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling vindt in zijn tabel relatieve frequenties die samen 1,04 geven. Wat besluit hij?",
        opties=[
            "er zit een rekenfout in, want de som moet één zijn",
            "dat kan door het afronden, hij laat het zo staan",
            "hij moet alles door 1,04 delen en dan klopt het",
            "hij moet een vierde kolom met cumulatieven toevoegen",
        ],
        antwoord=0,
        uitleg="Afronden kan een paar duizendsten schelen, geen vier honderdsten. Vier procent te veel is een fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de kolom met cumulatieve frequenties vooral?",
        opties=[
            "om snel te zien hoeveel gegevens onder een grens liggen",
            "om het gemiddelde van de dataset te berekenen",
            "om de modus van de dataset te bepalen",
            "om de standaardafwijking te kunnen uitrekenen",
        ],
        antwoord=0,
        uitleg="Hoeveel leerlingen haalden minder dan twaalf op twintig? Dat lees je in één keer uit die kolom.",
    ),
    dict(
        type="waarofniet",
        vraag="In een frequentietabel moet elke waarde van de dataset in precies één rij terechtkomen.",
        antwoord=True,
        uitleg="Anders tel je gegevens dubbel of vergeet je ze. Bij klassen betekent dat: geen overlap en geen gaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een klas van vijfentwintig leerlingen haalden er vijf een tien. Wat is de relatieve frequentie?",
        opties=["twintig procent", "vijf procent", "vijfentwintig procent", "tien procent"],
        antwoord=0,
        uitleg="Vijf gedeeld door vijfentwintig is een vijfde, dus twintig procent.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het aantal keer dat een waarde voorkomt? Twee woorden.",
        antwoord=["absolute frequentie", "de absolute frequentie"],
        uitleg="De absolute frequentie, tegenover de relatieve frequentie die het deel van het geheel geeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant zet alleen absolute frequenties in een tabel met twee heel verschillend grote groepen. Wat is daar het probleem mee?",
        opties=[
            "de lezer kan de twee groepen niet eerlijk vergelijken zonder percentages",
            "absolute frequenties mogen niet in een krant gepubliceerd worden",
            "absolute frequenties kunnen niet in een tabel gezet worden",
            "de lezer heeft dan ook de cumulatieve frequenties nodig",
        ],
        antwoord=0,
        uitleg="Honderd gevallen in een stad van een miljoen en honderd in een dorp van duizend zijn iets heel anders.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer groepeer je gegevens in klassen?",
        opties=[
            "als er heel veel verschillende waarden zijn",
            "als er maar een paar verschillende waarden zijn",
            "als de variabele niet-numeriek is",
            "als het totale aantal kleiner is dan tien",
        ],
        antwoord=0,
        uitleg="Bij duizend verschillende lengtes is een rij per waarde onbruikbaar. Dan maak je klassen van vijf centimeter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een klasse in een gegroepeerde frequentietabel?",
        opties=[
            "een interval waarin je verschillende waarden samen telt",
            "een rij met precies één waarde en haar frequentie",
            "de categorie met de hoogste frequentie van de tabel",
            "het gemiddelde van de hele dataset per groep",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld van 160 tot 165 centimeter. Alle lengtes in dat interval komen in dezelfde rij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de klassenbreedte van de klasse van 20 tot 30?",
        opties=["tien", "twintig", "dertig", "vijf"],
        antwoord=0,
        uitleg="Dertig min twintig is tien. In een goede tabel zijn alle klassen even breed.",
    ),
    dict(
        type="waarofniet",
        vraag="Het klassenmidden van de klasse van 20 tot 30 is 20.",
        antwoord=False,
        uitleg="Het klassenmidden is het gemiddelde van de twee grenzen, dus 25. Dat getal gebruik je om uit een gegroepeerde tabel te rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je het klassenmidden om een gemiddelde uit een gegroepeerde tabel te berekenen?",
        opties=[
            "omdat je de afzonderlijke waarden niet meer kent en het midden de beste gok is",
            "omdat het klassenmidden altijd gelijk is aan het echte gemiddelde",
            "omdat het klassenmidden de modus van de klasse weergeeft",
            "omdat je anders door het aantal klassen zou moeten delen",
        ],
        antwoord=0,
        uitleg="Het resultaat is daardoor een benadering. Bij ongelijk verdeelde klassen kan het een eind naast het echte gemiddelde liggen.",
    ),
    dict(
        type="invultekst",
        vraag="Wat is het klassenmidden van de klasse van 40 tot 50? Geef het getal in cijfers.",
        antwoord=["45"],
        uitleg="Het gemiddelde van de grenzen veertig en vijftig.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit een gegroepeerde frequentietabel kan je de oorspronkelijke waarden niet meer terughalen.",
        antwoord=True,
        uitleg="Dat is de prijs van het groeperen: je krijgt overzicht en je verliest detail.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gaat er mis als je klassen laat overlappen, bijvoorbeeld van 10 tot 20 en van 20 tot 30?",
        opties=[
            "de waarde twintig past in twee klassen en wordt dubbel geteld",
            "de som van de frequenties wordt automatisch kleiner",
            "de klassenbreedte is dan niet meer te berekenen",
            "het klassenmidden valt dan buiten de klasse",
        ],
        antwoord=0,
        uitleg="Daarom schrijft men meestal van 10 tot 20 waarbij 20 er niet meer bij hoort, en begint de volgende klasse bij 20.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt vijfhonderd meetwaarden tussen 0 en 100. Hoeveel klassen zijn een redelijke keuze?",
        opties=[
            "ongeveer tien klassen van tien eenheden breed",
            "ongeveer honderd klassen van één eenheid breed",
            "twee klassen van vijftig eenheden breed",
            "vijfhonderd klassen, één per meetwaarde",
        ],
        antwoord=0,
        uitleg="Te veel klassen geeft een rommelig beeld, te weinig verbergt de vorm. Vijf tot vijftien is meestal bruikbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij ongelijke klassenbreedtes wordt een histogram misleidend als je toch gewoon de frequentie als hoogte neemt.",
        antwoord=True,
        uitleg="Een dubbel zo brede klasse lijkt dan dubbel zo belangrijk. In een histogram is de oppervlakte wat telt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een gegroepeerde en een niet-gegroepeerde frequentietabel?",
        opties=[
            "in een niet-gegroepeerde tabel staat elke waarde apart",
            "in een gegroepeerde tabel staat elke waarde apart",
            "een niet-gegroepeerde tabel heeft geen relatieve frequenties",
            "een gegroepeerde tabel kan enkel met ICT opgesteld worden",
        ],
        antwoord=0,
        uitleg="Bij weinig verschillende waarden, zoals een schoolcijfer van 0 tot 20, groepeer je niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor welke variabele groepeer je zeker niet?",
        opties=[
            "het aantal broers en zussen van een leerling",
            "de lengte in millimeter van duizend planten",
            "het jaarinkomen van vijfduizend gezinnen",
            "de reactietijd in milliseconden van honderd proefpersonen",
        ],
        antwoord=0,
        uitleg="Daar zijn maar een handvol waarden, van nul tot pakweg acht. Een rij per waarde is dan het duidelijkst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel klassen heeft een tabel met de klassen van 0 tot 20, 20 tot 40, 40 tot 60 en 60 tot 80? Geef het getal in cijfers.",
        antwoord=["4", "vier"],
        uitleg="Vier klassen, elk twintig eenheden breed.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het groeperen moet elke klasse minstens één waarde bevatten.",
        antwoord=False,
        uitleg="Een lege klasse mag en is zelfs informatief: een gat in de data valt dan op in het histogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gegroepeerde tabel heeft de klassen van 0 tot 10 met frequentie 12, van 10 tot 20 met 18 en van 20 tot 30 met 10. Hoeveel gegevens liggen onder 20?",
        opties=["dertig", "achttien", "twaalf", "veertig"],
        antwoord=0,
        uitleg="Twaalf plus achttien is dertig. Dat is de cumulatieve frequentie bij de grens twintig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling maakt klassen van 0 tot 10, van 11 tot 20 en van 21 tot 30 voor een continue variabele. Wat is het probleem?",
        opties=[
            "de waarden tussen 10 en 11 vallen in geen enkele klasse",
            "de klassen zijn niet allemaal even breed gekozen",
            "er zijn te weinig klassen voor een continue variabele",
            "het klassenmidden valt niet op een geheel getal",
        ],
        antwoord=0,
        uitleg="Bij hele getallen werkt dat wel, bij lengte of gewicht niet. Gebruik dan aansluitende grenzen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal klassen dat je kiest, verandert hoe de verdeling eruitziet in een histogram.",
        antwoord=True,
        uitleg="Met drie klassen lijkt bijna alles symmetrisch, met vijftig zie je vooral ruis. Probeer er altijd een paar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het voordeel van groeperen bij een dataset van tienduizend waarden?",
        opties=[
            "je ziet de vorm van de verdeling in één oogopslag",
            "je berekent er een exacter gemiddelde mee",
            "je kan er de oorspronkelijke waarden uit afleiden",
            "je hoeft geen relatieve frequenties meer te berekenen",
        ],
        antwoord=0,
        uitleg="Overzicht is precies waarvoor je groepeert. Voor exacte kengetallen gebruik je de ruwe data.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het gemiddelde van de twee grenzen van een klasse? Eén woord.",
        antwoord=["klassenmidden", "klassemidden", "het klassenmidden"],
        uitleg="Het klassenmidden, dat je gebruikt om uit een gegroepeerde tabel te rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je berekent uit een gegroepeerde tabel een gemiddelde van 34,2 terwijl de ruwe data 33,8 geeft. Wat zeg je?",
        opties=[
            "dat is normaal, want het klassenmidden is een benadering van de echte waarden",
            "er zit een rekenfout in een van de twee berekeningen",
            "de gegroepeerde tabel is altijd nauwkeuriger dan de ruwe data",
            "de klassen waren te smal gekozen voor deze dataset",
        ],
        antwoord=0,
        uitleg="Een klein verschil hoort erbij. Heb je de ruwe data, gebruik dan altijd die voor je kengetallen.",
    ),
]
