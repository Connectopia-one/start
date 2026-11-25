"""Ontwikkeling: de basisbegrippen — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_basisbegrippen: groeien, rijpen en leren, de negen
levensloopfasen, nature, nurture en zelfbepaling, en de ontwikkelingsdomeinen.
Met een zelfgetekende tijdlijn van de levensloop."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, GEEL, BLAUW

LL = Prent("levensloop-leeg", "De levensloop in negen fasen", "een pijl van links naar rechts met negen lege vakjes, letters A tot I")
LL.pijl(40, 330, 965, 330, DONKER, 4)
Z = {}
for i, t in enumerate("ABCDEFGHI"):
    x = 50 + i * 102
    LL.rect(x, 250, 90, 160, LICHTGROEN, DONKER, 12, 2)
    LL.letter(x + 45, 290, t)
    Z[t] = [Prent.zone(x, 250, 90, 160)]
LL.tekst(500, 480, "van de bevruchting tot de oude dag", 22)
U = "levensloop-leeg.svg"

SITUATIE = ("Lees de situatie.\n\n"
            "Lotte is zeven. Ze lijkt sprekend op haar oma en is net als haar mama erg lang. Ze groeit op in een gezin met veel boeken. "
            "Ze kiest zelf om elke avond een verhaaltje voor te lezen aan haar knuffels. Deze zomer leerde ze zwemmen.")

VRAGEN = [
    klik("Bekijk de tijdlijn. Klik op het vakje van de adolescentie.", U, Z["F"], "Prenataal, baby, peuter, kleuter, lagereschoolkind en dan de adolescentie."),
    klik("Klik op het vakje van de kleutertijd.", U, Z["D"], "De kleutertijd komt na de peutertijd."),
    klik("Klik op het vakje van de midden-volwassenheid.", U, Z["H"], "Vroege, midden- en late volwassenheid."),
    klik("Klik op het vakje van de fase waarin nog niemand je ziet.", U, Z["A"], "De prenatale fase loopt van de bevruchting tot de geboorte."),
    sorteer("Groeien, rijpen of leren?", ["groeien", "rijpen", "leren"],
            [("Een peuter wordt drie kilo zwaarder.", "groeien"), ("Een baby kan plots zijn hoofd rechtop houden.", "rijpen"), ("Een kind leert fietsen na veel oefenen.", "leren"), ("Een tiener krijgt bredere schouders.", "groeien"), ("Een kind kent het alfabet nadat de juf het aanleerde.", "leren"), ("Een baby begint vanzelf te brabbelen.", "rijpen")],
            "Groeien is groter worden, rijpen gebeurt vanzelf, leren komt van ervaring."),
    sorteer("Nature, nurture of zelfbepaling?", ["nature", "nurture", "zelfbepaling"],
            [("Een kind heeft dezelfde krullen als zijn papa.", "nature"), ("Een kind spreekt thuis Turks en op school Nederlands.", "nurture"), ("Een meisje kiest zelf om elke dag piano te oefenen.", "zelfbepaling"), ("Een kind heeft de bloedgroep van zijn mama.", "nature"), ("Een kind leert beleefdheid door de opvoeding.", "nurture"), ("Een tiener beslist zelf om voor een andere sport te kiezen.", "zelfbepaling")],
            "Erfelijkheid, omgeving en wat het kind zelf kiest."),
    tabel("Welk ontwikkelingsdomein?",
          [("leren tellen tot honderd", "cognitief"), ("een vriendschap sluiten", "socio-emotioneel"), ("leren veters strikken", "fysiek"), ("begrijpen waarom stelen niet mag", "moreel"), ("ontdekken wie je bent", "persoonlijkheid")],
          "Elk domein kijkt naar een ander stuk van de ontwikkeling.", ["fysiek", "cognitief", "moreel", "socio-emotioneel", "persoonlijkheid"]),
    koppel("Koppel het ontwikkelingsdomein aan wie het beschreef.",
           [("de cognitieve ontwikkeling", "Piaget"), ("de morele ontwikkeling", "Kohlberg"), ("de persoonlijkheidsontwikkeling", "Erikson")],
           ["Lalonde"],
           "Lalonde beschreef de gezondheidsdeterminanten."),
    casus(SITUATIE, [
        keuze("Dat Lotte lang is zoals haar mama, komt door [[*nature|nurture|zelfbepaling]].", "Wat je meekrijgt van je ouders."),
        keuze("Het gezin met veel boeken is [[*nurture|nature|zelfbepaling]].", "Wat de omgeving aanbiedt."),
        keuze("Elke avond zelf kiezen om voor te lezen is [[*zelfbepaling|nature|rijpen]].", "Lotte geeft zelf mee richting aan haar ontwikkeling."),
        keuze("Deze zomer leren zwemmen is vooral [[*leren|groeien|rijpen]].", "Het kwam door oefening en ervaring."),
        keuze("Lotte zit in de [[*midden-kindertijd|adolescentie|prenatale fase]].", "Een kind van de lagere school."),
    ]),
    mk("Waarom is ontwikkeling meer dan groeien?",
       ["ook rijpen en leren horen erbij", "omdat groeien enkel bij baby's gebeurt", "omdat groeien niets met het lichaam te maken heeft", "omdat ontwikkeling alleen over het denken gaat"],
       0, "Ontwikkeling is altijd een combinatie van groeien, rijpen en leren."),
    tabel("Klopt dit over ontwikkeling?",
          [("Rijpen vraagt veel oefening.", F), ("Leren komt door ervaring en oefening.", J), ("Een kind kan niet stappen voor zijn lichaam er klaar voor is.", J), ("Groeien gaat enkel over je hersenen.", F)],
          "Rijpen gebeurt vanzelf; leren vraagt oefening."),
    volgorde("Zet deze levensloopfasen in de juiste volgorde.",
             ["de babytijd", "de peutertijd", "de kleutertijd", "de midden-kindertijd", "de adolescentie"],
             "Na de lagereschoolkindfase volgt de adolescentie."),
    mk("Een baby van zes weken kan nog niet zitten, hoeveel je ook oefent. Waarom?",
       ["zijn lichaam is er nog niet rijp voor", "hij wil gewoon nog niet zitten", "zijn ouders hebben het hem nog niet aangeleerd", "zitten hoort bij de cognitieve ontwikkeling"],
       0, "Zonder rijping helpt oefenen niet."),
    inv("Hoe noem je het deel van de ontwikkeling waarbij het lichaam vanzelf klaar wordt voor een volgende stap? Eén woord.", ["rijpen", "rijping", "het rijpen"], "Rijpen."),
    keuze("Nurture staat voor alles wat de [[*omgeving|erfelijkheid|leeftijd]] aanbrengt.", "Opvoeding, school, vrienden en cultuur."),
    mk("Welk voorbeeld toont zelfbepaling?",
       ["een kind dat zelf kiest om bij de scouts te gaan", "een kind met blauwe ogen zoals zijn vader", "een kind dat Frans leert van zijn grootouders in Frankrijk", "een kind dat in één zomer vijf centimeter groeit"],
       0, "Bij zelfbepaling geeft het kind zelf richting."),
    tabel("Hoort deze fase bij de kindertijd?",
          [("de peutertijd", J), ("de vroege volwassenheid", F), ("de babytijd", J), ("de late volwassenheid", F), ("de kleutertijd", J)],
          "De volwassenheid heeft drie fasen."),
    keuze("Leren omgaan met boosheid hoort bij de [[*socio-emotionele|fysieke|cognitieve]] ontwikkeling.", "Omgaan met emoties is socio-emotioneel."),
    sleep("Groter worden heet [[groeien]], vanzelf klaar worden heet [[rijpen]] en veranderen door ervaring heet [[leren]]. Wat je erft, heet [[nature]]; wat de omgeving aanbrengt, heet [[nurture]].",
          ["zelfbepaling"],
          "Zelfbepaling is wat het kind zelf kiest."),
    mk("Eeneiige tweelingen groeien op in verschillende gezinnen en worden heel verschillend. Wat toont dat?",
       ["de omgeving speelt mee in de ontwikkeling", "erfelijkheid speelt helemaal geen rol bij mensen", "tweelingen hebben nooit dezelfde erfelijkheid", "rijpen gebeurt bij elke tweeling op een andere manier"],
       0, "Zelfde nature, andere nurture: dan zie je wat de omgeving doet."),
    tabel("Hoort dit bij de ontwikkeling zelf?",
          [("groeien", J), ("verhuizen naar een andere stad", F), ("rijpen", J), ("van school veranderen", F), ("leren", J)],
          "Verhuizen kan invloed hebben, maar is zelf geen deel van de ontwikkeling."),
    keuze("Een kind van vier dat graag doet alsof, zit in de [[*kleutertijd|peutertijd|babytijd]].", "Na de peutertijd komt de kleutertijd."),
    mk("Welke fase volgt meteen op de babytijd?",
       ["de peutertijd", "de kleutertijd", "de prenatale fase", "de midden-kindertijd"],
       0, "Baby, peuter, kleuter."),
    keuze("Een vrouw van vijfenvijftig zit in de [[*midden-volwassenheid|vroege volwassenheid|adolescentie]].", "De volwassenheid heeft een vroege, een midden- en een late fase."),
    tabel("Klopt dit over nature en nurture?",
          [("Nature is wat je meekrijgt van je ouders.", J), ("Opvoeding hoort bij nature.", F), ("Vrienden en school horen bij nurture.", J), ("Een kind heeft zelf geen invloed op zijn ontwikkeling.", F)],
          "Zelfbepaling is de derde factor."),
    open_("Kies een vaardigheid die je zelf hebt, zoals fietsen of zwemmen. Leg uit welke rol groeien, rijpen en leren erin speelden.",
          "Fietsen: ik moest groot genoeg zijn om de pedalen te halen (groeien), mijn evenwicht moest klaar zijn (rijpen) en ik heb veel geoefend met mijn papa (leren)."),
]
