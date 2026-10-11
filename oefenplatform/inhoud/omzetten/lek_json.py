import json, re, sys
for pad in sys.argv[1:]:
    data = json.load(open(pad, encoding="utf-8"))
    def loop(x, waar=""):
        if isinstance(x, str):
            kaal = re.sub(r"\\\(.*?\\\)", "", x)
            if "\\" in kaal or re.search(r"[°×−≤≥∈∩∪∅²³π]", kaal):
                print(f"  LEK {waar}: {x[:150]}")
        elif isinstance(x, dict):
            for k, v in x.items(): loop(v, waar)
        elif isinstance(x, list):
            for v in x: loop(v, waar)
    for h in data["hoofdstukken"]:
        loop(h, h["titel"])
    print(f"{pad} nagekeken")
