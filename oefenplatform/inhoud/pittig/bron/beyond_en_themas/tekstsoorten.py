"""Tekstsoorten en de bedoeling van een tekst — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the text.\n\n"
    "SAVE OUR LIBRARY!\n"
    "The council wants to close Westbridge Library next spring to save £80,000 a year. "
    "But the library is far more than a room full of books. Every week, more than 900 people use it: "
    "pensioners read the papers, job seekers use the free computers and toddlers come to story time. "
    "Where else can they go? Surely a town that spends £2 million on a new car park can find the money. "
    "Come to the protest meeting on Friday at 7 p.m. and sign our petition online."
)

TEKST2 = (
    "Read the text.\n\n"
    "Minutes of the student council meeting – 12 October\n"
    "Present: 9 members. Apologies: Leah, Sam.\n"
    "1. The chair opened the meeting at 12.30.\n"
    "2. The canteen survey: 64% of pupils want more vegetarian options. Agreed: Noah will send the results to the head teacher.\n"
    "3. Charity day: the date was moved to 20 November.\n"
    "Next meeting: 26 October."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Welk doel heeft deze tekst vooral?",
                ["Overtuigen en aanzetten tot actie", "Informeren over openingsuren", "Een verhaal vertellen", "Uitleggen hoe je een petitie maakt"],
                0,
                "Save our library!, Surely … en Come to the protest meeting.",
            ),
            mk(
                "Welke functie heeft de vraag « Where else can they go? »?",
                ["Ze is retorisch", "Ze vraagt de lezer om een adres", "Ze is een enquêtevraag", "Ze vraagt om uitleg bij de cijfers"],
                0,
                "De schrijver verwacht geen antwoord: het moet de lezer overtuigen dat er geen andere plek is.",
            ),
            tabel(
                "Feit of mening?",
                [
                    ("Every week, more than 900 people use the library.", "Feit"),
                    ("The library is far more than a room full of books.", "Mening"),
                    ("The council wants to save £80,000 a year.", "Feit"),
                ],
                "Een feit kan je nagaan; een mening is een oordeel.",
                kolommen=["Feit", "Mening"],
            ),
            keuze(
                "Het woord surely maakt de bewering [[*sterker|voorzichtiger]].",
                "Surely duwt de lezer naar akkoord gaan.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Welk soort tekst is dit verslag van de leerlingenraad?",
                ["Notulen", "Een uitnodiging voor een schoolfeest", "Een kort krantenbericht", "Een handleiding voor leden"],
                0,
                "Minutes, present en apologies zijn typisch voor een verslag.",
            ),
            inv(
                "Hoeveel leden waren afwezig met verwittiging? Schrijf het getal.",
                ["2", "twee"],
                "Apologies: Leah, Sam.",
            ),
            mk(
                "Wat moet Noah doen?",
                ["De resultaten doorsturen", "De volgende vergadering leiden", "De liefdadigheidsdag verplaatsen", "Een nieuwe enquête maken"],
                0,
                "Agreed: Noah will send the results to the head teacher.",
            ),
            keuze(
                "De toon van dit verslag is [[*zakelijk|emotioneel]].",
                "Korte zinnen, cijfers en geen meningen.",
            ),
        ],
    ),
    tabel(
        "Welk soort tekst is deze zin?",
        [
            ("« Press the green button and wait for the beep. »", "Prescriptief"),
            ("« The Thames is 346 kilometres long. »", "Informatief"),
            ("« We must stop selling plastic bottles. »", "Argumentatief"),
            ("« The old man opened the door and froze. »", "Narratief"),
        ],
        "Kijk wat de tekst met de lezer wil doen.",
        kolommen=["Informatief", "Prescriptief", "Argumentatief", "Narratief"],
    ),
    sorteer(
        "Formeel of informeel?",
        ["Formeel", "Informeel"],
        [
            ("I look forward to hearing from you.", "Formeel"),
            ("Cheers, see you!", "Informeel"),
            ("With regard to your letter of 5 May…", "Formeel"),
            ("Guess what happened today!", "Informeel"),
            ("Yours faithfully", "Formeel"),
        ],
        "Vaste formules zijn formeel; uitroepen en spreektaal informeel.",
    ),
    koppel(
        "Koppel het Engelse woord aan zijn betekenis.",
        [
            ("audience", "publiek"),
            ("purpose", "doel"),
            ("tone", "toon"),
            ("headline", "kop van een krantenbericht"),
        ],
        ["schrijver"],
        "Met die vier woorden beschrijf je wat een tekst doet.",
    ),
    mk(
        "Lees: « Studies suggest that green spaces may reduce stress. » Hoe zeker is de schrijver?",
        ["Voorzichtig", "Helemaal zeker", "Het is een grap", "Hij is boos"],
        0,
        "Suggest en may zwakken de bewering af.",
    ),
    mk(
        "Lees: « Dear Sir or Madam » Hoe sluit je zo'n brief af?",
        ["Yours faithfully", "Love, Tom", "See you soon", "Yours sincerely, mate"],
        0,
        "Als je de naam niet kent: Yours faithfully. Ken je de naam: Yours sincerely.",
    ),
    mk(
        "Lees: « Hurry! Only 3 days left to get 50% off all jackets! » Welke middelen gebruikt deze tekst?",
        ["Tijdsdruk en een uitroep", "Een wetenschappelijk onderzoek", "Een vertelde gebeurtenis", "Een stappenplan"],
        0,
        "Hurry en only 3 days left jagen je op.",
    ),
    mk(
        "Lees: « Bus 41 will not run on Sunday due to roadworks. » Wat is het doel van deze tekst?",
        ["Informeren", "Overtuigen", "Ontroeren", "De lezer amuseren"],
        0,
        "Het is een zakelijke mededeling.",
    ),
    mk(
        "Welke openingszin past bij een narratieve tekst?",
        ["« It was a cold night when the phone rang. »", "« Take two tablets a day after a meal. »", "« Smoking should be banned in all our parks. »", "« Paris has been the capital of France for ages. »"],
        0,
        "Een verhaal zet een tijd, een plaats en een gebeurtenis neer.",
    ),
    mk(
        "Lees: « Experts agree: this is the only diet that works. » Wat doe je als kritische lezer?",
        ["Nagaan welke experts het zijn", "Het meteen geloven, het zijn experts", "Het dieet direct proberen", "De tekst onmiddellijk delen"],
        0,
        "Experts agree zonder namen of bron is een vage autoriteit.",
    ),
    mk(
        "Lees: « It has been claimed that the bridge is unsafe. » Wat weet je niet?",
        ["Wie dat beweert", "Over welke brug het gaat", "Wat er beweerd wordt", "Of het over veiligheid gaat"],
        0,
        "De passieve vorm verbergt wie het zegt.",
    ),
    tabel(
        "Maakt dit woord een bewering voorzichtiger?",
        [
            ("perhaps", J),
            ("definitely", F),
            ("it seems that", J),
            ("without a doubt", F),
        ],
        "Perhaps en it seems zwakken af; definitely en without a doubt versterken.",
    ),
    keuze(
        "Een tekst voor jonge kinderen gebruikt [[*kortere|langere]] zinnen dan een vakartikel.",
        "Het publiek bepaalt de stijl.",
    ),
    keuze(
        "Een reclametekst geeft feiten, maar zijn hoofddoel is [[*overtuigen|informeren]].",
        "De feiten zijn gekozen om je te doen kopen.",
    ),
    inv(
        "Welke afkorting van vier letters zet je op een Engelse uitnodiging voor « gelieve te antwoorden »?",
        ["RSVP", "rsvp", "R.S.V.P."],
        "RSVP komt van répondez s'il vous plaît.",
    ),
    mk(
        "Lees: « Caution: wet floor. » Wat voor tekst is dit?",
        ["Een waarschuwing", "Een advertentie voor een poetsmiddel", "Een uitnodiging om te dweilen", "Een stuk uit een verhaal"],
        0,
        "Caution kondigt een gevaar aan.",
    ),
    mk(
        "Lees: « Fewer young people are buying cars. This is partly because public transport has improved. » Wat doet de tweede zin?",
        ["Ze geeft een oorzaak", "Ze geeft een tegenvoorbeeld", "Ze herhaalt de eerste zin", "Ze geeft een persoonlijke mening"],
        0,
        "Because kondigt een oorzaak aan; partly maakt ze voorzichtig.",
    ),
    tabel(
        "Past deze zin in een formele sollicitatiebrief?",
        [
            ("« I am writing to apply for the position of shop assistant. »", J),
            ("« Wanna give me the job? »", F),
            ("« Please find my CV attached. »", J),
            ("« Lots of love, Mia xx »", F),
        ],
        "Een sollicitatiebrief is formeel: geen spreektaal of kusjes.",
    ),
    keuze(
        "Lees: « Some say the film is too long. I could not disagree more. » De schrijver vindt de film [[*niet te lang|ook te lang]].",
        "I could not disagree more betekent: ik ben het helemaal oneens.",
    ),
    mk(
        "Lees: « Click here to claim your free prize now!!! » Wat is de beste reactie?",
        ["Wantrouwig zijn", "Meteen klikken voor de prijs", "De link aan vrienden sturen", "Je gegevens invullen"],
        0,
        "Druk, uitroeptekens en gratis prijzen zijn kenmerken van oplichting.",
    ),
    inv(
        "Lees: « Dear Ms Brown » Welk Engels woord vul je in bij de slotformule « Yours … »? ",
        ["sincerely", "Sincerely"],
        "Als je de naam kent: Yours sincerely.",
    ),
    sleep(
        "Een tekst die zegt wat je moet doen, is [[prescriptief]]. Een tekst die je wil overtuigen, is [[argumentatief]]. Een verhaal is [[narratief]].",
        ["informatief", "literair"],
        "De soort volgt uit het doel.",
    ),
    open_(
        "Lees: « Hey guys! You won't believe how cool our new app is. Download it now! » Leg uit voor welk publiek deze tekst bedoeld is en hoe je dat merkt.",
        "De tekst is bedoeld voor jongeren. Je merkt het aan de informele toon: Hey guys, spreektaal als cool, een uitroep en een rechtstreekse oproep om de app te downloaden.",
    ),
]
