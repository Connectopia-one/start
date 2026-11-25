# -*- coding: utf-8 -*-
"""Uitdaging Biologie 🌍 Beyond (25 november 2026), in de vormen van het
examen van de Examencommissie: 40 vragen die alle hoofdstukken door elkaar
halen, van de cel en de afweer tot erfelijkheid, genexpressie en evolutie.
Casussen, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde,
rekenvragen, vier klikvragen op twee zelf getekende prenten en een open
vraag. Geen nieuwe leerstof: alles staat in de hoofdstukken van Biologie
Beyond.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_biologie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Biologie"
BESTAND = "beyond-biologie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/biologie-beyond-uitdaging"
CEL = "dierlijke-cel.svg"
STAMBOOM = "stamboom-recessief.svg"
# klikvakken: zie maak_prenten_beyond_biologie.py
MITOCHONDRION = [63.0, 28.2, 21.0, 16.1]
LYSOSOOM = [20.0, 27.4, 10.0, 16.1]
PERSOON = {1: [33.0, 20.2, 10.0, 25.0], 2: [57.0, 20.2, 10.0, 25.0], 4: [45.0, 60.6, 10.0, 25.0]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Een dierlijke cel (prent)
    klik("Bekijk de cel. Klik op het organel waar de eindoxidaties van de celademhaling gebeuren.",
         CEL, [MITOCHONDRION],
         "Organel 2 is een mitochondrion. Op de cristae gebeuren de eindoxidaties, die de meeste ATP opleveren."),
    klik("Klik op het blaasje vol verteringsenzymen dat versleten organellen en opgenomen deeltjes afbreekt.",
         CEL, [LYSOSOOM],
         "Organel 5 is een lysosoom. Het bevat enzymen die stoffen afbreken, bijvoorbeeld een bacterie die door fagocytose binnenkwam."),
    met_prent(CEL, mk(
        "Organel 3 is bezet met kleine bolletjes. Wat is het?",
        ["het glad endoplasmatisch reticulum, dat vetten maakt", "het ruw endoplasmatisch reticulum, met ribosomen", "een stapel mitochondriën", "het cytoskelet van microfilamenten"],
        1,
        "De bolletjes zijn ribosomen. Een netwerk van membranen met ribosomen erop is het ruw ER: daar worden eiwitten gemaakt.")),
    met_prent(CEL, keuze(
        "Organel 4 is het [[*golgiapparaat|chloroplast|kernlichaampje]]. Het [[*verpakt en verstuurt|breekt af|kopieert]] eiwitten in blaasjes.",
        "Het golgiapparaat bewerkt eiwitten uit het ruw ER en stuurt ze in blaasjes naar hun bestemming.")),
    met_prent(CEL, tabel(
        "Klopt dit over deze cel?",
        [
            ("Het DNA ligt in organel 1, gescheiden van het cytoplasma door een kernmembraan.", J),
            ("Deze cel heeft een celwand en chloroplasten.", F),
            ("Een ribosoom is een organel zonder membraan.", J),
        ],
        "Een dierlijke cel heeft geen celwand, geen chloroplasten en geen grote vacuole: dat zijn kenmerken van een plantencel.")),

    # Stamboom (prent)
    klik("Bekijk de stamboom. De aandoening erft autosomaal recessief over. Klik op de persoon die zeker homozygoot recessief is.",
         STAMBOOM, [PERSOON[4]],
         "Een recessief kenmerk zie je enkel bij een homozygoot recessief genotype (aa). Persoon 4 heeft de aandoening."),
    klik("Klik op een persoon die zeker heterozygoot is.",
         STAMBOOM, [PERSOON[1], PERSOON[2]],
         "Persoon 4 is aa en kreeg van elke ouder een a. Ouders 1 en 2 zijn gezond, dus hebben ze ook een A: allebei Aa."),
    met_prent(STAMBOOM, inv(
        "Ouders 1 en 2 krijgen nog een kind. Hoeveel procent kans heeft dat kind op de aandoening? Geef enkel het getal.",
        "25",
        "Aa maal Aa geeft 1 AA, 2 Aa en 1 aa. Eén op vier, dus 25 procent, is aa.")),
    met_prent(STAMBOOM, mk(
        "Hoe groot is de kans dat de gezonde zoon 3 drager (Aa) is?",
        [r"\(\tfrac{1}{4}\)", r"\(\tfrac{1}{2}\)", r"\(\tfrac{2}{3}\)", r"\(\tfrac{3}{4}\)"],
        2,
        "Van de mogelijkheden AA, Aa, Aa en aa valt aa weg, want hij is gezond. Van de drie die overblijven, zijn er twee Aa.")),
    met_prent(STAMBOOM, tabel(
        "Klopt dit over deze familie?",
        [
            ("Een recessief allel kan generaties lang verborgen blijven.", J),
            ("Als 4 een kind krijgt met een AA-partner, heeft dat kind de aandoening.", F),
            ("Het genotype van 5 kan AA of Aa zijn.", J),
        ],
        "aa maal AA geeft enkel Aa: dragers, maar gezond. Een gezond kind van twee dragers kan AA of Aa zijn.")),

    # Casus: een enzymproef
    casus(
        "Jonas wil weten bij welke temperatuur het enzym amylase zetmeel het snelst afbreekt. Hij zet vijf proefbuizen met evenveel zetmeel en amylase in waterbaden van 10, 20, 37, 50 en 70 °C.",
        [
            tabel(
                "Klopt dit over zijn proef?",
                [
                    ("De temperatuur is de variabele die hij zelf instelt.", J),
                    ("Hij zet de temperatuur op de verticale as van zijn grafiek.", F),
                    ("Een buis met zetmeel zonder amylase is een goede controleproef.", J),
                ],
                "De variabele die je zelf instelt, komt op de horizontale as. Een buis zonder enzym toont dat het zetmeel niet vanzelf verdwijnt."),
            mk("Bij 70 °C wordt er bijna geen zetmeel meer afgebroken. Hoe komt dat?",
               ["Het enzym is gedenatureerd door de hitte.", "Het zetmeel is bij die temperatuur verdampt.", "Het enzym werkt sneller, maar het zetmeel is op.", "Amylase werkt enkel bij lage temperaturen."],
               0,
               "Een eiwit verliest bij te hoge temperatuur zijn vorm. Dan past het substraat niet meer in het actief centrum."),
            keuze(
                "Het enzym past enkel op zetmeel. Het is [[*substraatspecifiek|onomkeerbaar|hydrofoob]]. Het splitst zetmeel met water: een [[*hydrolyse|condensatie|fotosynthese]].",
                "Een enzym past als een sleutel op één soort substraat. Splitsen met water heet hydrolyse."),
        ],
    ),

    # Casus: een vaccin
    casus(
        "Sara krijgt een vaccin tegen mazelen. Haar baby is de eerste maanden beschermd door antilichamen die via de placenta en de moedermelk binnenkwamen.",
        [
            tabel(
                "Welke vorm van immunisatie is het?",
                [
                    ("Sara krijgt het vaccin.", "Kunstmatig actief"),
                    ("De baby krijgt antilichamen via de moeder.", "Natuurlijk passief"),
                    ("Sara is ooit zelf ziek geweest van waterpokken.", "Natuurlijk actief"),
                    ("Iemand krijgt na een slangenbeet een spuit met antilichamen.", "Kunstmatig passief"),
                ],
                "Actief: je maakt zelf antilichamen en geheugencellen. Passief: je krijgt ze kant-en-klaar. Kunstmatig gaat via een spuit, natuurlijk vanzelf.",
                kolommen=["Natuurlijk actief", "Kunstmatig actief", "Natuurlijk passief", "Kunstmatig passief"]),
            mk("Waarom is Sara jaren beschermd en haar baby maar enkele maanden?",
               ["Zij maakte zelf geheugencellen, de baby niet.", "Antilichamen van de moeder zijn sterker dan die van een vaccin.", "De baby breekt het vaccin sneller af dan Sara.", "Het vaccin werkt enkel bij volwassenen."],
               0,
               "Na een vaccin blijven er geheugencellen over die snel reageren. Gekregen antilichamen worden na een tijd afgebroken, zonder geheugen."),
            mk("Welke cel maakt de antilichamen na de vaccinatie?",
               ["de plasmacel", "de rode bloedcel", "de dendritische cel", "de bloedplaat"],
               0,
               "Een B-lymfocyt deelt zich en wordt een plasmacel die antilichamen maakt."),
        ],
    ),

    # Casus: bloedgroepen
    casus(
        "Een moeder heeft bloedgroep AB en de vader bloedgroep O.",
        [
            sorteer(
                "Kan een kind van dit koppel deze bloedgroep hebben?",
                ["Kan", "Kan niet"],
                [
                    ["A", "Kan"],
                    ["B", "Kan"],
                    ["AB", "Kan niet"],
                    ["O", "Kan niet"],
                ],
                "De moeder geeft A of B door, de vader altijd O. Een kind is dus AO (bloedgroep A) of BO (bloedgroep B)."),
            keuze(
                "De allelen A en B zijn [[*codominant|recessief]] tegenover elkaar. Iemand met bloedgroep AB is de universele [[*ontvanger|donor]].",
                "Bij AB komen beide antigenen tot uiting: codominantie. AB heeft geen antilichamen tegen A of B en kan dus elk ABO-bloed ontvangen."),
            mk("De moeder is resusnegatief en verwacht een resuspositief kind. Waarom houdt de arts dat in het oog?",
               ["Omdat de moeder anti-D-antilichamen kan aanmaken.", "Omdat het kind dan zeker bloedgroep O krijgt.", "Omdat de bloedgroep van de moeder tijdens de zwangerschap verandert.", "Omdat resuspositief bloed niet door de placenta kan."],
               0,
               "Komt resuspositief bloed van het kind in het bloed van de moeder, dan kan ze anti-D-antilichamen maken. Bij een volgende zwangerschap kunnen die het kind schaden."),
        ],
    ),

    # Casus: van gen tot eiwit
    casus(
        "Een stukje van de matrijsstreng van een gen leest: 3'-TAC GGA AAT-5'.",
        [
            inv("Welke drie basen vormen het eerste codon op het mRNA? Typ ze zonder spaties, bijvoorbeeld GCU.",
                ["AUG", "aug"],
                "Het mRNA is complementair aan de matrijs, met U in plaats van T: TAC wordt AUG. Dat is meteen het startcodon."),
            inv("Welk anticodon past op het tweede codon van dat mRNA? Typ de drie basen zonder spaties.",
                ["GGA", "gga"],
                "GGA op de matrijs wordt CCU op het mRNA. Het anticodon van het tRNA is daar weer complementair aan: GGA."),
            volgorde(
                "Zet de stappen van gen tot eiwit in de juiste volgorde bij een eukaryote cel.",
                ["transcriptie in de kern", "introns uitknippen uit het pre-mRNA", "het mRNA verlaat de kern", "translatie op het ribosoom", "posttranslationele modificatie"],
                "Het DNA blijft in de kern. Het rijpe mRNA gaat naar het ribosoom, waar het eiwit gemaakt wordt en daarna nog bewerkt."),
        ],
    ),

    # Casus: resistente bacteriën
    casus(
        "In een ziekenhuis krijgt een patiënt antibiotica, maar hij stopt de kuur te vroeg. Een paar weken later is de infectie terug, en nu helpt hetzelfde middel niet meer.",
        [
            volgorde(
                "Zet de stappen van deze selectie in de juiste volgorde.",
                ["Door een mutatie is één bacterie toevallig resistent.", "Het antibioticum doodt de gevoelige bacteriën.", "De resistente bacterie overleeft en deelt zich.", "Bijna alle bacteriën in de nieuwe infectie zijn resistent."],
                "De resistentie bestond al voor het middel kwam. Het antibioticum selecteert: wie het overleeft, vermeerdert zich."),
            tabel(
                "Darwin of Lamarck?",
                [
                    ("Bacteriën worden resistent omdat ze het antibioticum moeten verdragen.", "Lamarck"),
                    ("Toevallig resistente bacteriën overleven en krijgen meer nakomelingen.", "Darwin"),
                    ("Wat een organisme gebruikt, groeit, en dat geeft het door.", "Lamarck"),
                ],
                "Darwin legt het uit met variatie en natuurlijke selectie. Lamarck dacht dat verworven kenmerken doorgegeven worden.",
                kolommen=["Darwin", "Lamarck"]),
            mk("Hoe kan die resistentie snel naar andere soorten bacteriën overspringen?",
               ["via plasmiden die bacteriën doorgeven", "via de rode bloedcellen van de patiënt", "via de mitochondriën van de patiënt", "via het kernmembraan van de bacterie"],
               0,
               "Bacteriën kunnen plasmiden met resistentiegenen aan elkaar doorgeven. Een bacterie heeft overigens geen kernmembraan."),
        ],
    ),

    # Losse vragen door elkaar
    volgorde(
        "Zet de fasen van de mitose in de juiste volgorde.",
        ["profase", "metafase", "anafase", "telofase"],
        "In de profase worden de chromosomen zichtbaar, in de metafase liggen ze in het evenaarsvlak, in de anafase gaan de chromatiden uit elkaar en in de telofase ontstaan twee kernen."),
    sorteer(
        "Hoort dit bij de mitose of bij de meiose?",
        ["Mitose", "Meiose"],
        [
            ["levert twee erfelijk gelijke dochtercellen", "Mitose"],
            ["levert vier haploïde cellen", "Meiose"],
            ["homologe chromosomen wisselen stukken uit in een chiasma", "Meiose"],
            ["zorgt voor groei en herstel van weefsel", "Mitose"],
            ["maakt geslachtscellen", "Meiose"],
        ],
        "De mitose kopieert: groei en herstel. De meiose halveert het aantal chromosomen en mengt de allelen: geslachtscellen."),
    mk("Je legt rode bloedcellen in zuiver water. Wat gebeurt er?",
       ["Ze verschrompelen, want water stroomt naar buiten.", "Er gebeurt niets, want het membraan laat geen water door.", "Ze zwellen op en barsten door osmose.", "Ze delen zich sneller door de extra ruimte."],
       2,
       "Zuiver water is hypotoon tegenover de cel. Water stroomt door osmose naar binnen tot de cel barst: hemolyse."),
    keuze(
        "De fotosynthese gebeurt in de [[*chloroplast|mitochondrion|kern]]. De glycolyse van de celademhaling gebeurt in het [[*cytoplasma|kernmembraan|lysosoom]].",
        "De glycolyse gebeurt in het cytoplasma. Daarna gaat het pyruvaat het mitochondrion in voor de verdere afbraak."),
    koppel(
        "Uit welke bouwstenen bestaat elk biomolecule?",
        [
            ["zetmeel", "glucose"],
            ["een eiwit", "aminozuren"],
            ["een vet", "glycerol en vetzuren"],
            ["DNA", "nucleotiden"],
        ],
        ["fructose en galactose", "ribosomen"],
        "Zetmeel is een ketting van glucose. Eiwitten zijn ketens van aminozuren. Een vet bestaat uit glycerol met vetzuren. DNA is een keten van nucleotiden."),
    tabel(
        "Welk gevolg heeft deze mutatie meestal?",
        [
            ("een substitutie die een codon geeft voor hetzelfde aminozuur", "Geen verschil in het eiwit"),
            ("een insertie van één base midden in een gen", "Groot verschil in het eiwit"),
            ("een deletie van één base vlak na het startcodon", "Groot verschil in het eiwit"),
        ],
        "Eén base erbij of eraf verschuift het leesraam: alle codons erna veranderen. Een substitutie kan stil blijven, omdat meerdere codons voor hetzelfde aminozuur coderen.",
        kolommen=["Geen verschil in het eiwit", "Groot verschil in het eiwit"]),
    mk("Waarvoor gebruikt een labo een PCR?",
       ["om DNA veel keren te kopiëren", "om DNA in stukken te knippen", "om eiwitten te scheiden in een gel", "om een bacterie te doden"],
       0,
       "Met een PCR maak je van een klein beetje DNA genoeg kopieën om het te onderzoeken, bijvoorbeeld voor een DNA-profiel."),
    mk("Een ziekte doodt bijna alle dieren van een populatie. De overlevers zijn toevallig allemaal erg verwant. Hoe heet dit?",
       ["gene flow", "een flessenhalseffect", "kunstmatige selectie door de mens", "convergente evolutie"],
       1,
       "De populatie krimpt sterk en verliest veel genetische variatie: een flessenhalseffect."),
    tabel(
        "Welke soort isolatie houdt deze soorten gescheiden?",
        [
            ("Twee soorten vogels hebben een ander baltsgedrag.", "Prezygotisch"),
            ("Een paard en een ezel krijgen een onvruchtbare muilezel.", "Postzygotisch"),
            ("Twee soorten bloeien in een andere maand.", "Prezygotisch"),
        ],
        "Prezygotische isolatie werkt voor er een zygote is. Postzygotisch: er ontstaat wel een zygote, maar de nakomeling is zwak of onvruchtbaar.",
        kolommen=["Prezygotisch", "Postzygotisch"]),
    sleep(
        "Na de bevruchting in de eileider ontstaat een [[zygote]]. Na enkele klievingsdelingen is dat een compact bolletje cellen, de [[morula]]. Daarna vormt zich een holle [[blastocyst]], die zich in het baarmoederslijmvlies [[innestelt]].",
        ["gastrula", "placenta"],
        "Zygote, morula, blastocyst en innesteling volgen elkaar op in de eerste week na de bevruchting."),
    keuze(
        "Een hoge concentratie oestrogeen en progesteron [[*remt|stimuleert]] de afgifte van FSH en LH. Dat is [[*negatieve|positieve]] feedback.",
        "Het product remt zijn eigen aanmaak. Op die manier werkt ook de combinatiepil."),
    mk("Eeneiige tweelingen hebben hetzelfde DNA, maar op latere leeftijd verschillen ze soms toch. Hoe kan dat?",
       ["Hun DNA wordt met de jaren van elkaar verschillend door epigenetische veranderingen.", "Door verschillen in leefstijl en omgeving gaan andere genen aan of uit.", "Eén van hen krijgt na de geboorte een ander genoom.", "Eeneiige tweelingen hebben eigenlijk ander DNA."],
       1,
       "Methylering en andere epigenetische veranderingen zetten genen aan of uit zonder de basenvolgorde te veranderen. Leefstijl en omgeving spelen daarin mee: nature en nurture samen."),
    inv("Hoeveel chromosomen zitten er in een menselijke zaadcel? Geef enkel het getal.",
        "23",
        "Een lichaamscel is diploïd, met 46 chromosomen. Een geslachtscel is haploïd: de helft, dus 23."),
    tabel(
        "Klopt dit over de afweer?",
        [
            ("Koorts helpt de afweer en remt de indringer.", J),
            ("Lysozym in tranen breekt de celwand van bacteriën af.", J),
            ("Alle bloedcellen worden in het beenmerg aangemaakt.", J),
            ("Antibiotica helpen goed tegen een griepvirus.", F),
        ],
        "Antibiotica werken tegen bacteriën, niet tegen virussen."),
    open_("Een bedrijf wil met gene editing een gewas maken dat beter tegen droogte kan. Geef één argument voor en één argument tegen.",
          "Voor: in droge streken kan zo'n gewas de oogst redden en honger voorkomen. Tegen: we weten nog niet goed wat het op lange termijn doet met andere soorten en de biodiversiteit.",
          "Een goed antwoord geeft een echt argument aan beide kanten en blijft bij de feiten."),
]
