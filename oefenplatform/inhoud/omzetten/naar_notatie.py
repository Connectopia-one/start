# -*- coding: utf-8 -*-
"""Zet de getallen en tekens in de vragen om naar wiskundige notatie.

Werkt op de bronbestanden van het oefenplatform: enkel de tekst van vraag=,
uitleg= en opties= wordt aangeraakt. antwoord= blijft eraf, want daar typt een
kind zijn antwoord in, en de tekeningen tussen {{ }} blijven ook staan.

    python3 -I notatie.py <bestand.py> ...

Het script knipt de tekst in stukjes (getal, teken, haakje, woord) en zoekt de
langste rij die een som vormt. Een woord mag in een som staan — "lengte · breedte"
hoort als geheel in de notatie — maar nooit aan het begin of het einde, want dan
is het gewone tekst. Lees het verschil achteraf na: waar formule en zin door
elkaar lopen, raadt het script.
"""
import ast, io, re, sys, tokenize

VELDEN = {"vraag", "uitleg", "stelling", "opties", "tekst"}

TEKENS = [
    ("⇔", r"\Leftrightarrow"), ("⇒", r"\Rightarrow"),
    ("×", r"\cdot"), ("·", "\ue001"),
    ("≈", r"\approx"), ("≠", r"\neq"),
    ("≤", r"\leq"), ("≥", r"\geq"),
    ("∞", r"\infty"), ("∅", r"\emptyset"),
    ("∉", r"\notin"), ("∈", r"\in"),
    ("∪", r"\cup"), ("∩", r"\cap"),
    ("⊂", r"\subset"), ("π", r"\pi"),
    ("√", r"\sqrt"), ("−", "\ue002"),
    ("ℕ", r"\mathbb{N}"), ("ℤ", r"\mathbb{Z}"),
    ("ℚ", r"\mathbb{Q}"), ("ℝ", r"\mathbb{R}"),
    ("⊄", r"\not\subset"), ("⊃", r"\supset"),
    (" \\ ", r" \setminus "),      # het verschil van twee verzamelingen
    ("…", r"\ldots"),             # de puntjes in "4,8 × … = 480" horen bij de som
]
HOOG = {"⁻": "-", "⁺": "+", "ⁿ": "n",
        "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
        "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9"}

WERKWOORD = r"\\not\\subset|\\(?:cdot|leq|geq|approx|neq|Rightarrow|Leftrightarrow|notin|in|cup|cap|subset|setminus)"
ALLEEN = r"\\left\|[^|]*\\right\||\\tfrac\{[^{}]*\}\{[^{}]*\}|\\sqrt\{[^{}]*\}|\\(?:infty|emptyset|pi|ldots)"      # staat op zichzelf, is geen bewerking
BUNDELS = "--bundels" in sys.argv    # leerbundels en oefenbundels: html met tags
SETS = "--sets" in sys.argv          # voor het thema Verzamelingen
TOKEN = re.compile(
    (r"(?P<verz>(?<![\\\w^}])\{ ?\d[\d, ]*\}|\\mathbb\{[A-Z]\})|(?P<naam>[A-Z](?![a-zA-Z]))|" if SETS else "")
    + r"(?P<num>\d+(?:\{,\}\d+)?(?:\\,\d{3})*(?:\\,\\%)?(?:\^\{[^{}]*\})?(?:\\text\{[^{}]*\})?)"
    r"|(?P<sym>" + WERKWOORD + r"|[-+=:<>\ue000\ue001\ue002])"
    r"|(?P<entiteit>&[a-z]+;)"
    r"|(?P<los>" + ALLEEN + r")"
    r"|(?P<haak>[()])"
    r"|(?P<exp>\^\{[^{}]*\})"
    r"|(?P<var>(?<![^\W\d_])[abcdknpqrtxyz]{1,2}(?![^\W\d_])(?:\^\{[^{}]*\})?)"
    r"|(?P<woord>[^\W\d_]+(?:\^\{[^{}]*\})?)"
    r"|(?P<ruimte> )"
    r"|(?P<rest>.)", re.S)

EENHEDEN = {"m", "cm", "dm", "mm", "km", "l", "dl", "cl", "ml", "g", "kg", "mg",
            "ton", "s", "min", "u", "h", "uur", "euro", "keer", "graden", "procent"}

NUMMER = re.compile(r"(?<![a-zA-Z])(?:deel|stap|hoofdstuk|vraag|reeks|bladzijde|nummer|oefening)$", re.I)
EENHEID = re.compile(r"(?<![A-Za-z])(cm|dm|mm|km|m|dl|cl|ml|l)([²³])")


def tokens(tekst):
    rij = [(m.lastgroup, m.group(0)) for m in TOKEN.finditer(tekst)]
    return tekens_aan_getal(rij)


def tekens_aan_getal(rij):
    """Een min of plus die aan een getal vastzit en niet achter een getal komt,
    is een voorteken en hoort bij dat getal: in "-3 \u00b0C" is het geen bewerking."""
    uit = []
    for soort, stuk in rij:
        # een exponent hoort bij wat ervoor staat: (x + 4)^{2}, x^{2}
        if soort == "exp" and uit and uit[-1][0] in ("num", "var", "haak", "verz", "naam"):
            uit[-1] = (uit[-1][0], uit[-1][1] + stuk)
            continue
        # een letter tegen een getal is een factor: 8x, 2ab
        if soort == "var" and uit and uit[-1][0] == "num":
            uit[-1] = ("num", uit[-1][1] + stuk)
            continue
        vorige = next((s for s, _ in reversed(uit) if s != "ruimte"), None)
        if (uit and uit[-1][1] in "-+\ue000" and uit[-1][0] == "sym" and soort in ("num", "var")
                and vorige == "sym"):
            eerder = [(s, k) for s, k in uit[:-1] if s != "ruimte"]
            achter_getal = bool(eerder) and (eerder[-1][0] in ("num", "var", "verz", "naam")
                                             or eerder[-1][1] == ")")
            if not achter_getal:
                uit[-1] = ("num", uit[-1][1] + stuk)
                continue
        uit.append((soort, stuk))
    return uit


def _buren(rij, i):
    """De twee buren van stukje i, met spaties, haakjes en tekens overgeslagen.
    Een woord dat via een teken aan een ander woord hangt, hoort bij dezelfde
    formule: in "(lengte + breedte)" hangt breedte aan lengte."""
    uit = []
    for stap in (-1, 1):
        j = i + stap
        while 0 <= j < len(rij) and rij[j][0] in ("ruimte", "haak"):
            j += stap
        uit.append(rij[j][1] if 0 <= j < len(rij) else None)
        if 0 <= j < len(rij) and rij[j][0] == "sym":
            while 0 <= j < len(rij) and rij[j][0] in ("ruimte", "haak", "sym"):
                j += stap
            uit.append(j if 0 <= j < len(rij) and rij[j][0] == "woord" else None)
    return uit


# Binnen een formule wordt een teken zijn latex, buiten een formule weer
# gewoon het teken dat in de tekst stond.
SENTINEL = {"\ue000": ("-", "&minus;"), "\ue001": (r"\cdot", "·"), "\ue002": ("-", "−")}


def binnenin(stuk: str) -> str:
    for teken, (latex, _) in SENTINEL.items():
        stuk = stuk.replace(teken, latex)
    return stuk


def buiten(stuk: str) -> str:
    for teken, (_, gewoon) in SENTINEL.items():
        if teken != "\ue000":      # die zet zet_om zelf terug naar &minus;
            stuk = stuk.replace(teken, gewoon)
    # Een komma in een getal werd {,} voor KaTeX. Bleef dat getal buiten een
    # formule staan, dan hoort de komma weer een gewone komma te zijn, anders
    # staan de accolades zichtbaar op de pagina.
    return stuk.replace("{,}", ",")


# Een woord dat alleen een zin aan elkaar praat, hoort nooit in een formule:
# "Bij × 1000" is geen "\text{Bij} \cdot 1000".
STOPWOORDEN = {
    "bij", "is", "of", "en", "van", "dus", "de", "het", "een", "in", "op", "naar",
    "met", "als", "dat", "zo", "nog", "ook", "maar", "want", "wordt", "worden",
    "staat", "staan", "per", "tot", "om", "aan", "voor", "na", "over", "dan",
    "je", "we", "er", "al", "dit", "die", "deze", "zijn", "heeft", "hebben",
    "doe", "doet", "krijg", "krijgt", "geeft", "geven", "maak", "maakt", "ken",
    "kent", "tel", "telt", "zet", "zie", "ziet", "reken", "rekent", "schrijf",
}


def klopt(rij) -> bool:
    """Is deze rij stukjes een som die je in haar geheel in notatie mag zetten?"""
    if not rij or rij[0][0] == "ruimte" or rij[-1][0] in ("ruimte", "sym"):
        return False
    if rij[0][0] == "sym" and rij[0][1] not in ("-", "\ue000", "\ue002"):
        return False
    soorten = [s for s, _ in rij]
    # twee getallen of namen na elkaar zonder teken ertussen is geen som maar
    # een zin ("\\text{van} 3"); er hoort een teken tussen te staan
    kaal = [s for s in soorten if s not in ("ruimte", "haak")]
    for eerste, tweede in zip(kaal, kaal[1:]):
        if eerste != "sym" and tweede != "sym":
            return False
    kern = {"num", "los", "var", "verz", "naam"} if SETS else {"num", "los", "var"}
    # Haakjes alleen maken nog geen formule: "kilo (k)" is een afkorting.
    if "sym" not in soorten and not ("haak" in soorten and "num" in soorten):
        return False
    if not (kern & set(soorten)):
        return False
    diep = 0
    for _, stuk in rij:
        diep += stuk.startswith("(") - stuk.startswith(")")
        if diep < 0:
            return False
    if diep:
        return False
    woorden = [i for i, s in enumerate(soorten) if s == "woord"]
    goed = set()
    gegroeid = True
    while gegroeid:
        gegroeid = False
        for i in woorden:
            if i in goed:
                continue
            if any(b == "\\cdot" or (b is not None and b in goed) for b in _buren(rij, i)):
                goed.add(i)
                gegroeid = True
    for i, soort in enumerate(soorten):
        if soort != "woord":
            continue
        if rij[i][1].lower() in EENHEDEN or rij[i][1].lower() in STOPWOORDEN:
            return False
        # een woord hoort enkel in een som als het met spaties naast een
        # bewerkingsteken staat: "lengte \cdot breedte" wel, "20 cm" niet
        links = soorten[i - 1] if i else None
        rechts = soorten[i + 1] if i + 1 < len(soorten) else None
        if links not in (None, "ruimte", "haak") or rechts not in (None, "ruimte", "haak"):
            return False
        if i not in goed:
            return False
    return True


def tekst_van(rij) -> str:
    def een(soort, stuk):
        if soort == "verz" and stuk.startswith("{"):
            return "\\{" + stuk[1:-1] + "\\}"
        if soort != "woord":
            return stuk
        letters, _, exponent = stuk.partition("^")
        return r"\text{" + letters + "}" + (("^" + exponent) if exponent else "")
    return binnenin("".join(een(soort, stuk) for soort, stuk in rij))


def sommen(tekst):
    rij, uit, i = tokens(tekst), [], 0
    while i < len(rij):
        if rij[i][0] in ("num", "sym", "los", "haak", "woord", "verz", "naam", "var"):
            einde = i
            while einde < len(rij) and rij[einde][0] in (
                    "num", "sym", "los", "haak", "woord", "ruimte", "verz", "naam", "var"):
                einde += 1
            # het langste stuk dat een som is, van links naar rechts gezocht
            keus = None
            for a in range(i, einde):
                for b in range(einde, a, -1):
                    if klopt(rij[a:b]):
                        keus = (a, b)
                        break
                if keus:
                    break
            if keus:
                a, b = keus
                voor = "".join(s for _, s in rij[:a]).rstrip()
                if NUMMER.search(voor.split(" ")[-1] if voor else ""):
                    uit.append(rij[i][1]); i += 1; continue
                uit.append("".join(s for _, s in rij[i:a]))
                uit.append("\\(" + tekst_van(rij[a:b]) + "\\)")
                i = b
                continue
        uit.append(rij[i][1]); i += 1
    return "".join(uit)


PLUKJE = r"(?<![\w%\\{])(?<!\d\.)(?:\\left\|[^|]*\\right\||\\tfrac\{[^{}]*\}\{[^{}]*\}|[-\ue000\ue002]?\d+(?:\{,\}\d+)?(?:\\,\d{3})*(?:\\,\\%)?(?:\^\{[^{}]*\})?(?:\\text\{[^{}]*\})?)(?![\w}]|\.\d)"


def los(tekst):
    def verz(m):
        return "\\(\\{" + m.group(0)[1:-1] + "\\}\\)"

    def een(m):
        voor = tekst[:m.start()].rstrip()
        if NUMMER.search(voor.split(" ")[-1] if voor else ""):
            return m.group(0)
        return "\\(" + binnenin(m.group(0)) + "\\)"
    if SETS:
        tekst = re.sub(r"(?<![\\\w^}])\{ ?\d[\d, ]*\}", verz, tekst)
        tekst = beschermd(tekst, lambda d: re.sub(PLUKJE, een, d))
        # een losse hoofdletter is de naam van een verzameling, ook in een zin
        return beschermd(tekst, lambda d: re.sub(
            r"(?<![\w\\{])[A-Z](?![\w}])", lambda m: "\\(" + m.group(0) + "\\)", d))
    return re.sub(PLUKJE, een, tekst)


_TEKEN_RAND = re.compile(
    r"(?:[-+=:<>]|\\(?:cdot|leq|geq|approx|neq|in|cup|cap|subset|setminus|notin))$"
    r"|^(?:[-+=:<>]|\\(?:cdot|leq|geq|approx|neq|in|cup|cap|subset|setminus|notin))")

LEKKEN = re.compile(
    r"\\(?:mathbb\{[A-Z]\}|tfrac\{[^{}]*\}\{[^{}]*\}|sqrt\{[^{}]*\}|not\\subset"
    r"|cdot|leq|geq|approx|neq|Rightarrow|Leftrightarrow|notin|in|cup|cap|subset"
    r"|supset|setminus|infty|emptyset|pi|ldots)(?![a-zA-Z])")


def plak(m):
    """Twee stukken notatie die enkel een spatie tussen zich hebben, horen samen:
    "\(2{,}5\) \(\text{m}^{2}\)" leest als "2,5 m²". Staat er een bewerkingsteken
    naast, dan zorgt KaTeX zelf voor de ruimte."""
    links, rechts = m.group(1), m.group(2)
    # "klas B 16" is geen formule: een losse hoofdletter blijft op zichzelf
    if re.fullmatch(r"\\\([A-Z]", links):
        return m.group(0)
    bewerking = _TEKEN_RAND.search(links) or _TEKEN_RAND.match(rechts)
    return links + ("" if bewerking else r"\,") + rechts


TERUG = {latex: teken for teken, latex in TEKENS if latex.startswith("\\")}


def terug(m):
    """Een teken dat buiten een formule is blijven staan, wordt weer het gewone
    teken uit de tekst. Zo staat er nooit \\cdot als letters op de pagina."""
    return TERUG.get(m.group(0), r"\(" + m.group(0) + r"\)")


def wrap(tekst: str) -> str:
    for teken, latex in TEKENS:
        tekst = tekst.replace(teken, latex)
    tekst = EENHEID.sub(lambda m: r"\(\text{" + m.group(1) + "}^{" + HOOG[m.group(2)] + r"}\)", tekst)
    # een rij bovengeschreven tekens wordt één exponent: 10¹² → 10^{12}, 2⁻² → 2^{-2}
    tekst = re.sub("[" + "".join(HOOG) + "]+",
                   lambda m: "^{" + "".join(HOOG[c] for c in m.group(0)) + "}", tekst)
    tekst = re.sub("(\\d+)[ \u00a0]?\u00b0C(?![a-z])",
                   lambda m: m.group(1) + r"^{\circ}\text{C}", tekst)
    tekst = re.sub("(\\d+)[ \u00a0]?\u00b0", lambda m: m.group(1) + r"^{\circ}", tekst)
    tekst = re.sub(r"(?<=\d),(?=\d)", "{,}", tekst)
    tekst = re.sub(r"(\d(?:\{,\}\d+)?)[ \u00a0]?%", r"\1\\,\\%", tekst)
    # een breuk krijgt een echte streep: 3/4 wordt \tfrac{3}{4}
    tekst = re.sub(r"(?<![\w/])(\d+)/(\d+)(?![\w/])", r"\\tfrac{\1}{\2}", tekst)
    tekst = re.sub(r"\|(-?\d+)\|", r"\\left|\1\\right|", tekst)
    tekst = re.sub(r"\\sqrt\(([^()]*)\)", r"\\sqrt{\1}", tekst)
    tekst = re.sub(r"\\sqrt(\d+)", r"\\sqrt{\1}", tekst)
    # duizendtallen: 12 000 000 hoort als één getal bij elkaar
    while re.search(r"\d[ \u00a0]\d{3}(?!\d)", tekst):
        tekst = re.sub(r"(\d)[ \u00a0](\d{3})(?!\d)", r"\1\\,\2", tekst)
    # Een dubbelpunt is enkel een deling als er een spatie voor staat. In
    # "samen 180 graden: 180 - 65" hoort hij bij de zin, niet bij de som.
    tekst = re.sub(r"(?<! ):", "\x00", tekst)
    tekst = sommen(tekst)
    tekst = beschermd(tekst, los)
    # Wat er aan notatie buiten de haakjes overblijft (een teken dat alleen in
    # een zin staat), krijgt zijn eigen haakjes.
    tekst = beschermd(tekst, lambda d: LEKKEN.sub(terug, d))
    # een exponent die buiten de notatie bleef staan (ZZ90^{\circ}) trekt het
    # getal ervoor mee naar binnen
    tekst = beschermd(tekst, lambda d: re.sub(
        r"(\d+)(\^\{[^{}]*\})", lambda m: r"\(" + m.group(1) + m.group(2) + r"\)", d))
    vorige = None
    while vorige != tekst:
        vorige = tekst
        tekst = re.sub(r"(\S*?)\\\) \\\((\S*)", plak, tekst)
    tekst = beschermd(tekst, buiten)
    return tekst.replace("\x00", ":")


def beschermd(tekst, werk):
    """Doet `werk` op alles behalve de tekeningen en de notatie die er al staat."""
    delen = re.split(r"(\{\{[^}]*\}\}|<[a-zA-Z/][^>]*>|\\\(.*?\\\))", tekst)
    for i in range(0, len(delen), 2):
        delen[i] = werk(delen[i])
    return "".join(delen)


def zet_om(tekst: str) -> str:
    if not BUNDELS:
        return beschermd(tekst, wrap)
    # In een bundel staat html. Binnen een formule mag < gewoon < zijn (bundel.py
    # zet het vlak voor het schrijven weer om), buiten een formule niet.
    tekst = beschermd(tekst, lambda d: d.replace("&lt;", "<").replace("&gt;", ">")
                                        .replace("&minus;", "\ue000"))
    tekst = beschermd(tekst, wrap)
    return beschermd(tekst, lambda d: d.replace("<", "&lt;").replace(">", "&gt;")
                                       .replace("\ue000", "&minus;"))


OVERSLAAN = re.compile(r"""^[rbfu]*["']\d+(?:px|%|em|rem|pt)["']$"""
                       r"""|^[rbfu]*["']#[0-9a-fA-F]{3,8}["']$|<svg|viewBox|<path""")
PROZA_CALLS = {"dict", "tabel", "mk", "invul", "won", "kleur", "sleep"}
# Argumenten die gewone tekst moeten blijven, per aanroep. Het antwoord van
# een invulvraag typt een kind in, en de kaartjes van een sleepvraag staan als
# platte tekst op de getallenlijn (components/Figuren.tsx tekent ze zonder
# <Formule>). De vorm van een kleurvraag ("cirkel") is een naam, geen tekst.
ANTWOORD_ARG = {"invul": {1}, "sleep": {1, 2}, "kleur": {1}}
# Velden die gewone tekst blijven. De titel van een bundel moet letterlijk
# gelijk blijven aan de titel van het hoofdstuk (daar hangt de koppeling
# aan vast), een kop is een titel en geen formule, en breed= is een
# css-breedte.
SLA_VELD_OVER = {"titel", "kop", "onder", "vak", "niveau", "breed", "label",
                 "richting", "vorm", "sleutel", "naam", "slug", "kleur"}   # de tekst van een bundel staat in dict(...) en tabel(...)


def te_zetten(bron: str):
    """De tekstjes die omgezet mogen worden, als tokens.

    Gewone bestanden: alles achter vraag=, uitleg= of opties=. Bundels: alle
    tekst, behalve wat in een functieaanroep of tussen blokhaken staat (de
    getallen van een tekening en de sleutel van een bundel blijven zo heel).
    """
    veld, wacht_is, vorige, stapel, uit = None, None, None, [], []
    for tok in tokenize.generate_tokens(io.StringIO(bron).readline):
        if tok.type in (tokenize.NL, tokenize.NEWLINE, tokenize.INDENT,
                        tokenize.DEDENT, tokenize.COMMENT):
            continue
        if tok.type == tokenize.OP and tok.string in "([":
            aanroep = vorige is not None and (
                vorige.type == tokenize.NAME or vorige.string in (")", "]"))
            soort = ("aanroep" if tok.string == "(" else "index") if aanroep else "rij"
            stapel.append([soort, vorige.string if vorige else "", 0, ""])
        elif tok.type == tokenize.OP and tok.string in ")]":
            if stapel:
                stapel.pop()
        elif tok.type == tokenize.OP and tok.string == "," and stapel:
            stapel[-1][2] += 1
            stapel[-1][3] = ""
        if tok.type == tokenize.NAME:
            wacht_is = tok.string
        elif tok.type == tokenize.OP and tok.string == "=" and wacht_is:
            veld, wacht_is = wacht_is, None
            if stapel:
                stapel[-1][3] = veld
        elif tok.type == tokenize.STRING:
            if vorige is None or vorige.type in (tokenize.NEWLINE, tokenize.NL,
                                                 tokenize.INDENT, tokenize.DEDENT):
                vorige = tok           # een docstring is geen tekst van een bundel
                continue
            if BUNDELS:
                binnen = [s for s, naam, _, _ in stapel
                          if s == "index" or (s == "aanroep" and naam not in PROZA_CALLS)]
                antwoord = any(soort == "aanroep" and nummer in ANTWOORD_ARG.get(naam, ())
                               for soort, naam, nummer, _ in stapel)
                sleutel = next((f[3] for f in reversed(stapel) if f[3]), None)
                if (not binnen and not antwoord and sleutel not in SLA_VELD_OVER
                        and not OVERSLAAN.search(tok.string)):
                    uit.append(tok)
            elif veld in VELDEN:
                uit.append(tok)
        if tok.type != tokenize.NAME:
            wacht_is = None
        vorige = tok
    return uit


def bestand(pad: str) -> None:
    bron = open(pad, encoding="utf-8").read()
    veranderd = te_zetten(bron)

    regels = bron.splitlines(keepends=True)
    begin = [0]
    for r in regels:
        begin.append(begin[-1] + len(r))
    for tok in reversed(veranderd):
        a = begin[tok.start[0] - 1] + tok.start[1]
        b = begin[tok.end[0] - 1] + tok.end[1]
        ruw = bron[a:b]
        prefix = ruw[:len(ruw) - len(ruw.lstrip("rRbBfFuU"))]
        if "f" in prefix.lower() or "b" in prefix.lower():
            continue
        quote = '"""' if ruw[len(prefix):].startswith('"""') else ruw[len(prefix)]
        nieuw = zet_om(ast.literal_eval(ruw))
        if quote in nieuw or nieuw.endswith("\\"):
            nieuw, p = nieuw.replace("\\", "\\\\").replace(quote, "\\" + quote), ""
        else:
            p = "r" if "\\" in nieuw else ""
        bron = bron[:a] + p + quote + nieuw + quote + bron[b:]
    open(pad, "w", encoding="utf-8").write(bron)
    print(f"{pad}: {len(veranderd)} teksten bekeken")


for pad in [a for a in sys.argv[1:] if not a.startswith("--")]:
    bestand(pad)
