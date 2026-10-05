# -*- coding: utf-8 -*-
"""Woordvelden: eten en drinken, winkelen, kleding, kleuren, wonen.

Uit de vakfiche Frans van de 2de graad dubbele finaliteit. De woordvelden die
hier aan bod komen: eten en drinken; winkels en diensten; cijfers, gewichten,
maten en hoeveelheden; kleding en accessoires; kleuren, vormen en materialen;
de woning met haar meubels en uitrusting; dagelijkse bezigheden; en dagelijkse
of persoonlijke voorwerpen.

Dit zijn de woorden van een gewone dag, en net daarom komen ze op het examen
voortdurend terug: in een recept, in een zoekertje, in een gesprek aan een
kassa, in een bericht aan een huisgenoot.

Deel 1 gaat over eten, winkelen en hoeveelheden. Deel 2 gaat over kleding,
kleuren en materialen, de woning, en wat je op een dag allemaal doet.
"""

MENU = (
    "Menu du jour — Entrée : soupe de légumes ou salade de tomates. Plat : poulet et frites, ou "
    "pâtes aux champignons (plat végétarien). Dessert : glace, fruits de saison ou crêpe au "
    "sucre. Boisson comprise : eau, jus d'orange ou limonade. 14 euros."
)
COURSES = (
    "N'oublie pas : un kilo de pommes de terre, 500 grammes de carottes, une bouteille de lait, "
    "six œufs et un paquet de pâtes. Si le pain est encore chaud, prends-en deux."
)
CAISSE = (
    "— Bonjour, ce sera tout ? — Oui, et je voudrais un sac, s'il vous plaît. — Ça fait "
    "23,40 euros. Vous payez par carte ou en espèces ? — Par carte. — Voilà votre ticket, bonne "
    "journée !"
)

DEEL1 = [
    # --- Le menu -----------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit menu: « {MENU} » Je eet geen vlees. Welk hoofdgerecht kies je?",
         opties=["pâtes aux champignons",
                 "poulet et frites",
                 "soupe de légumes",
                 "salade de tomates"],
         antwoord=0,
         uitleg="Le plat is het hoofdgerecht, en bij de pasta staat plat végétarien. Soep en tomatensalade zijn voorgerechten."),
    dict(type="invultekst",
         vraag="Hetzelfde menu. Hoeveel euro kost het? Schrijf alleen het getal.",
         antwoord=["14"],
         uitleg="14 euros, onderaan het menu."),
    dict(type="meerkeuze",
         vraag="Nog dat menu. Welke dranken zitten in de prijs?",
         opties=["water",
                 "sinaasappelsap",
                 "limonade",
                 "koffie"],
         antwoord=[0, 1, 2],
         uitleg="Boisson comprise betekent drank inbegrepen: eau, jus d'orange ou limonade. Koffie staat er niet bij."),
    dict(type="waarofniet",
         vraag="Une crêpe au sucre op dat menu is een nagerecht.",
         antwoord=True,
         uitleg="Ze staat bij dessert, samen met de glace en de fruits de saison. Le sucre is suiker."),
    dict(type="meerkeuze",
         vraag="Welk Frans woord betekent 'kip'?",
         opties=["le poulet", "le poisson", "le porc", "le pain"],
         antwoord=0,
         uitleg="Le poulet is kip, le poisson vis, le porc varkensvlees, le pain brood. Vier woorden met een p die je niet mag verwarren."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'kaas'? Schrijf het woord zonder lidwoord.",
         antwoord=["fromage"],
         uitleg="Le fromage. In Frankrijk komt hij op tafel vóór het dessert."),
    # --- Les courses --------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit boodschappenlijstje: « {COURSES} » Hoeveel eieren moet je meebrengen?",
         opties=["zes", "twee", "vijf", "een pak"],
         antwoord=0,
         uitleg="Six œufs. Un œuf is een ei; de f hoor je in het enkelvoud, in het meervoud niet."),
    dict(type="meerkeuze",
         vraag="Hetzelfde lijstje. Hoeveel gram wortelen staat erop?",
         opties=["500 gram", "een kilo", "250 gram", "een pak"],
         antwoord=0,
         uitleg="500 grammes de carottes. Une carotte is een wortel."),
    dict(type="invultekst",
         vraag="Nog dat lijstje. Welk Frans woord betekent 'fles'? Schrijf het woord zonder lidwoord.",
         antwoord=["bouteille"],
         uitleg="Une bouteille de lait: een fles melk."),
    dict(type="waarofniet",
         vraag="Volgens dat lijstje moet je twee broden meebrengen als het brood nog warm is.",
         antwoord=True,
         uitleg="Prends-en deux: neem er twee van. En vervangt hier het brood."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden drukken een hoeveelheid uit?",
         opties=["un kilo de",
                 "un paquet de",
                 "beaucoup de",
                 "parce que"],
         antwoord=[0, 1, 2],
         uitleg="Na een hoeveelheid komt de en geen lidwoord: beaucoup de sucre, un litre d'eau. Parce que betekent omdat."),
    # --- À la caisse ---------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit gesprekje: « {CAISSE} » Hoe betaalt de klant?",
         opties=["met de kaart", "met cash geld", "met een cheque", "met de app"],
         antwoord=0,
         uitleg="Par carte. En espèces betekent met cash geld, en dat is net wat hij niet doet."),
    dict(type="invultekst",
         vraag="Hetzelfde gesprekje. Welke Franse uitdrukking betekent 'met cash geld'? Vul in: « en ... ». Schrijf één woord.",
         antwoord=["espèces"],
         uitleg="Payer en espèces. Payer par carte is met de kaart betalen."),
    dict(type="meerkeuze",
         vraag="Je wil in een Franse winkel vragen hoeveel iets kost. Welke zin past?",
         opties=["Ça coûte combien ?",
                 "C'est quoi le prix pour moi ?",
                 "Je veux savoir l'argent.",
                 "Combien je paie l'argent ?"],
         antwoord=0,
         uitleg="Ça coûte combien ? of Combien ça coûte ? Allebei goed; de andere drie zijn geen Frans dat een winkelier zegt."),
    dict(type="waarofniet",
         vraag="Une boucherie is een bakkerij.",
         antwoord=False,
         uitleg="Une boucherie is een slagerij. Een bakkerij is une boulangerie, van le pain."),
    dict(type="meerkeuze",
         vraag="Waar koop je in Frankrijk een stokbrood?",
         opties=["à la boulangerie", "à la pharmacie", "à la librairie", "à la banque"],
         antwoord=0,
         uitleg="Une baguette koop je bij de bakker. Une librairie is een boekhandel, niet een bibliotheek."),
    dict(type="meerkeuze",
         vraag="Welke woorden horen bij het woordveld winkels en diensten?",
         opties=["le magasin",
                 "la poste",
                 "la banque",
                 "la cuisine"],
         antwoord=[0, 1, 2],
         uitleg="Winkel, post, bank. La cuisine is de keuken, en die hoort bij de woning."),
    dict(type="waarofniet",
         vraag="Un billet en une pièce zijn allebei geld van papier.",
         antwoord=False,
         uitleg="Un billet de vingt euros is een biljet, une pièce de deux euros een muntstuk. Un billet kan trouwens ook een ticket zijn, bijvoorbeeld voor de trein."),
    dict(type="meerkeuze",
         vraag="Je staat aan de kassa en de verkoper vraagt « Ce sera tout ? » Wat vraagt hij?",
         opties=["of dat alles is",
                 "of je een zak nodig hebt",
                 "of je met de kaart betaalt",
                 "of je een klantenkaart hebt"],
         antwoord=0,
         uitleg="Ce sera tout ? is letterlijk: dat zal alles zijn? Het hoort bij de vaste uitdrukkingen aan een kassa."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'kassabon'? Schrijf het woord zonder lidwoord.",
         antwoord=["ticket"],
         uitleg="Voilà votre ticket. Het Frans gebruikt hier hetzelfde woord als wij voor een ticket."),
]

VETEMENTS = (
    "Pour l'entretien, mets un pantalon noir et une chemise blanche. Pas de baskets : des "
    "chaussures fermées. S'il fait froid, prends ta veste grise, mais laisse ton bonnet dans ton "
    "sac."
)
MAISON = (
    "L'appartement a deux chambres, une cuisine équipée et une petite salle de bains. Le salon "
    "donne sur un balcon. Il y a un lave-linge dans la cave. Le loyer est de 650 euros par mois, "
    "charges comprises."
)
JOURNEE = (
    "En semaine, je me lève à six heures et demie. Je me douche, je prends mon petit-déjeuner et "
    "je pars à sept heures et quart. L'après-midi, je fais mes devoirs avant de sortir. Le soir, "
    "c'est moi qui mets la table et mon frère qui fait la vaisselle."
)

DEEL2 = [
    # --- Les vêtements -------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit bericht: « {VETEMENTS} » Wat mag je niet aandoen?",
         opties=["sportschoenen",
                 "een witte hemd",
                 "een zwarte broek",
                 "een grijze vest"],
         antwoord=0,
         uitleg="Pas de baskets: geen sportschoenen. Des chaussures fermées zijn gesloten schoenen."),
    dict(type="invultekst",
         vraag="Hetzelfde bericht. Welk Frans woord betekent 'broek'? Schrijf het woord zonder lidwoord.",
         antwoord=["pantalon"],
         uitleg="Un pantalon, in het Frans enkelvoud waar wij 'een broek' ook enkelvoud zeggen maar 'een paar broeken' niet bedoelen."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden zijn kledingstukken?",
         opties=["une chemise",
                 "une veste",
                 "une jupe",
                 "une assiette"],
         antwoord=[0, 1, 2],
         uitleg="Hemd, vest, rok. Une assiette is een bord en hoort bij de keuken."),
    dict(type="waarofniet",
         vraag="Un bonnet is een muts.",
         antwoord=True,
         uitleg="Un bonnet de bain is dan weer een badmuts, verplicht in veel Franse zwembaden."),
    dict(type="meerkeuze",
         vraag="Welke kleur is grise?",
         opties=["grijs", "groen", "geel", "bruin"],
         antwoord=0,
         uitleg="Gris of grise is grijs. Groen is vert, geel jaune, bruin brun of marron."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'zwart'? Schrijf de mannelijke vorm.",
         antwoord=["noir"],
         uitleg="Noir, in het vrouwelijk noire. Wit is blanc, in het vrouwelijk blanche."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden noemen een materiaal?",
         opties=["le bois",
                 "le verre",
                 "le coton",
                 "le carré"],
         antwoord=[0, 1, 2],
         uitleg="Hout, glas, katoen. Un carré is een vierkant, en dat is een vorm."),
    dict(type="waarofniet",
         vraag="Rond, carré en rectangulaire zijn in het Frans kleuren.",
         antwoord=False,
         uitleg="Het zijn vormen: rond, vierkant, rechthoekig. Kleuren, vormen en materialen staan in hetzelfde woordveld, maar zijn niet hetzelfde."),
    # --- La maison ------------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit zoekertje: « {MAISON} » Hoeveel slaapkamers heeft het appartement?",
         opties=["twee", "een", "drie", "dat staat er niet"],
         antwoord=0,
         uitleg="Deux chambres. Une chambre is een slaapkamer; une salle de bains is de badkamer."),
    dict(type="invultekst",
         vraag="Hetzelfde zoekertje. Hoeveel euro is de huur per maand? Schrijf alleen het getal.",
         antwoord=["650"],
         uitleg="Le loyer est de 650 euros par mois. Un loyer is de huur."),
    dict(type="meerkeuze",
         vraag="Nog dat zoekertje. Waar staat de wasmachine?",
         opties=["in de kelder", "in de keuken", "in de badkamer", "op het balkon"],
         antwoord=0,
         uitleg="Un lave-linge dans la cave. Une cave is een kelder, geen café."),
    dict(type="waarofniet",
         vraag="Volgens dat zoekertje zijn de kosten bij de huurprijs inbegrepen.",
         antwoord=True,
         uitleg="Charges comprises betekent kosten inbegrepen. Comprendre is hier insluiten, niet begrijpen."),
    dict(type="meerkeuze",
         vraag="Welke Franse woorden zijn meubels of uitrusting van een woning?",
         opties=["une table",
                 "un lit",
                 "un frigo",
                 "un loyer"],
         antwoord=[0, 1, 2],
         uitleg="Tafel, bed, koelkast. Un loyer is de huurprijs en dus geen voorwerp."),
    dict(type="invultekst",
         vraag="Welk Frans woord betekent 'keuken'? Schrijf het woord zonder lidwoord.",
         antwoord=["cuisine"],
         uitleg="La cuisine is zowel de keuken als de keukenkunst: la cuisine française."),
    # --- La journée ------------------------------------------------------------
    dict(type="meerkeuze",
         vraag=f"Lees dit tekstje: « {JOURNEE} » Hoe laat vertrekt deze persoon?",
         opties=["kwart na zeven", "half zeven", "kwart voor zeven", "zeven uur"],
         antwoord=0,
         uitleg="Sept heures et quart: zeven uur en een kwart, dus 7.15 u. Six heures et demie is half zeven."),
    dict(type="meerkeuze",
         vraag="Hetzelfde tekstje. Wie doet wat 's avonds?",
         opties=["de schrijver dekt de tafel, zijn broer doet de vaat",
                 "de schrijver doet de vaat, zijn broer dekt de tafel",
                 "ze doen allebei de vaat",
                 "hun ouders doen alles"],
         antwoord=0,
         uitleg="C'est moi qui mets la table et mon frère qui fait la vaisselle. Mettre la table is de tafel dekken, faire la vaisselle de vaat doen."),
    dict(type="invultekst",
         vraag="Nog dat tekstje. Welke Franse uitdrukking betekent 'ik sta op'? Vul in: « je me ... ». Schrijf één woord.",
         antwoord=["lève"],
         uitleg="Se lever is opstaan, een wederkerend werkwoord: je me lève, tu te lèves."),
    dict(type="meerkeuze",
         vraag="Welke Franse uitdrukkingen horen bij de dagelijkse bezigheden?",
         opties=["faire la vaisselle",
                 "ranger sa chambre",
                 "sortir la poubelle",
                 "avoir mal au dos"],
         antwoord=[0, 1, 2],
         uitleg="De vaat doen, je kamer opruimen, het vuilnis buitenzetten. Rugpijn hebben is geen bezigheid."),
    dict(type="waarofniet",
         vraag="Se doucher betekent zich scheren.",
         antwoord=False,
         uitleg="Se doucher is zich douchen. Zich scheren is se raser."),
    dict(type="meerkeuze",
         vraag="Welke persoonlijke voorwerpen zitten in deze rij Franse woorden?",
         opties=["les clés",
                 "le portefeuille",
                 "le parapluie",
                 "le balcon"],
         antwoord=[0, 1, 2],
         uitleg="Sleutels, portefeuille, paraplu. Un balcon hoort bij de woning en gaat niet mee in je zak."),
]
