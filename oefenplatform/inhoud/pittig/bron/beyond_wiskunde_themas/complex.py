"""Complexe getallen — pittig (🌍 Beyond doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik, met_prent
from .prentmaat import venster, punt_zone, vak_zone

GRAF = venster("complex-gauss-bey", -4, 4, -4, 4)

GRAFIEKEN = [
    dict(naam=GRAF, titel="Het vlak van Gauss met het getal z = 3 + 2i",
         krommen=[], punten=[(3, 2, "z")], xlabel="Re", ylabel="Im"),
]
PRENTEN = [dict(bestand=f"{GRAF}.svg", zelf=True, wat="vlak van Gauss met het punt 3 + 2i", vragen="klikvragen over toegevoegde, tegengestelde en draaiing")]

VRAGEN = [
    klik(
        r"Klik op het punt dat \(i \cdot z\) voorstelt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, -2, 3)],
        r"\(i(3 + 2i) = 3i + 2i^{2} = -2 + 3i\): een kwart slag tegen de klok in.",
    ),
    klik(
        r"Klik op het punt dat \(\overline{z}\) voorstelt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, 3, -2)],
        r"De toegevoegde heeft hetzelfde reëel deel en het tegengestelde imaginair deel.",
    ),
    klik(
        r"Klik op het punt dat \(-z\) voorstelt.",
        f"{GRAF}.svg",
        [punt_zone(GRAF, -3, -2)],
        r"Het tegengestelde is gespiegeld door de oorsprong.",
    ),
    met_prent(f"{GRAF}.svg", tabel(
        r"Kijk naar het punt \(z\) in het vlak van Gauss. Juist of fout?",
        [(r"\(|z| = \sqrt{13}\)", J), (r"Het argument van \(z\) ligt tussen \(0^\circ\) en \(90^\circ\).", J), (r"\(z + \overline{z}\) ligt op de imaginaire as.", F), (r"\(z \cdot \overline{z} = 13\)", J)],
        r"\(z + \overline{z} = 2\,\mathrm{Re}(z) = 6\) ligt op de reële as.",
        kolommen=["Juist", "Fout"],
    )),
    mk(
        r"Bereken \((2 + 3i)(1 - i)\).",
        [r"\(5 + i\)", r"\(-1 + i\)", r"\(2 - 3i\)", r"\(5 - i\)"],
        0,
        r"\(2 - 2i + 3i - 3i^{2} = 2 + i + 3\).",
    ),
    mk(
        r"Bereken \(\dfrac{3 + i}{1 - i}\).",
        [r"\(1 + 2i\)", r"\(2 + i\)", r"\(\tfrac{3}{2} + \tfrac{1}{2}i\)", r"\(1 - 2i\)"],
        0,
        r"Vermenigvuldig met \(1 + i\): \(\tfrac{(3 + i)(1 + i)}{2} = \tfrac{2 + 4i}{2}\).",
    ),
    inv(
        r"Schrijf \(i^{2027}\) zo eenvoudig mogelijk.",
        ["-i", "−i", "min i"],
        r"\(2027 = 4 \cdot 506 + 3\), dus \(i^{2027} = i^{3}\).",
    ),
    inv(
        r"Bereken \((1 + i)^{8}\). Schrijf het getal.",
        ["16", "zestien"],
        r"\((1 + i)^{2} = 2i\), dus \((1 + i)^{8} = (2i)^{4} = 16\).",
    ),
    casus(
        r"Neem \(w = 1 + i\sqrt{3}\).",
        [
            inv(r"Hoeveel is \(|w|\)?", ["2", "twee"], r"\(\sqrt{1 + 3}\)."),
            mk(r"Wat is het argument van \(w\)?", [r"\(60^\circ\)", r"\(30^\circ\)", r"\(45^\circ\)", r"\(120^\circ\)"], 0, r"\(\tan\theta = \sqrt{3}\) en \(w\) ligt in het eerste kwadrant."),
            inv(r"Bereken \(w^{6}\) met de formule van de Moivre.", ["64"], r"\(2^{6}(\cos 360^\circ + i\sin 360^\circ) = 64\)."),
        ],
    ),
    tabel(
        r"Is het een oplossing van \(z^{3} = 8\)?",
        [(r"\(2\)", J), (r"\(-2\)", F), (r"\(-1 + i\sqrt{3}\)", J), (r"\(-1 - i\sqrt{3}\)", J), (r"\(2i\)", F)],
        r"De drie oplossingen hebben modulus 2 en argumenten \(0^\circ\), \(120^\circ\) en \(240^\circ\).",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Wat zijn de oplossingen van \(x^{2} + 4x + 13 = 0\)?",
        [r"\(-2 \pm 3i\)", r"\(2 \pm 3i\)", r"\(-2 \pm 9i\)", r"\(-4 \pm 6i\)"],
        0,
        r"\(D = 16 - 52 = -36\), dus \(x = \tfrac{-4 \pm 6i}{2}\).",
    ),
    mk(
        r"Een veelterm met reële coëfficiënten heeft \(2 + i\) als nulwaarde. Welke tweedegraadsfactor zit er zeker in?",
        [r"\(x^{2} - 4x + 5\)", r"\(x^{2} + 4x + 5\)", r"\(x^{2} - 4x + 3\)", r"\(x^{2} + 1\)"],
        0,
        r"Ook \(2 - i\) is nulwaarde: \((x - 2)^{2} + 1\).",
    ),
    koppel(
        "Verbind de bewerking met wat ze doet in het vlak van Gauss.",
        [(r"vermenigvuldigen met \(i\)", "een kwart slag draaien rond de oorsprong"), (r"de toegevoegde nemen", "spiegelen om de reële as"), (r"vermenigvuldigen met \(2\)", "uitrekken vanuit de oorsprong"), (r"\(1 + i\) optellen", "verschuiven")],
        ["spiegelen om de imaginaire as"],
        "Elke bewerking is een meetkundige transformatie.",
    ),
    inv(
        r"Bepaal \(z\) als \(z + 2\overline{z} = 3 - i\). Schrijf in de vorm \(a + bi\).",
        ["1+i", "1 + i"],
        r"Met \(z = a + bi\): \(3a - bi = 3 - i\), dus \(a = 1\) en \(b = 1\).",
    ),
    sorteer(
        "In welk kwadrant ligt het getal?",
        ["Eerste", "Tweede", "Derde", "Vierde"],
        [(r"\(i(1 + i)\)", "Tweede"), (r"\((1 - i)^{2} - 1\)", "Derde"), (r"\(\overline{2 + 5i}\)", "Vierde"), (r"\(\dfrac{1}{1 - i}\)", "Eerste"), (r"\(-3 - i\)", "Derde"), (r"\(4 + i\)", "Eerste")],
        r"Reken eerst uit: \(i(1 + i) = -1 + i\) en \((1 - i)^{2} - 1 = -1 - 2i\).",
    ),
    keuze(
        r"Bij het vermenigvuldigen in goniometrische vorm [[*vermenigvuldig|tel je op|deel]] je de moduli en [[*tel je op|vermenigvuldig|trek je af]] de argumenten.",
        "Daarom is de goniometrische vorm zo handig bij machten.",
    ),
    tabel(
        "Juist of fout voor alle complexe getallen?",
        [(r"\(|z_{1}z_{2}| = |z_{1}| \cdot |z_{2}|\)", J), (r"\(|z_{1} + z_{2}| = |z_{1}| + |z_{2}|\)", F), (r"\(\overline{z_{1}z_{2}} = \overline{z_{1}} \cdot \overline{z_{2}}\)", J), (r"\(z^{2} \geq 0\)", F)],
        r"Voor \(z = i\) is \(z^{2} = -1\); complexe getallen kan je bovendien niet ordenen.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        r"Wat is de goniometrische vorm van \(1 - i\)?",
        [r"\(\sqrt{2}\left(\cos(-45^\circ) + i\sin(-45^\circ)\right)\)", r"\(\sqrt{2}\left(\cos(-135^\circ) + i\sin(-135^\circ)\right)\)", r"\(2\left(\cos(-45^\circ) + i\sin(-45^\circ)\right)\)", r"\(\sqrt{2}\left(\cos 135^\circ + i\sin 135^\circ\right)\)"],
        0,
        r"\(r = \sqrt{2}\) en het punt ligt in het vierde kwadrant.",
    ),
    inv(
        r"Hoeveel is \(|(2 - i)^{2}|\)? Schrijf het getal.",
        ["5", "vijf"],
        r"\(|2 - i|^{2} = 5\). Je kan ook uitrekenen: \(3 - 4i\) heeft modulus 5.",
    ),
    volgorde(
        r"Zet de stappen om \(z^{4} = 16\) op te lossen in volgorde.",
        [r"schrijf 16 in goniometrische vorm: modulus 16, argument \(0^\circ\)", r"neem de vierdemachtswortel van de modulus: 2", r"deel het argument door 4 en tel telkens \(90^\circ\) bij", r"schrijf de vier oplossingen: \(2,\ 2i,\ -2,\ -2i\)"],
        "De n oplossingen liggen gelijk verdeeld op een cirkel.",
    ),
    mk(
        r"Waar liggen de vijf oplossingen van \(z^{5} = 1\)?",
        ["op de eenheidscirkel, telkens 72° uit elkaar", "op de reële as", "op een cirkel met straal 5", "op de eenheidscirkel, telkens 90° uit elkaar"],
        0,
        r"\(360^\circ : 5 = 72^\circ\).",
    ),
    sleep(
        r"Het getal \(a + bi\) heeft reëel deel [[a]] en imaginair deel [[b]]. De modulus is [[\(\sqrt{a^{2} + b^{2}}\)]].",
        ["bi", r"\(a + b\)"],
        "Het imaginair deel is een reëel getal, zonder i.",
    ),
    mk(
        r"Welke vergelijking heeft \(3i\) en \(-3i\) als oplossingen?",
        [r"\(x^{2} + 9 = 0\)", r"\(x^{2} - 9 = 0\)", r"\(x^{2} + 3 = 0\)", r"\(x^{2} + 6x + 9 = 0\)"],
        0,
        r"\((x - 3i)(x + 3i) = x^{2} + 9\).",
    ),
    tabel(
        "Zuiver reëel, zuiver imaginair of geen van beide?",
        [(r"\((1 - i)^{2}\)", "zuiver imaginair"), (r"\((1 + i)(1 - i)\)", "zuiver reëel"), (r"\(i(2 + i)\)", "geen van beide"), (r"\(i^{6}\)", "zuiver reëel")],
        r"\((1 - i)^{2} = -2i\), \((1 + i)(1 - i) = 2\), \(i(2 + i) = -1 + 2i\), \(i^{6} = -1\).",
        kolommen=["zuiver reëel", "zuiver imaginair", "geen van beide"],
    ),
    inv(
        r"Schrijf \(\dfrac{1}{i}\) zo eenvoudig mogelijk.",
        ["-i", "−i", "min i"],
        r"Vermenigvuldig teller en noemer met \(-i\): \(\tfrac{-i}{-i^{2}} = \tfrac{-i}{1}\).",
    ),
    mk(
        r"\(z_{1} = 2(\cos 30^\circ + i\sin 30^\circ)\) en \(z_{2} = 3(\cos 60^\circ + i\sin 60^\circ)\). Hoeveel is \(z_{1}z_{2}\)?",
        [r"\(6i\)", r"\(5i\)", r"\(6\)", r"\(6(\cos 1800^\circ + i\sin 1800^\circ)\)"],
        0,
        r"Moduli maal elkaar: 6. Argumenten opgeteld: \(90^\circ\).",
    ),
    mk(
        r"Bereken \(\dfrac{6(\cos 100^\circ + i\sin 100^\circ)}{2(\cos 40^\circ + i\sin 40^\circ)}\).",
        [r"\(3(\cos 60^\circ + i\sin 60^\circ)\)", r"\(4(\cos 60^\circ + i\sin 60^\circ)\)", r"\(3(\cos 140^\circ + i\sin 140^\circ)\)", r"\(3(\cos 2{,}5^\circ + i\sin 2{,}5^\circ)\)"],
        0,
        r"Moduli delen, argumenten aftrekken.",
    ),
    inv(
        r"Hoeveel nulwaarden van \(x^{3} - 1\) zijn niet reëel? Schrijf het cijfer.",
        ["2", "twee"],
        r"\(x^{3} - 1 = (x - 1)(x^{2} + x + 1)\) en de tweede factor heeft \(D = -3 < 0\).",
    ),
]
