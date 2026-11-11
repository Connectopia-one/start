"""Monopolistische concurrentie, oligopolie en speltheorie — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, vak_zone, pix_zone, s_tekst, s_vak, GROEN, LICHT

# Prent 1: uitbetalingsmatrix van twee bakkerijen (eigen tekening).
M_X0, M_Y0, M_B, M_H = 360, 190, 280, 170
WINST = [[(12, 12), (3, 18)], [(18, 3), (6, 6)]]
KEUZES = ["hoge prijs", "lage prijs"]


def _matrix():
    d = [s_tekst(500, 60, "Winst van Bakkerij Noord ; winst van Bakkerij Zuid (in duizend euro)", 22, vet=True),
         s_tekst(M_X0 + M_B, 120, "Bakkerij Zuid", 22, kleur=GROEN, vet=True),
         s_tekst(150, M_Y0 + M_H + 8, "Bakkerij Noord", 22, kleur=GROEN, vet=True)]
    for j, k in enumerate(KEUZES):
        x = M_X0 + j * M_B
        d.append(s_vak(x, M_Y0 - 50, M_B, 50, vul=LICHT, rand=GROEN))
        d.append(s_tekst(x + M_B / 2, M_Y0 - 18, k, 21, vet=True))
    for i, k in enumerate(KEUZES):
        y = M_Y0 + i * M_H
        d.append(s_vak(M_X0 - 130, y, 130, M_H, vul=LICHT, rand=GROEN))
        d.append(s_tekst(M_X0 - 65, y + M_H / 2 + 7, k, 20, vet=True))
        for j in range(2):
            x = M_X0 + j * M_B
            a, b = WINST[i][j]
            d.append(s_vak(x, y, M_B, M_H, vul="#fffdf7", rand=GROEN))
            d.append(s_tekst(x + M_B / 2, y + M_H / 2 + 12, f"{a} ; {b}", 36, vet=True))
    return d


def cel(i, j):
    return pix_zone(M_X0 + j * M_B + 4, M_Y0 + i * M_H + 4, M_B - 8, M_H - 8)


# Prent 2: de geknikte prijsafzetcurve.
G = venster("oligopolie-geknikte-curve", 0, 40, 0, 12, 4, 2)

GRAFIEKEN = [
    dict(naam="oligopolie-uitbetalingsmatrix", titel="Uitbetalingsmatrix van twee bakkerijen", eigen=_matrix),
    dict(naam=G, titel="Geknikte prijsafzetcurve van een oligopolist",
         krommen=[(lambda q: 10 - 0.1 * q if q <= 20 else 13 - 0.25 * q, "groen", "P", (0, 38)),
                  (lambda q: 10 - 0.2 * q, "oranje", "", (0, 20)),
                  (lambda q: 13 - 0.5 * q, "oranje", "MO", (20, 25)),
                  (lambda q: 4.5, "blauw", "MK", (0, 38))],
         stippel=[("v", 20)],
         labelplek={"P": (30, 5.5), "MO": (24.5, 0.9), "MK": (6, 4.5)},
         punten=[(20, 8, "knik")],
         xlabel="hoeveelheid", ylabel="prijs, kosten", ijk_x=4, ijk_y=2),
]

PRENTEN = [
    dict(bestand="oligopolie-uitbetalingsmatrix.svg", zelf=True, wat=GRAFIEKEN[0]["titel"], vragen="klikvragen over dominante strategie en Nash-evenwicht"),
    dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[1]["titel"], vragen="klikvragen over prijsstarheid"),
]
PM = "oligopolie-uitbetalingsmatrix.svg"
PK = f"{G}.svg"

VRAGEN = [
    klik(
        "Klik op het vak dat het Nash-evenwicht van dit spel voorstelt.",
        PM, [cel(1, 1)],
        "Wat Zuid ook doet, voor Noord is een lage prijs het beste (18 > 12 en 6 > 3), en voor Zuid net zo. Beide laag, elk 6: daar wint niemand iets door in zijn eentje te veranderen.",
    ),
    klik(
        "Klik op het vak waar de twee bakkerijen samen de hoogste winst halen.",
        PM, [cel(0, 0)],
        "Beide een hoge prijs geeft samen 24. Dat is meer dan het Nash-evenwicht (samen 12): het gevangenendilemma.",
    ),
    met_prent(PM, mk(
        "Heeft Bakkerij Noord een dominante strategie?",
        ["Ja, de lage prijs: die geeft meer winst, wat Zuid ook kiest",
         "Ja, de hoge prijs: die geeft samen de hoogste winst voor beide bakkerijen",
         "Nee, de beste keuze van Noord hangt af van wat Zuid kiest",
         "Nee, een dominante strategie bestaat enkel bij volkomen concurrentie"],
        0,
        "Kiest Zuid hoog: 18 > 12. Kiest Zuid laag: 6 > 3. Laag is dus altijd beter voor Noord.",
    )),
    met_prent(PM, mk(
        "De bakkerijen spreken stiekem af dat ze allebei een hoge prijs vragen. Waarom is die afspraak niet stabiel?",
        ["Elke bakkerij wint erbij door stiekem toch een lage prijs te vragen (18 in plaats van 12)",
         "Bij een hoge prijs maken ze allebei verlies, dus ze houden het niet lang vol",
         "De klanten verplichten de bakkerijen om de prijs weer te verlagen tot het Nash-evenwicht",
         "Bij een hoge prijs halen ze samen minder dan in het Nash-evenwicht met een lage prijs"],
        0,
        "Wie als enige de prijs verlaagt, gaat van 12 naar 18. Dat maakt een kartel onstabiel. Bovendien is zo'n afspraak in de EU verboden.",
    )),
    met_prent(PM, inv(
        "Zuid kiest een hoge prijs. Hoeveel duizend euro winst haalt Noord met zijn best-response strategie? Schrijf enkel het getal.",
        "18",
        "Gegeven dat Zuid hoog kiest, is een lage prijs de beste keuze voor Noord: 18 in plaats van 12.",
    )),
    klik(
        "Klik op het deel van de prijsafzetcurve waar de vraag elastisch is.",
        PK, [vak_zone(G, 2, 18, 8.1, 9.9)],
        "Boven de knik volgen de concurrenten een prijsstijging niet. Wie zijn prijs verhoogt, verliest veel klanten: daar is de vraag elastisch.",
    ),
    klik(
        "Klik op de plaats waar de MO-curve een sprong maakt.",
        PK, [vak_zone(G, 18.5, 21.5, 2.6, 6.4)],
        "Door de knik in de prijsafzetcurve springt MO bij de knik van 6 naar 3.",
    ),
    met_prent(PK, mk(
        "De marginale kosten stijgen van 4,5 naar 5,5. Wat doet de oligopolist met zijn prijs?",
        ["Hij houdt zijn prijs op 8, want MK snijdt MO nog altijd in de sprong",
         "Hij verhoogt zijn prijs, want zijn kosten zijn gestegen en dat rekent hij door",
         "Hij verlaagt zijn prijs, om klanten van de concurrenten af te snoepen",
         "Hij stopt met produceren, want de prijs dekt zijn kosten niet meer"],
        0,
        "Tussen 3 en 6 snijdt MK de MO-curve in de sprong: de beste hoeveelheid en de prijs blijven gelijk. Dat is prijsstarheid.",
    )),
    keuze(
        "Bij een geknikte prijsafzetcurve volgen concurrenten wel een prijs[[*daling|stijging]], maar geen prijs[[*stijging|daling]]. Onder de knik is de vraag [[*inelastisch|elastisch]].",
        "Verlaagt één bedrijf de prijs, dan volgen de anderen meteen en wint het weinig klanten.",
    ),
    tabel(
        "Hoort dit kenmerk bij monopolistische concurrentie of bij oligopolie?",
        [
            ("Honderden aanbieders met elk een eigen variant van het product", "Monopolistische concurrentie"),
            ("Hoge toetredingsdrempels", "Oligopolie"),
            ("Op lange termijn is de winst nul door nieuwe toetreders", "Monopolistische concurrentie"),
            ("Elke beslissing houdt rekening met de reactie van enkele grote concurrenten", "Oligopolie"),
            ("Lage toetredingsdrempels", "Monopolistische concurrentie"),
        ],
        "Monopolistische concurrentie: veel aanbieders, lage drempels. Oligopolie: enkele grote, afhankelijke aanbieders, hoge drempels.",
        kolommen=["Monopolistische concurrentie", "Oligopolie"],
    ),
    mk(
        "Een nieuw soort koffiebar maakt in een stad veel winst. Wat gebeurt er op lange termijn bij monopolistische concurrentie?",
        ["Er komen nieuwe koffiebars bij, tot de winst verdwenen is en de prijs gelijk is aan de gemiddelde kosten",
         "De koffiebar blijft voor altijd winst maken, want zijn product is een beetje anders dan dat van de rest",
         "De overheid verbiedt nieuwe koffiebars om de winst van de eerste koffiebar te beschermen",
         "De koffiebar verhoogt zijn prijs steeds verder, want zijn prijsafzetcurve is horizontaal"],
        0,
        "Door de lage drempels treden nieuwe aanbieders toe. De prijsafzetcurve raakt dan de GK-curve: winst nul.",
    ),
    mk(
        "Een pizzeria in een stad met honderden restaurants steekt veel geld in reclame. Waarom?",
        ["Om haar product te onderscheiden van dat van de concurrent",
         "Omdat de wet haar verplicht haar prijzen bekend te maken",
         "Omdat alle restaurants exact hetzelfde product verkopen",
         "Om de toetredingsdrempels voor nieuwe restaurants te verlagen"],
        0,
        "Elk product is een beetje anders. Met reclame benadrukt een bedrijf dat verschil.",
    ),
    mk(
        "Bij monopolistische concurrentie maakt een aanbieder op korte termijn winst. Hoe kiest hij zijn hoeveelheid?",
        ["Waar MO = MK, zoals een monopolist", "Waar de prijs gelijk is aan de laagste GK",
         "Waar de totale opbrengst het grootst is", "Waar de prijs gelijk is aan MK, zoals op een atomische markt"],
        0,
        "Hij heeft een dalende prijsafzetcurve en kiest dus net als een monopolist waar MO = MK.",
    ),
    tabel(
        "Waar of niet waar over marktvormen en hun prijsafzetcurve?",
        [
            ("Bij oligopolie daalt de prijsafzetcurve van een aanbieder.", J),
            ("De meest elastische prijsafzetcurve van één aanbieder vind je bij volkomen concurrentie.", J),
            ("Bij monopolistische concurrentie is de prijsafzetcurve van één aanbieder horizontaal.", F),
            ("Speltheorie is vooral nuttig bij volkomen concurrentie.", F),
        ],
        "Monopolie, oligopolie en monopolistische concurrentie hebben een dalende curve. Speltheorie is vooral nuttig bij oligopolie.",
    ),
    koppel(
        "Koppel elk begrip uit de speltheorie aan zijn betekenis.",
        [
            ["Best-response strategie", "De beste keuze, gegeven wat de andere speler doet"],
            ["Dominante strategie", "De beste keuze, wat de andere speler ook doet"],
            ["Nash-evenwicht", "Niemand wint iets door in zijn eentje te veranderen"],
            ["Gevangenendilemma", "Eigenbelang geeft beide spelers een slechtere uitkomst"],
        ],
        ["De speler met de hoogste winst wint het spel"],
        "Dominant is altijd het beste; best-response hangt af van wat de ander doet.",
    ),
    mk(
        "Een leerling zegt: 'Een spel heeft enkel een Nash-evenwicht als elke speler een dominante strategie heeft.' Wat klopt?",
        ["Fout: een spel kan een Nash-evenwicht hebben zonder dat een speler een dominante strategie heeft",
         "Juist: zonder dominante strategie weet geen enkele speler wat hij moet kiezen, dus is er geen evenwicht",
         "Fout: een spel waarin een speler een dominante strategie heeft, heeft nooit een Nash-evenwicht",
         "Juist: het Nash-evenwicht is per definitie de dominante strategie van beide spelers"],
        0,
        "Het Nash-evenwicht vraagt enkel dat niemand wint door alleen te veranderen.",
    ),
    casus(
        "Twee luchtvaartmaatschappijen, Alfa en Beta, kiezen tussen veel reclame en weinig reclame. Winst (Alfa ; Beta) in miljoen euro: beide veel: 4 ; 4. Alfa veel en Beta weinig: 9 ; 2. Alfa weinig en Beta veel: 2 ; 9. Beide weinig: 7 ; 7.",
        [
            mk("Wat is de dominante strategie van Alfa?",
               ["Veel reclame", "Weinig reclame", "Alfa heeft geen dominante strategie", "Dezelfde keuze als Beta"], 0,
               "Kiest Beta veel: 4 > 2. Kiest Beta weinig: 9 > 7. Veel reclame is dus altijd beter voor Alfa."),
            mk("Wat is het Nash-evenwicht?",
               ["Beide veel reclame: 4 ; 4", "Beide weinig reclame: 7 ; 7", "Alfa veel, Beta weinig: 9 ; 2", "Er is geen Nash-evenwicht"], 0,
               "Beide hebben veel reclame als dominante strategie, dus komen ze uit op 4 ; 4."),
            mk("Waarom is dit een gevangenendilemma?",
               ["Met beide weinig reclame zouden ze elk 7 halen, maar eigenbelang brengt hen bij 4",
                "Omdat Alfa altijd meer winst maakt dan Beta, wat Beta ook kiest en hoeveel reclame ze maken",
                "Omdat er geen enkele combinatie van keuzes is waarbij beide maatschappijen winst maken",
                "Omdat het Nash-evenwicht hier de hoogste winst samen geeft voor beide maatschappijen"], 0,
               "Samen zouden ze beter af zijn, maar elk apart heeft er belang bij veel reclame te maken."),
        ],
    ),
    mk(
        "Drie cementproducenten spreken in het geheim een minimumprijs af. Hoe noem je dat, en mag het?",
        ["Een kartel, en dat is in de EU verboden", "Een kartel, en dat mag in de EU zolang het geheim blijft", "Een monopolie, en dat mag als ze samen een patent hebben", "Een Nash-evenwicht, en daar grijpt de overheid niet in"],
        0,
        "Kartelafspraken zijn in de Europese Unie verboden, ook als ze geheim blijven.",
    ),
    sleep(
        "Bij oligopolie blijft de prijs vaak lang gelijk, ook als de kosten veranderen. Dat heet [[prijsstarheid]]. De verklaring is de [[geknikte]] prijsafzetcurve.",
        ["prijsconcurrentie", "horizontale", "inflatie"],
        "De knik zorgt voor een sprong in de MO-curve.",
    ),
    open_(
        "Twee tankstations staan naast elkaar. Leg met de geknikte prijsafzetcurve uit waarom hun prijs vaak lang gelijk blijft.",
        "Verlaagt het ene station de prijs, dan volgt het andere meteen: het eerste wint weinig klanten (inelastische vraag onder de knik). Verhoogt het de prijs, dan volgt het andere niet en verliest het veel klanten (elastische vraag boven de knik). Geen van beide heeft er dus belang bij de prijs te veranderen.",
    ),
    mk(
        "Welk voorbeeld past het best bij een oligopolie?",
        ["De drie grote operatoren voor mobiele abonnementen in België", "De honderden kappers in een grote stad",
         "De duizenden graanboeren in Europa", "Het enige bedrijf dat een geneesmiddel met patent mag maken"],
        0,
        "Enkele grote aanbieders die van elkaar afhankelijk zijn, met hoge toetredingsdrempels.",
    ),
    tabel(
        "Wat hebben deze marktvormen gemeen met het monopolie?",
        [
            ("Oligopolie: de aanbieders hebben wat invloed op de prijs", J),
            ("Monopolistische concurrentie: een aanbieder kan op korte termijn winst maken", J),
            ("Atomische markt: een aanbieder kan de prijs beïnvloeden", F),
            ("Atomische markt: de prijsafzetcurve van een aanbieder daalt", F),
        ],
        "Bij volkomen concurrentie is één aanbieder prijsnemer met een horizontale prijsafzetcurve.",
    ),
    met_prent(PK, inv(
        "Lees af: bij welke hoeveelheid ligt de knik in de prijsafzetcurve? Schrijf enkel het getal.",
        "20",
        "De knik ligt bij hoeveelheid 20 en prijs 8.",
    )),
    met_prent(PK, mk(
        "Tussen welke waarden mogen de marginale kosten schommelen zonder dat de prijs van 8 verandert?",
        ["Tussen 3 en 6", "Tussen 0 en 8", "Tussen 6 en 10", "Tussen 4,5 en 8"],
        0,
        "Zolang MK door de sprong van de MO-curve loopt (van 6 naar 3), blijft de beste hoeveelheid 20 en de prijs 8.",
    )),
    keuze(
        "Speltheorie bestudeert beslissingen waarbij je uitkomst [[*afhangt van|los staat van]] wat de ander doet. Ze is dus vooral nuttig bij [[*oligopolie|volkomen concurrentie]].",
        "Bij enkele grote aanbieders hangt je winst sterk af van de zet van je concurrent.",
    ),
    sorteer(
        "Is dit een kenmerk van een Nash-evenwicht of van een dominante strategie?",
        ["Nash-evenwicht", "Dominante strategie"],
        [
            ["Niemand heeft spijt van zijn keuze, gegeven wat de ander deed", "Nash-evenwicht"],
            ["Is de beste keuze, wat de andere speler ook doet", "Dominante strategie"],
            ["Gaat over de combinatie van keuzes van alle spelers", "Nash-evenwicht"],
            ["Gaat over de keuze van één speler", "Dominante strategie"],
        ],
        "Een dominante strategie hoort bij één speler; een Nash-evenwicht is een combinatie van keuzes.",
    ),
    inv(
        "In de matrix van Alfa en Beta (beide veel: 4 ; 4, beide weinig: 7 ; 7) halen ze samen in het Nash-evenwicht 8 miljoen. Hoeveel miljoen meer zouden ze samen halen met beide weinig reclame? Schrijf enkel het getal.",
        "6",
        "Samen 14 tegenover samen 8: 6 miljoen meer.",
    ),
    volgorde(
        "Een oligopolist verhoogt als enige zijn prijs. Zet de gevolgen in de juiste volgorde.",
        ["De concurrenten volgen de prijsstijging niet", "Zijn product is nu duurder dan dat van de rest",
         "Veel klanten stappen over naar de concurrenten", "Zijn omzet daalt sterk"],
        "Boven de knik is de vraag elastisch: een hogere prijs kost veel klanten.",
    ),
]
