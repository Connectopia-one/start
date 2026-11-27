# -*- coding: utf-8 -*-
"""Launchpad Nederlands: spelling van klankzuivere woorden, ei/ij en au/ou, lange en korte klanken."""
from lp import K, I, W
import lpprent as P

TITEL = "Woorden goed schrijven"
UITLEG_1 = "Schrijf wat je hoort: maan, kip, boom."
UITLEG_2 = "Lastige klanken: ei of ij, au of ou."

DEEL_1 = [
    K("Hoe schrijf je het dier dat 'miauw' zegt?", "kat", ["kad", "kaat", "katt"], "k-a-t: je hoort een korte a.", None),
    K("Hoe schrijf je wat 's nachts aan de hemel staat?", "maan", ["man", "maam", "mahn"], "m-aa-n: een lange aa.", None),
    K("Hoe schrijf je het dier dat eieren legt?", "kip", ["kiep", "kipp", "kib"], "k-i-p: een korte i.", None),
    K("Hoe schrijf je wat in het bos groeit en blaadjes heeft?", "boom", ["bom", "boon", "bomm"], "b-oo-m: een lange oo.", None),
    K("Hoe schrijf je wat je aan je voet doet?", "sok", ["sook", "zok", "sokk"], "s-o-k: een korte o.", None),
    K("Hoe schrijf je waarmee je snijdt?", "mes", ["mees", "mez", "mess"], "m-e-s: een korte e.", None),
    K("Hoe schrijf je waarop je loopt?", "voet", ["voed", "foet", "vut"], "v-oe-t: aan het einde schrijf je t.", None),
    K("Hoe schrijf je het dier dat kaas lust?", "muis", ["mujs", "mous", "muus"], "m-ui-s.", None),
    W("'Pen' schrijf je met één e.", True, "p-e-n: een korte e."),
    W("'Raam' schrijf je met één a.", False, "r-aa-m: een lange aa, dus twee a's."),
    W("'Boom' schrijf je met twee o's.", True, "Een lange oo in het midden."),
    W("'Bus' schrijf je met uu.", False, "b-u-s: een korte u."),
    W("'Neus' schrijf je met eu.", True, "n-eu-s."),
    W("'Kip' schrijf je als 'kiep'.", False, "k-i-p: een korte i, dus één i."),
    K("Welk woord heeft een lange klank?", "maan", ["man", "pen", "kip"], "In maan hoor je een lange aa.", None),
    K("Welk woord heeft een korte klank?", "tak", ["taak", "boom", "roos"], "In tak hoor je een korte a.", None),
    K("Welke letter mis je? b_s (je rijdt ermee naar school)", "u", ["o", "a", "e"], "bus.", None),
    K("Welke letter mis je? p_p (je speelt ermee)", "o", ["a", "i", "u"], "pop.", None),
    K("Welke letters mis je? v__t (je loopt erop)", "oe", ["oo", "ee", "uu"], "voet.", None),
    K("Welke letters mis je? r__s (een bloem)", "oo", ["o", "oe", "ou"], "roos.", None),
]

DEEL_2 = [
    K("Hoe schrijf je wat een kip legt?", "ei", ["ij", "eij", "aai"], "Het woord ei schrijf je met ei.", None),
    K("Hoe schrijf je wat je eet als het warm is en dat koud is?", "ijs", ["eis", "ijss", "eijs"], "IJs schrijf je met ij.", None),
    K("Hoe schrijf je de dag na woensdag?", "donderdag", ["donderdach", "donnerdag", "donderdaag"], "don-der-dag.", None),
    K("Hoe schrijf je wat aan een vlieger hangt?", "touw", ["tauw", "tou", "toew"], "Touw schrijf je met ouw.", None),
    K("Hoe schrijf je het rijdende ding met vier wielen?", "auto", ["outo", "awto", "oto"], "Auto schrijf je met au.", None),
    K("Hoe schrijf je het mooie dier met een grote staart vol veren?", "pauw", ["pouw", "pau", "pouwe"], "Pauw schrijf je met auw.", None),
    K("Hoe schrijf je het gele, dure metaal?", "goud", ["gaud", "gout", "gouwd"], "Goud schrijf je met ou en een d.", None, prent=P.een("spel-goud", "lp-goud")),
    K("Hoe schrijf je waar een trein op rijdt?", "spoor", ["spor", "spoar", "sbour"], "sp-oo-r.", None),
    W("'Ei' schrijf je met ei.", True, "Het woord ei schrijf je met ei."),
    W("'IJs' schrijf je met ei.", False, "IJs schrijf je met ij."),
    W("'Trein' schrijf je met ei.", True, "Trein schrijf je met ei."),
    W("'Touw' schrijf je met au.", False, "Touw schrijf je met ou."),
    W("'Pauw' schrijf je met au.", True, "Pauw schrijf je met au."),
    W("'Fijn' schrijf je met ei.", False, "Fijn schrijf je met ij."),
    K("Welke letters mis je? tr__n (rijdt op het spoor)", "ei", ["ij", "ie", "ee"], "trein.", None),
    K("Welke letters mis je? r__st (wit en klein, je eet het)", "ij", ["ei", "ie", "ee"], "rijst.", None),
    K("Welke letters mis je? h__t (op je hoofd)", "oe", ["ou", "au", "ui"], "hoed.", None),
    K("Welke letters mis je? k__d (niet warm)", "ou", ["au", "oe", "ui"], "koud.", None),
    W("'Hond' schrijf je met een d, al hoor je een t.", True, "Bij honden hoor je de d: hond."),
    W("'Paard' schrijf je met een t aan het einde.", False, "Paard schrijf je met een d: paarden."),
]

PRENT_1 = [
    K("Hoe schrijf je wat je ziet?", "vis", ["vies", "fis", "viss"], "v-i-s: een korte i.", None, prent=P.een("spel-vis", "vis")),
    K("Welk woord is goed geschreven?", "pop", ["poop", "bop", "popp"], "p-o-p: een korte o.", None, prent=P.een("spel-pop", "lp-pop")),
    W("Het woord bij de prent schrijf je met twee o's.", True, "boom: een lange oo.", prent=P.een("spel-boom", "hoge-boom")),
    I("Welke letter mis je? t _ k", "a", "tak: een korte a.", None, prent=P.een("spel-tak", "lp-tak")),
]
PRENT_2 = [
    K("Kies het goede woord bij de prent.", "ijsje", ["eisje", "ijssje", "ijsie"], "IJsje schrijf je met ij.", None, prent=P.een("spel-ijsje", "ijsje")),
    W("Het woord bij de prent schrijf je met ij.", False, "Trein schrijf je met ei.", prent=P.een("spel-trein", "trein")),
    I("Welke letter mis je? r _ ng", "i", "ring.", None, prent=P.een("spel-ring", "ring")),
    K("Hoe schrijf je dit?", "huis", ["hius", "huiz", "hujs"], "h-ui-s.", None, prent=P.een("spel-huis", "huis")),
]
