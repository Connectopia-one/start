"""Welzijnswetenschappen: het ademhalingsstelsel — pittig
(🌍 Beyond doorstroom, natuurwetenschappen).

Eigen vragen en een eigen prent van een spirogram met getallen: luchtwegen
en longen, in- en uitademing, gaswisseling, transport van O₂ en CO₂,
longvolumes en aandoeningen.
"""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, BLAUW, assen

# Een spirogram met schaal ------------------------------------------------------------
SG = Prent("spirogram-getallen", "Spirogram van een leerling", "een spirogram: volume in de longen (liter, 0 tot 6) tegen de tijd (s, 0 tot 20); rustige ademhaling tussen 2,4 en 2,9 liter, dan een diepe inademing tot 5,0 liter en een krachtige uitademing tot 1,2 liter; een stippellijn op 1,2 liter; vier pijlen P, Q, R, S")
X, Y = assen(SG, 0, 20, 0, 6, "tijd (s)", "volume in de longen (L)", 2, 1, links=110, rechts=820)


def _v(t):
    if t <= 10:
        return 2.65 - 0.25 * math.cos(2 * math.pi * t / 2.5)
    if t <= 12:
        return 2.4 + (5.0 - 2.4) * (t - 10) / 2
    if t <= 15:
        return 5.0 - (5.0 - 1.2) * (t - 12) / 3
    if t <= 17:
        return 1.2 + (2.4 - 1.2) * (t - 15) / 2
    return 2.65 - 0.25 * math.cos(2 * math.pi * (t - 17) / 2.5)


pts = " ".join(f"{X(t / 10):.1f},{Y(_v(t / 10)):.1f}" for t in range(0, 201))
SG.svg(f'<polyline points="{pts}" fill="none" stroke="{BLAUW}" stroke-width="4"/>')
SG.lijn(X(0), Y(1.2), X(20), Y(1.2), DONKER, 2, True)
for (x, y1, y2, k) in ((850, 2.4, 2.9, "P"), (850, 2.9, 5.0, "Q"), (900, 1.2, 2.4, "R"), (900, 0, 1.2, "S")):
    SG.lijn(x, Y(y1), x, Y(y2), DONKER, 3)
    SG.lijn(x - 10, Y(y1), x + 10, Y(y1), DONKER, 3)
    SG.lijn(x - 10, Y(y2), x + 10, Y(y2), DONKER, 3)
    SG.letter(x + 40 if k in "PQ" else x + 45, (Y(y1) + Y(y2)) / 2, k)
ZS = {
    "P": [Prent.zone(835, Y(2.9) - 6, 80, Y(2.4) - Y(2.9) + 12)],
    "Q": [Prent.zone(835, Y(5.0), 80, Y(2.9) - Y(5.0) - 6)],
    "R": [Prent.zone(880, Y(2.4), 90, Y(1.2) - Y(2.4))],
    "S": [Prent.zone(880, Y(1.2), 90, Y(0) - Y(1.2))],
}

EIGEN = [
    klik("Klik op het volume dat bij een rustige ademhaling telkens in en uit gaat.", SG.bestand, ZS["P"],
         "Dat is het ademvolume, bij deze leerling ongeveer een halve liter."),
    klik("Klik op de lucht die ook na de krachtigste uitademing in de longen achterblijft.", SG.bestand, ZS["S"],
         "Het restvolume kan je niet uitademen. Een spirometer meet het daarom niet rechtstreeks."),
    klik("Klik op de lucht die je na een gewone uitademing nog extra kan uitblazen.", SG.bestand, ZS["R"],
         "Dat is het aanvullend of reservevolume bij uitademing."),
    met_prent(SG.bestand, inv("Lees het ademvolume af, in liter.", ["0,5", "0.5", "0,5 L", "0,5 liter"],
              "De rustige ademhaling gaat op en neer tussen 2,4 en 2,9 liter.")),
    met_prent(SG.bestand, inv("Hoe groot is de vitale capaciteit van deze leerling, in liter?", ["3,8", "3.8", "3,8 L", "3,8 liter"],
              "Van de diepste inademing (5,0 L) tot de krachtigste uitademing (1,2 L): 5,0 min 1,2 is 3,8 liter.")),
    met_prent(SG.bestand, inv("Hoe groot is het complementair volume, in liter?", ["2,1", "2.1", "2,1 L", "2,1 liter"],
              "Van het einde van een gewone inademing (2,9 L) tot de diepste inademing (5,0 L).")),
    met_prent(SG.bestand, tabel("Kijk naar het spirogram. Klopt dit?", [
        ("De totale longcapaciteit is 5,0 liter.", J),
        ("Q en P samen horen bij de vitale capaciteit.", J),
        ("S hoort bij de vitale capaciteit.", F),
        ("Bij een rustige ademhaling gebruikt de leerling meer dan de helft van zijn longvolume.", F),
    ], "Vitale capaciteit is P + Q + R. De totale longcapaciteit is de vitale capaciteit plus het restvolume S.")),
    casus(
        "Lotte (16) heeft astma. Tijdens een aanval hoort ze zichzelf piepen en krijgt ze "
        "moeilijk lucht uit haar longen. Haar vriend begint van de schrik heel snel en "
        "diep te ademen en krijgt tintelende vingers.",
        [
            mk("Wat gebeurt er in Lottes longen tijdens de aanval?",
               ["De bronchiolen vernauwen en zwellen op",
                "De longblaasjes vullen zich met bloed uit de haarvaten",
                "Het middenrif verlamt en kan niet meer samentrekken",
                "De luchtpijp valt dicht omdat de kraakbeenringen breken"], 0,
               "Door de vernauwde, gezwollen bronchiolen met extra slijm gaat vooral uitademen moeilijk."),
            keuze("Haar vriend [[*hyperventileert|heeft astma|heeft mucoviscidose]]: hij ademt te veel CO₂ uit.",
                  "Door te snel en te diep te ademen daalt het CO₂ in het bloed, met tintelingen en duizeligheid als gevolg."),
            tabel("Klopt dit over astma en andere longziekten?", [
                ("Astma is besmettelijk.", F),
                ("Bij een astma-aanval helpt een puffer die de bronchiolen verwijdt.", J),
                ("Mucoviscidose is een erfelijke ziekte met taai slijm.", J),
            ], "Astma en mucoviscidose zijn niet besmettelijk."),
        ],
    ),
    volgorde("Zet de delen in de volgorde waarin ingeademde lucht ze passeert.", [
        "neusholte", "keelholte", "strottenhoofd", "luchtpijp", "bronchiën", "bronchiolen", "longblaasjes",
    ], "Pas in de longblaasjes gebeurt de gaswisseling."),
    volgorde("Hoe verloopt een inademing? Zet de stappen van spier tot luchtstroom op volgorde.", [
        "middenrif en tussenribspieren trekken samen",
        "de borstholte wordt groter",
        "de druk in de longen daalt onder de buitenluchtdruk",
        "lucht stroomt naar binnen",
    ], "De longen hebben zelf geen spieren; ze volgen de borstkas via de pleuraholte."),
    tabel("Klopt dit over de bouw van de longblaasjes?", [
        ("Ze hebben samen een enorm groot oppervlak.", J),
        ("Hun wand is één cellaag dik.", J),
        ("Ze zijn omgeven door een net van haarvaten.", J),
        ("Ze hebben kraakbeenringen om open te blijven.", F),
    ], "Kraakbeenringen zitten in de luchtpijp en de bronchiën."),
    sorteer("Hoort dit bij de inademing of bij een rustige uitademing?", ["Inademing", "Rustige uitademing"], [
        ["het middenrif trekt samen en wordt platter", "Inademing"],
        ["de borstkas veert vanzelf terug", "Rustige uitademing"],
        ["de tussenribspieren tillen de ribben op", "Inademing"],
        ["het volume van de borstholte wordt kleiner", "Rustige uitademing"],
    ], "Een rustige uitademing is passief: de spieren ontspannen."),
    mk("Wat drijft de zuurstof van het longblaasje naar het bloed in het haarvat?",
       ["De partiële druk van O₂ is er hoger dan in het bloed",
        "Het hart zuigt zuurstof actief uit de longblaasjes aan",
        "De trilharen duwen zuurstof door de wand van het longblaasje",
        "Hemoglobine kruipt door de wand naar de lucht in het blaasje"], 0,
       "Gassen diffunderen van een hoge naar een lage partiële druk."),
    tabel("Laat hemoglobine hier zuurstof makkelijker los?", [
        ("in een hardwerkende spier die warm is", J),
        ("waar veel CO₂ is", J),
        ("waar de pH laag is", J),
        ("in de longblaasjes met veel zuurstof", F),
    ], "Warmte, CO₂ en een lage pH verlagen de zuurstofaffiniteit: precies waar de weefsels zuurstof nodig hebben."),
    keuze("In de longblaasjes verschuift het evenwicht deoxyhemoglobine + O₂ ⇌ oxyhemoglobine naar [[*rechts|links]].",
          "Veel zuurstof duwt het evenwicht naar oxyhemoglobine."),
    koppel("Koppel elke vorm van CO₂-transport aan zijn aandeel.", [
        ["als waterstofcarbonaat in het plasma", "het grootste deel"],
        ["gebonden aan hemoglobine", "een kleiner deel"],
        ["gewoon opgelost in het plasma", "het kleinste deel"],
    ], ["gebonden aan albumine in de lymfe"], "Het meeste CO₂ reist als waterstofcarbonaat."),
    koppel("Koppel elk deel aan zijn taak.", [
        ["neusholte", "verwarmt, bevochtigt en filtert de lucht"],
        ["strottenklepje", "sluit het strottenhoofd af bij het slikken"],
        ["trilhaarepitheel", "voert slijm met stof naar de keel"],
        ["pleuraholte", "laat de longen de borstkas volgen"],
    ], ["longhilus maakt slijm aan"], "Elk deel beschermt of ondersteunt de luchtwegen."),
    sleep("De rechterlong heeft [[drie]] longkwabben, de linkerlong [[twee]], want aan de linkerkant ligt ook het hart.",
          ["vier", "één"], "Bronchus, bloedvaten en zenuwen gaan de long binnen via de longhilus."),
    mk("Een roker hoest elke ochtend slijm op. Wat is daarvan de oorzaak?",
       ["Rook beschadigt de trilharen",
        "Rook doet de kraakbeenringen in de luchtpijp oplossen",
        "Rook laat de longblaasjes extra slijm aanmaken om zuurstof te binden",
        "Rook vergroot het restvolume tot de longen overlopen"], 0,
       "Zonder werkende trilharen blijft het slijm liggen en moet het opgehoest worden."),
    tabel("Kan dit de vitale capaciteit beïnvloeden?", [
        ("leeftijd", J),
        ("lichaamslengte", J),
        ("regelmatig sporten", J),
        ("bloedgroep", F),
    ], "Training versterkt de ademhalingsspieren; grote mensen hebben grotere longen."),
    met_prent(SG.bestand, inv("Hoeveel keer ademt de leerling rustig in per minuut, als je het ritme van de eerste 10 seconden aanhoudt?",
              ["24"], "Elke 2,5 seconde een ademhaling: 60 gedeeld door 2,5 is 24.")),
    klik("Klik op het volume dat je na een gewone inademing nog bij kan inademen.", SG.bestand, ZS["Q"],
         "Dat is het complementair volume of reservevolume bij inademing."),
    tabel("Hoort dit bij de ribademhaling of bij de buikademhaling?", [
        ("de tussenribspieren tillen de ribben op", "ribademhaling"),
        ("het middenrif trekt samen en duwt de buikorganen omlaag", "buikademhaling"),
        ("de buik bolt bij het inademen naar voren", "buikademhaling"),
    ], "Bij de buik- of middenrifademhaling werkt vooral het middenrif.", kolommen=["ribademhaling", "buikademhaling"]),
    keuze("De ribben die met hun eigen kraakbeen aan het borstbeen vastzitten, heten de [[*ware ribben|valse ribben|zwevende ribben]].",
          "Valse ribben hangen onrechtstreeks aan het borstbeen, zwevende ribben helemaal niet."),
    mk("Waarom stikt iemand met een lek in de pleuraholte bijna aan die kant?",
       ["De long volgt de borstkas niet meer en klapt samen",
        "Het middenrif scheurt mee en kan niet meer samentrekken",
        "De luchtpijp sluit zich af door de kraakbeenringen",
        "De longaders lopen vol lucht in plaats van bloed"], 0,
       "Het vocht in de pleuraholte houdt de long tegen de borstwand. Lucht ertussen verbreekt dat."),
    tabel("Klopt dit over de luchtwegen?", [
        ("Het strottenhoofd ligt tussen keelholte en luchtpijp.", J),
        ("In het strottenhoofd zitten de stembanden.", J),
        ("De bronchiën nemen zuurstof op in het bloed.", F),
    ], "Bronchiën geleiden de lucht; de gaswisseling gebeurt enkel in de longblaasjes."),
    sleep("Hoe groter de [[zuurstofaffiniteit]] van hemoglobine, hoe vaster het zuurstof [[vasthoudt]].",
          ["vitale capaciteit", "loslaat"], "In de weefsels daalt de affiniteit, zodat zuurstof vrijkomt."),
    open_("Leg uit hoe zuurstof van de longblaasjes tot in een spiercel komt en waarom het daar loslaat.",
          "In de longblaasjes is de partiële druk van zuurstof hoog, dus diffundeert zuurstof naar het bloed en bindt het aan hemoglobine. Het bloed brengt oxyhemoglobine naar de spier. Daar is weinig zuurstof, veel CO₂, een lagere pH en meer warmte, waardoor hemoglobine de zuurstof loslaat en die naar de cel diffundeert."),
]

VRAGEN = EIGEN
