"""Kunststoffen: polymeren en hun eigenschappen — pittig (⚗️ Beyond doorstroom, chemie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Ketenstructuren --------------------------------------------------------------
KS = Prent("ketenstructuren", "Drie kunststoffen op deeltjesniveau", "drie vakken met lange golvende ketens: links los naast elkaar, in het midden met enkele bruggen, rechts met heel veel bruggen; letters P, Q en R")
KLR = [BLAUW, ORANJE, GROEN, PAARS, ROOD]


def _ketens(p, x0, bruggen):
    p.rect(x0, 120, 270, 330, "#fbfbf7", DONKER, 14, 2)
    for j in range(5):
        y0 = 160 + j * 62
        pts = [(x0 + 20 + t * 2.3, y0 + 14 * math.sin(t / 12 + j)) for t in range(0, 101)]
        p.pad("M " + " L ".join(f"{a:.1f} {b:.1f}" for a, b in pts), "none", KLR[j], 4)
    for (j, t) in bruggen:
        x = x0 + 20 + t * 2.3
        y1 = 160 + j * 62 + 14 * math.sin(t / 12 + j)
        y2 = 160 + (j + 1) * 62 + 14 * math.sin(t / 12 + j + 1)
        p.lijn(x, y1, x, y2, DONKER, 4)


_ketens(KS, 50, [])
_ketens(KS, 365, [(0, 30), (1, 70), (2, 20), (3, 60)])
_ketens(KS, 680, [(j, t) for j in range(4) for t in (10, 30, 50, 70, 90)])
for k, x in zip("PQR", (185, 500, 815)):
    KS.letter(x, 510, k)
ZKS = {k: [Prent.zone(x - 135, 120, 270, 330), Prent.rond(x, 510, 22)] for k, x in zip("PQR", (185, 500, 815))}

# Vier polymeerketens --------------------------------------------------------
PK = Prent("vier-polymeerketens", "Een stukje uit vier polymeerketens", "vier rijen met een stuk polymeerketen in formule; letters A tot D")
KET = {
    "A": "–CH₂–CH₂–CH₂–CH₂–CH₂–CH₂–",
    "B": "–CH₂–CH(CH₃)–CH₂–CH(CH₃)–",
    "C": "–CH₂–CHCl–CH₂–CHCl–CH₂–CHCl–",
    "D": "–CF₂–CF₂–CF₂–CF₂–CF₂–CF₂–",
}
for i, (k, t) in enumerate(KET.items()):
    y = 140 + i * 115
    PK.rect(150, y - 42, 760, 84, "#ffffff", DONKER, 14, 2)
    PK.tekst(530, y + 10, t, 28, vet=True)
    PK.letter(95, y, k)
ZPK = {k: [Prent.zone(150, 98 + i * 115, 760, 84), Prent.rond(95, 140 + i * 115, 22)] for i, k in enumerate(KET)}

VRAGEN = [
    klik(
        "Klik op de kunststof die je kan indrukken en die daarna terugveert.",
        KS.bestand, ZKS["Q"],
        "Enkele crosslinks: de ketens kunnen bewegen maar worden teruggetrokken. Een elastomeer.",
    ),
    klik(
        "Klik op de kunststof die je niet opnieuw kan smelten en vormen.",
        KS.bestand, ZKS["R"],
        "Veel crosslinks: een thermoharder ontleedt eerder dan te smelten.",
    ),
    met_prent(KS.bestand, tabel(
        "Welke soort kunststof is dit?",
        [
            ("P", "Thermoplast"),
            ("Q", "Elastomeer"),
            ("R", "Thermoharder"),
        ],
        "Hoe meer bruggen tussen de ketens, hoe minder de kunststof vervormt.",
        kolommen=["Thermoplast", "Elastomeer", "Thermoharder"],
    )),
    met_prent(KS.bestand, tabel(
        "Kijk naar de drie structuren. Klopt dit?",
        [
            ("P wordt zacht als je hem verwarmt.", J),
            ("P is het makkelijkst te recycleren.", J),
            ("R vervormt het makkelijkst bij warmte.", F),
        ],
        "Losse ketens kunnen bij warmte langs elkaar schuiven.",
    )),
    klik(
        "Klik op de keten van PVC.",
        PK.bestand, ZPK["C"],
        "Het monomeer is chlooretheen: om het andere koolstofatoom hangt een Cl.",
    ),
    klik(
        "Klik op de keten van de kunststof in een antikleefpan.",
        PK.bestand, ZPK["D"],
        "PTFE, uit tetrafluoretheen.",
    ),
    met_prent(PK.bestand, tabel(
        "Uit welk monomeer is deze keten gemaakt?",
        [
            ("A", "etheen"),
            ("B", "propeen"),
            ("C", "chlooretheen"),
            ("D", "tetrafluoretheen"),
        ],
        "Neem het stukje van twee koolstofatomen dat zich herhaalt en zet de dubbele binding terug.",
        kolommen=["etheen", "propeen", "chlooretheen", "tetrafluoretheen"],
    )),
    met_prent(PK.bestand, keuze(
        "Alle vier de ketens ontstaan door een [[*polyadditie|polycondensatie]], want hun monomeren hebben een [[*dubbele binding|OH-groep]].",
        "Bij een polyadditie gaat de dubbele binding open en komt er geen bijproduct vrij.",
    )),
    tabel(
        "Wordt deze kunststof gemaakt met een polyadditie of een polycondensatie?",
        [
            ("PE", "Polyadditie"),
            ("PS", "Polyadditie"),
            ("PET", "Polycondensatie"),
            ("nylon", "Polycondensatie"),
        ],
        "Bij een polycondensatie komt er bij elke koppeling een kleine molecule vrij.",
        kolommen=["Polyadditie", "Polycondensatie"],
    ),
    koppel(
        "Koppel elke kunststof aan een typische toepassing.",
        [
            ("PET", "drankflessen"),
            ("PVC", "afvoerbuizen"),
            ("PTFE", "antikleeflaag van een pan"),
            ("PS-schuim", "schokbestendige verpakking"),
            ("PA", "touw en kledingvezels"),
        ],
        ["glas voor ramen"],
        "Eigenschappen zoals doorzichtig, stevig, glad of licht bepalen de keuze.",
    ),
    mk(
        "Bij de productie van nylon koppelen twee soorten monomeren. Wat is de rol van die twee?",
        [
            "Zuurgroep en aminegroep vormen de binding",
            "Het ene levert een dubbele binding voor het andere",
            "Ze vormen samen een polyadditie zonder bijproduct",
            "Het ene neemt het water op dat het andere afgeeft",
        ],
        0,
        "Bij elke amidebinding komt er water vrij: een polycondensatie.",
    ),
    casus(
        "Een fabriek maakt 1000 kg polyetheen uit etheen.",
        [
            inv(
                "Hoeveel kg etheen heeft ze daarvoor minstens nodig?",
                ["1000", "1000 kg"],
                "Bij een polyadditie zit alle massa van het monomeer in het polymeer.",
            ),
            keuze(
                "Bij deze reactie ontstaat [[*geen bijproduct|water|waterstofchloride]].",
                "De dubbele bindingen gaan open en koppelen aan elkaar.",
            ),
            mk(
                "Waarom smelt PE over een gebied van temperaturen en niet bij één temperatuur?",
                [
                    "De ketens zijn niet allemaal even lang",
                    "PE bevat heel veel crosslinks tussen de ketens",
                    "PE is opgebouwd als een ionrooster",
                    "PE bevat water tussen de ketens",
                ],
                0,
                "Een mengsel van ketens van verschillende lengte heeft geen scherp smeltpunt.",
            ),
        ],
    ),
    tabel(
        "Welke soort kunststof past het best bij deze toepassing?",
        [
            ("een rubberen band", "Elastomeer"),
            ("een stopcontact dat warm kan worden", "Thermoharder"),
            ("een fles die gerecycleerd wordt", "Thermoplast"),
            ("een fietsbel-handvat dat indrukbaar is", "Elastomeer"),
        ],
        "Warmtebestendig: thermoharder. Terugverend: elastomeer. Opnieuw te vormen: thermoplast.",
        kolommen=["Thermoplast", "Thermoharder", "Elastomeer"],
    ),
    volgorde(
        "Zet deze kunststoffen van weinig naar veel crosslinks.",
        ["thermoplast", "elastomeer", "thermoharder"],
        "Geen, enkele, heel veel bruggen.",
    ),
    mk(
        "Wat doet vulkaniseren met rubber?",
        [
            "Het legt zwavelbruggen tussen de ketens",
            "Het breekt alle bruggen tussen de ketens",
            "Het maakt van rubber een thermoplast",
            "Het vervangt waterstof door fluor",
        ],
        0,
        "Daardoor wordt kleverig rubber stevig en elastisch.",
    ),
    sleep(
        "Een polymeer bestaat uit duizenden [[monomeren]]. Bij een [[polyadditie]] gaan dubbele bindingen open. Bij een [[polycondensatie]] komt er telkens water vrij.",
        ["isomeren", "eliminatie"],
        "Het soort monomeer bepaalt welke reactie mogelijk is.",
    ),
    tabel(
        "Klopt dit over recycleren?",
        [
            ("Zuiver gesorteerde kunststof levert betere nieuwe kunststof.", J),
            ("Een thermoharder kan je niet opnieuw smelten.", J),
            ("Alle kunststoffen kan je samen smelten tot goede nieuwe kunststof.", F),
        ],
        "Gemengde kunststoffen geven een zwakker materiaal.",
    ),
    mk(
        "Waarom blijven kleine stukjes kunststof zo lang in zee zitten?",
        [
            "Bacteriën breken de ketens nauwelijks af",
            "Ze lossen op en slaan daarna weer neer",
            "Ze vormen crosslinks met het zeezout",
            "Ze worden telkens opnieuw gepolymeriseerd",
        ],
        0,
        "De stevige ketens worden door bacteriën nauwelijks afgebroken.",
    ),
    inv(
        "Hoeveel koolstofatomen telt het monomeer van polypropeen?",
        ["3", "drie"],
        "Propeen: CH₂=CH–CH₃.",
    ),
    tabel(
        "Waarom kiest men deze kunststof?",
        [
            ("PET voor flessen", "Doorzichtig en sterk"),
            ("PTFE in een pan", "Glad en hittebestendig"),
            ("PS-schuim als verpakking", "Licht en schokdempend"),
        ],
        "Eigenschappen volgen uit de structuur van de ketens en hun zijgroepen.",
        kolommen=["Doorzichtig en sterk", "Glad en hittebestendig", "Licht en schokdempend"],
    ),
    inv(
        "Hoeveel waterstofatomen van etheen zijn vervangen in het monomeer van PTFE?",
        ["4", "vier"],
        "Tetrafluoretheen: CF₂=CF₂.",
    ),
    mk(
        "Waarom gebruikt men voor een tandwiel in een warm toestel liever een thermoharder?",
        [
            "Hij vervormt niet bij warmte",
            "Hij is makkelijker te recycleren dan een thermoplast",
            "Hij veert terug na elke indruk",
            "Hij smelt bij een lagere temperatuur",
        ],
        0,
        "Het netwerk van crosslinks houdt de vorm vast.",
    ),
    tabel(
        "Klopt dit over een polycondensatie?",
        [
            ("Elk monomeer heeft minstens twee reactieve groepen.", J),
            ("Er komt een kleine molecule vrij, zoals water.", J),
            ("Het polymeer weegt evenveel als alle monomeren samen.", F),
        ],
        "Het water dat vrijkomt, zit niet meer in het polymeer.",
    ),
    keuze(
        "Polystyreen heeft een [[*benzeenring|chlooratoom|fluoratoom]] als zijgroep aan de keten.",
        "Het monomeer is fenyletheen of styreen.",
    ),
    sorteer(
        "Is dit een eigenschap van een thermoplast of van een thermoharder?",
        ["Thermoplast", "Thermoharder"],
        [
            ("wordt zacht bij verwarmen", "Thermoplast"),
            ("kan opnieuw gevormd worden", "Thermoplast"),
            ("ontleedt bij sterke verhitting", "Thermoharder"),
            ("bevat een dicht netwerk van bruggen", "Thermoharder"),
        ],
        "Het verschil zit in de crosslinks.",
    ),
    inv(
        "Een PE-keten heeft een molaire massa van 28 000 g/mol. Hoeveel etheenmonomeren (28 g/mol) bevat ze?",
        ["1000", "1 000", "duizend"],
        "28 000 / 28 = 1000.",
    ),
    tabel(
        "Uit welk monomeer maakt men deze kunststof?",
        [
            ("PE", "etheen"),
            ("PS", "fenyletheen"),
            ("PP", "propeen"),
        ],
        "De naam van de kunststof is poly + de naam van het monomeer.",
        kolommen=["etheen", "propeen", "fenyletheen"],
    ),
    open_(
        "Leg uit waarom een thermoplast zacht wordt bij verwarmen en een thermoharder niet.",
        "In een thermoplast liggen de ketens los naast elkaar en worden ze enkel door zwakke krachten bij elkaar gehouden. Bij verwarmen kunnen ze langs elkaar schuiven, zodat het materiaal zacht wordt. In een thermoharder zitten de ketens met heel veel crosslinks aan elkaar vast in een netwerk. Ze kunnen niet schuiven; bij te veel warmte breken de bindingen en ontleedt het materiaal.",
    ),
]
