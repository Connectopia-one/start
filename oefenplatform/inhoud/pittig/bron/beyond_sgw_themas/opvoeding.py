"""Opvoeden: milieus, dimensies, stijlen en middelen — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
schema van de opvoedingsstijlen, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Vier opvoedingsstijlen in een kruis -----------------------------------------------------
ST = Prent("opvoedingsstijlen-kruis", "Opvoedingsstijlen volgens twee dimensies", "een vierkant in vier vakken; horizontaal responsiviteit van weinig (links) naar veel (rechts), verticaal controle van weinig (onder) naar veel (boven); linksboven A, rechtsboven B, linksonder C, rechtsonder D")
L, T, B = 260, 80, 440
ST.rect(L, T, 2 * 220, 2 * 220, "#ffffff", DONKER, 0, 2)
ST.lijn(L + 220, T, L + 220, T + 440, DONKER, 2)
ST.lijn(L, T + 220, L + 440, T + 220, DONKER, 2)
ST.pijl(L, T + 470, L + 460, T + 470, DONKER, 3)
ST.tekst(L + 220, T + 505, "responsiviteit: weinig → veel", 20)
ST.pijl(L - 30, T + 440, L - 30, T - 10, DONKER, 3)
ST.tekst(L - 50, T + 220, "controle", 20, "end")
ST.tekst(L - 45, T + 15, "veel", 18, "end")
ST.tekst(L - 45, T + 440, "weinig", 18, "end")
VAK = {"A": (L, T), "B": (L + 220, T), "C": (L, T + 220), "D": (L + 220, T + 220)}
for k, (x, y) in VAK.items():
    ST.letter(x + 110, y + 110, k)


def vak(k):
    x, y = VAK[k]
    return [Prent.zone(x, y, 220, 220)]


VRAGEN = [
    klik("Klik op het vak van de democratisch-autoritatieve stijl.", ST.bestand, vak("B"),
         "Veel controle en veel responsiviteit."),
    klik("Klik op het vak van de autoritaire stijl.", ST.bestand, vak("A"),
         "Veel controle, weinig responsiviteit."),
    klik("Klik op het vak van de stijl die van de vier het ongunstigst uitvalt voor een kind.", ST.bestand, vak("C"),
         "Onverschillig of laissez-faire: geen grenzen en geen warmte."),
    met_prent(ST.bestand, keuze("Vak D is de [[*permissieve of toegeeflijke|autoritaire|onverschillige]] stijl.",
              "Veel warmte, weinig grenzen.")),
    tabel("Primair, secundair of tertiair opvoedingsmilieu?", [
        ("het gezin", "primair"),
        ("de jeugdbeweging", "secundair"),
        ("sociale media", "tertiair"),
        ("de buitenschoolse opvang", "secundair"),
        ("de buurt", "tertiair"),
    ], "Gezin; plaatsen met een opvoedingsopdracht; plaatsen zonder opdracht maar met invloed.",
       kolommen=["primair", "secundair", "tertiair"]),
    tabel("Welke opvoedingsdimensie zie je?", [
        ("'Als je zo doet, ben ik niet meer trots op jou.'", "psychologische controle"),
        ("'Om tien uur ben je thuis, en ik wacht op je.'", "gedragsmatige controle"),
        ("Een vader ziet dat zijn zoon zenuwachtig is en vraagt rustig wat er scheelt.", "responsiviteit"),
    ], "Sturen via schuld, regels en toezicht, of warm ingaan op wat een kind nodig heeft.",
       kolommen=["responsiviteit", "gedragsmatige controle", "psychologische controle"]),
    casus(
        "Lena (14) wil naar een fuif tot twee uur 's nachts. Haar mama zegt: 'Nee, om middernacht ben je thuis. "
        "Ik leg uit waarom: je moet zaterdag vroeg op voor je examen.' Lena protesteert, mama luistert, maar houdt de afspraak. "
        "Bij haar vriendin Jente thuis zegt papa: 'Doe maar wat je wil, ik wil geen ruzie.' "
        "Bij hun vriend Arno thuis zegt niemand iets, want niemand weet waar hij is.",
        [
            tabel("Welke opvoedingsstijl?", [
                ("de mama van Lena", "democratisch-autoritatief"),
                ("de papa van Jente", "permissief"),
                ("het gezin van Arno", "onverschillig"),
            ], "Warmte met grenzen, warmte zonder grenzen, of geen van beide.",
               kolommen=["democratisch-autoritatief", "permissief", "onverschillig"]),
            mk("Welke stijl komt in onderzoek het gunstigst uit?",
               ["de stijl van de mama van Lena",
                "de stijl van de papa van Jente",
                "de stijl in het gezin van Arno",
                "ze zijn alle drie even gunstig"], 0,
               "Grenzen met warmte en uitleg geven de beste resultaten."),
            keuze("Dat Lena protesteert en mama naar haar luistert, toont dat opvoeding een [[*transactioneel|eenrichtings|toevallig]] proces is.",
                  "Kind en opvoeder beïnvloeden elkaar voortdurend."),
        ],
    ),
    keuze("Autoritair en autoritatief [[*verschillen|betekenen hetzelfde]]: het ene is streng zonder warmte, het andere streng mét warmte.",
          "De klassieke valkuil."),
    tabel("Welk opvoedingsmiddel is dit?", [
        ("Elke ochtend in dezelfde volgorde: wassen, aankleden, ontbijten.", "gewoontevorming"),
        ("Een peuter wil aan het stopcontact; de ouder geeft hem een speelgoedauto.", "afleiden"),
        ("Een ouder legt uit waarom je niet met vreemden mee moet gaan.", "informatieoverdracht"),
        ("Een ouder leest zelf elke avond, en het kind gaat ook lezen.", "voorbeeldgedrag"),
    ], "Vaste routine, de aandacht verleggen, uitleg geven, of het goede voorbeeld.",
       kolommen=["gewoontevorming", "afleiden", "informatieoverdracht", "voorbeeldgedrag"]),
    mk("Responsiviteit en belonen horen allebei bij opvoeden. Hoe verschillen ze?",
       ["houding tegenover aanpak",
        "een stijl tegenover een milieu",
        "een regel tegenover een straf",
        "een kind tegenover een ouder"], 0,
       "Dimensies zijn houdingen; middelen zijn wat je concreet doet."),
    koppel("Koppel elke stijl aan de combinatie.", [
        ["autoritair", "veel controle, weinig responsiviteit"],
        ["democratisch-autoritatief", "veel controle, veel responsiviteit"],
        ["permissief", "weinig controle, veel responsiviteit"],
        ["onverschillig", "weinig controle, weinig responsiviteit"],
    ], ["enkel psychologische controle"], "Een stijl is een combinatie van dimensies."),
    tabel("Klopt dit over opvoeden?", [
        ("Het tertiaire milieu heeft geen invloed, want het heeft geen opdracht.", F),
        ("Wat op school gebeurt, werkt thuis door.", J),
        ("Straffen is een van de opvoedingsmiddelen.", J),
        ("Gedragsmatige en psychologische controle zijn hetzelfde.", F),
    ], "Het tertiaire milieu heeft wel invloed; de twee soorten controle verschillen."),
    inv("Hoeveel opvoedingsdimensies onderscheid je? Schrijf het getal.", ["3", "drie"],
        "Responsiviteit, gedragsmatige controle en psychologische controle."),
    keuze("Een kind met een moeilijk temperament maakt een ouder ongeduldig, en dat maakt het kind nog moeilijker. Dat toont dat het [[*kind|de buurt|de school]] ook een actor in de opvoeding is.",
          "Opvoeding is transactioneel."),
    sleep("De drie actoren in de opvoeding zijn het [[kind]], de [[opvoeder]] en de omgeving.",
          ["dimensie", "stijl"], "Ook de omgeving bepaalt mee wat een kind leert."),
    keuze("Een kind dat even uit de situatie gehaald wordt om af te koelen, krijgt een [[*time-out|beloning|gewoonte]].",
          "Negeren en time-out is een opvoedingsmiddel."),
    sorteer("Opvoedingsdimensie of opvoedingsmiddel?", ["Dimensie", "Middel"], [
        ["responsiviteit", "Dimensie"],
        ["belonen", "Middel"],
        ["psychologische controle", "Dimensie"],
        ["afleiden", "Middel"],
        ["gewoontevorming", "Middel"],
    ], "Drie dimensies, negen middelen."),
    mk("Een peuter van twee wil per se de schaar van de tafel. Welk middel is hier het meest geschikt?",
       ["afleiden met iets anders",
        "een uitgebreide uitleg over gevaar",
        "een week geen dessert als straf",
        "hem de schaar even laten proberen"], 0,
       "Afleiden werkt vooral bij jonge kinderen."),
    inv("Hoeveel opvoedingsstijlen onderscheid je? Schrijf het getal.", ["4", "vier"],
        "Autoritair, democratisch-autoritatief, permissief en onverschillig."),
    keuze("Het gezin is het [[*primaire|secundaire|tertiaire]] opvoedingsmilieu.",
          "Het eerste en meest nabije milieu."),
    keuze("Een andere naam voor de onverschillige stijl is [[*laissez-faire|toegeeflijk|autoritatief]].",
          "Laissez-faire: laten begaan."),
    mk("Een ouder zegt: 'Dat doe je omdat ik het zeg, en verder geen discussie.' Welke stijl hoor je?",
       ["autoritair", "democratisch-autoritatief", "permissief", "onverschillig"], 0,
       "Een regel zonder uitleg en zonder gesprek."),
    tabel("Welke dimensie is hoog of laag bij deze stijl? Kies voor de permissieve stijl.", [
        ("responsiviteit", "hoog"),
        ("gedragsmatige controle", "laag"),
        ("warmte tonen", "hoog"),
    ], "Veel warmte, weinig grenzen.", kolommen=["hoog", "laag"]),
    keuze("De school hoort bij het [[*secundaire|primaire|tertiaire]] opvoedingsmilieu.",
          "Plaatsen met een eigen opvoedingsopdracht."),
    inv("Hoe heet het opvoedingsmiddel waarbij een kind het gedrag van de ouder overneemt? Vul aan: voorbeeldgedrag of ...", ["modelleren"],
        "Voorbeeldgedrag of modelleren."),
    keuze("Een ouder die de liefde als voorwaarde gebruikt, zet [[*psychologische|gedragsmatige]] controle in.",
          "Psychologische controle werkt op het gevoel van het kind."),
    mk("Waarom is de omgeving een actor in de opvoeding?",
       ["ze bepaalt mee wat een kind meemaakt",
        "ze kiest de opvoedingsstijl van de ouders",
        "ze heeft altijd een opvoedingsopdracht",
        "ze vervangt de ouders na de lagere school"], 0,
       "Buurt, school en media bepalen mee wat een kind leert."),
    open_("Een ouder wil dat zijn kind van tien zijn huiswerk maakt voor het gamet. Beschrijf hoe een democratisch-autoritatieve ouder dat aanpakt, en waarom dat beter werkt dan een autoritaire aanpak.",
          "De ouder maakt een duidelijke afspraak (eerst huiswerk, dan gamen), legt uit waarom, luistert naar het kind en houdt de afspraak met warmte vol. Dat werkt beter dan autoritair, omdat het kind de regel begrijpt en zich gehoord voelt; streng zonder warmte en uitleg geeft minder gunstige resultaten."),
]
