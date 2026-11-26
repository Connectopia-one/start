"""Humane wetenschappen: globalisering, de VN en de Europese Unie — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen, enkel humane
wetenschappen). Eigen vragen in examenvorm en een eigen schema van hoe een
Europese wet tot stand komt, met de instellingen enkel als letter en rol.
Strikt binnen beyond/bron/sg_hw_globalisering.py."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

EU = Prent("eu-wetgeving", "Hoe een Europese wet tot stand komt (vereenvoudigd)",
           "vier vakken met een letter en een rol: A staatshoofden en regeringsleiders, bepalen de grote lijnen; B stelt wetten voor; C rechtstreeks gekozen door de burgers; D vakministers van de lidstaten; pijlen van B naar C en D, en van C en D samen naar een vak 'Europese wet'")
VAK = {"A": (290, 70, 420, 100, ["staatshoofden en regeringsleiders", "bepalen de grote lijnen"]),
       "B": (330, 230, 340, 100, ["stelt nieuwe wetten voor", "en voert het beleid uit"]),
       "C": (60, 390, 340, 100, ["rechtstreeks gekozen", "door de burgers"]),
       "D": (600, 390, 340, 100, ["vakministers van", "de lidstaten"])}
for k, (x, y, b, h, regels) in VAK.items():
    EU.rect(x, y, b, h, LICHTGROEN, DONKER, 14, 2)
    EU.letter(x + 36, y + h / 2, k)
    for i, r in enumerate(regels):
        EU.tekst(x + b / 2 + 25, y + h / 2 - 6 + i * 24, r, 18)
EU.lijn(500, 170, 500, 230, DONKER, 2, stippel=True)
EU.tekst(515, 205, "richting", 15, "start")
EU.pijl(420, 330, 260, 390, DONKER, 3)
EU.pijl(580, 330, 740, 390, DONKER, 3)
EU.tekst(300, 350, "voorstel", 16)
EU.tekst(700, 350, "voorstel", 16)
EU.rect(390, 540, 220, 70, "#ffffff", DONKER, 14, 3)
EU.tekst(500, 583, "Europese wet", 22, vet=True)
EU.pijl(230, 490, 400, 560, DONKER, 3)
EU.pijl(770, 490, 600, 560, DONKER, 3)
EU.tekst(500, 520, "beslissen samen", 16)


def inst(k):
    x, y, b, h, _ = VAK[k]
    return [Prent.zone(x, y, b, h)]


VRAGEN = [
    klik("Klik op de Europese Commissie.", EU.bestand, inst("B"),
         "De Commissie heeft het initiatiefrecht: ze stelt nieuwe Europese wetten voor en voert het beleid uit."),
    klik("Klik op het Europees Parlement.", EU.bestand, inst("C"),
         "Het Europees Parlement is de enige EU-instelling die rechtstreeks door de burgers gekozen wordt."),
    klik("Klik op de Raad van de Europese Unie.", EU.bestand, inst("D"),
         "In de Raad van de EU zitten de vakministers van de lidstaten."),
    klik("Klik op de instelling die geen wetten maakt, maar de prioriteiten van de EU bepaalt.", EU.bestand, inst("A"),
         "De Europese Raad met de staatshoofden en regeringsleiders bepaalt de grote lijnen."),
    klik("Klik op de instelling die vooral de belangen van de lidstaten vertegenwoordigt bij het goedkeuren van wetten.", EU.bestand, inst("D"),
         "In de Raad van de EU zitten de ministers van de lidstaten. Het Parlement vertegenwoordigt de burgers."),
    met_prent(EU.bestand, keuze("Een Europese wet komt er pas als [[*C en D|A en B|B en C]] allebei akkoord gaan.",
              "Bij de gewone wetgevingsprocedure beslissen het Parlement en de Raad van de EU samen.")),
    met_prent(EU.bestand, keuze("Vak A is de [[*Europese Raad|Raad van de Europese Unie|Europese Commissie]]. Vak D is de [[*Raad van de Europese Unie|Europese Raad|Europese Commissie]].",
              "Ze lijken op elkaar qua naam, maar de Europese Raad bestaat uit de regeringsleiders en de Raad van de EU uit de vakministers.")),
    met_prent(EU.bestand, volgorde("Zet de stappen van een Europese wet over verpakkingen in een logische volgorde.", [
        "de regeringsleiders maken van milieu een prioriteit",
        "de Commissie stelt een nieuwe regel voor",
        "het Parlement en de Raad van de EU keuren de regel goed",
        "de regel geldt in de lidstaten",
    ], "Eerst de richting, dan het voorstel, dan de beslissing en dan de toepassing.")),
    koppel("Koppel de organisatie aan haar opdracht.", [
        ["Verenigde Naties", "vrede en veiligheid in de wereld bewaren"],
        ["NAVO", "militair bondgenootschap dat de leden samen verdedigt"],
        ["WHO", "de gezondheid van mensen wereldwijd bevorderen"],
        ["Internationaal Strafhof", "personen berechten voor genocide en oorlogsmisdaden"],
        ["Europees Hof van de Rechten van de Mens", "oordelen over staten die mensenrechten schenden"],
    ], ["Europese wetten voorstellen"], "Elke organisatie met haar kernopdracht."),
    tabel("Is dit een instelling van de Europese Unie?", [
        ("het Europees Parlement", J),
        ("de Veiligheidsraad", F),
        ("de Europese Commissie", J),
        ("het Internationaal Strafhof", F),
    ], "De Veiligheidsraad hoort bij de VN. Het Internationaal Strafhof is geen instelling van de EU."),
    tabel("Is dit een verordening of een richtlijn?", [
        ("Een regel geldt meteen en op dezelfde manier in alle lidstaten.", "verordening"),
        ("Europa legt een doel vast en elk land kiest zelf hoe het dat bereikt.", "richtlijn"),
        ("Vlaanderen moet een Europees doel voor fijn stof omzetten in eigen maatregelen.", "richtlijn"),
    ], "Een verordening is meteen bindend, een richtlijn moet worden omgezet.",
       kolommen=["verordening", "richtlijn"]),
    casus(
        "Lena zit in een Belgische gevangenis. Haar cel is zo overvol dat ze op een matras op de grond slaapt. Ze stapte naar de Belgische rechter, "
        "maar kreeg geen gelijk. Op het nieuws hoort ze ook over een legerleider die van genocide beschuldigd wordt en die in zijn eigen land niet vervolgd wordt.",
        [
            mk("Waar kan Lena nog klagen?",
               ["bij het Europees Hof van de Rechten van de Mens", "bij de Navo-top in Brussel",
                "bij het Internationaal Strafhof", "bij de Wereldgezondheidsorganisatie"], 0,
               "Een burger die in eigen land geen gelijk kreeg, kan er klagen tegen een staat die zijn mensenrechten schond."),
            keuze("Dat Europese hof zetelt in [[*Straatsburg|Den Haag|New York]] en oordeelt over [[*staten|personen]].",
                  "Het Europees Hof van de Rechten van de Mens oordeelt in Straatsburg over staten."),
            keuze("De legerleider kan berecht worden door het [[*Internationaal Strafhof|Europees Hof van de Rechten van de Mens|Hof van Cassatie]] in Den Haag.",
                  "Het Internationaal Strafhof berecht personen, ook leiders, voor de zwaarste misdaden."),
            tabel("Klopt dit over de twee hoven?", [
                ("Het Europees Hof van de Rechten van de Mens en het Internationaal Strafhof zijn hetzelfde.", F),
                ("Het Internationaal Strafhof berecht personen.", J),
                ("Het Europees Hof kan oordelen dat België een verdrag schond.", J),
            ], "Het ene hof oordeelt over staten, het andere berecht personen."),
        ],
    ),
    tabel("Klopt dit over internationale organisaties?", [
        ("België is lid van de NAVO sinds de oprichting in 1949.", J),
        ("De VN werden opgericht na de Eerste Wereldoorlog.", F),
        ("De WHO is een organisatie van de VN.", J),
        ("De G7 is een militair bondgenootschap.", F),
    ], "De VN ontstonden in 1945, na de Tweede Wereldoorlog. De G7 is een overleg van zeven rijke landen."),
    keuze("Een organisatie boven de landen, waaraan landen een deel van hun macht afstaan, is [[*supranationaal|nationaal|lokaal]].",
          "Supra betekent boven."),
    mk("Waarom staan landen een deel van hun macht af aan een supranationale organisatie?",
       ["samen hebben ze meer slagkracht bij grensoverschrijdende problemen",
        "ze willen hun eigen parlement en hun eigen regering helemaal afschaffen",
        "ze zijn wettelijk verplicht om lid te worden van elke organisatie",
        "ze moeten dan zelf geen enkele gemeenschappelijke regel meer volgen"], 0,
       "Samenwerken helpt bij vrede, handel, gezondheid of klimaat. In ruil aanvaarden landen gemeenschappelijke regels."),
    sorteer("Op welk niveau gebeurt deze actie rond klimaat?", ["Mondiaal of Europees", "Lokaal"], [
        ["landen maken afspraken over de uitstoot van de hele wereld", "Mondiaal of Europees"],
        ["een gemeente legt nieuwe fietspaden aan", "Lokaal"],
        ["de EU legt een doel vast voor fijn stof", "Mondiaal of Europees"],
        ["een stad isoleert haar scholen", "Lokaal"],
    ], "Het mondiale en het lokale niveau hangen samen: een gemeente kan mee een mondiaal probleem aanpakken."),
    mk("Een partij besmet vlees wordt in tien landen verkocht. Waarom is een Europese aanpak hier nodig?",
       ["voedsel wordt over heel Europa verhandeld",
        "enkel de VN mag regels maken over voedsel en over landbouw",
        "elk land mag zelf kiezen of het de gezondheid van zijn burgers beschermt",
        "de NAVO moet de grenzen van al die landen militair afsluiten"], 0,
       "Daarom zijn er Europese regels en een waarschuwingssysteem voor voedselveiligheid."),
    keuze("Europees recht gaat [[*voor op|achter]] nationaal recht. Een Belgische rechter moet een Belgische regel die ermee in strijd is [[*buiten toepassing laten|altijd strenger toepassen]].",
          "Daarom heeft Europese wetgeving een grote invloed op de politiek in België."),
    sleep("De Europese verkiezingen vinden om de [[vijf]] jaar plaats. Grotere landen hebben [[meer]] zetels. Elke lidstaat levert één [[commissaris]], die het belang van heel de EU moet dienen.",
          ["minder", "twee"], "Het Parlement vertegenwoordigt de burgers, de Commissie het algemeen Europees belang."),
    tabel("Welk thema vraagt hier vooral een aanpak over de grenzen heen?", [
        ("Een virus verspreidt zich met reizigers over de hele wereld.", "gezondheid"),
        ("Mensen op de vlucht reizen door verschillende landen.", "migratie"),
        ("Uitstoot in één land verwarmt de hele aarde.", "klimaat"),
    ], "Eén land alleen kan deze problemen niet oplossen.",
       kolommen=["gezondheid", "migratie", "klimaat"]),
    mk("Een Europees land wordt bedreigd door een buurland buiten de EU. Via welke organisatie loopt de gezamenlijke militaire verdediging vooral?",
       ["de NAVO", "de WHO", "de G7", "de Europese Commissie"], 0,
       "De EU werkt ook rond veiligheid, maar de gezamenlijke militaire verdediging van de meeste Europese landen loopt via de NAVO."),
    keuze("Tijdens de coronapandemie gaf de [[*WHO|NAVO|G7]] advies en richtlijnen aan de landen.",
          "De WHO is de Wereldgezondheidsorganisatie van de VN."),
    keuze("Het hoofdkwartier van de NAVO ligt in [[*Brussel|Den Haag|Straatsburg]]. Het Europees Parlement vergadert in Brussel en [[*Straatsburg|Genève|Luxemburg]].",
          "De meeste EU-instellingen zetelen in Brussel. Het Parlement vergadert ook in Straatsburg."),
    met_prent(EU.bestand, tabel("Klopt dit over het schema?", [
        ("Vak A maakt zelf de Europese wetten.", F),
        ("Vak B heeft het recht om wetten voor te stellen.", J),
        ("De leden van vak C worden door de regeringen aangeduid.", F),
        ("Via vak C spreken de burgers mee, via vak D de lidstaten.", J),
    ], "De Europese Raad maakt geen wetten. Het Parlement wordt rechtstreeks gekozen.")),
    mk("Welke omschrijving past bij de G7?",
       ["een overleg van zeven rijke landen", "een rechtbank voor oorlogsmisdaden", "een afdeling van de NAVO", "een instelling van de Europese Unie"], 0,
       "De G7 zijn de Verenigde Staten, Canada, Japan, Duitsland, Frankrijk, Italië en het Verenigd Koninkrijk. De EU zit mee aan tafel."),
    keuze("In de NAVO geldt dat een aanval op één lid geldt als een aanval op [[*alle leden|enkel de grootste leden|niemand]].",
          "De leden beloven elkaar te verdedigen."),
    open_("Leg uit hoe Europese wetgeving invloed heeft op de politiek in België. Gebruik het verschil tussen een verordening en een richtlijn en geef een voorbeeld.",
          "Een Europese verordening geldt meteen en op dezelfde manier in alle lidstaten, ook in België. Een richtlijn legt een doel vast, en elk land moet dat zelf in zijn wetten of decreten omzetten. Zo legt Europa bijvoorbeeld een grens vast voor fijn stof, waarna Vlaanderen en de steden maatregelen moeten nemen. Europees recht gaat ook voor op Belgisch recht: een rechter moet een Belgische regel die ermee in strijd is, buiten toepassing laten."),
]
