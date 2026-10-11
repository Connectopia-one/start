import sys, pymupdf
for f in sys.argv[1:]:
    d = pymupdf.open(f)
    uit = []
    for pg in d:
        b = max((x[3] for x in pg.get_text("blocks") if x[3] < 788), default=0)
        for t in pg.get_drawings():
            if t["rect"].y1 < 788:
                b = max(b, t["rect"].y1)
        uit.append(round(b))
    print(f, uit)
