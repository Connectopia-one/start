# -*- coding: utf-8 -*-
"""Uitdaging Sociale en gedragswetenschappen 🚀 Boost doorstroom (25 november
2026), in de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Zes situaties en zes groepen om op te klikken,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een korte
schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Sociale en gedragswetenschappen Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_sgw.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Sociale en gedragswetenschappen"
BESTAND = "boost-sgw-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/sgw-boost-uitdaging"
SIT = "zes-situaties.svg"
GRP = "zes-groepen.svg"

# klikvakken: _blad.zone(i, 6)
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Situaties (prent)
    klik("Lees de zes situaties. Klik op het voorbeeld van animisme.",
         SIT, [Z[2]],
         "De kleuter geeft de maan een gevoel en een wil. Levenloze dingen gevoelens geven, heet animisme: een denkfout uit het pre-operationeel stadium."),
    klik("Klik op de situatie die het conflict identiteit versus verwarring van Erikson toont.",
         SIT, [Z[5]],
         "In de adolescentie zoekt een jongere wie hij is door stijlen, groepen en meningen uit te proberen."),
    klik("Klik op de situatie die bij het pre-conventionele stadium van Kohlberg hoort.",
         SIT, [Z[4]],
         "De jongen steelt niet uit angst voor straf. In het pre-conventionele stadium sturen straf en beloning het gedrag."),
    met_prent(SIT, tabel(
        "In welk stadium van Piaget zit het kind uit deze situatie?",
        [
            ("Situatie 1: de baby zoekt het speeltje niet", "Sensomotorisch"),
            ("Situatie 2: de maan volgt de kleuter", "Pre-operationeel"),
            ("Situatie 3: stokjes van klein naar groot leggen", "Concreet-operationeel"),
        ],
        "De baby mist nog objectpermanentie, de kleuter denkt animistisch en seriatie hoort bij het concreet-operationeel stadium.",
        kolommen=["Sensomotorisch", "Pre-operationeel", "Concreet-operationeel", "Formeel-operationeel"])),
    met_prent(SIT, keuze(
        "Situatie 6 toont de pool [[*integriteit|wanhoop|stagnatie]] uit de laatste fase van Erikson. De kracht die daarbij hoort, is [[*wijsheid|hoop|wil]].",
        "In de late volwassenheid speelt integriteit versus wanhoop. Wie tevreden terugkijkt, ontwikkelt wijsheid.")),

    # Groepen (prent)
    klik("Lees de zes verzamelingen mensen. Klik op de sociale categorie volgens Merton.",
         GRP, [Z[3]],
         "Linkshandigen delen één kenmerk, maar hebben geen contact en geen gevoel van samenhoren. Dat is een sociale categorie."),
    klik("Klik op het samenzijn volgens Merton.",
         GRP, [Z[4]],
         "Mensen die toevallig samen op de bus wachten, verbindt enkel de plaats, en dat maar even."),
    klik("Klik op de collectiviteit volgens Merton.",
         GRP, [Z[2]],
         "Supporters delen een gevoel van samenhoren zonder elkaar persoonlijk te kennen."),
    met_prent(GRP, tabel(
        "Is deze groep uit de prent primair en informeel, of secundair en formeel?",
        [
            ("Het gezin van Sara", "Primair en informeel"),
            ("Een vakbond met statuten", "Secundair en formeel"),
            ("Vijf vriendinnen die elke vrijdag afspreken", "Primair en informeel"),
        ],
        "Primair of secundair gaat over de band, formeel of informeel over vastgelegde regels.",
        kolommen=["Primair en informeel", "Secundair en formeel"])),

    # Ontwikkeling
    keuze(
        "Een kind leert fietsen na veel oefenen. Dat is vooral [[*leren|rijpen|groeien]]. De wisselwerking tussen erfelijkheid en omgeving heet [[*nature en nurture|zelfbepaling]].",
        "Ontwikkeling bestaat uit groeien, rijpen en leren. Nature is erfelijkheid, nurture is de omgeving."),
    tabel(
        "Grove of fijne motoriek?",
        [
            ("Leren stappen", "Grove motoriek"),
            ("Een pen tussen drie vingers houden", "Fijne motoriek"),
            ("Een bal ver weg gooien", "Grove motoriek"),
            ("Een knoop dichtdoen", "Fijne motoriek"),
        ],
        "Grove motoriek gebruikt grote spiergroepen. Fijne motoriek vraagt precieze bewegingen van hand en vingers.",
        kolommen=["Grove motoriek", "Fijne motoriek"]),
    volgorde(
        "Rangschik de vier stadia van de cognitieve ontwikkeling van Piaget, van baby tot adolescent.",
        ["sensomotorisch", "pre-operationeel", "concreet-operationeel", "formeel-operationeel"],
        "Van denken met zintuigen en bewegingen naar symbolisch, dan logisch-concreet en tot slot abstract denken."),
    mk("Je rolt een bol klei uit tot een worst. Een kleuter zegt dat er nu meer klei is. Hoe heet wat hij nog mist?",
       ["conservatie", "objectpermanentie", "persoonspermanentie", "intentioneel handelen"],
       0,
       "Conservatie is weten dat de hoeveelheid gelijk blijft als de vorm verandert. Die notie komt in het concreet-operationeel stadium."),

    # Kohlberg
    sorteer(
        "Bij welk stadium van Kohlberg hoort deze reden?",
        ["Pre-conventioneel", "Conventioneel", "Post-conventioneel"],
        [
            ["Ik doe het niet, anders word ik gestraft.", "Pre-conventioneel"],
            ["Het is tegen de wet.", "Conventioneel"],
            ["Een onrechtvaardige wet mag je aanklagen.", "Post-conventioneel"],
            ["Ik krijg er iets voor terug.", "Pre-conventioneel"],
            ["Wat zouden de anderen van me denken?", "Conventioneel"],
        ],
        "Pre-conventioneel: straf en beloning. Conventioneel: regels en wat anderen verwachten. Post-conventioneel: eigen principes."),

    # Hechting en sociaal
    keuze(
        "Een kind speelt rustig, kijkt af en toe of mama er nog is en speelt verder. Dat is [[*veilige|gedesorganiseerde|angstig-vermijdende]] hechting. Twee peuters spelen naast elkaar met eigen speelgoed: dat heet [[*parallel spel|samenspel]].",
        "Een veilig gehecht kind gebruikt de ouder als veilige basis. Peuters spelen eerst naast elkaar voor ze echt samen spelen."),
    tabel(
        "Wat weet je over gehechtheid? Duid aan wat klopt.",
        [
            ("Een kind kan zich aan meer dan één persoon hechten.", J),
            ("Scheidingsangst wijst er altijd op dat een kind onveilig gehecht is.", F),
            ("Er zijn drie vormen van onveilige hechting.", J),
        ],
        "Scheidingsangst is normaal rond een bepaalde leeftijd. De vormen van onveilige hechting zijn angstig-vermijdend, angstig-ambivalent en gedesorganiseerd."),

    # Erikson
    koppel(
        "Koppel het conflict van Erikson aan de kracht die het oplevert.",
        [
            ["vertrouwen versus wantrouwen", "hoop"],
            ["autonomie versus twijfel", "wil"],
            ["initiatief versus schuld", "doelgerichtheid"],
            ["integriteit versus wanhoop", "wijsheid"],
        ],
        ["rijkdom"],
        "Elke opgeloste fase levert een kracht op. Rijkdom is geen kracht van Erikson."),

    # Persoonlijkheid en zelfconcept
    koppel(
        "Welke beschrijving past bij elk van de vier temperamenten van Galenus?",
        [
            ["flegmatisch", "rustig en moeilijk uit zijn lood te slaan"],
            ["cholerisch", "snel kwaad en driftig"],
            ["sanguinisch", "opgewekt en levendig"],
            ["melancholisch", "somber en piekerend"],
        ],
        [],
        "Galenus beschreef vier temperamenten. Ze zijn vandaag niet wetenschappelijk bewezen, maar worden nog vaak gebruikt."),
    keuze(
        "Een leerling durft een moeilijke oefening aan omdat het vorige keer lukte. Dat is [[*self-efficacy|body-image|zelfwaardering]]. Het beeld dat je van je eigen lichaam hebt, heet je [[*body-image|temperament]].",
        "Self-efficacy is het vertrouwen dat je een taak aankunt. Body-image is het beeld van je lichaam, dat niet altijd met de werkelijkheid klopt."),
    mk("Iemand praat graag met vreemden en zoekt altijd gezelschap op. Welke trek van de big five is hoog?",
       ["extraversie", "zorgvuldigheid", "emotionele stabiliteit", "openheid voor nieuwe ideeën"],
       0,
       "Extraversie gaat over hoe graag iemand contact zoekt met anderen."),

    # Emoties en motivatie
    tabel(
        "Welke component van de emotie is dit?",
        [
            ("Je hart klopt sneller als je schrikt.", "Fysiologisch"),
            ("Je deinst achteruit voor een hond.", "Gedrag"),
            ("Je denkt: die hond gaat me bijten.", "Mentaal"),
        ],
        "Een emotie heeft een fysiologische, een mentale en een gedragscomponent.",
        kolommen=["Fysiologisch", "Gedrag", "Mentaal"]),
    sorteer(
        "Intrinsieke of extrinsieke motivatie?",
        ["Intrinsiek", "Extrinsiek"],
        [
            ["Hij oefent gitaar omdat hij het leuk vindt.", "Intrinsiek"],
            ["Ze studeert om een nieuwe gsm te verdienen.", "Extrinsiek"],
            ["Hij leest omdat hij nieuwsgierig is naar het verhaal.", "Intrinsiek"],
            ["Ze ruimt op om geen straf te krijgen.", "Extrinsiek"],
        ],
        "Intrinsieke motivatie komt van binnenuit. Extrinsieke motivatie komt van buitenaf: een beloning of een straf."),
    tabel(
        "Is deze attributie intern of extern, en kan je ze controleren?",
        [
            ("Ik heb te weinig geoefend.", "Intern en controleerbaar"),
            ("Ik heb er geen aanleg voor.", "Intern en oncontroleerbaar"),
            ("De toets was te moeilijk.", "Extern"),
        ],
        "Oefening ligt bij jou en kan je sturen. Aanleg ligt bij jou maar stuur je niet. Een moeilijke toets ligt buiten jou.",
        kolommen=["Intern en controleerbaar", "Intern en oncontroleerbaar", "Extern"]),

    # Cultuur en socialisatie
    koppel(
        "Koppel het begrip aan de omschrijving.",
        [
            ["enculturatie", "een kind leert de cultuur waarin het opgroeit"],
            ["acculturatie", "je past je aan een nieuwe cultuur aan"],
            ["etnocentrisme", "een andere cultuur beoordelen vanuit de jouwe"],
            ["subcultuur", "een groep met eigen gewoontes binnen de dominante cultuur"],
        ],
        ["een toevallige groep op één plek"],
        "Een toevallige groep op één plek is een samenzijn van Merton, geen cultuurbegrip."),
    tabel(
        "Welke cultuuruiting is dit?",
        [
            ("Een vlag", "Symbool"),
            ("Een trouwfeest met een vast verloop", "Ritueel"),
            ("'Je laat oudere mensen voorgaan.'", "Norm"),
        ],
        "Een vlag staat voor iets anders: een symbool. Een vast verloop bij een belangrijk moment is een ritueel. Een concrete gedragsregel is een norm.",
        kolommen=["Symbool", "Ritueel", "Norm"]),
    tabel(
        "Op welk niveau van socialisatie werkt dit vooral?",
        [
            ("het gezin", "Primair"),
            ("de school", "Secundair"),
            ("de massamedia", "Tertiair"),
        ],
        "Het gezin socialiseert primair, de school secundair en de media tertiair, zonder rechtstreeks persoonlijk contact.",
        kolommen=["Primair", "Secundair", "Tertiair"]),
    keuze(
        "Een leerling die al stage loopt om later verpleegkundige te worden, maakt [[*anticiperende|primaire]] socialisatie mee. Gedrag dat anderen helpt, heet [[*prosociaal|antisociaal]] gedrag.",
        "Anticiperende socialisatie bereidt je voor op een rol die nog komt."),

    # Positie, rol en status
    sorteer(
        "Is deze sociale positie toegewezen of verworven? Sorteer.",
        ["Toegewezen", "Verworven"],
        [
            ["dochter", "Toegewezen"],
            ["advocaat", "Verworven"],
            ["kapitein van de voetbalploeg", "Verworven"],
            ["zestienjarige", "Toegewezen"],
        ],
        "Een toegewezen positie krijg je zonder er iets voor te doen. Een verworven positie behaal je zelf."),
    tabel(
        "Welk soort rollenconflict beleeft deze persoon?",
        [
            ("Een student moet studeren maar ook avondwerk doen.", "Extern"),
            ("Een leerkracht moet streng zijn voor de directie en begripvol voor de leerling.", "Intern"),
            ("Een trainer coacht zijn eigen zoon in de ploeg.", "Extern"),
        ],
        "Bij een extern rollenconflict botsen twee posities. Bij een intern rollenconflict botsen verwachtingen binnen één positie.",
        kolommen=["Intern", "Extern"]),
    keuze(
        "Opklimmen of afzakken op de maatschappelijke ladder heet [[*sociale mobiliteit|socialisatie]]. Het doorgeven van een positie van ouder naar kind heet [[*reproductie|acculturatie]].",
        "Bij lage sociale mobiliteit bepaalt de positie van je ouders sterk je eigen kansen."),

    # Extra
    mk("Twee leerlingen werken even hard, maar de ene raakt verder dan de andere. Wat verklaart een sociaal wetenschapper daarmee?",
       ["Ook afkomst en netwerk bepalen hoe ver je raakt.", "Inzet heeft volgens hen geen enkel effect op succes.", "Kansen zijn voor iedereen in België precies gelijk.", "Inzet kan je niet meten, kansen wel met een test."],
       0,
       "Wie dezelfde inzet levert, raakt niet altijd even ver: afkomst, opleiding van de ouders en kennissen spelen mee."),
    sleep(
        "Het geheel van zelfbeeld, zelfwaardering, self-efficacy en body-image heet het [[zelfconcept]]. Hoe positief je over jezelf oordeelt, is je [[zelfwaardering]].",
        ["temperament", "karakter"],
        "Het zelfconcept heeft vier delen. Zelfwaardering is het oordeel over jezelf, het zelfbeeld de beschrijving."),

    mk("Een kind van acht rekent vlot met blokjes, maar snapt nog niet wat x betekent in een vergelijking. In welk stadium van Piaget zit het?",
       ["concreet-operationeel", "formeel-operationeel", "het pre-operationele stadium", "het sensomotorische stadium"],
       0,
       "De logica werkt al, maar heeft nog iets concreets nodig. Abstract denken over x komt pas in het formeel-operationeel stadium."),
    inv("Uit hoeveel stadia bestaat de morele ontwikkeling volgens Kohlberg? Schrijf het getal.",
        ["3", "drie"],
        "Pre-conventioneel, conventioneel en post-conventioneel."),
    tabel(
        "Welke functie van een emotie zie je hier vooral?",
        [
            ("Een baby huilt en zijn moeder komt kijken.", "Communiceren"),
            ("Je voelt angst in een donkere steeg en stapt sneller door.", "Waarschuwen"),
            ("Je praat stiller op een begrafenis dan op een feest.", "Aanpassen"),
        ],
        "Emoties laten anderen zien hoe je je voelt, waarschuwen voor gevaar en helpen je gedrag af te stemmen op de situatie.",
        kolommen=["Communiceren", "Waarschuwen", "Aanpassen"]),
    keuze(
        "Je beroep is een [[*verworven|toegewezen]] statusfactor. Je geslacht is een [[*toegewezen|verworven]] statusfactor.",
        "Een beroep behaal je zelf. Je geslacht krijg je bij de geboorte."),
    mk("In het dilemma van Heinz zegt iemand: 'Hij mag het medicijn stelen, want een mensenleven weegt zwaarder dan eigendom.' Welk stadium van Kohlberg past het best?",
       ["post-conventioneel", "pre-conventioneel", "het conventionele stadium", "het sensomotorische stadium"],
       0,
       "De persoon redeneert vanuit een eigen principe dat boven de wet staat. Dat hoort bij het post-conventionele stadium."),
    volgorde(
        "Zet de eerste vier conflicten van Erikson in de juiste volgorde.",
        ["vertrouwen versus wantrouwen", "autonomie versus twijfel", "initiatief versus schuld", "handvaardigheid versus minderwaardigheid"],
        "Babytijd, peutertijd, kleutertijd en lagereschooltijd volgen elkaar op met elk hun eigen conflict."),
    sleep(
        "Het gedrag dat anderen verwachten bij een positie, is de [[sociale rol]]. Alle rollen die bij één positie horen, vormen samen de [[rollenset]].",
        ["sociale categorie", "collectiviteit"],
        "Positie, rol en rollenset horen samen. Een sociale categorie en een collectiviteit zijn soorten van Merton."),
    # Schrijfopdracht
    open_("Een leerling zegt na een slechte toets: 'De leerkracht heeft me gewoon niet graag.' Leg in 4 à 6 zinnen uit wat een attributie is, welke attributie dit is en waarom een andere attributie hem meer zou helpen.",
          "Een attributie is de verklaring die iemand geeft voor een succes of een mislukking. Deze leerling geeft een externe attributie: de oorzaak ligt volgens hem bij de leerkracht. Die oorzaak kan hij niet controleren, dus hij denkt dat hij er niets aan kan doen. Als hij zegt 'ik heb te weinig geoefend', geeft hij een interne en controleerbare attributie. Dan kan hij zijn aanpak veranderen en de volgende keer beter scoren. Dat houdt ook zijn motivatie hoger.",
          "Een goed antwoord omschrijft attributie, benoemt de externe en oncontroleerbare verklaring, stelt een interne controleerbare attributie voor en legt het verband met motivatie."),
]
