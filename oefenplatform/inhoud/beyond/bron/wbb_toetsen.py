# -*- coding: utf-8 -*-
"""Bedrijfswetenschappen: hypothesetoetsen en correlatie.

Enkel voor bedrijfswetenschappen (fiche 2027_wiskunde_3DO_BED): de betekenis
van nulhypothese, alternatieve hypothese, significantieniveau en p-waarde
(steekproefproportie en -gemiddelde, populatieproportie en -gemiddelde,
steekproevenverdeling, eenzijdige en tweezijdige toets; de nadruk ligt op
de betekenis, niet op zelf rekenen) en het verband tussen twee numerieke
grootheden met een spreidingsdiagram (onafhankelijke en afhankelijke
variabele, soorten verbanden, trendlijn, correlatiecoëfficiënt, correlatie
en causaliteit).

Deel 1: hypothesetoetsen. Deel 2: spreidingsdiagram en correlatie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Een fabrikant zegt dat zijn pakken gemiddeld \(500\) g wegen. Een consumentenorganisatie denkt dat het minder is. Wat is de nulhypothese?",
        opties=[r"\(H_{0}: \mu = 500\)", r"\(H_{0}: \mu < 500\)", r"\(H_{0}: \mu > 500\)", r"\(H_{0}: \bar{x} = 500\)"],
        antwoord=0,
        uitleg=r"De nulhypothese is de bewering die je in twijfel trekt. Ze gaat over de populatie (\(\mu\)), niet over de steekproef (\(\bar{x}\)).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij datzelfde onderzoek naar de pakken van \(500\) g: wat is de alternatieve hypothese?",
        opties=[r"\(H_{1}: \mu < 500\)", r"\(H_{1}: \mu = 500\)", r"\(H_{1}: \mu \neq 500\)", r"\(H_{1}: \mu > 500\)"],
        antwoord=0,
        uitleg=r"De organisatie vermoedt dat het minder is: een eenzijdige toets naar links.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als je denkt dat een waarde anders is, zonder te weten of ze hoger of lager is, gebruik je een tweezijdige toets.",
        antwoord=True,
        uitleg=r"Dan is \(H_{1}: \mu \neq \mu_{0}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is de p-waarde?",
        opties=[
            r"de kans op een steekproefresultaat dat minstens zo extreem is, als \(H_{0}\) waar is",
            r"de kans dat \(H_{0}\) waar is",
            r"de kans dat \(H_{1}\) waar is",
            r"het gekozen significantieniveau",
        ],
        antwoord=0,
        uitleg=r"Hoe kleiner de p-waarde, hoe vreemder het resultaat als \(H_{0}\) zou kloppen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het significantieniveau is \(\alpha = 0{,}05\) en de p-waarde is \(0{,}02\). Wat besluit je?",
        opties=[r"je verwerpt \(H_{0}\)", r"je verwerpt \(H_{0}\) niet", r"je verwerpt \(H_{1}\)", r"je kan niets besluiten"],
        antwoord=0,
        uitleg=r"\(p < \alpha\): het resultaat is significant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het significantieniveau is \(\alpha = 0{,}01\) en de p-waarde is \(0{,}03\). Wat besluit je?",
        opties=[r"je verwerpt \(H_{0}\) niet", r"je verwerpt \(H_{0}\)", r"\(H_{1}\) is bewezen", r"\(H_{0}\) is bewezen"],
        antwoord=0,
        uitleg=r"\(p > \alpha\): er is te weinig bewijs tegen \(H_{0}\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Als je \(H_{0}\) niet verwerpt, heb je bewezen dat \(H_{0}\) waar is.",
        antwoord=False,
        uitleg=r"Je hebt enkel te weinig bewijs gevonden om ze te verwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat betekent een significantieniveau van \(5\%\)?",
        opties=[
            r"je aanvaardt \(5\%\) kans om \(H_{0}\) ten onrechte te verwerpen",
            r"\(5\%\) van de steekproef is fout",
            r"\(H_{0}\) is met \(5\%\) kans waar",
            r"de steekproef bevat \(5\%\) van de populatie",
        ],
        antwoord=0,
        uitleg=r"Je kiest \(\alpha\) vooraf: zoveel risico op een vals alarm neem je.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een partij beweert dat \(40\%\) van de kiezers voor haar stemt. In een steekproef van \(500\) kiezers zijn dat er \(180\). Wat is de steekproefproportie?",
        opties=[r"\(0{,}36\)", r"\(0{,}40\)", r"\(0{,}18\)", r"\(0{,}50\)"],
        antwoord=0,
        uitleg=r"\(\dfrac{180}{500} = 0{,}36\). De \(0{,}40\) is de populatieproportie uit de bewering.",
    ),
    dict(
        type="waarofniet",
        vraag=r"De steekproefproportie is in elke steekproef dezelfde.",
        antwoord=False,
        uitleg=r"Ze verschilt van steekproef tot steekproef. De steekproevenverdeling beschrijft hoe ze schommelt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke verdeling heeft het steekproefgemiddelde bij grote steekproeven bij benadering?",
        opties=[r"een normale verdeling", r"een uniforme verdeling", r"geen verdeling, het is een vast getal", r"altijd dezelfde verdeling als de populatie, ook als die scheef is"],
        antwoord=0,
        uitleg=r"De steekproevenverdeling van het steekproefgemiddelde is klokvormig rond het populatiegemiddelde.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Hoe kleiner de p-waarde, hoe sterker het bewijs tegen \(H_{0}\).",
        antwoord=True,
        uitleg=r"Het resultaat is dan heel onwaarschijnlijk als \(H_{0}\) waar zou zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een school denkt dat haar leerlingen hoger scoren dan het Vlaamse gemiddelde van \(65\). Welke hypothesen horen erbij?",
        opties=[r"\(H_{0}: \mu = 65\) en \(H_{1}: \mu > 65\)", r"\(H_{0}: \mu > 65\) en \(H_{1}: \mu = 65\)", r"\(H_{0}: \mu = 65\) en \(H_{1}: \mu \neq 65\)", r"\(H_{0}: \mu < 65\) en \(H_{1}: \mu > 65\)"],
        antwoord=0,
        uitleg=r"Wat je wil aantonen, zet je in \(H_{1}\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een onderzoeker zegt: \"De p-waarde is \(0{,}04\), dus er is \(4\%\) kans dat \(H_{0}\) waar is.\" Klopt dat?",
        opties=[
            r"nee, het is de kans op zo'n resultaat als \(H_{0}\) waar is",
            r"ja, dat is precies de betekenis",
            r"nee, het is de kans dat \(H_{1}\) waar is",
            r"ja, maar enkel bij een tweezijdige toets",
        ],
        antwoord=0,
        uitleg=r"De p-waarde rekent met de veronderstelling dat \(H_{0}\) klopt. Ze zegt niet hoe waarschijnlijk \(H_{0}\) zelf is.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Je kiest het significantieniveau voordat je de gegevens bekijkt.",
        antwoord=True,
        uitleg=r"Anders kan je het niveau aanpassen tot het besluit je uitkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een machine vult flessen van \(1\) liter. De controleur wil weten of de machine ontregeld is, te veel of te weinig. Welke toets?",
        opties=[r"tweezijdig, \(H_{1}: \mu \neq 1\)", r"eenzijdig, \(H_{1}: \mu < 1\)", r"eenzijdig, \(H_{1}: \mu > 1\)", r"geen toets nodig"],
        antwoord=0,
        uitleg=r"Beide richtingen tellen als probleem.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij \(\alpha = 0{,}05\) en \(p = 0{,}05\) verwerp je \(H_{0}\) zeker niet.",
        antwoord=False,
        uitleg=r"De afspraak is: verwerpen als \(p \le \alpha\). Op de grens verwerp je dus wel.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In de hypothese \(H_{0}: p = 0{,}40\) staat \(p\) voor ...",
        opties=[r"de populatieproportie", r"de p-waarde", r"de steekproefproportie", r"het significantieniveau"],
        antwoord=0,
        uitleg=r"Hypothesen gaan altijd over de populatie.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een toets geeft een p-waarde van \(0{,}30\). Wat is een correcte conclusie bij \(\alpha = 0{,}05\)?",
        opties=[
            r"het steekproefresultaat is goed te verklaren als \(H_{0}\) waar is",
            r"\(H_{0}\) is met \(30\%\) kans waar",
            r"\(H_{1}\) is bewezen",
            r"de steekproef was te klein, dus fout",
        ],
        antwoord=0,
        uitleg=r"\(p > \alpha\): geen reden om \(H_{0}\) te verwerpen.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij eenzelfde p-waarde verwerp je \(H_{0}\) sneller bij \(\alpha = 0{,}10\) dan bij \(\alpha = 0{,}01\).",
        antwoord=True,
        uitleg=r"Een groter \(\alpha\) is een lagere drempel.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Je onderzoekt of het aantal uren studie de punten op een toets beïnvloedt. Wat is de onafhankelijke variabele?",
        opties=[r"het aantal uren studie", r"de punten op de toets", r"het aantal leerlingen", r"de correlatiecoëfficiënt"],
        antwoord=0,
        uitleg=r"De onafhankelijke variabele staat op de horizontale as, de afhankelijke (de punten) op de verticale.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De correlatiecoëfficiënt \(r\) ligt altijd tussen ...",
        opties=[r"\(-1\) en \(1\)", r"\(0\) en \(1\)", r"\(0\) en \(100\)", r"\(-\infty\) en \(+\infty\)"],
        antwoord=0,
        uitleg=r"Het teken geeft de richting, de grootte de sterkte van het lineair verband.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"De punten in een spreidingsdiagram liggen dicht bij een dalende rechte. Welke \(r\) past het best?",
        opties=[r"\(r = -0{,}92\)", r"\(r = 0{,}92\)", r"\(r = -0{,}15\)", r"\(r = 0\)"],
        antwoord=0,
        uitleg=r"Dalend geeft een negatieve \(r\), dicht bij de rechte een waarde dicht bij \(-1\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een correlatiecoëfficiënt dicht bij \(0\) betekent dat er geen lineair verband is.",
        antwoord=True,
        uitleg=r"Er kan wel een ander verband zijn, bijvoorbeeld een kwadratisch.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een perfect kwadratisch verband (een parabool met de top in het midden) is \(r\) dicht bij \(1\).",
        antwoord=False,
        uitleg=r"\(r\) meet enkel lineaire verbanden. Bij zo'n parabool kan \(r\) dicht bij \(0\) liggen, ook al hangen de grootheden sterk samen.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee grootheden zijn recht evenredig. Hoe ziet het spreidingsdiagram eruit?",
        opties=[r"de punten liggen op een rechte door de oorsprong", r"de punten liggen op een hyperbool", r"de punten liggen op een parabool", r"de punten liggen willekeurig verspreid"],
        antwoord=0,
        uitleg=r"\(y = a \cdot x\): een rechte door \((0, 0)\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Twee grootheden zijn omgekeerd evenredig. Welk voorschrift past?",
        opties=[r"\(y = \dfrac{a}{x}\)", r"\(y = a \cdot x\)", r"\(y = a x^{2}\)", r"\(y = a x + b\)"],
        antwoord=0,
        uitleg=r"Het product \(x \cdot y\) blijft constant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een trendlijn is \(y = 2{,}5x + 40\), met \(x\) de reclame-uitgaven in duizend euro en \(y\) de verkoop in duizend stuks. Wat betekent \(2{,}5\)?",
        opties=[
            r"per duizend euro reclame extra stijgt de verkoop met ongeveer \(2500\) stuks",
            r"zonder reclame worden \(2500\) stuks verkocht",
            r"de correlatie is \(2{,}5\)",
            r"de verkoop verdubbelt elke \(2{,}5\) jaar",
        ],
        antwoord=0,
        uitleg=r"De richtingscoëfficiënt is de toename van \(y\) per eenheid \(x\). De \(40\) is de verwachte verkoop zonder reclame.",
    ),
    dict(
        type="invultekst",
        vraag=r"Met die trendlijn \(y = 2{,}5x + 40\): welke verkoop (in duizend stuks) verwacht je bij \(10\) duizend euro reclame?",
        antwoord=["65", "65 000", "65000"],
        uitleg=r"\(2{,}5 \cdot 10 + 40 = 65\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een sterke correlatie tussen twee grootheden bewijst dat de ene de andere veroorzaakt.",
        antwoord=False,
        uitleg=r"Correlatie is geen causaliteit. Er kan een derde verborgen variabele zijn, of toeval.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Welke waarde van \(r\) wijst op het sterkste lineair verband?",
        opties=[r"\(-0{,}95\)", r"\(0{,}80\)", r"\(0{,}50\)", r"\(-0{,}30\)"],
        antwoord=0,
        uitleg=r"Het gaat om de absolute waarde: \(0{,}95\) is het dichtst bij \(1\). Het minteken zegt enkel dat het verband dalend is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe heet een grafiek met een punt per waarneming, met de ene grootheid horizontaal en de andere verticaal?",
        opties=[r"een spreidingsdiagram", r"een histogram", r"een boxplot", r"een cirkeldiagram"],
        antwoord=0,
        uitleg=r"Je noemt het ook een scatterdiagram of puntenwolk.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een positieve correlatie betekent dat bij grotere waarden van \(x\) meestal ook grotere waarden van \(y\) horen.",
        antwoord=True,
        uitleg=r"De puntenwolk loopt van linksonder naar rechtsboven.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een stad hangen de ijsverkoop en het aantal zonnebrandgevallen sterk samen. Wat is de beste verklaring?",
        opties=[r"een derde verborgen variabele: het warme, zonnige weer", r"ijs eten veroorzaakt zonnebrand", r"zonnebrand veroorzaakt zin in ijs", r"het is zuiver toeval"],
        antwoord=0,
        uitleg=r"Beide stijgen als het zonnig is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een spreidingsdiagram toont een puntenwolk zonder enig patroon. Welke \(r\) past?",
        opties=[r"\(r \approx 0\)", r"\(r \approx 1\)", r"\(r \approx -1\)", r"\(r \approx 0{,}7\)"],
        antwoord=0,
        uitleg=r"Geen lineair verband betekent een correlatiecoëfficiënt dicht bij nul.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Met een trendlijn kan je veilig voorspellen ver buiten het bereik van de gemeten gegevens.",
        antwoord=False,
        uitleg=r"Buiten de gegevens weet je niet of het verband nog lineair is. Voorspel binnen het gemeten bereik.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Hoe bepaal je op het examen de trendlijn en de correlatiecoëfficiënt van een dataset?",
        opties=[r"met ICT, bijvoorbeeld een rekenapp of rekenblad", r"door de punten te tellen", r"door het gemiddelde van \(x\) te nemen", r"je schat ze altijd op zicht"],
        antwoord=0,
        uitleg=r"Je laat de berekening aan ICT over en interpreteert het resultaat.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Bij \(r = 0{,}35\) zeg je dat het lineair verband ...",
        opties=[r"zwak en positief is", r"sterk en positief is", r"zwak en negatief is", r"perfect is"],
        antwoord=0,
        uitleg=r"Positief teken, en ver van \(1\). Op het examen gebruik je de vuistregels uit het formularium.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Bij een lineair verband liggen de punten van het spreidingsdiagram ongeveer op een rechte.",
        antwoord=True,
        uitleg=r"Hoe dichter bij de rechte, hoe sterker het verband.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een onderzoek vindt \(r = -0{,}85\) tussen de prijs van een product en het aantal verkochte stuks. Wat betekent dat?",
        opties=[
            r"een sterk dalend lineair verband: bij hogere prijzen worden minder stuks verkocht",
            r"een zwak verband",
            r"bij hogere prijzen worden meer stuks verkocht",
            r"de prijs heeft geen invloed",
        ],
        antwoord=0,
        uitleg=r"Negatief: dalend. \(0{,}85\) ligt dicht bij \(1\): sterk.",
    ),
]
