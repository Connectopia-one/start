"""De bouw van het atoom en het periodiek systeem — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
import math
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Een stuk van het periodiek systeem (enkel hoofdgroepen) ---------------
PSE = Prent("pse-hoofdgroepen", "Een stuk van het periodiek systeem: de hoofdgroepen van de eerste vier perioden", "raster met H tot Ar, plus K en Ca, met atoomnummers")
RIJEN = [
    {1: ("H", 1), 8: ("He", 2)},
    {1: ("Li", 3), 2: ("Be", 4), 3: ("B", 5), 4: ("C", 6), 5: ("N", 7), 6: ("O", 8), 7: ("F", 9), 8: ("Ne", 10)},
    {1: ("Na", 11), 2: ("Mg", 12), 3: ("Al", 13), 4: ("Si", 14), 5: ("P", 15), 6: ("S", 16), 7: ("Cl", 17), 8: ("Ar", 18)},
    {1: ("K", 19), 2: ("Ca", 20)},
]
CEL = {}
for r, rij in enumerate(RIJEN):
    PSE.tekst(70, 150 + r * 110, f"periode {r + 1}", 16, "middle", "#666666")
    for k, (sym, z) in rij.items():
        x, y = 130 + (k - 1) * 105, 95 + r * 110
        kleur = "#eef4f8" if k == 8 else ("#fbe7c6" if sym in ("Li", "Be", "Na", "Mg", "Al", "K", "Ca") else "#ffffff")
        PSE.rect(x, y, 96, 96, kleur, DONKER, 8)
        PSE.tekst(x + 10, y + 22, z, 15, "start", "#666666")
        PSE.tekst(x + 48, y + 66, sym, 30, vet=True)
        CEL[sym] = Prent.zone(x, y, 96, 96)

# Het atoommodel van Bohr ------------------------------------------------
BOHR = Prent("bohr-atoom", "Een atoom volgens het model van Bohr, niet op schaal", "atoom met kern en drie schillen, configuratie 2, 8, 1")
CX, CY = 500, 330
for r in (70, 140, 210):
    BOHR.cirkel(CX, CY, r, "none", "#999999", 2)
BOHR.cirkel(CX, CY, 34, "#f7e2b0")
E = []
for r, n in ((70, 2), (140, 8), (210, 1)):
    for i in range(n):
        a = i * 2 * math.pi / n + (0.3 if r == 140 else -0.8)
        x, y = CX + r * math.cos(a), CY + r * math.sin(a)
        BOHR.cirkel(x, y, 10, BLAUW, DONKER, 1)
        E.append((r, x, y))
Z_KERN = Prent.rond(CX, CY, 42)
Z_VALENTIE = [Prent.rond(x, y, 22) for r, x, y in E if r == 210]
Z_SCHIL1 = [Prent.rond(x, y, 22) for r, x, y in E if r == 70]

VRAGEN = [
    klik(
        "Klik op het element met elektronenconfiguratie 2, 8, 7.",
        PSE.bestand, [CEL["Cl"]],
        "Twee plus acht plus zeven is 17 elektronen: chloor.",
    ),
    klik(
        "Klik op het element met twee valentie-elektronen en vier bezette schillen.",
        PSE.bestand, [CEL["Ca"]],
        "Tweede kolom van de hoofdgroepen en vierde periode: calcium.",
    ),
    klik(
        "Klik op het edelgas met twee bezette schillen.",
        PSE.bestand, [CEL["Ne"]],
        "Neon heeft 2, 8: een volle tweede schil.",
    ),
    klik(
        "Klik op het element uit periode 2 dat liefst twee elektronen opneemt.",
        PSE.bestand, [CEL["O"]],
        "Zuurstof heeft zes valentie-elektronen en neemt er nog twee op.",
    ),
    klik(
        "Klik op het element dat een ion vormt met 12 protonen en 10 elektronen.",
        PSE.bestand, [CEL["Mg"]],
        "Twaalf protonen is magnesium. Het staat twee elektronen af en wordt 2 plus.",
    ),
    klik(
        "Klik op het element waarvan het atoom maar één schil met elektronen heeft en één elektron.",
        PSE.bestand, [CEL["H"]],
        "Waterstof heeft atoomnummer 1: één proton en één elektron in de eerste schil.",
    ),
    met_prent(PSE.bestand, tabel(
        "Kijk naar het stuk van het periodiek systeem. Klopt dit?",
        [
            ("Na en K hebben evenveel valentie-elektronen.", J),
            ("Li en Na reageren op een vergelijkbare manier.", J),
            ("Mg heeft drie bezette schillen.", J),
            ("He en Ne staan in dezelfde periode.", F),
            ("De metalen staan rechts.", F),
        ],
        "Een kolom deelt het aantal valentie-elektronen, een rij het aantal bezette schillen. Metalen staan links.",
    )),
    klik(
        "Klik op de plek waar bijna de hele massa van dit atoom zit.",
        BOHR.bestand, [Z_KERN],
        "De kern bevat de protonen en neutronen en zo goed als alle massa.",
    ),
    klik(
        "Klik op het elektron dat dit atoom het makkelijkst afstaat.",
        BOHR.bestand, Z_VALENTIE,
        "Het enige elektron in de buitenste schil is het valentie-elektron. Na het afstaan blijft 2, 8 over.",
    ),
    met_prent(BOHR.bestand, tabel(
        "Het atoom op de prent is neutraal. Klopt dit?",
        [
            ("Het heeft 11 elektronen.", J),
            ("Het is een natriumatoom.", J),
            ("Het heeft één valentie-elektron.", J),
            ("Het staat in periode 2.", F),
            ("Het heeft een edelgasconfiguratie.", F),
        ],
        "Drie bezette schillen betekent periode 3. Met één elektron buiten is de schil niet vol.",
    )),
    tabel(
        "Klopt dit over de deeltjes in een atoom?",
        [
            ("Een proton is positief geladen.", J),
            ("Een neutron is negatief geladen.", F),
            ("Protonen en neutronen heten samen nucleonen.", J),
            ("Een elektron weegt ongeveer evenveel als een proton.", F),
            ("Het atoomnummer telt de protonen.", J),
        ],
        "Een neutron is neutraal. Een elektron weegt bijna tweeduizend keer minder dan een proton.",
    ),
    casus(
        "Een atoom heeft atoomnummer 19 en massagetal 39.",
        [
            inv(
                "Hoeveel neutronen zitten er in de kern?",
                ["20"],
                "Massagetal min atoomnummer: 39 min 19 is 20.",
            ),
            inv(
                "Hoeveel elektronen heeft het neutrale atoom?",
                ["19"],
                "In een neutraal atoom zijn er evenveel elektronen als protonen.",
            ),
            keuze(
                "De elektronenconfiguratie is [[*2, 8, 8, 1|2, 8, 9|2, 8, 8, 2]].",
                "Na 2 en 8 komen er 8 in de derde schil. Het negentiende elektron komt in de vierde.",
            ),
            mk(
                "Welk ion vormt dit atoom het liefst?",
                ["Een ion met lading 1 plus", "Een ion met lading 1 min", "Een ion met lading 7 min", "Geen ion, het is een edelgas"],
                0,
                "Eén elektron afstaan is veel makkelijker dan er zeven opnemen.",
            ),
        ],
    ),
    tabel(
        "Welke lading krijgt het ion?",
        [
            ("een atoom dat één elektron verliest", "1 plus"),
            ("een atoom uit groep 2 dat zijn valentie-elektronen afstaat", "2 plus"),
            ("een atoom dat twee elektronen opneemt", "2 min"),
            ("een chlooratoom dat één elektron opneemt", "1 min"),
        ],
        "Elektronen zijn negatief. Verlies maakt positief, winst maakt negatief.",
        kolommen=["1 plus", "2 plus", "1 min", "2 min"],
    ),
    koppel(
        "Koppel elk deeltje aan zijn beschrijving.",
        [
            ("12 protonen, 10 elektronen", "positief ion met lading 2 plus"),
            ("17 protonen, 18 elektronen", "negatief ion met lading 1 min"),
            ("8 protonen, 8 elektronen", "neutraal atoom"),
        ],
        ["isotoop met 2 protonen meer"],
        "Een isotoop verschilt in neutronen, niet in protonen.",
    ),
    tabel(
        "Klopt dit over isotopen?",
        [
            ("Ze hebben hetzelfde atoomnummer.", J),
            ("Ze hebben een verschillend massagetal.", J),
            ("Ze hebben een verschillend aantal protonen.", F),
            ("Ze gedragen zich chemisch hetzelfde.", J),
        ],
        "Isotopen verschillen enkel in het aantal neutronen.",
    ),
    sleep(
        "Een horizontale rij in het periodiek systeem is een [[periode]]. Het nummer ervan geeft het aantal bezette [[schillen]]. Een verticale kolom is een [[groep]].",
        ["nucleon", "isotoop"],
        "Elementen van één groep lijken sterk op elkaar.",
    ),
    mk(
        "Waarom lijken lithium, natrium en kalium chemisch zo op elkaar?",
        [
            "Ze hebben evenveel valentie-elektronen",
            "Ze hebben evenveel bezette schillen",
            "Ze hebben hetzelfde massagetal",
            "Ze hebben evenveel neutronen in de kern",
        ],
        0,
        "Het chemische gedrag wordt bepaald door de buitenste schil.",
    ),
    tabel(
        "Klopt dit over de relatieve en de absolute atoommassa?",
        [
            ("De relatieve atoommassa heeft geen eenheid.", J),
            ("Eén u is ongeveer de massa van één proton.", J),
            ("De absolute massa druk je uit in kilogram.", J),
            ("De relatieve atoommassa druk je uit in kilogram.", F),
        ],
        "Relatieve massa maal de waarde van u in kilogram geeft de absolute massa.",
    ),
    mk(
        "Waarom gaat een edelgas bijna geen bindingen aan?",
        [
            "Zijn buitenste schil is vol",
            "Het heeft geen elektronen",
            "Het heeft geen protonen in de kern",
            "Het is altijd een ion",
        ],
        0,
        "Dat is de edelgasconfiguratie: niets af te staan of op te nemen.",
    ),
    keuze(
        "De eerste schil is vol met [[*2|8|18]] elektronen, de tweede met 8.",
        "Daarom hebben helium en neon een volle buitenste schil.",
    ),
    klik(
        "Klik op een elektron in de schil die al vol is met twee elektronen.",
        BOHR.bestand, Z_SCHIL1,
        "De eerste schil, het dichtst bij de kern, is vol met twee elektronen.",
    ),
    inv(
        "Een atoom heeft 26 protonen en 30 neutronen. Wat is het massagetal?",
        ["56"],
        "Het massagetal telt de nucleonen: 26 plus 30 is 56.",
    ),
    tabel(
        "Wat weet je meteen als een element atoomnummer 17 heeft?",
        [
            ("De kern bevat 17 protonen.", J),
            ("Een neutraal atoom heeft 17 elektronen.", J),
            ("De kern bevat 17 neutronen.", F),
            ("Het massagetal is 17.", F),
        ],
        "Voor de neutronen en het massagetal heb je meer informatie nodig.",
    ),
    mk(
        "Een element staat in de derde kolom van de hoofdgroepen en in periode 3. Wat weet je over zijn atoom?",
        [
            "Drie valentie-elektronen en drie bezette schillen",
            "Drie valentie-elektronen en twee bezette schillen",
            "Twee valentie-elektronen en drie bezette schillen",
            "Acht valentie-elektronen en drie bezette schillen",
        ],
        0,
        "De kolom geeft de valentie-elektronen, de periode het aantal schillen. Het is aluminium.",
    ),
    keuze(
        "Een atoom en zijn ion hebben hetzelfde aantal [[*protonen|elektronen|ladingen]].",
        "Alleen de elektronen veranderen. Anders had je een ander element.",
    ),
    sorteer(
        "Staat dit element bij de metalen of de niet-metalen?",
        ["Metaal", "Niet-metaal"],
        [
            ["natrium", "Metaal"],
            ["magnesium", "Metaal"],
            ["kalium", "Metaal"],
            ["zuurstof", "Niet-metaal"],
            ["chloor", "Niet-metaal"],
            ["stikstof", "Niet-metaal"],
        ],
        "Metalen staan links en in het midden, niet-metalen rechtsboven.",
    ),
    open_(
        "Leg uit waarom natrium graag een ion met lading 1 plus vormt. Gebruik de woorden elektronenconfiguratie, valentie-elektron en edelgas.",
        "Natrium heeft elektronenconfiguratie 2, 8, 1: één valentie-elektron. Staat het dat ene elektron af, dan blijft 2, 8 over, dezelfde configuratie als het edelgas neon. Die volle buitenste schil is stabiel. Omdat er dan één proton meer is dan elektronen, krijgt het ion lading 1 plus.",
    ),
]
