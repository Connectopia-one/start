"""Spieren, beenderen en gewrichten — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_beweging, met een zelfgetekend gewricht en een arm
met biceps en triceps, aangevuld met enkele vragen uit biologie Boost doorstroom."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL
from ..boost_do_bi_themas import spieren as _s

GW = Prent("gewricht-schema", "Schema van een gewricht", "twee botuiteinden met kop en kom, kraakbeen, gewrichtsholte met smeer, kapsel en ligament, met letters A tot F")
BOT = "#f4ecd8"
GW.rect(360, 225, 280, 160, "#fff1a8", "none", 0, 0)                                # gewrichtsholte met smeer
GW.pad("M 352 205 Q 335 305 352 405", "none", DONKER, 4); GW.pad("M 648 205 Q 665 305 648 405", "none", DONKER, 4)   # kapsel
GW.lijn(325, 160, 325, 460, "#c0763a", 10); GW.lijn(675, 160, 675, 460, "#c0763a", 10)   # ligamenten
GW.pad("M 390 40 L 610 40 L 610 250 Q 500 360 390 250 Z", BOT, DONKER, 3)          # kop
GW.pad("M 390 600 L 610 600 L 610 305 Q 500 415 390 305 Z", BOT, DONKER, 3)        # kom
GW.pad("M 396 256 Q 500 352 604 256", "none", "#7fb4d8", 12)                         # kraakbeen op de kop
GW.pad("M 396 311 Q 500 407 604 311", "none", "#7fb4d8", 12)                         # kraakbeen in de kom
LET = {"A": (500, 140), "B": (500, 510), "C": (800, 240), "D": (200, 300), "E": (800, 450), "F": (800, 345)}
for t, (x, y) in LET.items():
    GW.letter(x, y, t)
GW.lijn(778, 240, 600, 262, DONKER, 1); GW.lijn(222, 300, 342, 300, DONKER, 1); GW.lijn(778, 450, 681, 450, DONKER, 1); GW.lijn(778, 345, 560, 330, DONKER, 1)
U = "gewricht-schema.svg"
Z = {t: Prent.rond(x, y, 30) for t, (x, y) in LET.items()}

VRAGEN = [_s.VRAGEN[i] for i in (8, 17, 23)] + [
    klik("Klik op de letter bij de gewrichtskop.", U, [Z["A"]],
         "De kop is het bolle botuiteinde dat in de kom past."),
    klik("Klik op de letter bij de gewrichtskom.", U, [Z["B"]],
         "De kom is het holle botuiteinde."),
    klik("Klik op de letter bij het gladde, veerkrachtige laagje dat schokken opvangt.", U, [Z["C"]],
         "Kraakbeen bedekt de botuiteinden."),
    klik("Klik op de letter bij het deel dat het gewricht afsluit en het smeer binnenhoudt.", U, [Z["D"]],
         "Het gewrichtskapsel."),
    klik("Klik op de letter bij de band die de twee botten samenhoudt.", U, [Z["E"]],
         "Een ligament of gewrichtsband houdt het gewricht stabiel."),
    klik("Klik op de letter bij de plaats van het gewrichtssmeer.", U, [Z["F"]],
         "Het smeer vermindert de wrijving tussen de botten."),
    casus("Sara tilt een volle boodschappentas op door haar elleboog te buigen.", [
        keuze("De spier die de beweging uitvoert, de [[*biceps|triceps]], is de agonist.",
              "De biceps buigt de arm."),
        keuze("Ondertussen [[*ontspant|trekt even hard]] de triceps.",
              "De antagonist laat los terwijl de agonist trekt."),
        keuze("Het ellebooggewricht is een [[*scharniergewricht|kogelgewricht]].",
              "Het buigt in één richting."),
        keuze("De biceps zit met [[*een pees|een ligament]] vast aan het bot.",
              "Een pees verbindt spier en bot."),
    ]),
    tabel("Kogelgewricht of scharniergewricht?",
          [("de schouder", "kogelgewricht"), ("de knie", "scharniergewricht"), ("de heup", "kogelgewricht"), ("de elleboog", "scharniergewricht")],
          "Een kogelgewricht draait alle kanten op.",
          kolommen=["kogelgewricht", "scharniergewricht"]),
    tabel("Rode of witte spiervezel?",
          [("een marathon lopen", "rood"), ("een sprint van honderd meter", "wit"), ("een zware bak één keer optillen", "wit"), ("een uur fietsen", "rood")],
          "Rode vezels houden lang vol met zuurstof, witte geven kort veel kracht.",
          kolommen=["rood", "wit"]),
    koppel("Welk bot hoort bij welk lichaamsdeel?",
           [("het opperarmbeen", "de bovenarm"), ("het dijbeen", "het bovenbeen"), ("het scheenbeen", "het onderbeen"), ("het spaakbeen", "de onderarm")], ["de hand"],
           "Het dijbeen is het langste bot."),
    keuze("Een spier kan enkel [[*trekken|duwen]]; daarom werken spieren in paren.",
          "Voor de tegengestelde beweging is een tweede spier nodig."),
    keuze("Een pees verbindt [[*een spier met een bot|twee botten]]; een ligament verbindt [[*twee botten|een spier met een bot]].",
          "Twee termen die je niet mag verwarren."),
    volgorde("Zet de bouw van een skeletspier van groot naar klein.",
             ["de spier", "de spierbuik met bindweefsel", "een spiervezel"],
             "Veel spiervezels samen vormen de spier."),
    tabel("Klopt dit over spierweefsel?",
          [("Het hart klopt onwillekeurig.", J), ("Glad spierweefsel zit in de darmwand.", J), ("De spieren van je arm werken onwillekeurig.", F), ("Een samentrekkende spier wordt korter en dikker.", J)],
          "Je arm stuur je zelf: willekeurig."),
    mk("Waarom heeft een gewricht kraakbeen en smeer?",
       ["om wrijving en schokken op te vangen", "om de twee botten stevig aan elkaar te lijmen", "om het bloed in het bot aan te maken", "om de spier stevig aan het bot te hechten"], 0,
       "Kraakbeen vangt schokken op, smeer vermindert wrijving."),
    tabel("Is dit een taak van de spieren?",
          [("om te bewegen", J), ("om warmte te maken", J), ("om rechtop te staan", J), ("om bloed te maken", F)],
          "Bloed wordt in het beenmerg gemaakt."),
    inv("Hoeveel spieren heb je minstens nodig om je arm te buigen én te strekken? Een cijfer.", ["2", "twee"],
        "De biceps buigt, de triceps strekt."),
    keuze("Het onderbeen heeft het [[*scheenbeen en het kuitbeen|dijbeen en het spaakbeen]].",
          "Het scheenbeen is het dikste van de twee."),
    tabel("Klopt dit over een kogelgewricht?",
          [("De kop zit in een kom.", J), ("Het draait alle kanten op.", J), ("De knie is er een.", F)],
          "De knie is een scharniergewricht."),
    keuze("Het langste bot van je lichaam is het [[*dijbeen|opperarmbeen|scheenbeen]].",
          "Het loopt van de heup tot de knie."),
    keuze("Een spiervezel is een [[*langgerekte spiercel|bundel pezen|stuk kraakbeen]].",
          "Veel vezels samen vormen de spier."),
    keuze("Een spier krijgt zuurstof en voedingsstoffen via het [[*bloed|gewrichtssmeer|kraakbeen]].",
          "Het bloed voert ook de afvalstoffen af."),
    sorteer("Willekeurig of onwillekeurig?", ["willekeurig", "onwillekeurig"],
            [("je been strekken", "willekeurig"), ("je hart dat klopt", "onwillekeurig"), ("je darmen die voedsel verplaatsen", "onwillekeurig"), ("je hand dichtknijpen", "willekeurig")],
            "Willekeurig stuur je zelf."),
    open_("Leg uit waarom de biceps en de triceps nooit tegelijk even hard trekken als je je arm buigt.",
          "Een spier kan enkel trekken. De biceps trekt om te buigen en de triceps ontspant. Trokken ze allebei even hard, dan bewoog de arm niet.",
          "Agonist en antagonist werken tegengesteld."),
]
