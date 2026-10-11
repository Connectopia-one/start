# -*- coding: utf-8 -*-
"""Zoekt een los koppelteken of een punt die buiten een formule is blijven
staan waar eerst een echt teken (− of ×) stond.

Zoekt ook een formule die midden in een woord eindigt: \\(5 = s\\)torten hoort
\\(5\\) = storten te zijn. Dat gebeurt als een omzetscript de eerste letter van
het volgende woord als een symbool leest."""
import re, sys, pathlib
SPAN = re.compile(r"\\\(.*?\\\)|\{\{[^}]*\}\}|<[^>]*>", re.S)
VERDACHT = re.compile(r" - |\d ?- ?\d| · |\d ?· ?\d")
# een formule mag nooit vlak voor een letter eindigen
IN_WOORD = re.compile(r"\\\)(?=[^\W\d_])")
for pad in sys.argv[1:]:
    t = pathlib.Path(pad).read_text(encoding="utf-8")
    for nr, regel in enumerate(t.split("\n"), 1):
        kaal = SPAN.sub(" ", regel)
        if VERDACHT.search(kaal):
            print(f"{pad}:{nr}: {regel.strip()[:140]}")
        if IN_WOORD.search(regel):
            print(f"{pad}:{nr}: formule eindigt in een woord: "
                  f"{regel.strip()[:140]}")
