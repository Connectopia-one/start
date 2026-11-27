# -*- coding: utf-8 -*-
"""Launchpad WO: mijn lichaam, zintuigen en gezond leven."""
from lp import K, I, W
import lpprent as P

TITEL = "Mijn lichaam en gezond leven"
UITLEG_1 = "De delen van je lichaam en je vijf zintuigen."
UITLEG_2 = "Gezond eten, bewegen, slapen en proper blijven."

DEEL_1 = [
    K("Waarmee kijk je?", "met je ogen", ["met je oren", "met je neus", "met je tong"], "Je ogen zien.", None),
    K("Waarmee hoor je?", "met je oren", ["met je ogen", "met je handen", "met je mond"], "Je oren horen.", None),
    K("Waarmee ruik je?", "met je neus", ["met je oren", "met je voeten", "met je ogen"], "Je neus ruikt.", None),
    K("Waarmee proef je?", "met je tong", ["met je neus", "met je oren", "met je knie"], "Je tong proeft zoet, zout en zuur.", None),
    K("Waarmee voel je of iets zacht is?", "met je huid", ["met je oren", "met je haren", "met je tanden"], "Met je huid voel je, vooral met je vingers.", None),
    K("Waar zit je knie?", "in je been", ["in je arm", "in je hoofd", "in je buik"], "Je knie zit in het midden van je been.", None),
    K("Waar zit je elleboog?", "in je arm", ["in je been", "in je nek", "in je voet"], "Je elleboog zit in het midden van je arm.", None),
    K("Wat zit in je mond?", "je tanden", ["je tenen", "je ogen", "je nagels van je voeten"], "In je mond zitten tanden en je tong.", None),
    I("Hoeveel zintuigen heb je? ___", 5, "Zien, horen, ruiken, proeven en voelen.", 5),
    I("Hoeveel vingers heb je aan één hand? ___", 5, "Duim, wijsvinger, middelvinger, ringvinger en pink.", 5),
    I("Hoeveel tenen heb je samen aan je twee voeten? ___", 10, "5 + 5 = 10.", 10),
    W("Je hart klopt in je borst.", True, "Je hart zit in je borst en pompt je bloed rond."),
    W("Met je oren kan je zien.", False, "Met je oren hoor je. Zien doe je met je ogen."),
    W("Je duim is een vinger.", True, "De duim is je dikste vinger."),
    W("Je enkel zit in je arm.", False, "Je enkel zit tussen je been en je voet."),
    W("Je longen helpen je ademen.", True, "Lucht gaat je longen in en uit."),
    W("Je tong proeft of iets zoet is.", True, "Je tong proeft zoet, zuur en zout."),
    W("Je neus gebruik je om te praten.", False, "Praten doe je met je mond. Je neus ruikt."),
    K("Welk zintuig gebruik je als je naar muziek luistert?", "horen", ["ruiken", "proeven", "zien"], "Muziek hoor je met je oren.", None),
    K("Welk zintuig gebruik je bij een bloem die lekker ruikt?", "ruiken", ["horen", "proeven", "voelen"], "Een geur ruik je met je neus.", None),
]

DEEL_2 = [
    K("Wat is een gezond tussendoortje?", "een appel", ["chips", "een snoepje", "frisdrank"], "Fruit is gezond.", None),
    K("Wat drink je het best als je dorst hebt?", "water", ["frisdrank", "limonade", "chocolademelk"], "Water is het gezondst.", None),
    K("Wanneer was je je handen?", "voor het eten en na het toilet", ["enkel op zondag", "nooit", "enkel als ze zwart zijn"], "Zo blijven je handen proper en word je minder ziek.", None),
    K("Hoe vaak poets je je tanden?", "'s morgens en 's avonds", ["één keer per week", "nooit", "enkel als ze pijn doen"], "Twee keer per dag poetsen houdt je tanden gezond.", None),
    K("Waarom ga je op tijd slapen?", "zodat je uitgerust bent", ["zodat je honger krijgt", "zodat je ziek wordt", "omdat het moet van de tv"], "Slaap geeft je lichaam rust.", None),
    K("Wat is goed bewegen?", "buiten spelen", ["de hele dag tv kijken", "lang op de bank liggen", "de hele dag gamen"], "Lopen, fietsen en spelen houden je fit.", None),
    K("Welke groente is oranje?", "een wortel", ["een tomaat", "een komkommer", "een bloemkool"], "Een wortel is oranje.", None),
    K("Wat doe je als je hoest?", "je hand of elleboog voor je mond", ["recht naar iemand hoesten", "niets doen", "hard roepen"], "Zo geef je je bacteriën niet door.", None),
    W("Groenten en fruit zijn gezond.", True, "Ze zitten vol goede stoffen voor je lichaam."),
    W("Elke dag veel snoep eten is gezond.", False, "Snoep is lekker, maar niet gezond. Af en toe mag."),
    W("Na het spelen met zand was je best je handen.", True, "Zo komt er geen vuil in je mond."),
    W("Je hoeft je tanden niet te poetsen als je geen snoep eet.", False, "Je poetst altijd, 's morgens en 's avonds."),
    W("Bewegen maakt je spieren sterk.", True, "Door te bewegen worden je spieren sterker."),
    W("Kinderen hebben maar een paar uur slaap nodig.", False, "Kinderen hebben ongeveer 10 tot 12 uur slaap nodig."),
    W("Water drinken is goed voor je lichaam.", True, "Je lichaam heeft elke dag water nodig."),
    W("Je mag je tandenborstel delen met een vriendje.", False, "Je tandenborstel is enkel van jou."),
    I("Hoeveel keer per dag poets je je tanden? ___", 2, "'s Morgens en 's avonds.", 2),
    K("Wat eet je het best als ontbijt?", "een boterham met kaas", ["een zak chips", "een stuk taart", "een lolly"], "Brood geeft je energie voor de hele ochtend.", None),
    K("Wat neem je mee naar school als gezond drankje?", "een fles water", ["een blikje cola", "een energiedrankje", "een flesje limonade"], "Water is het beste drankje.", None),
    K("Waarom draag je een muts in de winter?", "om warm te blijven", ["om beter te horen", "om sneller te lopen", "om je haar te wassen"], "Een muts houdt je hoofd warm.", None),
]

PRENT_1 = [
    I("Hoeveel vingers zie je?", 5, "Duim, wijsvinger, middelvinger, ringvinger en pink: 5.", 5, prent=P.een("lichaam-hand", "lp-hand")),
    K("Wat doet het kind?", "tanden poetsen", ["haren kammen", "handen wassen", "eten"], "Het kind poetst zijn tanden voor de spiegel.", None, prent=P.een("lichaam-tanden", "lp-tanden-poetsen")),
    W("Hier worden handen gewassen met zeep.", True, "Handen wassen met zeep onder de kraan.", prent=P.een("lichaam-handen", "lp-handen-wassen")),
    K("Welk zintuig hoort bij dit lichaamsdeel?", "zien", ["horen", "ruiken", "proeven"], "Met je ogen zie je.", None, prent=P.een("lichaam-oog", "oog")),
]
PRENT_2 = [
    W("In het mandje zitten snoepjes.", False, "In het mandje zitten groenten: wortels, tomaten, broccoli en komkommer.", prent=P.een("lichaam-groenten", "lp-groenten")),
    K("Wat zie je op de prent?", "een kind dat slaapt", ["een kind dat eet", "een kind dat zwemt", "een kind dat fietst"], "Het kind slaapt in bed met zijn knuffel.", None, prent=P.een("lichaam-slapen", "lp-slapen")),
    I("Welk tussendoortje is gezond? Schrijf de letter.", ["C", "c"], "De appel (C) is gezond. Chips, een lolly en frisdrank niet.", None, prent="/examenvormen/ready/lichaam-tussendoortje.webp"),
    W("Het kind draagt een fietshelm.", True, "Een fietshelm beschermt je hoofd.", prent=P.een("lichaam-fietshelm", "lp-kind-fietst")),
]
