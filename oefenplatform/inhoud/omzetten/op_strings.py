# -*- coding: utf-8 -*-
"""Past een omzetting enkel toe op de tekst in de string-literalen.

Nodig in de bundelbestanden: daar staat echte python tussen de tekst, en een
losse n, p of k is daar een variabele van het script. Gebruikt de tokenizer
van python zelf, en laat de korte sleutelwoorden van een blok met rust
("p" is een alinea, geen variabele).

Met `velden` gaat het nog een stap verder: dan wordt enkel de tekst bekeken
die bij een van die sleutels hoort, of dat nu `uitleg="..."` is of
`"uitleg": "..."` in een dict. Zo blijft een veld als `reken` (daar staat een
berekening in) of `antwoord` (dat wordt letterlijk vergeleken) gewone tekst.
"""
import io
import tokenize

# een string van hoogstens twee tekens is nooit lopende tekst
KORT = 2
VELDEN = {"vraag", "uitleg", "stelling", "opties", "tekst"}
RUIS = (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT,
        tokenize.DEDENT, tokenize.COMMENT)
DRIE = ('"""', "'''")


def _naam(s):
    """De inhoud van een string-literal als naam, zonder prefix en quotes.

    Let op: s.strip("rbu...") zou van "uitleg" ook de u afhalen."""
    return s[len(_kop(s)):].strip("\"'")


def _kop(s):
    i = 0
    while i < len(s) and s[i] not in "\"'":
        i += 1
    return s[:i]


def pas_toe(bron: str, functie, velden=None) -> str:
    """functie(tekst) -> tekst, op elke string-literal met inhoud."""
    stukken = []
    regels = bron.split("\n")

    def plek(rij, kol):
        return sum(len(r) + 1 for r in regels[: rij - 1]) + kol

    toks = [t for t in tokenize.generate_tokens(io.StringIO(bron).readline)
            if t.type not in RUIS]
    veld = None
    for i, tok in enumerate(toks):
        volgend = toks[i + 1] if i + 1 < len(toks) else None
        sleutel = (velden is not None and volgend is not None
                   and volgend.type == tokenize.OP
                   and volgend.string in ("=", ":"))
        if sleutel and tok.type == tokenize.NAME:
            veld = tok.string
            continue
        if sleutel and tok.type == tokenize.STRING:
            veld = _naam(tok.string)
            continue
        if tok.type != tokenize.STRING:
            continue
        if velden is not None and veld not in velden:
            continue
        kop = _kop(tok.string)
        if "b" in kop.lower() or tok.string.lstrip("rbuRBUfF").startswith(DRIE):
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

    for a, b, n in reversed(stukken):
        bron = bron[:a] + n + bron[b:]
    return bron
