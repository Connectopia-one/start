"""Van DNA naar eiwit: genexpressie — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Enkele pittige vragen biologie Beyond over de bouw van DNA (zelfde prent), verder eigen vragen binnen nwd_genexpressie."""
from ..beyond_bio_themas import dna as D
from ..beyond_bio_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 1, 2, 6, 7, 9, 10]) + [
    casus(
        "Bij een tweeling die bij de geboorte gescheiden werd, groeit Lars op in Noorwegen en Tom in Spanje. Ze hebben exact hetzelfde DNA. "
        "Als volwassenen hebben ze dezelfde oogkleur en dezelfde bloedgroep. Tom is wel veel bruiner en iets langer: hij at als kind meer en gevarieerder.",
        [
            keuze("Lars en Tom hebben [[*hetzelfde genotype|een ander genotype]].", "Hetzelfde DNA."),
            keuze("Dat Tom bruiner is, komt vooral door [[*de omgeving|zijn genen]].", "Meer zon."),
            keuze("Bloedgroep en oogkleur horen bij het [[*fenotype|genotype alleen]], want je kan ze waarnemen of meten.", "Wat je ziet of meet is het fenotype."),
            mk("Wat toont het lengteverschil tussen de twee?",
               ["Het fenotype hangt van genen én omgeving af.", "Tom heeft andere genen voor lengte gekregen.",
                "Lengte is helemaal niet erfelijk bij de mens.", "Het genotype verandert als je meer eet."], 0,
               "Hetzelfde genotype, toch een ander fenotype."),
            keuze("Als Tom zijn zongebruinde huid zou doorgeven aan zijn kinderen, dan zou dat [[*niet kunnen|altijd gebeuren]].",
                  "Wat niet in het DNA van de geslachtscellen staat, is niet erfelijk."),
        ],
    ),
    inv("Een DNA-streng leest A T G C C A. Geef de basen van de tegenoverliggende streng, zonder spaties.", ["TACGGT"],
        "A tegenover T, C tegenover G."),
    inv("Van een gen wordt een mRNA-kopie gemaakt. Het stukje DNA dat afgelezen wordt, leest T A C G. Welke basen krijgt het mRNA? Schrijf zonder spaties.", ["AUGC"],
        "Tegenover A staat in RNA U, en niet T."),
    sorteer("Gebeurt dit in de celkern of aan het ribosoom?", ["in de celkern", "aan het ribosoom"], [
        ["het gen wordt afgelezen", "in de celkern"], ["aminozuren worden aan elkaar gekoppeld", "aan het ribosoom"],
        ["er wordt een mRNA-kopie gemaakt", "in de celkern"], ["het eiwit wordt in elkaar gezet", "aan het ribosoom"],
    ], "Het DNA blijft in de kern; het eiwit wordt aan het ribosoom gemaakt."),
    volgorde("Zet de stappen van gen tot eiwit in de juiste volgorde.", [
        "het gen wordt in de kern afgelezen", "er ontstaat een mRNA-kopie", "het mRNA verlaat de kern",
        "het ribosoom koppelt aminozuren aan elkaar", "het eiwit doet zijn werk in de cel",
    ], "Van DNA via mRNA naar eiwit."),
    koppel("Koppel elk begrip aan zijn betekenis.", [
        ["gen", "stuk DNA met de code voor één eigenschap"], ["allel", "één versie van een gen"],
        ["genotype", "het geheel van het erfelijk materiaal"], ["fenotype", "wat je kan waarnemen of meten"],
    ], ["een bouwsteen van een eiwit"], "Een aminozuur is een bouwsteen van een eiwit."),
    tabel("Klopt dit over DNA en RNA?", [
        ("DNA bevat desoxyribose, RNA bevat ribose.", J), ("RNA bestaat uit twee strengen.", F),
        ("In RNA staat uracil in plaats van thymine.", J), ("Het mRNA brengt de code naar het ribosoom.", J),
    ], "RNA heeft maar één streng."),
    tabel("Erfelijk of niet erfelijk?", [
        ("je bloedgroep", "erfelijk"), ("een litteken van een val", "niet erfelijk"),
        ("mucoviscidose", "erfelijk"), ("gespierde benen door veel te fietsen", "niet erfelijk"),
    ], "Enkel wat in het DNA van de geslachtscellen staat, is erfelijk.", kolommen=["erfelijk", "niet erfelijk"]),
    tabel("Veredeling of genetische modificatie?", [
        ("twee rassen kruisen en de beste nakomelingen kiezen", "veredeling"),
        ("een menselijk gen in een bacterie brengen", "genetische modificatie"),
        ("koeien met veel melk laten paren", "veredeling"),
        ("een gen van een vis in een tomaat zetten", "genetische modificatie"),
    ], "Veredeling werkt met gewone voortplanting; bij modificatie verandert men het DNA zelf.",
        kolommen=["veredeling", "genetische modificatie"]),
    mk("Een spiercel en een huidcel van dezelfde persoon zien er heel anders uit. Waarom?",
       ["In elke cel staan andere genen aan.", "Ze hebben een ander DNA in hun kern.", "De spiercel heeft meer chromosomen dan de huidcel.", "De huidcel heeft geen genen meer."], 0,
       "Hetzelfde DNA, andere genen aan."),
    mk("Een mutatie verandert de volgorde van de basen in een gen. Waarom kan het eiwit dan anders worden?",
       ["De volgorde van de aminozuren kan veranderen.", "Het eiwit krijgt dan veel meer suikers erbij.", "Het ribosoom gaat dan in de celkern zitten.", "Het mRNA wordt dan dubbelstrengig, zoals DNA."], 0,
       "De basenvolgorde bepaalt de volgorde van de aminozuren, en die bepaalt de vorm van het eiwit."),
    mk("Hoe maakt men met recombinant DNA-technologie menselijke insuline?",
       ["Men brengt het menselijke insulinegen in een bacterie.", "Men kruist bacteriën met cellen van de alvleesklier.",
        "Men geeft bacteriën insuline te eten tot ze het namaken.", "Men haalt het insuline uit de bloedcellen van een donor."], 0,
       "De bacterie leest het gen af en maakt het eiwit."),
    inv("Hoe noem je de vorm van het DNA-molecule? Twee woorden.", ["dubbele helix"], "Twee strengen die om elkaar draaien."),
    keuze("Het DNA [[*blijft in de celkern|reist zelf naar het ribosoom]].", "Er gaat enkel een mRNA-kopie naar buiten."),
    keuze("Een eiwit is een keten van [[*aminozuren|basen]] in een vaste volgorde.", "Aminozuren zijn de bouwstenen."),
    keuze("Het gen voor oogkleur kan bij twee mensen een ander [[*allel|chromosoom]] hebben.", "Allelen zijn versies van een gen."),
    keuze("Een organisme waarvan het DNA bewust veranderd is, noem je een [[*GGO|hybride]].", "Genetisch gemodificeerd organisme."),
    sleep("In de [[celkern]] wordt een gen afgelezen tot [[mRNA]]. Aan het [[ribosoom]] worden de aminozuren aan elkaar gezet.",
          ["mitochondrion", "tRNA-kern"], "Van DNA naar eiwit."),
    open_("Leg uit waarom twee planten met hetzelfde genotype toch een verschillend fenotype kunnen hebben.",
          "Het fenotype hangt ook van de omgeving af: licht, water en voeding verschillen, en zo groeit de ene plant groter dan de andere.",
          "Genen én omgeving bepalen het fenotype."),
]
