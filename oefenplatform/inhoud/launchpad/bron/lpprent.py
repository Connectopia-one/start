# -*- coding: utf-8 -*-
"""Prenten voor de Launchpad-vragen (1ste en 2de leerjaar, Kim 27/11).

Kim maakte de prenten zelf met een beeldgenerator (eigen beeld van Connectopia). De
originelen staan in /mnt/project-files/launchpad/gegenereerd/ (lp-*.png). Voor dieren en
dingen die al bij Ready zaten, gebruiken we Kims Ready-prenten opnieuw
(/mnt/project-files/ready-prenten-26-11/gegenereerd/).

Zelfde zachte filter als bij Ready (Kims keuze 27/11). Hier zetten we ook de groepjes
om te tellen, de wijzers op de klok, de munten en de letters erop. Elke functie geeft
het pad terug dat in de vraag komt: /examenvormen/launchpad/<naam>.webp."""
import math, pathlib, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "ready" / "bron"))
import foto as F  # noqa: E402

LP = pathlib.Path("/mnt/project-files/launchpad/gegenereerd")
RD = pathlib.Path("/mnt/project-files/ready-prenten-26-11/gegenereerd")
MAP = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "launchpad"
BRON = "eigen beeld Connectopia (Kim, met een beeldgenerator, 27/11/2026)"
ORANJE, DARK = F.ORANJE, F.DARK
GEMAAKT = {}


def laad(n, maat=None, knip=False):
    """knip=True: snij de lege rand weg (voor kleine voorwerpen in een groepje) en
    maak de achtergrond helemaal wit, zodat er geen grijze vakjes verschijnen."""
    p = LP / f"{n}.png"
    if not p.exists(): p = RD / f"{n}.png"
    im = Image.open(p).convert("RGB")
    if knip:
        from PIL import ImageChops
        grijs = ImageChops.difference(im, Image.new("RGB", im.size, im.getpixel((3, 3)))).convert("L").point(lambda v: 255 if v > 18 else 0)
        bb = grijs.getbbox()
        if bb:
            m = 30; x0, y0, x1, y1 = max(bb[0] - m, 0), max(bb[1] - m, 0), min(bb[2] + m, im.width), min(bb[3] + m, im.height)
            z = max(x1 - x0, y1 - y0); cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
            vak = Image.new("RGB", (z, z), im.getpixel((3, 3))); vak.paste(im.crop((x0, y0, x1, y1)), ((z - (x1 - x0)) // 2, (z - (y1 - y0)) // 2))
            # achtergrond naar zuiver wit
            masker = grijs.crop((x0, y0, x1, y1)); m2 = Image.new("L", (z, z), 0); m2.paste(masker, ((z - (x1 - x0)) // 2, (z - (y1 - y0)) // 2))
            from PIL import ImageFilter
            m2 = m2.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(3))
            im = Image.composite(vak, Image.new("RGB", (z, z), "white"), m2)
    im = F.zacht(im)
    if knip:
        im = Image.composite(im, Image.new("RGB", im.size, "white"), m2)
    if maat: im = im.resize((maat, maat), Image.LANCZOS)
    return im


def _bronnen():
    f = MAP / "BRONNEN.txt"
    uit = {}
    if f.exists():
        for l in f.read_text(encoding="utf-8").splitlines()[1:]:
            if ": " in l: k, v = l.split(": ", 1); uit[k] = v
    return uit


def bewaar(naam, im):
    if max(im.size) > 900:
        f = 900 / max(im.size); im = im.resize((round(im.width * f), round(im.height * f)), Image.LANCZOS)
    MAP.mkdir(parents=True, exist_ok=True)
    im.save(MAP / f"{naam}.webp", "WEBP", quality=80, method=6)
    b = _bronnen(); b[f"{naam}.webp"] = BRON
    (MAP / "BRONNEN.txt").write_text("Prenten Launchpad die niet zelf getekend zijn:\n" + "".join(f"{k}: {v}\n" for k, v in sorted(b.items())), encoding="utf-8")
    GEMAAKT[naam] = True
    return f"/examenvormen/launchpad/{naam}.webp"


def een(naam, bron):
    """Eén prent, gewoon met het filter."""
    return bewaar(naam, laad(bron))


def groep(naam, bron, n, per=5, maat=170, tussen=14, extra=None):
    """n keer hetzelfde voorwerp, in rijtjes van 'per' (zoals een rekenrek).
    extra = (bron2, n2): daarna nog n2 van een ander voorwerp, in een nieuwe rij."""
    items = [bron] * n
    rijen = [items[i:i + per] for i in range(0, len(items), per)]
    if extra:
        e = [extra[0]] * extra[1]; rijen += [e[i:i + per] for i in range(0, len(e), per)]
    cols = max(len(r) for r in rijen)
    im = Image.new("RGB", (cols * (maat + tussen) + tussen, len(rijen) * (maat + tussen) + tussen), "white")
    cache = {}
    for y, r in enumerate(rijen):
        for x, b in enumerate(r):
            if b not in cache: cache[b] = laad(b, maat, True)
            im.paste(cache[b], (tussen + x * (maat + tussen), tussen + y * (maat + tussen)))
    return bewaar(naam, im)


def twee_groepen(naam, links, rechts, maat=150):
    """Twee groepjes naast elkaar met een streep ertussen (splitsen, vergelijken).
    links/rechts = (bron, aantal)."""
    def blok(b, n):
        per = 3 if n > 4 else 2
        rij = (n + per - 1) // per
        im = Image.new("RGB", (per * (maat + 10) + 10, max(rij, 1) * (maat + 10) + 10), "white")
        t = laad(b, maat, True)
        for i in range(n): im.paste(t, (10 + (i % per) * (maat + 10), 10 + (i // per) * (maat + 10)))
        return im
    a, b = blok(*links), blok(*rechts)
    h = max(a.height, b.height)
    im = Image.new("RGB", (a.width + b.width + 60, h), "white")
    im.paste(a, (0, (h - a.height) // 2)); im.paste(b, (a.width + 60, (h - b.height) // 2))
    ImageDraw.Draw(im).line([(a.width + 30, 10), (a.width + 30, h - 10)], fill=DARK, width=6)
    return bewaar(naam, im)


def rij(naam, bronnen, onder=None, maat=380):
    """Prenten naast elkaar met een letter of woord eronder."""
    h = maat + (120 if onder else 0)
    im = Image.new("RGB", (len(bronnen) * (maat + 30) + 30, h), "white"); d = ImageDraw.Draw(im)
    for i, b in enumerate(bronnen):
        x = 30 + i * (maat + 30); im.paste(laad(b, maat), (x, 0))
        if onder: F.letter(d, x + maat // 2, maat + 60, onder[i], 80 if len(onder[i]) <= 1 else 58, ORANJE if len(onder[i]) <= 1 else DARK)
    return bewaar(naam, im)


# Middelpunt en straal van de wijzerplaat op lp-wandklok.png (1254 x 1254)
KC, KR = (627, 636), 380


def klok(naam, uur, minuut):
    """Kims wandklok met cijfers en wijzers erop."""
    im = laad("lp-wandklok"); d = ImageDraw.Draw(im)
    f = ImageFont.truetype(F.FONT, 70); cx, cy = KC
    for i in range(1, 13):
        a = math.radians(i * 30 - 90)
        d.text((cx + (KR - 115) * math.cos(a), cy + (KR - 115) * math.sin(a)), str(i), font=f, fill=DARK, anchor="mm")
    au = math.radians((uur % 12 + minuut / 60) * 30 - 90); am = math.radians(minuut * 6 - 90)
    d.line([(cx, cy), (cx + KR * .48 * math.cos(au), cy + KR * .48 * math.sin(au))], fill=ORANJE, width=30)
    d.line([(cx, cy), (cx + KR * .6 * math.cos(am), cy + KR * .6 * math.sin(am))], fill=DARK, width=18)
    d.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], fill=DARK)
    return bewaar(naam, im)


def munten(naam, waarden, maat=230, per=3):
    """Munten en briefjes in euro, getekend, in rijen van 3 zodat alles groot blijft."""
    f = ImageFont.truetype(F.FONT, 64)
    rijen = [waarden[i:i + per] for i in range(0, len(waarden), per)]
    br = lambda w: maat if w <= 2 else int(maat * 1.5)
    W = max(sum(br(w) for w in r) + 30 * (len(r) + 1) for r in rijen)
    im = Image.new("RGB", (W, len(rijen) * (maat + 30) + 30), "white"); d = ImageDraw.Draw(im)
    for j, r in enumerate(rijen):
        x = 30; y = 30 + j * (maat + 30)
        for w in r:
            b = br(w)
            if w <= 2:
                d.ellipse([x, y, x + maat, y + maat], fill=(242, 217, 138), outline=(160, 123, 31), width=12)
                d.ellipse([x + 30, y + 30, x + maat - 30, y + maat - 30], outline=(200, 170, 80), width=4)
                d.text((x + maat / 2, y + maat / 2), f"€{w}", font=f, fill=(90, 68, 16), anchor="mm")
            else:
                d.rounded_rectangle([x, y + 25, x + b, y + maat - 25], 18, fill=(232, 240, 220), outline=DARK, width=8)
                d.text((x + b / 2, y + maat / 2), f"€ {w}", font=f, fill=DARK, anchor="mm")
            x += b + 30
    return bewaar(naam, im)


def strip(naam, bronnen, maat=420):
    """Prentverhaal: elk prentje in een kader, letter A, B, C eronder."""
    im = Image.new("RGB", (len(bronnen) * (maat + 30) + 30, maat + 130), "white"); d = ImageDraw.Draw(im)
    for i, b in enumerate(bronnen):
        x = 30 + i * (maat + 30); im.paste(laad(b, maat), (x, 0))
        d.rounded_rectangle([x, 0, x + maat - 1, maat - 1], 24, outline=DARK, width=6)
        F.letter(d, x + maat // 2, maat + 65, "ABCD"[i])
    return bewaar(naam, im)
