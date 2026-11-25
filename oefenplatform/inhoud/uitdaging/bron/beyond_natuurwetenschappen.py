# -*- coding: utf-8 -*-
"""Uitdaging Natuurwetenschappen 🌍 Beyond doorstroom (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die de gewone
hoofdstukken (biologie, chemie en fysica) door elkaar halen. De extra
hoofdstukken voor welzijnswetenschappen blijven erbuiten, zodat iedereen de
uitdaging kan maken. Een stamboom en het elektromagnetisch spectrum om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde,
rekenvragen en een korte uitleg in eigen woorden.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_natuurwetenschappen.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Natuurwetenschappen"
BESTAND = "beyond-natuurwetenschappen-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/natuurwetenschappen-beyond-uitdaging"
STAM = "stamboom-recessief.svg"
SPEC = "em-spectrum.svg"

# klikvakken uit maak_prenten_beyond_natuurwetenschappen.py
P1 = [34.0, 22.5, 9.8, 15.7]
P2 = [56.2, 22.5, 9.8, 15.7]
P3 = [22.9, 60.0, 9.8, 15.7]
P4 = [45.1, 60.0, 9.8, 15.7]
RADIO = [3.0, 31.6, 13.4, 52.6]
IR = [29.9, 31.6, 13.4, 52.6]
UV = [56.7, 31.6, 13.4, 52.6]
RONTGEN = [70.1, 31.6, 13.4, 52.6]
GAMMA = [83.6, 31.6, 13.4, 52.6]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Stamboom (prent)
    klik("De aandoening in deze stamboom erft autosomaal recessief over. Klik op een persoon die zeker drager is maar zelf gezond.",
         STAM, [P1, P2],
         "Persoon 3 is ziek (aa) en kreeg van elke ouder een a. Beide ouders zijn gezond, dus allebei Aa: zekere dragers."),
    klik("Klik op de persoon die zeker het genotype aa heeft.",
         STAM, [P3],
         "Bij een recessieve aandoening zijn enkel de zieken homozygoot recessief: persoon 3."),
    met_prent(STAM, mk(
        "Hoe groot is de kans dat persoon 4 drager is, wetende dat ze gezond is?",
        ["2/3", "1/2", "1/4", "3/4"],
        0,
        "Uit Aa × Aa komen AA, Aa, Aa en aa. Ze is gezond, dus aa valt weg: 2 van de 3 overblijvende mogelijkheden zijn Aa.")),
    met_prent(STAM, tabel(
        "Klopt dit over deze stamboom?",
        [
            ("Twee gezonde ouders kunnen een ziek kind krijgen bij een recessieve aandoening.", J),
            ("Elk volgend kind van 1 en 2 heeft 25 % kans om ziek te zijn.", J),
            ("Persoon 5 is zeker drager.", F),
            ("Als de aandoening dominant was, zou deze stamboom ook kunnen.", F),
        ],
        "Aa × Aa geeft 1/4 kans op aa. Persoon 5 kan AA of Aa zijn. Bij een dominante aandoening heeft een ziek kind minstens één zieke ouder.")),

    # Spectrum (prent)
    klik("Bekijk het spectrum. Klik op de straling met de grootste golflengte.",
         SPEC, [RADIO],
         "Radiogolven hebben golflengtes van centimeters tot kilometers: de langste van het spectrum."),
    klik("Klik op de straling met de grootste energie per foton.",
         SPEC, [GAMMA],
         "De energie van een foton is E = h · f. Gammastraling heeft de hoogste frequentie en dus de grootste energie."),
    klik("Klik op de straling die een arts gebruikt om een botbreuk te zien.",
         SPEC, [RONTGEN],
         "Röntgenstraling gaat door zacht weefsel maar wordt door botten tegengehouden."),
    klik("Klik op de straling die een warmtecamera opvangt.",
         SPEC, [IR],
         "Warme voorwerpen zenden infrarood uit. Een warmtecamera maakt die straling zichtbaar."),
    met_prent(SPEC, tabel(
        "Is deze straling ioniserend?",
        [
            ("Gammastraling", J),
            ("Radiogolven", F),
            ("Röntgenstraling", J),
            ("Zichtbaar licht", F),
        ],
        "Enkel straling met veel energie per foton (hoog uv, röntgen, gamma) kan elektronen uit atomen slaan. Radiogolven en zichtbaar licht niet.")),

    # Cel en energie
    tabel(
        "Welk organel past bij de functie?",
        [
            ("Celademhaling: energie vrijmaken uit glucose", "Mitochondrion"),
            ("Fotosynthese", "Bladgroenkorrel"),
            ("Eiwitten maken", "Ribosoom"),
            ("Eiwitten verpakken en verzenden", "Golgi-apparaat"),
        ],
        "Mitochondriën leveren ATP, bladgroenkorrels vangen licht, ribosomen maken eiwitten en het golgi-apparaat verpakt ze.",
        kolommen=["Mitochondrion", "Bladgroenkorrel", "Ribosoom", "Golgi-apparaat"]),
    keuze(
        "Bij fotosynthese worden koolstofdioxide en water met lichtenergie omgezet in [[*glucose en zuurstofgas|ATP en koolstofdioxide|zetmeel en water]]. Celademhaling gebeurt [[*in alle levende cellen|enkel in plantencellen|enkel in het donker]].",
        "6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂. Celademhaling gebeurt dag en nacht in elke levende cel, ook bij planten."),

    # Afweer en voortplanting
    sorteer(
        "Hoort dit bij de aspecifieke of de specifieke afweer?",
        ["Aspecifiek", "Specifiek"],
        [
            ["De huid als barrière", "Aspecifiek"],
            ["Antistoffen tegen één bepaald virus", "Specifiek"],
            ["Fagocytose door witte bloedcellen", "Aspecifiek"],
            ["Geheugencellen na een vaccin", "Specifiek"],
        ],
        "De aspecifieke afweer werkt tegen alles wat binnendringt. De specifieke afweer herkent één bepaald antigen en onthoudt het."),
    keuze(
        "Een vaccin bevat [[*verzwakte of onschadelijke antigenen|kant-en-klare antistoffen|antibiotica]] en zorgt voor [[*actieve|passieve]] immuniteit.",
        "Het lichaam maakt zelf antistoffen en geheugencellen aan: actieve immuniteit. Bij passieve immuniteit krijg je antistoffen van buitenaf."),
    mk("Welk hormoon houdt het baarmoederslijmvlies in stand na de eisprong?",
       ["Progesteron", "Testosteron", "Adrenaline", "Insuline"],
       0,
       "Het geel lichaam maakt progesteron, dat het slijmvlies klaarhoudt voor een eventuele innesteling."),

    # DNA en genetica
    inv("Een DNA-streng heeft de basenvolgorde ATGCCA. Wat is de complementaire streng? Zes letters.",
        ["TACGGT"],
        "A paart met T en G met C: ATGCCA wordt TACGGT."),
    tabel(
        "Mitose of meiose?",
        [
            ("Geeft twee identieke dochtercellen", "Mitose"),
            ("Halveert het aantal chromosomen", "Meiose"),
            ("Dient voor groei en herstel", "Mitose"),
            ("Vormt geslachtscellen", "Meiose"),
        ],
        "Mitose maakt identieke lichaamscellen. Meiose maakt haploïde geslachtscellen met nieuwe combinaties.",
        kolommen=["Mitose", "Meiose"]),
    volgorde(
        "Zet de stappen van de eiwitsynthese in de juiste volgorde.",
        ["DNA wordt overgeschreven naar mRNA", "mRNA verlaat de kern", "Ribosoom leest de codons", "tRNA brengt aminozuren", "Eiwitketen wordt gevormd"],
        "Transcriptie gebeurt in de kern; translatie gebeurt aan het ribosoom met hulp van tRNA."),
    mk("Wat is een gevolg van natuurlijke selectie?",
       ["Varianten die beter aangepast zijn, krijgen meer nakomelingen.", "Elk dier past zich tijdens zijn leven doelbewust aan zijn milieu aan.", "Alle individuen van een soort worden na één generatie identiek.", "Nieuwe eigenschappen ontstaan omdat een dier ze nodig heeft."],
       0,
       "Variatie bestaat al in een populatie. De omgeving selecteert: wie beter aangepast is, plant zich vaker voort."),

    # Biomoleculen
    koppel(
        "Koppel de biomolecule aan haar bouwsteen.",
        [
            ["eiwit", "aminozuur"],
            ["zetmeel", "glucose"],
            ["vet (triglyceride)", "glycerol en vetzuren"],
            ["DNA", "nucleotide"],
        ],
        ["ATP"],
        "Polymeren zijn opgebouwd uit monomeren: eiwitten uit aminozuren, zetmeel uit glucose, DNA uit nucleotiden. Vetten bestaan uit glycerol en drie vetzuren."),

    # Chemie
    tabel(
        "Welk effect heeft elke verandering op de reactiesnelheid?",
        [
            ("De temperatuur stijgt.", "Sneller"),
            ("Je gebruikt een blok in plaats van poeder.", "Trager"),
            ("Je voegt een katalysator toe.", "Sneller"),
            ("Je verdunt de oplossing.", "Trager"),
        ],
        "Meer botsingen of meer effectieve botsingen versnellen een reactie: hogere temperatuur, groter contactoppervlak, hogere concentratie, katalysator.",
        kolommen=["Sneller", "Trager"]),
    keuze(
        "Bij het evenwicht N₂ + 3 H₂ ⇌ 2 NH₃ (exotherm) verschuift het evenwicht naar [[*rechts|links]] als je de druk verhoogt, en naar [[*links|rechts]] als je de temperatuur verhoogt.",
        "Hogere druk bevoordeelt de kant met minder gasdeeltjes (2 tegen 4). Hogere temperatuur bevoordeelt de endotherme richting: naar links."),
    tabel(
        "Tot welke stofklasse behoort de stof?",
        [
            ("CH₃OH", "Alcohol"),
            ("CH₃COOH", "Carbonzuur"),
            ("C₃H₈", "Alkaan"),
            ("CH₃COOC₂H₅", "Ester"),
        ],
        "De functionele groep bepaalt de klasse: –OH alcohol, –COOH carbonzuur, enkel C en H met enkelvoudige bindingen alkaan, –COO– ester.",
        kolommen=["Alkaan", "Alcohol", "Carbonzuur", "Ester"]),
    mk("Waarom zijn veel kunststoffen een milieuprobleem?",
       ["De natuur breekt ze nauwelijks af.", "Ze lossen in zeewater meteen volledig op.", "Ze bestaan uit zware metalen zoals lood.", "Ze zijn altijd radioactief na het gebruik."],
       0,
       "Veel polymeren worden door micro-organismen bijna niet afgebroken en vallen uiteen in microplastics."),
    keuze(
        "Een principe van duurzame chemie is [[*afval vermijden in plaats van achteraf opruimen|zo veel mogelijk oplosmiddelen gebruiken]] en liefst [[*hernieuwbare|fossiele]] grondstoffen inzetten.",
        "Groene chemie wil afval en gevaarlijke stoffen beperken en gebruikt waar het kan hernieuwbare grondstoffen."),

    # Fysica
    inv("Twee ladingen van elk 2,0 · 10⁻⁶ C liggen 0,30 m uit elkaar. Bereken de coulombkracht in newton (k = 9,0 · 10⁹ N·m²/C²).",
        ["0,4", "0,40", "0.4", "0.40"],
        "F = k · q₁ · q₂ / r² = 9,0 · 10⁹ · 4,0 · 10⁻¹² / 0,09 = 0,40 N."),
    keuze(
        "Gelijke ladingen [[*stoten elkaar af|trekken elkaar aan]]. Als de afstand tussen twee ladingen verdubbelt, wordt de kracht [[*vier keer kleiner|twee keer kleiner|twee keer groter]].",
        "De coulombkracht is omgekeerd evenredig met het kwadraat van de afstand: 2² = 4."),
    tabel(
        "Ontstaat er een inductiestroom in de spoel?",
        [
            ("Je beweegt een magneet in de spoel.", J),
            ("De magneet ligt stil in de spoel.", F),
            ("Je trekt de magneet uit de spoel.", J),
            ("Er is geen magneet en geen stroom in de buurt.", F),
        ],
        "Er is enkel inductie als de magnetische flux door de spoel verandert."),
    inv("Een auto van 1200 kg versnelt van 0 tot 20 m/s in 8,0 s. Hoe groot is de resulterende kracht in newton?",
        ["3000", "3 000", "3.000"],
        "a = 20 / 8,0 = 2,5 m/s². F = m · a = 1200 · 2,5 = 3000 N."),
    tabel(
        "Een geluidsgolf heeft een frequentie van 680 Hz en de geluidssnelheid is 340 m/s.",
        [
            ("Golflengte (m)", "0,5"),
            ("Periode (ms)", "1,47"),
            ("Golflengte bij 340 Hz (m)", "1"),
        ],
        "λ = v / f = 340 / 680 = 0,5 m. T = 1 / f = 1 / 680 s ≈ 0,00147 s = 1,47 ms. Bij 340 Hz is λ = 340 / 340 = 1 m.",
        kolommen=["0,5", "1", "1,47"]),
    keuze(
        "Een hogere toon heeft een [[*grotere frequentie|grotere amplitude|langere periode]]. Een luider geluid heeft een [[*grotere amplitude|grotere frequentie|kortere golflengte]].",
        "De toonhoogte hangt af van de frequentie, de luidheid van de amplitude."),
    tabel(
        "Welk soort straling komt vrij?",
        [
            ("Een heliumkern komt vrij.", "Alfastraling"),
            ("Een elektron komt vrij uit de kern.", "Bètastraling"),
            ("Een foton met veel energie komt vrij.", "Gammastraling"),
        ],
        "Alfa is een heliumkern, bèta een elektron (bij bèta-min), gamma elektromagnetische straling.",
        kolommen=["Alfastraling", "Bètastraling", "Gammastraling"]),
    inv("Cesium-137 heeft een halveringstijd van ongeveer 30 jaar. Hoeveel procent van een staal is er na 120 jaar nog over?",
        ["6,25", "6.25"],
        "120 jaar = 4 halveringstijden: 100 → 50 → 25 → 12,5 → 6,25 %."),

    # Veiligheid, eenheden en onderzoek
    tabel(
        "Zet om.",
        [
            ("2,5 km in m", "2500"),
            ("72 km/h in m/s", "20"),
            ("350 mL in L", "0,35"),
        ],
        "1 km = 1000 m. Delen door 3,6 zet km/h om naar m/s. 1 L = 1000 mL.",
        kolommen=["0,35", "20", "2500"]),
    koppel(
        "Koppel het gevarenpictogram aan zijn betekenis.",
        [
            ["vlam", "ontvlambaar"],
            ["doodshoofd", "acuut giftig"],
            ["reageerbuisjes boven een hand", "bijtend"],
        ],
        ["radioactief afval", "stroomgevaar"],
        "GHS-pictogrammen waarschuwen voor het soort gevaar van een stof."),
    tabel(
        "Welke variabele is het in dit onderzoek? Je onderzoekt of de temperatuur invloed heeft op hoe snel een bruistablet oplost.",
        [
            ("De temperatuur van het water", "Onafhankelijke variabele"),
            ("De tijd tot de tablet opgelost is", "Afhankelijke variabele"),
            ("De hoeveelheid water en het soort tablet", "Constante variabelen"),
        ],
        "De onafhankelijke variabele verander je zelf, de afhankelijke meet je, en de rest hou je constant voor een eerlijke test.",
        kolommen=["Onafhankelijke variabele", "Afhankelijke variabele", "Constante variabelen"]),

    keuze(
        "Een oplossing met pH 3 is [[*zuur|basisch|neutraal]]. Ze bevat [[*tien keer meer|tien keer minder|evenveel]] H₃O⁺-ionen dan een oplossing met pH 4.",
        "Onder pH 7 is een oplossing zuur. Eén pH-eenheid lager betekent een tien keer grotere concentratie H₃O⁺."),
    mk("Een bal wordt horizontaal weggegooid van een toren. Welke kracht werkt er tijdens de vlucht op de bal als je de luchtweerstand verwaarloost?",
       ["Enkel de zwaartekracht, verticaal naar beneden.", "Een kracht in de bewegingsrichting en de zwaartekracht.", "Geen enkele kracht, want de bal beweegt vanzelf.", "Enkel een horizontale kracht van de werper."],
       0,
       "Na het loslaten duwt de hand niet meer. Enkel de zwaartekracht werkt: de horizontale snelheid blijft, de verticale neemt toe."),
    tabel(
        "Welke bloedgroep kan het kind hebben? Vader heeft bloedgroep AB, moeder bloedgroep O.",
        [
            ("Bloedgroep A", J),
            ("Bloedgroep B", J),
            ("Bloedgroep AB", F),
            ("Bloedgroep O", F),
        ],
        "De vader geeft I^A of I^B door, de moeder altijd i. Het kind is dus I^A i (A) of I^B i (B)."),
    sorteer(
        "Is dit een argument voor evolutie uit de fossielen, uit de vergelijkende anatomie of uit de moleculaire biologie?",
        ["Fossielen", "Vergelijkende anatomie", "Moleculaire biologie"],
        [
            ["Overgangsvormen zoals Archaeopteryx", "Fossielen"],
            ["Dezelfde botten in een vleermuisvleugel en een mensenarm", "Vergelijkende anatomie"],
            ["Een gelijkaardige DNA-volgorde bij mens en chimpansee", "Moleculaire biologie"],
            ["Oudere aardlagen bevatten eenvoudigere levensvormen", "Fossielen"],
        ],
        "Fossielen tonen veranderingen in de tijd, homologe organen een gemeenschappelijke bouw, en DNA verwantschap op moleculair niveau."),

    # Uitleg
    open_("Leg in 3 à 5 zinnen uit waarom een antibioticum niet helpt tegen griep, en wat er gebeurt als mensen antibiotica te vaak of verkeerd gebruiken.",
          "Griep wordt veroorzaakt door een virus, en antibiotica werken enkel tegen bacteriën. Ze hebben dus geen effect op griep. Als je antibiotica te vaak of te kort gebruikt, overleven de bacteriën die toevallig resistent zijn. Die vermenigvuldigen zich, zodat er resistente bacteriën ontstaan waartegen het antibioticum niet meer werkt.",
          "Een goed antwoord zegt dat antibiotica tegen bacteriën werken en niet tegen virussen, en legt resistentie uit als selectie van bacteriën die het antibioticum overleven."),
]
