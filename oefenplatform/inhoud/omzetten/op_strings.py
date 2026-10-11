# -*- coding: utf-8 -*-
"""Past een omzetting enkel toe op de tekst in de string-literalen.

Nodig in de bundelbestanden: daar staat echte python tussen de tekst, en een
losse n, p of k is daar een variabele van het script. Gebruikt de tokenizer
van python zelf, en laat de korte sleutelwoorden van een blok met rust
("p" is een alinea, geen variabele).
"""
import io
import tokenize

# een string van hoogstens twee tekens is nooit lopende tekst
KORT = 2


def _kop(s):
    i = 0
    while i < len(s) and s[i] not in "\"'":
        i += 1
    return s[:i]


def pas_toe(bron: str, functie) -> str:
    """functie(tekst) -> tekst, toegepast op elke string-literal met inhoud."""
    stukken, laatste = [], (1, 0)
    regels = bron.split("\n")

    def plek(rij, kol):
        return sum(len(r) + 1 for r in regels[: rij - 1]) + kol

    for tok in tokenize.generate_tokens(io.StringIO(bron).readline):
        if tok.type != tokenize.STRING:
            continue
        kop = _kop(tok.string)
        if "b" in kop.lower() or tok.string.lstrip("rbuRBUfF").startswith(('"""', "'''")):
            continue
        aanhaling = tok.string[len(kop)]
        inhoud = tok.string[len(kop) + 1: -1]
        if len(inhoud) <= KORT:
            continue
        nieuw = functie(inhoud)
        if nieuw == inhoud:
            continue
        if "\\" in nieuw and "r" not in kop.lower():
            kop = "r" + kop
        a, b = plek(*tok.start), plek(*tok.end)
        stukken.append((a, b, kop + aanhaling + nieuw + aanhaling))

    for a, b, nieuw in reversed(stukken):
        bron = bron[:a] + nieuw + bron[b:]
    return bron
