# -*- coding: utf-8 -*-
"""De vragen voor "Bedrijfsstrategie: missie, visie, SWOT en stakeholders"
(🚀 Boost doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
bedrijfswetenschappen, "bedrijfsstrategie": de missie en de visie van een
bedrijf of organisatie, de SWOT-analyse, waarom een strategie de succeskansen
verhoogt, en het begrip stakeholder met de band tussen de onderneming en haar
stakeholders. De marketing die daaruit volgt staat in [[bw_marketing]].

Deel 1 gaat over de missie, de visie en het belang van een strategie.
Deel 2 gaat over de SWOT-analyse en over de stakeholders.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de missie van een bedrijf?",
        opties=[
            "Waarvoor het bestaat",
            "Waar het binnen tien jaar wil staan",
            "Hoeveel winst het vorig jaar gemaakt heeft",
            "Welke machines het in het atelier heeft staan",
        ],
        antwoord=0,
        uitleg="De missie zegt waarom de onderneming er is: wat ze doet, voor wie, en waarin ze anders is. Ze gaat over het heden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de visie van een bedrijf?",
        opties=[
            "Waar het naartoe wil",
            "Wat het vandaag elke dag doet",
            "Hoeveel personeel het in dienst heeft",
            "Welke leveranciers het dit jaar gebruikt",
        ],
        antwoord=0,
        uitleg="De visie is het beeld van de toekomst: waar de onderneming binnen vijf of tien jaar wil staan. Ze geeft richting aan de keuzes van vandaag.",
    ),
    dict(
        type="waarofniet",
        vraag="De missie gaat over vandaag, de visie over de toekomst.",
        antwoord=True,
        uitleg="De missie beschrijft de bestaansreden nu, de visie het streefbeeld later. Samen vormen ze het vertrekpunt van de strategie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een missie is een lijst van de jaarcijfers van een bedrijf.",
        antwoord=False,
        uitleg="Cijfers staan in de jaarrekening. Een missie is een korte tekst over wat de onderneming doet en voor wie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het beeld van waar een bedrijf binnen tien jaar wil staan?",
        antwoord=["visie", "de visie"],
        uitleg="Dat is de visie. Ze zegt niet wat het bedrijf vandaag doet, maar waar het naartoe werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in een missie? Duid alles aan wat juist is.",
        opties=[
            "Wat het bedrijf doet",
            "Voor wie het dat doet",
            "Waarin het anders is",
            "De omzet van vorig jaar",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een missie beschrijft de activiteit, de doelgroep en het eigen karakter van de onderneming. Cijfers horen er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak van een bakkerij is een missie?",
        opties=[
            "Verse broden voor de buurt",
            "Volgend jaar een tweede winkel openen in de stad",
            "Over tien jaar de grootste bakkerij van het land zijn",
            "Deze maand voor tweeduizend euro meer verkopen dan vorige maand",
        ],
        antwoord=0,
        uitleg="Een missie zegt wat de zaak dag na dag doet en voor wie. De andere drie zijn doelstellingen of een visie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak is een visie?",
        opties=[
            "Over vijf jaar in elke stad een filiaal",
            "We bakken elke ochtend brood voor de buurt",
            "We hebben vandaag zeven mensen in dienst staan",
            "We kopen ons meel bij een molen uit de streek",
        ],
        antwoord=0,
        uitleg="Een visie kijkt vooruit en beschrijft een streefbeeld. De andere drie beschrijven de toestand van vandaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een bedrijfsstrategie belangrijk? Duid alles aan wat juist is.",
        opties=[
            "Iedereen trekt dezelfde kant uit",
            "Keuzes maken wordt makkelijker",
            "De kans op succes stijgt",
            "Er zijn dan geen concurrenten meer",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een strategie geeft richting, maakt beslissen eenvoudiger en verhoogt de succeskansen. Concurrenten verdwijnen er niet door.",
    ),
    dict(
        type="waarofniet",
        vraag="Een strategie helpt ook om te kiezen wat je niet doet.",
        antwoord=True,
        uitleg="Kiezen is ook afwijzen. Een duidelijke strategie zegt welke klanten, producten en markten je laat liggen, zodat je je kracht niet versnippert.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bedrijf zonder strategie maakt altijd verlies.",
        antwoord=False,
        uitleg="Zo streng is het niet. Zonder strategie is de kans op verkeerde keuzes wel groter en is het moeilijker om bij te sturen als de markt verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie bepaalt de strategie van een onderneming?",
        opties=[
            "De leiding",
            "De klanten in de winkel",
            "De boekhouder op het einde van het jaar",
            "De leverancier met de grootste omzet erbij",
        ],
        antwoord=0,
        uitleg="De zaakvoerder of de raad van bestuur legt de strategie vast, vaak na overleg met het personeel. Uitvoeren doet daarna de hele onderneming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij een bedrijfsstrategie? Duid alles aan wat juist is.",
        opties=[
            "Doelen op lange termijn",
            "De keuze van de doelgroep",
            "Hoe je je onderscheidt",
            "De planning van de leveringen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een strategie gaat over de grote lijnen: doelen, doelgroep en eigen karakter. Hoe de bestelwagen morgen rijdt, is dagelijkse organisatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een missie en een doelstelling?",
        opties=[
            "Een doelstelling is meetbaar",
            "Een missie geldt maar voor één jaar",
            "Een doelstelling staat nooit op papier",
            "Een missie wordt door de klanten bepaald",
        ],
        antwoord=0,
        uitleg="Een doelstelling heeft een cijfer en een datum, bijvoorbeeld tien procent meer omzet dit jaar. Een missie is blijvend en zonder cijfers.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reden waarom een organisatie bestaat?",
        antwoord=["missie", "de missie"],
        uitleg="Dat is de missie: wat de organisatie doet, voor wie, en waarin ze zich onderscheidt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen beantwoordt een visie? Duid alles aan wat juist is.",
        opties=[
            "Waar willen we staan",
            "Wat willen we betekenen",
            "Hoe groot willen we worden",
            "Hoeveel btw moeten we storten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een visie gaat over ambitie en richting. De btw is een verplichting van elke maand en heeft met de visie niets te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Heeft een vereniging zonder winstoogmerk ook een missie?",
        opties=[
            "Ja, ook een vzw",
            "Nee, enkel bedrijven met winst",
            "Nee, enkel vennootschappen met kapitaal",
            "Alleen als ze personeel in dienst heeft staan",
        ],
        antwoord=0,
        uitleg="Elke organisatie heeft een bestaansreden. Bij een vzw is die vaak nog belangrijker, want winst is er het doel niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijft een bedrijf zijn missie uit voor het personeel?",
        opties=[
            "Zodat iedereen hetzelfde weet",
            "Omdat de wet dat elk jaar oplegt",
            "Omdat de bank dat vraagt bij een lening",
            "Omdat de klanten die tekst willen lezen",
        ],
        antwoord=0,
        uitleg="Als iedereen weet waarvoor de zaak staat, nemen mensen dezelfde soort beslissingen, ook zonder dat de baas erbij staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een kernwaarde van een onderneming?",
        opties=[
            "Iets waar ze voor staat",
            "De waarde van haar gebouwen en machines",
            "Het bedrag dat op de balans als kapitaal staat",
            "De prijs die ze voor haar belangrijkste product vraagt",
        ],
        antwoord=0,
        uitleg="Kernwaarden zijn de principes waar de onderneming niet van afwijkt, bijvoorbeeld eerlijkheid of duurzaamheid. Ze horen bij de missie, niet bij de balans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf schrijft: in 2035 werken we volledig zonder afval. Wat is dat?",
        opties=[
            "Een visie",
            "Een missie van het bedrijf",
            "Een sterkte uit de SWOT-analyse",
            "Een stakeholder van het bedrijf",
        ],
        antwoord=0,
        uitleg="Het is een streefbeeld voor later met een jaartal erbij, dus een visie. De missie zou zeggen wat het bedrijf vandaag doet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de vier letters van SWOT?",
        opties=[
            "Sterktes, zwaktes, kansen en bedreigingen",
            "Strategie, winst, omzet en tevredenheid van de klanten",
            "Samenwerking, werking, opbrengst en toekomst van het bedrijf",
            "Sparen, werken, ondernemen en tewerkstellen in een onderneming",
        ],
        antwoord=0,
        uitleg="SWOT komt van strengths, weaknesses, opportunities en threats: sterktes, zwaktes, kansen en bedreigingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee delen van een SWOT gaan over het bedrijf zelf?",
        opties=[
            "Sterktes en zwaktes",
            "Kansen en bedreigingen van buiten",
            "Sterktes en kansen uit de omgeving",
            "Zwaktes en bedreigingen van de markt",
        ],
        antwoord=0,
        uitleg="Sterktes en zwaktes zijn intern: ze gaan over het personeel, de machines, de merknaam. Kansen en bedreigingen komen van buiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Kansen en bedreigingen komen van buiten het bedrijf.",
        antwoord=True,
        uitleg="Ze zitten in de omgeving: de wet, de economie, de technologie, de concurrenten. Het bedrijf kan ze niet zelf kiezen, enkel erop inspelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een sterkte is iets wat buiten het bedrijf gebeurt.",
        antwoord=False,
        uitleg="Een sterkte zit in het bedrijf zelf, bijvoorbeeld vakkundig personeel of een goede ligging. Wat buiten gebeurt, is een kans of een bedreiging.",
    ),
    dict(
        type="invultekst",
        vraag="In welk deel van een SWOT zet je een nieuwe wet die het bedrijf moeilijkheden bezorgt?",
        antwoord=["bedreiging", "bedreigingen", "een bedreiging"],
        uitleg="Een nieuwe wet komt van buiten en maakt het lastiger, dus is het een bedreiging. Zou ze juist deuren openen, dan is het een kans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn interne punten in een SWOT? Duid alles aan wat juist is.",
        opties=[
            "Vakkundig personeel",
            "Een oude machine",
            "Een sterke merknaam",
            "Een nieuwe concurrent",
        ],
        antwoord=[0, 1, 2],
        uitleg="Personeel, machines en merknaam zitten in het bedrijf: dat zijn sterktes of zwaktes. Een nieuwe concurrent komt van buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn externe punten in een SWOT? Duid alles aan wat juist is.",
        opties=[
            "Een nieuwe wet",
            "Een stijgende grondstofprijs",
            "Een groeiende vraag",
            "Een verouderd machinepark",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wet, prijzen en vraag zijn omgeving: kansen of bedreigingen. Oude machines zijn een interne zwakte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakker heeft een recept dat niemand anders heeft. Wat is dat in een SWOT?",
        opties=[
            "Een sterkte",
            "Een kans uit de omgeving",
            "Een zwakte van de onderneming",
            "Een bedreiging van buitenaf gezien",
        ],
        antwoord=0,
        uitleg="Het zit in de zaak zelf en het helpt: dus een sterkte. Daarop kan hij zijn strategie bouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De energieprijs stijgt sterk voor een bakker met grote ovens. Wat is dat?",
        opties=[
            "Een bedreiging",
            "Een sterkte van de zaak",
            "Een zwakte van de zaak zelf",
            "Een kans uit de omgeving gezien",
        ],
        antwoord=0,
        uitleg="De prijsstijging komt van buiten en maakt het moeilijker, dus is het een bedreiging. Zijn grote ovens kunnen daarbij wel een zwakte worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een SWOT helpt om te kiezen waar een bedrijf op inzet.",
        antwoord=True,
        uitleg="Door sterktes op kansen te leggen, ziet een bedrijf waar het kan groeien. En door zwaktes naast bedreigingen te zetten, ziet het waar het moet oppassen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zwakte kan een bedrijf nooit zelf aanpakken.",
        antwoord=False,
        uitleg="Zwaktes zitten juist in het bedrijf zelf, dus kan het eraan werken: opleiding geven, machines vernieuwen, de website herbouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="De gemeente legt een drukke fietsroute aan die langs de winkel komt. Wat is dat?",
        opties=[
            "Een kans",
            "Een sterkte van de winkel",
            "Een zwakte van de winkel zelf",
            "Een bedreiging van de concurrentie",
        ],
        antwoord=0,
        uitleg="Meer passage komt van buiten en het is gunstig, dus een kans. Of de winkel ze pakt, hangt van haar eigen sterktes af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een stakeholder?",
        opties=[
            "Iemand met een belang",
            "Iemand die aandelen op de beurs koopt",
            "Iemand die in de winkel iets komt kopen",
            "Iemand die bij het bedrijf in dienst treedt",
        ],
        antwoord=0,
        uitleg="Een stakeholder of belanghebbende is iedereen die iets te winnen of te verliezen heeft bij wat de onderneming doet: personeel, klanten, buurt, overheid, leveranciers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn stakeholders van een bedrijf? Duid alles aan wat juist is.",
        opties=[
            "De werknemers",
            "De klanten",
            "De leveranciers",
            "De machines in het atelier",
        ],
        antwoord=[0, 1, 2],
        uitleg="Stakeholders zijn mensen en organisaties met een belang. Machines zijn bezittingen, geen belanghebbenden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je iemand die een belang heeft bij wat een onderneming doet?",
        antwoord=["stakeholder", "een stakeholder", "belanghebbende"],
        uitleg="Dat is een stakeholder, in het Nederlands een belanghebbende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke belangen hebben de werknemers van een bedrijf? Duid alles aan wat juist is.",
        opties=[
            "Een goed loon",
            "Een veilige werkplek",
            "Werkzekerheid",
            "Een zo hoog mogelijk dividend",
        ],
        antwoord=[0, 1, 2],
        uitleg="Loon, veiligheid en zekerheid van werk zijn de belangen van het personeel. Een dividend is het belang van de aandeelhouders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het belang van de aandeelhouders?",
        opties=[
            "Winst en dividend",
            "Een hoger loon voor het personeel",
            "Zo weinig mogelijk lawaai in de buurt",
            "Een lagere prijs voor dezelfde goederen",
        ],
        antwoord=0,
        uitleg="Aandeelhouders hebben geld ingebracht en willen een vergoeding zien: winst, een dividend, en een aandeel dat in waarde stijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het belang van de buurt rond een fabriek?",
        opties=[
            "Weinig lawaai en verkeer",
            "Een zo hoog mogelijke winst per jaar",
            "Een zo laag mogelijk loon voor de werknemers",
            "Een zo groot mogelijke voorraad in het magazijn",
        ],
        antwoord=0,
        uitleg="Buurtbewoners willen vooral weinig overlast: geluid, geur, vrachtwagens. Daarom overlegt een bedrijf met hen bij een uitbreiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom houdt een onderneming rekening met haar stakeholders?",
        opties=[
            "Ze heeft hen nodig",
            "Omdat de wet dat voor elk bedrijf verbiedt",
            "Omdat dat de boekhouding eenvoudiger maakt",
            "Omdat ze dan geen belastingen hoeft te betalen",
        ],
        antwoord=0,
        uitleg="Zonder personeel, klanten, leveranciers of een buurt die haar aanvaardt, kan een onderneming niet werken. Wie hun belangen negeert, komt dat vroeg of laat tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stakeholder is een interne stakeholder?",
        opties=[
            "Het personeel",
            "De klant in de winkel",
            "De gemeente waar het bedrijf ligt",
            "De leverancier van de grondstoffen",
        ],
        antwoord=0,
        uitleg="Interne stakeholders zitten in de onderneming: het personeel, de zaakvoerders, de aandeelhouders. Klanten, leveranciers en overheid staan erbuiten.",
    ),
]
