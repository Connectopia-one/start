# -*- coding: utf-8 -*-
"""Uitdaging Nederlands 🚀 Boost dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Een zelf geschreven nieuwsbericht en
verhaalfragment om op te klikken, tabellen, keuzelijsten, slepen, koppelen,
sorteren, volgorde en een korte schrijfopdracht. Geen nieuwe leerstof: alles
staat in de hoofdstukken van Nederlands Boost dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_nederlands.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Nederlands"
BESTAND = "boost-df-nederlands-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/nederlands-boost-df-uitdaging"
BERICHT = "bericht-jeugdhuis.svg"
VERHAAL = "verhaal-pier.svg"


def regel(i, n):
    """Klikvak van regel i (vanaf 1) op een prent met n regels (zie maak_prenten)."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Nieuwsbericht (prent): feit, mening en structuuraanduiders
    klik("Lees het bericht. Klik op de zin waarin de schrijver een mening geeft.",
         BERICHT, [regel(3, 6)],
         "'Eindelijk eens een schitterende beslissing' is een oordeel van de schrijver. Je kan het niet controleren zoals een datum of een bedrag. De andere zinnen geven feiten."),
    klik("Klik op de zin die met een signaalwoord een tegenstelling aankondigt.",
         BERICHT, [regel(5, 6)],
         "'Toch' zet de zin tegenover het vorige: er komt een nieuw jeugdhuis, maar niet iedereen is blij."),
    met_prent(BERICHT, tabel(
        "Welk verband legt het signaalwoord in het bericht?",
        [
            ("'want' in zin 4", "Reden"),
            ("'Toch' in zin 5", "Tegenstelling"),
            ("'Daarom' in zin 6", "Gevolg"),
        ],
        "'Want' geeft de reden waarom het oude jeugdhuis sloot. 'Toch' brengt een tegenstelling. 'Daarom' geeft het gevolg van de klachten van de buren.",
        kolommen=["Reden", "Tegenstelling", "Gevolg"])),
    met_prent(BERICHT, mk(
        "Wat is de hoofdgedachte van het bericht?",
        ["Velddorp krijgt een nieuw jeugdhuis, dat om middernacht sluit.", "Het oude jeugdhuis van Velddorp was al jaren niet meer veilig genoeg.", "De buren van de bibliotheek willen helemaal geen jeugdhuis in hun straat.", "Het gemeentebestuur geeft te veel geld uit aan een nieuw jeugdhuis."],
        0,
        "De hoofdgedachte vat de hele tekst samen. Het oude gebouw en de buren zijn deelonderwerpen. Dat het te veel geld kost, staat er niet.")),
    met_prent(BERICHT, keuze(
        "Zonder zin 3 is dit een [[*informatieve|prescriptieve|narratieve]] tekst. Met zin 3 erbij is het bericht niet meer helemaal [[*objectief|subjectief]].",
        "Een nieuwsbericht wil informeren. Een mening van de schrijver maakt de tekst gekleurd: dan is hij niet meer objectief.")),

    # Verhaalfragment (prent): beeldspraak, tijd en ruimte
    klik("Lees het fragment. Klik op de zin met een personificatie.",
         VERHAAL, [regel(3, 6)],
         "Golven kunnen niet echt fluisteren. Ze krijgen een menselijke eigenschap: dat is een personificatie."),
    klik("Klik op de zin met een metafoor.",
         VERHAAL, [regel(4, 6)],
         "'Hij was een rots' zegt niet dat de broer een steen is. Hij wordt zonder 'als' vergeleken met een rots: stil en sterk. Dat is een metafoor."),
    met_prent(VERHAAL, tabel(
        "Klopt dit over het fragment?",
        [
            ("Zin 1 vertelt iets over de tijd van het verhaal.", J),
            ("Zin 2 vertelt iets over de ruimte van het verhaal.", J),
            ("Het fragment is non-fictie, want een pier bestaat echt.", F),
            ("De verteller is Lotte zelf, die in de ik-vorm vertelt.", F),
        ],
        "De laatste avond van de vakantie is de tijd, de pier en de zee zijn de ruimte. Dat een plaats echt bestaat, maakt een verzonnen verhaal nog geen non-fictie. Er staat 'ze' en 'Lotte': het is een hij- of zij-verteller.")),
    met_prent(VERHAAL, mk(
        "Welk gevoel roept het fragment vooral op?",
        ["afscheid en twijfel voor wat komt", "uitgelaten blijdschap om de vakantie", "boosheid op haar zwijgende broer", "angst voor de golven die te hoog komen"],
        0,
        "Het is de laatste avond, 'morgen zou alles anders zijn' en ze staat op om te gaan. Dat wijst op afscheid en onzekerheid, niet op blijdschap of angst."),
    ),

    # Communicatie
    casus(
        "Sara stuurt haar leerkracht 's avonds laat een spraakbericht via een chatapp: 'Yo meneer, k ben morgen ni op school want ziek, ok?' Op de achtergrond staat de televisie luid.",
        [
            koppel(
                "Koppel elk begrip aan wat het in deze situatie is.",
                [
                    ["zender", "Sara"],
                    ["ontvanger", "de leerkracht"],
                    ["kanaal", "een spraakbericht"],
                    ["ruis", "de luide televisie"],
                ],
                ["de school", "de ziekte"],
                "De zender stuurt de boodschap, de ontvanger krijgt ze. Het kanaal is de weg waarlangs ze gaat. Ruis is alles wat de boodschap stoort."),
            mk("Wat is er mis met het register van Sara?",
               ["Het is te informeel voor een bericht aan een leerkracht.", "Het is te formeel en klinkt daardoor veel te afstandelijk.", "Het is standaardtaal, maar de zinnen zijn net te lang.", "Er is niets mis mee, want ze laat weten dat ze ziek is."],
               0,
               "'Yo', 'k' en 'ni' horen bij informeel taalgebruik tussen vrienden. Tegenover een leerkracht past een beleefder register in standaardtaal."),
            sleep(
                "Een betere versie: '[[Beste]] meneer Claes, ik ben morgen helaas ziek en kom niet naar school. [[Met vriendelijke groeten]], Sara.' Zo kies je een [[formeel]] register.",
                ["Yo", "informeel"],
                "Een aanspreking, een volledige zin in standaardtaal en een beleefde groet maken het bericht formeel."),
        ],
    ),
    tabel(
        "Welke tekstsoort is dit naar het doel?",
        [
            ("een handleiding voor een nieuwe gsm", "Prescriptief"),
            ("een folder die je overhaalt om een nieuwe frisdrank te kopen", "Persuasief"),
            ("een spannend verhaal over een ontsnapping", "Narratief"),
            ("een nieuwsbericht over een verkeersongeval", "Informatief"),
        ],
        "Een prescriptieve tekst geeft instructies, een persuasieve wil overtuigen om iets te doen of te kopen, een narratieve vertelt een verhaal en een informatieve geeft informatie.",
        kolommen=["Informatief", "Prescriptief", "Narratief", "Persuasief"]),

    # Argumentatie en bronnen
    sorteer(
        "Is dit een feit of een mening?",
        ["Feit", "Mening"],
        [
            ["België telt tien provincies.", "Feit"],
            ["Wiskunde is het leukste vak.", "Mening"],
            ["De les begint om 8.25 uur.", "Feit"],
            ["Die film duurt veel te lang.", "Mening"],
            ["Water kookt bij 100 graden op zeeniveau.", "Feit"],
        ],
        "Een feit kan je controleren en is voor iedereen hetzelfde. Een mening is een persoonlijk oordeel; anderen kunnen het daar terecht mee oneens zijn."),
    volgorde(
        "Zet de delen van een betoog in de juiste volgorde.",
        ["de inleiding met de stelling", "het eerste argument", "het tweede argument", "de conclusie die de stelling herhaalt"],
        "Een argumentatieve tekst begint met het standpunt, geeft daarna argumenten en sluit af met een conclusie."),
    mk("'Gsm's moeten verboden worden op school, want gsm's horen niet op school.' Wat is hier fout aan?",
       ["Het argument herhaalt gewoon de stelling.", "Het argument is een feit en geen mening van iemand.", "De stelling staat achteraan, na het argument erbij.", "Er staat een signaalwoord dat een doel aankondigt."],
       0,
       "Een argument moet een reden geven waarom de stelling klopt. Hier zegt het argument hetzelfde als de stelling: dat is een cirkelredenering."),
    tabel(
        "Welke vraag helpt je om de betrouwbaarheid van een bericht na te gaan?",
        [
            ("Wie is de zender en wat wil die bereiken?", J),
            ("Hoeveel mensen hebben het bericht al gedeeld?", F),
            ("Vind je hetzelfde nieuws ook bij andere, betrouwbare bronnen?", J),
            ("Staan er veel uitroeptekens en hoofdletters in de titel?", J),
        ],
        "Kijk naar de zender en zijn doel, en vergelijk met andere bronnen. Veel uitroeptekens en schreeuwende titels wijzen vaak op nepnieuws. Hoe vaak iets gedeeld is, zegt niets over de waarheid."),

    # Taalvariëteiten
    tabel(
        "Is dit standaardtaal of tussentaal?",
        [
            ("Hedde gij da gezien?", "Tussentaal"),
            ("Heb jij dat gezien?", "Standaardtaal"),
            ("Ik ga dat ne keer vragen.", "Tussentaal"),
            ("Ik zal het eens vragen.", "Standaardtaal"),
        ],
        "Tussentaal ligt tussen dialect en standaardtaal: vormen als 'hedde', 'gij', 'da' en 'ne keer' hoor je vaak in Vlaanderen, maar ze horen niet bij de standaardtaal.",
        kolommen=["Standaardtaal", "Tussentaal"]),

    # Woordsoorten
    tabel(
        "Welke woordsoort is elk woord in de zin 'De snelle fietser reed gisteren naar huis.'?",
        [
            ("snelle", "Bijvoeglijk naamwoord"),
            ("gisteren", "Bijwoord"),
            ("naar", "Voorzetsel"),
            ("fietser", "Zelfstandig naamwoord"),
        ],
        "'Snelle' zegt iets over het zelfstandig naamwoord 'fietser'. 'Gisteren' zegt iets over het werkwoord. 'Naar' is een voorzetsel dat een verhouding aangeeft.",
        kolommen=["Zelfstandig naamwoord", "Bijvoeglijk naamwoord", "Bijwoord", "Voorzetsel"]),
    keuze(
        "In 'Zij helpen [[*elkaar|zich]] met hun huiswerk' gebruik je een wederkerig voornaamwoord. In 'Is dit jouw boek of [[*het mijne|mijn]]?' gebruik je het voornaamwoord zelfstandig.",
        "'Elkaar' drukt uit dat ze het over en weer doen. 'Het mijne' staat zonder zelfstandig naamwoord erachter."),

    # Werkwoorden en woordvorming
    keuze(
        "Gisteren [[*antwoordde|antwoorde]] hij meteen. Daarna heeft hij de brief [[*verbrand|verbrandt]]. [[*Word|Wordt]] jij daar niet moe van?",
        "De stam 'antwoord' eindigt op een d: daar komt -de achter, dus 'antwoordde'. Het voltooid deelwoord van 'verbranden' eindigt op een d. Staat 'jij' achter de persoonsvorm, dan valt de t weg."),
    tabel(
        "Bepaal de tijd van elke zin.",
        [
            ("Ik fietste naar school.", "Onvoltooid verleden tijd"),
            ("Ik had de bus gemist.", "Voltooid verleden tijd"),
            ("Ik heb hard gelopen.", "Voltooid tegenwoordige tijd"),
            ("Ik zal morgen bellen.", "Onvoltooid toekomende tijd"),
        ],
        "Voltooid betekent dat er een voltooid deelwoord bij staat. 'Had' is verleden, 'heb' tegenwoordig. 'Zal' wijst naar de toekomst.",
        kolommen=["Onvoltooid verleden tijd", "Voltooid verleden tijd", "Voltooid tegenwoordige tijd", "Onvoltooid toekomende tijd"]),
    sorteer(
        "Is dit woord een samenstelling of een afleiding?",
        ["Samenstelling", "Afleiding"],
        [
            ["voetbalveld", "Samenstelling"],
            ["vriendelijkheid", "Afleiding"],
            ["onweer", "Afleiding"],
            ["boekentas", "Samenstelling"],
            ["schoonheid", "Afleiding"],
        ],
        "Een samenstelling bestaat uit twee woorden die ook alleen kunnen staan. Een afleiding is een woord met een voor- of achtervoegsel zoals on-, -heid of -lijk."),

    # Zinsdelen
    tabel(
        "Welk zinsdeel is het? In 'Morgen geeft de trainer de spelers een nieuw schema.'",
        [
            ("geeft", "Persoonsvorm"),
            ("de trainer", "Onderwerp"),
            ("een nieuw schema", "Lijdend voorwerp"),
            ("de spelers", "Meewerkend voorwerp"),
        ],
        "'Geeft' verandert mee met het onderwerp. Wie geeft? De trainer. Wat geeft hij? Een nieuw schema. Aan wie? Aan de spelers.",
        kolommen=["Persoonsvorm", "Onderwerp", "Lijdend voorwerp", "Meewerkend voorwerp"]),
    mk("Wat is de bijzin in 'De wedstrijd ging door, hoewel het hard regende'?",
       ["hoewel het hard regende", "De wedstrijd ging door", "door, hoewel het hard regende", "De wedstrijd ging door, hoewel"],
       0,
       "Een bijzin kan niet alleen staan en begint hier met het voegwoord 'hoewel'."),
    keuze(
        "De zin 'Het lied wordt door het koor gezongen' staat in de [[*lijdende|bedrijvende]] vorm. In de andere vorm wordt dat: '[[*Het koor zingt het lied.|Het lied zingt het koor.]]'",
        "In de lijdende vorm staat er 'worden' of 'zijn' met een voltooid deelwoord, en wie de handeling doet, staat na 'door'."),

    # Spelling en leestekens
    tabel(
        "Is de zin correct geschreven?",
        [
            ("Op maandag heb ik Engels.", F),
            ("Hij vroeg of ik meekwam.", J),
            ("We gaan in juli naar Spanje.", J),
            ("Ze vroeg: 'Kom je ook'?", F),
        ],
        "Dagen en maanden krijgen geen hoofdletter, landen wel. Achter een indirecte vraag komt geen vraagteken. Bij een directe vraag staat het vraagteken binnen de aanhalingstekens."),
    sleep(
        "Na een opsomming die je aankondigt, zet je een [[dubbele punt]]. Een zin die je bewust onafgemaakt laat, eindigt met een [[beletselteken]]. Twee hoofdzinnen die nauw samenhangen, kan je scheiden met een [[puntkomma]].",
        ["vraagteken", "aanhalingsteken"],
        "De dubbele punt kondigt iets aan, het beletselteken bestaat uit drie puntjes en de puntkomma scheidt sterker dan een komma maar minder sterk dan een punt."),

    # Betekenis en gevoelswaarde
    koppel(
        "Koppel elk woord aan een woord met dezelfde betekenis maar een negatievere gevoelswaarde.",
        [
            ["zuinig", "gierig"],
            ["slank", "mager"],
            ["nieuwsgierig", "bemoeiziek"],
            ["praten", "kletsen"],
        ],
        ["vrijgevig", "gezellig"],
        "Synoniemen kunnen een andere gevoelswaarde hebben. 'Gierig' en 'bemoeiziek' klinken als verwijt, 'zuinig' en 'nieuwsgierig' veel neutraler."),
    tabel(
        "Welke vorm van beeldspraak is het?",
        [
            ("Ze is zo sterk als een beer.", "Vergelijking"),
            ("De wind huilde om het huis.", "Personificatie"),
            ("Mijn broer is een wandelende encyclopedie.", "Metafoor"),
        ],
        "Een vergelijking gebruikt 'als' of 'zoals'. Bij een personificatie krijgt iets een menselijke eigenschap. Bij een metafoor noem je het ene met de naam van het andere, zonder 'als'.",
        kolommen=["Vergelijking", "Metafoor", "Personificatie"]),
    mk("Wat betekent de uitdrukking 'iemand een hart onder de riem steken'?",
       ["iemand moed inspreken", "iemand stevig vastpakken", "iemand iets verwijten", "iemand iets laten beloven"],
       0,
       "Bij een uitdrukking haal je de betekenis niet uit de losse woorden. Je moedigt iemand aan die het moeilijk heeft."),

    inv("Welk leesteken staat er tussen 'auto' en 's' in het meervoud 'auto's'? Geef de naam.",
        ["apostrof", "de apostrof", "een apostrof"],
        "Bij woorden op een lange klinker zoals auto, foto of menu zet je een apostrof voor de s, anders zou je 'autos' anders uitspreken."),
    tabel(
        "Is de zin enkelvoudig of samengesteld?",
        [
            ("Na de training dronken alle spelers samen iets in de kantine.", "Enkelvoudig"),
            ("Ik bleef thuis, want ik had koorts.", "Samengesteld"),
            ("De leerling die het snelst klaar was, mocht naar buiten.", "Samengesteld"),
            ("Morgen vertrekken we heel vroeg naar zee.", "Enkelvoudig"),
        ],
        "Tel de persoonsvormen. Een enkelvoudige zin heeft er één, een samengestelde zin twee of meer: 'bleef' en 'had', 'was' en 'mocht'.",
        kolommen=["Enkelvoudig", "Samengesteld"]),
    mk("Je solliciteert per mail voor een vakantiejob. Welke slotzin past het best?",
       ["Ik hoop u binnenkort te ontmoeten voor een gesprek.", "Laat maar iets weten als het jou past, ok?", "Bel me, ik zit toch de hele dag thuis te niksen.", "Groetjes en tot gauw, xxx van mij aan jullie allemaal!"],
       0,
       "In een sollicitatie kies je een formeel register: u in plaats van jij, standaardtaal en geen chattaal of kusjes."),
    inv("Hoe noem je een woord dat het Nederlands uit een andere taal overnam, zoals 'computer' of 'garage'?",
        ["leenwoord", "een leenwoord", "leenwoorden"],
        "Een leenwoord komt uit een andere taal. Een inheems woord hoort van oudsher bij het Nederlands."),

    # Fictie
    tabel(
        "Is dit fictie of non-fictie?",
        [
            ("een biografie van een wielrenner", "Non-fictie"),
            ("een sprookje over een pratende vos", "Fictie"),
            ("een historische roman met verzonnen gesprekken", "Fictie"),
            ("een reportage over de bouw van een brug", "Non-fictie"),
        ],
        "Non-fictie vertelt over wat echt gebeurd is. Zodra de schrijver personages of gesprekken verzint, is het fictie, ook als het verhaal op ware feiten steunt.",
        kolommen=["Fictie", "Non-fictie"]),
    volgorde(
        "Zet de delen van een klassieke verhaallijn in de juiste volgorde.",
        ["de beginsituatie wordt geschetst", "er ontstaat een probleem", "de spanning loopt op tot een hoogtepunt", "het probleem wordt opgelost", "het verhaal sluit af"],
        "Veel verhalen volgen dit patroon: begin, conflict, climax, oplossing en slot."),
    mk("In een verhaal springt de schrijver plots terug naar de kindertijd van het hoofdpersonage. Hoe noem je dat?",
       ["een flashback", "een vooruitwijzing", "een open einde", "een cliffhanger"],
       0,
       "Een flashback is een terugblik naar iets wat vroeger gebeurde. Een vooruitwijzing verwijst naar later."),

    # Spreken en lichaamstaal
    tabel(
        "Helpt dit om sterk over te komen bij een mondelinge presentatie?",
        [
            ("je publiek aankijken", J),
            ("met je armen gekruist voor je borst staan", F),
            ("duidelijk articuleren en niet te snel spreken", J),
            ("je volledige tekst van een blad aflezen", F),
        ],
        "Oogcontact, een open houding en duidelijke articulatie maken je betrouwbaar en verstaanbaar. Gekruiste armen lijken afwerend en wie afleest, verliest het contact met het publiek."),

    # Schrijfopdracht
    open_("Je wil dat de school een overdekte fietsenstalling bouwt. Schrijf een korte alinea van vier tot zes zinnen voor de schoolkrant. Geef je standpunt, twee argumenten en een conclusie. Gebruik minstens twee signaalwoorden.",
          "Onze school heeft dringend een overdekte fietsenstalling nodig. Ten eerste komen meer dan driehonderd leerlingen met de fiets, en hun fietsen staan nu in de regen. Bovendien roesten kettingen en remmen sneller, waardoor fietsen minder veilig worden. Daarom vragen we de directie om nog dit schooljaar een overdekte stalling te bouwen.",
          "Een goed antwoord heeft een duidelijke stelling, twee argumenten die echt een reden geven, een conclusie en signaalwoorden zoals 'ten eerste', 'bovendien' en 'daarom'. Het register past bij een schoolkrant: standaardtaal, beleefd en zakelijk."),
]
