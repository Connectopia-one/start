"""Feedback en verbindend communiceren — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_feedback: feedback geven en ontvangen, het 4G-model, de
ik-boodschap, verbindend communiceren in vier stappen, geweldloze
communicatie en herstelgerichte vragen. Met een zelfgetekende
feedbackboodschap."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ORANJE

FB = Prent("feedback-kring", "Begeleider Ines geeft feedback aan Mo (10)", "vijf tekstballonnen in een willekeurige volgorde, letters A tot E")
ZINNEN = [("A", "Daardoor moest de hele groep telkens opnieuw beginnen."),
          ("B", "Je kwam vandaag drie keer te laat in de kring."),
          ("C", "Jij bent echt onbetrouwbaar."),
          ("D", "Ik zou graag hebben dat je om negen uur in de kring zit."),
          ("E", "Dat maakte me wat ongeduldig.")]
Z = {}
for i, (t, zin) in enumerate(ZINNEN):
    y = 70 + i * 108
    FB.rect(80, y, 840, 80, "#ffffff", ORANJE, 26, 3)
    FB.pad(f"M 110 {y + 80} L 95 {y + 100} L 140 {y + 80}", "#ffffff", ORANJE, 3)
    FB.letter(130, y + 40, t)
    FB.tekst(170, y + 48, zin, 22, "start")
    Z[t] = [Prent.zone(80, y, 840, 80)]
U = "feedback-kring.svg"

RUZIE = ("Lees de situatie.\n\n"
         "In de jeugdbeweging hebben Lars en Wout ruzie gemaakt. Wout duwde Lars in de modder, en de nieuwe jas van Lars is vuil. "
         "De leiding neemt de twee jongens apart en werkt herstelgericht.")

VRAGEN = [
    klik("Bekijk de zinnen. Klik op de zin die het gevolg benoemt.", U, Z["A"], "Het gevolg: wat er door het gedrag gebeurd is."),
    klik("Klik op de zin die het gevoel benoemt.", U, Z["E"], "Wat het gedrag bij Ines teweegbracht."),
    klik("Klik op de zin met het gewenste gedrag.", U, Z["D"], "Tot slot zeg je wat je graag anders zou zien."),
    klik("Klik op de zin die niet in goede feedback hoort.", U, Z["C"], "Feedback gaat over gedrag, nooit over wie iemand is."),
    sorteer("Welke stap van verbindend communiceren?", ["waarneming", "gevoel", "behoefte", "verzoek"],
            [("'Ik zie dat de afwas nog in de gootsteen staat.'", "waarneming"), ("'Ik voel me moe en wat geïrriteerd.'", "gevoel"), ("'Ik heb nood aan een opgeruimde keuken.'", "behoefte"), ("'Wil je de afwas doen voor het avondeten?'", "verzoek"), ("'Je kwam vandaag twintig minuten later.'", "waarneming"), ("'Ik ben ongerust.'", "gevoel")],
            "Waarneming, gevoel, behoefte, verzoek."),
    tabel("Ik-boodschap of jij-boodschap?",
          [("'Ik schrik als er plots geroepen wordt.'", "ik-boodschap"), ("'Jij roept altijd zo hard.'", "jij-boodschap"), ("'Ik word onrustig als het lawaai blijft duren.'", "ik-boodschap"), ("'Jij bent echt onmogelijk vandaag.'", "jij-boodschap")],
          "Een ik-boodschap vertrekt bij wat jij ziet en voelt.", ["ik-boodschap", "jij-boodschap"]),
    casus(RUZIE, [
        volgorde("Zet de herstelgerichte vragen in een logische volgorde.",
                 ["Wat is er gebeurd?", "Wie heeft er last van?", "Wat heb je nodig om het goed te maken?"],
                 "Eerst het verhaal, dan wie geraakt is, dan het herstel."),
        keuze("Herstelgericht werken richt zich hier vooral op [[*het herstellen van wat kapot ging|een zo zwaar mogelijke straf|wie het meest schuld heeft]].", "Herstel, geen straf."),
        mk("Waarom hoort de leiding eerst de twee jongens?",
           ["iedereen krijgt zijn eigen verhaal", "zo kan ze sneller straffen", "omdat Lars altijd liegt", "omdat de jas dan vanzelf weer helemaal schoon wordt"],
           0, "Eerst het verhaal van beide kanten, voor er iets beslist wordt."),
        open_("Wout wil het goedmaken. Bedenk een herstel dat past bij wat er gebeurd is.",
              "Wout zegt sorry en helpt Lars de jas schoon te maken, of vraagt zijn ouders om de jas te laten wassen. Samen spreken ze af hoe ze volgende keer een ruzie oplossen."),
    ]),
    koppel("Koppel de G van het 4G-model aan het voorbeeld.",
           [("gedrag", "'Je liet je fiets voor de deur liggen.'"), ("gevoel", "'Ik schrok ervan.'"), ("gevolg", "'Oma struikelde er bijna over.'"), ("gewenst gedrag", "'Zet je fiets voortaan in de berging.'")],
           ["'Jij bent zo slordig.'"],
           "Een oordeel over iemand hoort er niet bij."),
    tabel("Verzoek of eis?",
          [("'Wil je me helpen de tafel te dekken? Als het nu niet past, is het ook goed.'", "verzoek"), ("'Jij dekt nu de tafel, punt.'", "eis"), ("'Zou je je muziek wat stiller willen zetten?'", "verzoek"), ("'Zet die muziek stil, of ik neem je gsm af.'", "eis")],
          "Als nee geen optie is, is het geen verzoek.", ["verzoek", "eis"]),
    keuze("Feedback gaat altijd over [[*gedrag|wie iemand is|iemands familie]].", "Over wat je zag, niet over de persoon."),
    mk("Je krijgt feedback die je niet meteen begrijpt. Wat doe je?",
       ["je vraagt wat de ander juist bedoelt", "je begint je meteen te verdedigen", "je doet alsof je het niet gehoord hebt", "je geeft meteen feedback terug"],
       0, "Eerst luisteren, dan navragen."),
    keuze("Een duim omhoog na een goede presentatie is [[*non-verbale|verbale]] feedback.", "Feedback kan ook zonder woorden."),
    tabel("Is dit een waarneming zonder oordeel?",
          [("'Je kwam tien minuten later dan afgesproken.'", J), ("'Je bent onbetrouwbaar.'", F), ("'Je nam drie keer je gsm tijdens de les.'", J), ("'Je bent altijd zo ongeïnteresseerd.'", F)],
          "Een waarneming beschrijft wat je zag of hoorde."),
    inv("Hoe noem je de laatste G van het 4G-model? Twee woorden.", ["gewenst gedrag", "het gewenste gedrag", "gewenste gedrag"], "Gewenst gedrag."),
    tabel("Is dit een kenmerk van geweldloze communicatie?",
          [("respectvol", J), ("dwingend", F), ("empathisch", J), ("direct", J), ("spottend", F)],
          "Direct, doeltreffend, emotioneel, empathisch en respectvol."),
    mk("Welke zin is empathisch?",
       ["'Het lijkt me echt moeilijk dat je opa ziek is.'", "'Daar moet je niet zo lang over zeuren, hoor.'", "'Dat heb ik ook al eens gehad, dus ik weet precies hoe het zit.'", "'Ga maar gewoon iets leuks doen, dan vergeet je het.'"],
       0, "Je leeft je in de ander in."),
    sleep("Verbindend communiceren gaat in vier stappen: eerst de [[waarneming]], dan het [[gevoel]], dan de [[behoefte]] en tot slot een [[verzoek]].",
          ["straf", "bevel"],
          "Straffen en bevelen horen er niet bij."),
    keuze("Positieve feedback werkt [[*even sterk als|veel minder goed dan]] zeggen wat beter kan.", "Zeggen wat goed loopt, is ook feedback."),
    mk("Een collega zegt: 'Jij kunt echt niet plannen!' Welke ik-boodschap is beter?",
       ["'Ik raak gestrest als de planning op het laatste moment verandert.'", "'Jij moet echt eens leren plannen, zoals ik.'", "'Iedereen vindt dat jij slecht plant.'", "'Ik vind dat jij echt nooit iets goed kunt plannen, dat weet iedereen hier.'"],
       0, "Een echte ik-boodschap vertrekt bij jezelf, niet bij een oordeel over de ander."),
    keuze("'Doe het nu, en ik wil geen nee horen' is een [[*eis|verzoek|waarneming]].", "Bij een verzoek mag nee."),
    tabel("Klopt dit over herstelgericht werken?",
          [("Iedereen krijgt de kans om zijn verhaal te doen.", J), ("Het doel is vooral een straf vinden.", F), ("Wie last had, mag zeggen wat hij nodig heeft.", J), ("De begeleider beslist alles zonder te luisteren.", F)],
          "Samen zoek je hoe het hersteld raakt."),
    inv("Welke stap komt na de waarneming bij verbindend communiceren? Eén woord.", ["gevoel", "het gevoel"], "Het gevoel."),
    keuze("Je benoemt je gevoel, zodat de ander [[*beter begrijpt wat zijn gedrag teweegbrengt|zich schuldig moet voelen|meteen gestraft wordt]].", "Zo weet hij wat zijn gedrag met jou doet."),
    mk("Welke feedback is positief en concreet?",
       ["'Je hebt alle bekers netjes in de kast gezet, dank je!'", "'Goed zo.'", "'Je bent de beste van de hele wereld en ver daarbuiten!'", "'Het was oké, denk ik, maar ook niet echt super.'"],
       0, "Je benoemt precies welk gedrag goed was."),
    keuze("Wie zich inleeft in de ander, communiceert [[*empathisch|dwingend|oppervlakkig]].", "Je probeert te voelen hoe het voor de ander is."),
    mk("Waarom hoort 'Jij bent zo slordig' niet in goede feedback?",
       ["het gaat over wie iemand is, niet over gedrag", "het is veel te kort om echte feedback te kunnen zijn", "slordig zijn bestaat niet", "het is te positief"],
       0, "Feedback benoemt gedrag dat je zag."),
    open_("Een klasgenoot leent elke dag je pen zonder het te vragen. Geef hem feedback met het 4G-model.",
          "Gedrag: je nam vandaag weer mijn pen zonder te vragen. Gevoel: dat ergert me. Gevolg: ik zat zonder pen tijdens het dictee. Gewenst gedrag: vraag het voortaan eerst."),
]
