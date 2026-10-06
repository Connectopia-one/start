"""
Maakt van de A5-pdf een A4-pdf. A4 en A5 hebben dezelfde verhouding, dus
het blad past er precies op; alles wordt gewoon groter.

    python3 maak-a4.py
"""
import pymupdf

bron = pymupdf.open("../flyer-wachtkamer-A5.pdf")
uit = pymupdf.open()
a4 = pymupdf.paper_rect("a4")
blad = uit.new_page(width=a4.width, height=a4.height)
blad.show_pdf_page(blad.rect, bron, 0)
uit.save("../flyer-wachtkamer-A4.pdf")
print("A4 gemaakt:", blad.rect)
