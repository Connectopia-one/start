# -*- coding: utf-8 -*-
"""Uitdaging Engels 🌍 Beyond dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen. Een zelf geschreven review en een bericht om op te klikken,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde en een korte
schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Engels Beyond dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_df_engels.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Engels"
BESTAND = "beyond-df-engels-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/engels-beyond-df-uitdaging"
REVIEW = "review-hostel.svg"
BERICHT = "bericht-mia.svg"


def zin(i, n=6):
    """Klikvak van zin i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Review (prent)
    klik("Lees de review. Klik op de zin met een nadeel van de jeugdherberg.",
         REVIEW, [zin(4)],
         "'Unfortunately' (jammer genoeg) kondigt iets negatiefs aan: de douches waren vaak koud."),
    klik("Klik op de zin waarin de schrijver de jeugdherberg aanraadt.",
         REVIEW, [zin(6)],
         "'I would definitely recommend it' betekent: ik zou ze zeker aanraden."),
    klik("Klik op de zin die zegt hoe ver de jeugdherberg van een bezienswaardigheid ligt.",
         REVIEW, [zin(2)],
         "'Five minutes' walk from the castle' betekent vijf minuten te voet van het kasteel."),
    met_prent(REVIEW, tabel(
        "Klopt dit volgens de review?",
        [
            ("De schrijver bleef drie nachten.", J),
            ("Het ontbijt is duur voor Edinburgh.", F),
            ("Het personeel hielp bij het plannen van uitstappen.", J),
            ("De douches waren altijd warm.", F),
        ],
        "Zin 1 noemt drie nachten, zin 3 het behulpzame personeel. Het ontbijt is 'quite cheap' en de douches waren vaak koud.")),
    met_prent(REVIEW, keuze(
        "Een review is vooral een [[*beschouwende|prescriptieve|narratieve]] tekst: de schrijver geeft zijn [[*mening en ervaring|instructies|definitie]].",
        "Een review beschrijft en beoordeelt een ervaring. Ze helpt anderen kiezen.")),

    # Bericht (prent)
    klik("Lees het bericht van Mia. Klik op de zin waarin ze een voorstel doet.",
         BERICHT, [zin(4)],
         "'Shall we ...?' is een manier om iets voor te stellen: zullen we naar het strand rijden?"),
    klik("Klik op de zin die zegt tegen wanneer Jess moet antwoorden.",
         BERICHT, [zin(6)],
         "'Let me know by Thursday' betekent: laat het me weten tegen donderdag."),
    met_prent(BERICHT, tabel(
        "In welke tijd staat het werkwoord in het bericht?",
        [
            ("I've just got my driving licence", "Present perfect"),
            ("I passed the test this morning", "Past simple"),
            ("My dad is going to lend me his car", "Future (going to)"),
        ],
        "Have + voltooid deelwoord met 'just' is present perfect. Een afgelopen moment (this morning) vraagt past simple. Going to drukt een plan uit.",
        kolommen=["Present perfect", "Past simple", "Future (going to)"])),
    met_prent(BERICHT, mk(
        "Welk antwoord van Jess past het best bij het bericht?",
        ["Congrats! Saturday sounds great, see you at ten!", "Dear Madam, thank you for your kind letter of 3 May.", "I am writing to complain about your driving lessons.", "Yours faithfully, Jess, from the driving school."],
        0,
        "Het bericht is informeel en vraagt of Jess zaterdag mee wil. Een kort, vriendelijk antwoord past; formele briefzinnen niet.")),

    # Tekstsoorten en cultuur
    tabel(
        "Welk soort tekst is dit?",
        [
            ("Turn left at the second traffic lights.", "Instructie"),
            ("Once upon a time there lived a poor fisherman.", "Verhaal"),
            ("Big summer sale: everything half price!", "Reclame"),
            ("The Thames is 346 km long.", "Informatie"),
        ],
        "Een wegbeschrijving geeft instructies, een sprookje vertelt, een uitverkoop wil je overhalen te kopen en een feit informeert.",
        kolommen=["Informatie", "Instructie", "Verhaal", "Reclame"]),
    keuze(
        "In Groot-Brittannië betaal je met [[*pounds|euros|dollars]] en rijdt het verkeer [[*links|rechts]].",
        "De munt is het Britse pond (£) en men rijdt links."),
    tabel(
        "Brits of Amerikaans Engels?",
        [
            ("flat", "Brits"),
            ("apartment", "Amerikaans"),
            ("lorry", "Brits"),
            ("truck", "Amerikaans"),
        ],
        "Britten zeggen flat en lorry, Amerikanen apartment en truck.",
        kolommen=["Brits", "Amerikaans"]),

    # Woordvelden
    koppel(
        "Koppel het Engelse woord aan de vertaling.",
        [
            ["a ticket office", "een loket"],
            ["a pharmacy", "een apotheek"],
            ["a rent", "een huur"],
            ["a wage", "een loon"],
            ["a canteen", "een refter"],
        ],
        ["een zakdoek", "een rekening"],
        "Deze woorden komen uit de woordvelden reizen, gezondheid, wonen, werk en school."),
    sorteer(
        "Bij welk woordveld hoort het woord?",
        ["Eten", "Verkeer", "Natuur"],
        [
            ["a recipe", "Eten"],
            ["a roundabout", "Verkeer"],
            ["a forest", "Natuur"],
            ["a starter", "Eten"],
            ["a speed bump", "Verkeer"],
            ["pollution", "Natuur"],
        ],
        "Een recept en een voorgerecht horen bij eten, een rotonde en een verkeersdrempel bij verkeer, een bos en vervuiling bij natuur en milieu."),
    inv("Hoe zeg je 'een sollicitatiegesprek' in het Engels? Drie woorden, met lidwoord.",
        ["a job interview", "an interview"],
        "A job interview is een sollicitatiegesprek."),
    keuze(
        "Ik heb hoofdpijn: I have a [[*headache|headpain|headsick]]. Ik ben verkouden: I have a [[*cold|cool|chill]].",
        "Pijn in een lichaamsdeel krijgt vaak -ache: headache, toothache, stomachache. Verkouden zijn is 'to have a cold'."),

    # Naamwoorden en hoeveelheden
    keuze(
        "How [[*much|many]] money do you have? How [[*many|much]] tickets did you buy? I've got [[*a few|a little]] friends in London.",
        "Much en a little bij ontelbare woorden (money), many en a few bij telbare (tickets, friends)."),
    tabel(
        "Wat is het meervoud?",
        [
            ("a woman", "women"),
            ("a foot", "feet"),
            ("a city", "cities"),
            ("a box", "boxes"),
        ],
        "Woman en foot zijn onregelmatig. Medeklinker + y wordt -ies, en na x komt -es.",
        kolommen=["women", "feet", "cities", "boxes"]),

    # Voornaamwoorden
    keuze(
        "This is my brother, [[*who|which]] works in a hotel. That's the phone [[*which|who]] I bought last week. Is this bag [[*yours|your]]?",
        "Who verwijst naar personen, which naar dingen. Yours staat zelfstandig, zonder zelfstandig naamwoord erna."),
    tabel(
        "Vul het juiste voornaamwoord in.",
        [
            ("Tom and Lisa talked to ___ (elkaar) for hours.", "each other"),
            ("Be careful, you might cut ___ !", "yourself"),
            ("Give the keys to ___ , I'll open the door.", "me"),
        ],
        "Each other is wederkerig, yourself wederkerend, en na een voorzetsel staat de voorwerpsvorm me.",
        kolommen=["each other", "yourself", "me"]),

    # Bijvoeglijke naamwoorden en bijwoorden
    tabel(
        "Wat is de vergrotende trap?",
        [
            ("cheap", "cheaper"),
            ("expensive", "more expensive"),
            ("bad", "worse"),
            ("happy", "happier"),
        ],
        "Korte woorden krijgen -er, lange woorden more. Bad is onregelmatig, en bij happy wordt de y een i.",
        kolommen=["cheaper", "more expensive", "worse", "happier"]),
    keuze(
        "She sings [[*beautifully|beautiful]]. The soup smells [[*good|well]]. He arrived [[*late|lately]] for work.",
        "Bij een handelingswerkwoord hoort een bijwoord: beautifully. Na smell (koppelwerkwoord) volgt een bijvoeglijk naamwoord. Late is ook een bijwoord; lately betekent onlangs."),
    tabel(
        "Kies het juiste voorzetsel.",
        [
            ("My birthday is ___ May.", "in"),
            ("The meeting is ___ Monday.", "on"),
            ("The film starts ___ eight o'clock.", "at"),
        ],
        "In bij maanden en jaren, on bij dagen en datums, at bij een uur.",
        kolommen=["in", "on", "at"]),

    # Tijden
    keuze(
        "I usually [[*walk|am walking]] to school, but today I [[*am taking|take]] the bus. We [[*have known|know]] each other for ten years.",
        "Een gewoonte: present simple. Iets wat vandaag anders is: present continuous. For + periode tot nu: present perfect."),
    tabel(
        "Wat is het voltooid deelwoord (past participle)?",
        [
            ("to write", "written"),
            ("to drive", "driven"),
            ("to forget", "forgotten"),
            ("to choose", "chosen"),
        ],
        "Deze onregelmatige werkwoorden eindigen op -en in het voltooid deelwoord.",
        kolommen=["written", "driven", "forgotten", "chosen"]),
    inv("Vul de juiste vorm in: « While I ___ (to cook), the phone rang. » Twee woorden.",
        ["was cooking"],
        "Een handeling die bezig was toen iets anders gebeurde, staat in de past continuous: was cooking."),
    mk("Welke Engelse zin over een film van vorige week is juist?",
       ["I saw that film last week.", "I have seen that film last week.", "I have saw that film last week.", "I seen that film last week."],
       0,
       "Met een afgesloten tijdstip (last week) gebruik je de past simple: I saw."),

    # Toekomst en modals
    keuze(
        "It's cold. I [[*will|am going to]] close the window. Next year we [[*are going to|will]] move to Ghent: we've already bought a house.",
        "Will voor een beslissing op het moment zelf, going to voor een plan dat al vastligt."),
    tabel(
        "Welk modaal werkwoord past?",
        [
            ("Je bent verplicht: You ___ wear a helmet.", "must"),
            ("Het is een goede raad: You ___ see a doctor.", "should"),
            ("Je hebt de toestemming: You ___ leave early today.", "may"),
        ],
        "Must drukt een verplichting uit, should een raad, may een toelating.",
        kolommen=["must", "should", "may"]),

    # Zinsbouw en voorwaarde
    volgorde(
        "Zet de woorden in de juiste volgorde.",
        ["We", "never", "eat", "meat", "at home", "during the week"],
        "Onderwerp, frequentiebijwoord, werkwoord, voorwerp, plaats, tijd."),
    sleep(
        "If you [[heat]] water to 100 degrees, it boils. If it [[snows]] tomorrow, we will build a snowman.",
        ["will heat", "snowed"],
        "In de if-zin van een algemene waarheid of reële voorwaarde staat de present simple."),
    mk("Hoe vraag je beleefd de weg?",
       ["Excuse me, could you tell me the way to the station?", "Hey you, where is the station, tell me right now!", "Station? Where? Quick, quick, I'm in a hurry, mate.", "You must tell me where the train station is located."],
       0,
       "Excuse me en could you ... maken de vraag beleefd. De andere zinnen zijn bot of bevelend."),

    # Extra
    inv("Vul de vraagstaart in: « It's a nice day, ___ ? » Twee woorden.",
        ["isn't it", "is it not"],
        "Na een bevestigende zin met is volgt een ontkennende vraagstaart: isn't it?"),
    keuze(
        "Ik ben goed in tekenen: I'm good [[*at|in|on]] drawing. Ik ben bang voor spinnen: I'm afraid [[*of|for|from]] spiders.",
        "Vaste combinaties: good at, afraid of."),
    tabel(
        "Past deze Engelse zin in een formele of in een informele tekst?",
        [
            ("Dear Mr Smith,", "Formeel"),
            ("Hiya!", "Informeel"),
            ("I look forward to hearing from you.", "Formeel"),
            ("See ya soon!", "Informeel"),
        ],
        "In een formele brief gebruik je een beleefde aanspreking en vaste zinnen. Bij vrienden mag het kort en los.",
        kolommen=["Formeel", "Informeel"]),
    mk("Wat betekent: « I'm looking forward to the holidays »?",
       ["Ik kijk uit naar de vakantie.", "Ik kijk terug op de vakantie.", "Ik zoek een plek voor de vakantie.", "Ik heb geen zin in de vakantie."],
       0,
       "To look forward to something betekent ernaar uitkijken."),

    tabel(
        "Welk woord past bij het reizen?",
        [
            ("De plek waar je je bagage afgeeft op de luchthaven", "check-in desk"),
            ("Een biljet heen en terug", "return ticket"),
            ("De plaats waar je trein vertrekt", "platform"),
        ],
        "Op de luchthaven geef je je bagage af aan de check-in desk. Een return ticket is heen en terug. Een trein vertrekt van een platform (perron).",
        kolommen=["check-in desk", "return ticket", "platform"]),
    keuze(
        "Een tekst die je wil overtuigen om iets te doen, heeft vaak een [[*gebiedende wijs|verleden tijd]], zoals in « [[*Join our club today!|We joined a club last year.]] »",
        "Overtuigende teksten spreken de lezer rechtstreeks aan met een gebiedende wijs."),
    mk("Wat betekent: « The train was delayed because of the snow »?",
       ["De trein had vertraging door de sneeuw.", "De trein werd afgeschaft na de sneeuw.", "De trein reed sneller door de sneeuw.", "De trein vertrok vroeger door de sneeuw."],
       0,
       "To be delayed betekent vertraging hebben. Because of betekent door of wegens."),

    # Schrijfopdracht
    open_("Write a short message (4 to 6 sentences) to a friend. Invite him or her to your birthday party: say when and where it is, what you are going to do and ask for an answer.",
          "Hi Sam! I'm having a birthday party next Saturday at my place. It starts at seven o'clock. We're going to have a barbecue and play some games in the garden. Can you come? Let me know by Thursday! See you, Lies",
          "Een goed antwoord heeft een informele begroeting en afsluiting, vermeldt wanneer en waar het feest is, wat jullie gaan doen (going to), en vraagt om een antwoord."),
]
