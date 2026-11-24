"""Woordvelden: wetenschap, techniek en taal — pittig (🌍 Beyond doorstroom, Engels)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Read the text.\n\n"
    "A team of researchers at the University of Bristol ran a survey among 2,000 teenagers about their use of AI chatbots for homework. "
    "The findings were surprising: 70% said they used a chatbot at least once a week, but only a third checked the answers. "
    "The researchers warn that the data show a risk: pupils may hand in work that contains mistakes they do not notice. "
    "However, they stress that the sample was small and that more research is needed before any conclusions can be drawn."
)

TEKST2 = (
    "Read the e-mail.\n\n"
    "Dear customer,\n"
    "We have detected unusual activity on your account. To avoid suspension, click the link below within 24 hours "
    "and enter your password and bank details.\n"
    "Regards, The Security Team"
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Hoeveel van de jongeren keek de antwoorden van de chatbot na?",
                ["Een derde", "Zeventig procent", "Bijna iedereen", "Niemand"],
                0,
                "Only a third checked the answers.",
            ),
            mk(
                "Waarom zijn de onderzoekers voorzichtig met hun besluit?",
                ["De steekproef was klein", "De chatbots werkten niet goed", "De leerlingen logen allemaal", "Het onderzoek was te duur"],
                0,
                "The sample was small and more research is needed.",
            ),
            keuze(
                "In « the data show a risk » staat het werkwoord in het meervoud omdat data [[*een meervoud is|altijd fout is]].",
                "Data is het meervoud van datum.",
            ),
            tabel(
                "Staat dit in de tekst (over wetenschap en taal)?",
                [
                    ("Het onderzoek gebeurde met een enquête.", J),
                    ("Er deden 2000 jongeren mee.", J),
                    ("De onderzoekers verbieden chatbots.", F),
                ],
                "Ze waarschuwen, maar verbieden niets.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Wat voor bericht is dit waarschijnlijk?",
                ["Phishing", "Een echte melding van je bank", "Een reclame voor een nieuwe app", "Een bevestiging van een aankoop"],
                0,
                "Tijdsdruk en een vraag naar je wachtwoord: een valse mail die je gegevens vist.",
            ),
            keuze(
                "Een echte bank vraagt nooit om je [[*wachtwoord|naam]] via een link in een mail.",
                "Geef je password nooit door.",
            ),
        ],
    ),
    koppel(
        "Koppel elk Engels woord aan zijn betekenis (over wetenschap en taal).",
        [
            ("a device", "een toestel"),
            ("a breakthrough", "een doorbraak"),
            ("a backup", "een reservekopie"),
            ("evidence", "bewijsmateriaal"),
        ],
        ["een uitvinder"],
        "Een uitvinder is an inventor.",
    ),
    tabel(
        "Is dit een valse vriend? (het Engelse woord betekent iets anders dan het lijkt)",
        [
            ("eventually", J),
            ("actually", J),
            ("computer", F),
            ("library", J),
        ],
        "Eventually is uiteindelijk, actually eigenlijk, library bibliotheek.",
    ),
    sorteer(
        "Voorvoegsel of achtervoegsel?",
        ["Voorvoegsel (prefix)", "Achtervoegsel (suffix)"],
        [
            ("un- in unhappy", "Voorvoegsel (prefix)"),
            ("-ness in kindness", "Achtervoegsel (suffix)"),
            ("re- in rewrite", "Voorvoegsel (prefix)"),
            ("-less in hopeless", "Achtervoegsel (suffix)"),
            ("dis- in dislike", "Voorvoegsel (prefix)"),
        ],
        "Een prefix staat vooraan, een suffix achteraan.",
    ),
    mk(
        "Wat betekent « careless » als je het in delen leest?",
        ["Onzorgvuldig", "Zonder auto", "Heel voorzichtig", "Zorgzaam"],
        0,
        "Care plus -less: zonder zorg.",
    ),
    mk(
        "Wat betekent « unbreakable »?",
        ["Onbreekbaar", "Gebroken", "Snel stuk", "Breekbaar maar duur"],
        0,
        "Un- + break + -able.",
    ),
    mk(
        "« Eventually, the scientists found a cure. » Wat betekent eventually hier?",
        ["Uiteindelijk", "Eventueel", "Gelukkig", "Bij toeval"],
        0,
        "Een valse vriend: eventually is uiteindelijk.",
    ),
    mk(
        "Welke zin is correct?",
        ["The dog wagged its tail.", "The dog wagged it's tail.", "The dog wagged its' tail.", "The dog wagged it is tail."],
        0,
        "Its is bezittelijk; it's is it is.",
    ),
    mk(
        "« Their laptop crashed and they hadn't made a backup. » Wat gebeurde er?",
        ["De laptop viel uit", "De laptop viel op de grond", "De laptop werd gestolen", "De laptop botste met een auto"],
        0,
        "To crash: vastlopen, uitvallen.",
    ),
    mk(
        "« It's raining cats and dogs. » Wat is dit?",
        ["Een idioom", "Een weerbericht over dieren", "Een fout in het Engels", "Een synoniem van regen"],
        0,
        "Een vaste uitdrukking die je niet letterlijk vertaalt: het giet.",
    ),
    tabel(
        "Brits of Amerikaans gespeld?",
        [
            ("colour", "Brits"),
            ("center", "Amerikaans"),
            ("programme", "Brits"),
            ("organize", "Amerikaans"),
        ],
        "Brits -our, -re, -mme; Amerikaans -or, -er, -m. Brits Engels gebruikt ook -ise.",
        kolommen=["Brits", "Amerikaans"],
    ),
    keuze(
        "In « knife » is de k een [[*stille letter|harde klank]].",
        "Silent letters: de k van knife, de w van write.",
    ),
    keuze(
        "« We need more research » is correct, want research is [[*ontelbaar|altijd meervoud]].",
        "Niet researches.",
    ),
    keuze(
        "Een « synonym » van big is [[*large|small]].",
        "Small is een antonym.",
    ),
    inv(
        "Vul aan met het achtervoegsel: « A person who paints is a paint___. »",
        ["er", "-er"],
        "-er maakt de persoon die het doet.",
    ),
    inv(
        "Vul aan met één Engels woord: « Never share your ___ with anyone; it protects your account. »",
        ["password"],
        "A password is een wachtwoord.",
    ),
    inv(
        "Welk Engels woord vormt het tegengestelde van « possible » met een voorvoegsel?",
        ["impossible"],
        "Im- voor een p: impossible.",
    ),
    mk(
        "Wat is « croissant » in het Engels?",
        ["Een leenwoord", "Een valse vriend", "Een idioom", "Een synoniem"],
        0,
        "Het Engels leende het woord uit het Frans.",
    ),
    mk(
        "« The new drug is still on trial. » Wat betekent dat?",
        ["Het wordt nog getest", "Het staat voor de rechter", "Het is al te koop", "Het werd verboden"],
        0,
        "A trial is bij geneesmiddelen een proef.",
    ),
    mk(
        "« Click here to download the app. » Wat doe je dan?",
        ["De app binnenhalen", "Een bestand naar de server sturen", "De app van je toestel verwijderen", "De app beoordelen in de winkel"],
        0,
        "To download: binnenhalen; to upload: doorsturen.",
    ),
    mk(
        "« Scientists made a breakthrough in cancer research. » Wat deden ze?",
        ["Een doorbraak", "Ze braken een toestel", "Ze stopten het onderzoek", "Ze vroegen meer geld"],
        0,
        "A breakthrough is een grote vooruitgang.",
    ),
    volgorde(
        "Zet de stappen van een wetenschappelijk onderzoek in de juiste volgorde.",
        ["a research question", "an experiment", "the findings", "a conclusion"],
        "Vraag, proef, resultaten, besluit.",
    ),
    tabel(
        "Klopt deze betekenis (over wetenschap en taal)?",
        [
            ("a sample – een steekproef", J),
            ("a scam – oplichterij", J),
            ("a chemist (Brits) – ook een apotheker", J),
            ("a keyboard – een sleutelbord aan de muur", F),
        ],
        "A keyboard is een toetsenbord.",
    ),
    sleep(
        "Een woord dat je niet woord voor woord kan vertalen, is an [[idiom]]. Een woord met dezelfde betekenis is a [[synonym]]. Het stukje un- in unhappy is a [[prefix]].",
        ["suffix", "loanword"],
        "Prefix vooraan, suffix achteraan.",
    ),
    open_(
        "Leg in het Nederlands uit waarom « sympathetic » een valse vriend is en wat het echt betekent.",
        "Sympathetic lijkt op sympathiek, maar het betekent meelevend of begripvol. Sympathiek is in het Engels nice of likeable.",
    ),
]
