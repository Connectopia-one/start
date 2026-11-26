# -*- coding: utf-8 -*-
"""Ready (3de en 4de leerjaar), Nederlands, proefhoofdstuk "Spelling".

Officieel doel einde 4de leerjaar (brochure Minimumdoelen en visieteksten
... 4de en 6de jaar lager onderwijs, Vlaamse overheid, stand 25/11/2026):
klankgroepen ei/ij, au/ou, aai/oei/ooi, eeuw/ieuw, ng/nk, ch/g; b/p en d/t
aan het eind; meervoud; verkleinwoord; hoofdletters.
Bouwen en nakijken: python3 bouw.py nederlands_spelling
"""

TITEL = "Spelling"

UITLEG_1 = 'ei of ij, au of ou, ng of nk.'

UITLEG_2 = 'd of t, meervoud, verkleinwoord en hoofdletters.'

DEEL_1 = [
    dict(type="waarofniet", vraag="Je schrijft trein met ei.", antwoord=True,
         uitleg="Trein is een ei-woord, net als klein, geit en plein."),
    dict(type="invultekst", vraag="Vul ei of ij in: de g__t eet gras.", antwoord="ei",
         uitleg="Geit schrijf je met ei."),
    dict(type="invultekst", vraag="Vul ei of ij in: ik heb v__f vingers aan elke hand.", antwoord="ij",
         uitleg="Vijf schrijf je met ij."),
    dict(type="meerkeuze", vraag="In welk woord hoort ij?", opties=["tr__n", "t__d", "pl__n", "g__t"], antwoord=1,
         uitleg="Tijd schrijf je met ij. Trein, plein en geit zijn ei-woorden."),
    dict(type="waarofniet", vraag="Je schrijft blauw met ou, net als koud.", antwoord=False,
         uitleg="Blauw schrijf je met au. Koud schrijf je wel met ou."),
    dict(type="meerkeuze", vraag="Welk woord is fout geschreven?", opties=["koud", "zaut", "pauw", "vrouw"], antwoord=1,
         uitleg="Het is zout, met ou. De andere woorden zijn juist."),
    dict(type="invultekst", vraag="Vul au of ou in: de p__w heeft een prachtige staart.", antwoord="au",
         uitleg="Pauw schrijf je met au."),
    dict(type="invultekst", vraag="Vul au of ou in: in de winter is het k__d.", antwoord="ou",
         uitleg="Koud schrijf je met ou, net als oud en goud."),
    dict(type="meerkeuze", vraag="Hoe schrijf je het dier dat melk geeft?", opties=["koeij", "koei", "koeie", "kooi"], antwoord=1,
         uitleg="Koei schrijf je met oei. Een kooi is iets anders: daar zit een vogel in."),
    dict(type="waarofniet", vraag="Mooi schrijf je met ooi, net als kooi en hooi.", antwoord=True,
         uitleg="Mooi, kooi en hooi eindigen allemaal op ooi."),
    dict(type="invultekst", vraag="Vul aai, oei of ooi in: een h__ zwemt in de zee en heeft scherpe tanden.", antwoord="aai",
         uitleg="Haai schrijf je met aai, net als kraai."),
    dict(type="meerkeuze", vraag="Welk woord is juist geschreven?", opties=["sneew", "sneuw", "sneeuw", "sneauw"], antwoord=2,
         uitleg="Sneeuw schrijf je met eeuw, net als leeuw en meeuw."),
    dict(type="waarofniet", vraag="Nieuw schrijf je met eeuw.", antwoord=False,
         uitleg="Nieuw schrijf je met ieuw."),
    dict(type="invultekst", vraag="Vul eeuw of ieuw in: de l___ is de koning van de dieren.", antwoord="eeuw",
         uitleg="Leeuw schrijf je met eeuw."),
    dict(type="meerkeuze", vraag="Welk woord eindigt op nk?", opties=["ring", "bank", "koning", "bang"], antwoord=1,
         uitleg="In bank hoor je op het einde een k. In ring, koning en bang niet."),
    dict(type="invultekst", vraag="Vul ng of nk in: ik dri__ elke dag water.", antwoord="nk",
         uitleg="Drink: je hoort op het einde een k."),
    dict(type="waarofniet", vraag="Bij nk hoor je op het einde een k, bij ng niet.", antwoord=True,
         uitleg="Bank, drink en denk hoor je met een k. Ring, bang en koning niet."),
    dict(type="meerkeuze", vraag="Dag of dach? Wat is juist, en waarom?",
         opties=["dach, want je hoort ch", "dag, want je zegt dagen", "dag, want het is een kort woord", "dach, want het meervoud is dachen"], antwoord=1,
         uitleg="Maak het woord langer: dagen. Je hoort een g, dus schrijf je dag."),
    dict(type="invultekst", vraag="Vul g of ch in: die mop is grappig, ik la__ hard.", antwoord="ch",
         uitleg="Maak het woord langer: lachen. Je hoort ch, dus schrijf je lach."),
    dict(type="waarofniet", vraag="Je schrijft berch met ch op het einde.", antwoord=False,
         uitleg="Maak het woord langer: bergen. Je hoort een g, dus schrijf je berg."),
]

DEEL_2 = [
    dict(type="meerkeuze", vraag="Hond of hont? Wat is juist, en waarom?",
         opties=["hont, want je hoort een t", "hond, want het is een dier", "hond, want je zegt honden", "hont, want het meervoud is honten"], antwoord=2,
         uitleg="Maak het woord langer: honden. Je hoort een d, dus schrijf je hond."),
    dict(type="invultekst", vraag="Vul d of t in: op mijn b__ ligt een dikke deken.", antwoord="d",
         uitleg="Maak het woord langer: bedden. Je hoort een d, dus schrijf je bed."),
    dict(type="invultekst", vraag="Vul d of t in: de ka__ jaagt op een muis.", antwoord="t",
         uitleg="Maak het woord langer: katten. Je hoort een t, dus schrijf je kat."),
    dict(type="invultekst", vraag="Vul b of p in: de spin maakt een we__.", antwoord="b",
         uitleg="Maak het woord langer: webben. Je hoort een b, dus schrijf je web."),
    dict(type="waarofniet", vraag="Je schrijft paart met een t, want je hoort een t.", antwoord=False,
         uitleg="Maak het woord langer: paarden. Je hoort een d, dus schrijf je paard."),
    dict(type="meerkeuze", vraag="Wat is het meervoud van boom?", opties=["boomen", "bomen", "boommen", "booms"], antwoord=1,
         uitleg="Eén boom, twee bomen. In bo-men hoor je de o lang, dus één o is genoeg."),
    dict(type="meerkeuze", vraag="Wat is het meervoud van bal?", opties=["balen", "bals", "ballen", "baalen"], antwoord=2,
         uitleg="Eén bal, twee ballen. De a blijft kort, daarom komt er een l bij."),
    dict(type="invultekst", vraag="Eén huis, twee ___ .", antwoord="huizen",
         uitleg="In het meervoud wordt de s een z: huizen."),
    dict(type="meerkeuze", vraag="Wat is het meervoud van tafel?", opties=["tafelen", "tafels", "tafel's", "taffels"], antwoord=1,
         uitleg="Bij tafel komt er gewoon een s achter: tafels."),
    dict(type="waarofniet", vraag="Het meervoud van auto is auto's.", antwoord=True,
         uitleg="Eindigt een woord op a, o, u of i, dan zet je er 's achter: auto's, oma's."),
    dict(type="invultekst", vraag="Eén brief, drie ___ .", antwoord="brieven",
         uitleg="In het meervoud wordt de f een v: brieven."),
    dict(type="meerkeuze", vraag="Welk meervoud is juist geschreven?", opties=["kaaten", "kipen", "sloten", "brugen"], antwoord=2,
         uitleg="Slot wordt sloten. Het moet ook katten, kippen en bruggen zijn."),
    dict(type="meerkeuze", vraag="Wat is het verkleinwoord van boom?", opties=["boomje", "boompje", "boomtje", "bommetje"], antwoord=1,
         uitleg="Na een m komt er vaak -pje: boompje, raampje."),
    dict(type="invultekst", vraag="Een kleine stoel is een ___ .", antwoord="stoeltje",
         uitleg="Na een l komt er vaak -tje: stoeltje."),
    dict(type="meerkeuze", vraag="Wat is het verkleinwoord van bal?", opties=["baltje", "balje", "ballentje", "balletje"], antwoord=3,
         uitleg="Bij een kort woord met een korte klank komt er -etje en verdubbelt de l: balletje."),
    dict(type="waarofniet", vraag="Het verkleinwoord van koning is koninkje.", antwoord=True,
         uitleg="Na ng komt er -kje, en de g wordt een k: koninkje."),
    dict(type="invultekst", vraag="Een klein huis is een ___ .", antwoord="huisje",
         uitleg="Na een s komt er gewoon -je: huisje."),
    dict(type="meerkeuze", vraag="Welke woorden krijgen altijd een hoofdletter?",
         opties=["de namen van de dagen en de maanden", "namen van mensen, steden en landen",
                 "alle zelfstandige naamwoorden in een zin", "elk woord dat na een komma staat"], antwoord=1,
         uitleg="Namen van mensen, steden en landen krijgen een hoofdletter. Dagen en maanden niet."),
    dict(type="waarofniet", vraag="Maandag schrijf je met een hoofdletter.", antwoord=False,
         uitleg="Dagen van de week schrijf je met een kleine letter: maandag. Alleen aan het begin van een zin krijgen ze een hoofdletter."),
    dict(type="meerkeuze", vraag="Welke zin is juist geschreven?",
         opties=["sara woont in gent.", "Sara woont in gent.", "Sara woont in Gent.", "sara woont in Gent."], antwoord=2,
         uitleg="Een zin begint met een hoofdletter, en Sara en Gent zijn namen."),
]
