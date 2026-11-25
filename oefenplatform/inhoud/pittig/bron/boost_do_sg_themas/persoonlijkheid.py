"""Persoonlijkheid, karakter en temperament — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_persoonlijkheid: identiteit, karakter en
temperament, nature, nurture en zelfbepaling, de categorieën van identiteit,
de big five en de vier temperamenten van Galenus. Met een zelfgetekend
profiel."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ROOD

BF = Prent("profiel-big-five", "Het profiel van Lore op vijf schalen", "vijf schalen met twee uitersten en een stip, letters A tot E")
SCHAAL = [("A", "introversie", "extraversie", 0.85), ("B", "afstandelijkheid", "vriendelijkheid", 0.7),
          ("C", "emotionele stabiliteit", "neuroticisme", 0.8), ("D", "onzorgvuldigheid", "zorgvuldigheid", 0.25),
          ("E", "geslotenheid", "openheid", 0.9)]
for i, (t, links, rechts, pos) in enumerate(SCHAAL):
    y = 110 + i * 100
    BF.lijn(300, y, 760, y, DONKER, 4)
    for k in range(6):
        BF.lijn(300 + k * 92, y - 8, 300 + k * 92, y + 8, DONKER, 2)
    BF.tekst(285, y + 7, links, 20, "end"); BF.tekst(775, y + 7, rechts, 20, "start")
    BF.cirkel(300 + pos * 460, y, 14, ROOD, DONKER, 2)
    BF.letter(32, y, t)
U = "profiel-big-five.svg"
Z = {t: [Prent.zone(20, 70 + i * 100, 960, 80)] for i, (t, a, b, c) in enumerate(SCHAAL)}

BAS = ("Lees de voorstelling.\n\n"
       "« Ik ben Bas, zestien jaar, de jongste van vier. Ik woon in Genk en spreek thuis Nederlands en Turks. "
       "Ik speel graag schaak, want ik denk lang na voor ik iets doe. Mijn mama zegt dat ik als baby al een rustig kind was dat zelden huilde. »")

VRAGEN = [
    klik("Bekijk het profiel van Lore. Lore maakt zich snel zorgen. Klik op de schaal die dat toont.", U, Z["C"], "Neuroticisme tegenover emotionele stabiliteit."),
    klik("Lore komt vaak te laat en werkt haar taken zelden af. Klik op de schaal die dat toont.", U, Z["D"], "Zorgvuldigheid: plannen, afwerken, op tijd komen."),
    klik("Lore zoekt graag gezelschap en praat makkelijk met vreemden. Klik op de schaal die dat toont.", U, Z["A"], "Extraversie."),
    klik("Lore probeert graag nieuwe dingen en is nieuwsgierig naar andere ideeën. Klik op de schaal die dat toont.", U, Z["E"], "Openheid tegenover geslotenheid."),
    casus(BAS, [
        sorteer("Welke categorie van identiteit?", ["relationele identiteit", "culturele identiteit", "persoonlijke identiteit"],
                [("de jongste van vier", "relationele identiteit"), ("spreekt thuis Nederlands en Turks", "culturele identiteit"), ("denkt lang na voor hij iets doet", "persoonlijke identiteit")],
                "Je plaats tegenover anderen, je taal en gewoontes, wat jou eigen maakt."),
        keuze("Dat Bas als baby al rustig was, zegt vooral iets over zijn [[*temperament|karakter|sociale identiteit]].", "De aangeboren grondtoon."),
        keuze("Van de vier temperamenten van Galenus past de rustige baby het best bij het [[*flegmatische|cholerische|sanguinische]] temperament.", "Kalm en moeilijk uit zijn lood te slaan."),
        mk("Bas is zestien. Waarom staat zijn identiteit nu sterk op het spel?",
           ["hij zit in de adolescentie", "omdat hij in Genk woont en niet in een andere stad", "omdat zijn temperament op die leeftijd verdwijnt", "omdat de jongste van vier geen identiteit heeft"],
           0, "Identiteit versus identiteitsverwarring, zei Erikson."),
    ]),
    koppel("Koppel het temperament van Galenus aan de beschrijving.",
           [("sanguinisch", "vrolijk, spontaan en snel enthousiast"), ("cholerisch", "fel, gedreven en snel kwaad"), ("flegmatisch", "kalm, traag op gang en volhardend"), ("melancholisch", "ernstig, gevoelig en diep nadenkend")],
           ["altijd honger en moe"], "Vier temperamenten uit de oude geneeskunde."),
    sorteer("Identiteit, karakter of temperament?", ["identiteit", "karakter", "temperament"],
            [("'Ik ben een Limburger en een voetbalster.'", "identiteit"), ("Ze werkt haar taken altijd zorgvuldig af.", "karakter"), ("Als baby was hij al snel van streek.", "temperament"), ("'Ik ben de oudste dochter.'", "identiteit")],
            "Wie je bent, hoe je doet, en de aangeboren grondtoon."),
    tabel("Klopt dit over persoonlijkheid?",
          [("De persoonlijkheid ligt volledig vast bij de geboorte.", F), ("Persoonlijkheid is grotendeels stabiel.", J), ("Je kan meer dan één sociale identiteit tegelijk hebben.", J), ("Persoonlijkheid en gedrag zijn hetzelfde.", F)],
          "Gedrag is één moment; persoonlijkheid is het patroon erachter."),
    mk("Een baby is van bij de geboorte prikkelbaar. Als tiener leert hij geduldig te zijn. Wat toont dat over temperament en karakter?",
       ["het ene is aangeboren, het andere groeit", "dat temperament alleen bij kinderen en karakter bij volwassenen hoort", "dat zijn temperament volledig verdwenen is", "dat temperament en karakter precies hetzelfde zijn"],
       0, "Temperament is de aanleg waarmee je begint."),
    keuze("Iemand noemt zichzelf moslim. Geloof hoort bij de [[*culturele|relationele|persoonlijke]] identiteit.", "Samen met taal, gewoontes en tradities."),
    keuze("Een introvert persoon is [[*niet per se verlegen|altijd verlegen|nooit graag alleen]]: hij haalt vooral energie uit rust.", "Extraversie en introversie zijn twee uitersten van één schaal."),
    tabel("Hoort deze trek bij de big five?",
          [("extraversie", J), ("vriendelijkheid", J), ("cholerisch", F), ("zorgvuldigheid", J), ("openheid", J)],
          "Cholerisch is een temperament van Galenus."),
    mk("Op het werk is Noah stil, thuis is hij een lolbroek. Wat leert dat over een persoonlijkheidstest?",
       ["gedrag hangt ook van de situatie af", "dat Noah eigenlijk geen persoonlijkheid heeft", "dat een test altijd juist is, wat hij ook doet", "dat zijn temperament elke dag verandert"],
       0, "Dezelfde persoon doet anders op het werk dan thuis."),
    sleep("Persoonlijkheid bestaat uit [[identiteit]], [[karakter]] en [[temperament]].",
          ["intelligentie", "lengte"], "Drie elementen."),
    keuze("Een tweeling wordt apart opgevoed en krijgt toch dezelfde hobby. Dat wijst op het gewicht van [[*nature|nurture|zelfbepaling]].", "Verschillende omgeving en toch hetzelfde."),
    keuze("De vier temperamenten van Galenus zijn [[*een oud model, niet wetenschappelijk bewezen|vandaag wetenschappelijk bewezen|een onderdeel van de big five]].", "Een model uit de geneeskunde van de lichaamssappen."),
    tabel("Is dit een categorie van identiteit?",
          [("persoonlijke identiteit", J), ("genderidentiteit", J), ("motorische identiteit", F), ("relationele identiteit", J)],
          "Identiteit groeit in contact met anderen."),
    mk("Twee zussen uit hetzelfde gezin hebben een heel ander karakter. Hoe kan dat?",
       ["aanleg en ervaring verschillen", "omdat ze een ander temperament kozen", "omdat karakter enkel uit de genen komt", "omdat ze in een andere levensloopfase geboren zijn"],
       0, "Zelfs binnen één gezin krijgt elk kind andere ervaringen."),
    keuze("De persoonlijke identiteit [[*onderscheidt|verbindt]] je van anderen; de sociale identiteit verbindt je met een groep.", "Wat jou anders maakt tegenover waar je bij hoort."),
    inv("Hoeveel trekken telt het big five model? Schrijf het getal.", ["5", "vijf"], "Elk met twee uitersten."),
    keuze("De persoonlijkheid van een peuter is nog moeilijk te beschrijven, want ze is nog [[*volop in ontwikkeling|volledig af|onzichtbaar]].", "Het temperament is wel al zichtbaar."),
    tabel("Klopt dit over zelfbepaling?",
          [("Je maakt zelf keuzes.", J), ("Je kiest binnen je mogelijkheden.", J), ("Zelfbepaling maakt nature en nurture overbodig.", F)],
          "Ze staat naast nature en nurture."),
    keuze("Iemand is fel, gedreven en heeft een kort lontje. Dat past bij het [[*cholerische|melancholische|flegmatische]] temperament.", "Veel energie en snel kwaad."),
    tabel("Welke uitersten horen samen op één schaal van de big five?",
          [("extraversie en introversie", J), ("openheid en geslotenheid", J), ("zorgvuldigheid en vriendelijkheid", F), ("neuroticisme en emotionele stabiliteit", J)],
          "Elke trek heeft zijn eigen tegenpool."),
    keuze("'Ik ben dochter, student, Limburger en voetbalster.' Iemand kan [[*meerdere sociale identiteiten|maar één sociale identiteit]] tegelijk hebben.", "Ze botsen soms."),
    mk("Een vriend die je tien jaar niet zag, is nog altijd even zorgvuldig en grappig. Welk kenmerk van persoonlijkheid zie je?",
       ["ze is stabiel", "ze verandert elke dag een beetje opnieuw", "ze is bij iedereen precies dezelfde", "ze ligt al voor de geboorte volledig vast"],
       0, "Grote gebeurtenissen kunnen iemand wel doen veranderen."),
    open_("Beschrijf jezelf of een verzonnen persoon met één voorbeeld van identiteit, één karaktertrek en één temperament.",
          "Bijvoorbeeld: Lien is de oudste van drie (relationele identiteit). Ze is zorgvuldig: ze plant haar taken en werkt alles af (karakter). Als baby was ze al levendig en snel enthousiast, wat past bij een sanguinisch temperament."),
]
