# -*- coding: utf-8 -*-
"""Zet een r voor elke gewone string die een backslash gekregen heeft.

Gebruikt de tokenizer van python zelf, zodat een r-string niet verschuift.
"""
import io, sys, tokenize

for pad in sys.argv[1:]:
    bron = open(pad, encoding="utf-8").read()
    stuk = []          # (regel, kolom) van elke string die een r nodig heeft
    for tok in tokenize.generate_tokens(io.StringIO(bron).readline):
        if tok.type != tokenize.STRING:
            continue
        kop = tok.string[: tok.string.index(tok.string.lstrip("rbuRBUfF")[0])] if tok.string[0] not in "\"'" else ""
        if "r" in kop.lower() or "b" in kop.lower():
            continue
        if tok.string.startswith(('"""', "'''")) or tok.string.startswith(('f"""',)):
            continue          # een docstring laten we met rust
        if "\\" in tok.string:
            stuk.append((tok.start[0], tok.start[1]))
    if not stuk:
        continue
    regels = bron.split("\n")
    for rg, kol in sorted(stuk, reverse=True):
        r = regels[rg - 1]
        regels[rg - 1] = r[:kol] + "r" + r[kol:]
    open(pad, "w", encoding="utf-8").write("\n".join(regels))
    print(pad, len(stuk), "rauwe strings gezet")
