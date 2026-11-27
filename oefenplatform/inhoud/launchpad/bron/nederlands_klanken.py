# -*- coding: utf-8 -*-
"""Launchpad Nederlands: letters en klanken (eerste klank, laatste klank, hakken en plakken)."""
from lp import K, I, W
import lpprent as P

TITEL = "Letters en klanken"
UITLEG_1 = "Welke klank hoor je eerst? Welke hoor je laatst?"
UITLEG_2 = "Woorden hakken in klanken en weer plakken."

DEEL_1 = [
    K("Met welke klank begint 'maan'?", "m", ["n", "a", "p"], "m-aa-n: eerst hoor je m.", None),
    K("Met welke klank begint 'kip'?", "k", ["p", "i", "t"], "k-i-p: eerst hoor je k.", None),
    K("Met welke klank begint 'sok'?", "s", ["k", "o", "z"], "s-o-k: eerst hoor je s.", None),
    K("Met welke klank begint 'raam'?", "r", ["m", "aa", "l"], "r-aa-m: eerst hoor je r.", None),
    K("Met welke klank eindigt 'pen'?", "n", ["p", "e", "m"], "p-e-n: laatst hoor je n.", None),
    K("Met welke klank eindigt 'tak'?", "k", ["t", "a", "p"], "t-a-k: laatst hoor je k.", None),
    K("Met welke klank eindigt 'bus'?", "s", ["b", "u", "t"], "b-u-s: laatst hoor je s.", None),
    K("Met welke klank eindigt 'jas'?", "s", ["j", "a", "z"], "j-a-s: laatst hoor je s.", None),
    K("Welk woord begint met de klank v?", "voet", ["boot", "noot", "hoed"], "v-oe-t begint met v.", None),
    K("Welk woord begint met de klank h?", "hek", ["bek", "nek", "mes"], "h-e-k begint met h.", None),
    K("Welke klank hoor je in het midden van 'pop'?", "o", ["p", "a", "oo"], "p-o-p: in het midden hoor je o.", None),
    K("Welke klank hoor je in het midden van 'muis'?", "ui", ["m", "s", "ij"], "m-ui-s: in het midden hoor je ui.", None),
    W("'Mes' begint met de klank m.", True, "m-e-s."),
    W("'Kat' eindigt met de klank k.", False, "k-a-t eindigt met t."),
    W("'Aap' en 'aan' beginnen met dezelfde klank.", True, "Allebei beginnen ze met aa."),
    W("'Bus' en 'pen' beginnen met dezelfde klank.", False, "Bus begint met b, pen met p."),
    W("'Neus' begint met de klank n.", True, "n-eu-s."),
    W("'Uil' eindigt met de klank u.", False, "ui-l eindigt met l."),
    K("Welke twee woorden rijmen?", "kat en mat", ["kat en kip", "kat en bus", "kat en pen"], "kat en mat eindigen allebei op -at."),
    K("Welk woord rijmt op 'pop'?", "top", ["pen", "pit", "pak"], "pop en top eindigen allebei op -op."),
]

DEEL_2 = [
    K("Hak 'roos' in klanken.", "r - oo - s", ["r - o - s", "ro - os", "r - oo - z"], "r-oo-s: drie klanken.", None),
    K("Hak 'kip' in klanken.", "k - i - p", ["ki - p", "k - ie - p", "k - i - b"], "k-i-p: drie klanken.", None),
    K("Hak 'vis' in klanken.", "v - i - s", ["v - ie - s", "vi - s", "f - i - s"], "v-i-s: drie klanken.", None),
    K("Plak de klanken: b - oo - m", "boom", ["bom", "boon", "room"], "b-oo-m wordt boom.", None),
    K("Plak de klanken: m - ui - s", "muis", ["mus", "huis", "mis"], "m-ui-s wordt muis.", None),
    K("Plak de klanken: s - o - k", "sok", ["zak", "sik", "kos"], "s-o-k wordt sok.", None),
    K("Plak de klanken: t - a - k", "tak", ["tas", "kat", "tik"], "t-a-k wordt tak.", None),
    K("Plak de klanken: p - au - w", "pauw", ["pauze", "pap", "touw"], "p-auw wordt pauw.", None),
    I("Hoeveel klanken hoor je in 'pen'? ___", 3, "p-e-n: 3 klanken.", 3),
    I("Hoeveel klanken hoor je in 'ei'? ___", 1, "ei is één klank.", 1),
    I("Hoeveel klanken hoor je in 'raam'? ___", 3, "r-aa-m: 3 klanken. aa is één klank.", 3),
    I("Hoeveel klanken hoor je in 'touw'? ___", 2, "t-ouw: 2 klanken.", 2),
    W("In 'maan' hoor je 3 klanken.", True, "m-aa-n."),
    W("In 'kat' hoor je 4 klanken.", False, "k-a-t: 3 klanken."),
    W("'aa' in 'raam' is één klank.", True, "Twee letters, maar je hoort één klank."),
    W("'sok' en 'kos' zijn hetzelfde woord.", False, "Dezelfde klanken, maar in een andere volgorde: ander woord."),
    W("'ui' in 'muis' is één klank.", True, "Twee letters, één klank."),
    W("'oe' is twee klanken.", False, "oe is één klank, zoals in voet."),
    K("Welke letters maken samen de klank 'oe'?", "o en e", ["o en o", "u en e", "o en u"], "o + e = oe, zoals in boek."),
    K("Welk woord heeft de klank 'eu'?", "neus", ["nees", "nies", "noes"], "n-eu-s.", None),
]

PRENT_1 = [
    K("Met welke klank begint dit dier?", "k", ["m", "p", "s"], "k-a-t: eerst hoor je k.", None, prent=P.een("klank-kat", "lp-kat")),
    I("Met welke klank eindigt het woord bij de prent?", "s", "m-e-s: laatst hoor je s.", None, prent=P.een("klank-mes", "lp-mes")),
    W("Het woord bij de prent begint met de klank v.", True, "v-i-s.", prent=P.een("klank-vis", "vis")),
    K("Welk woord rijmt op wat je ziet?", "dak", ["dik", "tas", "kip"], "tak en dak eindigen allebei op -ak.", None, prent=P.een("klank-tak", "lp-tak")),
]
PRENT_2 = [
    K("Hoeveel klanken hoor je in het woord bij de prent?", "3", ["2", "4", "1"], "p-o-p: 3 klanken.", None, prent=P.een("klank-pop", "lp-pop")),
    W("In het woord bij de prent hoor je de klank ui.", True, "m-ui-s.", prent=P.een("klank-muis", "lp-muis")),
    I("Plak de klanken: z - o - n. Welk woord is het?", "zon", "z-o-n wordt zon.", None, prent=P.een("klank-zon", "zon")),
    W("Het woord bij de prent eindigt met de klank p.", False, "b-oo-m eindigt met m.", prent=P.een("klank-boom", "hoge-boom")),
]
