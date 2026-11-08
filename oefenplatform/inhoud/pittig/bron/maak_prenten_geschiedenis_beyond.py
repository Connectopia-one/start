"""Tekent de prenten die Claude zelf maakt voor de pittige vragen geschiedenis 🌍 Beyond.

    python3 inhoud/pittig/bron/maak_prenten_geschiedenis_beyond.py

Schrijft naar public/examenvormen/geschiedenis-beyond/. Enkel eenvoudige
tekeningen zonder auteursrecht: tijdlijnen, schema's en grafieken met cijfers
uit de leerbundel. Foto's, affiches en spotprenten zoekt Kim zelf; die staan op
de prentenlijst.

De klikvakken (zones) in de vragen zijn in procent van de breedte en hoogte.
Wie hier iets verschuift, rekent de zones na met zone_jaar().
"""
import pathlib

UIT = pathlib.Path(__file__).resolve().parents[3] / "public" / "examenvormen" / "geschiedenis-beyond"
GROEN, DONKER, ACHTER = "#2f4a22", "#24331b", "#fffdf7"

# ---------------------------------------------------------------- tijdlijn 1750-2030
B, H = 1000, 210
X0, X1 = 50, 923
J0, J1 = 1750, 2030


def x_jaar(jaar):
    return X0 + (jaar - J0) / (J1 - J0) * (X1 - X0)


def zone_jaar(jaar, breed=20):
    """Een klikvak rond een jaar, in procent: breed is de breedte in jaren."""
    links = x_jaar(jaar - breed / 2) / B * 100
    return [round(links, 1), 25, round(breed / (J1 - J0) * (X1 - X0) / B * 100, 1), 55]


def tijdlijn():
    d = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {B} {H}" width="{B}" height="{H}" font-family="Arial, sans-serif">',
         f'<rect width="{B}" height="{H}" fill="{ACHTER}"/>',
         f'<line x1="{X0}" y1="110" x2="{X1}" y2="110" stroke="{GROEN}" stroke-width="5"/>',
         f'<polygon points="{X1},98 {X1+24},110 {X1},122" fill="{GROEN}"/>']
    for j in range(J0, J1 + 1, 10):
        x = x_jaar(j)
        if j % 50 == 0:
            d.append(f'<line x1="{x:.1f}" y1="92" x2="{x:.1f}" y2="128" stroke="{GROEN}" stroke-width="4"/>')
            d.append(f'<text x="{x:.1f}" y="166" font-size="28" text-anchor="middle" fill="{DONKER}">{j}</text>')
        else:
            d.append(f'<line x1="{x:.1f}" y1="102" x2="{x:.1f}" y2="118" stroke="{GROEN}" stroke-width="1.5"/>')
    d.append("</svg>")
    (UIT / "tijdlijn-1750-2030.svg").write_text("\n".join(d) + "\n", encoding="utf-8")


if __name__ == "__main__":
    UIT.mkdir(parents=True, exist_ok=True)
    tijdlijn()
    for j in (1789, 1815, 1830, 1871, 1914, 1945, 1989):
        print(j, zone_jaar(j))
