"""Bestanden beheren en bewaren — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Eigen vragen strikt binnen te_bewaren, met een zelfgetekend venster van een
bestandsbeheerder om mappen, pad en bestandsnamen aan te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS

VK = Prent("verkenner-mappen", "", "venster van een bestandsbeheerder met een mappenboom links, een pad bovenaan en bestanden rechts, met letters A tot F")
VK.rect(60, 40, 880, 560, "#ffffff", DONKER, 12)
VK.rect(60, 40, 880, 54, "#eceae4", DONKER, 12)
VK.rect(150, 54, 470, 28, "#ffffff", GRIJS, 6)
VK.tekst(162, 74, "Documenten > Boekhouding > 2027 > Aankoop", 16, "start")
VK.rect(670, 54, 210, 28, "#ffffff", GRIJS, 6); VK.tekst(682, 74, "Zoeken...", 16, "start", kleur=GRIJS)
VK.lijn(300, 94, 300, 600, GRIJS, 1)
boom = [(80, 130, "Documenten"), (100, 165, "Boekhouding"), (120, 200, "2026"), (120, 235, "2027"), (140, 270, "Aankoop"), (140, 305, "Verkoop"), (100, 340, "Personeel"), (100, 375, "Marketing"), (80, 530, "Prullenbak")]
for x, y, t in boom:
    VK.rect(x, y - 14, 18, 14, "#e8c66a", "#b8962a", 2, 1)
    VK.tekst(x + 26, y, t, 17, "start", vet=(t == "Aankoop"))
bestanden = [("2027-01-factuur-dewolf.pdf", "pdf"), ("2027-02-factuur-vermeulen.pdf", "pdf"), ("2027-02-bestelbon-vermeulen.docx", "docx"), ("scan 1 (2) - kopie.pdf", "pdf"), ("2027-03-overzicht-aankopen.xlsx", "xlsx")]
for i, (n, _) in enumerate(bestanden):
    y = 140 + i * 50
    VK.rect(330, y - 18, 16, 20, "#f4f2ec", DONKER, 2, 1)
    VK.tekst(360, y, n, 17, "start")
LET = {"A": (630, 68), "B": (912, 68), "C": (274, 270), "D": (700, 290), "E": (260, 530), "F": (900, 340)}
for t, (x, y) in LET.items():
    VK.letter(x, y, t)
VK.pijl(680, 290, 600, 290, DONKER, 2)   # D wijst naar bestand 4 (y=290)
VK.pijl(880, 340, 650, 340, DONKER, 2)   # F wijst naar bestand 5
U = "verkenner-mappen.svg"
Z = {t: Prent.rond(x, y, 30) for t, (x, y) in LET.items()}
Z["A"] = Prent.zone(150, 50, 505, 36)
Z["B"] = Prent.zone(680, 50, 255, 36)

VRAGEN = [
    klik("Klik op het pad van de map die nu open staat.", U, [Z["A"]],
         "Het pad is de rij mappen van Documenten tot Aankoop."),
    klik("Klik op de letter bij de submap die nu open staat.", U, [Z["C"]],
         "Aankoop is een submap van 2027, die zelf in Boekhouding zit."),
    klik("Klik op de letter bij het bestand met een slechte bestandsnaam.", U, [Z["D"]],
         "Uit 'scan 1 (2) - kopie' leer je niet wat erin staat, en er staan spaties en haakjes in."),
    klik("Klik op de letter bij de plaats waar een gewist bestand eerst terechtkomt.", U, [Z["E"]],
         "De prullenbak: pas als je die leegmaakt is het bestand echt weg."),
    klik("Klik op de letter bij het bestand dat je opent in een rekenblad.", U, [Z["F"]],
         "De extensie .xlsx hoort bij een rekenblad."),
    casus("Bekijk het venster.", [
        tabel("Klopt dit volgens het venster?",
              [("De map Aankoop zit in de map 2027.", J), ("De map Personeel zit in Boekhouding.", F), ("De bestanden staan op datum doordat de datum vooraan in de naam staat.", J), ("Er staan twee bestanden over Vermeulen in de map.", J)],
              "Personeel staat naast Boekhouding, niet erin."),
        inv("Hoeveel pdf-bestanden staan er in de map Aankoop? Schrijf enkel het getal.", ["3"],
            "Drie bestanden eindigen op .pdf."),
        keuze("Een betere naam voor het bestand in D, een factuur van maart van Peeters, is [[*2027-03-factuur-peeters.pdf|factuur peeters maart!!.pdf|scan-nieuw-def.pdf]].",
              "Datum vooraan, dan waarover het gaat en voor wie, zonder spaties of rare tekens."),
    ]),
    tabel("Is dit een goede bestandsnaam?",
          [("2027-04-loonbrief-janssens.pdf", J), ("nieuw document (3).docx", F), ("def def ECHT def.xlsx", F), ("2027-q1-btw-aangifte.pdf", J)],
          "Een goede naam zegt wat erin staat en zet de datum vooraan."),
    koppel("Welk soort bestand hoort bij welke extensie?",
           [(".docx", "tekstdocument"), (".xlsx", "rekenblad"), (".pptx", "presentatie"), (".pdf", "vast opgemaakt document")], ["programma"],
           "Een programma heeft vaak de extensie .exe."),
    sorteer("Blijft het origineel staan?", ["ja", "nee"],
            [("kopiëren", "ja"), ("verplaatsen", "nee"), ("hernoemen", "nee"), ("een back-up maken", "ja")],
            "Kopiëren en een back-up maken laten het origineel staan; verplaatsen en hernoemen veranderen het."),
    keuze("Twee bestanden met dezelfde naam kunnen bestaan als ze in [[*een andere map|dezelfde map]] staan.",
          "Hun pad is dan verschillend."),
    volgorde("Bouw een logische mappenstructuur van breed naar smal.",
             ["Boekhouding", "2027", "Verkoop", "2027-05-factuur-claes.pdf"],
             "Eerst het onderwerp, dan het jaar, dan het soort, dan het bestand."),
    mk("Een bureaublad staat vol losse bestanden. Wat is de beste aanpak?",
       ["mappen per onderwerp maken en alles erin zetten", "alles samen in één grote map met de naam Varia slepen", "eerst alle bestanden wissen die je niet herkent", "alle bestandsnamen korter maken dan acht tekens"], 0,
       "Een vaste indeling met duidelijke namen maakt orde."),
    tabel("Offline of online back-up?",
          [("een externe schijf die je na het kopiëren loskoppelt", "offline"), ("een kopie op een server in de cloud", "online"), ("een usb-stick in de kluis", "offline"), ("een dienst die elke nacht kopieert naar een datacenter", "online")],
          "Offline staat los van het internet, online op een server elders.",
          kolommen=["offline", "online"]),
    mk("De laptop van de zaak wordt gestolen. Welke back-up redt de boekhouding?",
       ["een kopie op een externe schijf thuis", "een tweede map met kopieën op dezelfde laptop", "de inhoud van de prullenbak van de laptop", "een snelkoppeling naar de map op het bureaublad"], 0,
       "Een back-up hoort op een ander toestel of een andere plaats."),
    keuze("Een boekhouding bewaar je best [[*dagelijks|één keer per jaar|enkel bij het afsluiten]] in een back-up.",
          "Anders verlies je alles sinds de laatste kopie."),
    tabel("Uploaden of downloaden?",
          [("een factuur van je laptop naar de cloud zetten", "uploaden"), ("een handleiding van een website halen", "downloaden"), ("een foto naar een webwinkel sturen", "uploaden"), ("een bijlage uit je mail op je toestel bewaren", "downloaden")],
          "Uploaden gaat naar een server, downloaden komt ervan.",
          kolommen=["uploaden", "downloaden"]),
    keuze("Je past een bestand aan op je laptop. Door [[*synchroniseren|downloaden|hernoemen]] is het ook in de cloud meteen aangepast.",
          "Synchroniseren houdt het bestand overal hetzelfde."),
    mk("Wanneer geraak je niet aan je bestanden in de cloud?",
       ["zonder internet", "op een ander toestel", "als een collega het ook open heeft", "na het synchroniseren"], 0,
       "Cloudopslag bereik je via het internet."),
    tabel("Welk recht geef je bij het delen?",
          [("een klant die enkel de offerte moet zien", "alleen lezen"), ("een collega die mee de planning invult", "bewerken"), ("de boekhouder die de cijfers enkel nakijkt", "alleen lezen"), ("een collega die mee de folder schrijft", "bewerken")],
          "Geef alleen lezen als de ander niets hoeft te wijzigen.",
          kolommen=["alleen lezen", "bewerken"]),
    mk("Een lijst met adressen van klanten wordt gedeeld met een link die iedereen kan openen. Wat is het probleem?",
       ["Wie de link krijgt, ziet de persoonsgegevens.", "De lijst wordt na het delen automatisch gewist.", "Een deellink werkt enkel op dezelfde computer.", "Het bestand verliest door het delen zijn extensie."], 0,
       "Deel gevoelige gegevens per persoon en enkel met wie ze nodig heeft."),
    tabel("Hoort dit bij het veilig bewaren van gegevens van werknemers?",
          [("een wachtwoord op het bestand", J), ("enkel de personeelsdienst erbij laten", J), ("een back-up op een andere plaats", J), ("het bestand op een openbare schijf zetten", F)],
          "Persoonsgegevens mogen niet bij wie ze niet nodig heeft."),
    keuze("Een collega wijzigt een gedeeld bestand in de cloud. Jij ziet de wijziging [[*ook|niet]], want er is maar één bestand.",
          "Daarom werkt samenwerken in de cloud."),
    sleep("De rij mappen tot een bestand heet het [[pad]]. Het stukje achter de punt in de naam is de [[extensie]].",
          ["back-up", "submap"], "Twee begrippen uit dit hoofdstuk."),
    tabel("Wat moet een zaak afspreken over haar documenten?",
          [("waar ze bewaard worden", J), ("wie eraan mag", J), ("hoe lang ze bijgehouden worden", J), ("welke kleur de mappen krijgen", F)],
          "Voor een boekhouding legt de wet de bewaartermijn vast."),
    klik("Klik op de letter bij het deel waar je een bestand op naam terugvindt zonder door de mappen te klikken.", U, [Z["B"]],
         "In het zoekvak typ je een stuk van de naam. Met een goede naam vind je het meteen."),
    tabel("Klopt dit over de prullenbak?",
          [("Een gewist bestand kan je uit de prullenbak terugzetten.", J), ("Een teruggezet bestand gaat naar de map waar het stond.", J), ("Na het leegmaken van de prullenbak kan je het nog terugzetten.", F)],
          "Pas als je de prullenbak leegmaakt is het echt weg."),
    mk("Waarom gebruik je streepjes in plaats van spaties in een bestandsnaam?",
       ["Spaties geven soms problemen bij doorsturen.", "Streepjes maken het bestand een stuk kleiner.", "Een naam met spaties wordt nooit opgeslagen.", "Spaties veranderen de extensie van het bestand."], 0,
       "Bij doorsturen of op een website gaat het met spaties soms mis."),
    open_("Een kleine zaak bewaart al haar facturen enkel op de computer aan de kassa. Geef twee maatregelen om ze niet te verliezen en zeg waarom.",
          "Een back-up maken op een externe schijf die niet in de winkel blijft, en een online back-up in de cloud. Als de kassacomputer stuk gaat, gestolen wordt of afbrandt, staan de facturen nog op een andere plaats.",
          "Een back-up hoort op een andere plaats dan het origineel."),
]
