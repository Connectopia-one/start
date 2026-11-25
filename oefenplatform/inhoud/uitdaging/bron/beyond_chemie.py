# -*- coding: utf-8 -*-
"""Uitdaging Chemie 🌍 Beyond doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen, van naamgeving en bindingen tot evenwicht, zuren en basen,
redox en organische reacties. Casussen, tabellen, keuzelijsten, koppelen,
sorteren, volgorde, rekenvragen, klikvragen op twee zelf getekende prenten
(een energiediagram en een titratiecurve) en een open vraag. Geen nieuwe
leerstof: alles staat in de hoofdstukken van Chemie Beyond doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_chemie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Chemie"
BESTAND = "beyond-chemie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/chemie-beyond-uitdaging"
ENERGIE = "energiediagram-katalysator.svg"
TITRATIE = "titratiecurve-azijnzuur.svg"
# klikvakken: zie maak_prenten_beyond_chemie.py
TOP = [48.0, 17.5, 8.0, 13.3]
PRODUCTEN = [80.0, 70.0, 8.0, 13.3]
EQUIVALENTIE = [47.9, 36.5, 7.2, 11.6]
HALF = [27.7, 56.1, 7.2, 11.6]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Energiediagram (prent)
    klik("Bekijk het energiediagram. Klik op het geactiveerd complex van de reactie zonder katalysator.",
         ENERGIE, [TOP],
         "Het geactiveerd complex is de toestand met de hoogste energie, bovenaan de bult. Zonder katalysator ligt die op ongeveer 125 kJ."),
    klik("Klik op het energieniveau van de reactieproducten.",
         ENERGIE, [PRODUCTEN],
         "Rechts, na de bult, eindigt de reactie op het niveau van de producten: 20 kJ."),
    met_prent(ENERGIE, tabel(
        "Lees af en reken uit, in kJ.",
        [
            ("de activeringsenergie zonder katalysator", "\\(65\\)"),
            ("de activeringsenergie met katalysator", "\\(30\\)"),
            ("de reactie-energie \\(\\Delta E\\)", "\\(-40\\)"),
        ],
        "Activeringsenergie is de top min het niveau van de reagentia: \\(125 - 60\\) en \\(90 - 60\\). De reactie-energie is producten min reagentia: \\(20 - 60 = -40\\) kJ.",
        kolommen=["\\(-40\\)", "\\(30\\)", "\\(65\\)"])),
    met_prent(ENERGIE, keuze(
        "Deze reactie is [[*exo-energetisch|endo-energetisch]]. Een katalysator verlaagt de [[*activeringsenergie|reactie-energie]], zodat meer botsingen [[*effectief|onmogelijk]] worden.",
        "De producten liggen lager dan de reagentia: er komt energie vrij. Een katalysator biedt een andere weg met een lagere top, maar verandert de begin- en eindtoestand niet.")),

    # Titratiecurve (prent)
    klik("Bekijk de titratiecurve. Klik op het equivalentiepunt.",
         TITRATIE, [EQUIVALENTIE],
         "Het equivalentiepunt ligt midden in de steile sprong, bij 20 mL: daar is evenveel base toegevoegd als er zuur was."),
    klik("Klik op het punt van de curve waar de pH gelijk is aan de pKz van azijnzuur.",
         TITRATIE, [HALF],
         "Bij het halfequivalentiepunt, 10 mL, is de helft van het zuur omgezet in acetaat. Dan zijn zuur en geconjugeerde base even groot en is pH gelijk aan pKz."),
    met_prent(TITRATIE, inv(
        "Lees uit de curve de pKz van azijnzuur af. Rond af op één decimaal.",
        ["4,8", "4.8", "4,7", "4.7", "4,75", "4.75"],
        "Bij 10 mL, de helft van het equivalentievolume, lees je een pH van ongeveer 4,75 af. Dat is de pKz.")),
    met_prent(TITRATIE, tabel(
        "Klopt dit over deze titratie?",
        [
            ("Bij het equivalentiepunt is de pH groter dan 7.", J),
            ("Tussen 5 en 15 mL werkt de oplossing als een buffer.", J),
            ("De beginconcentratie van het azijnzuur is \\(0{,}1\\) mol/L.", J),
            ("Methyloranje is hier een goede indicator.", F),
        ],
        "Bij het equivalentiepunt is er enkel acetaat, een zwakke base: de pH is ongeveer 8,7. In het vlakke stuk zijn zuur en base samen aanwezig. 20 mL base van 0,1 mol/L neutraliseert 20 mL zuur, dus ook 0,1 mol/L. Methyloranje slaat te vroeg om; fenolftaleïne past bij een sprong rond pH 9.")),

    # Stofklassen en naamgeving
    tabel(
        "Tot welke stofklasse behoort deze stof?",
        [
            ("\\(\\mathrm{NaCl}\\)", "Zout"),
            ("\\(\\mathrm{H_2SO_4}\\)", "Zuur"),
            ("\\(\\mathrm{Ca(OH)_2}\\)", "Hydroxide"),
            ("\\(\\mathrm{CO_2}\\)", "Oxide"),
        ],
        "Een zout is een metaalion met een zuurrest. Een zuur heeft waterstof en een zuurrest. Een hydroxide bevat OH⁻. Een oxide is een verbinding van een element met zuurstof.",
        kolommen=["Oxide", "Hydroxide", "Zuur", "Zout"]),
    koppel(
        "Koppel de functionele groep aan de stofklasse.",
        [
            ["\\(-\\mathrm{OH}\\) aan een koolstofketen", "alcohol"],
            ["\\(-\\mathrm{COOH}\\)", "carbonzuur"],
            ["\\(-\\mathrm{CHO}\\) aan het uiteinde", "aldehyde"],
            ["\\(\\mathrm{C{=}O}\\) midden in de keten", "keton"],
            ["\\(-\\mathrm{NH_2}\\)", "amine"],
        ],
        ["ester", "ether"],
        "Elke stofklasse heeft haar eigen functionele groep. Bij een aldehyde zit de C=O-groep aan het uiteinde, bij een keton tussen twee koolstofatomen."),
    tabel(
        "Welke soort isomerie is dit?",
        [
            ("butaan en methylpropaan", "Ketenisomerie"),
            ("propanal en propanon", "Functie-isomerie"),
            ("but-1-een en but-2-een", "Plaatsisomerie"),
            ("cis- en trans-but-2-een", "Z/E-isomerie"),
        ],
        "Bij ketenisomerie verschilt de vertakking, bij plaatsisomerie de plaats van de functionele groep, bij functie-isomerie de stofklasse. Z/E-isomerie gaat over de ligging rond een dubbele binding.",
        kolommen=["Ketenisomerie", "Plaatsisomerie", "Functie-isomerie", "Z/E-isomerie"]),

    # Atoombouw en binding
    mk("Welke elektronenconfiguratie hoort bij natrium (Z = 11)?",
       ["\\(1s^{2}\\,2s^{2}\\,2p^{6}\\,3s^{1}\\)", "\\(1s^{2}\\,2s^{2}\\,2p^{7}\\)", "\\(1s^{2}\\,2s^{2}\\,2p^{5}\\,3s^{2}\\)", "\\(1s^{2}\\,2s^{1}\\,2p^{6}\\,3s^{2}\\)"],
       0,
       "Eerst wordt 1s gevuld (2), dan 2s (2), dan 2p (6) en het laatste elektron komt in 3s. Een p-subniveau kan hoogstens 6 elektronen bevatten."),
    tabel(
        "Welke ruimtelijke vorm heeft de molecule?",
        [
            ("\\(\\mathrm{CH_4}\\)", "Tetraëder"),
            ("\\(\\mathrm{NH_3}\\)", "Piramide"),
            ("\\(\\mathrm{H_2O}\\)", "Gebogen"),
            ("\\(\\mathrm{CO_2}\\)", "Lineair"),
        ],
        "Vier bindende paren geven een tetraëder. Bij ammoniak duwt één vrij paar de drie bindingen naar beneden: een piramide. Water heeft twee vrije paren en is gebogen. CO₂ heeft geen vrije paren op het centrale atoom en is lineair.",
        kolommen=["Lineair", "Gebogen", "Piramide", "Tetraëder"]),
    sorteer(
        "Is deze molecule polair of apolair?",
        ["Polair", "Apolair"],
        [
            ["\\(\\mathrm{H_2O}\\)", "Polair"],
            ["\\(\\mathrm{CO_2}\\)", "Apolair"],
            ["\\(\\mathrm{NH_3}\\)", "Polair"],
            ["\\(\\mathrm{CH_4}\\)", "Apolair"],
            ["\\(\\mathrm{HCl}\\)", "Polair"],
        ],
        "Een molecule is polair als de ladingen niet symmetrisch verdeeld zijn. In CO₂ en CH₄ heffen de polaire bindingen elkaar op door de symmetrie."),

    # Chemisch rekenen
    inv("Hoeveel gram natriumhydroxide (\\(M = 40\\) g/mol) heb je nodig voor \\(0{,}5\\) mol? Geef enkel het getal.",
        "20",
        "\\(m = n \\cdot M = 0{,}5 \\cdot 40 = 20\\) gram."),
    inv("Je lost \\(5{,}85\\) g NaCl (\\(M = 58{,}5\\) g/mol) op tot \\(250\\) mL oplossing. Wat is de concentratie in mol/L? Geef enkel het getal.",
        ["0,4", "0.4", "0,40", "0.40"],
        "\\(n = 5{,}85 / 58{,}5 = 0{,}1\\) mol. \\(c = n / V = 0{,}1 / 0{,}250 = 0{,}4\\) mol/L."),
    casus(
        "Je laat \\(4\\) mol waterstofgas reageren met \\(3\\) mol zuurstofgas volgens \\(2\\,\\mathrm{H_2} + \\mathrm{O_2} \\rightarrow 2\\,\\mathrm{H_2O}\\).",
        [
            keuze(
                "Het limiterend reagens is [[*waterstofgas|zuurstofgas]]. Er blijft [[*1|2|0]] mol zuurstofgas over.",
                "4 mol H₂ heeft maar 2 mol O₂ nodig. Er is 3 mol O₂, dus H₂ raakt eerst op en 1 mol O₂ blijft over."),
            inv("Hoeveel gram water ontstaat er (\\(M = 18\\) g/mol)? Geef enkel het getal.",
                "72",
                "Uit 4 mol H₂ ontstaat 4 mol water: \\(4 \\cdot 18 = 72\\) gram."),
        ],
    ),
    inv("Welk volume in liter neemt \\(0{,}5\\) mol van een gas in bij \\(0\\) °C en normale druk? Geef enkel het getal.",
        ["11,2", "11.2"],
        "Het molair volume bij 0 °C en normale druk is 22,4 liter per mol: \\(0{,}5 \\cdot 22{,}4 = 11{,}2\\) liter."),

    # Snelheid en evenwicht
    tabel(
        "De reactie \\(\\mathrm{N_2} + 3\\,\\mathrm{H_2} \\rightleftharpoons 2\\,\\mathrm{NH_3}\\) is exo-energetisch. In welke richting verschuift het evenwicht?",
        [
            ("je verhoogt de druk", "Naar rechts"),
            ("je verhoogt de temperatuur", "Naar links"),
            ("je haalt ammoniak weg", "Naar rechts"),
            ("je voegt een katalysator toe", "Geen verschuiving"),
        ],
        "Hogere druk bevoordeelt de kant met minder gasdeeltjes (2 tegen 4). Warmte bevoordeelt de endo-energetische terugreactie. Een product wegnemen trekt het evenwicht naar rechts. Een katalysator versnelt beide richtingen evenveel.",
        kolommen=["Naar links", "Naar rechts", "Geen verschuiving"]),
    mk("Wat is de uitdrukking voor de evenwichtsconstante van \\(\\mathrm{N_2} + 3\\,\\mathrm{H_2} \\rightleftharpoons 2\\,\\mathrm{NH_3}\\)?",
       ["\\(K = \\dfrac{[\\mathrm{NH_3}]^{2}}{[\\mathrm{N_2}]\\,[\\mathrm{H_2}]^{3}}\\)", "\\(K = \\dfrac{[\\mathrm{N_2}]\\,[\\mathrm{H_2}]^{3}}{[\\mathrm{NH_3}]^{2}}\\)", "\\(K = \\dfrac{2\\,[\\mathrm{NH_3}]}{[\\mathrm{N_2}] + 3\\,[\\mathrm{H_2}]}\\)", "\\(K = \\dfrac{[\\mathrm{NH_3}]}{[\\mathrm{N_2}]\\,[\\mathrm{H_2}]}\\)"],
       0,
       "Producten staan in de teller, reagentia in de noemer, met de coëfficiënten als exponent."),
    keuze(
        "Een reactie gaat sneller als je de temperatuur [[*verhoogt|verlaagt]], de concentratie [[*verhoogt|verlaagt]] of de stof [[*fijner verdeelt|in één groot stuk gebruikt]].",
        "Volgens het botsingsmodel botsen deeltjes dan vaker en met meer energie, of is er meer contactoppervlak."),

    # Zuren en basen
    koppel(
        "Koppel elk zuur aan zijn geconjugeerde base.",
        [
            ["\\(\\mathrm{NH_4^{+}}\\)", "\\(\\mathrm{NH_3}\\)"],
            ["\\(\\mathrm{H_2O}\\)", "\\(\\mathrm{OH^{-}}\\)"],
            ["\\(\\mathrm{HCl}\\)", "\\(\\mathrm{Cl^{-}}\\)"],
            ["\\(\\mathrm{H_3O^{+}}\\)", "\\(\\mathrm{H_2O}\\)"],
        ],
        ["\\(\\mathrm{NH_2^{-}}\\)", "\\(\\mathrm{H_2}\\)"],
        "De geconjugeerde base is wat overblijft als het zuur één proton heeft afgestaan."),
    tabel(
        "Bereken de pH bij \\(25\\) °C.",
        [
            ("\\([\\mathrm{H_3O^{+}}] = 0{,}01\\) mol/L", "\\(2\\)"),
            ("een NaOH-oplossing van \\(0{,}001\\) mol/L", "\\(11\\)"),
            ("een oplossing met pOH \\(4\\)", "\\(10\\)"),
        ],
        "\\(\\mathrm{pH} = -\\log[\\mathrm{H_3O^{+}}] = 2\\). NaOH is een sterke base: pOH 3, dus pH 11. Bij 25 °C is pH + pOH = 14.",
        kolommen=["\\(2\\)", "\\(10\\)", "\\(11\\)"]),
    mk("Welk mengsel vormt een buffer?",
       ["azijnzuur met natriumacetaat", "zoutzuur met natriumchloride", "natriumhydroxide met water", "zoutzuur met zwavelzuur"],
       0,
       "Een buffer bevat een zwak zuur en zijn geconjugeerde base. Zoutzuur is een sterk zuur, en Cl⁻ is geen bruikbare base."),

    keuze(
        "Een molecule etheen, \\(\\mathrm{C_2H_4}\\), heeft [[*5|4|6]] sigmabindingen en [[*1|2|0]] pi-binding.",
        "Vier C-H-bindingen en één van de twee bindingen tussen de koolstofatomen zijn sigmabindingen. De tweede binding van de dubbele binding is een pi-binding."),
    inv("Bereken de pH van zoutzuur met een concentratie van \\(0{,}001\\) mol/L. Geef enkel het getal.",
        "3",
        "Zoutzuur is een sterk zuur en splitst volledig: \\([\\mathrm{H_3O^{+}}] = 10^{-3}\\) mol/L, dus pH 3."),
    inv("Je titreert \\(25\\) mL zoutzuur met natriumhydroxide van \\(0{,}2\\) mol/L en verbruikt \\(15\\) mL tot het equivalentiepunt. Wat is de concentratie van het zoutzuur, in mol/L? Geef enkel het getal.",
        ["0,12", "0.12"],
        "Bij het equivalentiepunt is \\(n(\\mathrm{HCl}) = n(\\mathrm{NaOH}) = 0{,}2 \\cdot 0{,}015 = 0{,}003\\) mol. \\(c = 0{,}003 / 0{,}025 = 0{,}12\\) mol/L."),

    # Redox en elektrochemie
    tabel(
        "Welk oxidatiegetal heeft het genoemde element?",
        [
            ("zwavel in \\(\\mathrm{H_2SO_4}\\)", "\\(+6\\)"),
            ("mangaan in \\(\\mathrm{KMnO_4}\\)", "\\(+7\\)"),
            ("stikstof in \\(\\mathrm{NH_3}\\)", "\\(-3\\)"),
            ("zuurstof in \\(\\mathrm{H_2O_2}\\)", "\\(-1\\)"),
        ],
        "De som van de oxidatiegetallen in een neutrale molecule is nul. H is meestal +1, O meestal −2 (behalve in peroxiden, waar het −1 is) en K is +1.",
        kolommen=["\\(-3\\)", "\\(-1\\)", "\\(+6\\)", "\\(+7\\)"]),
    keuze(
        "Bij \\(\\mathrm{Zn} + \\mathrm{Cu^{2+}} \\rightarrow \\mathrm{Zn^{2+}} + \\mathrm{Cu}\\) is zink de [[*reductor|oxidator]]. Het koperion wordt [[*gereduceerd|geoxideerd]].",
        "Zink staat elektronen af: het is de reductor en wordt zelf geoxideerd. Het koperion neemt elektronen op en wordt gereduceerd."),
    inv("Wat is de bronspanning van een galvanische cel met een koper- en een zinkhalfcel bij normomstandigheden? Gebruik \\(E^{0}(\\mathrm{Cu^{2+}/Cu}) = 0{,}34\\) V en \\(E^{0}(\\mathrm{Zn^{2+}/Zn}) = -0{,}76\\) V. Geef enkel het getal in volt.",
        ["1,10", "1,1", "1.10", "1.1"],
        "Bronspanning is de normpotentiaal van de kathode min die van de anode: \\(0{,}34 - (-0{,}76) = 1{,}10\\) V."),
    tabel(
        "Geldt dit bij een elektrolyse?",
        [
            ("Aan de anode gebeurt een oxidatie.", J),
            ("De anode is de positieve pool.", J),
            ("De elektrolyse levert elektrische energie op.", F),
            ("Aan de kathode worden deeltjes gereduceerd.", J),
        ],
        "Bij een elektrolyse duwt een stroombron een reactie die niet vanzelf verloopt. Ze kost dus elektrische energie. Oxidatie aan de positieve anode, reductie aan de negatieve kathode."),
    mk("Waarom bevestigt men blokken zink aan een stalen scheepsromp?",
       ["Zink is een sterkere reductor en roest in de plaats van het ijzer.", "Zink maakt het zeewater minder zout, zodat het ijzer niet roest.", "Zink is een sterkere oxidator en neemt de elektronen van ijzer op.", "Zink maakt het schip zwaarder, zodat het stabieler in het water ligt."],
       0,
       "Zink staat makkelijker elektronen af dan ijzer. Zolang er zink is, wordt dat geoxideerd en blijft het ijzer gespaard."),

    # Organische reacties en polymeren
    tabel(
        "Tot welk type organische reactie behoort elk voorbeeld?",
        [
            ("methaan reageert met chloor onder licht", "Substitutie"),
            ("etheen reageert met broom", "Additie"),
            ("ethanol wordt etheen en water", "Eliminatie"),
            ("een zuur en een alcohol vormen een ester en water", "Condensatie"),
        ],
        "Bij substitutie wordt een atoom vervangen. Bij additie verdwijnt een dubbele binding en komen er atomen bij. Bij eliminatie ontstaat een dubbele binding en valt er een kleine molecule af. Bij condensatie koppelen twee moleculen met afsplitsing van water.",
        kolommen=["Substitutie", "Additie", "Eliminatie", "Condensatie"]),
    volgorde(
        "Zet de stappen van het radicalaire substitutiemechanisme in de juiste volgorde.",
        ["initiatie: licht splitst \\(\\mathrm{Cl_2}\\) in twee radicalen", "propagatie: radicalen reageren en maken nieuwe radicalen", "terminatie: twee radicalen vormen samen een stabiele molecule"],
        "Eerst ontstaan er radicalen, dan houdt een kettingreactie zichzelf in stand, en ten slotte stopt ze als radicalen met elkaar reageren."),
    sorteer(
        "Is dit een thermoplast of een thermoharder?",
        ["Thermoplast", "Thermoharder"],
        [
            ["wordt zacht bij verwarmen en kan opnieuw gevormd worden", "Thermoplast"],
            ["heeft een sterk vernette structuur", "Thermoharder"],
            ["een PET-fles die je kan omsmelten", "Thermoplast"],
            ["verkoolt bij verwarmen in plaats van te smelten", "Thermoharder"],
        ],
        "Een thermoplast bestaat uit losse ketens die bij verwarming langs elkaar glijden. Een thermoharder is één groot netwerk: verwarmen breekt eerder bindingen dan dat het smelt."),

    # Nano, duurzaam, labo
    mk("Waarom gedragen nanodeeltjes zich vaak anders dan een groot stuk van dezelfde stof?",
       ["Ze hebben een veel groter oppervlak ten opzichte van hun volume.", "Ze bestaan uit andere atomen dan het grote stuk van die stof.", "Ze hebben geen massa meer, omdat ze kleiner zijn dan een atoom.", "Ze verliezen al hun elektronen zodra ze kleiner worden dan een millimeter."],
       0,
       "Hoe kleiner het deeltje, hoe meer atomen aan het oppervlak zitten. Daardoor veranderen eigenschappen zoals reactiviteit, kleur en sterkte."),
    keuze(
        "Een reactie heeft een hoge [[*atoomeconomie|activeringsenergie]] als bijna alle atomen van de reagentia in het gewenste product terechtkomen. Dat past bij [[*duurzame|klassieke]] chemie.",
        "Hoe minder afval, hoe beter. Duurzame chemie probeert reacties zo te kiezen dat zo weinig mogelijk atomen verloren gaan."),
    tabel(
        "Hoeveel beduidende cijfers heeft dit meetresultaat?",
        [
            ("\\(0{,}0045\\) g", "2"),
            ("\\(12{,}0\\) mL", "3"),
            ("\\(4{,}500\\) g", "4"),
        ],
        "Nullen vooraan tellen niet mee, nullen achter de komma op het einde wel: ze zeggen iets over de nauwkeurigheid.",
        kolommen=["2", "3", "4"]),

    # Open vraag
    open_("Ethanol (\\(\\mathrm{CH_3CH_2OH}\\)) en dimethylether (\\(\\mathrm{CH_3OCH_3}\\)) hebben dezelfde brutoformule. Ethanol kookt bij \\(78\\) °C, dimethylether bij \\(-24\\) °C. Verklaar dat verschil.",
          "Beide moleculen zijn functie-isomeren met dezelfde massa. Ethanol heeft een OH-groep: een waterstofatoom aan een sterk elektronegatief zuurstofatoom. Daardoor vormen ethanolmoleculen waterstofbruggen met elkaar. Dimethylether heeft geen H aan O en kan dat niet. Om ethanol te laten koken moet je die sterke waterstofbruggen verbreken, en dat vraagt veel meer energie: het kookpunt is hoger.",
          "Een goed antwoord noemt de waterstofbruggen bij ethanol, legt uit waarom dimethylether ze niet kan vormen en verbindt sterkere intermoleculaire krachten met een hoger kookpunt."),
]
