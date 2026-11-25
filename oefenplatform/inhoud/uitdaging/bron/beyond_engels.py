# -*- coding: utf-8 -*-
"""Uitdaging Engels 🌍 Beyond doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen. Een zelf geschreven opiniestuk en een klachtenmail om op te
klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een
korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken
van Engels Beyond doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_engels.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Engels"
BESTAND = "beyond-engels-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/engels-beyond-uitdaging"
ARTIKEL = "artikel-smartphones.svg"
MAIL = "mail-klacht.svg"


def zin(i, n=6):
    """Klikvak van zin i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Opiniestuk (prent)
    klik("Lees de tekst. Klik op de zin waarin de schrijver zijn eigen mening geeft.",
         ARTIKEL, [zin(5)],
         "'In my opinion' kondigt een persoonlijke mening aan. De zinnen ervoor geven weer wat anderen denken of wat er gebeurt."),
    klik("Klik op de zin die met een signaalwoord een tegenstelling inleidt.",
         ARTIKEL, [zin(3)],
         "'However' betekent echter. Het zet de critici tegenover de voorstanders uit zin 2."),
    met_prent(ARTIKEL, tabel(
        "Welke functie heeft het signaalwoord?",
        [
            ("However (zin 3)", "Tegenstelling"),
            ("Therefore (zin 6)", "Gevolg of conclusie"),
            ("In my opinion (zin 5)", "Mening"),
        ],
        "'However' brengt een tegenstelling, 'therefore' een gevolg of besluit, en 'in my opinion' kondigt een standpunt aan.",
        kolommen=["Tegenstelling", "Gevolg of conclusie", "Mening"])),
    met_prent(ARTIKEL, mk(
        "Welk standpunt verdedigt de schrijver van dit opiniestuk?",
        ["Leer leerlingen verstandig met hun gsm omgaan in plaats van hem te verbieden.", "Gsm's moeten volledig uit elke school in Europa verdwijnen, ook tijdens de pauzes.", "Leerlingen concentreren zich beter met hun gsm aan, dus ze moeten hem altijd bij hebben.", "Scholen mogen zelf niets beslissen; de regering moet de regels voor gsm's maken."],
        0,
        "In zin 5 vindt de schrijver een volledig verbod te ver gaan, en in zin 6 stelt hij voor om leerlingen te leren hoe ze hun gsm verstandig gebruiken.")),
    met_prent(ARTIKEL, keuze(
        "Deze tekst is vooral [[*argumentatief|prescriptief|narratief]]. Het woord 'wisely' in zin 6 is een [[*bijwoord|bijvoeglijk naamwoord|werkwoord]].",
        "De schrijver weegt argumenten af en neemt een standpunt in. 'Wisely' zegt iets over het werkwoord 'use' en eindigt op -ly: een bijwoord.")),

    # Klachtenmail (prent)
    klik("Lees de mail. Klik op de zin die niet past in een formele brief.",
         MAIL, [zin(4)],
         "'Total rubbish' en 'mate' zijn informeel en onbeleefd. In een formele klachtenbrief blijf je zakelijk."),
    klik("Klik op de zin waarin de schrijfster vraagt wat ze wil dat de winkel doet.",
         MAIL, [zin(5)],
         "'I would be grateful if you could...' is een beleefde, formele manier om iets te vragen: een nieuw paar of haar geld terug."),
    met_prent(MAIL, tabel(
        "Klopt dit over de mail?",
        [
            ("'Yours faithfully' past bij de aanspreking 'Dear Sir or Madam'.", J),
            ("De schrijfster kent de naam van de persoon die de mail zal lezen.", F),
            ("Zin 2 zegt meteen waarom ze schrijft.", J),
            ("De mail is een voorbeeld van een narratieve tekst.", F),
        ],
        "Ken je de naam niet, dan schrijf je 'Dear Sir or Madam' en sluit je af met 'Yours faithfully'. Een klachtenbrief wil iets bereiken: hij is niet narratief.")),
    met_prent(MAIL, mk(
        "Hoe kan je zin 4 formeel herschrijven?",
        ["I am very disappointed with the quality of this product.", "This thing is a joke and I want my cash back right now.", "Hey, your headphones are pretty bad, you know that?", "Whatever, just send me something else that actually works."],
        0,
        "Een formele zin is zakelijk en beleefd, zonder spreektaal of verwijten."),
    ),

    # Tekstsoorten en woordenschat
    tabel(
        "Tot welk tekstsoort behoort elk van deze Engelse zinnen?",
        [
            ("Preheat the oven to 180 degrees and grease the tin.", "Prescriptief"),
            ("It was a dark night when the stranger knocked on the door.", "Narratief"),
            ("The museum is open from 10 a.m. to 6 p.m. every day.", "Informatief"),
            ("Vote for a greener town: join our campaign today!", "Persuasief"),
        ],
        "Een recept geeft instructies, een verhaal vertelt, openingsuren informeren en een campagne wil je overtuigen om iets te doen.",
        kolommen=["Informatief", "Prescriptief", "Narratief", "Persuasief"]),
    koppel(
        "Koppel het Engelse woord aan de juiste vertaling.",
        [
            ["a landlord", "een verhuurder"],
            ["a GP", "een huisarts"],
            ["a degree", "een universitair diploma"],
            ["a delay", "een vertraging"],
            ["a novel", "een roman"],
        ],
        ["een nieuwtje", "een graad Celsius"],
        "Let op valse vrienden: a novel is geen novelle en a degree is hier geen graad op de thermometer."),
    sorteer(
        "Bij welk woordveld hoort dit woord?",
        ["Gezondheid", "Werk en geld", "Politiek"],
        [
            ["a prescription", "Gezondheid"],
            ["a salary", "Werk en geld"],
            ["an election", "Politiek"],
            ["a symptom", "Gezondheid"],
            ["a job interview", "Werk en geld"],
            ["the House of Commons", "Politiek"],
        ],
        "Een voorschrift en een symptoom horen bij de dokter, een loon en een sollicitatiegesprek bij werk, verkiezingen en het Lagerhuis bij politiek."),
    inv("Welk Engels woord betekent een veiligheidskopie van je bestanden? Eén woord.",
        ["backup", "back-up"],
        "A backup is een kopie die je bewaart voor het geval je bestanden verloren gaan."),
    keuze(
        "Iemand die geen zorg besteedt aan zijn werk, is [[*careless|careful|caring]]. Een product dat de natuur niet schaadt, is [[*environmentally friendly|environmentally harmful]].",
        "Het achtervoegsel -less betekent zonder: careless is zonder zorg. Environmentally friendly is milieuvriendelijk."),

    # Naamwoorden en lidwoorden
    tabel(
        "Wat is het meervoud?",
        [
            ("child", "children"),
            ("mouse", "mice"),
            ("knife", "knives"),
            ("tooth", "teeth"),
        ],
        "Deze woorden hebben een onregelmatig meervoud. Bij knife wordt de f een v en komt er -es achter.",
        kolommen=["children", "mice", "knives", "teeth"]),
    keuze(
        "I need [[*an|a]] umbrella and [[*a|an]] university map. Can I have [[*some|any]] water, please? There isn't [[*any|some]] milk left.",
        "An voor een klinkerklank, a voor een medeklinkerklank: university begint met een j-klank. Some in bevestigende zinnen en beleefde vragen, any in ontkennende zinnen."),
    mk("Welke zin is juist?",
       ["There are fewer students in class today.", "There are less students in the class today.", "There is less students in class today.", "There is fewer student in class today."],
       0,
       "Fewer gebruik je bij telbare zelfstandige naamwoorden in het meervoud, less bij ontelbare: less water, fewer students."),

    # Voornaamwoorden en betrekkelijke bijzinnen
    keuze(
        "The girl [[*who|which]] won the race is my cousin. The bike [[*which|who]] she rode was new. That's the man [[*whose|who's]] car was stolen.",
        "Who verwijst naar personen, which naar dingen. Whose betekent van wie; who's is een verkorting van who is."),
    tabel(
        "Welk Engels voornaamwoord vult de zin juist aan?",
        [
            ("They helped ___ (elkaar).", "each other"),
            ("She hurt ___ while cooking.", "herself"),
            ("Is this your book or ___ ? (het mijne)", "mine"),
        ],
        "Each other drukt wederkerigheid uit, herself is wederkerend en mine is een zelfstandig bezittelijk voornaamwoord.",
        kolommen=["mine", "herself", "each other"]),

    # Bijvoeglijke naamwoorden, bijwoorden en voorzetsels
    keuze(
        "She speaks English very [[*well|good]]. This test is [[*more difficult|difficulter]] than the last one. He drives [[*carefully|careful]].",
        "Bij een werkwoord hoort een bijwoord: well en carefully. Lange bijvoeglijke naamwoorden krijgen more in de vergrotende trap."),
    tabel(
        "Vul het juiste voorzetsel in.",
        [
            ("I'm interested ___ history.", "in"),
            ("It depends ___ the weather.", "on"),
            ("She is good ___ maths.", "at"),
            ("We're looking forward ___ the holidays.", "to"),
        ],
        "Deze voorzetsels horen vast bij het woord ervoor: interested in, depend on, good at, look forward to.",
        kolommen=["in", "on", "at", "to"]),
    mk("Wat betekent: « He hardly studied for the test »?",
       ["Hij heeft amper gestudeerd voor de toets.", "Hij heeft heel hard gestudeerd voor de toets.", "Hij heeft te lang gestudeerd voor de toets.", "Hij heeft nooit een toets moeten afleggen."],
       0,
       "Hardly betekent nauwelijks of amper. Hard is hard of zwaar: he studied hard."),

    # Tijden
    keuze(
        "Listen! Someone [[*is knocking|knocks]] at the door. I [[*have lived|live]] here since 2020. We [[*went|have gone]] to Spain last summer.",
        "Iets dat nu bezig is: present continuous. Sinds een moment tot nu: present perfect. Een afgesloten tijdstip in het verleden (last summer): past simple."),
    tabel(
        "In welke tijd staat het werkwoord?",
        [
            ("She had already left when I arrived.", "Past perfect"),
            ("They were playing football at five o'clock.", "Past continuous"),
            ("I have never seen snow.", "Present perfect"),
            ("He walks to school every day.", "Present simple"),
        ],
        "Had + voltooid deelwoord: past perfect. Was/were + -ing: past continuous. Have/has + voltooid deelwoord: present perfect. Een gewoonte: present simple.",
        kolommen=["Present simple", "Present perfect", "Past continuous", "Past perfect"]),
    inv("Vul de juiste vorm in: « By the time we got to the station, the train ___ (to leave). » Twee woorden.",
        ["had left"],
        "Iets wat nog vroeger gebeurde dan een ander moment in het verleden, zet je in de past perfect: had left."),
    tabel(
        "Wat is de verleden tijd (past simple)?",
        [
            ("to bring", "brought"),
            ("to catch", "caught"),
            ("to buy", "bought"),
            ("to teach", "taught"),
        ],
        "Deze onregelmatige werkwoorden lijken op elkaar: brought en bought, caught en taught.",
        kolommen=["brought", "caught", "bought", "taught"]),

    # Toekomst, modale werkwoorden, gerund
    keuze(
        "Look at those clouds! It [[*is going to|will]] rain. You [[*mustn't|don't have to]] smoke here: it is forbidden. You [[*don't have to|mustn't]] wear a uniform, but you may.",
        "Going to gebruik je bij een voorspelling op basis van wat je ziet. Mustn't is een verbod, don't have to betekent dat iets niet hoeft."),
    sorteer(
        "Volgt na dit werkwoord een gerund (-ing) of een to-infinitive?",
        ["Gerund", "To-infinitive"],
        [
            ["enjoy", "Gerund"],
            ["decide", "To-infinitive"],
            ["avoid", "Gerund"],
            ["hope", "To-infinitive"],
            ["finish", "Gerund"],
            ["want", "To-infinitive"],
        ],
        "I enjoy swimming, avoid making mistakes, finish working. Maar: I decided to go, I hope to see you, I want to leave."),

    # Zinsbouw, indirecte rede, passief
    volgorde(
        "Zet de woorden in de juiste volgorde.",
        ["She", "often", "visits", "her grandmother", "in Bristol", "on Sundays"],
        "Onderwerp, frequentiebijwoord, werkwoord, voorwerp, plaats, tijd: dat is de vaste Engelse volgorde."),
    tabel(
        "Zet in de indirecte rede. Hoe begint de zin?",
        [
            ("'I am tired,' she said.", "She said that she was tired."),
            ("'I will call you,' he said.", "He said that he would call me."),
            ("'Do you like tea?' he asked.", "He asked if I liked tea."),
        ],
        "In de indirecte rede schuift de tijd een stap terug: am wordt was, will wordt would. Een ja-neevraag wordt ingeleid met if of whether.",
        kolommen=["She said that she was tired.", "He said that he would call me.", "He asked if I liked tea."]),
    mk("Welke zin staat in de passieve vorm?",
       ["The bridge was built in 1890.", "They built the bridge in 1890.", "The bridge has stood here since 1890.", "Builders worked on the bridge in 1890."],
       0,
       "Een passieve zin heeft een vorm van to be met een voltooid deelwoord: was built. Het onderwerp ondergaat de handeling."),
    inv("Zet in de passieve vorm: « Someone has stolen my bike. » Begin met « My bike ».",
        ["My bike has been stolen.", "My bike has been stolen", "my bike has been stolen.", "my bike has been stolen"],
        "Present perfect passief: has been + voltooid deelwoord. Wie het deed, is onbekend en laat je weg."),
    sleep(
        "If I [[had]] more time, I [[would]] learn another language. If it rains tomorrow, we [[will]] stay at home.",
        ["have", "did"],
        "Een onwaarschijnlijke situatie: if + past simple, would + infinitief. Een reële mogelijkheid: if + present simple, will + infinitief."),

    # Cultuur
    tabel(
        "Klopt dit over de Britse en Amerikaanse cultuur?",
        [
            ("Het Britse parlement bestaat uit het House of Commons en het House of Lords.", J),
            ("In Groot-Brittannië rijdt men links.", J),
            ("Chips betekent in het Amerikaans Engels hetzelfde als in het Brits Engels.", F),
        ],
        "Brits Engels chips zijn frieten; Amerikanen zeggen daarvoor fries en noemen chips wat Britten crisps noemen."),

    # Extra
    mk("Wat betekent: « I used to play the piano »?",
       ["Vroeger speelde ik piano, nu niet meer.", "Ik ben gewoon om elke dag piano te spelen.", "Ik heb de piano gebruikt om op te oefenen.", "Ik ga binnenkort beginnen met pianospelen."],
       0,
       "Used to + infinitief beschrijft een gewoonte in het verleden die voorbij is. 'Gewoon zijn aan' is to be used to + -ing."),
    keuze(
        "If you heat ice, it [[*melts|melted|would melt]]. If I [[*had known|knew|have known]] about the party, I would have come.",
        "Een algemene waarheid: if + present, present. Een gemiste kans in het verleden: if + past perfect, would have + voltooid deelwoord."),
    tabel(
        "Welk Engels woord hoort bij deze omschrijving rond solliciteren?",
        [
            ("Je schriftelijke kandidatuur", "an application"),
            ("Je overzicht van opleiding en ervaring", "a CV"),
            ("Het geld dat je per maand verdient", "a salary"),
        ],
        "An application is een sollicitatie, a CV (Amerikaans: a résumé) je levensloop, a salary je maandloon.",
        kolommen=["an application", "a CV", "a salary"]),
    inv("Vul de vraagstaart in: « You have finished your homework, ___ ? » Twee woorden.",
        ["haven't you", "have you not"],
        "Na een bevestigende zin volgt een ontkennende vraagstaart met hetzelfde hulpwerkwoord: haven't you?"),
    mk("Welke zin bevat een fout?",
       ["She doesn't likes coffee at breakfast.", "He has been working here for ten years.", "They didn't go to the cinema yesterday.", "We usually have dinner at seven o'clock."],
       0,
       "Na doesn't volgt de infinitief zonder -s: she doesn't like coffee."),

    # Schrijfopdracht
    open_("Write a short formal email (5 to 7 sentences) to a hotel in London. You want to book a room for two nights in July and you ask whether breakfast is included. Use a correct greeting and ending.",
          "Dear Sir or Madam, I am writing to book a double room for two nights, from 12 to 14 July. We will arrive in the afternoon of the 12th. Could you please tell me whether breakfast is included in the price? I would also like to know if there is a car park near the hotel. I look forward to hearing from you. Yours faithfully, Lies Janssens",
          "Een goed antwoord heeft een formele aanspreking en afsluiting die bij elkaar passen, zegt meteen waarom je schrijft, stelt de vraag beleefd (Could you please...) en gebruikt geen spreektaal of afkortingen."),
]
