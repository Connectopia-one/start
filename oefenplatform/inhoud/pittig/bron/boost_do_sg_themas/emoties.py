"""Emoties: componenten en functies — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_emoties: wat emoties zijn, de drie
componenten, de drie functies en de invloed op het gedrag. Met een
zelfgetekend tafereel."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, ORANJE

HD = Prent("schrik-voor-hond", "Lina schrikt van een blaffende hond", "een meisje dat achteruit stapt voor een hond, met letters A tot D")
# hond links
HD.ellips(200, 430, 90, 45, ORANJE, DONKER, 3); HD.cirkel(115, 380, 40, ORANJE, DONKER, 3)
HD.pad("M 95 350 L 85 310 L 115 345 Z", ORANJE, DONKER, 2); HD.cirkel(102, 372, 5, DONKER, DONKER, 1)
HD.pad("M 80 395 Q 95 410 115 398", "none", DONKER, 3)
for x in (150, 250):
    HD.rect(x - 10, 465, 18, 60, ORANJE, DONKER, 4, 2)
HD.tekst(220, 335, "Waf!", 30, kleur=DONKER, vet=True)
# meisje rechts
HD.cirkel(600, 190, 55, GRIJS, DONKER, 3)
HD.cirkel(582, 180, 9, "#ffffff", DONKER, 2); HD.cirkel(618, 180, 9, "#ffffff", DONKER, 2)
HD.ellips(600, 215, 12, 15, DONKER, DONKER, 1)
HD.rect(555, 250, 90, 160, "#9ec7e6", DONKER, 14, 3)
HD.pad("M 575 300 c -12 -16 -36 -4 -24 14 l 24 22 l 24 -22 c 12 -18 -12 -30 -24 -14 Z", ROOD, DONKER, 2)
HD.lijn(555, 270, 500, 230, DONKER, 8); HD.lijn(645, 270, 700, 230, DONKER, 8)
HD.lijn(580, 410, 600, 525, DONKER, 9); HD.lijn(620, 410, 680, 515, DONKER, 9)
for dy in (0, 16, 32):
    HD.lijn(520, 485 + dy, 555, 485 + dy, DONKER, 2)
# gedachtewolk
HD.pad("M 760 120 q -20 -45 30 -55 q 25 -40 80 -15 q 60 -10 60 40 q 30 35 -20 55 q -40 25 -90 5 q -60 10 -60 -30 Z", "#ffffff", DONKER, 3)
HD.tekst(845, 110, "Die bijt mij!", 22)
HD.cirkel(705, 175, 9, "#ffffff", DONKER, 2); HD.cirkel(680, 200, 6, "#ffffff", DONKER, 2)
LET = {"A": (520, 320), "B": (600, 120), "C": (930, 60), "D": (750, 545)}
for t, (x, y) in LET.items():
    HD.letter(x, y, t)
U = "schrik-voor-hond.svg"
Z = {"A": [Prent.zone(540, 270, 70, 80)], "B": [Prent.zone(540, 120, 120, 130)], "C": [Prent.zone(730, 40, 230, 160)], "D": [Prent.zone(500, 410, 280, 140)]}

TOETS = ("Lees het verhaal.\n\n"
         "Jens zit voor zijn wiskundetoets. Zijn handen zweten en zijn maag draait. « Dit ga ik nooit kunnen, » denkt hij. Hij leest de eerste vraag drie keer en snapt ze niet, al kende hij die oefening gisteren nog. "
         "Hij ademt een paar keer diep in en uit, zegt zachtjes tegen zichzelf « ik ben zenuwachtig, dat mag », en begint aan de vraag die hij het best kent.")

VRAGEN = [
    klik("Bekijk het tafereel. Klik op de letter bij de fysiologische component van Lina's schrik.", U, Z["A"], "Haar hart klopt sneller: het lichaam reageert vanzelf."),
    klik("Klik op de letter bij de mentale component.", U, Z["C"], "De gedachte bij de emotie: die bijt mij."),
    klik("Klik op de letter bij de gedragscomponent.", U, Z["D"], "Wat je zichtbaar doet: achteruitstappen."),
    klik("Iemand die voorbijkomt, ziet meteen dat Lina bang is. Klik op de letter bij wat haar emotie aan anderen laat weten.", U, Z["B"], "Je gezicht verraadt een emotie: de functie communiceren."),
    casus(TOETS, [
        sorteer("Welke component van de emotie zie je?", ["fysiologisch", "mentaal", "gedrag"],
                [("zwetende handen", "fysiologisch"), ("'Dit ga ik nooit kunnen.'", "mentaal"), ("Hij begint aan de vraag die hij het best kent.", "gedrag"), ("Zijn maag draait.", "fysiologisch")],
                "Lichaam, gedachte en wat je zichtbaar doet."),
        mk("Waarom snapt Jens een oefening niet die hij gisteren kende?",
           ["angst neemt ruimte in zijn werkgeheugen", "hij heeft de oefening gisteren gewoon niet goed gemaakt", "zijn emotie werkt altijd in zijn voordeel", "de toets was anders opgesteld dan alle vorige toetsen"],
           0, "Sterke emoties kleuren het denken."),
        keuze("Jens zegt 'ik ben zenuwachtig, dat mag'. Hij [[*benoemt zijn emotie|onderdrukt zijn emotie|negeert zijn emotie]].", "Benoemen maakt een emotie hanteerbaar."),
        keuze("Diep in- en uitademen helpt, want de fysiologische component is [[*niet rechtstreeks|wel volledig]] te sturen, maar je ademhaling wel.", "Zo help je je lichaam rustiger worden."),
    ]),
    koppel("Koppel de functie van een emotie aan het voorbeeld.",
           [("waarschuwen", "je springt opzij voor een auto"), ("communiceren", "een baby huilt en zijn moeder komt"), ("aanpassen", "je praat zachter omdat je collega boos kijkt")],
           ["je groeit tien centimeter"], "Drie functies."),
    tabel("Klopt dit over emoties?",
          [("Alle emoties zijn onaangenaam.", F), ("Een emotie duurt korter dan een stemming.", J), ("Er bestaan goede en slechte emoties.", F), ("Emoties hebben een nuttige functie.", J)],
          "Aangenaam of onaangenaam, niet goed of slecht."),
    mk("Iemand lacht op een feest, maar voelt zich vanbinnen verdrietig. Welke componenten botsen hier?",
       ["gedrag en mentaal", "fysiologisch en waarschuwen", "communiceren en aanpassen", "de basisemoties onderling"],
       0, "Het gedrag toont iets anders dan de beleving."),
    keuze("Schaamte en trots verschijnen [[*later|eerder]] dan blijdschap en angst, want ze vragen een besef van jezelf.", "Ze horen niet bij de eerste emoties van een baby."),
    tabel("Is dit een basisemotie?",
          [("blijdschap", J), ("angst", J), ("schaamte", F), ("woede", J), ("verdriet", J)],
          "Schaamte vraagt een besef van jezelf."),
    keuze("Een emotie onderdrukken is [[*niet hetzelfde als|hetzelfde als]] ze reguleren.", "Reguleren is erkennen en er iets mee doen."),
    mk("Waarom raadt men aan een belangrijke beslissing niet te nemen als je heel boos bent?",
       ["boosheid kleurt hoe je afweegt", "omdat boze mensen geen enkele beslissing kunnen nemen", "omdat woede geen echte emotie is", "omdat beslissingen altijd beter zijn als je moe bent"],
       0, "Boos of bang weeg je risico's anders af."),
    keuze("Angst en opwinding voor een wedstrijd lijken lichamelijk op elkaar: in beide gevallen [[*klopt je hart sneller|word je slaperig|daalt je hartslag]].", "Het lichaam reageert bijna gelijk."),
    sorteer("Welke functie van de emotie zie je?", ["waarschuwen", "communiceren", "aanpassen"],
            [("Je ruikt rook en schrikt wakker.", "waarschuwen"), ("Je vriendin ziet aan je gezicht dat je blij bent.", "communiceren"), ("Je merkt dat je moeder moe is en vraagt niets meer.", "aanpassen")],
            "Emoties zijn een systeem, geen storing."),
    keuze("Een kind leert dat het boos mag roepen, maar niet mag slaan. Het gevoel mag er zijn, het [[*gedrag|lichaam|denken]] heeft grenzen.", "Dat is emoties sturen."),
    inv("Hoe heet de component van een emotie die over wat je lichaam doet gaat? Eén woord.", ["fysiologisch", "fysiologische", "de fysiologische"], "Hartslag, zweten, spierspanning."),
    tabel("Klopt dit over emoties en cultuur?",
          [("De basisemoties zijn overal hetzelfde.", J), ("Hoe openlijk je ze toont, verschilt per cultuur.", J), ("In sommige culturen bestaat geen angst.", F)],
          "Het tonen verschilt, niet het voelen."),
    keuze("Iemand die geen angst kent, loopt meer gevaar. Dat toont de [[*waarschuwende|communicerende|aanpassende]] functie.", "Zonder dat alarm merk je gevaar te laat."),
    sleep("Een emotie heeft een [[fysiologische]] component, een [[mentale]] component en een [[gedragscomponent]].",
          ["muzikale", "erfelijke"], "Ze treden meestal samen op."),
    mk("Een verpleegkundige ziet aan het gezicht van een patiënt dat hij pijn heeft, nog voor hij iets zegt. Waarom helpt dat?",
       ["ze kan haar zorg afstemmen", "dan hoeft ze zelf geen emoties meer te voelen", "dan hoeft ze de patiënt niets meer te vragen", "dan weet ze wat de patiënt morgen zal doen"],
       0, "Emoties lezen hoort bij de sociale ontwikkeling."),
    keuze("Een baby toont al emoties [[*voor|pas nadat]] hij kan spreken.", "Hij huilt, lacht en schrikt."),
    keuze("Een emotie [[*komt op door iets en gaat weer weg|blijft altijd aanwezig|heeft nooit een aanleiding]].", "Een stemming hangt langer over een dag heen."),
    tabel("Kan een emotie dit doen met je gedrag?",
          [("sturen wat je doet", J), ("een beslissing versnellen", J), ("kleuren wat je onthoudt", J), ("je lengte veranderen", F)],
          "Emoties sturen gedrag en denken."),
    mk("Waarom helpt het om een kleuter te laten zeggen 'ik ben boos'?",
       ["benoemen helpt sturen", "zo vergeet de kleuter meteen dat hij boos was", "zo wordt de kleuter nooit meer boos", "zo leert hij zijn emoties te verbergen"],
       0, "Benoemen maakt een emotie hanteerbaar."),
    keuze("De functie [[*aanpassen|waarschuwen|communiceren]] zorgt dat je je reactie afstemt op de situatie.", "Een emotie stuurt je gedrag in de situatie."),
    inv("Een stemming duurt lang. Hoe noem je de kortdurende reactie die opkomt door iets? Eén woord.", ["emotie", "een emotie"], "Een emotie komt en gaat."),
    open_("Beschrijf een situatie waarin je bang was en benoem de drie componenten van die emotie en haar functie.",
          "Bijvoorbeeld: ik stak de straat over en een fietser kwam plots aan. Fysiologisch: mijn hart bonsde. Gedrag: ik sprong terug op de stoep. Mentaal: ik dacht 'die rijdt mij omver'. De functie was waarschuwen: de angst liet me sneller reageren dan ik kon nadenken."),
]
