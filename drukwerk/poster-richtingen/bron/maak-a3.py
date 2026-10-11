"""Maakt van de A4-pdf een A3-pdf, voor wie de poster groot wil ophangen.

    python3 -I maak-a3.py

Playwright zijn eigen `scale` zet een A4 in een A3-kader; dit schaalt de
bladzijde wel echt mee. Zelfde aanpak als in drukwerk/poster-ophangen/.
"""
import pymupdf

bron = pymupdf.open("../poster-richtingen-A4.pdf")
uit = pymupdf.open()
a3 = pymupdf.paper_rect("a3")
blad = uit.new_page(width=a3.width, height=a3.height)
blad.show_pdf_page(blad.rect, bron, 0)
uit.save("../poster-richtingen-A3.pdf")
print("A3 gemaakt:", blad.rect)
