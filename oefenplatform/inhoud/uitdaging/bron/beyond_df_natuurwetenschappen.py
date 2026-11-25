# -*- coding: utf-8 -*-
"""Uitdaging Natuurwetenschappen 🌍 Beyond dubbele finaliteit (25 november
2026), in de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Een voedingsetiket en een golf om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde,
rekenvragen en een korte uitleg in eigen woorden. Geen nieuwe leerstof: alles
staat in de hoofdstukken van Natuurwetenschappen Beyond dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_df_natuurwetenschappen.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Natuurwetenschappen"
BESTAND = "beyond-df-natuurwetenschappen-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/natuurwetenschappen-beyond-df-uitdaging"
ETIKET = "etiket-granen.svg"
GOLF = "golf-pijlen.svg"

# klikvakken uit maak_prenten_beyond_df_natuurwetenschappen.py
AMPLITUDE = [12.9, 38.1, 6.4, 12.3]
GOLFLENGTE = [37.3, 15.0, 6.4, 12.3]
HALVE = [26.8, 87.7, 6.4, 12.3]


def zin(i, n=6):
    """Klikvak van regel i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Etiket (prent)
    klik("Bekijk het etiket. Klik op de regel die toont hoeveel toegevoegde en natuurlijke suikers erin zitten.",
         ETIKET, [zin(3)],
         "Bij koolhydraten staat 'waarvan suikers': 22 g per 100 g."),
    klik("Klik op de regel die het belangrijkst is voor iemand die minder vet voor hart en bloedvaten wil eten.",
         ETIKET, [zin(2)],
         "Verzadigde vetzuren verhogen de cholesterol. Het etiket vermeldt ze apart bij de vetten."),
    klik("Klik op de voedingsstof die je lichaam vooral nodig heeft om spieren op te bouwen.",
         ETIKET, [zin(5)],
         "Eiwitten zijn bouwstoffen voor spieren en andere weefsels."),
    met_prent(ETIKET, tabel(
        "Reken met het etiket. Je eet een kom van 40 g.",
        [
            ("Suikers in die kom (g)", "8,8"),
            ("Energie in die kom (kJ)", "640"),
            ("Zout in die kom (g)", "0,36"),
        ],
        "40 g is 0,4 keer 100 g: 22 · 0,4 = 8,8 g suiker, 1600 · 0,4 = 640 kJ en 0,9 · 0,4 = 0,36 g zout.",
        kolommen=["0,36", "8,8", "640"])),
    met_prent(ETIKET, tabel(
        "Klopt dit volgens het etiket?",
        [
            ("Koolhydraten leveren het grootste deel van de massa.", J),
            ("Meer dan een kwart van de massa bestaat uit suikers.", F),
            ("Het product bevat voedingsvezels die de darmwerking helpen.", J),
            ("Het product bevat meer eiwitten dan koolhydraten.", F),
        ],
        "75 g op 100 g is koolhydraat. Suikers zijn 22 g, minder dan een kwart. Er zijn 8 g eiwitten tegen 75 g koolhydraten.")),

    # Golf (prent)
    klik("Bekijk de golf. Klik op het cijfer bij de pijl die de golflengte aangeeft.",
         GOLF, [GOLFLENGTE],
         "De golflengte is de afstand tussen twee opeenvolgende toppen: pijl 2."),
    klik("Klik op het cijfer bij de pijl die de amplitude aangeeft.",
         GOLF, [AMPLITUDE],
         "De amplitude is de grootste uitwijking ten opzichte van de evenwichtsstand: van de stippellijn tot de top."),
    met_prent(GOLF, keuze(
        "Pijl 3 gaat van een top tot een dal: dat is [[*een halve golflengte|twee golflengtes|de amplitude]]. Bij een transversale golf trillen de deeltjes [[*loodrecht op|evenwijdig met]] de voortplantingsrichting.",
        "Van top tot dal is een halve golflengte. Bij een transversale golf bewegen de deeltjes op en neer terwijl de golf vooruitgaat.")),
    met_prent(GOLF, inv(
        "De golflengte van deze golf is 2,0 m en de frequentie 5,0 Hz. Hoe groot is de golfsnelheid in m/s?",
        ["10", "10,0"],
        "v = λ · f = 2,0 · 5,0 = 10 m/s.")),

    # Voortplanting
    volgorde(
        "Zet de stappen in de juiste volgorde.",
        ["Eisprong", "Bevruchting in de eileider", "Klievingsdelingen", "Innesteling in de baarmoeder", "Ontwikkeling van de foetus"],
        "Na de eisprong kan een zaadcel de eicel in de eileider bevruchten. Het embryo deelt, nestelt zich in en groeit verder als foetus."),
    tabel(
        "Welke vorm van anticonceptie is het?",
        [
            ("Condoom", "Barrièremethode"),
            ("De pil", "Hormonaal"),
            ("Sterilisatie", "Definitief"),
        ],
        "Een condoom houdt zaadcellen tegen en beschermt ook tegen soa's. De pil werkt met hormonen. Sterilisatie is (bijna) onomkeerbaar.",
        kolommen=["Barrièremethode", "Hormonaal", "Definitief"]),
    keuze(
        "Een eeneiige tweeling ontstaat uit [[*één bevruchte eicel die splitst|twee eicellen met twee zaadcellen]] en heeft [[*hetzelfde|verschillend]] DNA.",
        "Eeneiige tweelingen komen uit één zygote en zijn genetisch identiek. Twee-eiige tweelingen zijn zoals gewone broers en zussen."),

    # Genetica
    inv("Een stukje DNA heeft de volgorde TACGGA. Welke mRNA-volgorde wordt ervan afgeschreven? Zes letters.",
        ["AUGCCU"],
        "In RNA staat U in plaats van T. T → A, A → U, C → G, G → C: AUGCCU."),
    tabel(
        "Twee ouders zijn allebei Bb (B = bruine ogen dominant, b = blauw). Hoeveel procent kans heeft een kind op",
        [
            ("genotype BB", "25 %"),
            ("genotype Bb", "50 %"),
            ("blauwe ogen", "25 %"),
            ("bruine ogen", "75 %"),
        ],
        "Kruising Bb × Bb geeft BB, Bb, Bb en bb. Bruin: BB of Bb (3 op 4). Blauw: enkel bb (1 op 4).",
        kolommen=["25 %", "50 %", "75 %"]),
    keuze(
        "Een gen is een stukje [[*DNA|eiwit|vet]] met de code voor een [[*eiwit|chromosoom|cel]].",
        "Bij genexpressie wordt de code van een gen via mRNA vertaald naar een eiwit."),

    # Evolutie
    sorteer(
        "Past dit bij de theorie van Darwin of bij een misvatting over evolutie?",
        ["Darwin", "Misvatting"],
        [
            ["In een populatie bestaat variatie tussen individuen.", "Darwin"],
            ["Een giraf kreeg een lange nek omdat ze haar nek uitrekte.", "Misvatting"],
            ["Wie beter aangepast is, krijgt meer nakomelingen.", "Darwin"],
            ["Dieren veranderen bewust om te overleven.", "Misvatting"],
        ],
        "Darwin: variatie bestaat al, de omgeving selecteert. Eigenschappen die je tijdens je leven verwerft, geef je niet door."),
    mk("Waarom worden bacteriën resistent tegen een antibioticum?",
       ["Toevallig resistente bacteriën overleven en vermenigvuldigen zich.", "Bacteriën beslissen samen om zich tegen het middel te verdedigen.", "Het antibioticum verandert vanzelf in voedsel voor de bacteriën.", "De patiënt wordt resistent, waardoor de bacteriën ook mee veranderen."],
       0,
       "Dat is natuurlijke selectie: het antibioticum doodt de gevoelige bacteriën, de resistente blijven over."),
    keuze(
        "Als twee populaties lang gescheiden leven, bijvoorbeeld door een gebergte, kunnen ze uitgroeien tot [[*twee soorten|één soort|een kruising]] die zich [[*niet meer|nog altijd]] onderling vruchtbaar kunnen voortplanten.",
        "Door isolatie en verschillende selectie groeien populaties uit elkaar. Zo ontstaan nieuwe soorten."),

    # Stoffen, etiketten en dosis
    koppel(
        "Koppel het gevarenpictogram aan zijn betekenis.",
        [
            ["vlam", "ontvlambaar"],
            ["uitroepteken", "schadelijk of irriterend"],
            ["dode vis en boom", "gevaarlijk voor het milieu"],
            ["corrosie (bijtende druppels)", "bijtend"],
        ],
        ["radioactief"],
        "GHS-pictogrammen staan in een rode ruit en tonen het soort gevaar."),
    tabel(
        "Wat betekent dit op een etiket?",
        [
            ("Ten minste houdbaar tot (THT)", "Kwaliteit kan daarna wat minder zijn"),
            ("Te gebruiken tot (TGT)", "Daarna niet meer opeten"),
            ("TGT op verse kip of gehakt", "Daarna niet meer opeten"),
            ("THT op een pak droge pasta", "Kwaliteit kan daarna wat minder zijn"),
        ],
        "THT gaat over kwaliteit: vaak is het product nog goed. TGT gaat over veiligheid bij bederfbare producten.",
        kolommen=["Kwaliteit kan daarna wat minder zijn", "Daarna niet meer opeten"]),
    inv("Je lost 5 g suiker op in 250 mL water. Wat is de massaconcentratie in g/L?",
        ["20"],
        "250 mL = 0,25 L. 5 g / 0,25 L = 20 g/L."),
    mk("Een kind van 20 kg mag 10 mg per kg lichaamsgewicht van een geneesmiddel krijgen. Hoeveel mg is dat?",
       ["200 mg", "20 mg", "2 mg", "2000 mg"],
       0,
       "10 mg · 20 kg = 200 mg."),
    keuze(
        "'De dosis maakt het gif' betekent dat [[*elke stof giftig kan zijn bij een te grote hoeveelheid|enkel kunstmatige stoffen giftig zijn]]. Zelfs [[*water|lucht in een ballon]] is gevaarlijk als je er extreem veel van drinkt.",
        "Paracelsus stelde dat de hoeveelheid bepaalt of iets schadelijk is."),

    # Duurzame chemie
    tabel(
        "Is dit een principe van duurzame (groene) chemie?",
        [
            ("Hernieuwbare grondstoffen gebruiken", J),
            ("Afval vermijden in plaats van opruimen", J),
            ("Zo veel mogelijk giftige oplosmiddelen gebruiken", F),
            ("Producten maken die in de natuur afbreekbaar zijn", J),
        ],
        "Groene chemie wil gevaarlijke stoffen en afval beperken en zuinig omgaan met grondstoffen en energie."),

    # Elektromagnetisme
    keuze(
        "Rond een draad waar stroom door loopt, ontstaat een [[*magnetisch veld|zwaartekrachtveld]]. Een elektromagneet wordt sterker als je [[*meer windingen gebruikt|de stroom uitschakelt]].",
        "Elektrische stroom maakt magnetisme. Meer windingen of een grotere stroom maken de elektromagneet sterker."),
    tabel(
        "Wat gebeurt er met een elektromagneet (een spoel met stroom)?",
        [
            ("Je wikkelt meer windingen.", "Sterker"),
            ("Je steekt er een ijzeren kern in.", "Sterker"),
            ("Je draait de stroomrichting om.", "Polen wisselen"),
            ("Je schakelt de stroom uit.", "Geen magnetisme"),
        ],
        "Meer windingen of een ijzeren kern versterken het veld. De stroomrichting bepaalt waar de noordpool ligt, en zonder stroom is er geen magnetisme.",
        kolommen=["Sterker", "Polen wisselen", "Geen magnetisme"]),

    # Golven en spectrum
    sorteer(
        "Is dit een mechanische golf of een elektromagnetische golf?",
        ["Mechanisch", "Elektromagnetisch"],
        [
            ["geluid", "Mechanisch"],
            ["licht", "Elektromagnetisch"],
            ["een golf op het water", "Mechanisch"],
            ["röntgenstraling", "Elektromagnetisch"],
        ],
        "Mechanische golven hebben een middenstof nodig. Elektromagnetische golven gaan ook door het luchtledige."),
    tabel(
        "Welke straling wordt hiervoor gebruikt?",
        [
            ("Eten opwarmen", "Microgolven"),
            ("Een botbreuk zien", "Röntgenstraling"),
            ("Een tv-afstandsbediening", "Infrarood"),
            ("Zonnebrand op je huid", "Ultraviolet"),
        ],
        "Elk deel van het elektromagnetisch spectrum heeft zijn eigen toepassingen en gevaren.",
        kolommen=["Microgolven", "Röntgenstraling", "Infrarood", "Ultraviolet"]),
    keuze(
        "Geluid gaat [[*niet|wel]] door het luchtledige. Het gehoor raakt beschadigd bij langdurig geluid boven ongeveer [[*80 dB|20 dB|5 dB]].",
        "Geluid heeft deeltjes nodig om te trillen. Lang luid geluid beschadigt de haarcellen in je oor."),

    # Kernfysica
    tabel(
        "Alfa, bèta of gamma?",
        [
            ("Wordt al tegengehouden door een blad papier", "Alfa"),
            ("Gaat door papier, maar niet door enkele mm aluminium", "Bèta"),
            ("Heeft dik lood of beton nodig om af te schermen", "Gamma"),
        ],
        "Alfadeeltjes zijn groot en zwaar, bètadeeltjes zijn elektronen en gammastraling is energierijke elektromagnetische straling.",
        kolommen=["Alfa", "Bèta", "Gamma"]),
    inv("Een stof heeft een halveringstijd van 6 uur. Hoeveel gram blijft er na 18 uur over van 80 g?",
        ["10"],
        "18 uur = 3 halveringstijden: 80 → 40 → 20 → 10 g."),
    mk("Wat gebeurt er bij kernsplijting in een kerncentrale?",
       ["Een zware kern splitst in lichtere kernen en er komt energie vrij.", "Twee lichte kernen smelten samen tot één zware kern, zoals in de zon.", "Elektronen springen van atoom naar atoom en er ontstaat stroom.", "Steenkool verbrandt met zuurstof en de warmte drijft een turbine."],
       0,
       "Uraniumkernen splitsen na het opvangen van een neutron. De vrijgekomen warmte maakt stoom die een turbine aandrijft."),
    keuze(
        "Een voordeel van kernenergie is dat ze [[*weinig CO₂|veel CO₂]] uitstoot. Een nadeel is het [[*radioactief afval|gebrek aan brandstof]] dat lang gevaarlijk blijft.",
        "Kerncentrales stoten tijdens de werking nauwelijks CO₂ uit, maar het afval moet duizenden jaren veilig opgeslagen worden."),

    # Veilig werken en onderzoek
    tabel(
        "Zet om.",
        [
            ("0,5 L in mL", "500"),
            ("2 kg in g", "2000"),
            ("3,5 cm in mm", "35"),
        ],
        "1 L = 1000 mL, 1 kg = 1000 g, 1 cm = 10 mm.",
        kolommen=["35", "500", "2000"]),
    volgorde(
        "In welke volgorde verloopt een natuurwetenschappelijk onderzoek?",
        ["Onderzoeksvraag", "Hypothese", "Experiment uitvoeren", "Resultaten verwerken", "Besluit"],
        "Je stelt een vraag, formuleert een vermoeden, test het, verwerkt de metingen en trekt een besluit."),
    mk("Waarom draag je een veiligheidsbril bij een proef met zuren?",
       ["Om je ogen te beschermen tegen spatten.", "Om de kleuren in de proef beter te zien.", "Om je handen te beschermen tegen het zuur.", "Om te verhinderen dat de dampen ontsnappen."],
       0,
       "Zuren zijn bijtend. Een spat in het oog kan blijvende schade geven."),

    tabel(
        "Is dit een geval van bestraling of van besmetting?",
        [
            ("Je krijgt een röntgenfoto en straalt daarna zelf niet.", "Bestraling"),
            ("Radioactief stof komt op je huid of in je lichaam.", "Besmetting"),
            ("Je eet groenten met radioactieve deeltjes.", "Besmetting"),
        ],
        "Bij bestraling word je van buitenaf getroffen door straling. Bij besmetting draag je de radioactieve stof zelf mee.",
        kolommen=["Bestraling", "Besmetting"]),
    keuze(
        "Een toon met een frequentie van 25 000 Hz is [[*ultrasoon|infrasoon|hoorbaar]] geluid. Mensen horen ongeveer van [[*20 Hz tot 20 000 Hz|0 Hz tot 200 Hz|1000 Hz tot 100 000 Hz]].",
        "Boven 20 000 Hz spreek je van ultrasoon geluid; vleermuizen en echografie gebruiken het."),
    mk("Waarom is een prenatale test zoals de NIPT soms zinvol?",
       ["Hij kan wijzen op chromosoomafwijkingen bij de foetus.", "Hij bepaalt de oogkleur van het kind met volledige zekerheid.", "Hij voorkomt dat de baby ooit ziek kan worden na de geboorte.", "Hij verandert het DNA van de foetus als dat nodig is."],
       0,
       "De NIPT onderzoekt DNA-stukjes van de foetus in het bloed van de moeder en kan bv. op trisomie 21 wijzen."),

    # Uitleg
    open_("Leg in 3 à 5 zinnen uit hoe je met een voedingsetiket twee soorten ontbijtgranen kan vergelijken om de gezondste te kiezen.",
          "Ik vergelijk de waarden per 100 g, zodat het eerlijk is. Ik kijk naar de suikers: hoe minder, hoe beter. Ik kijk ook naar de verzadigde vetten en het zout, die liefst laag zijn. Veel voedingsvezels en eiwitten zijn een pluspunt. Zo kies ik de granen met minder suiker en zout en meer vezels.",
          "Een goed antwoord vergelijkt per 100 g en noemt minstens drie waarden (suikers, verzadigde vetten, zout, vezels, eiwitten) met wat gezond is."),
]
