"""Reactiesnelheid, botsingsmodel en energiediagram — pittig (⚗️ Beyond doorstroom, chemie)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL, assen

# Energiediagram met en zonder katalysator ----------------------------------
ED = Prent("energiediagram-katalysator", "Energiediagram van een reactie, met en zonder katalysator", "een volle kromme die van een hoger niveau links over een hoge top naar een lager niveau rechts gaat, en een stippelkromme met een lagere top; letters A tot E")
X, Y = assen(ED, 0, 10, 0, 100, "reactieverloop", "energie (kJ)", 10, 20, links=130, rechts=900)


def _berg(top):
    pts = []
    for i in range(0, 101):
        t = i / 10
        basis = 40 - 20 * math.tanh((t - 5) / 1.2)
        bult = (top - 40) * math.exp(-((t - 5) ** 2) / 1.6)
        pts.append((X(t), Y(basis + bult)))
    return "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts)


ED.pad(_berg(90), "none", BLAUW, 4)
ED.pad(_berg(65), "none", ORANJE, 3)
ED.svg(f'<path d="{_berg(65)}" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="10 8"/>')
# pijlen
ED.pijl(X(1.6), Y(60), X(1.6), Y(20), DONKER, 2)
ED.lijn(X(1.6), Y(20), X(8.5), Y(20), GRIJS, 1, stippel=True)
ED.lijn(X(1.0), Y(60), X(5.6), Y(60), GRIJS, 1, stippel=True)
ED.pijl(X(5), Y(60), X(5), Y(88), DONKER, 2)
LED = {"A": (X(0.6), Y(68)), "B": (X(5), Y(97)), "C": (X(5.55), Y(74)), "D": (X(1.1), Y(40)), "E": (X(9.2), Y(28))}
for k, (x, y) in LED.items():
    ED.letter(x, y, k)
ED.lijn(X(2.6), Y(12), X(3.4), Y(12), ORANJE, 3)
ED.tekst(X(3.5), Y(12) + 6, "met katalysator", 15, "start")
ED.lijn(X(2.6), Y(5), X(3.4), Y(5), BLAUW, 4)
ED.tekst(X(3.5), Y(5) + 6, "zonder katalysator", 15, "start")
ZED = {k: [Prent.rond(x, y, 24)] for k, (x, y) in LED.items()}
ZED["B"].append(Prent.zone(X(4.5), Y(92), X(5.5) - X(4.5), 30))
ZED["C"].append(Prent.zone(X(5) - 12, Y(88), 24, Y(60) - Y(88)))
ZED["D"].append(Prent.zone(X(1.6) - 12, Y(60), 24, Y(20) - Y(60)))

# Concentratie-tijdgrafiek --------------------------------------------------
CT = Prent("concentratie-tijd", "Concentratie van een reagens en een product tijdens een reactie", "assenstelsel met de tijd in seconden horizontaal en de concentratie verticaal; een dalende en een stijgende kromme, drie punten P, Q en R op de dalende kromme")
X2, Y2 = assen(CT, 0, 100, 0, 1.0, "t (s)", "c (mol/L)", 10, 0.2, links=130, rechts=900)


def _c(t):
    return 0.8 * math.exp(-t / 25)


CT.pad("M " + " L ".join(f"{X2(t):.1f} {Y2(_c(t)):.1f}" for t in range(0, 101)), "none", BLAUW, 4)
CT.pad("M " + " L ".join(f"{X2(t):.1f} {Y2(0.8 - _c(t)):.1f}" for t in range(0, 101)), "none", ORANJE, 4)
CT.tekst(X2(50), Y2(0.17), "reagens", 17, kleur=BLAUW, vet=True)
CT.tekst(X2(70), Y2(0.82), "product", 17, kleur=ORANJE, vet=True)
PCT = {"P": 2, "Q": 25, "R": 75}
for k, t in PCT.items():
    CT.cirkel(X2(t), Y2(_c(t)), 7, GEEL, DONKER, 2)
    CT.letter(X2(t) + 30, Y2(_c(t)) - 28, k)
ZCT = {k: [Prent.rond(X2(t), Y2(_c(t)), 22), Prent.rond(X2(t) + 30, Y2(_c(t)) - 28, 22)] for k, t in PCT.items()}

VRAGEN = [
    klik(
        "Klik op de activeringsenergie van de reactie zonder katalysator.",
        ED.bestand, ZED["C"],
        "Van het niveau van de reagentia tot de top van de volle kromme.",
    ),
    klik(
        "Klik op de pijl die de reactie-energie toont.",
        ED.bestand, ZED["D"],
        "Het verschil tussen producten en reagentia. Hier daalt de energie: exo-energetisch.",
    ),
    met_prent(ED.bestand, tabel(
        "Wat stelt deze letter voor?",
        [
            ("A", "Reagentia"),
            ("B", "Geactiveerd complex"),
            ("E", "Producten"),
        ],
        "Op de top zijn oude bindingen half verbroken en nieuwe half gevormd.",
        kolommen=["Reagentia", "Geactiveerd complex", "Producten"],
    )),
    met_prent(ED.bestand, tabel(
        "Wat verandert er door de katalysator in dit diagram?",
        [
            ("de hoogte van de top", "Verandert"),
            ("de energie van de reagentia", "Blijft gelijk"),
            ("de reactie-energie", "Blijft gelijk"),
            ("de activeringsenergie", "Verandert"),
        ],
        "Een katalysator verlaagt alleen de berg, begin en einde blijven op hun plaats.",
        kolommen=["Verandert", "Blijft gelijk"],
    )),
    met_prent(ED.bestand, inv(
        "Lees af: hoeveel kJ bedraagt de reactie-energie? Gebruik een minteken als er energie vrijkomt.",
        ["-40", "−40", "-40 kJ", "−40 kJ"],
        "Van 60 kJ naar 20 kJ: −40 kJ, exo-energetisch.",
    )),
    klik(
        "Klik op het punt waar de reactie het snelst verloopt.",
        CT.bestand, ZCT["P"],
        "In het begin is de kromme het steilst: daar is de concentratie het hoogst.",
    ),
    met_prent(CT.bestand, tabel(
        "Kijk naar de concentratie-tijdgrafiek. Klopt dit?",
        [
            ("In R verloopt de reactie trager dan in Q.", J),
            ("De product-kromme stijgt even snel als de reagens-kromme daalt.", J),
            ("Na 100 s is alle reagens op.", F),
        ],
        "De kromme nadert nul maar raakt ze hier nog niet. Per mol reagens ontstaat één mol product.",
    )),
    met_prent(CT.bestand, mk(
        "Schat de gemiddelde reactiesnelheid tussen 0 en 25 s.",
        ["Ongeveer 0,02 mol/(L·s)", "Ongeveer 0,5 mol/(L·s)", "Ongeveer 25 mol/(L·s)", "Ongeveer 0,2 mol/(L·s)"],
        0,
        "De concentratie daalt van 0,8 naar ongeveer 0,3 mol/L: 0,5 / 25 = 0,02 mol/(L·s).",
    )),
    tabel(
        "Wordt de reactie sneller of trager?",
        [
            ("een stuk magnesium vervangen door magnesiumpoeder", "Sneller"),
            ("het reactiemengsel afkoelen", "Trager"),
            ("de oplossing verdunnen met water", "Trager"),
            ("een katalysator toevoegen", "Sneller"),
        ],
        "Contactoppervlak, temperatuur, concentratie en katalysator: de vier factoren.",
        kolommen=["Sneller", "Trager"],
    ),
    mk(
        "Waarom heeft een kleine temperatuurstijging zo'n groot effect op de snelheid?",
        [
            "Het deel deeltjes boven de activeringsenergie groeit sterk",
            "De activeringsenergie zelf daalt sterk bij opwarmen",
            "Er ontstaan bij opwarmen meer deeltjes in het mengsel",
            "Het geactiveerd complex verdwijnt bij een hogere temperatuur",
        ],
        0,
        "De Boltzmannverdeling schuift op en wordt breder: veel meer deeltjes hebben genoeg energie.",
    ),
    tabel(
        "Leidt deze botsing tot een reactie?",
        [
            ("genoeg energie en de juiste stand", "Ja"),
            ("genoeg energie maar een verkeerde stand", "Nee"),
            ("de juiste stand maar te weinig energie", "Nee"),
        ],
        "Alleen een effectieve botsing heeft allebei.",
        kolommen=["Ja", "Nee"],
    ),
    casus(
        "Voor de reactie A + B → C meet men de beginsnelheid bij verschillende concentraties. Verdubbelt men [A], dan wordt de snelheid vier keer groter. Verdubbelt men [B], dan blijft de snelheid gelijk.",
        [
            keuze(
                "De reactie is van [[*tweede|eerste|nulde]] orde in A.",
                "2² = 4.",
            ),
            keuze(
                "De reactie is van [[*nulde|eerste|tweede]] orde in B.",
                "De concentratie van B heeft geen invloed: exponent nul.",
            ),
            mk(
                "Welke snelheidsvergelijking past?",
                ["v = k · [A]²", "v = k · [A] · [B]", "v = k · [A]² · [B]", "v = k · [B]²"],
                0,
                "[B]⁰ = 1, dus B valt uit de vergelijking.",
            ),
        ],
    ),
    inv(
        "Wat is de totale orde van een reactie met v = k · [A] · [B]²?",
        ["3", "drie"],
        "1 + 2 = 3.",
    ),
    mk(
        "Bij een eerste orde in A verdrievoudig je [A]. Wat gebeurt er met de snelheid?",
        ["Ze wordt drie keer groter", "Ze wordt negen keer groter", "Ze blijft gelijk", "Ze wordt drie keer kleiner"],
        0,
        "Exponent één: de snelheid volgt de concentratie recht evenredig.",
    ),
    sleep(
        "Een katalysator [[verlaagt]] de activeringsenergie. Daardoor worden [[meer]] botsingen effectief en wordt de snelheidsconstante k [[groter]]. Zelf wordt hij [[niet verbruikt]].",
        ["verhoogt", "minder", "kleiner", "opgebruikt"],
        "De reactie-energie verandert niet.",
    ),
    tabel(
        "Is deze reactie exo- of endo-energetisch?",
        [
            ("de producten liggen lager dan de reagentia", "Exo"),
            ("er moet voortdurend warmte toegevoegd worden", "Endo"),
            ("de omgeving warmt op", "Exo"),
            ("de reactie-energie is positief", "Endo"),
        ],
        "Exo: energie komt vrij en de reactie-energie is negatief.",
        kolommen=["Exo", "Endo"],
    ),
    mk(
        "Een reactie is sterk exo-energetisch maar verloopt bij kamertemperatuur niet merkbaar. Hoe kan dat?",
        [
            "De activeringsenergie is hoog",
            "De reactie-energie is positief",
            "Er is geen geactiveerd complex",
            "De producten liggen hoger dan de reagentia",
        ],
        0,
        "De snelheid hangt af van de hoogte van de berg, niet van hoe diep je eindigt.",
    ),
    koppel(
        "Koppel elk voorbeeld aan de factor die de snelheid beïnvloedt.",
        [
            ("vlees in de koelkast", "temperatuur"),
            ("aanmaakhout in plaats van een blok", "verdelingsgraad"),
            ("een katalysator in de uitlaat van een auto", "katalysator"),
            ("sterker azijnzuur op kalk", "concentratie"),
        ],
        ["kleur van de stof"],
        "Elke factor verandert hoe vaak of hoe hard de deeltjes botsen, of hoe hoog de berg is.",
    ),
    tabel(
        "Klopt dit over een enzym?",
        [
            ("Het is een katalysator in een levend organisme.", J),
            ("Het werkt meestal maar op één soort stof.", J),
            ("Het wordt bij de reactie verbruikt.", F),
        ],
        "De actieve plaats past op één soort molecule, zoals een sleutel in een slot.",
    ),
    volgorde(
        "Zet de stappen van een effectieve botsing in de goede volgorde.",
        [
            "De deeltjes naderen elkaar",
            "Ze botsen met genoeg energie en in de juiste stand",
            "Het geactiveerd complex ontstaat",
            "Nieuwe bindingen vormen de producten",
        ],
        "Op de top van de berg zijn oude bindingen half verbroken.",
    ),
    inv(
        "Bij een reactie daalt [A] van 0,50 naar 0,30 mol/L in 10 s. Wat is de gemiddelde snelheid in mol/(L·s)?",
        ["0,02", "0.02", "0,02 mol/(L·s)"],
        "0,20 / 10 = 0,02 mol/(L·s).",
    ),
    tabel(
        "Klopt dit over de Boltzmannverdeling bij een hogere temperatuur?",
        [
            ("De top van de kromme schuift naar rechts.", J),
            ("De oppervlakte onder de kromme blijft gelijk.", J),
            ("Meer deeltjes hebben een energie boven de activeringsenergie.", J),
            ("De activeringsenergie schuift naar links.", F),
        ],
        "Het aantal deeltjes verandert niet, wel hoe de energie verdeeld is.",
    ),
    inv(
        "Lees af in het energiediagram met katalysator: hoeveel kJ is de activeringsenergie dan ongeveer? Rond af op een tiental.",
        ["10", "10 kJ"],
        "De stippelkromme stijgt van 60 naar ongeveer 65 à 70 kJ: ongeveer 10 kJ in plaats van 30 kJ.",
    ),
    mk(
        "Waarom bewaart men zuurstofwater in een donkere fles?",
        [
            "Licht levert energie om een binding te verbreken",
            "In het donker is de fles beter afgesloten",
            "Licht verhoogt de concentratie van zuurstofwater",
            "Een donkere fles werkt zelf als katalysator",
        ],
        0,
        "Licht kan de ontbinding van waterstofperoxide versnellen.",
    ),
    tabel(
        "Wat is de eenheid van k bij deze orde?",
        [
            ("nulde orde", "mol/(L·s)"),
            ("eerste orde", "1/s"),
            ("tweede orde", "L/(mol·s)"),
        ],
        "De eenheid van k volgt uit v = k · [A]ⁿ, met v in mol/(L·s).",
        kolommen=["mol/(L·s)", "1/s", "L/(mol·s)"],
    ),
    keuze(
        "De snelheidsconstante k wordt [[*groter|kleiner|niet anders]] als je de temperatuur verhoogt.",
        "Meer botsingen hebben dan genoeg energie: k groeit.",
    ),
    sorteer(
        "Werkt deze maatregel via meer botsingen of via meer effectieve botsingen?",
        ["Meer botsingen", "Groter deel effectief"],
        [
            ("de concentratie verhogen", "Meer botsingen"),
            ("fijner verdelen", "Meer botsingen"),
            ("een katalysator toevoegen", "Groter deel effectief"),
            ("de temperatuur verhogen", "Groter deel effectief"),
        ],
        "Temperatuur doet eigenlijk allebei, maar vooral het deel met genoeg energie groeit sterk.",
    ),
    open_(
        "Leg met het botsingsmodel uit waarom een hogere concentratie een reactie sneller maakt.",
        "Bij een hogere concentratie zitten er meer deeltjes in hetzelfde volume. Ze botsen dus vaker met elkaar. Het deel van de botsingen dat effectief is, blijft gelijk, maar omdat er meer botsingen zijn, zijn er per seconde ook meer effectieve botsingen. Daardoor ontstaat er sneller product.",
    ),
]
