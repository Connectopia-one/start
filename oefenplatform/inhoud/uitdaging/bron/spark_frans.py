# -*- coding: utf-8 -*-
"""Uitdaging Frans ✨ Spark: lezen, schrijven, woordenschat en grammatica door
elkaar. Net als de gewone hoofdstukken gaat dit enkel over de schriftelijke
onderdelen van het examen.
"""
NIVEAU = "spark"
VAK = "Frans"
BESTAND = "spark-frans-uitdaging.json"

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Lees: « Chère Lucie, je ne peux pas venir samedi. J'ai un match de foot à Namur. On se voit dimanche ? Bises, Théo. » Wat schrijft Théo?",
        "opties": [
            "Hij kan zaterdag niet en stelt zondag voor",
            "Hij komt zaterdag en blijft tot zondag logeren",
            "Hij vraagt of Lucie meegaat naar de match in Namen",
            "Hij zegt af omdat hij zich niet lekker voelt",
        ],
        "antwoord": 0,
        "uitleg": "« Je ne peux pas venir » is: ik kan niet komen. « On se voit dimanche ? » is: zien we elkaar zondag? Hij zegt dus af én stelt iets anders voor.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Lees: « Attention ! Le magasin sera fermé le lundi 3 novembre. Merci de votre compréhension. » Wat staat er?",
        "opties": [
            "De winkel is die maandag gesloten",
            "De winkel opent die maandag vroeger",
            "De winkel verhuist op 3 november",
            "De winkel houdt die maandag solden",
        ],
        "antwoord": 0,
        "uitleg": "« Fermé » betekent gesloten en « sera » is de toekomende tijd van être. « Merci de votre compréhension » is een beleefde slotzin: dank voor uw begrip.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul aan: « J'... à Hasselt. » (habiter, tegenwoordige tijd) Schrijf enkel de werkwoordsvorm.",
        "antwoord": "habite",
        "uitleg": "Habiter is een gewoon werkwoord op -er: j'habite. De je wordt j' omdat habite met een klinkerklank begint; de h telt in het Frans niet mee.",
    },
    {
        "type": "waarofniet",
        "vraag": "« Il fait beau » zegt iets over het weer, niet over hoe iemand eruitziet.",
        "antwoord": True,
        "uitleg": "Waar. Over het weer gebruik je in het Frans faire: il fait beau, il fait froid, il fait chaud. Letterlijk vertalen levert onzin op.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe zeg je « ik eet geen vlees » in het Frans?",
        "opties": [
            "Je ne mange pas de viande.",
            "Je ne mange pas la viande.",
            "Je mange pas viande.",
            "Je non mange de viande.",
        ],
        "antwoord": 0,
        "uitleg": "Een ontkenning zet je met twee woordjes rond het werkwoord: ne … pas. En na een ontkenning wordt du, de la of des gewoon de.",
    },
    {
        "type": "invultekst",
        "vraag": "Welke dag komt na « mardi »? Antwoord met één Frans woord.",
        "antwoord": "mercredi",
        "uitleg": "De week loopt: lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche. In het Frans schrijf je die dagen met een kleine letter.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe zeg je « we gaan morgen naar Parijs »?",
        "opties": [
            "Nous allons à Paris demain.",
            "Nous allez à Paris demain.",
            "Nous allons à Paris hier.",
            "Nous avons à Paris demain.",
        ],
        "antwoord": 0,
        "uitleg": "Bij nous hoort allons. Demain is morgen, hier is gisteren, en avons komt van avoir (hebben) in plaats van aller (gaan).",
    },
    {
        "type": "waarofniet",
        "vraag": "Voor een woord dat met een klinker begint, schrijf je in het Frans toch le of la voluit, zoals « le eau ».",
        "antwoord": False,
        "uitleg": "Niet waar. Voor een klinkerklank wordt le en la allebei l' : l'eau, l'école, l'ami. Dat leest en spreekt vlotter.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welk woordje past: « Je voudrais ... pain, s'il vous plaît. »",
        "opties": ["du", "de la", "des", "le"],
        "antwoord": 0,
        "uitleg": "Pain is mannelijk, en je vraagt een onbepaalde hoeveelheid: du pain. Bij een vrouwelijk woord zou het de la zijn, bij een meervoud des.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul aan: « Elle ... française. » (être) Schrijf enkel de werkwoordsvorm.",
        "antwoord": "est",
        "uitleg": "Être gaat: je suis, tu es, il/elle est. Het is een onregelmatig werkwoord, dus die vormen moet je uit het hoofd kennen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Lees: « D'abord, coupez les pommes. Ensuite, ajoutez le sucre. Enfin, mettez au four. » Welke drie woorden geven de volgorde aan?",
        "opties": [
            "D'abord, ensuite, enfin",
            "Coupez, ajoutez, mettez",
            "Les pommes, le sucre, le four",
            "Mais, puis, parce que",
        ],
        "antwoord": 0,
        "uitleg": "Dat zijn de signaalwoorden: eerst, daarna, ten slotte. De andere drie zijn de werkwoorden, oftewel wat je moet doen.",
    },
    {
        "type": "waarofniet",
        "vraag": "« Mais » betekent daarna en « puis » betekent maar.",
        "antwoord": False,
        "uitleg": "Niet waar, het is net omgekeerd: mais is maar, puis is daarna. Mais kondigt een tegenstelling aan, puis een volgende stap.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je beschrijft een foto: links staat een hond, in het midden staan twee kinderen. Welke zin klopt?",
        "opties": [
            "À gauche, il y a un chien. Au milieu, il y a deux enfants.",
            "À droite, il y a un chien. Au milieu, il y a deux enfants.",
            "Au milieu, il y a un chien. À gauche, il y a deux enfants.",
            "En haut, il y a un chien. À gauche, il y a deux enfants.",
        ],
        "antwoord": 0,
        "uitleg": "À gauche is links, à droite is rechts, au milieu is in het midden en en haut is bovenaan. « Il y a » is het vaste begin: er is of er zijn.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul aan: « Il ... chaud aujourd'hui. » (over het weer) Schrijf enkel de werkwoordsvorm.",
        "antwoord": "fait",
        "uitleg": "Over het weer zeg je in het Frans il fait: il fait chaud, il fait froid. Fait komt van faire.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je schrijft een mail aan de directeur van een Franse school. Welke slotgroet past?",
        "opties": ["Cordialement,", "Bises,", "Salut !", "À plus !"],
        "antwoord": 0,
        "uitleg": "Cordialement is de beleefde slotgroet voor iemand die je niet kent. Bises, salut en à plus horen bij vrienden.",
    },
    {
        "type": "waarofniet",
        "vraag": "« Je voudrais » klinkt beleefder dan « Je veux ».",
        "antwoord": True,
        "uitleg": "Waar. Je veux is ik wil, je voudrais is ik zou graag. In een winkel of een mail gebruik je die tweede vorm.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Lees: « En Belgique, on mange souvent des frites. En France, on mange plus de pain. » Wat besluit je?",
        "opties": [
            "De eetgewoonten verschillen van land tot land",
            "In Frankrijk eet men nooit frieten bij een maaltijd",
            "In België eet men helemaal geen brood meer",
            "De twee landen eten precies hetzelfde voedsel",
        ],
        "antwoord": 0,
        "uitleg": "Souvent is vaak en plus de is meer. De tekst vergelijkt gewoonten; hij zegt nergens dat het ene land iets nooit eet.",
    },
    {
        "type": "invultekst",
        "vraag": "Wat betekent « la boulangerie »? Antwoord met één Nederlands woord.",
        "antwoord": "bakkerij",
        "uitleg": "Le pain is het brood, en la boulangerie is de winkel waar je het koopt: de bakkerij.",
    },
    {
        "type": "waarofniet",
        "vraag": "Met « Quel livre ? » vraag je welk boek.",
        "antwoord": True,
        "uitleg": "Waar. Quel betekent welke, bij een mannelijk woord. Bij een vrouwelijk woord wordt dat quelle: quelle photo ?",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke zin is juist vervoegd?",
        "opties": [
            "Nous parlons français.",
            "Nous parlez français.",
            "Nous parle français.",
            "Nous parlent français.",
        ],
        "antwoord": 0,
        "uitleg": "Parler gaat: je parle, tu parles, il parle, nous parlons, vous parlez, ils parlent. Bij nous hoort dus parlons.",
    },
]
