# -*- coding: utf-8 -*-
"""Zoekt een los koppelteken of een punt die buiten een formule is blijven
staan waar eerst een echt teken (− of ×) stond."""
import re, sys, pathlib
SPAN = re.compile(r"\\\(.*?\\\)|\{\{[^}]*\}\}|<[^>]*>", re.S)
VERDACHT = re.compile(r" - |\d ?- ?\d| · |\d ?· ?\d")
for pad in sys.argv[1:]:
    t = pathlib.Path(pad).read_text(encoding="utf-8")
    for nr, regel in enumerate(t.split("\n"), 1):
        kaal = SPAN.sub(" ", regel)
        if VERDACHT.search(kaal):
            print(f"{pad}:{nr}: {regel.strip()[:140]}")
