"""Gezondheid bevorderen: preventie, voeding en beweging — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Eigen vragen strikt binnen gz_bevordering, met een zelfgetekende lege
voedingsdriehoek."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

VD = Prent("voedingsdriehoek-leeg", "De voedingsdriehoek zonder woorden", "een omgekeerde driehoek in vier lagen, van breed bovenaan naar smal onderaan, met een rondje ernaast, met letters A tot E")
# omgekeerde driehoek: top y=80 breedte 600 (x 150..750), punt y=560 op x=450
def _x(y):
    t = (y - 80) / 480
    return 150 + 300 * t, 750 - 300 * t
LAGEN = [(80, 200, "#bfe3f5"), (200, 320, "#bfe6b0"), (320, 440, "#f4dfa0"), (440, 560, "#f3c3b0")]
for y1, y2, kleur in LAGEN:
    a1, b1 = _x(y1); a2, b2 = _x(y2)
    VD.pad(f"M {a1:.0f} {y1} L {b1:.0f} {y1} L {b2:.0f} {y2} L {a2:.0f} {y2} Z", kleur, DONKER, 3)
VD.cirkel(870, 470, 70, "#e0e0e0", DONKER, 3)
LET = {"A": (450, 140), "B": (450, 260), "C": (450, 380), "D": (450, 490), "E": (870, 470)}
for t, (x, y) in LET.items():
    VD.letter(x, y, t)
U = "voedingsdriehoek-leeg.svg"
Z = {t: Prent.rond(x, y, 40) for t, (x, y) in LET.items()}

VRAGEN = [
    klik("Klik op de letter bij de plaats van de restgroep.", U, [Z["E"]],
         "De restgroep staat apart, buiten de driehoek: hoe minder, hoe beter."),
    klik("Klik op de letter bij de laag met water: wat je het meest drinkt.", U, [Z["A"]],
         "Water staat bovenaan in de brede laag."),
    klik("Klik op de letter bij de laag die je het minst nodig hebt binnen de driehoek.", U, [Z["D"]],
         "Onderaan, in de smalle punt, staan de dierlijke producten: daarvan eet je weinig."),
    sorteer("Welke preventie is dit?", ["primair", "secundair", "tertiair"],
            [("een vaccin tegen mazelen", "primair"), ("een bevolkingsonderzoek naar borstkanker", "secundair"), ("revalidatie na een hartaanval om herval te voorkomen", "tertiair"), ("niet beginnen met roken", "primair"), ("een gehoortest bij kleuters zonder klachten", "secundair")],
            "Primair voorkomt, secundair spoort vroeg op, tertiair beperkt de gevolgen."),
    tabel("Klopt dit over preventie?",
          [("Primaire preventie komt voor de ziekte er is.", J), ("Bij tertiaire preventie is de ziekte er al.", J), ("Secundaire preventie zoekt een ziekte bij mensen met zware klachten.", F)],
          "Secundaire preventie zoekt bij mensen die nog geen klachten hebben."),
    koppel("Koppel het onderdeel van gezondheidsbevordering aan het voorbeeld.",
           [("ziektepreventie", "een vaccinatie"), ("gezondheidsbescherming", "een rookverbod in cafés"), ("gezondheidspromotie", "een campagne om meer te bewegen")],
           ["een operatie aan de knie"],
           "Genezen hoort niet bij gezondheidsbevordering."),
    mk("Wat is het doel van gezondheidsbevordering?",
       ["de gezondheid verbeteren en beschermen", "zieke mensen zo snel mogelijk genezen", "enkel letten op wat mensen elke dag eten", "dokters minder werk geven in het ziekenhuis"],
       0, "Het gaat niet over genezen."),
    tabel("Is dit een manier om gezondheid te bevorderen?",
          [("een gezonde omgeving maken", J), ("vaardigheden aanleren", J), ("je gedrag aanpassen", J), ("alles aan de dokter overlaten", F)],
          "Er zijn vier manieren: omgeving, vaardigheden, gedrag en bewust omgaan met je gezondheid."),
    sleep("De drie uitgangspunten van de voedingsdriehoek: meer [[plantaardig]] dan dierlijk, zo weinig mogelijk [[lege]] calorieën en [[matig]] je consumptie.",
          ["dierlijk", "volle"],
          "De restgroep staat buiten de driehoek."),
    sorteer("Waar hoort dit?", ["in de driehoek", "restgroep"],
            [("volkorenbrood", "in de driehoek"), ("frisdrank", "restgroep"), ("een appel", "in de driehoek"), ("chips", "restgroep"), ("noten", "in de driehoek")],
            "Snoep, chips en frisdrank zijn lege calorieën."),
    mk("Waarom zijn de calorieën in frisdrank leeg?",
       ["veel energie maar bijna geen vitaminen of vezels", "er zitten helemaal geen calorieën in een blikje frisdrank", "frisdrank is eigenlijk gewoon water met een kleurtje", "de suiker verdwijnt meteen weer uit je lichaam"],
       0, "Lege calorieën geven energie zonder nuttige voedingsstoffen."),
    sorteer("In welke bewegingscategorie valt dit?", ["sedentair gedrag", "licht intensief", "matig intensief", "hoog intensief"],
            [("twee uur gamen in de zetel", "sedentair gedrag"), ("rustig de afwas doen", "licht intensief"), ("stevig wandelen naar school", "matig intensief"), ("een sprint lopen", "hoog intensief")],
            "Bij matig intensief kan je nog praten, bij hoog intensief niet meer."),
    mk("Je fietst naar school. Je ademt sneller, maar je kan nog vlot praten. Hoe intensief beweeg je?",
       ["matig intensief", "hoog intensief", "sedentair", "licht intensief, zonder sneller te ademen"],
       0, "Praten lukt nog: matig intensief."),
    keuze("De bewegingsdriehoek raadt vooral aan om [[*minder lang stil te zitten|enkel in het weekend te sporten|elke dag een uur te sprinten]].",
          "Beweeg zo veel mogelijk, verspreid over de hele dag."),
    tabel("Hoort dit bij een goede slaaphygiëne?",
          [("elke dag een vast slaapuur", J), ("een donkere, koele kamer", J), ("vlak voor het slapen nog een stevige training", F), ("het laatste uur op je gsm scrollen", F)],
          "Een scherm of een late training houdt je wakker."),
    tabel("Hangt de hoeveelheid slaap die je nodig hebt hiervan af?",
          [("de leeftijd", J), ("de kwaliteit van de slaap", J), ("de kleur van je pyjama", F)],
          "Ook het moment van inslapen speelt mee."),
    mk("Waarom is slapen zo belangrijk voor een tiener?",
       ["het lichaam herstelt, groeit en verwerkt wat je leerde", "het lichaam verbruikt dan veel meer energie dan bij het sporten", "je hoeft dan de volgende dag veel minder te eten", "je hersenen staan dan de hele nacht volledig uit"],
       0, "In je slaap verwerken je hersenen wat je die dag leerde."),
    tabel("Moet je je handen zeker wassen?",
          [("voor je gaat koken", J), ("na een toiletbezoek", J), ("na het aaien van een hond", J), ("na het lezen van een boek", F)],
          "Ook na het niezen en voor het eten."),
    mk("Na het tuinieren zitten je handen vol aarde. Wat doe je?",
       ["eerst wassen met water en zeep", "meteen ontsmetten met wat handgel", "afvegen aan een droge keukenhanddoek", "niets, want aarde is niet echt vies"],
       0, "Ontsmetten werkt enkel op schone handen."),
    tabel("Wassen of ontsmetten?",
          [("haalt vuil en kiemen weg", "wassen"), ("doodt de kiemen maar laat vuil liggen", "ontsmetten"), ("werkt enkel op schone handen", "ontsmetten")],
          "Eerst wassen, dan eventueel ontsmetten.", ["wassen", "ontsmetten"]),
    volgorde("Zet de stappen van correct handen wassen in de juiste volgorde.",
             ["handen nat maken en zeep nemen", "palmen, rug, tussen de vingers, duimen en nagels wrijven", "afspoelen", "goed afdrogen"],
             "Vergeet de plaatsen tussen de vingers niet."),
    keuze("Tandplak veroorzaakt gaatjes en [[*tandvleesontsteking|hooikoorts|lege calorieën]].",
          "Poetsen houdt dat tegen."),
    casus("Yusuf (16) zit na school uren te gamen, drinkt elke dag twee blikjes cola en gaat pas om één uur slapen. 's Ochtends is hij moe.", [
        tabel("Wat zou Yusuf helpen?",
              [("water in plaats van cola", J), ("een vast slaapuur", J), ("nog langer gamen om te ontspannen", F)],
              "Minder stilzitten, minder lege calorieën en een vast slaapuur."),
        keuze("Uren gamen in de zetel is [[*sedentair gedrag|matig intensief bewegen|hoog intensief bewegen]].", "Zitten terwijl je wakker bent, met bijna geen energieverbruik."),
        keuze("Een school die cola uit de automaat haalt, doet aan [[*gezondheidsbescherming|tertiaire preventie|secundaire preventie]].", "De omgeving gezonder maken beschermt iedereen."),
    ]),
    tabel("Klopt dit over gezondheidsbevordering?",
          [("Gezondheidsbevordering gaat ook over slaap en hygiëne.", J), ("Schoon drinkwater is een vorm van gezondheidsbescherming.", J), ("Een vaccin is secundaire preventie.", F)],
          "Een vaccin voorkomt de ziekte: primaire preventie."),
    inv("Hoeveel bewegingscategorieën onderscheidt de bewegingsdriehoek? Een getal.", ["4", "vier"], "Sedentair, licht, matig en hoog intensief."),
    keuze("Een kind heeft [[*meer|minder|evenveel]] slaap nodig dan een volwassene.", "De leeftijd bepaalt mee hoeveel slaap je nodig hebt."),
    open_("Leg met een voorbeeld het verschil uit tussen primaire en secundaire preventie.",
          "Primaire preventie voorkomt dat je ziek wordt, zoals een vaccin. Secundaire preventie spoort een ziekte vroeg op bij mensen zonder klachten, zoals een bevolkingsonderzoek naar kanker."),
    inv("Hoe noem je de preventie die de gevolgen van een ziekte zo klein mogelijk houdt? Eén woord.",
        ["tertiaire", "tertiair", "tertiaire preventie"],
        "Tertiaire preventie."),
]
