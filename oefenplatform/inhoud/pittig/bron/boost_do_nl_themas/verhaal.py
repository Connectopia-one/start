"""Verhalen ontleden: verteller, tijd en ruimte — pittig (🚀 Boost doorstroom, Nederlands).

Eigen verhaalfragmenten en vragen strikt binnen nl_verhaal, met een
zelfgetekende spanningsboog."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

SB = Prent("spanningsboog", "De spanningsboog van een verhaal", "een lijn die van links laag langzaam stijgt naar een hoogste punt en daarna snel daalt, met letters A tot D")
SB.lijn(100, 540, 920, 540, DONKER, 3); SB.lijn(100, 540, 100, 80, DONKER, 3)
SB.tekst(510, 590, "verloop van het verhaal", 22); SB.tekst(60, 310, "spanning", 22)
SB.pad("M 110 500 C 300 480 500 330 680 140 C 740 200 790 420 900 470", "none", ROOD, 6)
LET = {"A": (150, 450), "B": (470, 330), "C": (680, 95), "D": (860, 400)}
for t, (x, y) in LET.items():
    SB.letter(x, y, t)
U = "spanningsboog.svg"
Z = {t: Prent.rond(x, y, 36) for t, (x, y) in LET.items()}

FRAGMENT = ("Lees het fragment.\n\n"
            "Ik zag de klink van de deur langzaam naar beneden gaan. Mijn hart bonsde in mijn keel. Niemand wist dat ik hier was, dacht ik. "
            "Buiten in de gang stond mijn broer, met de sleutel die ik al drie dagen kwijt was. Hij grijnsde.\n\n"
            "Drie jaar later lachten we er nog altijd om.")

VRAGEN = [
    klik("Klik op de letter bij de climax: het hoogtepunt van de spanning.", U, [Z["C"]], "Na de climax volgt de ontknoping."),
    klik("Klik op de letter bij de ontknoping.", U, [Z["D"]], "De spanning loopt daar weer af."),
    klik("Klik op de letter waar de spanning wordt opgebouwd, maar het hoogtepunt nog niet bereikt is.", U, [Z["B"]], "De spanningsboog loopt op naar de climax."),
    casus(FRAGMENT, [
        keuze("Het verhaal wordt verteld door een [[*ik-verteller|alwetende verteller|personele zij-verteller]].", "Je leest 'ik'."),
        keuze("In 'Mijn hart bonsde in mijn keel' staat de ik er middenin: een [[*belevende|vertellende]] ik-verteller.", "Hij weet nog niet hoe het afloopt."),
        keuze("'Drie jaar later' is een [[*tijdsprong|flashback|cliffhanger]].", "Een stuk tijd wordt overgeslagen."),
        mk("Waarom weet de lezer niet meteen wie er aan de deur staat?",
           ["de ik kent enkel zijn eigen kant", "de schrijver vergat het gewoon te vertellen", "het verhaal is eigenlijk non-fictie", "de broer is de alwetende verteller hier"],
           0, "Een ik-verteller kan alleen gissen wat anderen doen of denken."),
    ]),
    sorteer("Fictie of non-fictie?", ["fictie", "non-fictie"],
            [("een fabel over een vos en een raaf", "fictie"), ("een biografie van een wielrenner", "non-fictie"), ("een graphic novel over een verzonnen superheld", "fictie"), ("een reportage over de zorg", "non-fictie"), ("een gothic novel", "fictie")],
            "Non-fictie doet uitspraken over de werkelijkheid."),
    koppel("Koppel het begrip aan de uitleg.",
           [("protagonist", "de hoofdpersoon"), ("antagonist", "de tegenstander van de hoofdpersoon"), ("antiheld", "een hoofdpersoon zonder klassieke heldeneigenschappen")],
           ["de verteller die alles weet"],
           "Protagonist betekent: de eerste speler."),
    sorteer("Vlak of rond personage?", ["vlak", "rond"],
            [("een knecht die van begin tot eind de grappige sukkel blijft", "vlak"), ("een meisje dat eerst bang is en op het einde de leiding neemt", "rond"), ("een held met tegenstrijdige eigenschappen", "rond"), ("een boze stiefmoeder die alleen maar boos is", "vlak")],
            "Een rond personage groeit of verandert."),
    sorteer("Kennisvoorsprong of kennisachterstand?", ["kennisvoorsprong", "kennisachterstand"],
            [("Jij ziet de dief achter het gordijn, het personage niet.", "kennisvoorsprong"), ("Het personage weet al wie de dader is, jij nog niet.", "kennisachterstand"), ("Je weet dat de brug zal instorten, de chauffeur niet.", "kennisvoorsprong")],
            "Allebei maken ze spanning."),
    mk("Waarom vinden lezers een antiheld vaak geloofwaardig?",
       ["hij twijfelt en faalt, zoals zij", "hij wint altijd zonder enige moeite", "hij is altijd de tegenstander van iemand", "hij vertelt het verhaal altijd zelf"],
       0, "Een held zonder zwaktes is makkelijk te bewonderen, maar moeilijk om in te geloven."),
    tabel("Klopt dit over spanning?",
          [("Non-fictie kan ook spannend zijn.", J), ("Een cliffhanger breekt af op het spannendste moment.", J), ("Een enjambement hoort bij de spanningsopbouw van een verhaal.", F)],
          "Een enjambement hoort bij poëzie."),
    mk("Je leest twintig bladzijden over één voetbalmatch van negentig minuten. Wat klopt?",
       ["de verteltijd is lang, de vertelde tijd kort", "de verteltijd en de vertelde tijd zijn gelijk", "de vertelde tijd is langer dan de verteltijd", "er is een tijdsprong van negentig minuten"],
       0, "De schrijver vertraagt: daar legt hij de nadruk."),
    keuze("'Twintig jaar gingen voorbij.' Hier is er veel vertelde tijd in [[*weinig|veel]] verteltijd.", "Die twintig jaar zijn blijkbaar niet belangrijk voor het verhaal."),
    sorteer("Flashback, flashforward of tijdsprong?", ["flashback", "flashforward", "tijdsprong"],
            [("'Ze dacht terug aan de zomer toen ze zes was.'", "flashback"), ("'Hij wist toen nog niet dat hij haar nooit meer zou zien.'", "flashforward"), ("'Tien jaar later stond hij weer voor dezelfde deur.'", "tijdsprong")],
            "Alle drie doorbreken ze de chronologie."),
    sorteer("Welke soort ruimte staat hier op de voorgrond?", ["geografisch", "sociaal", "symbolisch", "sfeerscheppend"],
            [("Het verhaal speelt in Brugge, in 1990.", "geografisch"), ("Een verpauperde achterbuurt toont de stand van de personages.", "sociaal"), ("Een muur tussen twee tuinen staat voor de ruzie tussen twee families.", "symbolisch"), ("Een donker, mistig bos in een griezelverhaal.", "sfeerscheppend")],
            "Dezelfde plaats kan meer dan één functie hebben."),
    tabel("Welk vertelperspectief?",
          [("'Ik zag de klink bewegen en mijn hart bonsde.'", "belevende ik-verteller"), ("'Toen wist ik nog niet dat dit mijn laatste zomer daar was.'", "vertellende ik-verteller"), ("'Lies keek naar de deur. Wat wilde hij van haar?'", "personele zij-verteller"), ("'Lies was bang. Ook Tom, aan de andere kant van de stad, kon niet slapen.'", "alwetende verteller")],
          "De alwetende verteller kijkt in het hoofd van alle personages.", ["belevende ik-verteller", "vertellende ik-verteller", "personele zij-verteller", "alwetende verteller"]),
    mk("Waarom kiest een schrijver soms een alwetende verteller?",
       ["om de lezer meer te laten weten", "om het verhaal korter te maken", "omdat een ik-verteller verboden is in fictie", "om enkel de gedachten van één personage te tonen"],
       0, "Zo kan hij kennisvoorsprong opbouwen."),
    keuze("De vos en de raaf is een [[*fabel|biografie|reportage]]: dieren gedragen zich als mensen en het eindigt met een les.", "De les op het einde heet de moraal."),
    keuze("Bij een detective verwacht je een misdaad en een oplossing. Dat hoort bij het [[*genre|vertelperspectief|verhaallijn]].", "Het genre wekt verwachtingen."),
    inv("Hoe noem je het geheel van gebeurtenissen dat een verhaal draagt? Eén woord.", ["verhaallijn", "de verhaallijn"], "De verhaallijn."),
    tabel("Klopt dit over de verteller?",
          [("Een ik-verteller weet altijd wat anderen denken.", F), ("Bij een personele verteller kijk je mee met één personage.", J), ("Chronologisch vertellen volgt de volgorde van de gebeurtenissen.", J)],
          "Een ik-verteller kan alleen gissen."),
    keuze("In een verhaal zoekt een rechercheur een seriemoordenaar. De seriemoordenaar is de [[*antagonist|protagonist|verteller]].", "Hij werkt de hoofdpersoon tegen."),
    keuze("Een rond personage [[*verandert in de loop van het verhaal|blijft altijd hetzelfde|heeft maar één eigenschap]].", "Je leert ook zijn zwakke kanten kennen."),
    keuze("Na de climax volgt de [[*ontknoping|cliffhanger|flashback]].", "De spanning loopt weer af."),
    inv("Hoe noem je het hoogtepunt van de spanning in een verhaal? Eén woord.", ["climax", "de climax", "hoogtepunt"], "De climax."),
    keuze("Een flashback is een terugblik naar iets wat [[*vóór|na]] het verhaalheden gebeurde.", "Hij geeft achtergrond op het moment dat je hem nodig hebt."),
    tabel("Is dit een fictiegenre?",
          [("fabel", J), ("gothic novel", J), ("bijsluiter", F), ("graphic novel", J)],
          "Een bijsluiter is prescriptieve non-fictie."),
    open_("Leg uit waarom kennisvoorsprong de spanning verhoogt. Geef een voorbeeld.",
          "Bij kennisvoorsprong weet de lezer meer dan het personage. Je ziet bijvoorbeeld de dief achter de deur staan terwijl het personage nietsvermoedend binnenkomt. Je ziet het gevaar aankomen en wil bijna roepen dat het personage moet opletten."),
]
