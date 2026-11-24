"""Tekstsoorten en de bedoeling van een tekst — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le texte.\n\n"
    "SAUVONS NOTRE PISCINE !\n"
    "La commune veut fermer la piscine de Saint-Gilles l'année prochaine pour économiser 90 000 euros par an. "
    "Pourtant, chaque semaine, plus de 1 000 personnes y nagent : des écoles, des clubs, des personnes âgées. "
    "Où iront nos enfants pour apprendre à nager ? À notre avis, une commune qui dépense deux millions pour un nouveau parking "
    "peut bien trouver cet argent. Venez à la réunion de vendredi à 19 h et signez notre pétition en ligne !"
)

TEKST2 = (
    "Lisez le texte.\n\n"
    "Le gouvernement aurait décidé de reporter la réforme des pensions. Selon plusieurs sources, la décision serait annoncée lundi. "
    "Le ministre n'a pas encore réagi."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            mk(
                "Welke bedoeling heeft deze tekst vooral?",
                ["Overtuigen en oproepen", "Informeren over de openingsuren", "Een spannend verhaal vertellen", "Uitleggen hoe je leert zwemmen"],
                0,
                "Sauvons …!, à notre avis, venez, signez.",
            ),
            mk(
                "Welke functie heeft de vraag « Où iront nos enfants pour apprendre à nager ? »?",
                ["Ze is retorisch", "Ze vraagt de lezer om een adres", "Het is een vraag uit een enquête", "Ze vraagt uitleg bij de cijfers"],
                0,
                "De schrijver verwacht geen antwoord: de vraag moet overtuigen.",
            ),
            tabel(
                "Feit of mening in de tekst over het zwembad?",
                [
                    ("Plus de 1 000 personnes y nagent chaque semaine.", "Feit"),
                    ("Une commune … peut bien trouver cet argent.", "Mening"),
                    ("La commune veut économiser 90 000 euros par an.", "Feit"),
                ],
                "Een feit kan je nagaan; à notre avis kondigt een mening aan.",
                kolommen=["Feit", "Mening"],
            ),
            keuze(
                "De imperatieven « venez » en « signez » maken van de tekst [[*een oproep|een verslag]].",
                "De imperatief zet aan tot handelen.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            mk(
                "Wat zegt de conditionnel « aurait décidé »?",
                ["Het is onbevestigd", "Het is zeker al beslist", "Het zal zeker nooit gebeuren", "Het is een bevel aan de minister"],
                0,
                "De conditionnel in het nieuws geeft een onbevestigd bericht.",
            ),
            keuze(
                "Dit bericht is [[*informatief|literair]].",
                "Het brengt nieuws, zonder mening.",
            ),
        ],
    ),
    tabel(
        "Welke soort tekst is deze Franse zin?",
        [
            ("« Appuyez sur le bouton vert et attendez le signal. »", "Prescriptief"),
            ("« La Seine mesure 777 kilomètres. »", "Informatief"),
            ("« Il faut interdire les sacs en plastique. »", "Argumentatief"),
            ("« Le vieil homme ouvrit la porte et s'arrêta net. »", "Narratief"),
        ],
        "Kijk wat de tekst met de lezer wil doen.",
        kolommen=["Informatief", "Prescriptief", "Argumentatief", "Narratief"],
    ),
    sorteer(
        "Formeel of informeel Frans?",
        ["Formeel", "Informeel"],
        [
            ("Veuillez agréer mes salutations distinguées.", "Formeel"),
            ("Salut, ça va ?", "Informeel"),
            ("Je me permets de vous écrire…", "Formeel"),
            ("C'était trop cool !", "Informeel"),
            ("Bisous, à plus !", "Informeel"),
        ],
        "Vaste formules en vous zijn formeel; spreektaal en tu informeel.",
    ),
    koppel(
        "Koppel het Franse woord aan zijn betekenis.",
        [
            ("le destinataire", "de ontvanger van de tekst"),
            ("un avis", "een mededeling"),
            ("le registre", "het taalgebruik"),
            ("le but", "het doel"),
        ],
        ["de schrijver"],
        "De schrijver is l'auteur.",
    ),
    mk(
        "Lees: « Des études suggèrent que les espaces verts pourraient réduire le stress. » Hoe zeker is de schrijver?",
        ["Voorzichtig", "Helemaal zeker", "Hij maakt een grap", "Hij is boos"],
        0,
        "Suggèrent en pourraient zwakken af.",
    ),
    mk(
        "Lees: « Madame, Monsieur, » Hoe sluit je zo'n brief af?",
        ["Salutations distinguées.", "Bisous et à très bientôt !", "Salut, à plus tard les amis !", "Je t'embrasse très fort."],
        0,
        "Bij een formele brief hoort een formele slotformule.",
    ),
    mk(
        "Lees: « Vite ! Plus que 3 jours pour profiter de -50 % sur tous les manteaux ! » Welke middelen gebruikt deze tekst?",
        ["Tijdsdruk en een uitroep", "Een wetenschappelijk onderzoek", "Een verhaal over een klant", "Een stappenplan om te kopen"],
        0,
        "Vite en plus que 3 jours jagen je op.",
    ),
    mk(
        "Lees: « Le bus 41 ne circulera pas dimanche en raison de travaux. » Wat is het doel?",
        ["Informeren", "Overtuigen", "Ontroeren", "De lezer amuseren"],
        0,
        "Een zakelijke mededeling.",
    ),
    mk(
        "Welke openingszin past bij een narratieve tekst?",
        ["« Il faisait nuit quand le téléphone sonna. »", "« Prenez deux comprimés par jour. »", "« Il faut interdire le tabac dans les parcs. »", "« Paris est la capitale de la France depuis longtemps. »"],
        0,
        "Een verhaal zet een tijd, plaats en gebeurtenis neer; sonna is passé simple.",
    ),
    mk(
        "Lees: « Les experts sont unanimes : c'est le seul régime qui marche. » Wat doe je als kritische lezer?",
        ["Nagaan welke experts", "Het meteen geloven", "Het dieet direct proberen", "De tekst onmiddellijk delen"],
        0,
        "Les experts zonder namen of bron is een vage autoriteit.",
    ),
    tabel(
        "Maakt dit een bewering voorzichtiger?",
        [
            ("peut-être", J),
            ("sans aucun doute", F),
            ("il semble que", J),
            ("certainement", F),
        ],
        "Peut-être en il semble que zwakken af.",
    ),
    keuze(
        "Tegen een onbekende volwassene zeg je in een brief [[*vous|tu]].",
        "Vouvoyer is beleefd.",
    ),
    keuze(
        "Een reclametekst bevat feiten, maar zijn hoofddoel is [[*overtuigen|informeren]].",
        "De feiten zijn gekozen om je te doen kopen.",
    ),
    keuze(
        "« Il arriva, elle partit » staat in de passé simple en wijst op een [[*literaire of verhalende|zakelijke]] tekst.",
        "De passé simple komt vooral in verhalen voor.",
    ),
    inv(
        "Welke afkorting van vier letters staat onderaan een Franse uitnodiging om te vragen dat je antwoordt?",
        ["RSVP", "rsvp", "R.S.V.P."],
        "Répondez s'il vous plaît.",
    ),
    tabel(
        "Past deze zin in een formele sollicitatiebrief in het Frans?",
        [
            ("« Je me permets de poser ma candidature au poste de vendeur. »", J),
            ("« Salut, tu me files le job ? »", F),
            ("« Vous trouverez ci-joint mon CV. »", J),
            ("« Gros bisous, Léa »", F),
        ],
        "Een sollicitatiebrief is formeel.",
    ),
    mk(
        "Lees: « Certains disent que le film est trop long. Je ne suis pas du tout d'accord. » Wat vindt de schrijver?",
        ["Niet te lang", "Ook te lang", "Te kort", "Hij heeft hem niet gezien"],
        0,
        "Pas du tout d'accord: helemaal niet akkoord.",
    ),
    mk(
        "Lees: « Cliquez ici pour réclamer votre cadeau gratuit !!! » Wat is de beste reactie?",
        ["Wantrouwig zijn", "Meteen klikken voor het cadeau", "De link naar vrienden sturen", "Je gegevens invullen"],
        0,
        "Druk, uitroeptekens en gratis cadeaus wijzen op oplichting.",
    ),
    mk(
        "Lees: « Attention : sol glissant. » Wat voor tekst is dit?",
        ["Een waarschuwing", "Een advertentie voor een poetsmiddel", "Een uitnodiging om te dweilen", "Een stuk uit een verhaal"],
        0,
        "Attention kondigt een gevaar aan.",
    ),
    inv(
        "Welke Franse uitdrukking van drie woorden kondigt een mening aan, in de wij-vorm? (« naar onze mening »)",
        ["à notre avis", "A notre avis", "À notre avis"],
        "À mon avis, à notre avis.",
    ),
    mk(
        "Lees: « Comment réussir son examen en cinq étapes » Wat belooft deze titel?",
        ["Concrete stappen", "Een verhaal over een examen", "Een mening over examens", "De uitslag van een examen"],
        0,
        "Comment … en cinq étapes: een prescriptieve tekst.",
    ),
    keuze(
        "« C'était dingue ! » hoort in [[*een sms aan een vriend|een brief aan de directeur]].",
        "Dingue is spreektaal.",
    ),
    tabel(
        "Feit of mening?",
        [
            ("« L'eau bout à 100 degrés. »", "Feit"),
            ("« Le thé est meilleur que le café. »", "Mening"),
            ("« Il est prouvé que le tabac nuit à la santé. »", "Feit"),
        ],
        "Il est prouvé que kondigt een feit aan.",
        kolommen=["Feit", "Mening"],
    ),
    sleep(
        "Een tekst die zegt wat je moet doen, is [[prescriptief]]. Een tekst die je wil overtuigen, is [[argumentatief]]. Een verhaal is [[narratief]].",
        ["informatief", "literair"],
        "De soort volgt uit het doel.",
    ),
    open_(
        "Lees: « Coucou les amis ! Notre nouvelle appli est trop géniale. Téléchargez-la vite ! » Leg uit voor welk publiek deze tekst bedoeld is en hoe je dat merkt.",
        "De tekst is bedoeld voor jongeren. Je merkt het aan de informele toon: coucou, spreektaal als trop géniale, uitroeptekens en een rechtstreekse oproep om de app te downloaden.",
    ),
]
