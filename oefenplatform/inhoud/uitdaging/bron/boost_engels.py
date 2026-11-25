# -*- coding: utf-8 -*-
"""Uitdaging Engels 🚀 Boost doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door elkaar
halen. Een kort verhaal en een mail om op te klikken, tabellen, keuzelijsten,
slepen, koppelen, sorteren, volgorde, invulvragen en een korte
schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Engels Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_engels.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Engels"
BESTAND = "boost-engels-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/engels-boost-uitdaging"
VERHAAL = "verhaal-trein.svg"
MAIL = "mail-feestje.svg"

# klikvakken: _blad.zone(i, 6)
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Verhaal (prent)
    klik("Lees het verhaal 'A rainy Saturday'. Klik op de zin met een past perfect.",
         VERHAAL, [Z[3]],
         "'The train had already left' is een past perfect (had + voltooid deelwoord). Het vertrek van de trein gebeurde vóór ze op het perron kwamen."),
    klik("Klik op de zin die een achtergrond schetst met de past continuous.",
         VERHAAL, [Z[2]],
         "'They were cycling' (was/were + -ing) beschrijft wat er aan de gang was. Dat is de typische achtergrond in een verhaal."),
    klik("Klik op de zin die naar de toekomst kijkt.",
         VERHAAL, [Z[6]],
         "'They will never forget' gebruikt will + infinitief en kijkt vooruit."),
    met_prent(VERHAAL, tabel(
        "Lees het verhaal opnieuw. Klopt dit?",
        [
            ("Tom en zijn zus gingen met de fiets naar het station.", J),
            ("Ze kwamen te laat voor de trein.", J),
            ("Tom was boos op zijn zus.", F),
            ("De volgende trein kwam pas een uur later.", F),
        ],
        "Ze fietsten naar het station (by bike) en de trein was al weg. De zus was boos, Tom lachte. Er kwam een trein in twintig minuten.")),
    met_prent(VERHAAL, keuze(
        "In zin 4 legt 'but' een [[*tegenstelling|oorzaak|opsomming]]. In zin 5 verwijst 'he' naar [[*Tom|de trein|Toms zus]].",
        "'But' kondigt een tegenstelling aan: de zus was boos, Tom lachte. 'He' verwijst naar de enige man in het verhaal, Tom.")),

    # Mail (prent)
    klik("Lees de mail aan Lisa. Klik op de zin waarmee Sara haar uitnodigt.",
         MAIL, [Z[3]],
         "'Would you like to come …?' is een beleefde uitnodiging."),
    klik("Klik op de zin waarin Sara een advies geeft.",
         MAIL, [Z[5]],
         "'You should …' geeft een advies."),
    met_prent(MAIL, mk(
        "Waarom past 'Love, Sara' hier als afsluiter?",
        ["Het is een informele mail aan een vriendin.", "Het is een formele brief aan een onbekende.", "Sara kent de naam van de ontvanger niet goed.", "In elke Engelse mail sluit je altijd zo af."],
        0,
        "'Love' en 'Hi' passen bij een informele mail. In een formele brief aan een onbekende gebruik je 'Dear Sir or Madam' en 'Yours faithfully'.")),
    met_prent(MAIL, keuze(
        "In zin 4 betekent 'you don't have to bring anything' dat Lisa [[*niets hoeft mee te brengen|niets mag meebrengen]]. Je gebruikt 'anything' omdat de zin [[*ontkennend|bevestigend]] is.",
        "'Don't have to' betekent 'hoeft niet'. 'Mustn't' betekent 'mag niet'. In vragen en ontkenningen gebruik je anything.")),

    # Tegenwoordige tijden
    tabel(
        "Welke tijd past het best?",
        [
            ("She usually ___ (walk) to school.", "Present simple"),
            ("Look! It ___ (snow).", "Present continuous"),
            ("I ___ (live) here since 2020.", "Present perfect"),
            ("Water ___ (boil) at 100 °C.", "Present simple"),
        ],
        "Gewoontes en feiten: present simple. Iets wat nu bezig is: present continuous. Iets wat in het verleden begon en nog duurt, met since: present perfect.",
        kolommen=["Present simple", "Present continuous", "Present perfect"]),
    inv("Vul de juiste vorm in: My brother ___ (study) every evening. Schrijf één woord.",
        ["studies"],
        "Derde persoon enkelvoud: -s. Na medeklinker + y wordt het -ies: studies."),
    keuze(
        "I have lived in Ghent [[*for|since]] ten years. She has been waiting [[*since|for]] nine o'clock.",
        "For gebruik je bij een duur (ten years). Since gebruik je bij een beginmoment (nine o'clock)."),

    # Verleden en toekomst
    tabel(
        "Is de past simple juist geschreven?",
        [
            ("buy → bought", J),
            ("stop → stoped", F),
            ("go → went", J),
            ("try → tried", J),
        ],
        "Stop verdubbelt de medeklinker: stopped. Buy en go zijn onregelmatig, try wordt tried."),
    keuze(
        "Kijk naar die donkere wolken: it [[*is going to|will]] rain. Wacht, ik help je met die zware tas: I [[*will|am going to]] carry it.",
        "Going to gebruik je als je iets al ziet aankomen. Will gebruik je bij een plotse beslissing of aanbod."),
    inv("Vul aan met één woord: ___ you see the match yesterday? Gebruik de juiste hulpwerkwoordvorm.",
        ["Did", "did"],
        "In een vraag in de past simple gebruik je did, en het werkwoord blijft in de basisvorm: Did you see …?"),

    # Modals
    koppel(
        "Koppel de zin aan de betekenis.",
        [
            ["You mustn't smoke here.", "Het is verboden."],
            ["You don't have to come.", "Het is niet nodig."],
            ["You should rest.", "Het is een goed advies."],
            ["You can swim.", "Je bent het in staat."],
        ],
        [],
        "Mustn't is een verbod, don't have to betekent dat het niet nodig is, should geeft een advies en can drukt een vermogen uit."),
    mk("Welke zin vraagt het meest beleefd om toestemming?",
       ["May I open the window, please?", "Open the window now, it is too warm!", "I open the window and that is it.", "You must open the window for me."],
       0,
       "Met 'May I …?' vraag je op een formele manier om toestemming."),

    # Infinitief en gerund
    sorteer(
        "Welke vorm volgt na dit werkwoord?",
        ["-ing-vorm", "to + infinitief"],
        [
            ["enjoy", "-ing-vorm"],
            ["want", "to + infinitief"],
            ["finish", "-ing-vorm"],
            ["decide", "to + infinitief"],
        ],
        "Na enjoy en finish komt de -ing-vorm: I enjoy reading. Na want en decide komt to + infinitief: I want to go."),

    # Voornaamwoorden
    keuze(
        "This is the girl [[*whose|who|which]] bike was stolen. The phone [[*that|who]] I bought last week is broken.",
        "Whose geeft een bezit aan. Bij een ding gebruik je that of which, niet who."),
    tabel(
        "Is deze Engelse zin met een voornaamwoord juist?",
        [
            ("She hurt herself when she fell.", J),
            ("This bag is my.", F),
            ("Everybody is here.", J),
            ("These books are for they.", F),
        ],
        "Wederkerend: herself. Een zelfstandig bezittelijk voornaamwoord: mine. Everybody neemt een enkelvoud. Na een voorzetsel: them."),

    # Bijvoeglijk en bijwoord
    keuze(
        "He sings very [[*well|good]]. This soup smells [[*good|well]].",
        "Bij een werkwoord als zingen hoort het bijwoord well. Na een koppelwerkwoord als smell komt een bijvoeglijk naamwoord: good."),
    tabel(
        "Is de vergrotende of overtreffende trap juist?",
        [
            ("big → bigger", J),
            ("good → goodest", F),
            ("expensive → more expensive", J),
            ("bad → worst", J),
        ],
        "Big verdubbelt de medeklinker. Good wordt better en best. Lange woorden krijgen more en most. Bad wordt worse en worst."),
    keuze(
        "I was born [[*on|in|at]] 14 March. We arrived [[*at|to]] the station at six.",
        "Bij een datum gebruik je on. Je komt aan at een station (een punt) en in een stad of land."),

    # Zelfstandige naamwoorden en hoeveelheden
    tabel(
        "Wat is het meervoud?",
        [
            ("child → children", J),
            ("city → citys", F),
            ("sheep → sheep", J),
            ("knife → knives", J),
        ],
        "City wordt cities. Child en sheep zijn onregelmatig, knife wordt knives."),
    keuze(
        "How [[*much|many]] water do you need? There are only a [[*few|little]] students in the classroom.",
        "Much en a little bij ontelbare woorden zoals water. Many en a few bij telbare woorden zoals students."),
    inv("Schrijf het rangtelwoord bij 3 voluit in het Engels.",
        ["third"],
        "One, two, three → first, second, third."),

    # Zinsbouw
    volgorde(
        "Zet de woorden in de juiste volgorde: een vraag naar een gewoonte.",
        ["Does", "your sister", "play", "tennis", "on Sundays?"],
        "Een vraag in de present simple: does + onderwerp + basisvorm van het werkwoord."),
    keuze(
        "Unless you hurry, you will miss the bus. Dat betekent: [[*als je je niet haast|als je je haast]], mis je de bus. If it rains tomorrow, we [[*will stay|would stay|stayed]] at home.",
        "Unless betekent 'als … niet'. In een voorwaardelijke zin over iets wat echt kan gebeuren: if + present simple, will + infinitief."),

    # Tekst en verbanden
    sorteer(
        "Welk verband legt dit signaalwoord?",
        ["Tegenstelling", "Oorzaak", "Gevolg"],
        [
            ["although", "Tegenstelling"],
            ["because", "Oorzaak"],
            ["so", "Gevolg"],
            ["despite", "Tegenstelling"],
            ["therefore", "Gevolg"],
        ],
        "Although en despite: tegenstelling. Because: oorzaak. So en therefore: gevolg."),
    mk("'The library will be closed from 3 to 10 August for building work.' Welke tekstsoort is dit vooral?",
       ["informatief", "verhalend", "overtuigend", "literair en poëtisch"],
       0,
       "De tekst deelt een feit mee zonder mening of verhaal: informatief."),

    # Woordenschat en cultuur
    koppel(
        "Koppel het Britse woord aan het Amerikaanse woord.",
        [
            ["lift", "elevator"],
            ["autumn", "fall"],
            ["flat", "apartment"],
            ["biscuit", "cookie"],
        ],
        ["platform"],
        "Britten en Amerikanen gebruiken soms een ander woord voor hetzelfde."),
    sleep(
        "Mijn zus heeft een zoon. Die jongen is mijn [[nephew]]. Haar dochter is mijn [[niece]].",
        ["cousin", "uncle"],
        "Nephew is neef (zoon van je broer of zus), niece is nicht. Cousin is het kind van je oom of tante."),
    tabel(
        "Klopt dit over de Engelstalige wereld?",
        [
            ("Een Britse datum 5/3/2027 is 5 maart 2027.", J),
            ("Football betekent in de Verenigde Staten hetzelfde als bij ons.", F),
            ("Het Verenigd Koninkrijk bestaat uit vier landsdelen.", J),
        ],
        "Britten schrijven eerst de dag. In de VS is football American football; ons voetbal heet daar soccer."),
    mk("Hoe begin je een mail aan een onbekende medewerker van een school?",
       ["Dear Sir or Madam,", "Hi mate, how are you doing?", "Hey there, what's up?", "Love, see you soon,"],
       0,
       "In een formele mail aan iemand van wie je de naam niet kent, begin je met 'Dear Sir or Madam,'."),
    sorteer(
        "Hoort deze Engelse zin of afsluiter in een formele of een informele mail?",
        ["Formeel", "Informeel"],
        [
            ["Yours faithfully", "Formeel"],
            ["See you soon!", "Informeel"],
            ["I am writing to ask about …", "Formeel"],
            ["Thanks a lot for your message!", "Informeel"],
        ],
        "Een formele mail is beleefd en volledig. Een informele mail aan een vriend mag kort en hartelijk zijn."),

    mk("Wat is de past simple van 'to think'?",
       ["thought", "thinked", "thank", "thinking"],
       0,
       "Think is onregelmatig: think – thought – thought."),
    inv("Vul aan met één woord: Look, the children are ___ (swim) in the lake.",
        ["swimming"],
        "Kort woord met één klinker en één medeklinker op het einde: de medeklinker verdubbelt. Swim wordt swimming."),
    mk("Je bent in Londen en hebt hoofdpijn. Waar koop je pijnstillers?",
       ["at the chemist's", "at the butcher's", "at the estate agent's", "at the platform"],
       0,
       "Een chemist's is in het Verenigd Koninkrijk een apotheek. Een butcher's is een slagerij, een estate agent verkoopt huizen."),
    # Tijd en getallen
    keuze(
        "'Quarter to nine' is [[*8.45|9.15|9.45]]. 'Half past seven' is [[*7.30|6.30]].",
        "Quarter to = kwart voor. Half past seven = half acht in het Nederlands, dus 7.30."),

    # Schrijfopdracht
    open_("Schrijf een korte mail van 60 à 80 woorden aan een Engelse vriend. Vertel wat je vorig weekend deed en nodig hem uit voor iets volgend weekend.",
          "Hi James,\nThanks for your last message! Last weekend I went to the seaside with my family. We walked on the beach and ate fish and chips. On Sunday it rained, so we watched a film at home. Would you like to come to the cinema with me next Saturday? The film starts at 3 pm. Let me know if you can come!\nBest,\nLotte",
          "Een goed antwoord heeft een aanspreking en afsluiter, gebruikt de past simple voor het weekend, nodigt uit met een vaste formule (Would you like to …?) en blijft binnen het aantal woorden."),
]
