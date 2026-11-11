"""De conjunctuur, conjunctuurindicatoren en de begroting — pittig (🌍 Beyond, economie)."""
import math

from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import venster, punt_zone

G = venster("conjunctuur-golf", 0, 12, 0, 10, 1, 1)
TREND = lambda t: 2 + 0.4 * t                                # noqa: E731
GOLF = lambda t: TREND(t) + 1.6 * math.sin(t * math.pi / 4)  # noqa: E731
_K = math.acos(-0.4 / (1.6 * math.pi / 4)) * 4 / math.pi        # top en dal van de golf (afgeleide nul)
PUNTEN = {k: (t, GOLF(t)) for k, t in {"A": _K, "B": 4, "C": 8 - _K, "D": 8}.items()}

GRAFIEKEN = [
    dict(naam=G, titel="Reëel bbp door de tijd: de conjunctuurgolf en de trend",
         krommen=[(TREND, "oranje", "trend", (0, 12)), (GOLF, "groen", "", (0, 12))],
         labelplek={"trend": (11, TREND(11) - 1.2)},
         punten=[(x, y, k) for k, (x, y) in PUNTEN.items()],
         xlabel="tijd", ylabel="reëel bbp", ijk_x=1, ijk_y=1),
]

PRENTEN = [dict(bestand=f"{G}.svg", zelf=True, wat=GRAFIEKEN[0]["titel"] + " (punten A tot D)", vragen="klikvragen over de fasen van de conjunctuur")]
P = f"{G}.svg"

VRAGEN = [
    klik(
        "Klik op het punt dat het hoogtepunt van de conjunctuur, de boom, voorstelt.",
        P, [punt_zone(G, *PUNTEN["A"])],
        "De boom is het hoogtepunt van de golf: punt A.",
    ),
    klik(
        "Klik op het punt dat het dieptepunt, de depressie, voorstelt.",
        P, [punt_zone(G, *PUNTEN["C"])],
        "De depressie is het dieptepunt van de golf: punt C.",
    ),
    met_prent(P, mk(
        "In welke fase zit de economie in punt B?",
        ["In de neergaande fase: recessie", "In de opgaande fase: expansie", "Op het hoogtepunt: boom", "Op het dieptepunt: depressie"],
        0,
        "Tussen de boom (A) en de depressie (C) daalt de activiteit: de neergaande fase.",
    )),
    met_prent(P, mk(
        "Wat stelt de oranje lijn voor?",
        ["De trend: de groeilijn op lange termijn", "Het potentieel bbp min het reëel bbp",
         "De conjunctuur: de schommelingen rond de groeilijn", "De werkloosheid door de tijd"],
        0,
        "De trend is de groeilijn op lange termijn; de conjunctuur zijn de schommelingen eromheen.",
    )),
    met_prent(P, volgorde(
        "Zet de fasen van de conjunctuur in de juiste volgorde, te beginnen bij de boom.",
        ["Boom", "Recessie", "Depressie", "Herstel"],
        "Na het hoogtepunt volgt de neergang, dan het dieptepunt en dan het herstel.",
    )),
    tabel(
        "Hoort dit bij de opgaande fase (expansie) of bij de neergaande fase (recessie)?",
        [
            ("Hoge investeringen", "Opgaande fase"),
            ("Stijgende werkloosheid", "Neergaande fase"),
            ("Meer faillissementen", "Neergaande fase"),
            ("Sterke groei van het bbp", "Opgaande fase"),
        ],
        "In de expansie groeit de economie sterk en daalt de werkloosheid; in de recessie omgekeerd.",
        kolommen=["Opgaande fase", "Neergaande fase"],
    ),
    tabel(
        "Is er een recessie volgens de definitie? Groei van het reëel bbp per kwartaal:",
        [
            ("+0,4 %, −0,2 %, −0,3 %", "Wel"),
            ("−0,5 %, +0,1 %, −0,2 %", "Niet"),
            ("+0,6 %, +0,2 %, +0,1 %", "Niet"),
        ],
        "Een recessie: het reëel bbp daalt twee kwartalen na elkaar. Bij de tweede reeks daalt het niet twee keer na elkaar.",
        kolommen=["Wel", "Niet"],
    ),
    mk(
        "Een leerling zegt: 'Tijdens een hoogconjunctuur dalen de investeringen.' Wat klopt?",
        ["Fout: tijdens een hoogconjunctuur stijgen de investeringen meestal",
         "Juist: bedrijven sparen dan hun winst op voor de slechtere tijden die komen",
         "Fout: de investeringen blijven in elke fase van de conjunctuur ongeveer gelijk",
         "Juist: bij een boom is er altijd onderbesteding, dus bedrijven hebben geen reden om te investeren"],
        0,
        "In de opgaande fase en de boom investeren bedrijven veel.",
    ),
    casus(
        "Het potentieel bbp van een land is 640 miljard euro.",
        [
            inv("Het reëel bbp is 610 miljard. Hoe groot is de outputkloof in miljard euro? Zet een minteken als ze negatief is.", "-30",
                "Reëel min potentieel = 610 − 640 = −30."),
            mk("Hoe heet die situatie?", ["Onderbesteding", "Overbesteding", "Bestedingsevenwicht", "Stagflatie"], 0,
               "Een negatieve outputkloof: de vraag is kleiner dan wat de economie kan produceren."),
            mk("Een jaar later is het reëel bbp 660 miljard en het potentieel bbp nog altijd 640. Wat verwacht je?",
               ["Prijsstijgingen, want de vraag is groter dan de productiecapaciteit", "Dalende prijzen, want er is onderbesteding in de economie",
                "Meer werkloosheid, want de outputkloof is nu negatief geworden", "Niets, want het verschil met het potentieel bbp is maar klein"], 0,
               "Een positieve outputkloof wijst op overbesteding, met prijsstijgingen tot gevolg."),
        ],
    ),
    tabel(
        "Exogene of endogene verklaring van een conjunctuurschommeling?",
        [
            ("Een pandemie legt de economie stil", "Exogeen"),
            ("Bedrijven investeerden te veel en moeten nu afbouwen", "Endogeen"),
            ("Een oorlog doet de olieprijs fors stijgen", "Exogeen"),
        ],
        "Exogeen: van buiten de economie. Endogeen: binnen de economie zelf.",
        kolommen=["Exogeen", "Endogeen"],
    ),
    tabel(
        "Is deze indicator voorlopend, gelijklopend of achterlopend?",
        [
            ("Het consumentenvertrouwen", "Voorlopend"),
            ("De industriële productie", "Gelijklopend"),
            ("Het ondernemersvertrouwen", "Voorlopend"),
        ],
        "Vertrouwen en beurs veranderen voor de economie, de industriële productie samen ermee.",
        kolommen=["Voorlopend", "Gelijklopend", "Achterlopend"],
    ),
    sorteer(
        "Is deze indicator kwalitatief of kwantitatief?",
        ["Kwalitatief", "Kwantitatief"],
        [
            ["Het consumentenvertrouwen", "Kwalitatief"],
            ["Het aantal faillissementen", "Kwantitatief"],
            ["Het ondernemersvertrouwen", "Kwalitatief"],
            ["De industriële productie", "Kwantitatief"],
        ],
        "Kwalitatief: verwachtingen en gevoelens, via enquêtes. Kwantitatief: iets tellen.",
    ),
    mk(
        "Het ondernemersvertrouwen daalt sterk. Wat verwacht je de komende maanden?",
        ["Minder investeringen en minder groei", "Een sterke daling van de werkloosheid",
         "Meer investeringen, omdat bedrijven willen inhalen", "Niets: vertrouwen heeft geen invloed op de economie"],
        0,
        "Het ondernemersvertrouwen is een voorlopende indicator.",
    ),
    mk(
        "Waarom is de werkloosheid een achterlopende indicator?",
        ["Bedrijven ontslaan pas mensen als de economie al een tijd verslechterd is",
         "De werkloosheid wordt maar één keer per tien jaar gemeten door de overheid",
         "Werklozen merken als eersten dat er een crisis aankomt en melden dat",
         "De werkloosheid daalt altijd tijdens een recessie, en stijgt in een boom"],
        0,
        "De werkloosheid verandert na de economie, niet ervoor.",
    ),
    casus(
        "Een overheid ontvangt 312 miljard euro en geeft 330 miljard euro uit.",
        [
            inv("Hoe groot is het begrotingssaldo in miljard euro? Zet een minteken als het negatief is.", "-18",
                "Inkomsten min uitgaven = 312 − 330 = −18."),
            mk("Wat gebeurt er met de staatsschuld?", ["Ze stijgt, want de overheid moet het tekort lenen", "Ze daalt met 18 miljard, want de overheid gaf minder uit",
                                                       "Ze blijft gelijk, want het tekort is maar tijdelijk", "Ze verdwijnt, want de ECB betaalt het tekort terug"], 0,
               "Een tekort moet de overheid lenen."),
            mk("Er komt een recessie. Wat gebeurt er met het saldo?",
               ["Het verslechtert: minder belastinginkomsten en meer uitkeringen", "Het verbetert: de overheid spaart meer in moeilijke tijden",
                "Het blijft gelijk: de begroting ligt voor het hele jaar vast", "Het verbetert: er zijn minder werklozen die een uitkering krijgen"], 0,
               "In een recessie dalen de belastinginkomsten en stijgen de uitkeringen."),
        ],
    ),
    tabel(
        "Welk soort overheidsinkomen is dit?",
        [
            ("De personenbelasting", "Directe belasting"),
            ("De btw", "Indirecte belasting"),
            ("Bijdragen voor de sociale zekerheid", "Sociale bijdrage"),
            ("De verkoop van een overheidsgebouw", "Niet-fiscaal"),
            ("De vennootschapsbelasting", "Directe belasting"),
        ],
        "Direct: op inkomen of winst. Indirect: op goederen. De verkoop van een gebouw is geen belasting.",
        kolommen=["Directe belasting", "Indirecte belasting", "Sociale bijdrage", "Niet-fiscaal"],
    ),
    keuze(
        "Het potentieel bbp is wat de economie [[*normaal kan produceren|dit jaar werkelijk produceerde]]. De outputkloof is het reëel bbp [[*min|plus]] het potentieel bbp.",
        "Een negatieve outputkloof wijst op onderbesteding.",
    ),
    mk(
        "Wat is een crisis in de conjunctuur?",
        ["Een plotse en scherpe omslag naar een neergang", "Het hoogtepunt van de golf, met hoogconjunctuur en overbesteding",
         "Een lange periode van sterke groei en dalende werkloosheid", "Het moment waarop de groei na het dieptepunt terugkomt"],
        0,
        "Een crisis is de plotse omslag; het dieptepunt heet depressie.",
    ),
    sleep(
        "De [[trend]] is de groeilijn op lange termijn. De [[conjunctuur]] zijn de schommelingen van de economische activiteit rond die groeilijn.",
        ["begroting", "inflatie"],
        "Een conjunctuurgolf beweegt rond de trend.",
    ),
    open_(
        "Leg uit waarom het begrotingssaldo van een overheid verslechtert tijdens een recessie, ook al verandert de overheid niets aan haar beleid.",
        "In een recessie verdienen mensen en bedrijven minder, dus ontvangt de overheid minder belastingen. Tegelijk stijgt de werkloosheid, dus betaalt ze meer uitkeringen. Minder inkomsten en meer uitgaven: het saldo verslechtert.",
    ),
    inv(
        "Het reëel bbp is 505 miljard en het potentieel bbp 500 miljard euro. Hoe groot is de outputkloof in miljard euro? Schrijf enkel het getal.",
        "5",
        "505 − 500 = +5: een positieve outputkloof, overbesteding.",
    ),
    tabel(
        "Onderbesteding, bestedingsevenwicht of overbesteding?",
        [
            ("De vraag is kleiner dan wat de economie kan produceren", "Onderbesteding"),
            ("De vraag is groter dan de productiecapaciteit", "Overbesteding"),
            ("De outputkloof is ongeveer nul", "Bestedingsevenwicht"),
        ],
        "Negatieve outputkloof: onderbesteding. Positieve: overbesteding.",
        kolommen=["Onderbesteding", "Bestedingsevenwicht", "Overbesteding"],
    ),
    mk(
        "Welke uitgave is een overheidsuitgave?",
        ["De lonen van leerkrachten", "De btw op een nieuwe auto", "De vennootschapsbelasting", "De sociale bijdragen van werknemers"],
        0,
        "De andere drie zijn overheidsinkomsten.",
    ),
    mk(
        "Beursindices stijgen sterk, terwijl de economie nog in een dieptepunt zit. Hoe verklaar je dat?",
        ["Beursindices zijn voorlopend: ze stijgen vaak al voor de economie zich herstelt",
         "Beursindices zijn achterlopend: ze reageren nu pas op de boom van enkele jaren geleden",
         "Beursindices hebben niets met de economie te maken, enkel met speculanten",
         "Beursindices stijgen altijd tijdens een depressie, omdat aandelen dan goedkoop zijn"],
        0,
        "Beleggers kijken vooruit en kopen al aandelen als ze herstel verwachten.",
    ),
    keuze(
        "Tijdens een recessie [[*stijgt|daalt]] de werkloosheid en [[*nemen|dalen]] de faillissementen toe.",
        "In de neergaande fase daalt het reëel bbp.",
    ),
    koppel(
        "Koppel elke fase aan haar omschrijving.",
        [
            ["Boom", "Het hoogtepunt, soms met overbesteding"],
            ["Depressie", "Het dieptepunt"],
            ["Herstel", "De groei komt terug na het dieptepunt"],
        ],
        ["Het potentieel bbp stijgt plots sterk"],
        "Een plotse, scherpe omslag naar een neergang heet een crisis.",
    ),
]
