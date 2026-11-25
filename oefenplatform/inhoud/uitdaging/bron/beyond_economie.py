# -*- coding: utf-8 -*-
"""Uitdaging Economie 🌍 Beyond doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen. Een marktdiagram en een conjunctuurgolf om op te klikken,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde, rekenvragen en
een korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Economie Beyond doorstroom. Alle cijfers zijn verzonnen.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_economie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Economie"
BESTAND = "beyond-economie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/economie-beyond-uitdaging"
MARKT = "markt-fietshelmen.svg"
GOLF = "conjunctuurgolf.svg"

# klikvakken uit maak_prenten_beyond_economie.py
E = [39.6, 45.6, 7.2, 10.3]
VAK1 = [17.2, 38.3, 6.8, 9.7]
VAK2 = [17.2, 52.3, 6.8, 9.7]
P_ = [16.0, 43.6, 7.2, 12.9]
Q_ = [26.7, 52.7, 7.2, 12.9]
R_ = [37.3, 61.8, 7.2, 12.9]
S_ = [58.5, 27.1, 7.2, 12.9]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Marktdiagram (prent)
    klik("Bekijk het marktdiagram. Klik op het marktevenwicht.",
         MARKT, [E],
         "Het evenwicht ligt waar vraag en aanbod elkaar snijden: bij 800 helmen per week en een prijs van 60 euro."),
    klik("Klik op het cijfer in het vlak dat het consumentensurplus voorstelt.",
         MARKT, [VAK1],
         "Het consumentensurplus ligt onder de vraagcurve en boven de marktprijs: kopers die meer wilden betalen, betalen maar 60 euro."),
    klik("Klik op het cijfer in het vlak dat het producentensurplus voorstelt.",
         MARKT, [VAK2],
         "Het producentensurplus ligt boven de aanbodcurve en onder de marktprijs: verkopers die ook voor minder wilden verkopen, krijgen 60 euro."),
    met_prent(MARKT, inv(
        "Hoe groot is het consumentensurplus in het evenwicht, in euro per week? Enkel het getal.",
        ["16000", "16 000", "16.000"],
        "Een driehoek met basis 800 helmen en hoogte 100 − 60 = 40 euro: ½ · 800 · 40 = 16 000 euro.")),
    met_prent(MARKT, tabel(
        "De overheid legt de maximumprijs van 40 euro op. Wat gebeurt er?",
        [
            ("Gevraagde hoeveelheid per week", "1200"),
            ("Aangeboden hoeveelheid per week", "400"),
            ("Tekort op de markt per week", "800"),
        ],
        "Bij 40 euro vragen kopers 1200 helmen, maar verkopers bieden er maar 400 aan. Er is een tekort van 800 helmen.",
        kolommen=["400", "800", "1200"])),
    met_prent(MARKT, keuze(
        "Een maximumprijs onder de evenwichtsprijs zorgt voor een [[*tekort|overschot]]. Een minimumprijs boven de evenwichtsprijs zorgt voor een [[*overschot|tekort]].",
        "Onder het evenwicht willen kopers meer dan verkopers aanbieden: een tekort. Boven het evenwicht is het omgekeerd: een overschot.")),

    # Conjunctuurgolf (prent)
    klik("Bekijk de conjunctuurgolf. Klik op een punt waar de economie op haar laagste punt zit: het dal.",
         GOLF, [R_],
         "Het dal (recessie op haar diepst) is het laagste punt van de golf onder de trendlijn: punt R."),
    klik("Klik op het hoogste punt van de hoogconjunctuur.",
         GOLF, [S_],
         "Punt S is de hoogste top boven de trend: daar is de hoogconjunctuur het sterkst."),
    met_prent(GOLF, tabel(
        "In welke fase zit de economie?",
        [
            ("Tussen P en R", "Afgaande fase"),
            ("Tussen R en S", "Opgaande fase"),
            ("Net na punt S", "Afgaande fase"),
        ],
        "Van een top naar een dal daalt de groei: de afgaande fase (laagconjunctuur in aantocht). Van een dal naar een top herstelt de economie.",
        kolommen=["Opgaande fase", "Afgaande fase"])),
    met_prent(GOLF, mk(
        "Wat stelt de oranje stippellijn voor?",
        ["De groei van het bbp op lange termijn.", "Het bbp van één jaar met de hoogste groei.", "Het begrotingstekort van de overheid per jaar.", "Het verloop van de inflatie gedurende de periode."],
        0,
        "De trendlijn toont de gemiddelde groei op lange termijn. De conjunctuur schommelt daarrond.")),

    # Kringloop en bbp
    keuze(
        "In de kringloop leveren gezinnen [[*productiefactoren|consumptiegoederen]] aan bedrijven en krijgen ze daarvoor [[*een inkomen|belastingen]].",
        "Gezinnen stellen arbeid, kapitaal en grond ter beschikking van bedrijven en ontvangen loon, rente, huur en winst."),
    inv("Een land heeft C = 300, I = 80, O = 120, X = 250 en M = 230 (miljard euro). Hoe groot is het bbp in miljard euro? Enkel het getal.",
        ["520"],
        "bbp = C + I + O + (X − M) = 300 + 80 + 120 + 20 = 520 miljard euro."),
    tabel(
        "Telt dit mee in het bbp van België?",
        [
            ("Een nieuwe auto, gebouwd in Gent", J),
            ("Een tweedehands fiets die je verkoopt aan een buur", F),
            ("Het loon van een Belgische kapper in Antwerpen", J),
            ("De kinderbijslag die een gezin ontvangt", F),
        ],
        "Het bbp telt de nieuwe goederen en diensten die in een jaar binnen het land gemaakt worden. Tweedehands verkoop en overdrachten zoals kinderbijslag tellen niet mee."),
    mk("Het nominale bbp stijgt met 5 % en de prijzen stijgen met 3 %. Hoeveel stijgt het reële bbp ongeveer?",
       ["Ongeveer 2 %", "Ongeveer 8 %", "Ongeveer 5 %", "Ongeveer 1,7 % daling"],
       0,
       "Reële groei is ongeveer nominale groei min inflatie: 5 − 3 = 2 %."),
    sorteer(
        "Is dit een welvaartsindicator die enkel op geld let, of een bredere welzijnsindicator?",
        ["Enkel geld", "Breder welzijn"],
        [
            ["bbp per inwoner", "Enkel geld"],
            ["Human Development Index (HDI)", "Breder welzijn"],
            ["nationaal inkomen", "Enkel geld"],
            ["levensverwachting en scholing", "Breder welzijn"],
        ],
        "De HDI combineert inkomen met gezondheid en onderwijs. Bbp en nationaal inkomen meten enkel de productie in geld."),

    # Elasticiteit
    inv("De prijs van een concertticket stijgt van 50 naar 55 euro. De gevraagde hoeveelheid daalt van 1000 naar 800. Wat is de prijselasticiteit van de vraag? Gebruik de gewone procentformule en geef het getal met minteken.",
        ["-2", "−2", "-2,0"],
        "Hoeveelheid −20 %, prijs +10 %: −20 / 10 = −2. De vraag is elastisch."),
    tabel(
        "Is de vraag naar dit goed eerder elastisch of inelastisch?",
        [
            ("Insuline voor een diabetespatiënt", "Inelastisch"),
            ("Een merk frisdrank met veel alternatieven", "Elastisch"),
            ("Brood", "Inelastisch"),
            ("Een citytrip naar Barcelona", "Elastisch"),
        ],
        "Noodzakelijke goederen zonder alternatief hebben een inelastische vraag. Luxe of makkelijk te vervangen goederen hebben een elastische vraag.",
        kolommen=["Elastisch", "Inelastisch"]),
    keuze(
        "Als het inkomen stijgt en mensen kopen minder van een goed, dan is het een [[*inferieur goed|luxegoed|normaal goed]]. De inkomenselasticiteit is dan [[*negatief|groter dan 1|nul]].",
        "Bij een inferieur goed daalt de vraag als het inkomen stijgt: de inkomenselasticiteit is negatief."),

    # Marktvormen
    tabel(
        "Welke marktvorm past?",
        [
            ("Eén aanbieder, geen vervangers, hoge toetredingsdrempels", "Monopolie"),
            ("Enkele grote aanbieders die op elkaar letten", "Oligopolie"),
            ("Veel aanbieders met een eigen merk of stijl", "Monopolistische concurrentie"),
            ("Veel aanbieders van een identiek product", "Volkomen concurrentie"),
        ],
        "Het aantal aanbieders en hoe gelijk de producten zijn, bepalen de marktvorm.",
        kolommen=["Volkomen concurrentie", "Monopolistische concurrentie", "Oligopolie", "Monopolie"]),
    mk("Bij welke hoeveelheid maximaliseert een monopolist zijn winst?",
       ["Waar marginale opbrengst gelijk is aan marginale kost.", "Waar de prijs zo hoog mogelijk is, ongeacht de kost.", "Waar de totale opbrengst het grootst is op de markt.", "Waar de gemiddelde kost het laagst is voor het bedrijf."],
       0,
       "Elk bedrijf maximaliseert de winst waar MO = MK. Een monopolist vraagt daarna de prijs die de vraagcurve bij die hoeveelheid toelaat."),

    # Overheid en marktfalen
    sorteer(
        "Is dit een positief of een negatief extern effect?",
        ["Positief extern effect", "Negatief extern effect"],
        [
            ["Een buur die zijn tuin mooi onderhoudt", "Positief extern effect"],
            ["Lawaai van een fabriek 's nachts", "Negatief extern effect"],
            ["Iemand die zich laat vaccineren", "Positief extern effect"],
            ["Uitlaatgassen in een drukke straat", "Negatief extern effect"],
        ],
        "Een extern effect treft iemand die niet bij de ruil betrokken is. Is het voordelig, dan is het positief; schaadt het, dan is het negatief."),
    keuze(
        "Een vuurtoren is een [[*publiek goed|privaat goed]]: niemand kan uitgesloten worden en het gebruik door de één [[*vermindert niet|vermindert wel]] het gebruik door een ander.",
        "Publieke goederen zijn niet-uitsluitbaar en niet-rivaliserend. Daardoor wil niemand ervoor betalen en zorgt de overheid ervoor."),
    mk("De overheid legt een accijns op tabak. Wat gebeurt er op die markt?",
       ["De prijs stijgt en de verkochte hoeveelheid daalt.", "De prijs daalt en de verkochte hoeveelheid stijgt.", "De prijs en de hoeveelheid blijven gelijk als vroeger.", "De vraagcurve verschuift naar rechts en de prijs stijgt."],
       0,
       "Een belasting verschuift het aanbod naar links: de prijs voor de koper stijgt en er wordt minder verkocht."),

    # Arbeidsmarkt
    inv("Een land heeft 5 miljoen mensen in de beroepsbevolking, waarvan 300 000 werkzoekend. Hoeveel procent bedraagt de werkloosheidsgraad? Enkel het getal.",
        ["6", "6,0"],
        "Werkloosheidsgraad = werklozen / beroepsbevolking · 100 = 300 000 / 5 000 000 · 100 = 6 %."),
    tabel(
        "Welk type werkloosheid beschrijft elke situatie?",
        [
            ("Een ijsjesverkoper heeft in de winter geen werk.", "Seizoenswerkloosheid"),
            ("Een drukker verliest zijn job omdat alles digitaal wordt.", "Structurele werkloosheid"),
            ("Door een recessie ontslaan veel bedrijven mensen.", "Conjuncturele werkloosheid"),
            ("Een afgestudeerde zoekt enkele weken naar een job.", "Frictiewerkloosheid"),
        ],
        "Seizoensgebonden, door een blijvende verandering in de economie, door de conjunctuur, of gewoon tijd tussen twee jobs.",
        kolommen=["Frictiewerkloosheid", "Seizoenswerkloosheid", "Conjuncturele werkloosheid", "Structurele werkloosheid"]),

    # Geld en financiële markt
    keuze(
        "Banken scheppen geld door [[*kredieten toe te kennen|biljetten te drukken]]. De Europese Centrale Bank kan de inflatie afremmen door de rente te [[*verhogen|verlagen]].",
        "Een lening die op een rekening wordt gezet, is nieuw giraal geld. Een hogere rente maakt lenen duurder en remt de bestedingen."),
    tabel(
        "Is dit een aandeel of een obligatie?",
        [
            ("Je wordt mede-eigenaar van het bedrijf.", "Aandeel"),
            ("Je leent geld uit tegen een vaste rente.", "Obligatie"),
            ("Je kan een dividend krijgen.", "Aandeel"),
            ("Op de vervaldag krijg je je geld terug.", "Obligatie"),
        ],
        "Een aandeel is een stukje eigendom met een onzeker dividend. Een obligatie is een lening met vaste rente en een vervaldag.",
        kolommen=["Aandeel", "Obligatie"]),

    # Ongelijkheid
    mk("Wat betekent een Gini-coëfficiënt die dichter bij 1 ligt?",
       ["De inkomens zijn ongelijker verdeeld.", "Iedereen heeft ongeveer hetzelfde inkomen.", "Het gemiddelde inkomen in het land is hoger.", "De armoede is volledig uit het land verdwenen."],
       0,
       "Een Gini van 0 betekent volledige gelijkheid, een Gini van 1 betekent dat één persoon alles heeft."),
    koppel(
        "Koppel het instrument aan de manier van herverdelen.",
        [
            ["progressieve personenbelasting", "wie meer verdient, betaalt een groter deel"],
            ["leefloon", "minimuminkomen voor wie niets heeft"],
            ["gratis openbaar onderwijs", "een dienst die voor iedereen toegankelijk is"],
        ],
        ["een hogere btw op alle voeding"],
        "Herverdeling gebeurt via belastingen, uitkeringen en diensten. Een hogere btw op voeding treft juist lage inkomens het hardst."),

    # Internationale handel en wisselmarkt
    keuze(
        "Als de euro duurder wordt tegenover de dollar, worden Europese producten voor Amerikanen [[*duurder|goedkoper]] en daalt de Europese [[*export|import]] meestal.",
        "Een sterkere euro betekent dat Amerikanen meer dollars moeten betalen voor dezelfde Europese producten."),
    sorteer(
        "Op welke rekening van de betalingsbalans komt dit?",
        ["Lopende rekening", "Financiële rekening"],
        [
            ["Export van Belgische chocolade", "Lopende rekening"],
            ["Een Amerikaans bedrijf koopt een Belgische fabriek", "Financiële rekening"],
            ["Toeristen die in Brugge overnachten", "Lopende rekening"],
            ["Een Belg koopt Duitse aandelen", "Financiële rekening"],
        ],
        "Goederen en diensten staan op de lopende rekening. Investeringen en beleggingen staan op de financiële rekening."),
    tabel(
        "Klopt dit over internationale samenwerking?",
        [
            ("In de eurozone voeren landen samen één monetair beleid.", J),
            ("De WTO heeft als doel de handel tussen landen vrijer te maken.", J),
            ("Een douane-unie heft binnen de groep hogere invoertarieven.", F),
            ("Protectionisme betekent dat een land alle grenzen opent.", F),
        ],
        "In een douane-unie vallen de tarieven binnen de groep weg en is er één gemeenschappelijk buitentarief. Protectionisme beschermt de eigen markt."),

    # Inkomensevenwicht en inflatie
    inv("De marginale consumptiequote is 0,8. Hoe groot is de multiplicator? Enkel het getal.",
        ["5", "5,0"],
        "Multiplicator = 1 / (1 − c) = 1 / 0,2 = 5. Elke extra euro bestedingen verhoogt het inkomen met 5 euro."),
    tabel(
        "Is dit vraaginflatie of kosteninflatie?",
        [
            ("De olieprijs verdubbelt en bedrijven rekenen dat door.", "Kosteninflatie"),
            ("Iedereen wil tegelijk meer kopen dan er gemaakt wordt.", "Vraaginflatie"),
            ("De lonen stijgen sneller dan de productiviteit.", "Kosteninflatie"),
        ],
        "Stijgende kosten (grondstoffen, lonen) duwen de prijzen omhoog: kosteninflatie. Een te grote vraag trekt de prijzen omhoog: vraaginflatie.",
        kolommen=["Vraaginflatie", "Kosteninflatie"]),
    mk("Wat is het gevolg van deflatie voor iemand met een vaste schuld?",
       ["De schuld weegt zwaarder, want geld wordt meer waard.", "De schuld verdwijnt vanzelf, want de prijzen dalen.", "De schuld weegt lichter, want het inkomen stijgt mee.", "Er verandert niets, want de rente blijft altijd gelijk."],
       0,
       "Bij deflatie stijgt de koopkracht van geld. Een vaste schuld is dan in reële termen meer waard: ze weegt zwaarder."),

    # Onderzoek
    volgorde(
        "Zet de stappen van een economisch onderzoek in de juiste volgorde.",
        ["Onderzoeksvraag stellen", "Hypothese formuleren", "Gegevens verzamelen", "Gegevens analyseren", "Besluit trekken"],
        "Je start met een vraag en een vermoeden, verzamelt daarna gegevens, verwerkt ze en trekt dan pas een besluit."),
    mk("Welke MVO-maatregel past bij de P van 'planet'?",
       ["Een bedrijf plaatst zonnepanelen op zijn daken.", "Een bedrijf betaalt een eerlijk loon aan zijn personeel.", "Een bedrijf verhoogt zijn winst met tien procent.", "Een bedrijf sponsort de lokale voetbalploeg ruim."],
       0,
       "Maatschappelijk verantwoord ondernemen let op people, planet en profit. Planet gaat over het milieu."),

    inv("Een korf kost 400 euro in het basisjaar en 424 euro dit jaar. Hoeveel procent bedraagt de inflatie? Enkel het getal.",
        ["6", "6,0"],
        "Prijsindex = 424 / 400 · 100 = 106. De prijzen stegen dus met 6 %."),
    mk("Twee oligopolisten zouden samen het meest winnen door een hoge prijs te houden, maar elk afzonderlijk wint meer door de prijs te verlagen. Hoe heet die situatie in de speltheorie?",
       ["Het gevangenendilemma", "Het marktevenwicht bij volkomen concurrentie", "De wet van de dalende meeropbrengst", "Een natuurlijk monopolie in de energiesector"],
       0,
       "In het gevangenendilemma kiest elke speler wat voor zichzelf het best lijkt, waardoor ze samen slechter uitkomen dan als ze zouden samenwerken."),

    # Schrijfopdracht
    open_("Een stad wil een maximumhuurprijs invoeren voor studentenkoten. Leg in 4 à 6 zinnen uit wat er volgens de marktwerking gebeurt en geef één voordeel en één nadeel.",
          "Als de maximumprijs onder de evenwichtsprijs ligt, willen meer studenten een kot huren dan er verhuurd worden: er ontstaat een tekort. Sommige eigenaars verhuren hun kot niet meer of onderhouden het minder. Een voordeel is dat studenten die een kot vinden minder betalen. Een nadeel is dat er wachtlijsten komen en dat sommige studenten geen kot vinden. Er kan ook een zwarte markt ontstaan.",
          "Een goed antwoord legt uit dat een maximumprijs onder het evenwicht een tekort veroorzaakt, en noemt een voordeel (lagere huur voor wie een kot heeft) en een nadeel (tekort, wachtlijsten, minder onderhoud of zwarte markt)."),
]
