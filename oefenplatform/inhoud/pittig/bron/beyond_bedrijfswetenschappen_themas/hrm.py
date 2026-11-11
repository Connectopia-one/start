"""Human-resources-management — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import raster_zone, kaart_zone, RASTER_KOP, RASTER_CEL

# Personeelsgegevens van drukkerij Inkt nv (verzonnen), getekend als kaart
HR_GEGEVENS = [
    ("Gemiddeld aantal werknemers in 2026", "80", False),
    ("Werknemers die in 2026 vertrokken", "12", False),
    ("Nieuwe werknemers in 2026", "15", False),
    ("Gemiddeld aantal zieke werknemers per werkdag", "4", False),
    ("Opleidingsuren in 2026, alle werknemers samen", "1 200", False),
    ("Werknemers tevreden of zeer tevreden (enquête)", "56", False),
]


def _hr(i):
    return kaart_zone(i, len(HR_GEGEVENS))


def _stroom(k):
    """Kolom k, kop en vak samen."""
    x, y, w, h = raster_zone(0, k, 1, 3, rijkoppen=False)
    kop = h * RASTER_KOP / RASTER_CEL
    return [x, round(y - kop, 1), w, round(h + kop, 1)]


PRENTEN = [
    dict(bestand="hr-gegevens.svg", zelf=True,
         wat="Kaart met personeelsgegevens van een drukkerij (verzonnen cijfers).",
         vragen="klikvragen en rekenvragen over hr-KPI's"),
    dict(bestand="hr-stromen.svg", zelf=True,
         wat="Drie vakken: instroom, doorstroom en uitstroom.",
         vragen="klikvragen over de hrm-instrumenten"),
]

VRAGEN = [
    klik(
        "Een werknemer krijgt na zijn ontslag begeleiding naar een nieuwe job, betaald door zijn vroegere werkgever. Klik op de fase waar dit hoort.",
        "hr-stromen.svg",
        [_stroom(2)],
        "De werknemer verlaat de onderneming: dat is de uitstroom.",
    ),
    klik(
        "Een nieuwe medewerker krijgt op zijn eerste dag een rondleiding, een peter en een onthaalbrochure. Klik op de fase waar dit hoort.",
        "hr-stromen.svg",
        [_stroom(0)],
        "Het onthaal hoort bij de instroom.",
    ),
    klik(
        "Een werkneemster volgt een opleiding om teamleider te worden. Klik op de fase waar dit hoort.",
        "hr-stromen.svg",
        [_stroom(1)],
        "Opleiding en loopbaanplanning horen bij de doorstroom: groeien binnen de onderneming.",
    ),
    met_prent("hr-stromen.svg", tabel(
        "Bij welke fase hoort elk hrm-instrument?",
        [
            ("Een vacature op een jobsite plaatsen", "Instroom"),
            ("Een jaarlijks functioneringsgesprek", "Doorstroom"),
            ("Een exitgesprek met wie zelf ontslag neemt", "Uitstroom"),
            ("Een assessment voor kandidaten", "Instroom"),
            ("Een afscheid bij pensioen", "Uitstroom"),
        ],
        "Instroom: binnenkomen. Doorstroom: groeien. Uitstroom: vertrekken.",
        kolommen=["Instroom", "Doorstroom", "Uitstroom"],
    )),
    klik(
        "Klik op het gegeven dat je nodig hebt om het ziekteverzuim te berekenen, naast het gemiddeld aantal werknemers.",
        "hr-gegevens.svg",
        [_hr(3)],
        "Ziekteverzuim = gemiddeld aantal zieken per dag / gemiddeld aantal werknemers.",
    ),
    met_prent("hr-gegevens.svg", mk(
        "Hoeveel procent is het personeelsverloop van Inkt nv in 2026?",
        ["15 %", "12 %", "18,75 %", "6,7 %"],
        0,
        "Vertrokken werknemers / gemiddeld aantal werknemers = 12 / 80 = 0,15 = 15 %.",
    )),
    met_prent("hr-gegevens.svg", mk(
        "Hoeveel procent is het ziekteverzuim van Inkt nv?",
        ["5 %", "4 %", "20 %", "8 %"],
        0,
        "4 / 80 = 0,05 = 5 %.",
    )),
    met_prent("hr-gegevens.svg", mk(
        "Hoeveel opleidingsuren kreeg een werknemer van Inkt nv gemiddeld in 2026?",
        ["15 uur", "12 uur", "80 uur", "100 uur"],
        0,
        "1 200 uur / 80 werknemers = 15 uur per werknemer.",
    )),
    met_prent("hr-gegevens.svg", mk(
        "Hoeveel procent van de werknemers is tevreden of zeer tevreden?",
        ["70 %", "56 %", "44 %", "80 %"],
        0,
        "56 / 80 = 0,70 = 70 %.",
    )),
    met_prent("hr-gegevens.svg", tabel(
        "Een vergelijkbare drukkerij heeft een personeelsverloop van 8 % en een ziekteverzuim van 3 %. Wat kan Inkt nv besluiten?",
        [
            ("Bij Inkt nv vertrekken verhoudingsgewijs meer werknemers.", J),
            ("Bij Inkt nv is het ziekteverzuim lager dan bij de andere drukkerij.", F),
            ("Inkt nv heeft redenen om haar hr-beleid bij te sturen.", J),
        ],
        "15 % tegenover 8 % en 5 % tegenover 3 %: Inkt nv doet het op beide punten slechter.",
    )),
    volgorde(
        "Zet de stappen van een aanwerving in de juiste volgorde.",
        ["Een vacature opstellen", "Kandidaten aantrekken om te solliciteren", "De beste kandidaat kiezen", "De nieuwe medewerker verwelkomen"],
        "Eerst weet je wie je zoekt, dan trek je kandidaten aan, je kiest, en je verwelkomt.",
    ),
    tabel(
        "Welke selectietool is het?",
        [
            ("De kandidaat lost een uur lang vragen over boekhouding op", "Test"),
            ("De kandidaat speelt een gesprek na met een boze klant", "Assessment"),
            ("Het bedrijf belt met toestemming de vorige werkgever", "Referentie"),
            ("De kandidaat praat met de leidinggevende en iemand van hr", "Interview"),
        ],
        "Elke tool toont iets anders: kennis, gedrag in de praktijk, ervaring van anderen of de persoon zelf.",
        kolommen=["Test", "Assessment", "Referentie", "Interview"],
    ),
    sorteer(
        "Financiële of niet-financiële beloning?",
        ["Financieel", "Niet-financieel"],
        [
            ["Een eindejaarspremie", "Financieel"],
            ["Een compliment van de leidinggevende", "Niet-financieel"],
            ["Winstdeelname", "Financieel"],
            ["Meer verantwoordelijkheid in een project", "Niet-financieel"],
            ["Maaltijdcheques", "Financieel"],
            ["Thuiswerken op vrijdag", "Niet-financieel"],
        ],
        "Financieel: alles wat geld of een geldwaarde heeft. Niet-financieel: waardering, uitdaging en vrijheid.",
    ),
    mk(
        "Wat maakt een cafetariaplan anders dan een gewone bonus?",
        [
            "De werknemer kiest zelf uit een pakket voordelen",
            "De werkgever betaalt geen enkele bijdrage",
            "Iedereen krijgt verplicht dezelfde bedrijfswagen",
            "Het vervangt het volledige loon van de werknemer",
        ],
        0,
        "Bijvoorbeeld een fiets, extra vakantiedagen of een laptop in plaats van een deel van de bonus.",
    ),
    keuze(
        "Iemand uit het eigen bedrijf aanwerven voor een nieuwe functie heet [[*interne|externe|tijdelijke]] werving. Een advertentie op een jobsite plaatsen is [[*externe|interne|duurzame]] werving.",
        "Intern: de kandidaat kent het bedrijf al. Extern: je haalt nieuw talent binnen.",
    ),
    tabel(
        "Waar of niet waar over hrm?",
        [
            ("Hrm gaat over de hele loopbaan van een werknemer, niet enkel over de aanwerving.", J),
            ("Werknemers die zich gewaardeerd voelen, blijven meestal langer.", J),
            ("Duurzaam hr-beleid zorgt dat medewerkers lang en gezond kunnen blijven werken.", J),
            ("Een hoog ziekteverzuim is een goed teken voor het hr-beleid.", F),
        ],
        "Hrm volgt de werknemer van instroom tot uitstroom en zorgt voor werkbaar werk.",
    ),
    mk(
        "Een bedrijf ziet dat veel nieuwe werknemers binnen het jaar vertrekken. Welke maatregel past het best?",
        [
            "Het onthaal en de begeleiding van nieuwe werknemers verbeteren",
            "Enkel nog tijdelijke contracten aanbieden aan alle nieuwe werknemers",
            "Stoppen met het meten van het personeelsverloop",
            "De selectie volledig overlaten aan toeval",
        ],
        0,
        "Een goed onthaal verkleint de kans dat nieuwe medewerkers snel vertrekken.",
    ),
    koppel(
        "Koppel de taak van de hr-afdeling aan het voorbeeld.",
        [
            ["Aanwerven", "Sollicitatiegesprekken plannen"],
            ["Opleiden", "Een cursus Excel organiseren"],
            ["Evalueren", "Functioneringsgesprekken voorbereiden"],
            ["Welzijn op het werk", "Een ergonomische werkplek laten inrichten"],
        ],
        ["De voorraad in het magazijn tellen"],
        "Voorraad tellen is geen hr-taak: dat hoort bij de logistiek.",
    ),
    mk(
        "Een bedrijf heeft gemiddeld 250 werknemers en een personeelsverloop van 8 %. Hoeveel werknemers vertrokken er?",
        ["20", "8", "31", "25"],
        0,
        "8 % van 250 = 0,08 × 250 = 20.",
    ),
    inv(
        "Hoe noemt men het pakket van begeleiding dat een werkgever betaalt om een ontslagen werknemer naar een nieuwe job te helpen?",
        "outplacement",
        "Het hoort bij de uitstroom.",
    ),
    mk(
        "Waarom is hrm belangrijk voor het hele bedrijfsbeleid?",
        [
            "Gemotiveerde en goed opgeleide mensen zijn nodig om de doelen te halen",
            "Hrm bepaalt de verkoopprijs van alle producten en diensten van het bedrijf",
            "Zonder hrm moet een bedrijf geen belastingen betalen",
            "Hrm is enkel belangrijk voor bedrijven met meer dan 1 000 werknemers",
        ],
        0,
        "De mensen voeren de strategie uit: zonder de juiste mensen lukt geen enkel plan.",
    ),
    sleep(
        "Een [[hr-KPI]] is een cijfer dat het hr-beleid meet, zoals het [[personeelsverloop]] of het [[ziekteverzuim]].",
        ["cafetariaplan", "assessment"],
        "Met die cijfers kan een bedrijf zien of zijn maatregelen werken.",
    ),
    tabel(
        "Instrument voor duurzaam hr-beleid of niet?",
        [
            ("Werknemers kunnen hun hele loopbaan opleidingen volgen", J),
            ("Oudere werknemers zo snel mogelijk vervangen door jongere", F),
            ("Aandacht voor stress en een gezonde werkdruk", J),
        ],
        "Duurzaam: werkbaar werk, levenslang leren en aandacht voor welzijn.",
    ),
    mk(
        "Een werkgever wil weten waarom goede werknemers vertrekken. Welk instrument geeft hem daarover het meest rechtstreeks informatie?",
        ["Een exitgesprek", "Een assessment", "Een vacature", "Een cafetariaplan"],
        0,
        "In een exitgesprek vertelt de vertrekkende werknemer zelf waarom hij gaat.",
    ),
    mk(
        "Een werknemer krijgt elke maand 100 euro extra als zijn team de productiedoelen haalt. Welke beloning is dit?",
        ["Een financiële beloning op basis van prestaties", "Een niet-financiële motivatie, zoals erkenning van de baas", "Een cafetariaplan", "Outplacement"],
        0,
        "Het is geld, gekoppeld aan prestaties: een financiële beloningstechniek.",
    ),
    mk(
        "Een werkgever doet een beroep op een uitzendkantoor. Bij welke hr-stap helpt dat kantoor vooral?",
        ["Bij de werving", "Bij het exitgesprek", "Bij de pensionering", "Bij de loonsverhoging"],
        0,
        "Een uitzendkantoor zoekt kandidaten en stelt ze voor aan de werkgever.",
    ),
    open_(
        "Inkt nv heeft een hoog personeelsverloop en een hoog ziekteverzuim. Stel twee concrete hr-maatregelen voor en leg uit welk cijfer ze moeten verbeteren.",
        "1. Een beter onthaal met een peter voor nieuwe werknemers, zodat minder mensen snel vertrekken (verloop). 2. Aandacht voor werkdruk en ergonomie, bijvoorbeeld betere stoelen en flexibele uren, zodat minder mensen ziek worden (verzuim).",
        "Koppel elke maatregel aan het cijfer dat ze moet doen dalen.",
    ),
    casus(
        "Bakkerij Korst zoekt een nieuwe verkoper. Er komen 40 kandidaten. Na een eerste schifting blijven er 6 over, die een gesprek krijgen en een uur in de winkel meedraaien.",
        [
            mk(
                "Welke fase is het aantrekken van de 40 kandidaten?",
                ["Werving", "Selectie", "Onthaal", "Doorstroom"],
                0,
                "Werving: kandidaten aantrekken om te solliciteren.",
            ),
            mk(
                "Een uur in de winkel meedraaien om te zien hoe de kandidaat met klanten omgaat. Welke selectietool lijkt daar het meest op?",
                ["Een assessment met praktijkopdrachten", "Een referentie", "Een schriftelijke kennistest", "Een cafetariaplan"],
                0,
                "Een assessment laat de kandidaat opdrachten uitvoeren zoals in de echte job.",
            ),
            tabel(
                "De nieuwe verkoper begint. Wat hoort bij een goed onthaal?",
                [
                    ("Uitleg over de werking van de winkel en de kassa.", J),
                    ("Een vaste collega bij wie hij met vragen terechtkan.", J),
                    ("Hem de eerste dag alleen in de winkel laten staan.", F),
                ],
                "Een goed onthaal helpt nieuwe medewerkers snel hun weg te vinden.",
            ),
        ],
    ),
]
