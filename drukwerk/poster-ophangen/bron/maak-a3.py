"""
Maakt van de A4-pdf een A3-pdf, zodat de poster ook groot opgehangen kan
worden. Playwright zijn eigen `scale` zette een A4 in een A3-kader; dit
schaalt de bladzijde wel echt mee.

    python3 maak-a3.py
"""
import pymupdf

bron = pymupdf.open("../poster-connectopia-A4.pdf")
uit = pymupdf.open()
a3 = pymupdf.paper_rect("a3")
blad = uit.new_page(width=a3.width, height=a3.height)
blad.show_pdf_page(blad.rect, bron, 0)
uit.save("../poster-connectopia-A3.pdf")
print("A3 gemaakt:", blad.rect)
