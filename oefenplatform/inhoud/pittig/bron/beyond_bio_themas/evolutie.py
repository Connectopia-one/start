"""Argumenten voor evolutie en de evolutietheorieën — pittig (🧬 Beyond doorstroom, biologie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Homologe voorpoten -------------------------------------------------------
HV = Prent("voorpoten-homoloog", "De voorpoot van drie zoogdieren (schematisch)", "arm van een mens, vleugel van een vleermuis en vin van een walvis; telkens dezelfde beenderen in dezelfde kleur")
OPP, ONDER, POLS, VING = "#e8a0b0", "#8fc1e3", "#f2c14e", "#9fd39a"


def _been(p, x1, y1, x2, y2, kl, dik=14):
    p.svg(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{DONKER}" stroke-width="{dik + 4}" stroke-linecap="round"/>')
    p.svg(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{kl}" stroke-width="{dik}" stroke-linecap="round"/>')


# mens
_been(HV, 170, 120, 170, 250, OPP, 18)
_been(HV, 160, 265, 150, 380, ONDER, 10)
_been(HV, 182, 265, 192, 380, ONDER, 10)
HV.rect(140, 392, 64, 28, POLS, DONKER, 6, 2)
for dx in (-26, -10, 6, 22, 38):
    _been(HV, 172 + dx * 0.6, 425, 172 + dx * 1.3, 500 if dx != -26 else 465, VING, 7)
HV.tekst(170, 560, "mens", 18, vet=True)
# vleermuis
HV.pad("M505 258 L 430 470 L 520 480 L 610 470 L 680 420 L 720 330 L 560 250 Z", "#efe6f5", DONKER, 1.5)
_been(HV, 440, 170, 500, 250, OPP, 14)
_been(HV, 505, 258, 545, 320, ONDER, 8)
_been(HV, 560, 250, 552, 322, ONDER, 8)
HV.rect(535, 325, 36, 22, POLS, DONKER, 5, 2)
for x2, y2 in ((430, 470), (520, 480), (610, 470), (680, 420), (720, 330)):
    _been(HV, 553, 350, x2, y2, VING, 6)
HV.tekst(560, 560, "vleermuis", 18, vet=True)
# walvis
HV.pad("M800 160 C 760 260 760 420 840 520 C 920 420 920 260 880 160 Z", "#dde6ee", DONKER, 2)
_been(HV, 840, 175, 840, 225, OPP, 22)
_been(HV, 828, 240, 826, 300, ONDER, 12)
_been(HV, 852, 240, 856, 300, ONDER, 12)
HV.rect(815, 310, 50, 26, POLS, DONKER, 6, 2)
for dx, lang in ((-20, 120), (-7, 170), (7, 170), (20, 120)):
    _been(HV, 840 + dx, 345, 840 + dx * 1.6, 345 + lang, VING, 7)
HV.tekst(840, 560, "walvis", 18, vet=True)
ZHV = {"opp_vleermuis": [Prent.zone(425, 160, 90, 100)], "ving_walvis": [Prent.zone(790, 340, 100, 180)],
       "onder_mens": [Prent.zone(135, 255, 75, 130)]}

# Gesteentelagen -----------------------------------------------------------
GL = Prent("gesteentelagen", "Gesteentelagen in een rotswand", "vijf horizontale lagen P (bovenaan) tot T (onderaan), met in elke laag een fossiel")
KLL = ["#f4e3c0", "#e6cfa0", "#d8bb85", "#c9a76c", "#b79358"]
for i, kl in enumerate(KLL):
    GL.rect(150, 100 + i * 90, 700, 90, kl, DONKER, 0, 1.5)
# fossielen: P zoogdiertand, Q vogel, R dinosaurus-voetafdruk, S vis, T trilobiet
GL.svg(f'<path d="M500 125 L 515 170 L 485 170 Z" fill="#fff" stroke="{DONKER}" stroke-width="2"/>')
GL.pad("M470 255 C 500 225 540 225 560 250 L 600 235 L 580 260 C 540 285 500 285 470 255 Z", "#fff", DONKER, 2)
for dx, dy in ((0, 0), (-18, -20), (0, -26), (18, -20)):
    GL.ellips(520 + dx, 350 + dy, 8 if (dx, dy) != (0, 0) else 14, 12, "#fff", DONKER, 2)
GL.pad("M460 420 C 490 395 550 395 575 420 L 605 400 L 605 440 L 575 420 C 550 445 490 445 460 420 Z", "#fff", DONKER, 2)
GL.ellips(520, 505, 40, 26, "#fff", DONKER, 2)
for k in range(-2, 3):
    GL.lijn(485, 505 + k * 9, 555, 505 + k * 9, DONKER, 1)
for i, k in enumerate("PQRST"):
    GL.letter(100, 145 + i * 90, k)
ZGL = {k: [Prent.zone(150, 100 + i * 90, 700, 90), Prent.rond(100, 145 + i * 90, 22)] for i, k in enumerate("PQRST")}

VRAGEN = [
    klik(
        "Klik op het bot in de vleermuisvleugel dat overeenkomt met ons opperarmbeen.",
        HV.bestand, ZHV["opp_vleermuis"],
        "Hetzelfde bot, in dezelfde kleur: dat maakt de voorpoten homoloog.",
    ),
    klik(
        "Klik op de vingerbeentjes van de walvis.",
        HV.bestand, ZHV["ving_walvis"],
        "Een walvisvin bevat dezelfde beenderen als onze hand, maar in een andere vorm.",
    ),
    met_prent(HV.bestand, tabel(
        "Kijk naar de drie voorpoten. Klopt dit?",
        [
            ("Ze hebben dezelfde bouw.", J),
            ("Ze hebben een verschillende functie.", J),
            ("Het zijn homologe organen.", J),
            ("Ze wijzen erop dat de drie dieren niet verwant zijn.", F),
        ],
        "Dezelfde bouw wijst op een gemeenschappelijke voorouder.",
    )),
    klik(
        "Klik op de laag met de oudste fossielen.",
        GL.bestand, ZGL["T"],
        "De lagen stapelen zich op: de onderste is de oudste.",
    ),
    met_prent(GL.bestand, tabel(
        "Kijk naar de gesteentelagen. Klopt dit?",
        [
            ("Het fossiel in S is ouder dan dat in Q.", J),
            ("Laag P is het laatst afgezet.", J),
            ("Het fossiel in R is jonger dan dat in T.", J),
            ("Het fossiel in P is het oudste.", F),
        ],
        "Hoe dieper, hoe ouder, zolang de lagen niet omgekeerd zijn.",
    )),
    tabel(
        "Homoloog of analoog?",
        [
            ("vleugel van een vogel en arm van een mens", "Homoloog"),
            ("vleugel van een insect en vleugel van een vogel", "Analoog"),
            ("voorpoot van een hond en vin van een walvis", "Homoloog"),
            ("vin van een haai en vin van een dolfijn", "Analoog"),
        ],
        "Analoog: zelfde functie, andere bouw. Homoloog: zelfde bouw.",
        kolommen=["Homoloog", "Analoog"],
    ),
    sorteer(
        "Uit welk vakgebied komt dit argument voor evolutie?",
        ["Anatomie", "Paleontologie", "Moleculaire biologie"],
        [
            ("rudimentaire organen", "Anatomie"),
            ("een continue reeks fossielen bij paardachtigen", "Paleontologie"),
            ("de universele genetische code", "Moleculaire biologie"),
            ("Archaeopteryx", "Paleontologie"),
            ("cytochroom c vergelijken", "Moleculaire biologie"),
            ("homologe organen", "Anatomie"),
        ],
        "Paleontologie bestudeert fossielen.",
    ),
    tabel(
        "Hoeveel aminozuren van cytochroom c verschillen met die van de mens? Welke soort is dan het nauwst verwant?",
        [
            ("chimpansee: 0 verschillen", "Nauwst"),
            ("hond: 11 verschillen", "Middel"),
            ("gist: 44 verschillen", "Verst"),
            ("paard: 12 verschillen", "Middel"),
        ],
        "Hoe minder verschillen, hoe recenter de gemeenschappelijke voorouder.",
        kolommen=["Nauwst", "Middel", "Verst"],
    ),
    mk(
        "Waarom is Archaeopteryx een sterk argument voor evolutie?",
        [
            "Hij heeft kenmerken van reptielen én van vogels",
            "Hij is het oudste fossiel dat ooit gevonden werd",
            "Hij leeft vandaag nog op enkele eilanden",
            "Hij is de rechtstreekse voorouder van de mens",
        ],
        0,
        "Veren zoals een vogel, maar tanden en een benige staart zoals een reptiel.",
    ),
    koppel(
        "Koppel elke wetenschapper of gedachte aan wat erbij hoort.",
        [
            ("Lamarck", "erfelijkheid van verworven eigenschappen"),
            ("Darwin", "natuurlijke selectie"),
            ("moderne evolutietheorie", "mutaties en allelfrequenties"),
        ],
        ["elk dier is apart en onveranderlijk geschapen", "evolutie binnen één leven"],
        "Darwin kende de genen nog niet. De moderne theorie voegde de genetica toe.",
    ),
    tabel(
        "Lamarck of Darwin?",
        [
            ("de giraffe rekt zijn nek en geeft die langere nek door", "Lamarck"),
            ("giraffen met een langere nek krijgen meer jongen", "Darwin"),
            ("wat een dier veel gebruikt, groeit en wordt doorgegeven", "Lamarck"),
            ("er worden meer jongen geboren dan er kunnen overleven", "Darwin"),
        ],
        "Bij Darwin bestaat de variatie al voor de selectie.",
        kolommen=["Lamarck", "Darwin"],
    ),
    casus(
        "Een ziekenhuis behandelt een infectie met een antibioticum. Na een paar weken werkt het middel niet meer.",
        [
            mk(
                "Hoe verklaart de moderne evolutietheorie dit?",
                [
                    "Enkele bacteriën waren al resistent en overleefden",
                    "Het antibioticum maakte de bacteriën doelbewust sterker",
                    "Alle bacteriën leerden het antibioticum te verdragen",
                    "De patiënt werd zelf resistent tegen het middel",
                ],
                0,
                "Mutaties ontstaan toevallig, het antibioticum selecteert.",
            ),
            keuze(
                "Het antibioticum zorgt hier voor een sterke [[*selectiedruk|mutatie|biodiversiteit]].",
                "De omgeving bevoordeelt het resistente kenmerk.",
            ),
            tabel(
                "Klopt dit?",
                [
                    ("De allelfrequentie van het resistentie-allel stijgt.", J),
                    ("Bacteriën delen snel, dus gaat dit snel.", J),
                    ("Dit is evolutie die je vandaag kunt volgen.", J),
                    ("Een enkele bacterie is tijdens haar leven geëvolueerd.", F),
                ],
                "Evolutie gebeurt in een populatie, niet in één individu.",
            ),
        ],
    ),
    volgorde(
        "Zet de stappen van natuurlijke selectie in een logische volgorde.",
        ["Door mutaties ontstaan verschillende allelen", "Er is variatie tussen de individuen", "De omgeving bevoordeelt een kenmerk", "Die individuen krijgen meer nakomelingen", "De allelfrequentie verandert"],
        "Variatie, selectie en erfelijkheid: de drie pijlers van Darwin.",
    ),
    tabel(
        "Klopt dit over mutaties en evolutie?",
        [
            ("Mutaties ontstaan toevallig, niet op bestelling.", J),
            ("Mutaties zijn de bron van nieuwe allelen.", J),
            ("De omgeving kiest welke allelen vaker doorgaan.", J),
            ("Een dier krijgt een mutatie omdat het die nodig heeft.", F),
        ],
        "Selectie werkt op de variatie die er al is.",
    ),
    keuze(
        "Een orgaan zonder functie meer, zoals de staartbeentjes bij de mens, heet [[*rudimentair|analoog|homoloog]].",
        "Het verwijst naar een voorouder bij wie het orgaan nog werkte.",
    ),
    mk(
        "Waarom zitten er in Australië zoveel buideldieren en zo weinig andere zoogdieren?",
        [
            "Australië raakte vroeg los van de rest",
            "Buideldieren werden er later door mensen uitgezet",
            "Het klimaat van Australië is overal net hetzelfde",
            "Andere zoogdieren kunnen geen eucalyptus eten",
        ],
        0,
        "Door de continentendrift evolueerden de buideldieren daar apart.",
    ),
    tabel(
        "Populatie of niet?",
        [
            ("alle karpers in één vijver", J),
            ("alle vissen in één vijver", F),
            ("alle mussen in één dorp", J),
            ("alle dieren in een bos", F),
        ],
        "Een populatie: individuen van één soort in één gebied.",
    ),
    sleep(
        "De peper-en-zoutvlinder werd in de industriestreken donkerder. Op [[roetzwarte]] bomen werden de lichte vlinders vaker [[opgegeten]]. Daardoor steeg de [[allelfrequentie]] van het donkere allel.",
        ["groene", "geboren", "mutatie"],
        "De vogels waren hier de selectiedruk.",
    ),
    tabel(
        "Klopt dit over een gemeenschappelijke voorouder?",
        [
            ("Mens en chimpansee stammen af van dezelfde voorouder.", J),
            ("De mens stamt af van de chimpansee van vandaag.", F),
            ("Hoe verwanter twee soorten, hoe meer hun DNA gelijkt.", J),
        ],
        "Beide soorten zijn elk langs een eigen weg verder geëvolueerd.",
    ),
    mk(
        "Een zeldzame diersoort telt nog maar twintig dieren die sterk op elkaar lijken. Waarom loopt ze extra gevaar bij een nieuwe ziekte?",
        [
            "Weinig variatie om op te selecteren",
            "Ze heeft net te veel verschillende allelen",
            "Ze kan helemaal geen jongen meer krijgen",
            "Ze evolueert veel sneller dan andere soorten",
        ],
        0,
        "Komt er een nieuwe ziekte, dan is er misschien geen enkel individu dat ze overleeft.",
    ),
    tabel(
        "Klopt dit over Darwins survival of the fittest?",
        [
            ("Fit betekent: passend bij de omgeving.", J),
            ("Wie beter past, krijgt meer nakomelingen.", J),
            ("Fit betekent altijd: de sterkste en de snelste.", F),
        ],
        "Een kleine, goed gecamoufleerde soort kan de fitste zijn.",
    ),
    keuze(
        "De boom die de verwantschap tussen alle soorten voorstelt, heet de [[*tree of life|food chain|karyogram]].",
        "Elke vertakking staat voor een gemeenschappelijke voorouder.",
    ),
    tabel(
        "Klopt dit over fossielen?",
        [
            ("Een continue reeks toont een soort stap voor stap veranderen.", J),
            ("Een overgangsvorm heeft kenmerken van twee groepen.", J),
            ("Een vis met pootachtige vinnen kan zo'n overgangsvorm zijn.", J),
            ("Van elke soort die ooit leefde, vond men een fossiel.", F),
        ],
        "Fossilisatie is zeldzaam: veel soorten lieten geen sporen na.",
    ),
    keuze(
        "Een kenmerk waarmee een organisme beter bij zijn omgeving past, heet een [[*adaptatie|mutatie|populatie]].",
        "Bv. de witte vacht van een ijsbeer.",
    ),
    tabel(
        "Waarom is er variatie binnen een populatie?",
        [
            ("door mutaties in het DNA", J),
            ("door mixing en crossing-over bij de meiose", J),
            ("door de bevruchting, die allelen van twee ouders samenbrengt", J),
            ("doordat dieren zelf kiezen welke genen ze willen", F),
        ],
        "De moderne evolutietheorie verklaart zo waar Darwins variatie vandaan komt.",
    ),
    mk(
        "Waarom lijken de embryo's van een vis, een kip en een mens in het begin zo op elkaar?",
        [
            "Verwante soorten ontwikkelen zich gelijkaardig",
            "Ze leven alle drie in het begin in het water",
            "Ze hebben op dat moment precies hetzelfde DNA",
            "Ze worden alle drie in een ei geboren",
        ],
        0,
        "Zo'n gelijke start wijst op een gemeenschappelijke voorouder.",
    ),
    tabel(
        "Klopt dit over biodiversiteit?",
        [
            ("Ze omvat de verscheidenheid aan soorten.", J),
            ("Ook de genetische diversiteit binnen een soort hoort erbij.", J),
            ("Ook de verscheidenheid aan ecosystemen hoort erbij.", J),
            ("Ze telt alleen het aantal dieren in een gebied.", F),
        ],
        "Biodiversiteit bestaat op drie niveaus.",
    ),
    open_(
        "Leg uit waarom de erfelijkheid van verworven eigenschappen, zoals Lamarck die zag, niet klopt.",
        "Wat een dier tijdens zijn leven verandert, zoals sterkere spieren door training, zit in zijn lichaamscellen en niet in het DNA van zijn gameten. Alleen wat in de eicellen en zaadcellen zit, gaat naar de nakomelingen. Een smid met sterke armen krijgt dus geen kinderen met sterke armen door zijn werk.",
    ),
]
