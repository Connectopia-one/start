"""Commerciële documenten en de documentenstroom — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_documenten, met een zelfgetekend schema van de
documentenstroom tussen koper en leverancier."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, BLAUW, ORANJE, GRIJS

DS = Prent("documentenstroom-zeven", "Documentenstroom tussen koper en leverancier", "tijdlijn met zeven pijlen A tot G tussen koper en leverancier, zonder namen van documenten")
DS.rect(70, 60, 220, 56, LICHTGROEN, DONKER, 12, 2); DS.tekst(180, 96, "koper", 22, vet=True)
DS.rect(710, 60, 220, 56, "#eef3f8", DONKER, 12, 2); DS.tekst(820, 96, "leverancier", 22, vet=True)
DS.lijn(180, 116, 180, 620, GRIJS, 3, True); DS.lijn(820, 116, 820, 620, GRIJS, 3, True)
PIJL = [("A", "->"), ("B", "<-"), ("C", "->"), ("D", "<-"), ("E", "<-"), ("F", "<-"), ("G", "<-")]
Y0, DY = 160, 70
for i, (t, r) in enumerate(PIJL):
    y = Y0 + i * DY
    if r == "->":
        DS.pijl(195, y, 805, y, BLAUW, 4)
    else:
        DS.pijl(805, y, 195, y, ORANJE, 4)
    DS.letter(500, y - 24, t)
DS.tekst(500, 632, "tijd loopt van boven naar onder", 17)
U = "documentenstroom-zeven.svg"
Z = {t: Prent.rond(500, Y0 + i * DY - 24, 30) for i, (t, _) in enumerate(PIJL)}

VRAGEN = [
    klik("De pijlen tonen de documenten bij een gewone aankoop, in volgorde. Klik op de letter bij de offerte.", U, [Z["B"]],
         "Eerst vraagt de koper een prijs (A), de leverancier antwoordt met een offerte (B)."),
    klik("Klik op de letter bij de bestelbon.", U, [Z["C"]],
         "Na de offerte bestelt de koper schriftelijk: de bestelbon gaat van de koper naar de leverancier."),
    klik("Klik op de letter bij de orderbevestiging.", U, [Z["D"]],
         "De leverancier laat weten dat de bestelling binnen is en wanneer hij levert."),
    klik("Klik op de letter bij de creditnota die volgt omdat er iets terug moest.", U, [Z["G"]],
         "De creditnota zet de factuur recht en komt dus na de factuur."),
    klik("Klik op de letter bij het document dat met de goederen meekomt.", U, [Z["E"]],
         "De leverbon komt mee met de levering, nog vóór de factuur."),
    tabel("Klopt dit volgens het schema van de documentenstroom?",
          [("Pijl A is de prijsaanvraag.", J), ("Pijl F is de factuur.", J), ("De factuur gaat van de koper naar de leverancier.", F), ("Elk document na de bestelbon komt van de leverancier.", J)],
          "Prijsaanvraag en bestelbon gaan van de koper naar de leverancier; de rest de andere richting uit."),
    casus("Lees de documenten van een aankoop door restaurant De Smaak.\n\nBestelbon: 20 dozen servetten aan 4 euro per doos.\nLeverbon: 18 dozen servetten.\nFactuur: 20 dozen servetten aan 4,50 euro per doos.", [
        tabel("Wat klopt er niet?",
              [("het aantal op de factuur tegenover de leverbon", "fout"), ("de prijs per doos op de factuur tegenover de bestelbon", "fout"), ("de omschrijving van de goederen", "juist")],
              "Je controleert de factuur tegen de bestelbon en de leverbon.",
              kolommen=["juist", "fout"]),
        inv("Hoeveel euro zonder btw had De Smaak moeten betalen voor wat geleverd werd, aan de afgesproken prijs? Schrijf enkel het getal.", ["72"],
            "18 dozen × 4 euro = 72 euro."),
        mk("Wat doet De Smaak best?",
           ["de leverancier bellen en een creditnota vragen", "de factuur meteen betalen om geen boete te riskeren", "zelf een nieuwe bestelbon voor 2 extra dozen sturen", "de leverbon terugsturen en helemaal niets betalen"], 0,
           "Een fout die je niet opmerkt, betaal je zelf. De verkoper zet ze recht met een creditnota."),
    ]),
    volgorde("Zet de documenten bij een aankoop in de juiste volgorde.",
             ["prijsaanvraag", "offerte", "bestelbon", "orderbevestiging", "leverbon", "factuur"],
             "Eerst weten wat het kost, dan bestellen, leveren en factureren."),
    sorteer("Van wie naar wie gaat dit document?", ["koper naar leverancier", "leverancier naar koper"],
            [("de prijsaanvraag", "koper naar leverancier"), ("de offerte", "leverancier naar koper"), ("de bestelbon", "koper naar leverancier"), ("de factuur", "leverancier naar koper"), ("een klacht bij een fout", "koper naar leverancier"), ("de creditnota", "leverancier naar koper")],
            "De koper vraagt en bestelt; de verkoper biedt aan, levert en factureert."),
    tabel("Staat dit verplicht op een factuur?",
          [("de datum en het nummer", J), ("de gegevens van beide partijen", J), ("de btw en het totaal", J), ("de hobby's van de klant", F)],
          "En de omschrijving van de goederen of diensten."),
    keuze("Een leverbon vermeldt vooral de [[*aantallen|prijzen|btw-bedragen]]; de bedragen staan op de factuur.",
          "Zo kan de ontvanger meteen nagaan of alles er is."),
    keuze("Voor de verkoper is het een [[*verkoopfactuur|aankoopfactuur]], voor de koper een [[*aankoopfactuur|verkoopfactuur]].",
          "Dezelfde factuur, een andere rol."),
    mk("Waarom staat er een geldigheidsduur op een offerte?",
       ["De leverancier zit zolang aan zijn prijs vast.", "De koper moet binnen die tijd zeker bestellen.", "Daarna wordt de factuur automatisch verstuurd.", "Zo weet de boekhouding wanneer ze moet betalen."], 0,
       "Een offerte bindt de leverancier aan zijn prijs zolang ze geldig is."),
    koppel("Wanneer gebruik je welk document?",
           [("je wil eerst weten wat iets kost", "prijsaanvraag"), ("de klant stuurt goederen terug", "creditnota"), ("de leverancier bevestigt dat hij de bestelling kreeg", "orderbevestiging"), ("de goederen vertrekken naar de klant", "leverbon")],
           ["loonbrief"], "Een loonbrief is een personeelsdocument, geen commercieel document."),
    tabel("Welke afdeling doet dit bij een aankoop?",
          [("de bestelling plaatsen", "aankoop"), ("de goederen ontvangen en tellen", "logistiek"), ("de factuur boeken en betalen", "boekhouding")],
          "De aankoop bestelt, de logistiek ontvangt, de boekhouding boekt en betaalt.",
          kolommen=["aankoop", "logistiek", "boekhouding"]),
    mk("De factuur vermeldt een hoger bedrag dan de offerte. Wat doe je?",
       ["Je contacteert de leverancier.", "Je betaalt, want de factuur telt.", "Je stuurt zelf een creditnota.", "Je gooit de factuur gewoon weg."], 0,
       "Je vraagt uitleg en zo nodig een creditnota."),
    tabel("Controleer je dit op een inkomende factuur?",
          [("de geleverde aantallen", J), ("de afgesproken prijzen", J), ("de berekening van de btw", J), ("de kleur van het briefpapier", F)],
          "En of de kortingen uit de offerte er echt op staan."),
    keuze("Bij een verkoop gebruik je [[*dezelfde|helemaal andere]] documenten als bij een aankoop; enkel je rol wisselt.",
          "Van koper naar verkoper."),
    inv("Een factuur vermeldt 12 stoelen aan 45 euro. Hoeveel is dat samen zonder btw, in euro? Schrijf enkel het getal.", ["540"],
        "12 × 45 = 540 euro. Narekenen hoort bij de controle."),
    sleep("De klant vraagt met een [[prijsaanvraag]] wat iets kost. De leverancier antwoordt met een [[offerte]].",
          ["factuur", "leverbon"], "De eerste twee stappen van de documentenstroom."),
    open_("Waarom vergelijkt een magazijnier de leverbon met de bestelbon voor hij tekent?",
          "Zo ziet hij of alles wat besteld werd ook echt geleverd is, in dezelfde aantallen. Ontbreekt er iets, dan kan hij het meteen melden, zodat de onderneming niet betaalt voor goederen die nooit aankwamen.",
          "Controle voorkomt dat je te veel betaalt."),
    keuze("Een creditnota maakt de [[*verkoper|koper]] bij een retour, een korting achteraf of een fout op de factuur.",
          "Ze zet de factuur recht."),
    keuze("Het document waarmee de klant schriftelijk zegt wat hij wil, in welke aantallen en aan welke prijs, is de [[*bestelbon|offerte|leverbon]].",
          "De bestelbon komt van de koper."),
    mk("Waarvoor dient een orderbevestiging?",
       ["De klant weet dat de bestelling binnen is.", "De klant vraagt er de prijs mee op bij twee firma's.", "De leverancier vraagt er de betaling mee.", "De leverancier zet er een fout mee recht."], 0,
       "Ze geeft zekerheid: de bestelling is aangekomen, en wanneer ze geleverd wordt."),
    tabel("Is dit een commercieel document?",
          [("de offerte", J), ("de creditnota", J), ("de loonbrief", F), ("de orderbevestiging", J)],
          "Een loonbrief is een personeelsdocument."),
    keuze("Een factuur controleer je tegen de [[*bestelbon en de leverbon|offerte en de loonbrief|creditnota en het organogram]].",
          "Zo betaal je enkel wat je bestelde en ook kreeg."),
    tabel("Hoort dit bij een correct opgesteld commercieel document?",
          [("een duidelijke datum", J), ("een kloppende berekening", J), ("een nummer om het terug te vinden", J), ("een fout die je later wel rechtzet", F)],
          "Wie zijn documenten laat kloppen, levert kwaliteit af."),
    keuze("De factuur komt meestal als [[*laatste|eerste]] document, tenzij er nog een [[*creditnota|prijsaanvraag]] volgt.",
          "Er kan nog iets terug moeten."),
]
