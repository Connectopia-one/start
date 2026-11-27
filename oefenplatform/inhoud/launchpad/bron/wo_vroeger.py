# -*- coding: utf-8 -*-
"""Launchpad WO: vroeger en nu (tijd, toen ik klein was, opa en oma, dingen van vroeger)."""
from lp import K, I, W
import lpprent as P

TITEL = "Vroeger en nu"
UITLEG_1 = "Baby, kind, volwassene: zo word je ouder."
UITLEG_2 = "Hoe leefden opa en oma toen ze klein waren?"

DEEL_1 = [
    K("Wie is het jongst?", "een baby", ["een kleuter", "een tiener", "een opa"], "Een baby is pas geboren.", None),
    K("Wie is het oudst?", "een overgrootmoeder", ["een mama", "een kind", "een baby"], "De mama van je opa of oma is je overgrootmoeder.", None),
    K("Wat kon je als baby nog niet?", "lopen", ["huilen", "slapen", "drinken"], "Een baby leert pas lopen rond 1 jaar.", None),
    K("Wie is de mama van je mama?", "je oma", ["je tante", "je zus", "je nicht"], "De mama van je mama of papa is je oma.", None),
    K("Wie is de papa van je papa?", "je opa", ["je oom", "je broer", "je neef"], "De papa van je papa of mama is je opa.", None),
    K("Wat gebeurt er elk jaar op je verjaardag?", "je wordt een jaar ouder", ["je wordt jonger", "je wordt een baby", "er gebeurt niets"], "Op je verjaardag word je een jaar ouder.", None),
    K("Wat gebeurde eerst?", "je was een baby", ["je ging naar het 1ste leerjaar", "je leerde fietsen", "je leerde lezen"], "Eerst baby, dan kleuter, dan school.", None),
    K("Waar zie je foto's van toen je klein was?", "in een fotoalbum", ["in de koelkast", "in een kookboek", "op de stoep"], "Oude foto's zitten in een album of op de computer.", None),
    W("Je bent nu groter dan toen je een baby was.", True, "Elk jaar groei je een beetje."),
    W("Een baby kan al lezen.", False, "Lezen leer je in het 1ste leerjaar."),
    W("Je oma was vroeger ook een kind.", True, "Iedereen was ooit een kind."),
    W("Gisteren is in de toekomst.", False, "Gisteren is voorbij: het verleden."),
    W("Morgen is in de toekomst.", True, "Morgen moet nog komen."),
    W("Je opa is jonger dan jij.", False, "Je opa is ouder dan je mama of papa, en dus ook ouder dan jij."),
    W("In een fotoalbum kan je zien hoe je vroeger was.", True, "Foto's tonen vroeger."),
    W("Volwassenen worden elk jaar jonger.", False, "Iedereen wordt elk jaar ouder."),
    I("Je bent 6 jaar. Hoe oud ben je over 1 jaar? ___", 7, "6 + 1 = 7.", 7),
    I("Je zus is 3 jaar ouder dan jij. Jij bent 7. Hoe oud is ze? ___", 10, "7 + 3 = 10.", 10),
    K("Welk woord past bij iets dat al voorbij is?", "vroeger", ["morgen", "straks", "later"], "Vroeger is voorbij.", None),
    K("Welk woord past bij iets dat nog moet komen?", "later", ["gisteren", "vroeger", "vorig jaar"], "Later is in de toekomst.", None),
]

DEEL_2 = [
    K("Waarmee belden mensen vroeger?", "een telefoon met een draad", ["een gsm", "een tablet", "een slimme horloge"], "Vroeger hing de telefoon met een draad aan de muur.", None),
    K("Waarmee gaf men licht voor er elektriciteit was?", "een kaars", ["een lamp met batterij", "een gsm-lampje", "een ledlamp"], "Vroeger gebruikte men kaarsen en olielampen.", None),
    K("Hoe reisden mensen heel vroeger?", "te voet of met paard en kar", ["met het vliegtuig", "met de elektrische auto", "met de metro onder de grond"], "Auto's bestonden nog niet.", None),
    K("Hoe wasten mensen vroeger hun kleren?", "met de hand in een kuip", ["met een moderne wasmachine", "met een droogkast", "in de vaatwasmachine"], "Vroeger waste men met de hand.", None),
    K("Wat is nieuw, dat er vroeger niet was?", "een tablet", ["een boek", "een stoel", "een lepel"], "Tablets bestaan nog niet zo lang.", None),
    K("Wat is oud, dat er vroeger ook al was?", "een fiets", ["een gsm", "een tablet", "een spelconsole"], "Fietsen bestaan al heel lang.", None),
    K("Waarop schreven kinderen vroeger op school?", "een lei met een griffel", ["een tablet", "een laptop", "een groot digitaal schoolbord"], "Vroeger schreven kinderen op een leitje.", None),
    K("Wie kan je vragen hoe het vroeger was?", "je opa of oma", ["je kleine broer", "de baby", "je knuffel"], "Opa en oma weten hoe het vroeger was.", None),
    W("Vroeger had iedereen een gsm.", False, "Gsm's bestaan pas ongeveer 30 jaar."),
    W("Vroeger gebruikten mensen kaarsen voor licht.", True, "Voor er elektriciteit was."),
    W("Je opa speelde als kind met een tablet.", False, "Tablets bestonden toen nog niet."),
    W("Een paard en kar is een oud vervoermiddel.", True, "Voor de auto reden mensen met paard en kar."),
    W("Vroeger waren er al vliegtuigen voor iedereen.", False, "Lang geleden bestonden er nog geen vliegtuigen."),
    W("Kinderen speelden vroeger ook met een bal.", True, "Ballen bestaan al heel lang."),
    W("Een oude telefoon had vaak een draad.", True, "Die hing aan de muur of stond op een kastje."),
    W("Een gsm is ouder dan een kaars.", False, "Kaarsen bestaan al veel langer."),
    I("Hoeveel jaar zitten in 10 jaar plus 10 jaar? ___", 20, "10 + 10 = 20.", 20),
    K("Wat zet je op een tijdlijn eerst?", "het oudste", ["het nieuwste", "het mooiste", "het grootste"], "Op een tijdlijn zet je het oudste vooraan.", None),
    K("Wat is het oudst?", "een kaars", ["een gloeilamp", "een ledlamp", "een gsm-lampje"], "Kaarsen bestaan al het langst.", None),
    K("Wat is het nieuwst?", "een gsm", ["een oude telefoon met draad", "een brief", "een postduif"], "De gsm is het nieuwst.", None),
]

PRENT_1 = [
    K("Wat gebruikte men vroeger om licht te maken?", "de kaars", ["de lamp", "allebei even oud"], "Kaarsen bestaan al veel langer dan lampen.", None, prent=P.rij("vroeger-kaars-lamp", ["kaars", "gloeilamp"])),
    W("De telefoon met draad is ouder dan de gsm.", True, "Eerst had men telefoons met een draad, later kwam de gsm.", prent=P.rij("vroeger-telefoons", ["oude-telefoon", "gsm"])),
    I("Hoeveel kaarsjes staan op de taart?", 4, "Tel de kaarsjes: 4.", 4, prent=P.een("vroeger-taart", "lp-verjaardag")),
    K("Wanneer werd deze tekening gemaakt?", "heel lang geleden", ["gisteren na school", "vorige week"], "Mensen van heel vroeger tekenden dieren op de muur van een grot.", None, prent=P.een("vroeger-grot", "grotschildering")),
]
PRENT_2 = [
    K("Bestond dit al toen je overgrootouders kind waren?", "nee", ["ja"], "Gsm's bestaan nog niet zo lang.", None, prent=P.een("vroeger-gsm", "gsm")),
    W("Mensen gebruiken al heel lang kaarsen.", True, "Kaarsen bestaan al heel lang.", prent=P.een("vroeger-kaars", "kaars")),
    K("Wat vier je met deze taart?", "een verjaardag", ["Kerstmis", "Pasen", "Halloween"], "Een taart met kaarsjes hoort bij een verjaardag.", None, prent=P.een("vroeger-verjaardag", "lp-verjaardag")),
    I("Wat is het oudst? Schrijf de letter.", ["A", "a"], "De kaars (A) is het oudst. Daarna kwam de lamp, en het laatst de gsm.", None, prent="/examenvormen/ready/tijd-oudste.webp"),
]
