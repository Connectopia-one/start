# -*- coding: utf-8 -*-
"""Launchpad wiskunde: meten (lang, zwaar, vol) en geld tot 100 euro."""
from lp import K, I, W
import lpprent as P

TITEL = "Meten en geld"
UITLEG_1 = "Langer, zwaarder, meer: meten met meter, kilogram en liter."
UITLEG_2 = "Betalen met munten en briefjes in euro."

DEEL_1 = [
    K("Wat is het langst?", "een bus", ["een fiets", "een potlood", "een schoen"], "Een bus is veel langer dan een fiets.", None),
    K("Wat is het zwaarst?", "een olifant", ["een hond", "een kat", "een muis"], "Een olifant weegt het meest.", None),
    K("Waar kan het meeste water in?", "een bad", ["een glas", "een tas", "een emmer"], "In een bad past veel meer water dan in een emmer.", None),
    K("Waarmee meet je hoe lang iets is?", "een meetlat", ["een weegschaal", "een klok", "een maatbeker"], "Met een meetlat of lintmeter meet je lengte.", None),
    K("Waarmee meet je hoe zwaar iets is?", "een weegschaal", ["een meetlat", "een thermometer", "een klok"], "Een weegschaal toont het gewicht.", None),
    K("Wat meet je in liter?", "melk in een fles", ["de lengte van een tafel", "het gewicht van een appel", "hoe laat het is"], "Liter gebruik je voor wat je kan gieten.", None),
    K("Wat meet je in kilogram?", "een zak aardappelen", ["een fles water gieten", "de lengte van een gang", "de tijd van een film"], "Kilogram gaat over hoe zwaar iets is.", None),
    K("Hoe lang is een deur ongeveer?", "2 meter", ["2 centimeter", "20 meter", "200 meter"], "Een volwassene past er net onder: ongeveer 2 meter.", None),
    W("Een meter is langer dan een centimeter.", True, "In 1 meter passen 100 centimeter."),
    W("Een veer is zwaarder dan een steen.", False, "Een steen is zwaarder."),
    W("Een emmer water kan je meten in liter.", True, "Water giet je, dus meet je in liter."),
    W("Een meetlat gebruik je om te wegen.", False, "Een meetlat gebruik je om lengte te meten. Wegen doe je met een weegschaal."),
    W("Een pak melk is vaak 1 liter.", True, "De meeste pakken melk zijn 1 liter."),
    W("Een appel weegt ongeveer 10 kilogram.", False, "Een appel weegt veel minder: ongeveer 200 gram."),
    I("Een plank is 8 meter. Je zaagt er 3 meter af. Hoeveel meter blijft er over? ___", 5, "8 − 3 = 5.", 5),
    I("Een lint is 6 cm. Een ander lint is 9 cm. Hoeveel cm samen? ___", 15, "6 + 9 = 15.", 15),
    I("In een kan zit 4 liter. Je giet er 2 liter bij. Hoeveel liter nu? ___", 6, "4 + 2 = 6.", 6),
    I("Jan weegt 25 kg. Zijn zus weegt 30 kg. Hoeveel kg weegt zijn zus meer? ___", 5, "30 − 25 = 5.", 5),
    W("Hoe langer de streep, hoe meer centimeter.", True, "Een langere streep meet meer centimeter."),
    W("Een zwaar ding is altijd groot.", False, "Een kleine steen kan zwaarder zijn dan een groot kussen."),
]

DEEL_2 = [
    I("Een munt van 2 euro en een munt van 1 euro. Hoeveel euro is dat? ___", 3, "2 + 1 = 3.", 3),
    I("Een briefje van 10 euro en een briefje van 5 euro. Hoeveel euro? ___", 15, "10 + 5 = 15.", 15),
    I("Twee briefjes van 20 euro. Hoeveel euro? ___", 40, "20 + 20 = 40.", 40),
    I("Een briefje van 50 euro en een briefje van 10 euro. Hoeveel euro? ___", 60, "50 + 10 = 60.", 60),
    I("Een boek kost 8 euro. Je betaalt met 10 euro. Hoeveel krijg je terug? ___", 2, "10 − 8 = 2.", 2),
    I("Een bal kost 15 euro. Je betaalt met 20 euro. Hoeveel krijg je terug? ___", 5, "20 − 15 = 5.", 5),
    K("Welk geld is het meest waard?", "een briefje van 20 euro", ["een munt van 2 euro", "een briefje van 10 euro", "een briefje van 5 euro"], "20 euro is het meest.", None),
    K("Welke munt is er GEEN?", "een munt van 3 euro", ["een munt van 1 euro", "een munt van 2 euro", "een munt van 50 cent"], "Munten van 3 euro bestaan niet.", None),
    K("Hoe betaal je 7 euro met munten?", "2 + 2 + 2 + 1", ["2 + 2 + 2 + 2", "2 + 2 + 1", "1 + 1 + 2 + 2"], "2 + 2 + 2 + 1 = 7.", None),
    K("Hoe betaal je 25 euro?", "20 + 5", ["20 + 10", "10 + 10", "10 + 5 + 5"], "20 + 5 = 25.", None),
    W("Een briefje van 10 euro is evenveel als 5 munten van 2 euro.", True, "2 + 2 + 2 + 2 + 2 = 10."),
    W("Een munt van 1 euro is meer waard dan een briefje van 5 euro.", False, "5 euro is meer dan 1 euro."),
    W("Twee briefjes van 50 euro is samen 100 euro.", True, "50 + 50 = 100."),
    W("Met 10 euro kan je een fiets van 100 euro betalen.", False, "Je hebt dan 90 euro te weinig."),
    I("Een ijsje kost 3 euro. Hoeveel kosten 2 ijsjes? ___", 6, "3 + 3 = 6.", 6),
    I("Je hebt 12 euro. Je koopt een strip van 7 euro. Hoeveel hou je over? ___", 5, "12 − 7 = 5.", 5),
    K("Een appel kost 1 euro, een peer kost 2 euro. Hoeveel betaal je voor de twee samen?", "3 euro", ["2 euro", "4 euro", "1 euro"], "1 + 2 = 3.", None),
    K("Lisa heeft 5 euro. Wat kan ze kopen?", "een schrift van 4 euro", ["een spel van 9 euro", "een pet van 6 euro", "een bal van 12 euro"], "4 euro is minder dan 5 euro.", None),
    W("Op een kassabon staat hoeveel je betaald hebt.", True, "Op een kassabon zie je wat je kocht en wat het kostte."),
    W("Hoe duurder iets is, hoe minder geld je ervoor nodig hebt.", False, "Hoe duurder, hoe meer geld je nodig hebt."),
]

PRENT_1 = [
    K("Welk dier is het zwaarst?", "de olifant", ["de muis", "ze wegen evenveel"], "Een olifant weegt veel meer dan een muis.", None, prent=P.rij("meten-olifant-muis", ["lp-olifant", "lp-muis"])),
    K("Welk ding is in het echt het langst?", "de deur", ["het potlood", "het mes"], "Een deur is ongeveer 2 meter. Een potlood en een mes zijn veel korter.", None, prent=P.rij("meten-deur-potlood-mes", ["lp-deur", "lp-potlood", "lp-mes"])),
    W("Het glas is vol water.", False, "Het glas is leeg.", prent=P.een("meten-glas-leeg", "lp-glas-leeg")),
    I("Hoeveel euro is dit samen?", 5, "2 + 2 + 1 = 5.", 5, prent=P.munten("meten-geld-5", [2, 2, 1])),
]
PRENT_2 = [
    I("Hoeveel euro is dit samen?", 8, "5 + 2 + 1 = 8.", 8, prent=P.munten("meten-geld-8", [5, 2, 1])),
    K("Een boek kost 12 euro. Je betaalt met dit geld. Hoeveel krijg je terug?", "3 euro", ["2 euro", "5 euro", "13 euro"], "10 + 5 = 15. 15 − 12 = 3.", None, prent=P.munten("meten-geld-15", [10, 5])),
    W("Dit is evenveel als een briefje van 10 euro.", True, "5 munten van 2 euro: 10 euro.", prent=P.munten("meten-geld-10", [2, 2, 2, 2, 2])),
    K("Wat is het lichtst?", "de ballon", ["de olifant", "ze wegen evenveel"], "Een ballon is heel licht.", None, prent=P.rij("meten-ballon-olifant", ["lp-ballon", "lp-olifant"])),
]
