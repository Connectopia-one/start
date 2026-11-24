"""Werving, selectie en de werkplek — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_hr, met een zelfgetekende vacature om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, LICHTGROEN, DONKER, GROEN

VA = Prent("vacature-magazijnier", "", "vacature voor een magazijnier met zeven regels en letters A tot G")
VA.rect(70, 30, 860, 580, "#ffffff", DONKER, 14, 3)
VA.rect(70, 30, 860, 70, LICHTGROEN, DONKER, 14, 3)
VA.tekst(500, 76, "Fietsen Trappers zoekt een magazijnier (m/v/x)", 26, vet=True)
REGELS = [
    ("A", "Je ontvangt leveringen, slaat fietsen op en maakt bestellingen klaar."),
    ("B", "Je hebt een diploma secundair onderwijs."),
    ("C", "Je werkte al minstens één jaar in een magazijn."),
    ("D", "Je kan met een heftruck rijden en een rekenblad gebruiken."),
    ("E", "Je bent punctueel, nauwkeurig en je werkt graag samen."),
    ("F", "Wij bieden een vast contract, een fietsvergoeding en opleiding."),
    ("G", "Stuur je cv en je sollicitatiebrief vóór 15 december."),
]
Y0, DY = 160, 66
for i, (t, r) in enumerate(REGELS):
    y = Y0 + i * DY
    VA.letter(120, y - 7, t)
    VA.tekst(160, y, r, 21, "start")
U = "vacature-magazijnier.svg"
Z = {t: Prent.rond(120, Y0 + i * DY - 7, 30) for i, (t, _) in enumerate(REGELS)}

VRAGEN = [
    klik("Klik op de letter bij de regel die een attitude vraagt.", U, [Z["E"]],
         "Punctueel en nauwkeurig zijn, graag samenwerken: dat is een houding, iets dat je bent."),
    klik("Klik op de letter bij de regel die ervaring vraagt.", U, [Z["C"]],
         "Ervaring is wat je al deed; een diploma is je opleidingsniveau."),
    klik("Klik op de letter bij de regel met vaardigheden.", U, [Z["D"]],
         "Met een heftruck rijden en een rekenblad gebruiken is iets dat je kan."),
    klik("Klik op de letter bij het aanbod van de onderneming.", U, [Z["F"]],
         "Het aanbod en de verloning horen in een vacature; anders solliciteert niemand."),
    klik("Klik op de letter bij de functiebeschrijving: wat de job inhoudt.", U, [Z["A"]],
         "De taken van de magazijnier."),
    tabel("Hoort deze regel bij de functiebeschrijving of bij het functieprofiel?",
          [("A", "functiebeschrijving"), ("B", "functieprofiel"), ("D", "functieprofiel"), ("E", "functieprofiel")],
          "De beschrijving gaat over de job, het profiel over de persoon die je zoekt.",
          kolommen=["functiebeschrijving", "functieprofiel"]),
    sorteer("Vaardigheid of attitude?", ["vaardigheid", "attitude"],
            [("een kassa bedienen", "vaardigheid"), ("vriendelijk blijven bij drukte", "attitude"), ("een heftruck besturen", "vaardigheid"), ("op tijd komen", "attitude"), ("een offerte opmaken in een rekenblad", "vaardigheid"), ("eerlijk zijn", "attitude")],
            "Een vaardigheid is iets dat je kan, een attitude iets dat je bent."),
    volgorde("Zet de stappen van een eenvoudige selectieprocedure in de juiste volgorde.",
             ["De vacature opstellen.", "De vacature bekendmaken.", "De cv's screenen.", "Gesprekken voeren met de beste kandidaten.", "Een keuze maken en die laten weten."],
             "Eerst weten wie je zoekt, dan pas bekendmaken."),
    tabel("Hoort dit in een cv?",
          [("je opleiding", J), ("je werkervaring", J), ("je rijksregisternummer", F), ("je vaardigheden", J)],
          "Je rijksregisternummer en je rekeningnummer geef je pas als je aangeworven bent."),
    koppel("Welk document hoort bij welke omschrijving?",
           [("een overzicht van je opleiding, ervaring en vaardigheden", "cv"), ("waarom jij de job wil en erbij past", "sollicitatiebrief"), ("het bericht dat een open job aankondigt", "vacature"), ("de taken en verantwoordelijkheden van de job", "functiebeschrijving")],
           ["loonfiche"], "De loonfiche komt pas als iemand al in dienst is."),
    mk("Waarom legt een selectieverantwoordelijke elk cv naast de vacature?",
       ["Zo weegt hij elke kandidaat op dezelfde punten.", "Zo ziet hij meteen welke kandidaat het oudst is.", "Zo kan hij het juiste loon van elke kandidaat berekenen.", "Zo weet hij welke kandidaat het dichtst bij de zaak woont."], 0,
       "Een duidelijk profiel maakt het kiezen eerlijker en makkelijker."),
    keuze("Een cv hoort [[*kort en overzichtelijk|lang en uitgebreid]] te zijn, want wie tientallen cv's leest, heeft per cv maar een minuut.",
          "Eén of twee bladzijden."),
    tabel("Ervaring of opleidingsniveau?",
          [("een diploma bachelor boekhouden", "opleidingsniveau"), ("drie jaar als kassier gewerkt", "ervaring"), ("een getuigschrift tweede graad", "opleidingsniveau"), ("twee zomers vakantiewerk in een magazijn", "ervaring")],
          "Ervaring is wat je al deed, opleidingsniveau is het diploma dat je haalde.",
          kolommen=["ervaring", "opleidingsniveau"]),
    casus("Lees de situatie.\n\nYasmine werkt de hele dag aan een bureau in een boekhoudkantoor. Haar scherm staat laag naast haar, haar stoel is te hoog zodat haar voeten bengelen, en ze zit acht uur in dezelfde houding. Het licht is zwak en ze heeft 's avonds vaak hoofdpijn.", [
        tabel("Wat moet beter aan haar werkplek?",
              [("het scherm", "op ooghoogte en recht voor haar"), ("de stoel", "lager, met de voeten plat op de grond"), ("de houding", "afwisselen tussen zitten en staan"), ("het licht", "sterker licht")],
              "Een ergonomische werkplek past zich aan de mens aan.",
              kolommen=["op ooghoogte en recht voor haar", "lager, met de voeten plat op de grond", "afwisselen tussen zitten en staan", "sterker licht"]),
        keuze("Haar hoofdpijn komt wellicht door [[*het zwakke licht|de kleur van de muren|het uitzicht]].",
              "Slecht licht geeft vermoeide ogen en hoofdpijn."),
        inv("Hoe noem je het aanpassen van de werkplek aan de mens? Schrijf één woord.", ["ergonomie", "de ergonomie"],
            "Ergonomie."),
    ]),
    volgorde("Zet de stappen om een zware doos veilig op te tillen in de juiste volgorde.",
             ["Ga dicht bij de doos staan.", "Zak door je knieën met een rechte rug.", "Neem de doos vast en houd ze dicht bij je lichaam.", "Kom recht door je benen te strekken.", "Draai met je voeten, niet met je rug."],
             "Je rug blijft recht, je benen doen het werk."),
    sorteer("Veiligheid, ergonomie of hygiëne?", ["veiligheid", "ergonomie", "hygiëne"],
            [("veiligheidsschoenen in de loods", "veiligheid"), ("een regelbare bureaustoel", "ergonomie"), ("handen wassen in de keuken", "hygiëne"), ("een risicoanalyse van de machines", "veiligheid"), ("het scherm op ooghoogte", "ergonomie"), ("een propere werktafel", "hygiëne")],
            "Samen bepalen ze of iemand er gezond kan werken."),
    tabel("Klopt dit over de werkplek?",
          [("Beschermingsmiddelen zijn vrijblijvend voor de werknemer.", F), ("De werkgever moet een arbeidsongevallenverzekering afsluiten.", J), ("Een arbeidsongeval meld je meteen.", J), ("Een zware doos til je met een gebogen rug.", F)],
          "De werkgever moet beschermingsmiddelen geven en de werknemer moet ze gebruiken."),
    mk("Waarvoor dient een veiligheidsschoen met een stalen neus in een loods?",
       ["om je tenen te beschermen", "om sneller te kunnen lopen", "om de vloer niet te beschadigen", "om er netjes uit te zien"], 0,
       "Een vallende doos of een rolwagen kan je tenen verpletteren."),
    keuze("Bij een risicoanalyse ga je [[*vooraf|achteraf]] na wat er kan mislopen en neem je maatregelen.",
          "Je spoort de gevaren op voor er iets gebeurt."),
    mk("Een magazijnier verstuikt zijn enkel op het werk. Wat moet de werkgever doen?",
       ["het aangeven bij de verzekering", "niets, want het is de fout van de werknemer", "de werknemer meteen ontslaan om het risico", "de dokter zelf betalen uit de kas van de zaak"], 0,
       "Een arbeidsongeval meld je meteen; de werkgever geeft het aan bij de verzekering."),
    sleep("Een [[vacature]] kondigt een open job aan. In je [[sollicitatiebrief]] schrijf je waarom je de job wil.",
          ["loonbrief", "organogram"], "Twee documenten bij het solliciteren."),
    open_("Waarom zet een onderneming het aanbod en de verloning in haar vacature?",
          "Kandidaten willen weten wat ze krijgen: het loon, het soort contract en extra's zoals opleiding of een fietsvergoeding. Zonder aanbod solliciteert bijna niemand, of solliciteren mensen voor wie de job toch niet past.",
          "Een vacature is ook reclame voor de onderneming."),
    keuze("Wie lang aan een scherm werkt, wisselt best zijn [[*taken en houding|stoel en bureau|collega's]] af om niet stijf te worden.",
          "Afwisseling spaart je rug, je nek en je ogen."),
    klik("Klik op de letter bij de regel die het gevraagde opleidingsniveau noemt.", U, [Z["B"]],
         "Het diploma secundair onderwijs is het opleidingsniveau."),
    keuze("Na het screenen van de cv's worden de beste kandidaten uitgenodigd voor een [[*sollicitatiegesprek|functioneringsgesprek|ontslaggesprek]].",
          "Daarin stellen ze zichzelf voor."),
    tabel("Is dit een kenmerk van een ergonomische werkplek?",
          [("een regelbare stoel", J), ("genoeg ruimte voor je benen", J), ("weinig licht om de ogen te sparen", F), ("het scherm op armlengte", J)],
          "Te weinig licht is juist slecht voor je ogen."),
    mk("Wat is het verschil tussen een functiebeschrijving en een functieprofiel?",
       ["Het eerste gaat over de job, het tweede over de persoon.", "Het eerste gaat over het loon, het tweede over de taken.", "Het eerste schrijft de kandidaat, het tweede de werkgever.", "Er is geen verschil: het zijn twee woorden voor hetzelfde."], 0,
       "De beschrijving zegt wat de job inhoudt, het profiel wie je ervoor zoekt."),
    keuze("Een werkplek in een keuken of een zorgcentrum moet vooral [[*hygiënisch|ergonomisch|stil]] zijn.",
          "Waar met voeding of met mensen gewerkt wordt, is netheid extra belangrijk."),
]
