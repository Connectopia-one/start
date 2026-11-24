"""Bedrijfsstrategie: missie, visie, SWOT en stakeholders — pittig (🚀 Boost doorstroom, economie).

Eigen vragen strikt binnen bw_strategie, met een zelfgetekende SWOT om op te klikken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GROEN, ROOD, BLAUW, ORANJE

SW = Prent("swot-leeg", "SWOT-analyse", "lege SWOT met vier vakken: sterktes, zwaktes, kansen, bedreigingen, met intern en extern aangeduid")
SW.tekst(110, 250, "INTERN", 20, vet=True); SW.tekst(110, 470, "EXTERN", 20, vet=True)
VAK = {"S": (200, 140, "#e8f0dd", "Sterktes"), "W": (560, 140, "#f6e2dc", "Zwaktes"), "O": (200, 360, "#e3ebf3", "Kansen"), "T": (560, 360, "#f6ead4", "Bedreigingen")}
Z = {}
for k, (x, y, kleur, naam) in VAK.items():
    SW.rect(x, y, 340, 200, kleur, DONKER, 10, 2)
    SW.tekst(x + 170, y + 110, naam, 28, vet=True)
    Z[k] = Prent.zone(x, y, 340, 200)
SW.tekst(370, 120, "helpt", 20, vet=True); SW.tekst(730, 120, "hindert", 20, vet=True)
U = "swot-leeg.svg"

VRAGEN = [
    klik("Fietsenwinkel Trapkracht heeft drie zeer ervaren herstellers. Klik op het vak waar dat hoort.", U, [Z["S"]],
         "Het zit in het bedrijf zelf en helpt: een sterkte."),
    klik("De gemeente plant een nieuwe fietssnelweg vlak bij de winkel. Klik op het vak waar dat hoort.", U, [Z["O"]],
         "Het komt van buiten en is gunstig: een kans."),
    klik("Een grote webwinkel verkoopt dezelfde fietsen veel goedkoper. Klik op het vak waar dat hoort.", U, [Z["T"]],
         "Het komt van buiten en is ongunstig: een bedreiging."),
    klik("De winkel heeft geen eigen website. Klik op het vak waar dat hoort.", U, [Z["W"]],
         "Het zit in het bedrijf zelf en is ongunstig: een zwakte. Daar kan de winkel zelf iets aan doen."),
    casus("Lees de teksten van Bakkerij Korenaar.\n\n1. 'Wij bakken elke dag vers en ambachtelijk brood voor de mensen in onze wijk.'\n2. 'Tegen 2032 willen we drie filialen hebben en enkel nog met lokale granen werken.'\n3. 'Volgend jaar willen we de omzet met 8 % laten stijgen.'\n4. 'Eerlijkheid, vakmanschap en respect voor de natuur.'", [
        tabel("Wat is deze tekst?",
              [("tekst 1", "missie"), ("tekst 2", "visie"), ("tekst 3", "doelstelling"), ("tekst 4", "kernwaarden")],
              "Missie: waarom nu. Visie: waar naartoe. Doelstelling: meetbaar. Kernwaarden: waar je voor staat.",
              kolommen=["missie", "visie", "doelstelling", "kernwaarden"]),
        keuze("Tekst 3 is meetbaar, want hij bevat [[*een cijfer en een termijn|een mooie belofte|een kernwaarde]].",
              "Een doelstelling heeft een cijfer en een datum."),
    ]),
    sorteer("Intern of extern?", ["intern", "extern"],
            [("een verouderde kassa", "intern"), ("een nieuwe wet op verpakkingen", "extern"), ("gemotiveerd personeel", "intern"), ("stijgende energieprijzen", "extern"), ("een sterk merk", "intern"), ("een nieuwe concurrent in de straat", "extern")],
            "Sterktes en zwaktes zijn intern, kansen en bedreigingen extern."),
    tabel("Sterkte, zwakte, kans of bedreiging voor een ijssalon?",
          [("een geheim recept voor pistache-ijs", "sterkte"), ("een te kleine diepvries", "zwakte"), ("een warme zomer voorspeld", "kans"), ("de melkprijs verdubbelt", "bedreiging")],
          "Intern of extern, en helpt het of hindert het?",
          kolommen=["sterkte", "zwakte", "kans", "bedreiging"]),
    koppel("Welk belang hoort bij welke stakeholder?",
           [("aandeelhouders", "winst en dividend"), ("werknemers", "een goed loon en werkzekerheid"), ("buurtbewoners", "weinig lawaai en verkeer"), ("klanten", "goede kwaliteit aan een eerlijke prijs"), ("overheid", "belastingen en het naleven van de wet")],
           ["een hoge beurskoers voor de concurrent"], "Elke stakeholder heeft eigen belangen."),
    sorteer("Interne of externe stakeholder?", ["intern", "extern"],
            [("het personeel", "intern"), ("de leveranciers", "extern"), ("de zaakvoerder", "intern"), ("de banken", "extern"), ("de klanten", "extern"), ("de buurt", "extern")],
            "Intern zit in de onderneming zelf."),
    mk("Een fabriek wil 's nachts gaan produceren. Welke stakeholder zal het meest bezwaar hebben?",
       ["de buurtbewoners", "de aandeelhouders", "de leveranciers van grondstoffen", "de klanten in het buitenland"], 0,
       "Nachtwerk betekent lawaai en verkeer in de buurt."),
    tabel("Klopt dit over missie en visie?",
          [("Een missie gaat over vandaag, een visie over de toekomst.", J), ("Een missie is een lijst met jaarcijfers.", F), ("Ook een vzw heeft een missie.", J), ("Een visie is altijd meetbaar.", F)],
          "Meetbaar is een doelstelling."),
    keuze("De strategie van een onderneming wordt bepaald door [[*de leiding|de klanten|de buurt]].",
          "De zaakvoerder of de raad van bestuur."),
    keuze("Een strategie helpt ook om te kiezen wat je [[*niet|altijd]] doet.",
          "Kiezen is ook afwijzen."),
    keuze("SWOT staat voor strengths, weaknesses, opportunities en [[*threats|targets|tools]].",
          "Threats zijn bedreigingen."),
    tabel("Hoort dit bij een bedrijfsstrategie?",
          [("doelen op lange termijn", J), ("de keuze van de doelgroep", J), ("hoe je je onderscheidt van concurrenten", J), ("de kleur van de bureaustoelen", F)],
          "Een strategie gaat over de grote keuzes."),
    mk("Waarom laat een bedrijf zijn personeel de missie kennen?",
       ["Zo trekt iedereen dezelfde kant uit.", "Zo kan het personeel de jaarrekening maken.", "Zo hoeft het bedrijf geen visie te schrijven.", "Zo betaalt het bedrijf minder belastingen."], 0,
       "Een gedeelde missie helpt bij dagelijkse keuzes."),
    keuze("Een zwakte kan een bedrijf [[*zelf aanpakken|nooit veranderen]], bijvoorbeeld met een opleiding of een investering.",
          "Zwaktes zitten in het bedrijf zelf."),
    keuze("Wie sterktes op kansen legt, ziet waar het bedrijf [[*kan groeien|zwak staat|moet stoppen]].",
          "Zo helpt een SWOT bij keuzes."),
    sleep("De [[missie]] zegt waarom een bedrijf bestaat. De [[visie]] zegt waar het naartoe wil. Een [[doelstelling]] is meetbaar, met een cijfer en een datum.",
          ["SWOT", "stakeholder"], "Drie begrippen die je niet mag verwarren."),
    tabel("Is dit een stakeholder van een supermarkt?",
          [("de werknemers", J), ("de leveranciers", J), ("de gemeente", J), ("een supermarkt in een ander land zonder enige band", F)],
          "Een stakeholder heeft iets te winnen of te verliezen bij wat het bedrijf doet."),
    keuze("Een bedrijf schrijft: 'In 2040 zijn we het groenste transportbedrijf van Vlaanderen.' Dat is een [[*visie|missie|kernwaarde]].",
          "Een streefbeeld voor later."),
    klik("Het personeel van Trapkracht spreekt geen Frans, terwijl er veel Franstalige toeristen langskomen. Klik op het vak voor 'geen Frans spreken'.", U, [Z["W"]],
         "Het zit in het bedrijf zelf en hindert: een zwakte."),
    klik("Fietsen met elektrische ondersteuning worden steeds populairder. Klik op het vak waar dat hoort voor Trapkracht.", U, [Z["O"]],
         "Een trend in de markt, van buiten, die de winkel kan benutten: een kans."),
    keuze("Een nieuwe wet maakt de verpakkingen van een snoepfabriek duurder. In de SWOT is dat een [[*bedreiging|zwakte|kans]].",
          "Het komt van buiten en hindert."),
    inv("Hoe noem je iemand die iets te winnen of te verliezen heeft bij wat een bedrijf doet? Schrijf één Nederlands woord.", ["belanghebbende", "de belanghebbende"],
        "In het Engels: stakeholder."),
    tabel("Is dit een kernwaarde?",
          [("eerlijkheid", J), ("klantvriendelijkheid", J), ("een omzet van 2 miljoen euro", F)],
          "Kernwaarden zijn principes, geen cijfers."),
    keuze("De aandeelhouders willen hogere winst, de werknemers hogere lonen. Dat zijn [[*tegengestelde belangen|dezelfde belangen]] van stakeholders.",
          "Een bedrijf moet zulke belangen tegen elkaar afwegen."),
    tabel("Welk soort stakeholder: intern of extern?",
          [("de raad van bestuur", "intern"), ("de bank die een lening gaf", "extern"), ("de vakbond van het personeel", "extern")],
          "Intern zit in de onderneming zelf.",
          kolommen=["intern", "extern"]),
    open_("Bedenk voor een frituur in je buurt één sterkte en één bedreiging.",
          "Sterkte: zelfgemaakte sauzen die iedereen lekker vindt. Bedreiging: er opent een grote fastfoodketen vlakbij.",
          "Een sterkte zit in de zaak zelf; een bedreiging komt van buiten."),
]
