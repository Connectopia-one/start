# -*- coding: utf-8 -*-
"""Uitdaging Frans 🚀 Boost dubbele finaliteit (25 november 2026), in de
vormen van het examen van de Examencommissie: 40 vragen die alle hoofdstukken
door elkaar halen, van tekstbegrip en tekstsoorten tot woordenschat,
grammatica, uitspraak en de Franstalige wereld. Een verzonnen uitnodiging en
zes losse zinnen om op te klikken, tabellen, keuzelijsten, slepen, koppelen,
sorteren, volgorde, een casus en een korte schrijfopdracht. Geen nieuwe
leerstof: alles staat in de hoofdstukken van dit vak.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_frans.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Frans"
BESTAND = "boost-df-frans-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/frans-boost-df-uitdaging"
FETE = "uitnodiging-buurtfeest.svg"
ZINNEN = "zes-zinnen.svg"
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Uitnodiging buurtfeest
    klik("Lees de uitnodiging voor het buurtfeest. Klik op de zin die zegt waar je moet afspreken.",
         FETE, [Z[2]],
         "« Le rendez-vous est à 15 h, devant l'école communale » : je spreekt af voor de gemeentelijke school."),
    klik("Klik op de zin die zegt wat elke familie moet meebrengen.",
         FETE, [Z[3]],
         "« Chaque famille apporte un plat ou un dessert à partager » : een gerecht of een dessert om te delen."),
    klik("Het regent op de dag van het feest. Klik op de zin die zegt wat er dan gebeurt.",
         FETE, [Z[4]],
         "« S'il pleut » betekent 'als het regent'. Dan gaat het feest door in de sportzaal."),
    klik("Klik op de zin die een beperking aankondigt met een woord van tegenstelling.",
         FETE, [Z[5]],
         "« Mais » kondigt een tegenstelling aan: honden mogen niet mee in de zaal."),
    met_prent(FETE, tabel(
        "Klopt dit volgens de uitnodiging?",
        [
            ("Het feest begint om drie uur 's middags.", J),
            ("Je schrijft je in na 10 mei.", F),
            ("Het feest is op een zondag.", F),
        ],
        "15 h is drie uur 's middags. Je schrijft je in vóór (avant) 10 mei. Samedi is zaterdag.")),
    met_prent(FETE, keuze(
        "Deze tekst is vooral een [[*informatieve|narratieve|literaire]] tekst. In zin 6 staat « envoyez » in de [[*impératif|imparfait]].",
        "De uitnodiging geeft praktische informatie. « Envoyez » is een bevel in de vous-vorm.")),

    # Zes zinnen
    klik("Bekijk de zes zinnen. Klik op de zin met een fout na een hoeveelheid.",
         ZINNEN, [Z[3]],
         "Na een hoeveelheid komt « de » : un kilo de pommes."),
    klik("Klik op de zin waarin het bijvoeglijk naamwoord niet overeenkomt.",
         ZINNEN, [Z[5]],
         "« Mes amies » is vrouwelijk meervoud, dus: sportives."),
    klik("Klik op de zin in de passé composé met être.",
         ZINNEN, [Z[2]],
         "« Nous sommes allés » : aller vormt de passé composé met être, en het deelwoord krijgt -s voor het meervoud."),
    klik("Klik op de zin die een hoffelijke vraag stelt met de conditionnel.",
         ZINNEN, [Z[6]],
         "« Je voudrais » is de conditionnel de politesse van vouloir: zo vraag je iets beleefd."),
    met_prent(ZINNEN, keuze(
        "Zin 4 is een [[*ontkennende|vragende]] zin. Na « ne ... pas » wordt « de la viande » [[*de viande|du viande]].",
        "Ne ... pas staat rond het werkwoord. In een ontkenning wordt het delend lidwoord « de »." )),

    # Tekstsoorten en tekstverbanden
    tabel(
        "Welke tekstsoort hoort bij deze vier korte Franse zinnetjes?",
        [
            ("« Coupez les tomates et ajoutez un peu de sel. »", "prescriptief"),
            ("« Venez nombreux, c'est gratuit ! »", "persuasief"),
            ("« Hier, j'ai raté mon bus et je suis arrivé en retard. »", "narratief"),
            ("« La piscine est ouverte du lundi au samedi. »", "informatief"),
        ],
        "Een recept zegt wat je moet doen. Een oproep wil je overtuigen. Een verhaal vertelt wat er gebeurde. Openingsuren geven informatie.",
        kolommen=["informatief", "persuasief", "prescriptief", "narratief"]),
    koppel(
        "Koppel het Franse signaalwoord aan het verband.",
        [
            ["parce que", "oorzaak"],
            ["donc", "gevolg"],
            ["cependant", "tegenstelling"],
            ["d'abord", "volgorde"],
        ],
        ["voorwaarde"],
        "Signaalwoorden tonen hoe zinnen met elkaar samenhangen."),
    volgorde(
        "Zet de stappen van dit recept in de juiste volgorde.",
        ["D'abord, lavez les légumes.",
         "Ensuite, coupez-les en morceaux.",
         "Puis, faites-les cuire dix minutes.",
         "Enfin, servez la soupe bien chaude."],
        "D'abord, ensuite, puis en enfin tonen de volgorde van de stappen."),

    # Woordenschat
    sorteer(
        "Bij welk woordveld hoort dit Franse woord?",
        ["gezondheid", "eten", "kleding"],
        [
            ["l'ordonnance", "gezondheid"],
            ["le fromage", "eten"],
            ["la chemise", "kleding"],
            ["mal à la gorge", "gezondheid"],
            ["les chaussures", "kleding"],
        ],
        "Een ordonnance is een voorschrift van de dokter. Fromage is kaas. Chemise en chaussures zijn kleding."),
    inv("Hoe zeg je in het Frans 'verjaardag'? Schrijf het woord zonder lidwoord.",
        ["anniversaire"],
        "Joyeux anniversaire ! betekent gelukkige verjaardag."),
    mk("Waar koop je in Frankrijk geneesmiddelen met een voorschrift van de dokter?",
       ["À la pharmacie", "À la boulangerie, naast het brood", "Au marché, bij de groenteboer", "À la librairie, bij de boeken"],
       0,
       "Geneesmiddelen koop je bij de apotheker: à la pharmacie."),
    keuze(
        "« Il [[*pleut|fait]] » betekent 'het regent'. « Il [[*fait|est]] beau » betekent 'het is mooi weer'.",
        "Het weer beschrijf je vaak met « il fait ». Voor regen gebruik je « il pleut »."),
    koppel(
        "Koppel het Franse woord aan de Nederlandse betekenis.",
        [
            ["l'épaule", "de schouder"],
            ["l'assiette", "het bord"],
            ["le stage", "de stage"],
            ["le vendeur", "de verkoper"],
        ],
        ["de leraar"],
        "Leer woorden per woordveld: lichaam, tafel, werk."),

    # Grammatica
    inv("Vul in: « Nous ... nos devoirs. » Het werkwoord is faire, in de présent.",
        ["faisons"],
        "Faire in de présent: je fais, tu fais, il fait, nous faisons, vous faites, ils font."),
    tabel(
        "Is deze Franse zin grammaticaal juist?",
        [
            ("Je ne vais jamais au cinéma.", J),
            ("C'est une belle maison.", J),
            ("Elle est plus bon que moi.", F),
            ("Ils ont mangé une pizza.", J),
        ],
        "Ne ... jamais staat rond het werkwoord. Belle is de vrouwelijke vorm van beau. De vergrotende trap van bon is meilleur."),
    keuze(
        "J'habite [[*à|en]] Bruxelles. Le livre est [[*sur|sous]] la table: het ligt erop.",
        "Bij een stad gebruik je « à ». « Sur » betekent op, « sous » betekent onder."),
    sleep(
        "Quand j'[[étais]] petit, j'allais souvent chez ma grand-mère. Un jour, j'y [[ai]] trouvé un vieux chat.",
        ["suis", "avais"],
        "Een gewoonte in het verleden staat in de imparfait (étais). Een eenmalige gebeurtenis staat in de passé composé (ai trouvé)."),
    mk("Welke ontkenning van « elle va sortir ce soir » is juist?",
       ["Elle ne va pas sortir ce soir.", "Elle va ne sortir pas ce soir.", "Elle ne va sortir pas ce soir.", "Elle pas va sortir ne ce soir !"],
       0,
       "Ne ... pas staat rond de vervoegde vorm van aller: elle ne va pas sortir."),
    tabel(
        "Welke Franse tijd herken je in deze zin?",
        [
            ("« Je vais partir demain. »", "futur proche"),
            ("« Je viens de manger. »", "passé récent"),
            ("« Je partirai demain. »", "futur simple"),
        ],
        "Aller + infinitief is de futur proche. Venir de + infinitief is de passé récent. Partirai is de futur simple.",
        kolommen=["futur proche", "passé récent", "futur simple"]),
    keuze(
        "« Je [[*me|se]] lève à sept heures. » Het bevel in de tu-vorm is « [[*Lève-toi|Te lève]] ! »",
        "Bij een wederkerend werkwoord past het voornaamwoord bij het onderwerp. In het bevel komt « toi » achter het werkwoord."),
    inv("Vul één woord in: « ... livre est à toi ? » Je wijst één mannelijk boek aan.",
        ["Ce"],
        "Het aanwijzend woord voor een mannelijk enkelvoud is « ce »."),
    keuze(
        "In « Je les vois » vervangt « les » een [[*lijdend voorwerp|onderwerp]]. In « Je lui parle » betekent « lui » aan hem of aan [[*haar|hen]].",
        "Les is een COD. Lui is een COI en kan zowel aan hem als aan haar betekenen."),

    inv("Wat is het meervoud van « un gâteau » zonder lidwoord? Eén woord.",
        ["gâteaux"],
        "Woorden op -eau krijgen in het meervoud een -x: des gâteaux."),
    keuze(
        "« Mes parents travaillent à Namur. » Het onderwerp is [[*mes parents|Namur]]. Et, mais, donc en car zijn [[*nevenschikkende|onderschikkende]] voegwoorden.",
        "Het onderwerp doet de handeling. Nevenschikkende voegwoorden verbinden twee gelijkwaardige stukken."),
    tabel(
        "Juiste vorm van het bezittelijk woord?",
        [
            ("mon école", J),
            ("ma amie", F),
            ("leurs enfants", J),
        ],
        "Voor een vrouwelijk woord met een klinker vooraan gebruik je mon: mon amie, mon école. Leurs staat bij meer bezitters en meer dingen."),
    sleep(
        "Le français n'est pas parlé qu'en France : on le parle aussi en [[Suisse]] et au Luxembourg. En France, on se dit souvent bonjour en faisant [[la bise]].",
        ["Allemagne", "la main"],
        "Frans spreekt men ook in België, Zwitserland en Luxemburg. La bise is de kus op de wang als begroeting."),

    # Uitspraak en spelling
    tabel(
        "Klopt dit over de Franse uitspraak en spelling?",
        [
            ("De cédille in français zorgt dat je de c als s uitspreekt.", J),
            ("Bij een vraag zonder vraagwoord gaat je stem op het einde omhoog.", J),
            ("De é in été klinkt net als de è in père.", F),
        ],
        "De cédille geeft een s-klank. In een vraag als « Tu viens ? » stijgt je stem. De é is gesloten, de è open."),

    # Franstalige wereld en omgangsvormen
    sorteer(
        "Is dit een officiële taal in België?",
        ["ja", "nee"],
        [
            ["le néerlandais", "ja"],
            ["le français", "ja"],
            ["l'allemand", "ja"],
            ["l'anglais", "nee"],
        ],
        "België heeft drie officiële talen: Nederlands, Frans en Duits."),
    mk("Je schrijft een mail aan een vrouw van een bedrijf, maar je kent haar naam niet. Hoe begin je?",
       ["Madame,", "Salut ma belle,", "Coucou Madame,", "Bonjour mon amie,"],
       0,
       "In een formele mail begin je met « Madame, ». Salut en coucou zijn voor vrienden."),
    koppel(
        "Koppel de situatie aan de gepaste Franse reactie.",
        [
            ["Iemand zegt: « Je suis désolé, je suis en retard. »", "Ce n'est pas grave."],
            ["Je begrijpt je gesprekspartner niet.", "Pouvez-vous répéter, s'il vous plaît ?"],
            ["Je bestelt iets in een café.", "Je voudrais un jus d'orange, s'il vous plaît."],
        ],
        ["Cordialement."],
        "Een gepaste reactie past bij de situatie en bij het register."),
    keuze(
        "Je kent je gesprekspartner niet en hij is ouder: je zegt [[*vous|tu]]. Een formele mail sluit je af met [[*Cordialement|Bisous]].",
        "Vous is beleefd en afstandelijk. Cordialement past in een formele mail."),

    casus(
        "Lees dit bericht: « Salut Léa ! Ce week-end, je vais à Liège chez mon oncle. On va visiter le musée samedi matin, et l'après-midi on fera du vélo le long de la Meuse. Tu veux venir avec nous ? Réponds-moi avant jeudi ! Bises, Tom »",
        [
            tabel(
                "Klopt dit volgens het bericht van Tom?",
                [
                    ("Tom gaat naar zijn oom in Luik.", J),
                    ("Ze gaan zaterdagnamiddag naar het museum.", F),
                    ("Léa moet antwoorden voor donderdag.", J),
                ],
                "Chez mon oncle is bij mijn oom. Het museum is zaterdagvoormiddag (samedi matin). Avant jeudi is voor donderdag."),
            mk("Welk register gebruikt Tom?",
               ["Informeel: hij schrijft naar een vriendin", "Formeel: hij schrijft naar een groot bedrijf", "Formeel: hij schrijft naar zijn eigen leraar", "Zakelijk: hij solliciteert voor een job"],
               0,
               "Salut, tu en Bises tonen een informeel register tussen vrienden."),
        ]),

    open_("Schrijf een kort antwoord van Léa aan Tom (drie à vier zinnen in het Frans). Zeg of je meegaat, stel één vraag en sluit gepast af.",
          "Salut Tom ! Merci pour ton invitation. Je viens avec plaisir ! À quelle heure est-ce qu'on part samedi ? Bises, Léa",
          "Een goed antwoord zegt of Léa meegaat, stelt een vraag, gebruikt een informeel register en sluit gepast af."),
]
