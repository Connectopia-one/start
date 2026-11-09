# Maakt de kaartdata voor public/spellen/kaartpuzzel.html uit Natural Earth (publiek domein).
# Nodig: bel.json (ne_10m_admin_1_states_provinces, enkel BEL) en ne50c.json (ne_50m_admin_0_countries).
# Daarna sorteert een klein stukje de gebieden van groot naar klein en plakt de data in de html (zie git-historie, 9/11/2026).
import json, math

def dp(pts, eps):
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy) or 1e-9
    imax, dmax = 0, 0
    for i in range(1, len(pts) - 1):
        x, y = pts[i]
        d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / n if (dx or dy) else math.hypot(x - x1, y - y1)
        if d > dmax:
            imax, dmax = i, d
    if dmax > eps:
        return dp(pts[:imax + 1], eps)[:-1] + dp(pts[imax:], eps)
    return [pts[0], pts[-1]]

def polys(geom):
    if geom['type'] == 'Polygon':
        return [geom['coordinates']]
    return geom['coordinates']

def bouw(features, naam, speelbaar, lat0, bbox, breedte, eps, minring):
    k = math.cos(math.radians(lat0))
    lon0, lat_min, lon1, lat_max = bbox
    sx = breedte / ((lon1 - lon0) * k)
    hoogte = (lat_max - lat_min) * sx
    proj = lambda lon, lat: ((lon - lon0) * k * sx, (lat_max - lat) * sx)
    uit = []
    for f in features:
        d = []
        cx = cy = cn = 0
        for poly in polys(f['geometry']):
            for ri, ring in enumerate(poly):
                if ri > 0:
                    continue
                p = [proj(*c[:2]) for c in ring]
                xs = [a for a, b in p]; ys = [b for a, b in p]
                if max(xs) < -50 or min(xs) > breedte + 50 or max(ys) < -50 or min(ys) > hoogte + 50:
                    continue
                if (max(xs) - min(xs)) * (max(ys) - min(ys)) < minring:
                    continue
                q = dp(p, eps)
                if len(q) < 3:
                    continue
                d.append('M' + 'L'.join(f'{x:.1f},{y:.1f}' for x, y in q) + 'Z')
                if ri == 0:
                    area = (max(xs) - min(xs)) * (max(ys) - min(ys))
                    cx += sum(xs) / len(xs) * area; cy += sum(ys) / len(ys) * area; cn += area
        if not d:
            continue
        n = naam(f)
        uit.append({'naam': n, 'speel': n in speelbaar, 'd': ''.join(d), 'cx': round(cx / cn, 1), 'cy': round(cy / cn, 1)})
    return {'b': breedte, 'h': round(hoogte, 1), 'gebieden': uit}

bel = json.load(open('bel.json'))['features']
NL = {'Provincie Antwerpen': 'Antwerpen', 'Brussels Hoofdstedelijk Gewest': 'Brussel'}
belg = bouw(bel, lambda f: NL.get(f['properties']['name_nl'], f['properties']['name_nl']),
            set(['West-Vlaanderen', 'Oost-Vlaanderen', 'Antwerpen', 'Limburg', 'Vlaams-Brabant', 'Brussel',
                 'Waals-Brabant', 'Henegouwen', 'Namen', 'Luik', 'Luxemburg']),
            50.5, (2.5, 49.45, 6.45, 51.55), 640, 0.8, 0)

c = json.load(open('ne50c.json'))['features']
EUR = {'België', 'Nederland', 'Luxemburg', 'Frankrijk', 'Duitsland', 'Verenigd Koninkrijk', 'Ierland', 'Spanje',
       'Portugal', 'Italië', 'Zwitserland', 'Oostenrijk', 'Polen', 'Tsjechië', 'Denemarken', 'Zweden', 'Noorwegen',
       'Finland', 'Griekenland'}
c = [f for f in c if f['properties'].get('CONTINENT') in ('Europe', 'Africa', 'Asia')]
eur = bouw(c, lambda f: f['properties'].get('NAME_NL') or f['properties']['NAME'], EUR,
           52, (-12, 34.5, 34, 71.5), 640, 0.9, 6)
gevonden = {g['naam'] for g in eur['gebieden'] if g['speel']}
print('Europa ontbreekt:', EUR - gevonden)
print('Belgie:', [g['naam'] for g in belg['gebieden']])
json.dump({'belgie': belg, 'europa': eur}, open('kaartdata.json', 'w'), ensure_ascii=False, separators=(',', ':'))
import os; print(os.path.getsize('kaartdata.json'))
