"""Tekstverwerking met Word — pittig
(🌍 Beyond doorstroom, samenleving en economie). Eigen vragen en een eigen schermafdruk
van een pagina, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Een bladzijde met zes delen, de tekst als grijze balkjes ----------------------------
WP = Prent("word-bladzijde", "Een bladzijde in Word (verkleind)", "een staande bladzijde met zes delen A tot F: A een smalle balk helemaal bovenaan; B een korte, vette regel in het midden; C een alinea waarvan de rechterkant rafelig is; D een alinea waarvan links en rechts recht zijn; E een alinea waarvan alleen de eerste regel verder naar rechts begint; F een smalle balk helemaal onderaan met '3' in het midden")
WP.rect(300, 50, 400, 580, "#ffffff", DONKER, 2, 2)
L, R = 350, 650
WP.lijn(L, 58, R, 58, "#e4e1d6", 1, True)
WP.rect(L, 70, 160, 10, GRIJS, GRIJS, 2, 0)                      # A koptekst
WP.rect(430, 120, 140, 16, DONKER, DONKER, 2, 0)                  # B titel gecentreerd
for i, b in enumerate((300, 270, 290, 230, 140)):                 # C links uitgelijnd
    WP.rect(L, 170 + i * 18, b, 8, GRIJS, GRIJS, 2, 0)
for i in range(5):                                                # D uitgevuld
    WP.rect(L, 290 + i * 18, 300 if i < 4 else 120, 8, GRIJS, GRIJS, 2, 0)
for i, (x, b) in enumerate(((390, 260), (L, 300), (L, 285), (L, 296), (L, 170))):   # E eerste regel inspringen
    WP.rect(x, 410 + i * 18, b, 8, GRIJS, GRIJS, 2, 0)
WP.lijn(L, 590, R, 590, "#e4e1d6", 1, True)
WP.tekst(500, 612, "3", 14)                                       # F voettekst
for k, (x, y) in {"A": (260, 75), "B": (260, 128), "C": (260, 205), "D": (260, 325), "E": (260, 445), "F": (260, 607)}.items():
    WP.letter(x, y, k)
ZW = {
    "A": [Prent.zone(235, 55, 470, 35)], "B": [Prent.zone(235, 105, 470, 45)],
    "C": [Prent.zone(235, 160, 470, 100)], "D": [Prent.zone(235, 280, 470, 100)],
    "E": [Prent.zone(235, 400, 470, 100)], "F": [Prent.zone(235, 592, 470, 36)],
}

VRAGEN = [
    klik("Klik op de alinea die uitgevuld is.", WP.bestand, ZW["D"],
         "Bij uitvullen sluit de tekst links én rechts recht aan; enkel de laatste regel mag korter zijn."),
    klik("Klik op de alinea waar enkel de eerste regel inspringt.", WP.bestand, ZW["E"],
         "Inspringen laat de alinea of een deel ervan verder van de marge beginnen."),
    klik("Klik op het deel dat op elke bladzijde automatisch onderaan terugkomt.", WP.bestand, ZW["F"],
         "De voettekst, hier met een automatisch paginanummer."),
    klik("Klik op de alinea die links uitgelijnd is.", WP.bestand, ZW["C"],
         "Links recht, rechts rafelig: links uitlijnen."),
    met_prent(WP.bestand, keuze("Titel B is [[*gecentreerd|links uitgelijnd|uitgevuld]].",
              "Hij staat in het midden tussen de marges.")),
    met_prent(WP.bestand, tabel("Kijk naar de bladzijde. Klopt dit?", [
        ("A staat in de koptekst en komt op elke bladzijde terug.", J),
        ("Om C uit te vullen, moet je eerst elke letter van C selecteren.", F),
        ("Het cijfer in F past zich aan als je vooraan een bladzijde toevoegt.", J),
    ], "Uitlijning is alineaopmaak: je cursor in de alinea volstaat.")),
    sorteer("Tekenopmaak of alineaopmaak?", ["Tekenopmaak", "Alineaopmaak"], [
        ["vet", "Tekenopmaak"],
        ["regelafstand", "Alineaopmaak"],
        ["superscript", "Tekenopmaak"],
        ["uitlijning", "Alineaopmaak"],
        ["markeren", "Tekenopmaak"],
        ["inspringen", "Alineaopmaak"],
    ], "Tekenopmaak werkt op de geselecteerde letters, alineaopmaak op de hele alinea."),
    tabel("Welke opmaak gebruik je?", [
        ("de 2 in m² (vierkante meter)", "superscript"),
        ("de 2 in H₂O", "subscript"),
        ("een zin die geschrapt is maar leesbaar moet blijven", "doorhalen"),
        ("een belangrijk woord met een gele achtergrond", "markeren"),
    ], "Superscript boven de regel, subscript eronder.",
       kolommen=["superscript", "subscript", "doorhalen", "markeren"]),
    casus(
        "Femke maakt een verslag van twaalf bladzijden voor haar stage. Haar mentor vraagt: "
        "een liggend blad voor de grote tabel op bladzijde 7, de naam van het bedrijf bovenaan "
        "elke bladzijde, paginanummers die kloppen als ze nog iets toevoegt, en het verslag "
        "doorsturen zodat niemand het per ongeluk wijzigt.",
        [
            keuze("Voor bladzijde 7 wijzigt ze de [[*afdrukstand|marge|regelafstand]] naar liggend.",
                  "Staand of liggend is de afdrukstand."),
            keuze("De naam van het bedrijf zet ze in de [[*koptekst|voettekst|titel]].",
                  "Wat bovenaan op elke bladzijde terugkomt, is de koptekst."),
            mk("Waarom kiest ze automatische paginanummering?",
               ["De nummers schuiven vanzelf mee",
                "Zo kan ze de nummers in een andere kleur zetten",
                "Zelf getypte nummers zijn verboden in een verslag",
                "Zo wordt het bestand automatisch een PDF"], 0,
               "Voeg je een bladzijde toe, dan klopt alles meteen."),
            keuze("Ze stuurt het verslag door als [[*PDF|Word-document|afbeelding van één bladzijde]].",
                  "Een PDF houdt de opmaak vast en wordt niet zomaar gewijzigd."),
        ],
    ),
    koppel("Koppel elk onderdeel van de tabelopmaak aan wat het doet.", [
        ["randen", "de lijnen rond de cellen"],
        ["arcering", "een kleur als achtergrond van een cel"],
        ["cellen samenvoegen", "van meerdere cellen één cel maken"],
        ["cellen splitsen", "van één cel meerdere cellen maken"],
    ], ["de regelafstand"], "Tabelontwerp en tabelindeling."),
    tabel("Hoort dit bij de paginaopmaak?", [
        ("de marges", J),
        ("de afdrukstand", J),
        ("het formaat A4", J),
        ("de tekstkleur", F),
    ], "Marges, afdrukstand en formaat samen."),
    mk("Je wil dat één woord midden in een zin cursief staat. Wat doe je?",
       ["Het woord selecteren en op cursief klikken",
        "Je cursor in de alinea zetten en op cursief klikken",
        "De hele alinea selecteren en uitvullen",
        "De afdrukstand wijzigen"], 0,
       "Cursief is tekenopmaak: het werkt op wat geselecteerd is."),
    keuze("De witruimte tussen twee alinea's regel je met de [[*afstand tussen alinea's|regelafstand|marges]].",
          "De regelafstand is de ruimte binnen een alinea."),
    tabel("Kan je dit instellen bij het afdrukken?", [
        ("enkelzijdig of dubbelzijdig", J),
        ("in kleur of zwart-wit", J),
        ("de sortering van de exemplaren", J),
        ("superscript", F),
    ], "Superscript is opmaak, geen afdrukinstelling."),
    volgorde("Je wil een titel over drie kolommen van een tabel laten lopen. Zet de stappen in volgorde.", [
        "de drie bovenste cellen selecteren",
        "cellen samenvoegen kiezen",
        "de titel typen en centreren",
    ], "Samenvoegen maakt één cel van meerdere."),
    sleep("Een kleur achter de tekst, zoals met een fluostift, heet [[markeren]]. Een andere kleur voor de letters zelf heet [[tekstkleur]].",
          ["arcering", "doorhalen"], "Arcering geldt voor een tabelcel."),
    mk("Waarom is uitvullen handig in een krantenkolom?",
       ["Links en rechts lopen recht",
        "De letters worden groter en beter leesbaar",
        "De kolom komt automatisch in de koptekst",
        "Het document wordt automatisch een PDF"], 0,
       "Word rekt de spaties zodat beide kanten recht zijn."),
    tabel("Wat doe je als je een vijfde rij onderaan een tabel wil?", [
        ("een rij onder de laatste rij invoegen", J),
        ("de tabel opnieuw tekenen", F),
        ("de cellen van de laatste rij splitsen", F),
    ], "Rijen toevoegen hoort bij de tabelindeling."),
    klik("Klik op het deel dat op elke bladzijde automatisch bovenaan terugkomt.", WP.bestand, ZW["A"],
         "Dat is de koptekst."),
    met_prent(WP.bestand, mk("Je zet je cursor in alinea C en klikt op uitvullen. Wat verandert er?",
       ["Alinea C wordt rechts ook recht",
        "Enkel het woord bij je cursor wordt uitgevuld",
        "Alle alinea's van het document worden uitgevuld",
        "Alinea C springt op de eerste regel in"], 0,
       "Alineaopmaak geldt voor de hele alinea waar de cursor staat.")),
    tabel("Is dit tekenopmaak?", [
        ("onderstrepen", J),
        ("tekengrootte", J),
        ("afstand tussen alinea's", F),
        ("inspringen", F),
    ], "Inspringen en afstand tussen alinea's zijn alineaopmaak."),
    keuze("Staand heet ook [[*portret|landschap]], liggend heet ook [[*landschap|portret]].",
          "Dat is de afdrukstand."),
    mk("Je document telt tien bladzijden en je verwijdert bladzijde 2. Wat gebeurt er met automatische paginanummers?",
       ["Ze passen zich vanzelf aan",
        "Je moet alle nummers zelf aanpassen",
        "De nummering verdwijnt volledig",
        "Bladzijde 2 blijft leeg met een nummer"], 0,
       "Automatische nummering volgt het document."),
    sleep("Marges, afdrukstand en [[formaat]] vormen samen de [[paginaopmaak]].",
          ["tekenopmaak", "arcering"], "A4 en A5 zijn formaten."),
    tabel("Wanneer sla je op als PDF?", [
        ("je stuurt een sollicitatiebrief naar een bedrijf", J),
        ("je collega moet je tekst nog aanvullen in Word", F),
        ("je wil dat de opmaak op elke computer gelijk blijft", J),
    ], "Een PDF zet de opmaak vast, maar is niet bedoeld om verder te bewerken."),
    sorteer("Tabelontwerp of paginaopmaak?", ["Tabelontwerp en tabelindeling", "Paginaopmaak"], [
        ["arcering van een cel", "Tabelontwerp en tabelindeling"],
        ["marges van het blad", "Paginaopmaak"],
        ["een kolom verwijderen", "Tabelontwerp en tabelindeling"],
        ["het formaat A5", "Paginaopmaak"],
    ], "Tabelopmaak werkt in de tabel, paginaopmaak op het hele blad."),
    open_("Leg uit waarom je voor de regelafstand van een alinea niet alle tekst hoeft te selecteren, maar voor vet wel.",
          "Regelafstand is alineaopmaak en geldt voor de hele alinea waar je cursor staat. Vet is tekenopmaak en werkt enkel op de letters die je geselecteerd hebt."),
]
