"""Online veilig en volgens de regels — pittig
(🌍 Beyond doorstroom, samenleving en economie). Eigen vragen en een eigen nagemaakte
verdachte mail, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Een verdachte mail --------------------------------------------------------------------
ML = Prent("verdachte-mail", "Een mail in je inbox", "een mail met bovenaan de afzender 'Jouw Bank <klantendienst@jouwbank-veilig-login.net>' (A), het onderwerp 'Dringend: je rekening wordt geblokkeerd' (B), de aanhef 'Beste klant' (C), een zin 'Bevestig binnen 24 uur je gegevens of je rekening wordt afgesloten' (D), een groene knop 'Gegevens bevestigen' (E) en onderaan de handtekening 'Je bank' met het logo (F)")
ML.rect(90, 55, 820, 540, "#ffffff", GRIJS, 10, 2)
ML.rect(90, 55, 820, 120, "#f4f4f2", GRIJS, 10, 1)
ML.tekst(120, 95, "Van:", 18, "start", GRIJS)
ML.tekst(175, 95, "Jouw Bank <klantendienst@jouwbank-veilig-login.net>", 20, "start")
ML.letter(860, 90, "A")
ML.tekst(120, 145, "Onderwerp:", 18, "start", GRIJS)
ML.tekst(225, 145, "Dringend: je rekening wordt geblokkeerd", 20, "start", DONKER, True)
ML.letter(860, 140, "B")
ML.tekst(130, 225, "Beste klant,", 21, "start")
ML.letter(330, 218, "C")
ML.tekst(130, 285, "Wij hebben ongewone aktiviteit op je rekening gezien.", 20, "start")
ML.tekst(130, 325, "Bevestig binnen 24 uur je gegevens,", 20, "start")
ML.tekst(130, 355, "anders wordt je rekening afgesloten.", 20, "start")
ML.letter(560, 340, "D")
ML.rect(130, 400, 290, 60, "#3f7a3a", "#3f7a3a", 10, 1)
ML.tekst(275, 438, "Gegevens bevestigen", 21, "middle", "#ffffff", True)
ML.letter(470, 430, "E")
ML.tekst(130, 520, "Met vriendelijke groet,", 19, "start")
ML.tekst(130, 552, "Je bank", 19, "start", DONKER, True)
ML.rect(240, 528, 60, 34, "#d9e4ee", GRIJS, 6, 1)
ML.letter(360, 545, "F")

ZONE = {"A": [Prent.zone(170, 70, 560, 40)], "B": [Prent.zone(220, 120, 430, 40)],
        "C": [Prent.zone(125, 200, 160, 40)], "D": [Prent.zone(125, 300, 430, 70)],
        "E": [Prent.zone(130, 400, 290, 60)], "F": [Prent.zone(125, 500, 200, 70)]}

VRAGEN = [
    klik("Klik op het adres dat verraadt dat deze mail niet van de echte bank komt.", ML.bestand, ZONE["A"],
         "Het adres eindigt niet op de gewone naam van de bank, maar op een verzonnen naam met 'veilig-login' erbij."),
    klik("Klik op het deel dat je onder tijdsdruk wil zetten.", ML.bestand, ZONE["D"],
         "'Binnen 24 uur, anders afgesloten': haast is een klassiek trucje bij phishing."),
    klik("Klik op wat je zeker NIET mag aanklikken.", ML.bestand, ZONE["E"],
         "Die knop leidt naar een nagemaakte site die je gegevens steelt. Ga zelf naar de site of app van je bank."),
    klik("Klik op de aanhef die toont dat de afzender je naam niet kent.", ML.bestand, ZONE["C"],
         "Een echte bank kent je naam; 'Beste klant' is algemeen."),
    met_prent(ML.bestand, tabel("Kijk naar de mail. Klopt dit?", [
        ("Het logo onderaan bewijst dat de mail echt is.", F),
        ("De taalfout 'aktiviteit' is een extra waarschuwing.", J),
        ("Een echte bank vraagt nooit om via een link je gegevens te bevestigen.", J),
        ("Omdat het onderwerp dringend is, klik je best meteen.", F),
    ], "Een logo kan iedereen kopiëren. Haast en taalfouten zijn alarmsignalen.")),
    met_prent(ML.bestand, mk("Wat doe je best met deze mail?",
              ["niet klikken en zelf in de app van je bank kijken",
               "op de knop klikken en enkel je naam invullen, niet je code",
               "antwoorden en vragen of de mail wel echt van de bank komt",
               "de mail doorsturen naar al je vrienden als waarschuwing"], 0,
              "Contact zoek je zelf langs de echte site of app, nooit via de mail.")),
    met_prent(ML.bestand, inv("Hoe heet deze vorm van oplichting? Eén woord.", ["phishing", "phising", "Phishing"],
              "Phishing: 'hengelen' naar je gegevens.")),
    casus(
        "Jana maakt een affiche voor de schoolfuif. Ze gebruikt een foto die ze online vond zonder vermelding, "
        "een tekening onder creative commons met naamsvermelding, en een foto van haar vriend Ruben die "
        "op de vorige fuif danste. Ze wil de affiche ook op de schoolpagina zetten.",
        [
            mk("Wat geldt voor de foto zonder vermelding?",
               ["ze is beschermd, ze vraagt toelating",
                "ze is vrij omdat er geen enkele naam bij staat",
                "ze mag als Jana de foto wat bijknipt",
                "ze is vrij omdat ze voor school is"], 0,
               "Zonder vermelding ga je ervan uit dat het werk beschermd is."),
            keuze("Bij de tekening moet Jana [[*de naam van de maker vermelden|niets doen|de maker betalen]].",
                  "Naamsvermelding is de voorwaarde van die licentie."),
            inv("Welk recht van Ruben speelt mee als ze zijn foto gebruikt?", ["portretrecht", "het portretrecht"],
                "Ruben is herkenbaar, dus beslist hij mee over het gebruik van zijn beeld."),
        ],
    ),
    tabel("Welk recht speelt hier?", [
        ("een fotograaf beslist wie zijn foto mag afdrukken", "auteursrecht"),
        ("je wil niet dat een foto van jou online staat", "portretrecht"),
        ("een winkel vraagt meer gegevens dan nodig", "privacyrecht"),
        ("een schrijver beslist over een vertaling van zijn boek", "auteursrecht"),
    ], "Maker, wie erop staat, of je persoonsgegevens.",
       kolommen=["auteursrecht", "portretrecht", "privacyrecht"]),
    sorteer("Sterk of zwak wachtwoordgedrag?", ["Sterk", "Zwak"], [
        ["een lange zin van vier losse woorden", "Sterk"],
        ["je naam met je geboortejaar", "Zwak"],
        ["overal hetzelfde wachtwoord", "Zwak"],
        ["tweestapsverificatie aanzetten", "Sterk"],
    ], "Lang, niet te raden, uniek en met een tweede slot."),
    volgorde("Een klasgenoot wordt online gepest. Zet de stappen in een goede volgorde.", [
        "schermafbeeldingen van de berichten nemen",
        "niet terugschelden of meedoen",
        "het melden aan een leerkracht of vertrouwenspersoon",
        "het account of bericht melden op het platform",
    ], "Eerst bewijs bewaren, dan niet meedoen en hulp halen."),
    koppel("Koppel elk begrip aan de uitleg.", [
        ["netiquette", "omgangsregels voor hoe je je online gedraagt"],
        ["creative commons", "toelating vooraf, onder voorwaarden"],
        ["tweestapsverificatie", "een tweede slot naast je wachtwoord"],
        ["nepnieuws", "met opzet onjuiste berichten als echt nieuws"],
    ], ["een sterk wachtwoord"], "Elk begrip hoort bij een andere regel online."),
    tabel("Nepnieuws nakijken: helpt dit?", [
        ("nakijken of ernstige media het ook brengen", J),
        ("de foto omgekeerd opzoeken", J),
        ("kijken hoeveel keer het al gedeeld werd", F),
        ("nagaan wie het bericht eerst plaatste", J),
    ], "Veel gedeeld betekent niet dat het klopt."),
    mk("Hoelang na het overlijden van een schrijver mag je zijn roman vrij gebruiken in ons land?",
       ["na zeventig jaar", "na tien jaar", "meteen bij het overlijden", "na honderd jaar"], 0,
       "Het auteursrecht loopt nog zeventig jaar na het overlijden."),
    keuze("Een kort stukje uit een boek in je werkje overnemen mag, als je [[*de bron vermeldt|het in hoofdletters zet|de auteur een mail stuurt]].",
          "Kort citeren met bronvermelding mag."),
    tabel("Welke rechten heb je over gegevens die een bedrijf over jou bijhoudt?", [
        ("ze opvragen en inkijken", J),
        ("fouten laten verbeteren", J),
        ("ze in veel gevallen laten wissen", J),
        ("ze verkopen aan een ander bedrijf", F),
    ], "Het privacyrecht geeft je controle over je eigen gegevens."),
    sleep("Wie een werk maakt, heeft het [[auteursrecht]]. Wie herkenbaar op een foto staat, heeft het [[portretrecht]].",
          ["privacyrecht", "netiquette"], "Bij een foto van een persoon spelen dus twee rechten."),
    mk("Je krijgt een sms: 'Je pakje wacht, betaal 1,99 euro verzendkosten via deze link.' Je verwacht geen pakje. Wat doe je?",
       ["niet klikken en het bericht verwijderen",
        "snel betalen, want het is maar een klein bedrag",
        "op de link klikken om te zien wat het is",
        "terugsms'en met je adres zodat het pakje komt"], 0,
       "Ook een klein bedrag is een lokmiddel om je kaartgegevens te stelen."),
    tabel("Hoort dit bij goede netiquette?", [
        ("een bericht helemaal in hoofdletters tikken", F),
        ("eerst nadenken voor je reageert in een groep", J),
        ("een privébericht doorsturen zonder te vragen", F),
    ], "Netiquette vraagt respect, ook online."),
    inv("Welke afkorting gebruik je voor een licentie waarmee de maker vooraf toelating geeft onder voorwaarden? Twee letters.",
        ["CC", "cc"], "CC staat voor creative commons."),
    tabel("Sterk wachtwoord of niet?", [
        ("Zomer2026", F),
        ("fiets-wolk-tafel-regen", J),
        ("123456", F),
    ], "Lengte en losse woorden helpen meer dan een woord met een jaartal."),
    mk("Iemand belt en zegt dat hij van de helpdesk is. Hij vraagt je wachtwoord om een probleem op te lossen. Wat doe je?",
       ["je geeft het niet en hangt op",
        "je geeft het, want hij kent je naam al",
        "je geeft enkel de eerste helft ervan",
        "je stuurt het liever veilig via mail door"], 0,
       "Een echte helpdesk vraagt nooit je wachtwoord."),
    keuze("Met tweestapsverificatie kan iemand die je wachtwoord kent [[*toch niet zomaar binnen|meteen binnen|enkel 's nachts binnen]].",
          "Hij heeft ook de tweede code of je vinger nodig."),
    tabel("Mag dit zonder toelating?", [
        ("een foto van een herkenbare klasgenoot online zetten", F),
        ("een werk delen waarvan de maker zeventig jaar geleden stierf, in ons land", J),
        ("een liedje van een bekende zanger onder je eigen filmpje zetten", F),
    ], "Portretrecht en auteursrecht, behalve als het werk al vrij is."),
    koppel("Koppel elk alarmsignaal aan een voorbeeld.", [
        ["vreemd afzenderadres", "info@bpost-pakjes.co"],
        ["tijdsdruk", "binnen 2 uur reageren of je verliest alles"],
        ["algemene aanhef", "Beste gebruiker"],
    ], ["een bekende vriend die je bij naam noemt"], "Bij phishing komen zulke signalen vaak samen voor."),
    sorteer("Persoonsgegeven of niet?", ["Persoonsgegeven", "Geen persoonsgegeven"], [
        ["je thuisadres", "Persoonsgegeven"],
        ["een foto van jou", "Persoonsgegeven"],
        ["de openingsuren van een winkel", "Geen persoonsgegeven"],
        ["je rijksregisternummer", "Persoonsgegeven"],
    ], "Alles wat over jou als persoon gaat, valt onder het privacyrecht."),
    inv("Hoe zoek je na waar een verdachte foto eerder online opdook? Vul aan: de foto ... opzoeken.",
        ["omgekeerd", "omgekeerd opzoeken"], "Zo zie je of een oude foto bij een nieuw bericht gezet werd."),
    open_("Een vriend wil een grappige foto van een klasgenoot in de klasgroep zetten. Leg uit welke regels meespelen en wat hij best doet.",
          "Wie herkenbaar op de foto staat heeft portretrecht: hij moet eerst toelating vragen. Doorsturen zonder toelating kan kwetsend zijn en zelfs cyberpesten worden. Zegt de klasgenoot nee, dan zet hij de foto niet online."),
]
