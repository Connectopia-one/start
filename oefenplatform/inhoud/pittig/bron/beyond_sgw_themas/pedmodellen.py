"""Pedagogische modellen en opvoeden in bijzondere contexten — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
tekening van het balansmodel, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Twee weegschalen van het balansmodel ---------------------------------------------------
BA = Prent("balansmodel-twee-gezinnen", "Het balansmodel bij twee gezinnen", "twee weegschalen naast elkaar, elk met links een schaal 'draaglast' en rechts een schaal 'draagkracht'; bij gezin A hangt de draaglast veel lager, bij gezin B hangt de draagkracht lager")


def schaal(p, cx, kantel):
    p.lijn(cx, 520, cx, 230, DONKER, 4)
    p.rect(cx - 60, 520, 120, 16, "#c4d5b5", DONKER, 3, 2)
    lx, ly, rx, ry = cx - 130, 230 + kantel, cx + 130, 230 - kantel
    p.lijn(lx, ly, rx, ry, DONKER, 5)
    for x, y, naam in [(lx, ly, "draaglast"), (rx, ry, "draagkracht")]:
        p.lijn(x, y, x - 40, y + 70, GRIJS, 2)
        p.lijn(x, y, x + 40, y + 70, GRIJS, 2)
        p.pad(f"M{x - 55} {y + 70} L{x + 55} {y + 70} L{x + 35} {y + 95} L{x - 35} {y + 95} Z", "#e8efe1", DONKER, 2)
        p.tekst(x, y + 130, naam, 19)


schaal(BA, 250, 50)
schaal(BA, 750, -50)
BA.letter(250, 590, "A")
BA.letter(750, 590, "B")

VRAGEN = [
    klik("Klik op het gezin waar de kans op problemen in de opvoeding het grootst is.", BA.bestand,
         [Prent.zone(60, 120, 420, 500)],
         "Bij gezin A weegt de draaglast zwaarder dan de draagkracht."),
    met_prent(BA.bestand, tabel("Wat kan gezin A helpen volgens het balansmodel?", [
        ("een grootmoeder die elke week de kinderen opvangt", J),
        ("een extra verhuis en een nieuwe job tegelijk", F),
        ("hulp van een gezinsbegeleider", J),
    ], "Je kan de draagkracht vergroten of de draaglast verkleinen.")),
    met_prent(BA.bestand, keuze("Bij gezin B is de draagkracht [[*groter|kleiner]] dan de draaglast.",
              "De schaal van de draagkracht hangt lager: die weegt zwaarder.")),
    met_prent(BA.bestand, inv("Van wie is het balansmodel? Familienaam van de eerste naam.", ["Bakker"],
              "Het balansmodel van Bakker en anderen.")),
    koppel("Koppel elke historische visie aan haar kern.", [
        ["Confucius", "respect, deugd en het goede voorbeeld"],
        ["Plato", "opvoeding als opdracht van de samenleving"],
        ["Rousseau", "de natuur van het kind volgen"],
    ], ["gezag door aanwezigheid, niet door macht"], "Drie van de vier historische visies."),
    tabel("Historische of hedendaagse visie?", [
        ("Al-Ghazali", "historisch"),
        ("nieuwe autoriteit", "hedendaags"),
        ("behoefteondersteunende opvoeding", "hedendaags"),
        ("Rousseau", "historisch"),
    ], "Vier historische namen en twee hedendaagse visies.", kolommen=["historisch", "hedendaags"]),
    keuze("Bij de nieuwe autoriteit blijven de grenzen, maar het gezag komt uit [[*aanwezigheid en steun|macht en straf|toegeven]].",
          "Gezag door nabijheid, niet door macht."),
    sorteer("Risicofactor of beschermende factor?", ["Risicofactor", "Beschermende factor"], [
        ["een sterk netwerk van vrienden", "Beschermende factor"],
        ["langdurige werkloosheid", "Risicofactor"],
        ["een warme band met een leerkracht", "Beschermende factor"],
        ["zware schulden", "Risicofactor"],
    ], "Een risicofactor verhoogt de kans op problemen, een beschermende factor verkleint ze."),
    keuze("Opvoeding is [[*multifactorieel|monofactorieel]]: er werken altijd meerdere factoren samen.",
          "Je zoekt nooit één oorzaak."),
    tabel("Op welk niveau speelt deze factor?", [
        ("ruzie tussen de ouders thuis", "micro"),
        ("slecht contact tussen school en gezin", "meso"),
        ("een tekort aan betaalbare kinderopvang in het land", "macro"),
    ], "Rond het kind, tussen milieus, of in de samenleving.", kolommen=["micro", "meso", "macro"]),
    tabel("In welke soort bijzondere context hoort dit?", [
        ("ADHD", "ontwikkelingsstoornis"),
        ("dyscalculie", "leerstoornis"),
        ("kansarmoede", "maatschappelijke kwetsbaarheid"),
        ("ASS", "ontwikkelingsstoornis"),
    ], "ADHD en ASS, dyslexie en dyscalculie, of nadeel in de samenleving.",
       kolommen=["ontwikkelingsstoornis", "leerstoornis", "maatschappelijke kwetsbaarheid"]),
    inv("Waarvoor staat VOS?", ["verontrustende opvoedingssituatie", "een verontrustende opvoedingssituatie"],
        "Een situatie waarin de ontwikkeling van een kind bedreigd is."),
    casus(
        "Tibo (9) heeft een verstandelijke handicap. Hij woont in een kleine studio met zijn mama. Hij wil graag zelf "
        "zijn boterhammen smeren en meedoen met de voetbalclub in de buurt, maar de club zegt dat dat niet gaat. "
        "Thuis is het vaak rumoerig, en de regels veranderen van dag tot dag.",
        [
            tabel("Bij welk deel van kwaliteit van bestaan van Schalock en Verdugo hoort dit?", [
                ("zelf zijn boterhammen smeren", "onafhankelijkheid"),
                ("meedoen met de voetbalclub", "sociale participatie"),
                ("een kleine studio, weinig geld", "welbevinden"),
            ], "Zelfbepaling, inclusie en materieel welbevinden.",
               kolommen=["onafhankelijkheid", "sociale participatie", "welbevinden"]),
            tabel("Welke variabele van Rink zie je?", [
                ("Tibo zelf", "K"),
                ("zijn mama", "O"),
                ("de regels die van dag tot dag veranderen", "St"),
            ], "K is het kind, O de opvoeder, St de situatietypes.", kolommen=["K", "O", "St"]),
            mk("Waarom is het model van Rink hier handig?",
               ["je kijkt of de situatie anders kan",
                "je zoekt enkel wat er mis is met Tibo zelf",
                "je meet hoe intelligent zijn mama is",
                "je vergelijkt Tibo met andere kinderen"], 0,
               "Door context en situatietypes te bekijken, pas je meer aan dan alleen het kind."),
        ],
    ),
    koppel("Koppel elk model aan zijn makers.", [
        ["kwaliteit van bestaan", "Schalock en Verdugo"],
        ["viervariabelenmodel", "Rink"],
        ["balansmodel", "Bakker en anderen"],
        ["bio-ecologisch model", "Bronfenbrenner"],
    ], ["Costa en McCrae"], "Twee pedagogische en twee orthopedagogische modellen."),
    sorteer("Pedagogisch of orthopedagogisch model?", ["Pedagogisch", "Orthopedagogisch"], [
        ["balansmodel", "Pedagogisch"],
        ["viervariabelenmodel", "Orthopedagogisch"],
        ["bio-ecologisch model", "Pedagogisch"],
        ["kwaliteit van bestaan", "Orthopedagogisch"],
    ], "De orthopedagogische modellen zijn voor bijzondere contexten."),
    keuze("Bij Rink horen de activiteiten, de regels en de [[*sfeer|stijl|draagkracht]] bij de situatietypes.",
          "Drie zaken bij de situatietypes."),
    sleep("Kwaliteit van bestaan heeft drie grote delen: [[onafhankelijkheid]], sociale participatie en [[welbevinden]].",
          ["draaglast", "responsiviteit"], "Schalock en Verdugo."),
    tabel("Klopt dit over pedagogische modellen?", [
        ("Een risicofactor maakt problemen zeker.", F),
        ("Een bijzondere context raakt ook de opvoeders en de omgeving.", J),
        ("Kwaliteit van bestaan kijkt enkel naar de gezondheid.", F),
        ("Historische visies werken vandaag nog door.", J),
    ], "Een risicofactor verhoogt de kans; welbevinden is maar een deel."),
    mk("Een leerling heeft veel moeite met lezen en spellen. Een andere met rekenen. Welke twee stoornissen zijn dat?",
       ["dyslexie en dyscalculie", "ADHD en ASS, allebei ontwikkelingsstoornissen", "kansarmoede en een VOS", "dyscalculie en ADHD"], 0,
       "Dyslexie is moeite met lezen en spellen, dyscalculie met rekenen."),
    keuze("Volgens Rousseau is een kind van nature [[*goed|slecht|leeg]].",
          "Opvoeden moet daarom de natuur van het kind volgen."),
    inv("Hoeveel variabelen heeft het model van Rink? Schrijf het getal.", ["4", "vier"],
        "Kind, opvoeder, situationele context en situatietypes."),
    keuze("Plato denkt opvoeding vanuit [[*de ideale staat|de natuur van het kind|het geloof]].",
          "Opvoeding is bij hem een opdracht van de samenleving."),
    mk("Welke visie vertrekt van de basisbehoeften van een kind?",
       ["behoefteondersteunend opvoeden", "de visie van de nieuwe autoriteit", "de visie van Plato op de staat", "het balansmodel van Bakker"], 0,
       "Een hedendaagse visie die ingaat op wat een kind nodig heeft."),
    tabel("Welke soort handicap?", [
        ("een kind dat blind is", "zintuiglijk"),
        ("een kind in een rolstoel", "fysiek"),
        ("een kind dat traag leert en veel begeleiding nodig heeft", "verstandelijk"),
    ], "Zintuigen, lichaam of verstand.", kolommen=["fysiek", "zintuiglijk", "verstandelijk"]),
    keuze("Een gezin dat telkens op nadeel botst in de samenleving, zoals bij kansarmoede, leeft in [[*maatschappelijke kwetsbaarheid|een ontwikkelingsstoornis|een VOS]].",
          "Maatschappelijke kwetsbaarheid."),
    inv("Hoe heet bij Rink de variabele met de letter O?", ["opvoeder", "de opvoeder"],
        "K is het kind, O de opvoeder."),
    mk("Een grootmoeder vangt elke week op en staat het gezin bij. Wat is ze in de opvoeding?",
       ["een beschermende factor", "een risicofactor in het gezin", "een situatietype van Rink", "een factor op macroniveau"], 0,
       "Steun uit de omgeving verkleint de kans op problemen."),
    open_("Een gezin krijgt op korte tijd een ziekte, een ontslag en een verhuis te verwerken. Leg met het balansmodel uit wanneer dat tot problemen leidt en hoe je kan helpen.",
          "Problemen ontstaan als de draaglast (ziekte, ontslag, verhuis) groter wordt dan de draagkracht (netwerk, geld, veerkracht). Je kan helpen door de draaglast te verkleinen, bijvoorbeeld hulp bij de verhuis, of de draagkracht te vergroten, bijvoorbeeld familie die opvangt of een gezinsbegeleider."),
]
