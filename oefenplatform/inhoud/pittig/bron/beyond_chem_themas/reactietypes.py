"""Organische reacties: substitutie en het radicalaire mechanisme — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Drie reactieschema's -------------------------------------------------------
SP = Prent("splitsingen", "Drie reactiestappen met de elektronen getekend als puntjes", "drie rijen: Cl₂ dat in twee chlooratomen met elk één puntje splitst; broommethaan dat splitst in een positief koolstofdeel en een bromide-ion; een hydroxide-ion dat broommethaan aanvalt; letters P, Q en R")
RIJ = {
    "P": "Cl : Cl   →   Cl •   +   • Cl",
    "Q": "H₃C : Br   →   H₃C⁺   +   :Br⁻",
    "R": "HO⁻  +  H₃C–Br   →   H₃C–OH  +  Br⁻",
}
for i, (k, t) in enumerate(RIJ.items()):
    y = 150 + i * 150
    SP.rect(160, y - 50, 760, 100, "#fbfbf7", DONKER, 16, 2)
    SP.tekst(540, y + 12, t, 30, vet=True)
    SP.letter(100, y, k)
ZSP = {k: [Prent.zone(160, 100 + i * 150, 760, 100), Prent.rond(100, 150 + i * 150, 22)] for i, k in enumerate(RIJ)}

# Chlorering van methaan in stappen ------------------------------------------
CM = Prent("chlorering-methaan", "Stappen bij de reactie van methaan met chloorgas onder uv-licht", "vier vakken met een reactiestap: A Cl₂ naar twee Cl-radicalen, B Cl-radicaal met CH₄, C methylradicaal met Cl₂, D twee methylradicalen; letters A tot D")
STAP = {
    "A": "Cl₂   →   2 Cl•",
    "B": "Cl•  +  CH₄   →   HCl  +  •CH₃",
    "C": "•CH₃  +  Cl₂   →   CH₃Cl  +  Cl•",
    "D": "•CH₃  +  •CH₃   →   C₂H₆",
}
for i, (k, t) in enumerate(STAP.items()):
    y = 110 + i * 120
    CM.rect(170, y - 42, 700, 84, "#ffffff", DONKER, 14, 2)
    CM.tekst(520, y + 10, t, 28, vet=True)
    CM.letter(110, y, k)
ZCM = {k: [Prent.zone(170, 68 + i * 120, 700, 84), Prent.rond(110, 110 + i * 120, 22)] for i, k in enumerate(STAP)}

VRAGEN = [
    klik(
        "Klik op de homolytische splitsing.",
        SP.bestand, ZSP["P"],
        "Elk atoom houdt één elektron: er ontstaan twee radicalen.",
    ),
    klik(
        "Klik op de stap waarin een nucleofiel aanvalt.",
        SP.bestand, ZSP["R"],
        "OH⁻ brengt een vrij elektronenpaar mee naar het positief gepolariseerde koolstofatoom.",
    ),
    met_prent(SP.bestand, tabel(
        "Wat ontstaat er in deze stap?",
        [
            ("P", "Radicalen"),
            ("Q", "Ionen"),
            ("R", "Een alcohol en een ion"),
        ],
        "Heterolytisch splitsen geeft ionen: één atoom krijgt het hele paar.",
        kolommen=["Radicalen", "Ionen", "Een alcohol en een ion"],
    )),
    klik(
        "Klik op de initiatiestap.",
        CM.bestand, ZCM["A"],
        "Uv-licht splitst Cl₂ homolytisch in twee radicalen.",
    ),
    klik(
        "Klik op de propagatiestap waarin het product chloormethaan ontstaat.",
        CM.bestand, ZCM["C"],
        "Het methylradicaal neemt een chlooratoom en er komt een nieuw Cl-radicaal vrij.",
    ),
    met_prent(CM.bestand, tabel(
        "Welk soort stap is dit?",
        [
            ("A", "Initiatie"),
            ("B", "Propagatie"),
            ("C", "Propagatie"),
            ("D", "Terminatie"),
        ],
        "In een propagatiestap reageert een radicaal en ontstaat er weer een.",
        kolommen=["Initiatie", "Propagatie", "Terminatie"],
    )),
    met_prent(CM.bestand, mk(
        "Waarom is stap D een terminatie, al ontstaat er een stof die niet de bedoeling was?",
        [
            "Er blijft geen radicaal over",
            "Er ontstaat chloormethaan, het eindproduct",
            "Er komt bij die stap uv-licht vrij",
            "De binding splitst daar heterolytisch in ionen",
        ],
        0,
        "Ethaan is een bijproduct; de ketting stopt omdat er geen ongepaard elektron overblijft.",
    )),
    met_prent(CM.bestand, inv(
        "Hoeveel radicalen ontstaan er in stap A uit één molecule Cl₂?",
        ["2", "twee"],
        "Elk chlooratoom houdt één elektron.",
    )),
    tabel(
        "Welk reactietype is dit?",
        [
            ("CH₄ + Cl₂ → CH₃Cl + HCl", "Substitutie"),
            ("CH₂=CH₂ + Br₂ → CH₂Br–CH₂Br", "Additie"),
            ("CH₃CH₂OH → CH₂=CH₂ + H₂O", "Eliminatie"),
            ("alcohol + carbonzuur → ester + water", "Condensatie"),
        ],
        "Vervangen, toevoegen, iets klein afsplitsen met een dubbele binding, of koppelen met water eruit.",
        kolommen=["Substitutie", "Additie", "Eliminatie", "Condensatie"],
    ),
    tabel(
        "Welk deeltje valt aan bij deze reactie?",
        [
            ("chlorering van ethaan onder uv-licht", "Radicaal"),
            ("broom met benzeen en een katalysator", "Elektrofiel"),
            ("water met broomethaan", "Nucleofiel"),
            ("ammoniak met chloormethaan", "Nucleofiel"),
        ],
        "Alkaan: radicaal. Aromaat: elektrofiel. Halogeenalkaan: nucleofiel.",
        kolommen=["Radicaal", "Elektrofiel", "Nucleofiel"],
    ),
    tabel(
        "Welk product ontstaat er bij de nucleofiele substitutie van broomethaan met dit deeltje?",
        [
            ("water", "Alcohol"),
            ("ammoniak", "Amine"),
            ("methanol", "Ether"),
        ],
        "Het atoom met het vrije paar komt op de plaats van het broom.",
        kolommen=["Alcohol", "Amine", "Ether"],
    ),
    casus(
        "Benzeen reageert met broom in aanwezigheid van FeBr₃.",
        [
            keuze(
                "Het is een [[*elektrofiele substitutie|elektrofiele additie|radicalaire substitutie]].",
                "Een elektrofiel valt de elektronenrijke ring aan en vervangt een H-atoom.",
            ),
            mk(
                "Welke producten ontstaan er?",
                ["Broombenzeen en HBr", "Dibroomcyclohexaan", "Benzeen en twee Br⁻", "Broombenzeen en H₂"],
                0,
                "Eén H wordt vervangen door Br, het H-atoom vormt met het andere Br-atoom HBr.",
            ),
            mk(
                "Waarom gebeurt er geen additie zoals bij een alkeen?",
                [
                    "De stabiele ring zou verloren gaan",
                    "Benzeen heeft geen enkele pi-elektronen",
                    "Broom kan nooit een additie aangaan",
                    "De katalysator verhindert elke reactie",
                ],
                0,
                "Bij substitutie blijft de stabiele ring behouden.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over radicalen?",
        [
            ("Ze hebben een ongepaard elektron.", J),
            ("Ze zijn heel reactief.", J),
            ("Ze ontstaan bij een heterolytische splitsing.", F),
        ],
        "Radicalen ontstaan bij een homolytische splitsing.",
    ),
    volgorde(
        "Zet de stappen van een radicalaire substitutie in de goede volgorde.",
        ["initiatie", "propagatie", "terminatie"],
        "Start, kettingreactie, stop.",
    ),
    mk(
        "Hexaan en hexeen krijgen allebei broomwater in het donker. Waarom ontkleurt alleen bij hexeen het broom meteen?",
        [
            "Hexaan mist een elektronenrijke plaats",
            "Hexaan heeft te veel pi-bindingen voor broom",
            "Hexaan is zelf een sterk elektrofiel deeltje",
            "Hexaan lost veel beter op in water dan hexeen",
        ],
        0,
        "Alle bindingen zijn sterke, weinig polaire sigma-bindingen.",
    ),
    sleep(
        "Een [[nucleofiel]] heeft een vrij elektronenpaar en zoekt een positieve plaats. Een [[elektrofiel]] zoekt een plaats met veel elektronen. Een [[radicaal]] heeft een ongepaard elektron.",
        ["katalysator", "ion"],
        "Het aanvallende deeltje bepaalt de naam van de substitutie.",
    ),
    tabel(
        "Klopt dit over de verestering?",
        [
            ("Er komt water vrij.", J),
            ("Ze is een condensatie.", J),
            ("Ze is omkeerbaar.", J),
            ("Er ontstaat een ether.", F),
        ],
        "Alcohol + carbonzuur ⇌ ester + water. De omgekeerde reactie is een hydrolyse.",
    ),
    koppel(
        "Koppel elk reactietype aan wat er gebeurt.",
        [
            ("substitutie", "een atoom of groep wordt vervangen"),
            ("additie", "er komt iets bij op een dubbele binding"),
            ("eliminatie", "er gaat iets af en er ontstaat een dubbele binding"),
            ("condensatie", "twee moleculen koppelen en er komt water vrij"),
        ],
        ["een metaal wordt geoxideerd"],
        "De vier organische reactietypes.",
    ),
    mk(
        "Waarom reageert een halogeenalkaan makkelijker met een nucleofiel dan een alkaan?",
        [
            "De C–X-binding is polair, C is licht positief",
            "Een halogeenalkaan heeft een dubbele binding",
            "Een alkaan heeft te veel vrije elektronenparen",
            "Een halogeenalkaan is een radicaal",
        ],
        0,
        "Het halogeen trekt elektronen naar zich toe; het koolstofatoom wordt een doelwit.",
    ),
    inv(
        "Hoeveel waterstofatomen van methaan kunnen er in totaal vervangen worden door chlooratomen?",
        ["4", "vier"],
        "Na lang genoeg reageren ontstaat zelfs CCl₄.",
    ),
    tabel(
        "Is deze splitsing homolytisch of heterolytisch?",
        [
            ("Br₂ onder uv-licht", "Homolytisch"),
            ("C–Br bij een nucleofiele substitutie", "Heterolytisch"),
            ("H–Cl in water", "Heterolytisch"),
        ],
        "Ontstaan er ionen, dan is de splitsing heterolytisch.",
        kolommen=["Homolytisch", "Heterolytisch"],
    ),
    mk(
        "Wat ontstaat er als twee moleculen ethanol reageren en er water uitgaat?",
        ["Diethylether", "Ethylethanoaat", "Etheen en ethaan", "Ethaanzuur"],
        0,
        "Twee alcoholen geven een ether bij een condensatie.",
    ),
    keuze(
        "Een ester valt met water terug uiteen in een [[*hydrolyse|verestering|eliminatie]].",
        "Met een base noemt men dat een verzeping.",
    ),
    tabel(
        "Welk deeltje is een nucleofiel?",
        [
            ("OH⁻", "Ja"),
            ("NH₃", "Ja"),
            ("H⁺", "Nee"),
            ("CH₄", "Nee"),
        ],
        "Een nucleofiel heeft een vrij elektronenpaar om aan te bieden.",
        kolommen=["Ja", "Nee"],
    ),
    inv(
        "Hoeveel verschillende monochloorproducten kunnen er ontstaan bij de radicalaire chlorering van ethaan?",
        ["1", "een", "één"],
        "Alle zes H-atomen zijn gelijkwaardig: alleen chloorethaan.",
    ),
    mk(
        "Waarom brengt een katalysator zoals FeBr₃ de bromering van benzeen op gang?",
        [
            "Hij maakt broom echt elektrofiel",
            "Hij splitst broom in radicalen",
            "Hij breekt de benzeenring open",
            "Hij levert uv-licht aan het mengsel",
        ],
        0,
        "Zonder katalysator is broom te zwak als elektrofiel voor de stabiele ring.",
    ),
    sorteer(
        "Bij welke substitutie hoort deze stof als uitgangsstof?",
        ["Radicalair", "Elektrofiel", "Nucleofiel"],
        [
            ("propaan met chloorgas onder uv-licht", "Radicalair"),
            ("cyclohexaan met broom onder uv-licht", "Radicalair"),
            ("benzeen met broom en FeBr₃", "Elektrofiel"),
            ("chloorpropaan met water", "Nucleofiel"),
            ("broomethaan met ammoniak", "Nucleofiel"),
        ],
        "De stof bepaalt het mechanisme: alkaan, aromaat of halogeenalkaan.",
    ),
    open_(
        "Leg uit waarom een radicalaire substitutie een kettingreactie genoemd wordt.",
        "In de propagatiestappen reageert een radicaal met een molecule en ontstaat er telkens opnieuw een radicaal. Dat nieuwe radicaal kan meteen een volgende molecule aanvallen. Zo loopt de reactie zichzelf verder, tot twee radicalen elkaar tegenkomen en koppelen in een terminatiestap.",
    ),
]
