"""Waar wonen de mensen? — pittig (🚀 Boost, aardrijkskunde).

Eigen vragen strikt binnen ak_wonen, met een zelfgetekende kaart van een
verzonnen land om op te klikken. ALG geldt voor doorstroom en dubbele
finaliteit; DO_ALLEEN gaat over de HDI (enkel doorstroom), DF_ALLEEN over de
scholingsgraad en de beïnvloedende factoren (enkel dubbele finaliteit)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, BLAUW, DONKER, GRIJS

# Verzonnen land met zes streken en een legende ---------------------------------
KLEUR = ["#f3ead2", "#e3c98d", "#c98f45", "#8a4f1d"]
LAND = Prent("land-dichtheid", "Bevolkingsdichtheid van het land Veldaria", "verzonnen land met zes streken in vier kleurklassen, een rivier met delta, bergen in het noorden en een legende")
STREKEN = {  # letter: (pad, klasse, labelpositie)
    "A": ("M 120 90 L 420 90 L 400 230 L 130 250 Z", 0, (260, 165)),
    "B": ("M 420 90 L 700 90 L 690 220 L 400 230 Z", 0, (550, 160)),
    "C": ("M 130 250 L 400 230 L 410 400 L 150 420 Z", 1, (270, 330)),
    "D": ("M 400 230 L 690 220 L 700 390 L 410 400 Z", 2, (550, 310)),
    "E": ("M 150 420 L 410 400 L 400 560 L 170 560 Z", 1, (280, 490)),
    "F": ("M 410 400 L 700 390 L 690 560 L 400 560 Z", 3, (550, 480)),
}
for t, (d, k, (lx, ly)) in STREKEN.items():
    LAND.pad(d, KLEUR[k], DONKER, 2)
for x in (180, 240, 300, 480, 560, 630):
    LAND.pad(f"M {x-25} 150 L {x} 110 L {x+25} 150 Z", "#ffffff", DONKER, 1)
LAND.pad("M 545 95 C 560 200 520 300 560 400 C 590 470 600 520 640 560", "none", BLAUW, 6)
LAND.pad("M 640 560 L 600 560 M 640 560 L 680 560 M 640 560 L 650 520", "none", BLAUW, 4)
LAND.tekst(745, 585, "zee", 18, kleur=BLAUW)
for t, (d, k, (lx, ly)) in STREKEN.items():
    LAND.letter(lx - 60 if t in "DF" else lx, ly, t)
LAND.tekst(760, 110, "inwoners per km²", 16, "start", vet=True)
for i, tt in enumerate(["minder dan 10", "10 tot 100", "100 tot 300", "meer dan 300"]):
    LAND.rect(760, 130 + i * 40, 30, 26, KLEUR[i], DONKER, 2, 1)
    LAND.tekst(800, 149 + i * 40, tt, 15, "start")
U = "land-dichtheid.svg"
Z = {t: Prent.rond(lx - 60 if t in "DF" else lx, ly, 70) for t, (d, k, (lx, ly)) in STREKEN.items()}

ALG = [
    klik("Klik op de streek met de hoogste bevolkingsdichtheid.", U, [Z["F"]],
         "F heeft de donkerste kleur: meer dan 300 inwoners per km², rond de riviermonding."),
    klik("Klik op een dunbevolkte streek in het bergland zonder rivier.", U, [Z["A"]],
         "A ligt in de bergen, minder dan 10 inwoners per km², en de rivier stroomt niet door A."),
    casus("Veldaria telt 4,8 miljoen inwoners op 60 000 km². Streek F telt 1,8 miljoen inwoners op 5000 km².", [
        inv("Hoe groot is de bevolkingsdichtheid van heel Veldaria, in inwoners per km²?", ["80"],
            "4 800 000 / 60 000 = 80 inwoners per km²."),
        inv("Hoe groot is de bevolkingsdichtheid van streek F?", ["360"],
            "1 800 000 / 5000 = 360 inwoners per km²; dat past bij de klasse 'meer dan 300'."),
        tabel("Klopt dit over Veldaria?",
              [("Het gemiddelde van het land verbergt grote verschillen tussen de streken.", J), ("In elke streek wonen ongeveer 80 mensen per km².", F), ("De delta trekt veel mensen aan door water en vruchtbare grond.", J)],
              "Een gemiddelde zegt niets over de spreiding."),
    ]),
    sorteer("Maakt deze factor een gebied eerder dicht- of dunbevolkt?", ["eerder dichtbevolkt", "eerder dunbevolkt"],
            [("een vruchtbare delta", "eerder dichtbevolkt"), ("een woestijnklimaat", "eerder dunbevolkt"), ("een hooggebergte", "eerder dunbevolkt"), ("een vlakke kustvlakte met havens", "eerder dichtbevolkt"), ("bevroren bodem een groot deel van het jaar", "eerder dunbevolkt")],
            "Water, vruchtbare grond en vlak reliëf trekken mensen aan; droogte, kou en bergen niet."),
    tabel("Klopt dit over de bevolkingsdichtheid?",
          [("Een land met veel inwoners heeft daarom nog geen hoge dichtheid.", J), ("Een hoge dichtheid betekent dat een gebied rijk is.", F), ("Twee gebieden met dezelfde dichtheid kunnen een heel andere spreiding hebben.", J)],
          "Dichtheid zegt hoeveel mensen per km² wonen, niet hoe rijk of hoe verspreid."),
    mk("Waarom woont bijna iedereen in Egypte op een smalle strook langs de Nijl?",
       ["Daar zijn water en vruchtbare grond.", "Daar is het klimaat kouder en natter.", "Daar liggen de hoogste bergen.", "Daar is de grond het goedkoopst."], 0,
       "Rond de rivier is er water en slib; de rest is woestijn."),
    koppel("Welke factor verklaart het best de lage dichtheid?",
           [("de Sahara", "te weinig neerslag"), ("het noorden van Canada", "lange koude en bevroren bodem"), ("de Himalaya", "steil en hoog reliëf"), ("het Amazonewoud", "dicht woud en arme bodem")],
           ["te veel steden"], "Klimaat, reliëf en bodem verklaren veel van het wereldpatroon."),
    volgorde("Rangschik van laagste naar hoogste bevolkingsdichtheid.",
             ["1 miljoen inwoners op 100 000 km²", "3 miljoen op 60 000 km²", "5 miljoen op 25 000 km²", "2 miljoen op 4000 km²"],
             "10, 50, 200 en 500 inwoners per km²."),
    inv("Een provincie telt 1,2 miljoen inwoners en heeft een dichtheid van 400 inwoners per km². Hoe groot is ze, in km²?", ["3000", "3 000"],
        "Oppervlakte = inwoners / dichtheid = 1 200 000 / 400 = 3000 km²."),
    sleep("De bevolkingsdichtheid is het aantal [[inwoners]] per [[vierkante kilometer]]. Je leest ze af van een thematische kaart door eerst de [[legende]] te lezen.",
          ["huizen", "titel"], "Dichtheid altijd per km², en een kaart lees je met de legende."),
    tabel("Klopt dit over de ontwikkelingsgraad?",
          [("Ze gaat over welvaart, gezondheid en onderwijs samen.", J), ("Een land vol grondstoffen is daarom hoog ontwikkeld.", F), ("Binnen één land kan ze sterk verschillen tussen streken.", J), ("Er is een vast verband met de bevolkingsdichtheid.", F)],
          "Wat een land met zijn rijkdom doet, telt meer dan de rijkdom zelf."),
    mk("Nederland is dichtbevolkt en hoog ontwikkeld. Bangladesh is dichtbevolkt en minder ontwikkeld. Wat besluit je?",
       ["Dichtheid en ontwikkeling hangen niet vast samen.", "Een hoge dichtheid zorgt altijd voor ontwikkeling.", "Een hoge dichtheid maakt een land altijd arm.", "Je kan de twee landen helemaal niet vergelijken."], 0,
       "Er is geen vast verband tussen die twee."),
    casus("Je vergelijkt twee provincies met een tabel: provincie P telt 900 000 inwoners op 3000 km², provincie Q telt 600 000 inwoners op 1200 km².", [
        mk("Welke provincie is het dichtst bevolkt?",
           ["Q, met 500 inwoners per km²", "P, met 300 inwoners per km²", "P, omdat ze meer inwoners heeft", "Q, omdat ze kleiner is"], 0,
           "P: 300 per km²; Q: 500 per km². Je moet delen, niet enkel vergelijken."),
        tabel("Welke gegevens heb je nodig om eerlijk te vergelijken?",
              [("het aantal inwoners van elke provincie", J), ("de oppervlakte van elke provincie", J), ("het aantal steden in elke provincie", F)],
              "Dichtheid = inwoners gedeeld door oppervlakte."),
    ]),
    keuze("Een patroon op een kaart toont [[*hoe iets over een gebied verspreid is|hoeveel iets precies kost|wie de kaart gemaakt heeft]].",
          "Bij de bevolking zie je zo bijvoorbeeld een lint langs een rivier."),
    tabel("Klopt dit over reliëf en wonen?",
          [("Bouwen op steile hellingen is duur en moeilijk.", J), ("Reliëf speelt vandaag geen enkele rol meer.", F), ("Vlakke gebieden zijn makkelijk voor wegen en landbouw.", J)],
          "Technisch kan veel, maar bergen blijven dunner bevolkt."),
    inv("Hoe noem je de vruchtbare vlakte die een rivier vormt waar ze in zee uitmondt?", ["delta", "een delta", "de delta"],
        "In een delta zet de rivier haar slib af."),
    klik("Klik op een streek met 10 tot 100 inwoners per km².", U, [Z["C"], Z["E"]],
         "C en E hebben de tweede kleur van de legende."),
    tabel("Lees de kaart van Veldaria. Klopt dit?",
          [("De dichtheid neemt toe van de bergen naar de kust.", J), ("Streek B is dichter bevolkt dan streek D.", F), ("Langs de rivier wonen meer mensen dan in de bergen.", J)],
          "Bergen in het noorden zijn dun bevolkt, de delta in het zuiden het dichtst."),
    mk("Waarom wonen er in Vlaanderen veel mensen per km²?",
       ["vlak land, goede grond en een gunstige ligging", "een heel droog klimaat met amper regen", "veel hooggebergte met koele lucht", "een bodem die lang bevroren is"], 0,
       "Vlak land, goede grond en een ligging aan zee en rivieren trekken mensen aan."),
]

DO_ALLEEN = [
    casus("Een tabel toont drie landen: Noorland met een levensverwachting van 83 jaar, 18 jaar onderwijs en een hoog inkomen; Middenland met 72 jaar, 12 jaar en een middelmatig inkomen; Zuidland met 58 jaar, 6 jaar en een laag inkomen.", [
        volgorde("Rangschik de landen van hoogste naar laagste HDI.", ["Noorland", "Middenland", "Zuidland"],
                 "De HDI combineert levensverwachting, onderwijs en inkomen."),
        mk("Welke HDI past het best bij Zuidland?",
           ["0,45", "0,95", "1,45", "45"], 0,
           "De HDI ligt tussen 0 en 1; een lage score ligt dicht bij 0,4 of 0,5."),
    ]),
    tabel("Klopt dit over de HDI?",
          [("Hij combineert levensverwachting, onderwijs en inkomen.", J), ("Hij ligt tussen 0 en 1.", J), ("Hij meet hoe gelijk de welvaart verdeeld is.", F), ("Hij kan door een oorlog dalen.", J)],
          "De gewone HDI werkt met gemiddelden en ziet ongelijkheid niet."),
    sorteer("Doet dit de HDI eerder stijgen of dalen?", ["eerder stijgen", "eerder dalen"],
            [("een langdurige oorlog", "eerder dalen"), ("meer kinderen die naar school gaan", "eerder stijgen"), ("een zware epidemie", "eerder dalen"), ("betere gezondheidszorg", "eerder stijgen"), ("scholen die jarenlang dicht zijn", "eerder dalen")],
            "De HDI volgt gezondheid, onderwijs en inkomen."),
    mk("Twee landen hebben allebei een HDI van 0,75. Wat weet je dan zeker?",
       ["Hun samengestelde score is gelijk.", "Ze hebben dezelfde levensverwachting.", "Ze hebben hetzelfde gemiddelde inkomen.", "Hun kinderen gaan even lang naar school."], 0,
       "Het ene land kan beter scoren op gezondheid, het andere op inkomen."),
    tabel("Een bron over de HDI. Waarop let je kritisch?",
          [("van welk jaar de cijfers zijn", J), ("wie de cijfers verzameld heeft", J), ("de kleur van de kaart", F)],
          "Recente cijfers van een betrouwbare instelling, zoals de Verenigde Naties."),
    keuze("De HDI wordt elk jaar berekend door [[*de Verenigde Naties|de Europese Unie|de NAVO]].",
          "De VN publiceren de Human Development Index."),
    mk("Waarom is de HDI een betere maat voor ontwikkeling dan het inkomen alleen?",
       ["Hij telt ook gezondheid en onderwijs mee.", "Hij is makkelijker te berekenen dan het inkomen.", "Hij geldt enkel voor de rijkste landen van de wereld.", "Hij telt ook het aantal inwoners per km²."], 0,
       "Een rijk land kan slecht scoren op gezondheid of onderwijs."),
]

DF_ALLEEN = [
    casus("Een tabel toont drie landen: in Noorland gaan kinderen gemiddeld 16 jaar naar school, in Middenland 10 jaar en in Zuidland 4 jaar. In Zuidland is er al jaren oorlog.", [
        volgorde("Rangschik van hoogste naar laagste scholingsgraad.", ["Noorland", "Middenland", "Zuidland"],
                 "De scholingsgraad toont hoe lang en hoeveel mensen naar school gaan."),
        mk("Welke factor verklaart het best de lage scholingsgraad in Zuidland?",
           ["de oorlog, die scholen sluit", "het grote aantal bergen", "de hoge bevolkingsdichtheid", "de ligging aan de zee"], 0,
           "De politieke en de oorlogssituatie beïnvloeden het onderwijs sterk."),
    ]),
    tabel("Is dit een factor die de ontwikkeling van een land beïnvloedt?",
          [("klimaat en klimaatverandering", J), ("de politieke en de oorlogssituatie", J), ("armoede", J), ("de kleur van de vlag", F)],
          "Ook reliëf, bodemkwaliteit en welvaart en welzijn horen in het rijtje."),
    sorteer("Is dit een fysische of een sociaaleconomische factor?", ["fysisch", "sociaaleconomisch"],
            [("het reliëf", "fysisch"), ("armoede", "sociaaleconomisch"), ("de bodemkwaliteit", "fysisch"), ("de scholingsgraad", "sociaaleconomisch"), ("een oorlog", "sociaaleconomisch")],
            "Fysisch komt uit de natuur; sociaaleconomisch uit hoe mensen samenleven."),
    mk("Waarom zegt de scholingsgraad iets over de ontwikkeling van een land?",
       ["Onderwijs geeft kansen op werk en gezondheid.", "Scholen maken een land dichter bevolkt.", "Een school verhoogt de neerslag in een streek.", "Wie naar school gaat, verhuist altijd naar de stad."], 0,
       "Wie langer naar school gaat, vindt makkelijker werk en leeft gezonder."),
    tabel("Klopt dit over welvaart en welzijn?",
          [("Welvaart gaat over wat je kan kopen.", J), ("Welzijn gaat ook over gezondheid en hoe goed je je voelt.", J), ("Wie welvaart heeft, heeft altijd welzijn.", F)],
          "Geld alleen maakt niet gezond of gelukkig."),
    keuze("Een droogte door klimaatverandering kan een gebied [[*dunner|dichter|niet anders]] bevolkt maken.",
          "Zonder water lukt landbouw niet en trekken mensen weg."),
    mk("Een tabel geeft per land het aantal inwoners en de oppervlakte. Wat bereken je daarmee?",
       ["de bevolkingsdichtheid", "de scholingsgraad", "de levensverwachting", "het gemiddelde inkomen"], 0,
       "Inwoners gedeeld door oppervlakte."),
]

VRAGEN = ALG + DO_ALLEEN
VRAGEN_DF = ALG + DF_ALLEEN
