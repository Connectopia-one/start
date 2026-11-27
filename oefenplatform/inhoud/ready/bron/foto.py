# -*- coding: utf-8 -*-
"""Gedetailleerde prenten voor Ready (Kim 27/11: de eenvoudige tekeningen van dieren en
voorwerpen hadden "veel te weinig detail"). Kim maakte 65 prenten met een beeldgenerator
(eigen beeld van Connectopia). De originelen staan in /mnt/project-files/ready-prenten-26-11/gegenereerd/
en op Kims pc in E:\\Afbeeldingen lesmateriaal\\Algemeen\\Ready-prenten.

Hier krijgen ze het zachtste filter (Kims keuze: kleuren minder fel, een tikje lichter),
worden ze verkleind tot webp, en zetten we zelf de pijlen, letters en prijzen erop.
prent.bewaar() roept maak() op voor elke naam in FOTO, zodat de vragen niets hoeven te veranderen."""
import pathlib
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

GEN = pathlib.Path("/mnt/project-files/ready-prenten-26-11/gegenereerd")
ORANJE, DARK = (196, 98, 45), (47, 74, 34)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
BRONREGEL = "eigen beeld Connectopia (Kim, met een beeldgenerator, 27/11/2026)"


def zacht(im):
    """Kims gekozen filter: kleur 65 procent, 15 procent wit erover."""
    im = ImageEnhance.Color(im.convert("RGB")).enhance(0.65)
    return Image.blend(im, Image.new("RGB", im.size, "white"), 0.15)


def laad(bestand, maat=None):
    im = zacht(Image.open(GEN / f"{bestand}.png"))
    if maat: im = im.resize((maat, maat), Image.LANCZOS)
    return im


def rand(im, m):
    """Witte rand rond de prent, zodat een pijl van buitenaf kan komen."""
    n = Image.new("RGB", (im.width + 2 * m, im.height + 2 * m), "white"); n.paste(im, (m, m)); return n


def pijl(im, van, naar, dik=22):
    """Oranje pijl met witte rand, met de punt op 'naar'."""
    d = ImageDraw.Draw(im)
    import math
    (x0, y0), (x1, y1) = van, naar
    a = math.atan2(y1 - y0, x1 - x0); L = dik * 2.6
    bx, by = x1 - L * math.cos(a), y1 - L * math.sin(a)
    kop = [(x1, y1), (bx + dik * 1.4 * math.sin(a), by - dik * 1.4 * math.cos(a)), (bx - dik * 1.4 * math.sin(a), by + dik * 1.4 * math.cos(a))]
    d.line([(x0, y0), (bx, by)], fill="white", width=dik + 14)
    d.polygon(kop, fill="white", outline="white", width=10)
    d.line([(x0, y0), (bx, by)], fill=ORANJE, width=dik)
    d.polygon(kop, fill=ORANJE)
    return im


def letter(d, x, y, s, groot=90, kleur=ORANJE):
    f = ImageFont.truetype(FONT, groot)
    d.text((x, y), s, font=f, fill=kleur, anchor="mm")


def rij(namen, onder=None, maat=420, tussen=30):
    """Prenten naast elkaar, met eronder een letter of prijs."""
    h = maat + (130 if onder else 0)
    im = Image.new("RGB", (len(namen) * maat + (len(namen) + 1) * tussen, h), "white")
    d = ImageDraw.Draw(im)
    for i, n in enumerate(namen):
        x = tussen + i * (maat + tussen)
        im.paste(laad(n, maat), (x, 0))
        if onder: letter(d, x + maat // 2, maat + 65, onder[i], 80 if len(onder[i]) <= 1 else 64, ORANJE if len(onder[i]) <= 1 else DARK)
    return im


def strip(namen, maat=420, tussen=30):
    """Verhaal in prentjes: elk in een kader, letter eronder."""
    im = Image.new("RGB", (len(namen) * maat + (len(namen) + 1) * tussen, maat + 130), "white")
    d = ImageDraw.Draw(im)
    for i, n in enumerate(namen):
        x = tussen + i * (maat + tussen)
        im.paste(laad(n, maat), (x, 0))
        d.rounded_rectangle([x, 0, x + maat - 1, maat - 1], 24, outline=DARK, width=6)
        letter(d, x + maat // 2, maat + 65, "ABC"[i])
    return im


def met_pijl(bestand, van, naar, m=220):
    im = rand(laad(bestand), m)
    return pijl(im, (van[0] + m, van[1] + m), (naar[0] + m, naar[1] + m))


def waterbak(bestand, letters):
    im = laad(bestand); im2 = Image.new("RGB", (im.width, im.height + 60), "white"); im2.paste(im, (0, 0))
    d = ImageDraw.Draw(im2)
    for x, s in zip((280, 615, 980), letters): letter(d, x, 1150, s, 150)
    return im2


E = lambda n: (lambda: laad(n))
FOTO = {
    # dieren
    "werkwoorden-vogel": E("vogel-zingt"), "woordsoorten-vogel": E("vogel-zingt"),
    "werkwoorden-vogel-2": E("vogel-vliegt-weg"),
    "spelling-hond": E("hond"), "woordsoorten-hond": E("hond-blaft"), "werkwoorden-hond": E("hond-slaapt-mand"),
    "spelling-honden": E("twee-honden"),
    "woordsoorten-koe": E("koe-wei"), "woordsoorten-koe-2": E("koe-wei"), "planten-koe": E("koe-kalf"),
    "spelling-vis": E("vis"), "werkwoorden-vis": E("vis"), "planten-vis": E("vis"),
    "planten-insect": E("insect"), "planten-spin": E("spin"),
    # dingen
    "werkwoorden-bal": E("voetbal-trappen"),
    "spelling-ijsje": E("ijsje"), "werkwoorden-ijs": E("ijsje"),
    "spelling-trein": E("trein"), "werkwoorden-trein": E("trein"), "techniek-trein": E("trein"),
    "lezen-huis": E("huis"), "werkwoorden-huis": E("huis"), "samenleven-huis": E("huis"),
    "spelling-boom": E("hoge-boom"), "woordsoorten-boom": E("hoge-boom"),
    "lezen-zon": E("zon"), "woordsoorten-zon": E("zon"), "kaarten-zon": E("zonsopgang"),
    "spelling-bank": E("zitbank"), "lezen-bank": E("zitbank"), "stoffen-bank": E("zitbank"),
    "spelling-ring": E("ring"),
    # seizoenen en weer
    "natuur-lente": E("boom-lente"), "natuur-herfst": E("boom-herfst"), "natuur-winter": E("boom-winter"),
    "natuur-regen": E("regen"),
    # planten
    "planten-pijl-wortel": lambda: met_pijl("plant-met-wortels", (1230, 960), (720, 960)),
    "planten-pijl-stengel": lambda: met_pijl("plant-met-wortels", (1000, 560), (640, 560)),
    "planten-pijl-blad": lambda: met_pijl("plant-met-wortels", (-180, 300), (300, 440)),
    "planten-pijl-bloem": lambda: met_pijl("plant-met-wortels", (1230, 160), (820, 160)),
    "taal-strip-plant": lambda: strip(["strip-bloem", "strip-zaadje", "strip-kiemplantje"]),
    "taal-strip-ijs": lambda: strip(["strip-ijs-half", "strip-ijs-leeg", "strip-ijs-vol"]),
    # eten
    "lichaam-tussendoortje": lambda: rij(["chips", "lolly", "appel", "blikje"], list("ABCD")),
    "natuur-afval-kiezen": lambda: rij(["blikje", "chips", "bananenschil", "lolly"], list("ABCD")),
    "vraagstukken-winkel": lambda: rij(["appel", "banaan", "blikje"], ["€ 0,40", "€ 0,30", "€ 1,20"]),
    # lichaam
    "lichaam-oog": E("oog"),
    "lichaam-hart": lambda: met_pijl("hart-en-longen", (1230, 820), (690, 820)),
    # stoffen
    "stoffen-ijsblokjes": E("ijsblokjes"), "stoffen-glas": E("glas-water"), "stoffen-pot": E("kokende-pot"),
    "stoffen-magneet": E("magneet"),
    "stoffen-waterbak": lambda: waterbak("drijven-zinken-1", "ABC"),
    "stoffen-waterbak-2": lambda: waterbak("drijven-zinken-2", "ABC"),
    # techniek
    "techniek-wip": E("wip"), "techniek-katrol": E("katrol"), "techniek-kruiwagen": E("kruiwagen"),
    "techniek-stopcontact": E("stopcontact"),
    # natuur en afval
    "natuur-pmd": E("pmd-zak"), "natuur-gft": E("gft-container"), "natuur-gft-2": E("gft-container"),
    # wereld
    "wereld-pool": E("poolgebied"), "wereld-woestijn": E("woestijn"), "wereld-regenwoud": E("regenwoud"),
    # geschiedenis
    "vroeger-grot": E("grotschildering"), "vroeger-vuistbijl": E("vuistbijl"), "vroeger-schild": E("ridderschild"),
    "vroeger-burcht-gracht": lambda: met_pijl("burcht", (300, 1440), (300, 1030)),
    "vroeger-burcht-brug": lambda: met_pijl("burcht", (1440, 1230), (900, 1000)),
    "vroeger-burcht-toren": lambda: met_pijl("burcht", (-190, 600), (40, 600)),
    "tijd-kaars-lamp": lambda: rij(["kaars", "gloeilamp"]),
    "tijd-telefoons": lambda: rij(["oude-telefoon", "gsm"]),
    "tijd-oudste": lambda: rij(["kaars", "gsm", "gloeilamp"], list("ABC")),
    # samenleven
    "samenleven-kerstboom": E("kerstboom"), "samenleven-paaseieren": E("paaseieren"),
    "samenleven-gemeentehuis": E("gemeentehuis"),
}


def maak(naam, MAP, bron):
    im = FOTO[naam]()
    if max(im.size) > 900:
        f = 900 / max(im.size); im = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
    MAP.mkdir(parents=True, exist_ok=True)
    im.save(MAP / f"{naam}.webp", "WEBP", quality=80, method=6)
    bron(f"{naam}.webp", BRONREGEL)
    return f"/examenvormen/ready/{naam}.webp"
