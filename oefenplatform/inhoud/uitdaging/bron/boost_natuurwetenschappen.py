# -*- coding: utf-8 -*-
"""Uitdaging Natuurwetenschappen 🚀 Boost doorstroom (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die biologie, chemie
en fysica door elkaar halen. Casussen, tabellen, keuzelijsten, slepen,
koppelen, sorteren, volgorde, rekenvragen, vier klikvragen op twee zelf
getekende prenten en een open onderzoeksvraag. Geen nieuwe leerstof: alles
staat in de hoofdstukken van Natuurwetenschappen Boost doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_natuurwetenschappen.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Natuurwetenschappen"
BESTAND = "boost-natuurwetenschappen-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/natuurwetenschappen-boost-uitdaging"
GRAFIEK = "fietser-v-t.svg"
SYSTEEM = "periodiek-uitsnede.svg"
# klikvakken: zie maak_prenten_boost_natuurwetenschappen.py
STUK_B = [36.7, 13.3, 40.0, 70.0]
STUK_C = [76.7, 13.3, 16.0, 70.0]
MG = [17.0, 68.1, 11.0, 23.4]
AR = [83.0, 68.1, 11.0, 23.4]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # De v(t)-grafiek van een fietser (prent)
    klik("Bekijk de v(t)-grafiek van de fietser. Klik op het stuk waar de fietser eenparig rechtlijnig beweegt.",
         GRAFIEK, [STUK_B],
         "In stuk B blijft de snelheid 8 meter per seconde: de grafiek loopt vlak. Een constante snelheid op een rechte baan is een eenparig rechtlijnige beweging."),
    klik("Klik in dezelfde grafiek op het stuk met de grootste versnelling, in grootte.",
         GRAFIEK, [STUK_C],
         "De steilheid van een v(t)-grafiek is de versnelling. In stuk A wint de fietser 8 meter per seconde in 4 seconden (2 meter per seconde kwadraat). In stuk C verliest hij 8 meter per seconde in 2 seconden (min 4 meter per seconde kwadraat). Stuk C is dus het steilst."),
    met_prent(GRAFIEK, inv(
        "Hoe groot is de versnelling van de fietser in stuk A, in meter per seconde kwadraat? Geef enkel het getal.",
        "2",
        "Versnelling is de verandering van de snelheid gedeeld door het tijdsverloop: 8 gedeeld door 4 geeft 2 meter per seconde kwadraat.")),
    met_prent(GRAFIEK, inv(
        "Hoeveel meter legt de fietser in totaal af in die 12 seconden? Geef enkel het getal.",
        "72",
        "De verplaatsing is de oppervlakte onder de v(t)-grafiek. Stuk A: driehoek, 4 maal 8 gedeeld door 2 is 16 meter. Stuk B: rechthoek, 6 maal 8 is 48 meter. Stuk C: driehoek, 2 maal 8 gedeeld door 2 is 8 meter. Samen 72 meter.")),
    met_prent(GRAFIEK, tabel(
        "Klopt dit over de fietser?",
        [
            ("In stuk B is de resulterende kracht op de fietser nul.", J),
            ("In stuk C werkt de resulterende kracht in de zin van de beweging.", F),
            ("In stuk A is de x(t)-grafiek een rechte lijn.", F),
            ("Na 12 seconden staat de fietser stil.", J),
        ],
        "Bij een constante snelheid is de resulterende kracht nul. Bij remmen werkt ze tegen de beweging in. Bij een versnelde beweging is de x(t)-grafiek een kromme, geen rechte. Op 12 seconden is de snelheid nul.")),

    # Een stukje periodiek systeem (prent)
    klik("Bekijk het stukje periodiek systeem. Klik in periode 3 op het element waarvan het atoom een volle buitenste schil heeft.",
         SYSTEEM, [AR],
         "Groep 18 zijn de edelgassen. Hun buitenste schil is vol, daarom reageren ze nauwelijks. In periode 3 is dat argon."),
    klik("Klik in periode 3 op het element waarvan het atoom twee valentie-elektronen heeft.",
         SYSTEEM, [MG],
         "Bij hoofdgroepelementen lees je het aantal valentie-elektronen af aan het groepsnummer: groep 2 heeft er twee. In periode 3 is dat magnesium."),
    met_prent(SYSTEEM, mk(
        "Natrium en chloor reageren samen tot keukenzout. Welk bindingstype ontstaat er?",
        ["een atoombinding, want ze delen een elektronenpaar", "een metaalbinding met een zee van vrije elektronen", "een ionbinding, want natrium geeft een elektron aan chloor", "geen binding, want chloor heeft al een volle buitenste schil"],
        2,
        "Natrium is een metaal met één valentie-elektron, chloor een niet-metaal met zeven. Natrium staat zijn elektron af aan chloor: zo ontstaan een positief en een negatief ion, en dus een ionbinding.")),
    met_prent(SYSTEEM, inv(
        "Hoeveel bezette elektronenschillen heeft een atoom aluminium? Geef enkel het getal.",
        "3",
        "Het periodenummer geeft het aantal bezette schillen. Aluminium staat in periode 3.")),
    met_prent(SYSTEEM, keuze(
        "Een zuurstofatoom neemt [[*twee|zes|één]] elektronen op en wordt zo een [[*negatief|positief]] ion.",
        "Zuurstof staat in groep 16 en heeft zes valentie-elektronen. Er twee bijnemen is veel makkelijker dan er zes afstaan. Met twee extra elektronen is het ion negatief.")),

    # Casus: een hete pan
    casus(
        "Lies grijpt per ongeluk een hete pan vast en trekt haar hand terug nog voor ze het goed beseft. Pas daarna voelt ze de pijn.",
        [
            volgorde(
                "Zet de weg van de impuls bij deze reflex in de juiste volgorde.",
                ["warmtereceptor in de huid", "sensorisch neuron", "schakelneuron in het ruggenmerg", "motorisch neuron", "spier in de arm"],
                "De prikkel wordt opgevangen door een receptor en gaat via een sensorisch neuron naar het ruggenmerg. Een schakelneuron geeft het bevel door aan een motorisch neuron, en de spier (de effector) trekt samen."),
            mk("Waarom voelt Lies de pijn pas nadat haar hand al weg is?",
               ["Omdat de pijnreceptoren pas na de reactie van de spier aanslaan.", "Omdat het ruggenmerg reageert voor de hersenen het weten.", "Omdat de impuls over een synaps sneller gaat dan over een axon.", "Omdat de spier eerst samentrekt en daarna pas een prikkel krijgt."],
               1,
               "Bij een reflex stuurt het ruggenmerg meteen een bevel terug. Het signaal naar de grote hersenen, waar je de pijn bewust voelt, komt iets later aan."),
            tabel(
                "Klopt dit over wat er in haar zenuwen gebeurt?",
                [
                    ("Tussen twee neuronen geeft een neurotransmitter het signaal door.", J),
                    ("Myeline rond de axonen maakt de impuls trager.", F),
                    ("Een prikkel onder de drempelwaarde had geen impuls opgeleverd.", J),
                ],
                "In de synaptische spleet draagt een neurotransmitter het signaal over. Myeline isoleert het axon en maakt de impuls net sneller."),
        ],
    ),

    # Casus: na de middag
    casus(
        "Na een stevig middagmaal met pasta stijgt het glucosegehalte in het bloed van Omar. Een paar uur later, na het sporten, daalt het.",
        [
            keuze(
                "Na de maaltijd maakt de [[*alvleesklier|hypofyse|schildklier]] meer [[*insuline|adrenaline|testosteron]] aan, zodat de lever glucose opslaat als [[*glycogeen|zetmeel|vet]].",
                "Insuline uit de alvleesklier laat het glucosegehalte dalen: de lever en de spieren slaan glucose op als glycogeen."),
            mk("Waarom noemen we deze regeling een feedbacksysteem?",
               ["Omdat de hoeveelheid glucose zelf de aanmaak van hormoon bijstuurt.", "Omdat er altijd evenveel insuline in het bloed blijft, wat je ook eet.", "Omdat de zenuwen het bevel geven en de hormonen het nooit doen.", "Omdat enkel de hersenen zelf beslissen wanneer de lever werkt."],
               0,
               "Het gevolg (veel of weinig glucose) stuurt het proces zelf bij: is er te veel, dan komt er insuline, en zakt het, dan stopt dat."),
        ],
    ),

    # Casus: een vijver
    casus(
        "Naast een vijver ligt een akker die zwaar bemest wordt. Na een warme zomer is het water groen van de algen en drijven er dode vissen.",
        [
            mk("Hoe noem je wat er met deze vijver gebeurd is?",
               ["eutrofiëring", "de stikstofkringloop", "antibiose", "sublimatie"],
               0,
               "Te veel meststoffen in het water laten de algen opbloeien. Als die afsterven, verbruiken de afbrekers veel zuurstof en sterven de vissen."),
            tabel(
                "Is dit een biotische of een abiotische factor in de vijver?",
                [
                    ("de watertemperatuur", "Abiotisch"),
                    ("de algen", "Biotisch"),
                    ("het zuurstofgehalte van het water", "Abiotisch"),
                    ("de bacteriën die dode algen afbreken", "Biotisch"),
                ],
                "Biotisch komt van levende organismen, abiotisch zijn de niet-levende factoren zoals temperatuur en zuurstof.",
                kolommen=["Biotisch", "Abiotisch"]),
            keuze(
                "De bacteriën die de dode algen afbreken, zijn [[*reducenten|producenten|consumenten]]. Ze verbruiken daarbij veel [[*zuurstof|stikstof|koolstofdioxide]].",
                "Reducenten breken dood materiaal af tot minerale stoffen. Daarvoor gebruiken ze zuurstof, die dan niet meer voor de vissen is."),
        ],
    ),

    # Casus: ijs opwarmen
    casus(
        "In het labo warmt Sara een blokje ijs van min 10 graden op tot er alleen nog stoom is. Ze noteert om de halve minuut de temperatuur en tekent een grafiek.",
        [
            mk("Haar grafiek heeft twee vlakke stukken. Bij welke temperaturen?",
               ["bij min 10 en bij 0 graden", "bij 0 en bij 50 graden", "bij 0 en bij 100 graden", "bij 50 en bij 100 graden"],
               2,
               "Tijdens een faseovergang blijft de temperatuur gelijk: bij 0 graden smelt het ijs en bij 100 graden kookt het water."),
            tabel(
                "Klopt dit over haar proef?",
                [
                    ("Tijdens het smelten gaat alle warmte naar het losmaken van de deeltjes.", J),
                    ("Verdampen vraagt meer warmte dan opwarmen van 0 naar 100 graden.", J),
                    ("Water dat kookt, wordt heter als je de brander hoger zet.", F),
                ],
                "In een vlak stuk gaat de warmte naar de faseovergang, niet naar een hogere temperatuur. Daarom blijft kokend water op 100 graden staan."),
            inv("Hoeveel joule heeft Sara nodig om 0,5 kilogram water van 20 naar 60 graden op te warmen? De specifieke warmtecapaciteit van water is 4180 joule per kilogram per graad. Geef enkel het getal.",
                ["83600", "83 600", "83.600"],
                "Merkbare warmte is specifieke warmtecapaciteit maal massa maal temperatuurverschil: 4180 maal 0,5 maal 40 is 83 600 joule."),
        ],
    ),

    # Casus: in het labo
    casus(
        "Op een fles in het labo staat: 'H314: veroorzaakt ernstige brandwonden en oogletsel'. Je moet er precies 10 milliliter van afmeten.",
        [
            mk("Welk gevarenpictogram verwacht je op die fles?",
               ["het pictogram met de vlam voor ontvlambare stoffen", "het pictogram voor bijtende stoffen", "het pictogram met de dode vis voor milieugevaar", "het pictogram met het uitroepteken"],
               1,
               "H314 gaat over brandwonden op de huid en letsel aan de ogen: dat is een bijtende stof."),
            mk("Waarmee meet je die 10 milliliter het nauwkeurigst af?",
               ["met een bekerglas met een maatverdeling", "met een erlenmeyer met een streepje erop", "met een volpipet", "met een theelepel van thuis"],
               2,
               "Een pipet is gemaakt om een bepaald klein volume heel nauwkeurig af te meten. Een bekerglas of erlenmeyer geeft maar een ruwe schatting."),
            inv("Je weegt daarna 12,40 gram af. Hoeveel beduidende cijfers heeft dat meetresultaat? Geef enkel het getal.",
                "4",
                "De nul achteraan telt mee: ze toont dat je tot op een honderdste gram nauwkeurig gemeten hebt. 1, 2, 4 en 0 zijn vier beduidende cijfers."),
        ],
    ),

    # Losse vragen door elkaar
    sorteer(
        "Is dit mengsel homogeen of heterogeen?",
        ["Homogeen", "Heterogeen"],
        [
            ["suikerwater", "Homogeen"],
            ["lucht", "Homogeen"],
            ["mayonaise", "Heterogeen"],
            ["mist", "Heterogeen"],
            ["messing", "Homogeen"],
        ],
        "In een homogeen mengsel zie je de bestanddelen niet, ook niet met een microscoop. Mayonaise is een emulsie en mist een aerosol: daar zie je de druppeltjes wel. Messing is een legering van koper en zink."),
    koppel(
        "Welke scheidingstechniek past het best bij elk mengsel?",
        [
            ["zand uit water halen", "filtreren"],
            ["de kleurstoffen van een stift scheiden", "chromatografie"],
            ["ijzervijlsel uit zand halen", "met een magneet"],
            ["olie die op water drijft afgieten", "decanteren"],
        ],
        ["sublimeren", "elektrolyse"],
        "Elke techniek steunt op een verschil in stofeigenschap: deeltjesgrootte, hoe ver een stof meeschuift, magnetisme of dichtheid."),
    tabel(
        "Welk roostertype heeft elke stof?",
        [
            ("keukenzout", "Ionrooster"),
            ("koper", "Metaalrooster"),
            ("diamant", "Atoomrooster"),
            ("suiker", "Molecuulrooster"),
        ],
        "Metaal met niet-metaal geeft een ionrooster. Een metaal heeft vrije elektronen. Diamant is één groot net van atoombindingen. Suiker bestaat uit losse moleculen.",
        kolommen=["Ionrooster", "Metaalrooster", "Atoomrooster", "Molecuulrooster"]),
    keuze(
        "Maak kloppend: [[*2|1|4]] H₂ + O₂ → [[*2|1|4]] H₂O.",
        "Links staan twee zuurstofatomen, dus rechts twee watermoleculen. Die hebben samen vier waterstofatomen, dus links twee H₂. Je past enkel de coëfficiënten aan, nooit de index."),
    mk("In een energiediagram liggen de reactieproducten hoger dan de reagentia. Wat weet je over die reactie?",
       ["Ze geeft energie af aan de omgeving en is exo-energetisch.", "Ze neemt energie op en is endo-energetisch.", "Er verandert geen energie, enkel de massa van de stoffen.", "De totale massa na de reactie is groter dan ervoor."],
       1,
       "Hoger eindigen betekent dat de stoffen energie bijkregen: de reactie is endo-energetisch. De massa blijft gelijk (wet van behoud van massa)."),
    inv("Je lost 0,2 mol keukenzout op tot je 0,4 liter oplossing hebt. Wat is de molaire concentratie, in mol per liter? Geef enkel het getal.",
        ["0,5", "0.5"],
        "Molaire concentratie is het aantal mol gedeeld door het volume in liter: 0,2 gedeeld door 0,4 is 0,5 mol per liter."),
    inv("Een gas van 6 liter bij 1 bar wordt bij gelijke temperatuur samengeperst tot 2 liter. Hoeveel bar is de druk dan? Geef enkel het getal.",
        "3",
        "Bij een gelijke temperatuur zijn druk en volume omgekeerd evenredig: druk maal volume blijft gelijk. 1 maal 6 is 3 maal 2."),
    inv("Een kast van 600 newton staat op vier poten, samen 0,02 vierkante meter. Hoeveel pascal is de druk op de vloer? Geef enkel het getal.",
        ["30000", "30 000", "30.000"],
        "Druk is kracht gedeeld door oppervlakte: 600 gedeeld door 0,02 is 30 000 pascal."),
    inv("Een skateboarder van 60 kilogram rijdt 5 meter per seconde. Hoeveel joule kinetische energie heeft hij? Geef enkel het getal.",
        "750",
        "Kinetische energie is de massa maal het kwadraat van de snelheid, gedeeld door twee: 60 maal 25 gedeeld door 2 is 750 joule."),
    mk("Een elektrische motor krijgt 500 joule en levert 400 joule beweging. Wat is zijn rendement?",
       ["20 procent, want 100 joule gaat verloren", "80 procent, want 400 van de 500 joule is nuttig", "125 procent, want 500 gedeeld door 400", "400 procent, want hij levert 400 joule nuttige energie"],
       1,
       "Rendement is de nuttige energie gedeeld door de toegevoerde energie: 400 gedeeld door 500 is 0,8 of 80 procent. Het kan nooit boven 100 procent."),
    inv("Over een weerstand van 20 ohm staat een spanning van 6 volt. Hoeveel ampère is de stroomsterkte? Geef enkel het getal.",
        ["0,3", "0.3"],
        "Volgens de wet van Ohm is de stroomsterkte de spanning gedeeld door de weerstand: 6 gedeeld door 20 is 0,3 ampère."),
    sleep(
        "Een plant neemt water op met de [[wortelharen]]. Het water stijgt door de [[houtvaten]] naar het blad en verdampt daar door de [[huidmondjes]]. Die verdamping heet [[transpiratie]].",
        ["zeefvaten", "chloroplasten"],
        "Houtvaten (xyleem) brengen water en zouten naar boven. Zeefvaten brengen suikers rond. Chloroplasten doen aan fotosynthese."),
    keuze(
        "Je kijkt van je gsm op naar een vliegtuig in de lucht. Je ooglens wordt dan [[*platter|boller]]. Dat aanpassen heet [[*accommoderen|reflecteren|depolariseren]].",
        "Voor iets ver weg moet de lens het licht minder breken: ze wordt platter. Het aanpassen van de lens heet accommoderen."),
    koppel(
        "Welke interactie tussen organismen is het?",
        [
            ["een lintworm in de darm van een hond", "parasitisme"],
            ["bijen die nectar halen en bloemen bestuiven", "mutualisme"],
            ["een vos die konijnen vangt", "predatie"],
            ["een schimmel die een stof maakt die bacteriën doodt", "antibiose"],
        ],
        ["fotosynthese", "conditioneren"],
        "Bij parasitisme wint één organisme en lijdt het andere. Bij mutualisme winnen beide. Bij predatie eet het ene het andere op. Bij antibiose remt of doodt een stof van het ene het andere."),
    tabel(
        "Klopt dit over micro-organismen?",
        [
            ("Bakkersgist laat brood rijzen.", J),
            ("Een virus vermeerdert zich door celsplitsing.", F),
            ("Melkzuurbacteriën maken yoghurt van melk.", J),
            ("Antibiotica helpen tegen een virusinfectie.", F),
        ],
        "Een virus laat een gastheercel nieuwe virusdeeltjes maken. Antibiotica werken tegen bacteriën, niet tegen virussen."),
    open_("Je wil onderzoeken of de temperatuur van het water invloed heeft op hoe snel suiker oplost. Schrijf een hypothese en zeg welke grootheid je verandert, welke je meet en welke je gelijk houdt.",
          "Hypothese: hoe warmer het water, hoe sneller de suiker oplost. Ik verander de temperatuur van het water. Ik meet de tijd tot alle suiker opgelost is. Ik houd de hoeveelheid water, de hoeveelheid suiker en het roeren gelijk.",
          "Een goede hypothese is een verwachting die je kunt testen. Verander maar één ding tegelijk, anders weet je niet wat het verschil veroorzaakt."),
]
