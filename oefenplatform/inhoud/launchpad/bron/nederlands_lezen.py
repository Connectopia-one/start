# -*- coding: utf-8 -*-
"""Launchpad Nederlands: korte woorden en zinnetjes lezen."""
from lp import K, I, W
import lpprent as P

TITEL = "Korte woorden lezen"
UITLEG_1 = "Korte woorden lezen en weten wat ze betekenen."
UITLEG_2 = "Kleine zinnen lezen en begrijpen."

DEEL_1 = [
    K("Wat kan je eten?", "een peer", ["een pen", "een pet", "een pop"], "Een peer is fruit.", None),
    K("Wat kan je aandoen?", "een jas", ["een tas", "een glas", "een vaas"], "Een jas trek je aan.", None),
    K("Welk woord is een dier?", "kip", ["kop", "kap", "kus"], "Een kip is een dier.", None),
    K("Welk woord is een kleur?", "rood", ["brood", "boot", "rok"], "Rood is een kleur.", None),
    K("Waar zit je op?", "een stoel", ["een stoep", "een steen", "een staart"], "Op een stoel zit je.", None),
    K("Wat groeit in de tuin?", "een roos", ["een rok", "een raam", "een riem"], "Een roos is een bloem.", None),
    K("Wat vliegt?", "een uil", ["een ui", "een uur", "een uier"], "Een uil is een vogel.", None),
    K("Waar woon je in?", "een huis", ["een muis", "een buis", "een luis"], "In een huis woon je.", None),
    K("Welk woord hoort niet bij het fruit?", "fiets", ["appel", "peer", "banaan"], "Appel, peer en banaan zijn fruit. Een fiets niet.", None),
    K("Welk woord hoort niet bij de dieren?", "boek", ["hond", "kat", "koe"], "Hond, kat en koe zijn dieren.", None),
    W("Een kat kan miauwen.", True, "Een kat zegt miauw."),
    W("Een boom kan lopen.", False, "Een boom staat stil en groeit."),
    W("Met een pen kan je schrijven.", True, "Een pen is om te schrijven."),
    W("Een vis woont in de lucht.", False, "Een vis woont in het water."),
    W("Je poetst je tanden met een tandenborstel.", True, "Tandenborstel en tandpasta."),
    W("Een ei is vierkant.", False, "Een ei is ovaal."),
    W("'Hek' en 'bek' verschillen maar in één letter.", True, "h-ek en b-ek."),
    W("'Mes' en 'vos' zijn hetzelfde woord.", False, "Het zijn twee andere woorden."),
    K("Welk woord lees je hier: k-oe", "koe", ["kou", "koek", "kei"], "k + oe = koe.", None),
    K("Welk woord lees je hier: b-oe-k", "boek", ["boer", "boom", "beek"], "b + oe + k = boek.", None),
]

DEEL_2 = [
    K("'De hond rent in de tuin.' Waar rent de hond?", "in de tuin", ["in het huis", "op straat", "in het bos"], "Er staat: in de tuin.", None),
    K("'Mia eet een rode appel.' Welke kleur heeft de appel?", "rood", ["groen", "geel", "blauw"], "Er staat: een rode appel.", None),
    K("'Tom heeft een bal.' Wie heeft een bal?", "Tom", ["Mia", "de hond", "mama"], "Tom heeft de bal.", None),
    K("'De kat slaapt op de bank.' Wat doet de kat?", "slapen", ["eten", "spelen", "lopen"], "Er staat: de kat slaapt.", None),
    K("'Papa bakt een taart.' Wat bakt papa?", "een taart", ["brood", "koekjes", "frietjes"], "Papa bakt een taart.", None),
    K("'Het regent. Sem neemt zijn paraplu.' Waarom neemt Sem een paraplu?", "omdat het regent", ["omdat het warm is", "omdat het sneeuwt", "omdat de zon schijnt"], "Bij regen neem je een paraplu.", None),
    K("'Lies is jarig. Ze wordt 7.' Hoe oud is Lies nu?", "7 jaar", ["6 jaar", "8 jaar", "5 jaar"], "Ze wordt 7.", None),
    K("'De vogel zit in de boom.' Waar zit de vogel?", "in de boom", ["op het dak", "in de kooi", "op de grond"], "Er staat: in de boom.", None),
    W("'De vis zwemt in de kom.' De vis zwemt in de zee.", False, "Er staat: in de kom."),
    W("'Ik heb een rode fiets.' Mijn fiets is rood.", True, "Een rode fiets is een fiets die rood is."),
    W("'Oma drinkt thee.' Oma drinkt koffie.", False, "Oma drinkt thee."),
    W("'Bram speelt met zijn zus.' Bram speelt niet alleen.", True, "Hij speelt samen met zijn zus."),
    W("'Het is nacht. De maan schijnt.' Het is donker buiten.", True, "'s Nachts is het donker."),
    W("'Ella heeft twee katten.' Ella heeft één kat.", False, "Ella heeft er twee."),
    K("Welke zin past bij een prent van een kind dat zwemt?", "Het kind zwemt in het zwembad.", ["Het kind slaapt in bed.", "Het kind eet een ijsje.", "Het kind leest een boek."], "Zwemmen doe je in het water.", None),
    K("Welk woord ontbreekt? 'De ... blaft.'", "hond", ["kat", "vis", "koe"], "Een hond blaft.", None),
    K("Welk woord ontbreekt? 'Ik ... een boek.'", "lees", ["eet", "slaap", "drink"], "Een boek lees je.", None),
    K("Welk woord ontbreekt? 'De zon is ...'", "geel", ["blauw", "paars", "zwart"], "De zon tekenen we geel.", None),
    W("'Ik ga naar school.' Dit is een zin.", True, "Er staat een hoofdletter vooraan en een punt achteraan."),
    W("'boom kat rood' is een goede zin.", False, "Losse woorden vormen nog geen zin."),
]

PRENT_1 = [
    K("Welk woord past bij de prent?", "kat", ["kar", "rat", "kast"], "Je ziet een kat.", None, prent=P.een("lezen-kat", "lp-kat")),
    K("Welk woord hoort bij dit dier?", "koe", ["kou", "koek", "kei"], "Je ziet een koe in de wei.", None, prent=P.een("lezen-koe", "koe-wei")),
    W("Op de prent zie je een muis.", False, "Je ziet een huis.", prent=P.een("lezen-huis", "huis")),
    K("Lees en kies: wat zie je?", "een bal", ["een bel", "een bol", "een bak"], "Je ziet een strandbal.", None, prent=P.een("lezen-bal", "lp-bal")),
]
PRENT_2 = [
    K("Welke zin past bij de prent?", "De hond slaapt.", ["De hond eet.", "De hond zwemt.", "De hond fietst."], "De hond ligt te slapen in zijn mand.", None, prent=P.een("lezen-hond-slaapt", "hond-slaapt-mand")),
    W("De vogel zingt.", True, "De vogel heeft zijn snavel open en zingt.", prent=P.een("lezen-vogel", "vogel-zingt")),
    K("Welke zin hoort bij deze prent?", "De kat zit.", ["De kat vliegt.", "De kat leest.", "De kat rijdt."], "De kat zit rechtop.", None, prent=P.een("lezen-kat-zit", "lp-kat")),
    W("De bus rijdt.", False, "Op de prent zie je een trein.", prent=P.een("lezen-trein", "trein")),
]
