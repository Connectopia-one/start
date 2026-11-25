# -*- coding: utf-8 -*-
"""Uitdaging Chemie 🚀 Boost doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door elkaar
halen. Een stuk van het periodiek systeem en een pH-schaal om op te klikken,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde, rekenvragen en
een korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Chemie Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_chemie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Chemie"
BESTAND = "boost-chemie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/chemie-boost-uitdaging"
PSE = "periodiek-systeem.svg"
PH = "ph-schaal.svg"

# klikvakken uit maak_prenten_boost_chemie.py
EL = {'H': [7.0, 21.2, 11.0, 21.2], 'He': [84.0, 21.2, 11.0, 21.2], 'Li': [7.0, 42.3, 11.0, 21.2],
      'Be': [18.0, 42.3, 11.0, 21.2], 'B': [29.0, 42.3, 11.0, 21.2], 'C': [40.0, 42.3, 11.0, 21.2],
      'N': [51.0, 42.3, 11.0, 21.2], 'O': [62.0, 42.3, 11.0, 21.2], 'F': [73.0, 42.3, 11.0, 21.2],
      'Ne': [84.0, 42.3, 11.0, 21.2], 'Na': [7.0, 63.5, 11.0, 21.2], 'Mg': [18.0, 63.5, 11.0, 21.2],
      'Al': [29.0, 63.5, 11.0, 21.2], 'Si': [40.0, 63.5, 11.0, 21.2], 'P': [51.0, 63.5, 11.0, 21.2],
      'S': [62.0, 63.5, 11.0, 21.2], 'Cl': [73.0, 63.5, 11.0, 21.2], 'Ar': [84.0, 63.5, 11.0, 21.2]}
OPL = {1: [3.0, 23.4, 15.0, 25.5], 2: [22.4, 23.4, 15.0, 25.5], 3: [41.8, 23.4, 15.0, 25.5],
       4: [61.2, 23.4, 15.0, 25.5], 5: [80.6, 23.4, 15.0, 25.5]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Periodiek systeem (prent)
    klik("Bekijk het periodiek systeem. Klik op het element met de elektronenconfiguratie 2, 8, 3.",
         PSE, [EL["Al"]],
         "2 + 8 + 3 = 13 elektronen, dus atoomnummer 13: aluminium. Drie bezette schillen betekent periode 3, drie valentie-elektronen betekent groep IIIA."),
    klik("Klik op het halogeen uit periode 3.",
         PSE, [EL["Cl"]],
         "De halogenen staan in groep VIIA. In periode 3 is dat chloor."),
    klik("Klik op het element met de hoogste elektronegativiteit.",
         PSE, [EL["F"]],
         "De elektronegativiteit stijgt naar rechtsboven in het periodiek systeem (zonder de edelgassen). Fluor is de koploper."),
    klik("Klik op het element dat een ion met lading 2+ vormt en net als neon 10 elektronen overhoudt.",
         PSE, [EL["Mg"]],
         "Magnesium (12 elektronen) staat in groep IIA en geeft twee elektronen af: Mg²⁺ heeft 10 elektronen, net als neon."),
    met_prent(PSE, tabel(
        "Hoort dit element bij de metalen, de niet-metalen of de edelgassen?",
        [
            ("Na", "Metaal"),
            ("S", "Niet-metaal"),
            ("Ar", "Edelgas"),
            ("Mg", "Metaal"),
        ],
        "Metalen staan links in het periodiek systeem, niet-metalen rechtsboven en de edelgassen in groep VIIIA.",
        kolommen=["Metaal", "Niet-metaal", "Edelgas"])),

    # pH (prent)
    klik("Bekijk de pH-schaal. Klik op de oplossing die het sterkst basisch is.",
         PH, [OPL[5]],
         "Hoe hoger de pH boven 7, hoe sterker basisch. De ontstopper zit rond pH 13."),
    klik("Klik op de oplossing die niet zuur en niet basisch is.",
         PH, [OPL[3]],
         "Zuiver water heeft een pH van 7: niet zuur en niet basisch."),
    met_prent(PH, keuze(
        "Je druppelt fenolftaleïne in de vijf oplossingen. Ze kleurt paars in [[*4 en 5|1 en 2|3, 4 en 5]]. Lakmoes kleurt rood in [[*1 en 2|4 en 5|3]].",
        "Fenolftaleïne wordt paars in een basisch midden (pH boven 7). Lakmoes wordt rood in een zuur midden en blauw in een basisch midden.")),
    met_prent(PH, mk(
        "Welk ion is in oplossing 1 in grote hoeveelheid aanwezig?",
        ["H⁺", "OH⁻", "Na⁺", "Cl⁻"],
        0,
        "Een zure oplossing bevat veel H⁺-ionen. Een basische oplossing bevat veel OH⁻-ionen.")),

    # Mengsels en scheiden
    tabel(
        "Welke scheidingstechniek kies je?",
        [
            ("Zuiver water uit zeewater halen", "Destilleren"),
            ("Zand uit water halen", "Filtreren"),
            ("De kleurstoffen van een stift scheiden", "Chromatografie"),
            ("Olie en water die in twee lagen liggen", "Decanteren"),
        ],
        "Destilleren benut het verschil in kookpunt, filtreren de deeltjesgrootte, chromatografie de verschillende hechting en decanteren de massadichtheid.",
        kolommen=["Destilleren", "Filtreren", "Chromatografie", "Decanteren"]),
    koppel(
        "Koppel het mengsel aan het soort mengsel.",
        [
            ["mayonaise", "emulsie"],
            ["vruchtensap met pulp die zakt", "suspensie"],
            ["rook", "vaste deeltjes in een gas"],
        ],
        ["zuivere stof"],
        "Een emulsie is vloeistof in vloeistof, een suspensie vaste deeltjes in een vloeistof en rook vaste deeltjes in een gas. Geen van de drie is een zuivere stof."),
    keuze(
        "Een zuivere stof heeft een vast [[*kookpunt|kooktraject]]. Een mengsel kookt over een [[*kooktraject|kookpunt]].",
        "Bij een mengsel verandert de samenstelling tijdens het koken, dus ook de temperatuur."),

    # Stoffen en formules
    sorteer(
        "Sorteer deze formules: enkelvoudige of samengestelde stof?",
        ["Enkelvoudig", "Samengesteld"],
        [
            ["O₃", "Enkelvoudig"],
            ["H₂O", "Samengesteld"],
            ["Fe", "Enkelvoudig"],
            ["NaCl", "Samengesteld"],
            ["N₂", "Enkelvoudig"],
            ["CO₂", "Samengesteld"],
        ],
        "Een enkelvoudige stof bevat maar één soort atomen, ook al staan er meerdere in een molecule zoals O₃."),
    inv("Hoeveel atomen zitten er in totaal in één formule-eenheid Ca(NO₃)₂?",
        ["9"],
        "1 Ca + 2 N + 6 O = 9 atomen."),

    # Reacties
    mk("Welke coëfficiënten maken de vergelijking … Al + … O₂ → … Al₂O₃ kloppend?",
       ["4, 3, 2", "2, 3, 1", "4, 2, 2", "2, 1, 1"],
       0,
       "Links 4 Al en 6 O, rechts 2 Al₂O₃ = 4 Al en 6 O. Je verandert enkel de coëfficiënten, nooit de indices."),
    inv("12 g magnesium reageert volledig met 8 g zuurstofgas. Hoeveel gram magnesiumoxide ontstaat er? Enkel het getal.",
        ["20"],
        "Volgens de wet van behoud van massa: 12 + 8 = 20 g."),
    sorteer(
        "Exo-energetisch of endo-energetisch?",
        ["Exo-energetisch", "Endo-energetisch"],
        [
            ["een kaars brandt", "Exo-energetisch"],
            ["fotosynthese", "Endo-energetisch"],
            ["de beker voelt koud aan tijdens de reactie", "Endo-energetisch"],
            ["de temperatuur stijgt van 20 naar 35 °C", "Exo-energetisch"],
        ],
        "Bij een exo-energetische reactie komt energie vrij (het wordt warmer). Bij een endo-energetische reactie wordt energie opgenomen."),

    # Atoombouw
    tabel(
        "Klopt dit voor het deeltje ²⁷Al³⁺ (atoomnummer 13)?",
        [
            ("Aantal protonen: 13", J),
            ("Aantal neutronen: 14", J),
            ("Aantal elektronen: 13", F),
            ("Het deeltje is een positief ion.", J),
        ],
        "Atoomnummer 13 = 13 protonen. 27 − 13 = 14 neutronen. Het ion gaf drie elektronen af, dus het heeft er nog 10."),
    keuze(
        "Een positief ion ontstaat doordat een atoom [[*elektronen afgeeft|protonen afgeeft|elektronen opneemt]]. Bijna de hele massa van een atoom zit in de [[*kern|elektronenwolk]].",
        "Het aantal protonen verandert niet bij een reactie. Elektronen zijn veel lichter dan protonen en neutronen."),

    # Bindingen en roosters
    tabel(
        "Welk bindingstype vind je in deze stof?",
        [
            ("NaCl", "Ionbinding"),
            ("H₂O", "Atoombinding"),
            ("koper", "Metaalbinding"),
            ("CH₄", "Atoombinding"),
        ],
        "Metaal en niet-metaal: ionbinding. Twee niet-metalen: atoombinding. Enkel metaalatomen: metaalbinding.",
        kolommen=["Ionbinding", "Atoombinding", "Metaalbinding"]),
    koppel(
        "Koppel de stof aan het roostertype.",
        [
            ["diamant", "atoomrooster"],
            ["keukenzout", "ionrooster"],
            ["vast koolstofdioxide", "molecuulrooster"],
            ["ijzer", "metaalrooster"],
        ],
        [],
        "Diamant is één groot netwerk van koolstofatomen, keukenzout een rooster van Na⁺ en Cl⁻, droog ijs bevat losse CO₂-moleculen en ijzer heeft vrije elektronen."),
    mk("Waarom geleidt een zoutoplossing elektriciteit en een vast zout niet?",
       ["In de oplossing kunnen de ionen vrij bewegen.", "In de oplossing ontstaan er plots vrije elektronen.", "Een vast zout bevat helemaal geen geladen deeltjes.", "Water zelf geleidt de stroom, het zout doet niets."],
       0,
       "In een vast zout zitten de ionen vast in het rooster. In water dissocieert het zout en bewegen de ionen vrij."),

    # Stofklassen
    tabel(
        "Tot welke stofklasse hoort deze stof?",
        [
            ("CaO", "Oxide"),
            ("H₂SO₄", "Zuur"),
            ("NaOH", "Hydroxide"),
            ("CaCO₃", "Zout"),
        ],
        "Een oxide bevat zuurstof gebonden aan één ander element, een zuur begint met H, een hydroxide bevat OH en een zout bestaat uit een positief en een negatief ion.",
        kolommen=["Oxide", "Zuur", "Hydroxide", "Zout"]),
    koppel(
        "Koppel de formule aan de naam.",
        [
            ["NO₃⁻", "nitraation"],
            ["SO₄²⁻", "sulfaation"],
            ["CO₃²⁻", "carbonaation"],
        ],
        ["ammoniumion"],
        "Het ammoniumion is NH₄⁺, een positief ion."),
    keuze(
        "Een niet-metaaloxide dat met water reageert, vormt een [[*zuur|hydroxide]]. Een metaaloxide is [[*basevormend|zuurvormend]].",
        "CO₂ in water geeft koolzuur. CaO in water geeft calciumhydroxide."),

    # Organisch
    inv("Hoeveel waterstofatomen heeft het alkaan met zes koolstofatomen?",
        ["14"],
        "Een alkaan heeft de formule CₙH₂ₙ₊₂. Met n = 6: 2 · 6 + 2 = 14. Dat is hexaan, C₆H₁₄."),
    sleep(
        "Bij de volledige verbranding van een alkaan ontstaan [[koolstofdioxide]] en [[water]].",
        ["koolstofmonoxide", "waterstofgas"],
        "Bij een volledige verbranding reageert het alkaan met genoeg zuurstofgas: CO₂ en H₂O."),
    mk("Tot welke stofklasse hoort ethaanzuur in keukenazijn?",
       ["carbonzuren", "alkanen", "alkenen", "oxiden van koolstof"],
       0,
       "Ethaanzuur heeft een COOH-groep, de functionele groep van een carbonzuur."),

    # Oplossen
    mk("Je schudt olie en water in een fles. Waarom vormen ze na een tijd weer twee lagen in plaats van een oplossing?",
       ["Olie is apolair en water is polair.", "Olie heeft een hogere massadichtheid dan water.", "Olie bestaat uit ionen die niet loskomen.", "Water is apolair en trekt geen olie aan."],
       0,
       "Watermoleculen trekken elkaar sterk aan met waterstofbruggen. Apolaire oliemoleculen kunnen daar niet tussen."),
    sorteer(
        "Lost deze stof goed op in water of niet?",
        ["Lost goed op", "Lost slecht op"],
        [
            ["keukenzout", "Lost goed op"],
            ["olie", "Lost slecht op"],
            ["suiker", "Lost goed op"],
            ["hexaan", "Lost slecht op"],
        ],
        "Polaire stoffen en ionverbindingen lossen goed op in het polaire water. Apolaire stoffen zoals olie en alkanen niet."),
    mk("Welke dissociatievergelijking is juist voor calciumchloride in water?",
       ["CaCl₂ → Ca²⁺ + 2 Cl⁻", "CaCl₂ → Ca⁺ + Cl₂⁻", "CaCl₂ → Ca²⁺ + Cl₂²⁻", "CaCl₂ → Ca + Cl₂ (zonder ionen)"],
       0,
       "Het zout valt uiteen in zijn ionen: één Ca²⁺ en twee Cl⁻. De ladingen samen zijn nul."),

    # Reactietypes
    tabel(
        "Welk soort reactie wordt hier beschreven?",
        [
            ("Zoutzuur reageert met natriumhydroxide tot zout en water.", "Neutralisatie"),
            ("Twee heldere oplossingen geven samen een witte vaste stof.", "Neerslagreactie"),
            ("Magnesium brandt in zuurstofgas tot magnesiumoxide.", "Redoxreactie"),
        ],
        "Zuur + base geeft zout en water. Een neerslag is een slecht oplosbaar zout. Bij een verbranding van een metaal worden elektronen overgedragen.",
        kolommen=["Neutralisatie", "Neerslagreactie", "Redoxreactie"]),
    keuze(
        "In 2 Mg + O₂ → 2 MgO geeft magnesium elektronen af. Magnesium wordt [[*geoxideerd|gereduceerd]] en zuurstofgas is de [[*oxidator|reductor]].",
        "Wie elektronen afgeeft, wordt geoxideerd en is de reductor. Zuurstofgas neemt de elektronen op en is de oxidator."),

    # Mol en concentratie
    inv("Hoeveel mol is 1,806 · 10²⁴ moleculen water? Enkel het getal.",
        ["3", "3,00"],
        "Eén mol bevat 6,02 · 10²³ deeltjes. 1,806 · 10²⁴ / 6,02 · 10²³ = 3,00 mol."),
    inv("Hoeveel gram is 0,25 mol NaOH? (Na 23,0 · O 16,0 · H 1,0) Enkel het getal.",
        ["10", "10,0"],
        "De molaire massa van NaOH is 23,0 + 16,0 + 1,0 = 40,0 g/mol. 0,25 · 40,0 = 10,0 g."),
    inv("Je lost 0,300 mol glucose op tot 1,50 L oplossing. Wat is de molaire concentratie in mol/L? Enkel het getal.",
        ["0,2", "0,200"],
        "c = n / V = 0,300 / 1,50 = 0,200 mol/L."),
    inv("Hoeveel mL van een voorraad van 5,00 mol/L heb je nodig voor 200 mL van 0,500 mol/L? Enkel het getal.",
        ["20", "20,0"],
        "c₁ · V₁ = c₂ · V₂, dus V₁ = 0,500 · 200 / 5,00 = 20,0 mL."),

    # Labo
    tabel(
        "Welk glaswerk kies je?",
        [
            ("Precies 25,0 mL van een oplossing afmeten", "Pipet"),
            ("Ongeveer 40 mL water afmeten", "Maatcilinder"),
            ("Een oplossing zwenken zonder te morsen", "Erlenmeyer"),
        ],
        "Een pipet is het nauwkeurigst, een maatcilinder volstaat voor een ruwe meting en een erlenmeyer heeft een nauwe hals.",
        kolommen=["Pipet", "Maatcilinder", "Erlenmeyer"]),
    volgorde(
        "Zet de stappen van een wetenschappelijk onderzoek in de juiste volgorde.",
        ["Onderzoeksvraag", "Hypothese", "Proef uitvoeren", "Resultaten verwerken", "Besluit"],
        "Je vertrekt van een vraag, voorspelt een antwoord, toetst het met een proef, verwerkt de metingen en trekt een besluit."),

    # Schrijfopdracht
    open_("Je krijgt een mengsel van zand, keukenzout en water. Beschrijf in 4 à 6 zinnen hoe je zuiver zand en zuiver zout overhoudt, en noem de scheidingstechnieken.",
          "Eerst filtreer ik het mengsel. Het zand blijft als residu op de filter liggen en ik laat het drogen. Het filtraat is een heldere zoutoplossing. Die damp ik in, zodat het water verdampt en het zout achterblijft. Zo heb ik met filtreren en indampen het zand en het zout van elkaar gescheiden.",
          "Een goed antwoord noemt filtreren (zand als residu) en indampen of kristalliseren (zout uit het filtraat), in de juiste volgorde."),
]
