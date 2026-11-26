# -*- coding: utf-8 -*-
"""Ready geschiedenis: Hoe leefden mensen vroeger? (prehistorie: jagers en verzamelaars,
de eerste boeren; Romeinen in onze streken; middeleeuwen: ridders, kastelen, steden).
Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Hoe leefden mensen vroeger?"
UITLEG_1 = "De eerste mensen en de Romeinen."
UITLEG_2 = "Ridders, kastelen en steden."

DEEL_1 = [
    mk("Hoe kwamen de eerste mensen aan hun eten?", ["door te jagen en te verzamelen", "in de supermarkt om de hoek", "met een pizzakoerier op de fiets", "uit de diepvries"], 0, "Ze jaagden op dieren en zochten bessen, noten en wortels."),
    wn("De eerste mensen maakten werktuigen van steen.", True, "Daarom noemt men die tijd ook de steentijd."),
    mk("Waarom trokken de eerste jagers rond?", ["Ze zochten eten.", "Ze waren op reis voor hun plezier.", "Ze moesten naar school.", "Ze zochten een winkel."], 0, "Als het eten op was, trokken ze verder."),
    inv("Mensen die op één plaats bleven wonen en graan zaaiden, werden de eerste ___. (b...)", ["boeren", "boer"], "Ze bouwden huizen, hielden dieren en zaaiden graan."),
    mk("Wat ontdekten de eerste mensen dat hen warm hield en waarop ze konden koken?", ["vuur", "elektriciteit", "gas", "de microgolfoven"], 0, "Vuur gaf warmte, licht en bescherming."),
    wn("De eerste mensen maakten nooit tekeningen.", False, "In grotten vond men tekeningen van dieren, zoals paarden en bizons."),
    wn("In de prehistorie konden de mensen al lezen en schrijven.", False, "Prehistorie betekent: de tijd vóór het schrift."),
    mk("Waar komen de Romeinen oorspronkelijk vandaan?", ["uit Rome", "uit Brugge", "uit Amerika", "uit China"], 0, "Rome ligt in Italië. Van daaruit veroverden ze een groot rijk."),
    mk("Welke Belgische stad gaat terug tot de Romeinen en geldt als de oudste stad van België?", ["Tongeren", "Genk", "Oostende", "Leuven"], 0, "Tongeren was een Romeinse stad: Atuatuca Tungrorum."),
    inv("De Romeinen spraken ___. (L...)", ["Latijn"], "Veel woorden in onze taal komen uit het Latijn, zoals muur (murus) en straat (strata)."),
    wn("De Romeinen hadden alleen kronkelige zandpaadjes.", False, "De Romeinen legden lange, rechte wegen aan. Daarover trokken soldaten en handelaars."),
    mk("Welke cijfers gebruikten de Romeinen?", ["I, V, X, L, C", "1, 2, 3, 4, 5", "a, b, c, d", "geen cijfers"], 0, "Romeinse cijfers zie je nog op sommige klokken: XII is 12."),
    inv("Het Romeinse cijfer V betekent ___.", "5", "I = 1, V = 5, X = 10.", 5),
    mk("Hoe heette de leider van het Romeinse Rijk?", ["de keizer", "de burgemeester", "de juf", "de koning van België"], 0, "Julius Caesar en Augustus zijn bekende Romeinse leiders."),
    wn("De Romeinen brachten nieuwe dingen naar onze streken, zoals stenen huizen en badhuizen.", True, "Ze bouwden met steen en hadden openbare badhuizen."),
    mk("Hoe noemt men de mensen die hier woonden toen de Romeinen kwamen?", ["Keltische stammen", "de Vikingen", "de Amerikanen", "de Chinezen"], 0, "Julius Caesar noemde die stammen hier de Belgen. Ambiorix was koning van de Eburonen."),
    wn("Ambiorix is een bekende leider die tegen de Romeinen vocht.", True, "Er staat een standbeeld van Ambiorix in Tongeren."),
    mk("Wat is XI in gewone cijfers?", ["9", "11", "15", "110"], 1, "X = 10 en I = 1: 10 + 1 = 11.", 11),
    wn("De Romeinen hadden al auto's om over hun wegen te rijden.", False, "Ze reden met karren, te paard of liepen."),
    wn("Een archeoloog graaft voorwerpen uit de grond om meer te weten over vroeger.", True, "Zo vond men in Tongeren veel Romeinse voorwerpen."),
]

DEEL_2 = [
    mk("Wie droeg een harnas en vocht te paard in de middeleeuwen?", ["een ridder", "een boer", "een monnik", "een koopman"], 0, "Ridders vochten voor hun heer, te paard en met een zwaard."),
    mk("Waarom stond een kasteel vaak op een heuvel of had het een gracht?", ["om zich beter te kunnen verdedigen", "voor het mooie uitzicht", "om makkelijk te zwemmen", "om vissen te kweken"], 0, "Vijanden konden er zo moeilijk binnen."),
    inv("Een brug die je omhoog kan trekken voor een kasteel, heet een ___brug. (o...)", ["ophaal", "ophaalbrug"], "Met de ophaalbrug kon het kasteel afgesloten worden."),
    wn("Het Gravensteen in Gent werd gebouwd door de Romeinen.", False, "Het Gravensteen is een middeleeuwse burcht. De graven van Vlaanderen woonden er."),
    mk("Wat deed een schildknaap?", ["Hij hielp een ridder.", "Hij schilderde schilden in alle kleuren.", "Hij was een soort leraar.", "Hij bakte brood."], 0, "Een jongen werd eerst page, dan schildknaap en daarna ridder."),
    mk("Waar woonden en werkten de monniken?", ["in een abdij of klooster", "in een kasteel", "op een schip", "in een fabriek"], 0, "Monniken baden, werkten en schreven boeken over met de hand."),
    wn("In de middeleeuwen werden boeken met de hand overgeschreven.", True, "De drukpers kwam pas op het einde van de middeleeuwen."),
    mk("Wat was een gilde?", ["mensen met hetzelfde beroep", "een soort kasteel", "een wapen", "een feestdag"], 0, "Bakkers, smeden en wevers hadden elk hun eigen gilde."),
    inv("In de middeleeuwen werden steden beschermd door hoge ___. (m...)", ["muren", "stadsmuren", "stadsmuur"], "Een stadsmuur met poorten hield vijanden buiten."),
    wn("De meeste mensen in de middeleeuwen waren ridders.", False, "De meeste mensen waren boeren die op het land werkten."),
    mk("Welk gebouw in een middeleeuwse stad diende als uitkijktoren en bewaarde belangrijke papieren?", ["het belfort", "de bakkerij", "de stal", "de molen"], 0, "Belforten staan nog in Brugge, Gent en andere steden."),
    mk("Hoe kreeg men licht in een kasteel?", ["met kaarsen en fakkels", "met lampen op batterijen", "met elektrisch licht", "met zaklampen"], 0, "Elektriciteit bestond nog niet."),
    wn("Een riddertoernooi was een wedstrijd tussen boeren.", False, "Het was een wedstrijd tussen ridders: ze reden met een lans op elkaar af."),
    inv("Een kasteel met een gracht errond: in de gracht zat ___.", ["water"], "Een gracht is een brede sloot met water."),
    mk("Wat was een markt in een middeleeuwse stad?", ["een plein om te kopen en verkopen", "een ridderkamp", "een school", "een ziekenhuis voor zieke ridders"], 0, "Op de Grote Markt kwamen boeren en handelaars samen."),
    wn("Lakens van wol maakten Vlaamse steden zoals Brugge en Ieper rijk.", True, "Vlaams laken werd tot ver buiten Vlaanderen verkocht."),
    mk("Wat at een gewone boer in de middeleeuwen meestal?", ["brood, pap en groenten", "frietjes met mayonaise en stoofvlees", "pizza", "sushi"], 0, "Vlees was duur. Boeren aten vooral brood, pap en groenten."),
    wn("Kinderen van boeren gingen in de middeleeuwen allemaal naar school.", False, "De meeste kinderen hielpen op het land. Weinig kinderen leerden lezen en schrijven."),
    mk("Welke volgorde gaat van vroeg naar laat?", ["prehistorie, Romeinen, middeleeuwen", "middeleeuwen, Romeinen, prehistorie", "Romeinen, prehistorie, middeleeuwen", "prehistorie, middeleeuwen, Romeinen"], 0, "Eerst de prehistorie, dan de Romeinen en daarna de middeleeuwen."),
    wn("Ridders leefden na de Romeinen.", True, "De middeleeuwen, de tijd van de ridders, kwamen na de Romeinse tijd."),
]


# Prentvragen (vraag 21 tot 24), Kim 26/11.
from vr import mk, inv, wn
import prent as P
PRENT_1 = [
    inv("Welk getal is dit in Romeinse cijfers?", "12", "X = 10 en II = 2. Samen 12.", 12, prent=P.p_tekst("vroeger-romeins-12", ["XII"], 60)),
    mk("Welk getal schreven de Romeinen zo?", ["8", "12", "3", "7"], 0, "V = 5 en III = 3. Samen 8.", prent=P.p_tekst("vroeger-romeins-8", ["VIII"], 60)),
    wn("De eerste mensen schilderden dieren op de wanden van grotten.", True, "Zulke grotschilderingen zijn duizenden jaren oud.", prent=P.p_grot("vroeger-grot")),
    mk("Waarvoor gebruikten de eerste mensen dit stenen werktuig?", ["om te snijden en te hakken", "om te schrijven", "om muziek te maken", "om mee te betalen"], 0, "Met een vuistbijl sneden ze vlees en hakten ze hout.", prent=P.p_ding("vroeger-vuistbijl", "vuistbijl")),
]
PRENT_2 = [
    mk("Hoe heet het deel van de burcht bij de pijl?", ["de slotgracht", "de toren", "de ophaalbrug", "de muur"], 0, "Rond de burcht lag water: de slotgracht.", prent=P.p_kasteel("vroeger-burcht-gracht", "gracht")),
    inv("Hoe heet het deel van de burcht bij de pijl? De o...", ["ophaalbrug", "de ophaalbrug"], "De ophaalbrug kon omhoog, zodat vijanden niet binnen konden.", prent=P.p_kasteel("vroeger-burcht-brug", "ophaalbrug")),
    wn("Vanop de toren konden de wachters ver kijken of er vijanden kwamen.", True, "Hoge torens gaven een goed uitzicht.", prent=P.p_kasteel("vroeger-burcht-toren", "toren")),
    mk("Waarom droeg een ridder een schild?", ["om zich te beschermen", "om mee te koken", "om op te zitten", "om er licht mee te maken"], 0, "Met het schild hield een ridder slagen en pijlen tegen.", prent=P.p_ding("vroeger-schild", "schild")),
]
