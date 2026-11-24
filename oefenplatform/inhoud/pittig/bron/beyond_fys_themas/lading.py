"""Elektrische lading, geleiders en influentie — pittig (🔭 Beyond doorstroom, fysica)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Influentie op een metalen bol ------------------------------------------------
IB = Prent("influentie-bol", "Een negatief geladen staaf bij een neutrale metalen bol", "links een staaf met mintekens, in het midden een metalen bol op een isolerende voet met de letters P (dichtste kant) en Q (verste kant), rechts een draad naar de aarde met een schakelaar S")
IB.rect(40, 250, 230, 60, "#d9d2c3", DONKER, 10, 2)
for x in range(70, 260, 40):
    IB.tekst(x, 290, "−", 34, kleur=BLAUW, vet=True)
IB.cirkel(520, 280, 140, "#cfd8e3", DONKER, 3)
IB.rect(505, 420, 30, 120, "#f3e3c8", DONKER, 4, 2)
IB.tekst(520, 575, "isolerende voet", 18)
IB.letter(420, 280, "P")
IB.letter(620, 280, "Q")
IB.lijn(660, 280, 760, 280, DONKER, 3)
IB.lijn(760, 280, 800, 255, DONKER, 3)
IB.cirkel(760, 280, 6, DONKER, DONKER, 1)
IB.cirkel(805, 280, 6, DONKER, DONKER, 1)
IB.letter(782, 220, "S")
IB.lijn(805, 280, 880, 280, DONKER, 3)
IB.lijn(880, 280, 880, 420, DONKER, 3)
for i, b in enumerate((70, 46, 22)):
    IB.lijn(880 - b / 2, 420 + i * 14, 880 + b / 2, 420 + i * 14, DONKER, 3)
IB.tekst(880, 490, "aarde", 18)
ZP = [Prent.rond(440, 280, 70), Prent.rond(420, 280, 26)]
ZQ = [Prent.rond(600, 280, 70), Prent.rond(620, 280, 26)]
ZS = [Prent.zone(740, 190, 90, 110)]

# Tribo-elektrische reeks ---------------------------------------------------------
TR = Prent("tribo-reeks", "Een tribo-elektrische reeks", "verticale lijst van stoffen: bovenaan geeft makkelijk elektronen af, onderaan neemt makkelijk elektronen op: glas, haar, wol, zijde, katoen, pvc, teflon")
STOF = ["glas", "haar", "wol", "zijde", "katoen", "pvc", "teflon"]
TR.tekst(500, 85, "geeft makkelijk elektronen af", 20, kleur=ROOD, vet=True)
for i, s in enumerate(STOF):
    TR.rect(380, 105 + i * 64, 240, 50, "#ffffff", DONKER, 12, 2)
    TR.tekst(500, 138 + i * 64, s, 24)
TR.tekst(500, 580, "neemt makkelijk elektronen op", 20, kleur=BLAUW, vet=True)
TR.pijl(680, 110, 680, 540, DONKER, 3)
ZT = {s: [Prent.zone(380, 105 + i * 64, 240, 50)] for i, s in enumerate(STOF)}

VRAGEN = [
    klik(
        "Klik op de kant van de bol waar de vrije elektronen naartoe geduwd worden.",
        IB.bestand, ZQ,
        "Gelijke ladingen stoten af: de elektronen vluchten weg van de negatieve staaf, naar de verste kant.",
    ),
    klik(
        "Klik op de kant van de bol die positief wordt, zolang de staaf in de buurt blijft.",
        IB.bestand, ZP,
        "Daar ontbreken nu elektronen. De bol als geheel blijft neutraal.",
    ),
    met_prent(IB.bestand, volgorde(
        "Zet de handelingen in de goede volgorde om de bol blijvend positief te laden.",
        [
            "Staaf bij de bol houden",
            "Schakelaar S sluiten",
            "Schakelaar S weer openen",
            "Staaf weghalen",
        ],
        "Eerst de aarding verbreken, pas dan de staaf weg: anders lopen de elektronen terug.",
    )),
    met_prent(IB.bestand, keuze(
        "Als S gesloten is, lopen er elektronen [[*van de bol naar de aarde|van de aarde naar de bol]].",
        "De staaf duwt de elektronen zo ver mogelijk weg, tot in de aarde.",
    )),
    met_prent(IB.bestand, tabel(
        "Wat is de totale lading van de bol in deze situatie?",
        [
            ("staaf in de buurt, S altijd open", "Nul"),
            ("staaf in de buurt, S gesloten en daarna geopend, staaf weg", "Positief"),
            ("staaf raakt de bol even aan", "Negatief"),
        ],
        "Influentie alleen verschuift lading; aarden of aanraken verandert de totale lading.",
        kolommen=["Nul", "Positief", "Negatief"],
    )),
    met_prent(IB.bestand, mk(
        "Je vervangt de metalen bol door een even grote bol uit glas. Wat gebeurt er nu bij de staaf?",
        [
            "De moleculen polariseren een beetje",
            "Alle elektronen schuiven naar de verste kant",
            "De bol wordt meteen blijvend negatief",
            "Er gebeurt in het glas helemaal niets",
        ],
        0,
        "In een isolator zitten de elektronen vast; elke molecule wordt hooguit een kleine dipool.",
    )),
    klik(
        "Je wrijft wol met pvc. Klik op de stof die negatief geladen wordt.",
        TR.bestand, ZT["pvc"],
        "Pvc staat lager: het neemt makkelijker elektronen op dan wol.",
    ),
    klik(
        "Je wrijft zijde met glas. Klik op de stof die positief geladen wordt.",
        TR.bestand, ZT["glas"],
        "Glas staat hoger en geeft dus elektronen af aan de zijde.",
    ),
    met_prent(TR.bestand, tabel(
        "Welke stof wordt negatief als je deze twee tegen elkaar wrijft?",
        [
            ("haar en teflon", "De tweede"),
            ("katoen en wol", "De eerste"),
            ("glas en zijde", "De tweede"),
        ],
        "De stof die lager in de reeks staat, neemt de elektronen op.",
        kolommen=["De eerste", "De tweede"],
    )),
    met_prent(TR.bestand, mk(
        "Na het wrijven van wol met teflon draagt het teflon −6 nC. Welke lading draagt de wol?",
        ["+6 nC", "−6 nC", "0 nC", "+12 nC"],
        0,
        "Lading verhuist alleen: Q₁ + Q₂ = 0.",
    )),
    inv(
        "Een staaf heeft 2,5 · 10¹¹ elektronen te weinig. Hoe groot is de lading in nC? Neem e = 1,6 · 10⁻¹⁹ C.",
        ["40", "+40", "40 nC", "+40 nC"],
        "Q = n · e = 2,5 · 10¹¹ · 1,6 · 10⁻¹⁹ C = 4,0 · 10⁻⁸ C = +40 nC. Te weinig elektronen geeft een positieve lading.",
    ),
    inv(
        "Een bolletje draagt −0,32 nC. Hoeveel elektronen heeft het te veel? Neem e = 1,6 · 10⁻¹⁹ C. Geef het getal als macht van tien.",
        ["2 · 10⁹", "2·10⁹", "2*10^9", "2e9", "2000000000", "2,0 · 10⁹"],
        "n = Q / e = 0,32 · 10⁻⁹ / 1,6 · 10⁻¹⁹ = 2 · 10⁹.",
    ),
    mk(
        "Welke lading kan een voorwerp onmogelijk dragen?",
        ["2,4 · 10⁻¹⁹ C", "3,2 · 10⁻¹⁹ C", "4,8 · 10⁻¹⁹ C", "1,6 · 10⁻¹⁸ C"],
        0,
        "2,4 · 10⁻¹⁹ C is anderhalve keer e, en lading komt altijd in hele pakjes e.",
    ),
    mk(
        "Twee gelijke metalen bollen dragen +18 nC en −6 nC. Ze raken elkaar even. Welke lading draagt elke bol daarna?",
        ["+6 nC", "+12 nC", "+9 nC", "−6 nC"],
        0,
        "Samen +12 nC, gelijk verdeeld over twee gelijke bollen: elk +6 nC.",
    ),
    mk(
        "Drie gelijke bollen: A draagt +27 nC, B en C zijn neutraal. A raakt eerst B, daarna raakt A ook C. Wat draagt A op het einde?",
        ["+6,75 nC", "+9 nC", "+13,5 nC", "+4,5 nC"],
        0,
        "Na B: elk +13,5 nC. Daarna A met C: (13,5 + 0) / 2 = +6,75 nC.",
    ),
    tabel(
        "Geleider of isolator?",
        [
            ("aluminiumfolie", "Geleider"),
            ("een pvc-buis", "Isolator"),
            ("een koperdraad", "Geleider"),
            ("een glazen staaf", "Isolator"),
        ],
        "Metalen hebben vrije elektronen, kunststof en glas niet.",
        kolommen=["Geleider", "Isolator"],
    ),
    sorteer(
        "Verschuift de lading door het hele voorwerp, of enkel binnen de moleculen?",
        ["Door het hele voorwerp", "Binnen de moleculen"],
        [
            ("een koperen bol bij een geladen staaf", "Door het hele voorwerp"),
            ("een stukje papier bij een geladen kam", "Binnen de moleculen"),
            ("een plastic rietje bij een geladen ballon", "Binnen de moleculen"),
            ("een aluminium blikje bij een geladen ballon", "Door het hele voorwerp"),
        ],
        "In een geleider bewegen vrije elektronen; in een isolator polariseren de moleculen.",
    ),
    casus(
        "Een elektroscoop is neutraal. Je brengt een positief geladen staaf dicht bij de bovenste knop, zonder te raken.",
        [
            mk(
                "Wat gebeurt er met de blaadjes?",
                [
                    "Ze wijken uit, want ze worden allebei positief",
                    "Ze blijven hangen, want er is geen contact",
                    "Ze wijken uit, want ze worden allebei negatief",
                    "Eén blaadje wordt positief en het andere negatief",
                ],
                0,
                "Elektronen worden naar de knop getrokken, dus onderaan ontbreken er elektronen.",
            ),
            keuze(
                "Haal je de staaf weer weg, dan [[*vallen de blaadjes terug|blijven de blaadjes open]].",
                "Er is niets toegevoegd of weggenomen: de lading verdeelt zich terug.",
            ),
            mk(
                "Wat moet je doen opdat de elektroscoop daarna blijvend negatief is?",
                [
                    "Even aarden terwijl de staaf er is",
                    "De staaf eerst weghalen en dan aarden",
                    "De knop raken met de positieve staaf",
                    "De blaadjes even aanraken met de vinger",
                ],
                0,
                "Uit de aarde komen elektronen bij, aangetrokken door de positieve staaf.",
            ),
        ],
    ),
    tabel(
        "Klopt deze uitspraak?",
        [
            ("Bij wrijven ontstaat er nieuwe lading.", F),
            ("Een neutraal voorwerp bevat evenveel protonen als elektronen.", J),
            ("Protonen verhuizen bij het laden van een vaste stof.", F),
            ("Na influentie zonder aarding is de totale lading nul.", J),
        ],
        "Lading verhuist, ze ontstaat niet. In vaste stoffen bewegen alleen elektronen.",
    ),
    koppel(
        "Koppel elke manier van laden aan wat er gebeurt.",
        [
            ("wrijving", "elektronen gaan van de ene stof naar de andere"),
            ("contact", "de lading verdeelt zich over beide voorwerpen"),
            ("influentie", "de lading verschuift zonder aanraking"),
        ],
        ["de protonen springen over"],
        "Bij influentie met aarding wordt het voorwerp tegengesteld geladen.",
    ),
    sleep(
        "Laden door contact geeft het voorwerp [[dezelfde]] soort lading als de staaf. Laden door influentie met aarding geeft een [[tegengestelde]] lading. Een stukje papier wordt aangetrokken door [[polarisatie]].",
        ["geen", "wrijving"],
        "Aarden laat elektronen weg of bij, aanraken deelt de lading.",
    ),
    mk(
        "Waarom trekt een geladen ballon een neutraal stukje papier aan?",
        [
            "De dichtste kant wordt tegengesteld",
            "Het papier wordt door de lucht geladen",
            "Het papier krijgt dezelfde lading als de ballon",
            "Neutrale stoffen worden altijd door alles aangetrokken",
        ],
        0,
        "Na polarisatie ligt de tegengestelde lading het dichtst, en die aantrekking wint.",
    ),
    tabel(
        "Berust deze toepassing op elektrostatica?",
        [
            ("poedercoating van een fietsframe", "Ja"),
            ("een fotokopieertoestel", "Ja"),
            ("een stoffilter in een schoorsteen", "Ja"),
            ("een fietsdynamo", "Nee"),
        ],
        "Een dynamo werkt met inductie, niet met stilstaande lading.",
        kolommen=["Ja", "Nee"],
    ),
    keuze(
        "Een staaf van 3 nC is [[*3 · 10⁻⁹ C|3 · 10⁻⁶ C|3 · 10⁻³ C]].",
        "Nano is 10⁻⁹, micro 10⁻⁶, milli 10⁻³.",
    ),
    open_(
        "Leg uit waarom je een metalen staaf die je in je hand houdt niet kan laden door wrijving, maar een pvc-staaf wel.",
        "Metaal is een geleider: de lading verspreidt zich meteen over de staaf en loopt via je hand en lichaam weg naar de aarde. Pvc is een isolator: de elektronen blijven zitten op de plek waar ze terechtkwamen, dus de staaf blijft geladen.",
    ),
    klik(
        "Klik op het onderdeel dat je moet openen vóór je de staaf weghaalt.",
        IB.bestand, ZS,
        "Blijft de aarding verbonden, dan lopen de elektronen terug en is de bol weer neutraal.",
    ),
    met_prent(TR.bestand, tabel(
        "Je wrijft wol met deze stof. Welke lading krijgt de wol?",
        [
            ("glas", "Negatief"),
            ("pvc", "Positief"),
            ("teflon", "Positief"),
        ],
        "Wol neemt elektronen op van stoffen die hoger staan en geeft ze af aan stoffen die lager staan.",
        kolommen=["Positief", "Negatief"],
    )),
    inv(
        "Twee gelijke metalen bollen raken elkaar even. De ene droeg +10 nC. Daarna draagt elke bol +2 nC. Hoeveel nC droeg de andere bol?",
        ["-6", "−6", "-6 nC", "−6 nC"],
        "Samen 2 · 2 = +4 nC, dus de andere droeg 4 − 10 = −6 nC.",
    ),
]
