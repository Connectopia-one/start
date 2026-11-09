"""Maten van de zelfgetekende prenten, gedeeld door de vragen (klikvakken) en
door maak_prenten_bedrijfswetenschappen_beyond.py (tekenen).

Een klikvak is [links, boven, breedte, hoogte] in procent van de prent.
"""

# ---- kaart: een document met regels (aanslagbiljet, factuur, loonbrief, ...)
KAART_B = 900
KAART_TOP = 90      # onder de titel
KAART_RIJ = 48


def kaart_hoogte(n):
    return KAART_TOP + n * KAART_RIJ + 30


def kaart_zone(i, n):
    """Klikvak over regel i (vanaf 0) van een kaart met n regels."""
    h = kaart_hoogte(n)
    return [2.0, round((KAART_TOP + i * KAART_RIJ) / h * 100, 1), 96.0, round(KAART_RIJ / h * 100, 1)]


# ---- raster: een schema met vakken (SWOT, BCG, BMC, balans)
def vak_zone(x, y, w, h, B, H):
    return [round(x / B * 100, 1), round(y / H * 100, 1), round(w / B * 100, 1), round(h / H * 100, 1)]


# ---- tijdlijn van een boekjaar (1 januari tot 31 december)
JAAR_B, JAAR_H = 1000, 260
JAAR_X0, JAAR_X1 = 60, 940


def x_dag(dag):
    """dag 1 = 1 januari, dag 365 = 31 december."""
    return JAAR_X0 + (dag - 1) / 364 * (JAAR_X1 - JAAR_X0)


VA_DAGEN = [("VA1", "10 april", 100), ("VA2", "10 juli", 191), ("VA3", "10 oktober", 283), ("VA4", "20 december", 354)]


def va_zone(i):
    x = x_dag(VA_DAGEN[i][2])
    return [round((x - 45) / JAAR_B * 100, 1), 20.0, 9.0, 70.0]


# ---- raster: rijkoppen links, kolomkoppen boven, cellen met tekst
RASTER_B = 1000
RASTER_TOP = 70       # titel
RASTER_KOP = 60       # hoogte kolomkoppen
RASTER_LINKS = 280    # breedte rijkoppen (0 als er geen zijn)
RASTER_CEL = 130      # hoogte van een rij


def raster_maat(n_rijen, rijkoppen=True):
    links = RASTER_LINKS if rijkoppen else 20
    return links, RASTER_B, RASTER_TOP + RASTER_KOP + n_rijen * RASTER_CEL + 20


def raster_zone(r, k, n_rijen, n_kol, rijkoppen=True):
    links, B, H = raster_maat(n_rijen, rijkoppen)
    w = (B - 20 - links) / n_kol
    x = links + k * w
    y = RASTER_TOP + RASTER_KOP + r * RASTER_CEL
    return vak_zone(x, y, w, RASTER_CEL, B, H)


# ---- balans voor financiële analyse (Velo nv)
BALANS_B, BALANS_H = 1000, 560
# naam: (x, y, w, h, label, bedrag)
BALANS_VAKKEN = {
    "langdurend": (20, 120, 470, 200, "Langdurende activa", "600 000"),
    "voorraad": (20, 330, 470, 60, "Voorraden", "150 000"),
    "vorderingen": (20, 395, 470, 60, "Vorderingen op ten hoogste een jaar", "180 000"),
    "liquide": (20, 460, 470, 60, "Liquide middelen", "70 000"),
    "ev": (510, 120, 470, 180, "Eigen vermogen", "450 000"),
    "vvlt": (510, 310, 470, 100, "Vreemd vermogen op lange termijn", "250 000"),
    "vvkt": (510, 420, 470, 100, "Vreemd vermogen op korte termijn", "300 000"),
}


def balans_zone(naam):
    x, y, w, h = BALANS_VAKKEN[naam][:4]
    return vak_zone(x, y, w, h, BALANS_B, BALANS_H)


# ---- bedrijfscyclus in dagen (liquiditeit)
CYCLUS_B, CYCLUS_H = 1000, 420
CYCLUS_X0, CYCLUS_DAG = 80, 10      # x van dag 0, pixels per dag
# naam: (van dag, tot dag, y, label)
CYCLUS_BALKEN = {
    "voorraad": (0, 50, 130, "Omlooptijd voorraad: 50 dagen"),
    "klant": (50, 80, 200, "Klantenkrediet: 30 dagen"),
    "leverancier": (0, 40, 270, "Leverancierskrediet: 40 dagen"),
    "ntfp": (40, 80, 340, "?"),
}


def cyclus_zone(naam):
    van, tot, y, _ = CYCLUS_BALKEN[naam]
    x = CYCLUS_X0 + van * CYCLUS_DAG
    return vak_zone(x, y - 10, (tot - van) * CYCLUS_DAG, 56, CYCLUS_B, CYCLUS_H)


# ---- Business Model Canvas
BMC_B, BMC_H = 1000, 640
_k = (1000 - 40) / 5          # breedte van een kolom
BMC_VAKKEN = {
    "partners": (20, 70, _k, 380, "Partners"),
    "activiteiten": (20 + _k, 70, _k, 190, "Kernactiviteiten"),
    "middelen": (20 + _k, 260, _k, 190, "Kernmiddelen"),
    "waarde": (20 + 2 * _k, 70, _k, 380, "Waardepropositie"),
    "relaties": (20 + 3 * _k, 70, _k, 190, "Klantrelaties"),
    "kanalen": (20 + 3 * _k, 260, _k, 190, "Kanalen"),
    "segmenten": (20 + 4 * _k, 70, _k, 380, "Klantsegmenten"),
    "kosten": (20, 450, 2.5 * _k, 170, "Kostenstructuur"),
    "inkomsten": (20 + 2.5 * _k, 450, 2.5 * _k, 170, "Inkomstenstromen"),
}


def bmc_zone(naam):
    x, y, w, h = BMC_VAKKEN[naam][:4]
    return vak_zone(x, y, w, h, BMC_B, BMC_H)


# ---- productlevenscyclus: vijf fasen van gelijke breedte
PLC_B, PLC_H = 1000, 480
PLC_X0, PLC_X1, PLC_TOP, PLC_ONDER = 90, 960, 90, 400


def plc_zone(i):
    w = (PLC_X1 - PLC_X0) / 5
    return vak_zone(PLC_X0 + i * w, PLC_TOP - 40, w, PLC_ONDER - PLC_TOP + 40, PLC_B, PLC_H)


# ---- opzegtermijnen bij ontslag (tabel met drie kolommen)
OPZEG_B = 1000
OPZEG_TOP = 140       # titel en kolomkoppen
OPZEG_RIJ = 40
OPZEG_KOL = [(20, 420), (420, 720), (720, 980)]
# anciënniteit, opzegtermijn als de werkgever opzegt, als de werknemer opzegt
OPZEG = [
    ("minder dan 3 maanden", "1 week", "1 week"),
    ("3 tot 4 maanden", "3 weken", "2 weken"),
    ("4 tot 5 maanden", "4 weken", "2 weken"),
    ("5 tot 6 maanden", "5 weken", "2 weken"),
    ("6 tot 9 maanden", "6 weken", "3 weken"),
    ("9 tot 12 maanden", "7 weken", "3 weken"),
    ("12 tot 15 maanden", "8 weken", "4 weken"),
    ("15 tot 18 maanden", "9 weken", "4 weken"),
    ("18 tot 21 maanden", "10 weken", "5 weken"),
    ("21 tot 24 maanden", "11 weken", "5 weken"),
    ("2 tot 3 jaar", "12 weken", "6 weken"),
    ("3 tot 4 jaar", "13 weken", "6 weken"),
    ("4 tot 5 jaar", "15 weken", "7 weken"),
    ("5 tot 6 jaar", "18 weken", "9 weken"),
]
OPZEG_H = OPZEG_TOP + len(OPZEG) * OPZEG_RIJ + 60


def opzeg_zone(r, k):
    """Klikvak over rij r (vanaf 0), kolom k (0 anciënniteit, 1 werkgever, 2 werknemer)."""
    x0, x1 = OPZEG_KOL[k]
    return vak_zone(x0, OPZEG_TOP + r * OPZEG_RIJ, x1 - x0, OPZEG_RIJ, OPZEG_B, OPZEG_H)


# ---- grafieken met assen (voorraad, voorraadkosten, break-even)
GRAF_B, GRAF_H = 1000, 520
GRAF_X0, GRAF_X1, GRAF_TOP, GRAF_ONDER = 110, 900, 80, 440


def gx(t, tmax):
    return GRAF_X0 + t / tmax * (GRAF_X1 - GRAF_X0)


def gy(v, vmax):
    return GRAF_ONDER - v / vmax * (GRAF_ONDER - GRAF_TOP)


def graf_zone(x, y, w, h):
    return vak_zone(x, y, w, h, GRAF_B, GRAF_H)


# voorraadverloop: 600 stuks, daalt in 30 dagen tot 100, levering van 500
VV_MAX, VV_MIN, VV_DAGEN, VV_CYCLUS = 600, 100, 90, 30
VV_VMAX = 700


def vv_zone(naam):
    if naam == "max":
        return graf_zone(GRAF_X0, gy(VV_MAX, VV_VMAX) - 22, GRAF_X1 - GRAF_X0 + 10, 44)
    if naam == "min":
        return graf_zone(GRAF_X0, gy(VV_MIN, VV_VMAX) - 22, GRAF_X1 - GRAF_X0 + 10, 44)
    if naam == "levering":   # de eerste levering op dag 30
        x = gx(VV_CYCLUS, VV_DAGEN)
        return graf_zone(x - 30, gy(VV_MAX, VV_VMAX) + 24, 60, gy(VV_MIN, VV_VMAX) - gy(VV_MAX, VV_VMAX) - 48)
    raise KeyError(naam)


# voorraadkosten: bewaarkosten stijgen, bestelkosten dalen, totaal is een dal
VK_QMAX = 1000
VK_OPT = 400          # optimale bestelgrootte


def vk_bewaar(q):
    return 0.1 * q


def vk_bestel(q):
    return 16000 / q


VK_VMAX = 120


def vk_zone(naam):
    if naam == "optimum":
        x, y = gx(VK_OPT, VK_QMAX), gy(vk_bewaar(VK_OPT) + vk_bestel(VK_OPT), VK_VMAX)
        return graf_zone(x - 35, y - 35, 70, 70)
    raise KeyError(naam)


# break-even: vaste kosten 20 000, variabel 30 per stuk, prijs 50
BE_VAST, BE_VAR, BE_PRIJS, BE_QMAX, BE_VMAX = 20000, 30, 50, 2000, 100000
BE_Q = BE_VAST // (BE_PRIJS - BE_VAR)


def _be_vak(q0, q1, v0, v1):
    return graf_zone(gx(q0, BE_QMAX), gy(v1, BE_VMAX), gx(q1, BE_QMAX) - gx(q0, BE_QMAX), gy(v0, BE_VMAX) - gy(v1, BE_VMAX))


def be_zone(naam):
    if naam == "punt":
        x, y = gx(BE_Q, BE_QMAX), gy(BE_Q * BE_PRIJS, BE_VMAX)
        return graf_zone(x - 35, y - 35, 70, 70)
    raise KeyError(naam)


# ---- databank: twee tabellen met een één-op-veel-relatie
DB_B, DB_H = 1000, 520
DB_KOP_Y, DB_VELD_Y, DB_RIJ = 90, 134, 44
DB_TABELLEN = {
    "Klanten": dict(x=20, w=420, velden=["Klantnr", "Naam", "Gemeente"], sleutel=0, records=[
        ["1", "Peeters", "Hasselt"], ["2", "Janssens", "Genk"], ["3", "Claes", "Alken"], ["4", "Maes", "Hasselt"]]),
    "Bestellingen": dict(x=500, w=480, velden=["Bestelnr", "Klantnr", "Datum", "Bedrag"], sleutel=0, records=[
        ["101", "1", "03/11", "120,00"], ["102", "3", "04/11", "45,50"], ["103", "1", "05/11", "89,90"],
        ["104", "2", "07/11", "230,00"], ["105", "1", "08/11", "15,00"]]),
}


def db_kol(tabel, k):
    t = DB_TABELLEN[tabel]
    w = t["w"] / len(t["velden"])
    return t["x"] + k * w, w


def db_veld_zone(tabel, k):
    x, w = db_kol(tabel, k)
    return vak_zone(x, DB_VELD_Y, w, DB_RIJ, DB_B, DB_H)


def db_record_zone(tabel, r):
    t = DB_TABELLEN[tabel]
    return vak_zone(t["x"], DB_VELD_Y + (r + 1) * DB_RIJ, t["w"], DB_RIJ, DB_B, DB_H)


def db_naam_zone(tabel):
    t = DB_TABELLEN[tabel]
    return vak_zone(t["x"], DB_KOP_Y, t["w"], DB_RIJ, DB_B, DB_H)


DB_RELATIE_Y = 440


def db_relatie_zone():
    x0 = db_kol("Klanten", 0)[0]
    x1, w1 = db_kol("Bestellingen", 1)
    return vak_zone(x0, DB_RELATIE_Y - 38, x1 + w1 - x0, 70, DB_B, DB_H)


def be_zones(naam):
    """Winst- of verlieszone als smalle stroken die helemaal tussen omzet en totale kosten liggen."""
    def omzet(q):
        return BE_PRIJS * q

    def kost(q):
        return BE_VAST + BE_VAR * q
    if naam == "winst":     # omzet boven, kosten onder
        stroken = [(1500, 1650), (1650, 1800), (1800, 2000)]
        return [_be_vak(q0, q1, kost(q1), omzet(q0)) for q0, q1 in stroken]
    if naam == "verlies":   # kosten boven, omzet onder
        stroken = [(0, 150), (150, 300), (300, 500)]
        return [_be_vak(q0, q1, omzet(q1), kost(q0)) for q0, q1 in stroken]
    raise KeyError(naam)
