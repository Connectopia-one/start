# -*- coding: utf-8 -*-
"""De leerbundels voor toegepaste economie op 🚀 Boost dubbele finaliteit.

Gebaseerd op de vakfiche 2DU toegepaste economie, geldig vanaf 1 januari 2027.
Die fiche geldt voor één studierichting: bedrijf en organisatie. Ze weegt de
twee bouwstenen gelijk, boekhouden 50 % en documenten en data verwerken 50 %,
dus acht bundels boekhouden en acht bundels ICT.

Het examen is digitaal en duurt 120 minuten. Word, Excel en de boekhoudsoftware
mogen níét gebruikt worden, dus de ICT-bundels gaan over het begrip en niet over
klikinstructies: wat een absolute verwijzing doet, waarom een as bij nul begint,
wat OCR is.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

Elk getalvoorbeeld dat hier beweerd wordt, staat ook in controleer.py, waar het
uitgerekend wordt in plaats van uitgeschreven.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Toegepaste economie"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    BUNDELS[slug + "-boost-dubbele-finaliteit"] = b


# ───────────────────────── 1. Waarom boekhouden en hoe het werkt
zet("waarom-boekhouden-en-hoe-het-werkt",
    titel="Waarom boekhouden en hoe het werkt",
    onder="Wat een boekhouding is en voor wie ze dient, de jaarrekening, en het dubbel boekhouden met debet, credit, journaal en grootboek.",
    secties=[
        dict(kop="Wat boekhouden is", blokken=[
            ("p", "<strong>Boekhouden is alle verrichtingen registreren.</strong> Elke aankoop, verkoop en "
                  "betaling wordt genoteerd, zodat je op elk moment weet wat de zaak bezit en wat ze schuldig "
                  "is. <strong>Een verrichting is een feit met een gevolg in geld</strong>: een aankoop, een "
                  "verkoop, een betaling, alles met een bedrag eraan."),
            ("p", "<strong>Een onderneming is wettelijk verplicht een boekhouding te voeren.</strong> De wet "
                  "legt op welke boeken je bijhoudt en hoe lang je ze bewaart. <strong>Ook een kleine "
                  "zelfstandige houdt documenten bij</strong>: ook een vereenvoudigde boekhouding vraagt een "
                  "aankoop- en een verkoopdagboek."),
            ("p", "<strong>Een boekhouding dient niet enkel om de belastingen te berekenen.</strong> Ze dient "
                  "vooral om te weten hoe de zaak ervoor staat en om te kunnen bijsturen."),
            ("kader", tabel(["wie", "waarom die de cijfers wil zien"],
                            [["<strong>de zaakvoerder</strong>", "<strong>om bij te sturen waar het misloopt</strong>, een investering te plannen of een prijs te herbekijken"],
                             ["<strong>de bank</strong>", "<strong>om een lening te beoordelen</strong>: de cijfers tonen of de onderneming kan terugbetalen"],
                             ["<strong>een investeerder</strong>", "<strong>om te beoordelen of de zaak gezond is</strong> voor hij er geld tegenover zet"],
                             ["<strong>de fiscus</strong>", "<strong>om te controleren</strong>; daarom moeten de documenten een aantal jaren bewaard blijven"],
                             ["<strong>de andere afdelingen</strong>", "<strong>de boekhouding levert de cijfers</strong> waar aankoop, verkoop en directie op steunen"]])),
            ("p", "<strong>Een boekhouding kijkt terug, maar wordt vooral gebruikt om vooruit te "
                  "beslissen.</strong> Dat is de reden waarom ze meer is dan een verplichting."),
        ]),
        dict(kop="De jaarrekening", blokken=[
            ("p", "<strong>De jaarrekening is het jaarlijks financieel verslag</strong> van de onderneming. "
                  "Ze bestaat uit <strong>drie delen</strong>: <strong>de balans</strong>, <strong>de "
                  "resultatenrekening</strong> en <strong>de toelichting</strong>. De twee grote delen naast "
                  "de toelichting zijn dus <strong>de balans en de resultatenrekening</strong>."),
            ("kader", tabel(["deel", "wat het toont"],
                            [["<strong>de balans</strong>", "<strong>het bezit en de schulden</strong>: links wat de onderneming bezit, rechts met welk geld dat betaald is"],
                             ["<strong>de resultatenrekening</strong>", "<strong>de kosten en de opbrengsten</strong>; het verschil is de winst of het verlies"],
                             ["<strong>de toelichting</strong>", "<strong>uitleg bij de cijfers</strong>, bij de posten van de balans en de resultatenrekening"]])),
            ("p", "<strong>Is het verschil tussen opbrengsten en kosten positief, dan is er winst</strong>; "
                  "<strong>zijn de kosten groter dan de opbrengsten, dan is er verlies</strong>. Dat verlies "
                  "gaat over naar het volgende boekjaar."),
            ("weetje", "Een uurrooster hoort niet in de jaarrekening maar bij de personeelsadministratie. "
                       "Op het examen is dat een klassieke afleider."),
        ]),
        dict(kop="Dubbel boekhouden", blokken=[
            ("p", "<strong>Dubbel boekhouden betekent dat elke verrichting twee rekeningen raakt</strong>: "
                  "<strong>debet bij de ene, credit bij de andere, voor hetzelfde bedrag</strong>. "
                  "<strong>Debet is de linkerkant, credit de rechterkant.</strong>"),
            ("p", "<strong>Waarom links en rechts? Omdat er altijd een herkomst en een bestemming is.</strong> "
                  "Geld komt ergens vandaan en gaat ergens heen, en het dubbel boekhouden toont beide kanten. "
                  "<strong>Daarom moet in een dubbele boekhouding debet altijd gelijk zijn aan credit</strong>, "
                  "en blijft het geheel in evenwicht."),
            ("p", "<strong>Een rekening is een overzicht per soort</strong>: elke soort bezit, schuld, kost of "
                  "opbrengst krijgt er een. <strong>Heeft een rekening een debetsaldo, dan is debet groter dan "
                  "credit</strong> en staat het saldo links; bij een creditsaldo is het omgekeerd."),
            ("kader", tabel(["boek", "wat erin staat", "waarvoor het dient"],
                            [["<strong>het journaal</strong>", "<strong>de boekingen op datum</strong>; ook dagboek genoemd", "<strong>het volgt de tijd</strong>"],
                             ["<strong>het grootboek</strong>", "<strong>dezelfde boekingen, gegroepeerd per rekening</strong>", "<strong>het saldo per rekening volgen</strong>"],
                             ["<strong>de inventaris</strong>", "<strong>de opmeting van bezit en schulden</strong>", "<strong>de cijfers staven op het einde van het jaar</strong>"]])),
            ("p", "<strong>Het journaal en het grootboek bevatten dezelfde verrichtingen</strong>, alleen "
                  "anders geordend: op datum of per rekening. <strong>Bij een boeking in het journaal horen de "
                  "datum, het rekeningnummer en het bedrag in debet of credit.</strong> De naam van de klant "
                  "staat op het document, niet noodzakelijk in de boeking."),
            ("p", "<strong>Koopt een zaak op krediet, dan stijgt de schuld</strong>: je krijgt de goederen nu "
                  "en betaalt later, dus de schuld aan de leverancier neemt toe."),
        ]),
        dict(kop="Het redeneerschema", blokken=[
            ("p", "<strong>Het redeneerschema is de vaste manier om tot een boeking te komen</strong>, en het "
                  "bestaat uit drie vragen na elkaar."),
            ("fig", svg.stappen(["welke rekeningen spelen mee?", "stijgen of dalen ze?", "debet of credit?"]),
             "De drie vragen van het redeneerschema, altijd in deze volgorde."),
            ("p", "Wie het document getekend heeft, verandert niets aan de boeking: die vraag hoort er niet "
                  "bij. <strong>Op het examen heeft een rekeningnummer vijf cijfers</strong>, en <strong>de "
                  "naam van de rekening verschijnt vanzelf zodra je het nummer invult</strong>. Daarom telt "
                  "het nummer en niet de spelling van de naam."),
            ("p", "<strong>Je krijgt enkel punten voor een boekingsregel die helemaal juist is</strong>: "
                  "<strong>het rekeningnummer, het bedrag en de kant</strong> moeten alle drie kloppen. En "
                  "<strong>je mag niet zoveel regels gebruiken als je wil</strong>: de fiche vraagt "
                  "uitdrukkelijk <strong>een minimum aantal boekingsregels</strong>."),
            ("weetje", "Debet en credit worden op het examen automatisch opgeteld. Een verschil tussen de twee "
                       "totalen kost geen punten, maar het is wel het eerste teken dat er een fout in je "
                       "boeking zit."),
        ]),
    ])


# ───────────────────────── 2. De balans en de resultatenrekening
zet("de-balans-en-de-resultatenrekening",
    titel="De balans en de resultatenrekening",
    onder="Actief en passief, vaste en vlottende activa, eigen en vreemd vermogen, en de kosten en opbrengsten die samen het resultaat van het boekjaar maken.",
    secties=[
        dict(kop="De twee kanten van de balans", blokken=[
            ("p", "<strong>Aan de actiefzijde staat wat de onderneming bezit</strong>: gebouwen, machines, "
                  "voorraad, geld. <strong>Aan de passiefzijde staat waarmee dat betaald is</strong>: het eigen "
                  "vermogen en de schulden, dus de herkomst van de middelen."),
            ("p", "<strong>Daarom is het actief altijd gelijk aan het passief.</strong> Alles wat je bezit is "
                  "met iets betaald, dus het totaal links is gelijk aan het totaal rechts. <strong>Het actief "
                  "staat links, het passief rechts.</strong>"),
            ("kader", tabel(["groep", "wat erin zit", "kant"],
                            [["<strong>vaste activa</strong>", "<strong>bezit voor langer dan een jaar</strong>: een gebouw, een machine, een bestelwagen", "<strong>actief</strong>"],
                             ["<strong>vlottende activa</strong>", "<strong>bezit voor korte tijd</strong>: voorraad, vorderingen op klanten, geld op de bank en in de kas", "<strong>actief</strong>"],
                             ["<strong>eigen vermogen</strong>", "<strong>het geld van de eigenaars</strong>: het ingebrachte kapitaal plus de winst die in de zaak bleef", "<strong>passief</strong>"],
                             ["<strong>vreemd vermogen</strong>", "<strong>de schulden</strong>: aan de bank, aan de leveranciers, aan de fiscus", "<strong>passief</strong>"]])),
            ("p", "<strong>De voorraad handelsgoederen hoort bij de vlottende activa</strong>, want ze is "
                  "bedoeld om binnen het jaar verkocht te worden. En <strong>een lening op lange termijn is "
                  "géén vast actief</strong>: een lening is een schuld en staat dus rechts."),
            ("p", "<strong>De beginbalans is de balans bij de start van het boekjaar</strong>, en ze is gelijk "
                  "aan de eindbalans van het vorige jaar."),
            ("p", "<strong>Op een balans lees je af wat de zaak bezit, wie de zaak gefinancierd heeft en hoe "
                  "groot het eigen vermogen is.</strong> Hoeveel klanten de zaak heeft, staat er niet op."),
        ]),
        dict(kop="Het eigen vermogen berekenen", blokken=[
            ("p", "<strong>Het eigen vermogen is het bezit min de schulden.</strong> <strong>Bezit een zaak "
                  "voor 80 000 euro en heeft ze 30 000 euro schulden, dan is het eigen vermogen 50 000 "
                  "euro.</strong>"),
            ("p", "<strong>Bezit een zaak 25 000 euro en heeft ze 25 000 euro schulden, dan is het eigen "
                  "vermogen nul</strong>: alles wat ze bezit is dan met vreemd vermogen betaald."),
            ("p", "<strong>De winst van het boekjaar komt bij het eigen vermogen op de balans.</strong> Winst "
                  "die in de zaak blijft, versterkt het eigen vermogen."),
            ("weetje", "De balans toont niet wat er tijdens het jaar verkocht is. Ze is een momentopname; wat "
                       "er verkocht is, staat in de resultatenrekening."),
        ]),
        dict(kop="De resultatenrekening", blokken=[
            ("p", "<strong>Een kost is wat de zaak verbruikt</strong>: lonen, huur, de aankoop van "
                  "handelsgoederen. <strong>Een opbrengst is wat de zaak verdient</strong>, vooral de "
                  "verkopen. <strong>Kosten verminderen het resultaat, opbrengsten verhogen het.</strong>"),
            ("p", "<strong>De resultatenrekening gaat over een periode, de balans over een moment.</strong> De "
                  "balans is een foto, de resultatenrekening is de film van het boekjaar."),
            ("kader", tabel(["resultaat", "hoe je het berekent"],
                            [["<strong>het bedrijfsresultaat</strong>", "<strong>bedrijfsopbrengsten min bedrijfskosten</strong>: de gewone werking, zonder de financiële verrichtingen"],
                             ["<strong>het financieel resultaat</strong>", "<strong>financiële opbrengsten min financiële kosten</strong>: ontvangen intresten tegenover betaalde intresten en bankkosten"],
                             ["<strong>het resultaat van de onderneming</strong>", "<strong>alle opbrengsten min alle kosten</strong>, en daarna de belastingen eraf"]])),
            ("p", "<strong>Die drie berekent de vakfiche na elkaar</strong>, en dat heeft een reden: "
                  "<strong>een onderneming kan winst maken op haar werking en toch verlies op haar financiële "
                  "verrichtingen</strong>."),
            ("p", "<strong>Heeft een zaak 120 000 euro opbrengsten en 95 000 euro kosten, dan is het resultaat "
                  "25 000 euro winst.</strong> <strong>Bij 60 000 euro opbrengsten en 72 000 euro kosten is er "
                  "12 000 euro verlies.</strong>"),
        ]),
        dict(kop="Omzet, afschrijving en investering", blokken=[
            ("p", "<strong>De omzet is de opbrengst uit de verkopen van het jaar.</strong> <strong>Omzet en "
                  "winst betekenen niet hetzelfde</strong>: omzet is wat binnenkomt uit verkopen, winst is wat "
                  "overblijft als alle kosten betaald zijn."),
            ("p", "<strong>De aankoop van een machine is geen kost in de resultatenrekening.</strong> Een "
                  "machine is een investering en staat op de balans; <strong>enkel de afschrijving is een "
                  "kost</strong>. <strong>Een afschrijving is de kost van de slijtage</strong>: de waarde van "
                  "een investering wordt over meerdere jaren als kost genomen."),
            ("kader", tabel(["kosten", "opbrengsten"],
                            [["<strong>de lonen</strong>", "<strong>de verkoop van handelsgoederen</strong>"],
                             ["<strong>de huur van het pand</strong>", "<strong>ontvangen intresten</strong>"],
                             ["<strong>de aankoop van handelsgoederen</strong>", "<strong>een ontvangen huurgeld</strong>"]])),
            ("p", "<strong>Voor de zaakvoerder toont de resultatenrekening waar het geld heen gaat</strong>: "
                  "je ziet welke kosten zwaar wegen en welke opbrengsten daartegenover staan."),
        ]),
    ])


# ───────────────────────── 3. Het MAR en het redeneerschema
zet("het-mar-en-het-redeneerschema",
    titel="Het MAR en het redeneerschema",
    onder="De zeven klassen van het minimum algemeen rekeningstelsel, de rekeningen die je het vaakst nodig hebt, en de vaste manier om van een document tot een boeking te komen.",
    secties=[
        dict(kop="Wat het MAR is", blokken=[
            ("p", "<strong>MAR staat voor minimum algemeen rekeningstelsel</strong>: een vaste lijst van "
                  "rekeningen met hun nummer. <strong>Je krijgt het MAR op het examen ter beschikking</strong>, "
                  "dus <strong>je moet de nummers niet uit het hoofd leren</strong>. Wat telt, is dat je er "
                  "snel de juiste rekening in vindt."),
            ("p", "<strong>Waarom werkt iedereen met hetzelfde rekeningstelsel? Zo zijn cijfers "
                  "vergelijkbaar</strong>: de fiscus, de bank en de boekhouder lezen dan dezelfde taal."),
            ("p", "<strong>Het MAR telt zeven klassen</strong>, genummerd van 1 tot en met 7."),
            ("kader", tabel(["klasse", "wat erin staat", "waar ze terechtkomt"],
                            [["<strong>1</strong>", "<strong>eigen vermogen en schulden op lange termijn</strong>", "<strong>de balans</strong>"],
                             ["<strong>2</strong>", "<strong>de vaste activa</strong>: gebouwen, machines, voertuigen", "<strong>de balans</strong>"],
                             ["<strong>3</strong>", "<strong>de voorraden</strong> en bestellingen in uitvoering", "<strong>de balans</strong>"],
                             ["<strong>4</strong>", "<strong>vorderingen en schulden op korte termijn</strong>: klanten, leveranciers, de btw-rekeningen", "<strong>de balans</strong>"],
                             ["<strong>5</strong>", "<strong>geldbeleggingen en liquide middelen</strong>: de kas en de bankrekening", "<strong>de balans</strong>"],
                             ["<strong>6</strong>", "<strong>de kosten</strong>", "<strong>de resultatenrekening</strong>"],
                             ["<strong>7</strong>", "<strong>de opbrengsten</strong>", "<strong>de resultatenrekening</strong>"]])),
            ("p", "Onthoud die scheiding: <strong>de klassen 1 tot 5 staan op de balans, de klassen 6 en 7 in "
                  "de resultatenrekening</strong>. <strong>Klasse 2 bevat dus geen kosten maar de vaste "
                  "activa</strong>; de kosten staan in klasse 6."),
        ]),
        dict(kop="De rekeningen die je het vaakst nodig hebt", blokken=[
            ("kader", tabel(["rekening", "wat ze betekent", "klasse"],
                            [["<strong>604 Aankopen handelsgoederen</strong>", "<strong>de aankoop van goederen om door te verkopen</strong>, dus een kost", "<strong>6</strong>"],
                             ["<strong>700 Verkopen handelsgoederen</strong>", "<strong>de verkoop</strong>, dus een opbrengst", "<strong>7</strong>"],
                             ["<strong>400 Handelsdebiteuren</strong>", "<strong>wat klanten nog moeten betalen</strong>: een vordering, dus een vlottend actief", "<strong>4</strong>"],
                             ["<strong>440 Leveranciers</strong>", "<strong>een schuld van de onderneming</strong>, op ten hoogste één jaar", "<strong>4</strong>"],
                             ["<strong>550 Kredietinstellingen</strong>", "<strong>de bankrekening</strong>", "<strong>5</strong>"]])),
            ("p", "<strong>In klasse 4 vind je dus 400 Handelsdebiteuren, 440 Leveranciers en de "
                  "btw-rekeningen.</strong> 604 hoort daar niet bij: die staat in klasse 6, bij de kosten."),
            ("p", "<strong>De rekening 550 Kredietinstellingen komt in beeld zodra er geld over de bank "
                  "gaat</strong>: een klant die via overschrijving betaalt, een leverancier die je via de bank "
                  "betaalt, of bankkosten. <strong>Een aankoop op krediet raakt de bank pas op het moment dat "
                  "je betaalt.</strong>"),
        ]),
        dict(kop="Welke kant kiest een rekening", blokken=[
            ("p", "<strong>In het redeneerschema gebruik je vier letters</strong>: <strong>A voor actief, P "
                  "voor passief, K voor kosten en O voor opbrengsten</strong>. Elke soort heeft haar eigen "
                  "kant, en die ligt vast."),
            ("kader", tabel(["soort", "stijgt in", "daalt in"],
                            [["<strong>A, een actief</strong>", "<strong>debet</strong>", "<strong>credit</strong>"],
                             ["<strong>P, een passief of schuld</strong>", "<strong>credit</strong>", "<strong>debet</strong>"],
                             ["<strong>K, een kost</strong>", "<strong>debet</strong>", "<strong>credit</strong>"],
                             ["<strong>O, een opbrengst</strong>", "<strong>credit</strong>", "<strong>debet</strong>"]])),
            ("p", "<strong>Een kost die stijgt komt dus in debet</strong>, net als een bezit dat stijgt. "
                  "<strong>Een schuld stijgt in credit</strong>, en <strong>een opbrengst stijgt niet in debet "
                  "maar in credit</strong>, samen met de schulden en het eigen vermogen."),
            ("kader", tabel(["verrichting", "debet", "credit"],
                            [["<strong>handelsgoederen kopen op krediet</strong>", "<strong>604 Aankopen handelsgoederen</strong>, de kost stijgt", "<strong>440 Leveranciers</strong>, de schuld stijgt"],
                             ["<strong>handelsgoederen verkopen op krediet</strong>", "<strong>400 Handelsdebiteuren</strong>, de vordering stijgt", "<strong>700 Verkopen</strong>, de opbrengst stijgt"],
                             ["<strong>een klant betaalt via de bank</strong>", "<strong>550 Kredietinstellingen</strong>, de bank stijgt", "<strong>400 Handelsdebiteuren</strong>, de vordering verdwijnt"],
                             ["<strong>contant betalen uit de kas</strong>", "<strong>de kost of de schuld</strong>", "<strong>de kas</strong>, een actief dat daalt"]])),
            ("p", "<strong>Het bedrag in debet mag nooit verschillen van het bedrag in credit.</strong> Elke "
                  "boeking is in evenwicht; is ze dat niet, dan zit er een fout in."),
        ]),
        dict(kop="Van document tot boeking", blokken=[
            ("p", "<strong>Voor je een factuur boekt, lees je eerst het document, ga je na wat er gebeurd is "
                  "en controleer je de bedragen.</strong> Eerst begrijpen, dan pas het redeneerschema invullen."),
            ("p", "<strong>Daarna volgen de drie vragen</strong>: welke rekeningen spelen mee, stijgen of "
                  "dalen ze, en komen ze in debet of in credit? <strong>Je boekt zo efficiënt mogelijk, met zo "
                  "weinig mogelijk regels</strong>, want de fiche vraagt uitdrukkelijk een minimum aantal "
                  "boekingsregels."),
            ("p", "<strong>Op het examen worden het rekeningnummer, het bedrag en de kant beoordeeld.</strong> "
                  "De soort rekening mag je invullen om te redeneren, maar daar krijg je geen punten voor."),
            ("weetje", "De naam van de rekening verschijnt vanzelf zodra je het nummer invult. Een spelfout in "
                       "de naam van een rekening kan je dus geen punten kosten."),
        ]),
    ])


# ───────────────────────── 4. Aankopen: documenten, kortingen en btw
zet("aankopen-documenten-kortingen-en-btw",
    titel="Aankopen: documenten, kortingen en btw",
    onder="De documenten van prijsaanvraag tot creditnota, de drie soorten aankopen, en het rekenen op een aankoopfactuur: eerst de kortingen, dan de kosten, dan de btw.",
    secties=[
        dict(kop="De documenten van een aankoop", blokken=[
            ("p", "<strong>Een aankoop verloopt in vaste stappen, en bij elke stap hoort een document.</strong> "
                  "Ken je de volgorde, dan weet je ook wat je met welk document moet vergelijken."),
            ("fig", svg.stappen(["prijsaanvraag", "offerte", "bestelbon", "leverbon", "factuur"]),
             "De vijf documenten van een aankoop, in de volgorde waarin ze elkaar opvolgen."),
            ("kader", tabel(["document", "wie maakt het", "waarvoor het dient"],
                            [["<strong>de prijsaanvraag</strong>", "<strong>de klant</strong>", "<strong>een prijs opvragen</strong> bij een leverancier, met de voorwaarden erbij"],
                             ["<strong>de offerte</strong>", "<strong>de leverancier</strong>", "<strong>het antwoord</strong>: prijs, hoeveelheid en voorwaarden. De klant is nog tot niets verplicht"],
                             ["<strong>de bestelbon</strong>", "<strong>de klant</strong>", "<strong>de bestelling vastleggen</strong>; hiermee legt de klant zich vast op hoeveelheid en prijs"],
                             ["<strong>de leverbon</strong>", "<strong>de leverancier</strong>", "<strong>bewijzen wat geleverd is</strong>; er staan geen bedragen op"],
                             ["<strong>de aankoopfactuur</strong>", "<strong>de leverancier</strong>", "<strong>de vraag om te betalen</strong>"],
                             ["<strong>de creditnota</strong>", "<strong>de leverancier</strong>", "<strong>een factuur rechtzetten</strong> die al verstuurd is"]])),
            ("p", "<strong>Een offerte verplicht de klant niet om te kopen</strong>: pas met de bestelbon legt "
                  "hij zich vast. En <strong>een leverbon vermeldt niet de prijs</strong>: die gaat over wat er "
                  "geleverd is, de bedragen staan op de factuur."),
            ("p", "<strong>Een inkomende creditnota krijg je bij een terugzending</strong>, of bij een "
                  "vergeten korting of een fout op de factuur. <strong>Ze verhoogt het te betalen bedrag "
                  "niet, ze vermindert het</strong> — vandaar haar naam."),
        ]),
        dict(kop="Controleren voor je betaalt", blokken=[
            ("p", "<strong>Bij de ontvangst van een levering controleer je of alles er is en of alles heel "
                  "is</strong>, door te vergelijken met de leverbon en met je eigen bestelbon."),
            ("p", "<strong>De factuur vergelijk je met de offerte, de bestelbon en de leverbon.</strong> Prijs, "
                  "hoeveelheid en korting moeten overeenkomen met wat afgesproken was. <strong>Je controleert "
                  "de hoeveelheid, de eenheidsprijs, de berekende korting en het btw-tarief per artikel.</strong>"),
            ("p", "<strong>Waarom dat belangrijk is? Om kwaliteit af te leveren</strong>, zegt de fiche zelf. "
                  "Een fout die je niet opmerkt, betaal je."),
            ("p", "<strong>De vakfiche onderscheidt drie soorten aankopen</strong>, elk met hun eigen rekening "
                  "in het MAR."),
            ("kader", tabel(["soort aankoop", "wat het is"],
                            [["<strong>handelsgoederen</strong>", "<strong>goederen om door te verkopen</strong>: ze gaan de voorraad in en daarna weer buiten, naar de klant"],
                             ["<strong>diensten en diverse goederen</strong>", "<strong>wat je verbruikt om te werken</strong>: huur, verzekering, elektriciteit"],
                             ["<strong>investeringen</strong>", "<strong>een aankoop voor lange termijn</strong>: een machine of een bestelwagen, die je meerdere jaren gebruikt en afschrijft"]])),
        ]),
        dict(kop="Kortingen en btw op een factuur", blokken=[
            ("p", "<strong>Op een factuur reken je in een vaste volgorde: eerst de kortingen, dan de "
                  "doorgerekende kosten, en pas dan de btw.</strong> <strong>De handelskorting wordt dus niet "
                  "ná de btw afgetrokken</strong>; anders zou je btw betalen op geld dat je niet betaalt."),
            ("kader", tabel(["begrip", "wat het is"],
                            [["<strong>handelskorting</strong>", "<strong>korting op de prijs</strong>, bijvoorbeeld bij een grote bestelling; ze gaat van de brutoprijs af"],
                             ["<strong>financiële korting</strong>", "<strong>korting bij snel betalen</strong>, ook kaskorting genoemd; ook zij gaat eraf vóór de btw"],
                             ["<strong>doorgerekende kosten</strong>", "<strong>vervoer bijvoorbeeld</strong>: die worden juist bijgeteld en verhogen het bedrag waarop btw komt"],
                             ["<strong>terugstuurbare verpakking</strong>", "<strong>valt buiten de maatstaf</strong>: je betaalt ze als waarborg en krijgt ze terug, dus er komt geen btw op"]])),
            ("p", "Het verschil tussen de twee kortingen zit in <strong>de reden van de korting</strong>: "
                  "handelskorting hoort bij de verkoop zelf, financiële korting bij snel betalen."),
            ("p", "<strong>In België bestaan er drie btw-tarieven: 21, 12 en 6 procent.</strong> 21 procent is "
                  "het gewone tarief, 6 procent geldt onder meer voor voeding. <strong>Daarom kunnen er "
                  "meerdere tarieven op één factuur staan</strong>: verschillende goederen, elk aan hun eigen "
                  "tarief."),
        ]),
        dict(kop="Rekenen op een aankoopfactuur", blokken=[
            ("kader", tabel(["opgave", "antwoord", "rekenwijze"],
                            [["<strong>1 000 euro met 10 procent handelskorting</strong>", "<strong>900 euro</strong>", "10 procent van 1 000 is 100, en 1 000 min 100 is 900"],
                             ["<strong>21 procent btw op 800 euro</strong>", "<strong>168 euro</strong>", "800 maal 0,21"],
                             ["<strong>6 procent btw op 200 euro</strong>", "<strong>12 euro</strong>", "200 maal 0,06"],
                             ["<strong>500 euro goederen en 50 euro doorgerekend vervoer</strong>", "<strong>btw op 550 euro</strong>", "doorgerekende kosten horen bij de maatstaf van heffing"],
                             ["<strong>1 000 euro goederen met 21 procent btw</strong>", "<strong>1 210 euro te betalen</strong>", "1 000 plus 210 euro btw"]])),
            ("p", "<strong>Op een aankoopfactuur staan het bedrag zonder btw, het btw-bedrag en het te betalen "
                  "totaal.</strong> Het loon van de verkoper staat er niet op."),
            ("weetje", "Een snelle controle: 21 procent btw op 100 euro is 21 euro. Daarmee schat je elk "
                       "btw-bedrag in je hoofd, en merk je een rekenfout meteen."),
        ]),
    ])


# ───────────────────────── 5. Verkopen en de verkoopfactuur
zet("verkopen-en-de-verkoopfactuur",
    titel="Verkopen en de verkoopfactuur",
    onder="Dezelfde verrichting van de andere kant bekeken: de documenten die de verkoper maakt, de vordering op de klant, en het rekenwerk op een verkoopfactuur.",
    secties=[
        dict(kop="De andere kant van dezelfde factuur", blokken=[
            ("p", "<strong>Dezelfde factuur is bij de verkoper een verkoopfactuur en bij de koper een "
                  "aankoopfactuur.</strong> Hetzelfde papier, een andere kant van de verrichting. Dat maakt dit "
                  "hoofdstuk makkelijker dan het lijkt: je kent de documenten al, je bekijkt ze nu vanuit de "
                  "verkoper."),
            ("kader", tabel(["moment", "wat de verkoper doet"],
                            [["<strong>bij een prijsaanvraag</strong>", "<strong>hij maakt een offerte</strong> met prijs, hoeveelheid en voorwaarden"],
                             ["<strong>bij de levering</strong>", "<strong>hij maakt een leverbon</strong>, die meegaat met de goederen en bij ontvangst getekend wordt"],
                             ["<strong>om betaald te worden</strong>", "<strong>hij stuurt de verkoopfactuur</strong>"],
                             ["<strong>bij een terugzending of een fout</strong>", "<strong>hij stuurt een uitgaande creditnota</strong>"]])),
            ("p", "<strong>De verkoper maakt dus zelf de offerte, de leverbon en de verkoopfactuur.</strong> "
                  "De btw-aangifte doet elke btw-plichtige voor zichzelf; die hoort niet in dat rijtje."),
            ("p", "<strong>Een offerte en een factuur zijn niet hetzelfde document</strong>: een offerte is een "
                  "voorstel, een factuur is de vraag om te betalen."),
        ]),
        dict(kop="Verkopen op krediet", blokken=[
            ("p", "<strong>Een verkoopfactuur levert de verkoper een opbrengst op</strong>: de opbrengst staat "
                  "in klasse 7, de vordering op de klant in klasse 4. <strong>Bij een verkoop vermindert de "
                  "voorraad</strong>, want de goederen gaan naar de klant."),
            ("p", "<strong>De verkoper moet niet wachten op de betaling om te leveren.</strong> Bij verkoop op "
                  "krediet gebeurt de levering eerst en volgt de betaling later: <strong>een betaling op "
                  "dertig dagen betekent dat de klant later betaalt</strong>, en ondertussen heeft de verkoper "
                  "<strong>een vordering</strong>, geld dat hij nog krijgt."),
            ("p", "<strong>In de boekhouding heet dat de handelsdebiteuren, rekening 400.</strong> "
                  "<strong>Betaalt een klant niet, dan blijft de vordering openstaan</strong> tot ze betaald of "
                  "afgeboekt wordt."),
            ("p", "<strong>Op een verkoopfactuur staan het factuurnummer, de datum en de btw-nummers</strong>, "
                  "ook dat van de verkoper zelf: dat zijn wettelijke vermeldingen. <strong>De verkoper nummert "
                  "zijn facturen doorlopend, zodat een ontbrekende factuur meteen opvalt</strong>, en "
                  "<strong>hij houdt een kopie bij als bewijs</strong>, want de wet vraagt dat facturen een "
                  "aantal jaren bewaard blijven."),
        ]),
        dict(kop="Rekenen op een verkoopfactuur", blokken=[
            ("p", "<strong>De verkoper berekent de btw op het bedrag na korting</strong>: eerst de kortingen "
                  "eraf, dan de doorgerekende kosten erbij, en pas dan de btw. <strong>Dat bedrag heet de "
                  "maatstaf van heffing</strong>, het bedrag waarop btw komt."),
            ("kader", tabel(["wat het bedrag verlaagt", "wat het bedrag verhoogt"],
                            [["<strong>de handelskorting</strong>", "<strong>doorgerekend vervoer</strong>"],
                             ["<strong>de financiële korting</strong>", "<strong>verpakking die niet terugkomt</strong>"],
                             ["<strong>een korting bij een grote bestelling</strong>", "<strong>de btw zelf, op het einde</strong>"]])),
            ("p", "<strong>De handelskorting staat niet los van het btw-bedrag</strong>: ze verlaagt de "
                  "maatstaf, dus wordt ook de btw kleiner. <strong>Terugstuurbare verpakking telt niet mee in "
                  "de maatstaf</strong>, want ze is een waarborg die je terugkrijgt."),
            ("kader", tabel(["opgave", "antwoord", "rekenwijze"],
                            [["<strong>2 000 euro met 5 procent handelskorting</strong>", "<strong>1 900 euro</strong>", "5 procent van 2 000 is 100"],
                             ["<strong>21 procent btw op 1 900 euro</strong>", "<strong>399 euro</strong>", "1 900 maal 0,21"],
                             ["<strong>10 procent handelskorting op 500 euro</strong>", "<strong>50 euro</strong>", "500 gedeeld door 10"],
                             ["<strong>600 euro aan 6 procent en 400 euro aan 21 procent</strong>", "<strong>120 euro btw</strong>", "36 euro plus 84 euro"],
                             ["<strong>500 euro goederen met 6 procent btw</strong>", "<strong>530 euro te betalen</strong>", "500 plus 30 euro btw"]])),
            ("p", "<strong>De btw wordt per tarief apart berekend</strong>, want de tarieven verschillen: "
                  "6 procent voor het ene artikel, 21 procent voor het andere, op dezelfde factuur. "
                  "<strong>Om een verkoopfactuur te berekenen heb je de hoeveelheid, de eenheidsprijs en het "
                  "btw-tarief nodig</strong>, en de kortingen die afgesproken zijn."),
            ("p", "<strong>Een uitgaande creditnota verlaagt de omzet</strong>, want de verkoop wordt deels of "
                  "helemaal teruggedraaid, en <strong>er staat ook een btw-bedrag op</strong>: de btw op het "
                  "teruggedraaide bedrag gaat mee terug."),
            ("weetje", "De verkoper mag de btw die hij int niet houden. Hij int ze voor de staat en stort ze "
                       "door via zijn btw-aangifte. Dat heet de verschuldigde btw.")
        ]),
    ])


# ───────────────────────── 6. De btw en de btw-aangifte
zet("de-btw-en-de-btw-aangifte",
    titel="De btw en de btw-aangifte",
    onder="Waarom btw een belasting op de toegevoegde waarde heet, het verschil tussen verschuldigde en aftrekbare btw, en de aangifte met de roosters 81, 82 en 83.",
    secties=[
        dict(kop="Hoe de btw werkt", blokken=[
            ("p", "<strong>Btw is een belasting op de toegevoegde waarde</strong>, en <strong>de eindklant "
                  "draagt ze</strong>. Een btw-plichtige onderneming schuift ze door; de particulier aan het "
                  "eind betaalt ze. <strong>Een particulier kan de btw die hij betaalt dan ook niet "
                  "terugvragen</strong>: alleen btw-plichtigen trekken af."),
            ("p", "<strong>Btw rekent iedereen aan die beroepshalve verkoopt</strong>: een winkel, een groothandel, een zelfstandige loodgieter. <strong>Het standaardtarief is 21 procent</strong>, en <strong>voor de meeste voeding geldt het verlaagde tarief van 6 procent</strong>."),
            ("p", "<strong>Btw is geen belasting op de winst</strong> — dat is de vennootschapsbelasting. "
                  "<strong>Btw hangt aan de omzet</strong>, dus ook een zaak met verlies rekent btw af."),
            ("kader", tabel(["begrip", "wat het is"],
                            [["<strong>verschuldigde btw</strong>", "<strong>de btw op je verkopen</strong>, die je aanrekende aan je klanten en moet doorstorten"],
                             ["<strong>aftrekbare btw</strong>", "<strong>de btw op je aankopen</strong>, die je mag terugvragen omdat je ze aan je leverancier betaalde"],
                             ["<strong>een btw-nummer</strong>", "<strong>het kenmerk van een btw-plichtige</strong>; in België begint het met BE, gevolgd door tien cijfers"]])),
            ("p", "<strong>Een onderneming int de btw voor de staat</strong>: ze is een doorgeefluik, het geld "
                  "is nooit van haar. <strong>Door de aftrek betaalt elke schakel enkel op wat ze zelf "
                  "toevoegt</strong>, en daar komt de naam vandaan."),
            ("p", "<strong>Een bakker die 6 euro btw betaalt op bloem en 18 euro btw aanrekent op brood, stort "
                  "12 euro door</strong>: 18 verschuldigd min 6 aftrekbaar. Hij betaalt dus enkel op wat hij "
                  "toevoegde."),
            ("p", "<strong>Om btw te mogen aftrekken heb je een geldige factuur nodig</strong>, met "
                  "<strong>het btw-nummer van de verkoper, de datum, het bedrag zonder btw en het "
                  "btw-bedrag</strong>. Zonder die vermeldingen is er geen aftrek. Een factuur hoeft niet "
                  "getekend te worden om geldig te zijn."),
        ]),
        dict(kop="De aangifte en haar roosters", blokken=[
            ("p", "<strong>Een btw-aangifte is een afrekening met de staat</strong>: je zet je verschuldigde "
                  "en je aftrekbare btw tegenover elkaar. <strong>Een gewone btw-plichtige dient ze elke maand "
                  "of elk kwartaal in</strong>, naargelang de omzet van de onderneming. <strong>Een aangifte "
                  "die te laat ingediend wordt, kost een boete</strong>: de termijnen liggen vast."),
            ("p", "<strong>De roosters zijn de genummerde vakken van de aangifte.</strong> Elk vak heeft een "
                  "nummer en een vaste betekenis, en je vult er een bedrag in. <strong>Je krijgt de aangifte "
                  "op het examen</strong>, dus <strong>je moet de roosternummers niet uit het hoofd "
                  "kennen</strong>; je moet wel weten welk bedrag waar hoort."),
            ("kader", tabel(["rooster", "wat erin komt"],
                            [["<strong>81</strong>", "<strong>de aankopen van handelsgoederen</strong>"],
                             ["<strong>82</strong>", "<strong>de aankopen van diensten en diverse goederen</strong>"],
                             ["<strong>83</strong>", "<strong>de aankopen van bedrijfsmiddelen</strong>, dus de investeringen"]])),
            ("p", "<strong>Op een aangifte vul je de omzet per tarief, de aankopen per soort en de aftrekbare "
                  "btw in.</strong> Het personeel hoort bij een heel andere aangifte. <strong>De bedragen "
                  "komen uit de facturen van die periode</strong>, en daarom houdt een onderneming ze goed bij."),
        ]),
        dict(kop="Het btw-saldo", blokken=[
            ("p", "<strong>Het btw-saldo is de verschuldigde btw min de aftrekbare.</strong> Is het resultaat "
                  "positief, dan betaal je; is het negatief, dan krijg je terug."),
            ("kader", tabel(["situatie", "wat er gebeurt"],
                            [["<strong>verschuldigd groter dan aftrekbaar</strong>", "<strong>je moet btw betalen</strong>: je inde meer dan je betaalde"],
                             ["<strong>aftrekbaar groter dan verschuldigd</strong>", "<strong>je krijgt btw terug</strong>, bijvoorbeeld in een kwartaal met een grote investering"],
                             ["<strong>allebei gelijk</strong>", "<strong>het saldo is nul</strong>: niets te betalen en niets terug te vorderen"]])),
            ("p", "<strong>Een zaak met 4 200 euro verschuldigde btw en 2 800 euro aftrekbare btw moet 1 400 "
                  "euro betalen.</strong> <strong>Is een zaak 3 000 euro verschuldigd en mag ze 3 000 euro "
                  "aftrekken, dan is het saldo nul.</strong>"),
            ("p", "<strong>Het btw-saldo is niet hetzelfde als de winst.</strong> Het gaat enkel over btw; met "
                  "winst heeft het niets te maken."),
            ("weetje", "21 procent btw op 50 euro is 10,5 euro. Een btw-bedrag mag dus gerust centen hebben; "
                       "rond het niet af omdat het er vreemd uitziet."),
        ]),
    ])


# ───────────────────────── 7. Aankopen, verkopen en bankverrichtingen boeken
zet("aankopen-verkopen-en-bankverrichtingen-boeken",
    titel="Aankopen, verkopen en bankverrichtingen boeken",
    onder="De drie regels van een factuurboeking, waarom de btw een eigen rekening krijgt, en hoe je een bankuittreksel en een kasdocument boekt.",
    secties=[
        dict(kop="Een aankoopfactuur boeken", blokken=[
            ("p", "<strong>De boeking van een aankoopfactuur met btw heeft minstens drie regels</strong>: de "
                  "aankoop in debet, de btw in debet, en de schuld aan de leverancier in credit. <strong>De "
                  "drie bedragen van een factuur — het bedrag zonder btw, het btw-bedrag en het totaal — "
                  "vallen precies samen met die drie regels.</strong>"),
            ("kader", tabel(["regel", "rekening", "bedrag"],
                            [["<strong>debet</strong>", "<strong>604 Aankopen handelsgoederen</strong>", "<strong>1 000 euro</strong>, het bedrag zonder btw"],
                             ["<strong>debet</strong>", "<strong>de terug te vorderen btw</strong>", "<strong>210 euro</strong>"],
                             ["<strong>credit</strong>", "<strong>440 Leveranciers</strong>", "<strong>1 210 euro</strong>, het volle bedrag"]])),
            ("p", "<strong>De schuld aan de leverancier is altijd het totaal, btw inbegrepen.</strong> Bij een "
                  "factuur van 500 euro plus 105 euro btw boek je dus <strong>605 euro</strong> bij de "
                  "leveranciers."),
            ("p", "<strong>Waarom boek je de btw apart van de aankoopprijs? Omdat je ze terugkrijgt.</strong> "
                  "<strong>De btw hoort niet bij de kostprijs van de handelsgoederen</strong>: ze is geen kost "
                  "maar een vordering op de staat, en daarom krijgt ze een eigen rekening."),
            ("p", "<strong>Bij een aankoop met handelskorting boek je het bedrag na korting.</strong> De "
                  "handelskorting krijgt geen eigen rekening: je boekt gewoon wat je betaalt. "
                  "<strong>Doorgerekende vervoerkosten boek je wel apart, bij de aankoopkosten</strong>, een "
                  "eigen kostenrekening in klasse 6."),
            ("p", "<strong>Een inkomende creditnota boek je omgekeerd aan de factuur</strong>: wat bij de "
                  "factuur in debet stond, komt nu in credit, en omgekeerd. <strong>Ze wordt dus wel degelijk "
                  "geboekt</strong>, want ze corrigeert een eerdere boeking."),
        ]),
        dict(kop="Een verkoopfactuur boeken", blokken=[
            ("p", "<strong>Bij een verkoop staat de btw in credit</strong>, niet in debet: de verschuldigde "
                  "btw is een schuld aan de staat."),
            ("kader", tabel(["regel", "rekening", "bedrag"],
                            [["<strong>debet</strong>", "<strong>400 Handelsdebiteuren</strong>", "<strong>2 420 euro</strong>, het totaal dat de klant moet betalen"],
                             ["<strong>credit</strong>", "<strong>700 Verkopen handelsgoederen</strong>", "<strong>2 000 euro</strong>"],
                             ["<strong>credit</strong>", "<strong>de te betalen btw</strong>", "<strong>420 euro</strong>"]])),
            ("p", "<strong>Na een verkoop van 100 euro plus 21 euro btw komt er dus 121 euro bij de klant in "
                  "debet.</strong> De klant moet altijd het totaal betalen."),
            ("p", "<strong>Dezelfde factuur wordt bij de verkoper anders geboekt dan bij de koper</strong>: bij "
                  "de ene is het een opbrengst met een vordering, bij de andere een kost met een schuld."),
        ]),
        dict(kop="De bank en de kas", blokken=[
            ("p", "<strong>Een bankrekeninguittreksel is een overzicht van de bank</strong>: het toont alle "
                  "bewegingen op de rekening, met hun datum en hun saldo. <strong>Het is een bewijsstuk voor "
                  "de boekhouding</strong>, dus <strong>elke beweging erop wordt geboekt</strong> en het "
                  "uittreksel wordt bewaard."),
            ("kader", tabel(["rekening", "waarvoor"],
                            [["<strong>550 Kredietinstellingen</strong>", "<strong>de bankrekening</strong>, klasse 5"],
                             ["<strong>570 Kassen</strong>", "<strong>het contante geld</strong>, ook klasse 5"]])),
            ("p", "<strong>Op een uittreksel vind je een ontvangst van een klant, een betaling aan een "
                  "leverancier en bankkosten.</strong> Een uittreksel gaat over geld, niet over goederen; de "
                  "aankoop zelf stond al in de boeken, op het uittreksel staat enkel de betaling."),
            ("p", "<strong>Betaalt een klant 1 210 euro via de bank, dan dalen de handelsdebiteuren met 1 210 "
                  "euro</strong>: de hele vordering verdwijnt, btw inbegrepen, en de bank stijgt. <strong>Een "
                  "betaling door een klant verhoogt de omzet niet opnieuw</strong>: die was al geboekt bij de "
                  "factuur, anders tel je dubbel."),
            ("p", "<strong>Betaal je zelf een leverancier via de bank, dan gaat 440 Leveranciers in "
                  "debet</strong> — de schuld daalt — <strong>en staat de bank in credit</strong>, want een "
                  "actief dat daalt komt in credit."),
            ("p", "<strong>Bankkosten boek je als een financiële kost.</strong> Ze horen bij het financieel "
                  "resultaat, niet bij het bedrijfsresultaat."),
            ("weetje", "Een creditering op je bankuittreksel betekent dat er geld binnenkomt. De bank schrijft "
                       "vanuit haar eigen boekhouding, dus haar credit is jouw ontvangst. Dat voelt omgekeerd "
                       "en is een klassieke valkuil."),
        ]),
        dict(kop="Kasdocumenten", blokken=[
            ("p", "<strong>Een kasdocument is een bewijs van contant geld</strong>: een kasticket of een "
                  "ontvangstbewijs, dat toont wat er contant binnenkwam of uitging. <strong>Een "
                  "bankrekeninguittreksel, een kasticket en een ontvangstbewijs zijn financiële "
                  "documenten</strong>; een leverbon niet, want die gaat over goederen."),
            ("p", "<strong>Betaal je 300 euro contant, dan daalt de kas met 300 euro.</strong> Contant betalen "
                  "haalt het geld meteen uit de kas."),
            ("p", "<strong>De kas kan nooit een negatief saldo hebben</strong>: je kan niet meer contant geld "
                  "uitgeven dan erin zit. Een negatieve kas wijst dus altijd op een fout. <strong>Daarom "
                  "controleer je de kas regelmatig</strong>: je telt het geld en vergelijkt met het saldo in "
                  "de boekhouding."),
        ]),
    ])


# ───────────────────────── 8. Van proefbalans tot eindbalans
zet("van-proefbalans-tot-eindbalans",
    titel="Van proefbalans tot eindbalans",
    onder="De proef- en saldibalans als controle, de eindejaarsverrichtingen met de afschrijvingen en de regularisaties, en de eindbalans die de beginbalans van volgend jaar wordt.",
    secties=[
        dict(kop="De proef- en saldibalans", blokken=[
            ("p", "<strong>Een proefbalans geeft de totalen van elke rekening</strong>: per rekening wat er in "
                  "debet en wat er in credit staat. <strong>Een saldibalans geeft de saldo's</strong>: per "
                  "rekening het verschil tussen debet en credit. <strong>Ze geven dus niet dezelfde "
                  "cijfers</strong>, en daarom staan ze naast elkaar."),
            ("p", "<strong>Het saldo is het verschil tussen debet en credit van één rekening</strong>, aan de "
                  "kant met het grootste totaal. <strong>Heeft de kasrekening 5 000 euro in debet en 3 200 "
                  "euro in credit, dan is het saldo 1 800 euro in debet.</strong> <strong>Bij 900 euro debet en "
                  "1 500 euro credit is het saldo 600 euro, in credit.</strong>"),
            ("p", "<strong>Waarvoor dient zo'n balans? Om na te gaan of alles klopt.</strong> <strong>In een "
                  "proefbalans is het totaal van debet gelijk aan dat van credit</strong>, want elke boeking "
                  "zette hetzelfde bedrag links en rechts. <strong>Zijn ze niet gelijk, dan zoek je de "
                  "fout</strong>: er ontbreekt een boeking of er staat er een verkeerd."),
            ("p", "<strong>Je controleert drie dingen</strong>: of debet en credit gelijk zijn, of elke "
                  "rekening een logisch saldo heeft, en of er geen boeking ontbreekt. <strong>Een "
                  "kostenrekening hoort een debetsaldo te hebben</strong>, want kosten stijgen in debet; een "
                  "creditsaldo daar verraadt een fout."),
            ("weetje", "Een proef- en saldibalans is een controle, geen document voor buiten. Wat naar buiten "
                       "gaat, is de jaarrekening."),
        ]),
        dict(kop="De eindejaarsverrichtingen", blokken=[
            ("p", "<strong>Een eindejaarsverrichting is een boeking bij de afsluiting</strong>, die de cijfers "
                  "rechtzet voor de jaarrekening opgemaakt wordt. <strong>Ze wordt gewoon in het journaal "
                  "geboekt</strong>, als elke andere boeking."),
            ("kader", tabel(["verrichting", "wat ze doet"],
                            [["<strong>de jaarlijkse afschrijvingen</strong>", "<strong>de waardevermindering van de investeringen als kost nemen</strong>"],
                             ["<strong>de regularisatie van schulden op meer dan een jaar</strong>", "<strong>het deel dat binnen het jaar vervalt, verhuizen naar de schulden op korte termijn</strong>"],
                             ["<strong>de overdracht van het resultaat</strong>", "<strong>de winst of het verlies naar het eigen vermogen brengen</strong>"]])),
            ("p", "<strong>Dat stuk van de schuld verhuist omdat de balans dan beter klopt</strong>: een lezer "
                  "ziet meteen welke schulden binnen het jaar betaald moeten worden."),
            ("p", "<strong>De winst van het boekjaar gaat over naar volgend jaar</strong> en versterkt het "
                  "eigen vermogen. <strong>Het verlies staat ook bij het eigen vermogen</strong>, maar met een "
                  "minteken: een verlies verkleint het."),
        ]),
        dict(kop="Afschrijven", blokken=[
            ("p", "<strong>Je schrijft een machine af omdat ze waarde verliest</strong>: je spreidt de "
                  "kostprijs over de jaren dat je ze gebruikt. <strong>Lineair afschrijven is elk jaar "
                  "hetzelfde bedrag nemen</strong>, namelijk de aankoopprijs gedeeld door het aantal jaren."),
            ("kader", tabel(["opgave", "per jaar", "rekenwijze"],
                            [["<strong>een machine van 20 000 euro, 5 jaar</strong>", "<strong>4 000 euro</strong>", "20 000 gedeeld door 5"],
                             ["<strong>een bestelwagen van 30 000 euro, 6 jaar</strong>", "<strong>5 000 euro</strong>", "30 000 gedeeld door 6"],
                             ["<strong>15 000 euro aan 3 000 euro per jaar</strong>", "<strong>5 jaar</strong>", "15 000 gedeeld door 3 000"]])),
            ("p", "<strong>De afschrijving komt bij de kosten terecht</strong>, in klasse 6, en tegelijk daalt "
                  "de waarde van het actief op de balans. <strong>Die waarde na aftrek van de afschrijvingen "
                  "heet de boekwaarde.</strong> <strong>Een machine van 20 000 euro die drie jaar is "
                  "afgeschreven aan 4 000 euro per jaar, heeft een boekwaarde van 8 000 euro.</strong>"),
            ("p", "<strong>Een afschrijving kost geen geld op het moment dat je ze boekt</strong>: het geld "
                  "ging al buiten bij de aankoop, de afschrijving spreidt die uitgave enkel over de jaren."),
            ("p", "<strong>Een machine, een bestelwagen en een computer worden afgeschreven. Grond niet</strong>: "
                  "grond slijt niet en verliest geen waarde door gebruik."),
        ]),
        dict(kop="De eindbalans", blokken=[
            ("p", "<strong>Het boekjaar sluit in drie stappen</strong>: eerst de voorlopige proef- en "
                  "saldibalans, dan de eindejaarsverrichtingen, dan de definitieve proef- en saldibalans en de "
                  "eindbalans. <strong>De eindbalans komt dus ná de eindejaarsverrichtingen</strong>; anders "
                  "zouden de afschrijvingen er niet in zitten."),
            ("fig", svg.stappen(["voorlopige proef- en saldibalans", "eindejaarsverrichtingen",
                                 "definitieve proef- en saldibalans", "eindbalans"]),
             "De vier stappen van een afsluiting, in de volgorde van de vakfiche."),
            ("p", "<strong>Bij de afsluiting gaan de rekeningen van klasse 6 en 7 naar nul</strong>: de kosten "
                  "en de opbrengsten staan niet meer op de eindbalans. <strong>Hun verschil is het resultaat, "
                  "en dat komt bij het eigen vermogen.</strong>"),
            ("p", "<strong>De eindbalans toont de toestand op het einde van het boekjaar, is in evenwicht, en "
                  "wordt de beginbalans van het volgende jaar.</strong> Daarmee is de cirkel rond: de "
                  "beginbalans waarmee dit vak begon, is de eindbalans van het jaar ervoor."),
        ]),
    ])


# ───────────────────────── 9. Tekstverwerking: klavier, opmaak en stijlen
zet("tekstverwerking-klavier-opmaak-en-stijlen",
    titel="Tekstverwerking: klavier, opmaak en stijlen",
    onder="Vlot klavieren met de sneltoetsen, de drie lagen van opmaak (teken, alinea en pagina), en waarom je met stijlen en sjablonen werkt.",
    secties=[
        dict(kop="Vlot klavieren", blokken=[
            ("p", "<strong>Het nut van een sneltoets is dat je sneller werkt</strong>: je handen blijven op "
                  "het klavier in plaats van naar de muis te gaan. <strong>De vakfiche noemt ctrl, shift en "
                  "alt gr</strong> als de toetsen waarmee je efficiënt klaviert; alt gr gebruik je voor het "
                  "apenstaartje en het euroteken."),
            ("kader", tabel(["toets of sneltoets", "wat ze doet"],
                            [["<strong>ctrl + a</strong>", "<strong>alles selecteren</strong>: het hele document"],
                             ["<strong>ctrl + c</strong>", "<strong>kopiëren</strong>; plakken is ctrl + v en knippen is ctrl + x"],
                             ["<strong>ctrl + u</strong>", "<strong>onderlijnen</strong>"],
                             ["<strong>ctrl + z</strong>", "<strong>de laatste wijziging ongedaan maken</strong>"],
                             ["<strong>home</strong>", "<strong>naar het begin van de regel</strong>; met ctrl erbij naar het begin van het document"],
                             ["<strong>backspace</strong>", "<strong>het teken links van de cursor wissen</strong>"],
                             ["<strong>delete</strong>", "<strong>het teken rechts van de cursor wissen</strong>"],
                             ["<strong>shift</strong>", "<strong>een hoofdletter typen</strong>; met caps lock aan blijft alles in hoofdletters"],
                             ["<strong>insert</strong>", "<strong>wisselen tussen invoegen en overschrijven</strong>, niet een nieuw document maken"],
                             ["<strong>tab</strong>", "<strong>in een tabel naar de volgende cel</strong>; in de laatste cel maakt ze er een rij bij"]])),
            ("p", "<strong>Een tab is iets anders dan een reeks spaties.</strong> Een tab springt naar een "
                  "vaste positie; met spaties schuift alles scheef zodra je iets wijzigt. <strong>Met de knop "
                  "Alles weergeven zie je de opmaaktekens</strong> — spaties, tabs en alineamarkeringen — en "
                  "dus waar je opmaak vandaan komt."),
        ]),
        dict(kop="Drie lagen van opmaak", blokken=[
            ("p", "<strong>Opmaak zit in drie lagen, en de vraag is telkens: waarop werkt ze?</strong> Op de "
                  "letters, op de alinea of op de bladzijde. Wie dat onderscheid kent, vindt elke instelling "
                  "terug."),
            ("kader", tabel(["laag", "waarop ze werkt", "wat erbij hoort"],
                            [["<strong>tekenopmaak</strong>", "<strong>de letters</strong>", "<strong>lettertype, tekengrootte, vet, cursief, kleur, markeren, doorhalen, klein kapitaal, super- en subscript</strong>"],
                             ["<strong>alineaopmaak</strong>", "<strong>hele alinea's</strong>", "<strong>regelafstand, afstand tussen alinea's, uitlijning, opsommingstekens, tabs</strong>"],
                             ["<strong>paginaopmaak</strong>", "<strong>de bladzijde</strong>", "<strong>marges, afdrukstand, paginanummers, kop- en voettekst, secties, kolommen</strong>"]])),
            ("p", "Let op de twee klassieke vergissingen: <strong>de regelafstand hoort niet bij de "
                  "tekenopmaak maar bij de alineaopmaak</strong>, en <strong>super- en subscript horen niet bij "
                  "de alineaopmaak maar bij de tekenopmaak</strong>, want ze veranderen hoe een teken staat en "
                  "niet de hele alinea. <strong>Doorhalen is een streep dóór de tekst</strong>, niet eronder."),
            ("p", "<strong>De marges zijn de witruimte rond de tekst</strong>, <strong>de afdrukstand is "
                  "staand of liggend</strong> — staand voor een brief, liggend voor een brede tabel — en "
                  "<strong>een sectie geeft een deel van je document een eigen paginaopmaak</strong>, zodat "
                  "één bladzijde liggend kan staan terwijl de rest staand blijft."),
            ("p", "<strong>In een koptekst staat tekst boven elke bladzijde</strong>, vaak het logo of de naam "
                  "van de onderneming; <strong>de voettekst staat onderaan</strong>. <strong>Allebei herhalen "
                  "ze zich op elke bladzijde van de sectie</strong>, dus je stelt ze maar één keer in. "
                  "<strong>Paginanummers typ je niet met de hand</strong>: je voegt ze één keer in en ze "
                  "tellen vanzelf verder."),
            ("p", "<strong>Met kolommen zet je de tekst in banen</strong>, zoals in een krant of een folder: "
                  "smallere regels lezen vlotter."),
        ]),
        dict(kop="Stijlen en sjablonen", blokken=[
            ("p", "<strong>Met een stijl geef je alle titels in één keer dezelfde opmaak</strong>, en wijzig "
                  "je de stijl achteraf, dan volgen alle titels mee. <strong>Dat is het voordeel: je past "
                  "alles in één keer aan</strong> in plaats van kop na kop."),
            ("p", "<strong>Een sjabloon is een voorbereid document</strong> waarmee je start en dat je "
                  "invult: een factuur, een brief, een cv, in het Engels een template. <strong>Een sjabloon en een stijl zijn niet "
                  "hetzelfde</strong>: een sjabloon is het document, een stijl is een set opmaakkenmerken "
                  "daarin."),
            ("p", "<strong>Zoeken en vervangen wijzigt een woord overal</strong>, in één keer door het hele "
                  "document heen: een verkeerde naam rechtzetten, een term door een andere vervangen, of snel "
                  "iets terugvinden."),
            ("kader", tabel(["soort document", "voorbeelden uit de vakfiche"],
                            [["<strong>commerciële documenten</strong>", "<strong>een factuur, verkoopvoorwaarden, garantiebepalingen, een label</strong>"],
                             ["<strong>personeelsdocumenten</strong>", "<strong>een cv, een vacature, een sollicitatiebrief</strong>"],
                             ["<strong>overeenkomsten</strong>", "<strong>contracten en afspraken op papier</strong>"]])),
            ("weetje", "Een rekenblad maak je niet in een tekstverwerker. Komt er rekenwerk bij kijken, dan "
                       "hoort het in een rekenbladprogramma thuis."),
        ]),
    ])


# ───────────────────────── 10. Illustraties, schema's en tabellen
zet("illustraties-schema-s-en-tabellen",
    titel="Illustraties, schema's en tabellen",
    onder="Beelden invoegen en laten meelopen met de tekst, schema's zoals een organogram, tabellen die alles uitgelijnd houden, en wat de spelling- en grammaticacontrole wel en niet ziet.",
    secties=[
        dict(kop="Illustraties in een document", blokken=[
            ("p", "<strong>Een illustratie is een afbeelding of een vorm</strong>: een foto, een pictogram, "
                  "een vorm of een schema. <strong>Een pictogram is geen foto</strong> maar een eenvoudige "
                  "tekening van een ding of een idee; <strong>je gebruikt het om iets snel duidelijk te "
                  "maken</strong>, want een oogje of een winkelkarretje leest sneller dan een woord."),
            ("p", "<strong>De tekstterugloop bepaalt hoe de tekst rond een afbeelding loopt</strong>: "
                  "vierkant, rondom, boven en onder, achter of voor de tekst. <strong>Met Achter de tekst "
                  "staat de afbeelding onder de tekst</strong> en loopt de tekst er gewoon over — handig voor "
                  "een watermerk. <strong>Een ingevoegde afbeelding kan je achteraf gewoon verplaatsen</strong>; "
                  "de tekstterugloop bepaalt dan hoe de tekst meeschuift."),
            ("kader", tabel(["handeling", "wat ze doet"],
                            [["<strong>bijsnijden</strong>, ook croppen genoemd", "<strong>de randen van een foto wegsnijden</strong>: de foto blijft heel, je toont er minder van"],
                             ["<strong>aan een hoekpunt slepen</strong>", "<strong>vergroten of verkleinen met de juiste verhouding</strong>"],
                             ["<strong>aan een zijkant slepen</strong>", "<strong>uitrekken in één richting</strong>, en dus de afbeelding vervormen"],
                             ["<strong>alternatieve tekst invullen</strong>", "<strong>een beschrijving van het beeld meegeven</strong>, die een voorleesprogramma voorleest aan wie het beeld niet ziet"]])),
            ("p", "<strong>Aan een vorm kan je de vulkleur, de rand en de grootte aanpassen</strong>, en ook "
                  "een schaduw, een doorzichtigheid en tekst erin. <strong>Een tekstvak is een kader met tekst "
                  "dat je vrij over de bladzijde schuift</strong>, los van de gewone tekst."),
            ("p", "<strong>Niet elke foto op het internet mag je gebruiken.</strong> Haal beeld uit een vrije "
                  "beeldbank: die zegt uitdrukkelijk wat mag."),
        ]),
        dict(kop="Schema's en het organogram", blokken=[
            ("p", "<strong>SmartArt is een kant-en-klaar schema</strong>: je typt je tekst en het schema "
                  "tekent zichzelf. <strong>Je maakt er onder meer een organogram, een stappenplan, een "
                  "cyclus of een piramide mee.</strong>"),
            ("p", "<strong>Een organogram laat zien wie onder wie werkt</strong>: de structuur van een "
                  "onderneming. <strong>Je ziet er de afdelingen, wie leiding geeft en de hiërarchie</strong>. "
                  "De omzet staat er niet op; die hoort in de resultatenrekening."),
            ("fig", svg.stappen(["zaakvoerder", "afdelingshoofd", "medewerker"]),
             "De eenvoudigste vorm van een organogram: drie niveaus onder elkaar."),
        ]),
        dict(kop="Tabellen", blokken=[
            ("p", "<strong>Een tabel is een raster van cellen</strong>: rijen en kolommen, met in elk vakje "
                  "een cel. <strong>Een rij loopt horizontaal, een kolom verticaal</strong>, en <strong>een "
                  "cel ligt op het kruispunt van de twee</strong>."),
            ("p", "<strong>Je zet gegevens in een tabel omdat ze dan netjes uitgelijnd blijven</strong>: elke "
                  "waarde staat onder de vorige, ook als je later iets bijzet. <strong>Een tabel moet "
                  "daarvoor geen zichtbare randen hebben</strong> — je kan ze wegnemen en de uitlijning "
                  "blijft."),
            ("kader", tabel(["begrip", "wat het is"],
                            [["<strong>cellen samenvoegen</strong>, ook mergen genoemd", "<strong>van twee cellen één maken</strong>, handig voor een titel over de hele breedte"],
                             ["<strong>de koprij</strong>", "<strong>de rij met de titels</strong>; je kan ze bovenaan elke bladzijde laten herhalen als de tabel doorloopt"],
                             ["<strong>wat je kan aanpassen</strong>", "<strong>de breedte van een kolom, de randen, de achtergrondkleur van een cel</strong>"]])),
            ("p", "<strong>In een handelsdocument is een goed opgemaakte tabel belangrijk</strong>: de "
                  "bedragen staan onder elkaar, de klant vindt snel wat hij zoekt, en het ziet verzorgd uit. "
                  "<strong>Een tekstverwerker rekent niet</strong>; dat doet een rekenblad of de "
                  "boekhoudsoftware."),
        ]),
        dict(kop="Spelling-, grammatica- en autocorrectie", blokken=[
            ("p", "<strong>De spellingcontrole toont verkeerd gespelde woorden</strong> door elk woord te "
                  "vergelijken met een woordenlijst. <strong>De grammaticacontrole kijkt naar de "
                  "zinsbouw</strong>, dus naar de zin en niet naar het losse woord. <strong>Een rode "
                  "kronkellijn is een melding van de spellingcontrole</strong>; ze staat enkel op je scherm en "
                  "wordt niet afgedrukt."),
            ("p", "<strong>Vertrouw de spellingcontrole niet blind: ze mist fouten in echte woorden.</strong> "
                  "Typ je “hij word” waar “hij wordt” moet staan, dan staat er een bestaand woord en zwijgt de "
                  "controle."),
            ("p", "<strong>Staat de taal van je document op Engels, dan keurt de controle je Nederlands "
                  "af</strong> en onderlijnt ze bijna elk woord. Zet de taal van de tekst dus juist."),
            ("p", "<strong>De autocorrectie zet typfouten meteen recht</strong>, maakt van de eerste letter na "
                  "een punt een hoofdletter en zet rechte aanhalingstekens om naar ronde. <strong>Ze vraagt "
                  "daarbij geen toestemming</strong>: ze wijzigt meteen, en je maakt het ongedaan met ctrl + z. "
                  "<strong>Het nadeel is dat ze ook wijzigt wat je wél zo wou</strong>, zoals een afkorting of "
                  "een merknaam."),
        ]),
    ])


# ───────────────────────── 11. Het rekenblad: cellen, bereiken en opmaak
zet("het-rekenblad-cellen-bereiken-en-opmaak",
    titel="Het rekenblad: cellen, bereiken en opmaak",
    onder="Hoe een rekenblad opgebouwd is, wat een celadres en een bereik zijn, en wat je met opmaak, sorteren, filteren en blokkeren doet.",
    secties=[
        dict(kop="Cellen, rijen en kolommen", blokken=[
            ("p", "<strong>Een cel is het vakje waar je typt</strong>, op het kruispunt van een rij en een "
                  "kolom. <strong>De kolommen krijgen letters</strong> — A, B, C, en na Z komt AA — <strong>de "
                  "rijen krijgen getallen</strong>, van boven naar onder."),
            ("p", "<strong>Het celadres is eerst de letter van de kolom en dan het nummer van de rij.</strong> "
                  "<strong>De cel in kolom B, rij 3 is dus B3</strong>, en <strong>die in kolom D, rij 7 is "
                  "D7</strong>."),
            ("p", "<strong>Een bereik is een groep cellen</strong>: een rechthoek die je samen selecteert of "
                  "in een formule gebruikt. <strong>Het bereik van A1 tot A10 schrijf je als A1:A10</strong>, "
                  "met een dubbele punt tussen de eerste en de laatste cel."),
            ("p", "<strong>Een werkblad heeft duizenden rijen en honderden kolommen</strong>, en <strong>één "
                  "bestand kan meerdere werkbladen bevatten</strong>, elk met zijn eigen tabblad onderaan. "
                  "<strong>Bij een werkblad horen een naam op het tabblad, rijen en kolommen, en een eigen "
                  "reeks cellen</strong>; de bestandsnaam geldt voor het hele bestand, niet per werkblad. Een "
                  "tabblad hernoem je door erop te dubbelklikken."),
        ]),
        dict(kop="Wat je op het scherm ziet", blokken=[
            ("kader", tabel(["onderdeel", "wat het toont"],
                            [["<strong>de formulebalk</strong>", "<strong>wat er echt in de cel zit</strong>: in de cel zie je het resultaat, hier de formule erachter"],
                             ["<strong>het naamvak</strong>", "<strong>het adres van de cel</strong>; je kan er ook een adres intypen om er meteen heen te springen"],
                             ["<strong>de statusbalk</strong>", "<strong>info over de selectie</strong>, zoals het aantal, het gemiddelde en de som van de geselecteerde cellen"]])),
            ("p", "<strong>Wat je in een cel ziet, is niet altijd precies wat erin staat</strong>: een cel kan "
                  "een formule verbergen of een afgerond getal tonen. Daarvoor is de formulebalk er."),
            ("p", "<strong>In een cel kan een getal, tekst of een formule staan</strong>, en ook een datum, "
                  "al is dat voor het rekenblad gewoon een getal. <strong>Een formule begint met een "
                  "isgelijkteken</strong>; zonder dat teken ziet het rekenblad je formule als gewone tekst."),
            ("p", "<strong>Selecteren gaat op drie manieren</strong>: op een kolomletter klikken voor een hele "
                  "kolom, op een rijnummer voor een hele rij, of slepen over cellen voor een bereik. Het hele "
                  "blad selecteer je met het vakje linksboven, of met ctrl + a."),
        ]),
        dict(kop="Opmaak en getalnotatie", blokken=[
            ("p", "<strong>De getalnotatie bepaalt hoe een getal getoond wordt</strong>: als bedrag, als "
                  "percentage, als datum of met een vast aantal cijfers na de komma. <strong>Met de "
                  "muntnotatie zet het rekenblad zelf het euroteken en twee cijfers na de komma</strong>, en "
                  "<strong>de percentagenotatie toont 0,25 als 25 procent</strong>: het rekenblad bewaart "
                  "0,25 en toont er 25 procent van."),
            ("p", "<strong>Afronden met de getalnotatie verandert de waarde in de cel niet.</strong> Je ziet "
                  "minder cijfers, maar het rekenblad blijft met het volledige getal rekenen. Dat is een "
                  "belangrijk verschil met de functie AFRONDEN."),
            ("p", "<strong>Staat een cel vol hekjes, dan is de kolom te smal.</strong> Maak ze breder en het "
                  "getal verschijnt gewoon; er is niets stuk."),
            ("p", "<strong>Met de opmaak van een cel zet je de rand, kleur je de achtergrond en centreer je de "
                  "tekst.</strong> Wissen is geen opmaak. <strong>Cellen samenvoegen maakt van meerdere cellen "
                  "één cel</strong>, vooral voor een titel boven meerdere kolommen; reken er niet mee."),
        ]),
        dict(kop="Doortrekken, sorteren, filteren en blokkeren", blokken=[
            ("kader", tabel(["handeling", "wat ze doet"],
                            [["<strong>de vulgreep</strong>", "<strong>een reeks verderzetten</strong>: je sleept het vierkantje rechtsonder de cel en een reeks dagen, een reeks getallen of een formule loopt door"],
                             ["<strong>sorteren</strong>", "<strong>de rijen herschikken</strong> op een kolom; selecteer het hele bereik, anders schuiven de kolommen los van elkaar"],
                             ["<strong>filteren</strong>", "<strong>enkel tonen wat je wil</strong>: de rijen die niet aan de voorwaarde voldoen worden verborgen, niet gewist"],
                             ["<strong>titels blokkeren</strong>", "<strong>de titelrij vastzetten</strong>, zodat ze zichtbaar blijft bij het scrollen door een lange lijst"],
                             ["<strong>een kolom verbergen</strong>", "<strong>ze onzichtbaar maken, niet wissen</strong>: de gegevens blijven staan en de formules die ernaar verwijzen blijven werken"]])),
            ("p", "<strong>Voeg je een rij bij boven een formule, dan schuift de formule mee</strong>: de "
                  "verwijzingen worden automatisch aangepast. <strong>Verwijder je daarentegen een kolom waar "
                  "een formule naar verwijst, dan geeft die formule een fout</strong>, want de cel waar ze "
                  "naar keek bestaat niet meer."),
            ("p", "<strong>Waarom is een rekenblad handig voor de boekhouding? Het rekent zelf verder bij een "
                  "wijziging, je ziet alle bedragen in kolommen en je neemt snel een totaal.</strong> Boeken "
                  "doet de boekhoudsoftware, niet het rekenblad."),
        ]),
    ])


# ───────────────────────── 12. Formules en functies in een rekenblad
zet("formules-en-functies-in-een-rekenblad",
    titel="Formules en functies in een rekenblad",
    onder="De rekenregel en de operatoren, de functies die je het vaakst nodig hebt, de functie ALS en de zoekfuncties, en het verschil tussen een relatieve en een absolute verwijzing.",
    secties=[
        dict(kop="Rekenen in een cel", blokken=[
            ("p", "<strong>Elke formule begint met een isgelijkteken.</strong> Daarna gebruik je de operatoren "
                  "van het rekenblad: <strong>het sterretje om te vermenigvuldigen, het schuine streepje om te "
                  "delen en het dakje om te verheffen</strong>. De letter x is voor een rekenblad gewoon tekst."),
            ("p", "<strong>De rekenregel is dezelfde als in de wiskunde</strong>: eerst machten, dan maal en "
                  "delen, dan plus en min, en <strong>haakjes gaan voor</strong>. <strong>=(2+3)*4 geeft 20, "
                  "=2+3*4 geeft 14.</strong>"),
            ("p", "<strong>Waarom gebruik je een functie in plaats van alles zelf op te tellen? Omdat de "
                  "formule zich aanpast</strong>: wijzig je een getal in het bereik, dan verandert het totaal "
                  "mee. <strong>Tussen de haakjes van een functie staat haar argument</strong>: een bereik van "
                  "cellen, een celadres of een getal."),
            ("p", "<strong>Een functienaam hoef je niet in hoofdletters te typen</strong>: typ je som(a1:a5), "
                  "dan maakt het rekenblad er zelf SOM(A1:A5) van."),
        ]),
        dict(kop="De functies die je het vaakst nodig hebt", blokken=[
            ("kader", tabel(["functie", "wat ze doet"],
                            [["<strong>SOM</strong>", "<strong>getallen optellen</strong>: =SOM(A1:A20) telt alles in dat bereik op"],
                             ["<strong>GEMIDDELDE</strong>", "<strong>de som gedeeld door het aantal</strong>, in één functie"],
                             ["<strong>MAX</strong> en <strong>MIN</strong>", "<strong>het hoogste en het laagste getal</strong> uit een bereik"],
                             ["<strong>AANTAL</strong>", "<strong>tellen hoeveel cellen een getal bevatten</strong>, niet hoeveel die getallen samen zijn"],
                             ["<strong>PRODUCT</strong>", "<strong>de getallen met elkaar vermenigvuldigen</strong>, niet optellen"],
                             ["<strong>AFRONDEN</strong>", "<strong>afronden op een aantal cijfers na de komma</strong>: =AFRONDEN(12,348;2) geeft 12,35"],
                             ["<strong>VANDAAG</strong>", "<strong>de datum van vandaag</strong>; ze past zich elke dag aan"],
                             ["<strong>NU</strong>", "<strong>datum en uur</strong>"],
                             ["<strong>JAAR</strong>", "<strong>het jaartal uit een datum halen</strong>"]])),
            ("p", "<strong>=SOM(A1:A5) telt vijf cellen op</strong>: A1, A2, A3, A4 en A5, de eerste en de "
                  "laatste meegerekend. <strong>=MIN(B2:B10) zoekt het laagste getal</strong> uit dat bereik."),
            ("weetje", "Zet VANDAAG niet in een factuur die je bewaart. De functie past zich elke dag aan, "
                       "dus morgen draagt je factuur een andere datum."),
        ]),
        dict(kop="Kiezen en opzoeken", blokken=[
            ("p", "<strong>De functie ALS kiest tussen twee uitkomsten op basis van een voorwaarde</strong>, "
                  "en ze heeft <strong>drie delen: de test, het antwoord als de test waar is, en het antwoord "
                  "als ze niet waar is</strong>. Bijvoorbeeld =ALS(A1&gt;100;\"korting\";\"geen korting\")."),
            ("p", "<strong>Een geneste ALS is een ALS in een ALS</strong>, en dient juist om meer dan één "
                  "voorwaarde na elkaar te testen, bijvoorbeeld drie kortingstarieven."),
            ("p", "<strong>In een boekhoudblad gebruik je ALS</strong> om korting te geven boven een bedrag, "
                  "een rekening te kiezen naar het soort kost, of te tonen of een factuur betaald is. Sorteren "
                  "is geen formule maar een bewerking op het blad."),
            ("kader", tabel(["functie", "wat ze doet"],
                            [["<strong>VERT.ZOEKEN</strong>", "<strong>zoekt in de eerste kolom van een tabel</strong> en geeft iets uit dezelfde rij terug; daarom moet de zoekkolom vooraan staan"],
                             ["<strong>HORIZ.ZOEKEN</strong>", "<strong>zoekt in de eerste rij</strong> van een tabel"],
                             ["<strong>LINKS</strong> en <strong>RECHTS</strong>", "<strong>de eerste of de laatste tekens van een tekst</strong>: =LINKS(A1;3) geeft de eerste drie"],
                             ["<strong>HOOFDLETTERS</strong> en <strong>KLEINE LETTERS</strong>", "<strong>tekst in kapitalen of in kleine letters zetten</strong>"]])),
            ("p", "<strong>Wordt de waarde niet gevonden, dan geeft een zoekfunctie een foutmelding.</strong> "
                  "Die kan je opvangen met een functie als ALS.FOUT."),
        ]),
        dict(kop="Relatief, absoluut en gemengd", blokken=[
            ("p", "<strong>Een relatieve celverwijzing schuift mee bij het kopiëren.</strong> Kopieer je "
                  "=A1+B1 een rij lager, dan staat er =A2+B2. Dat is wat je meestal wil."),
            ("p", "<strong>Een absolute verwijzing schuift niet mee.</strong> <strong>Je schrijft ze met "
                  "dollartekens</strong>: <strong>een absolute verwijzing naar cel C2 is $C$2</strong>, met een "
                  "dollarteken voor de kolomletter en een voor het rijnummer. <strong>Een gemengde verwijzing "
                  "zet de kolom of de rij vast, niet beide</strong>: $C2 houdt de kolom vast, C$2 de rij."),
            ("p", "<strong>Waarvoor dient dat? Voor een vast gegeven, zoals een btw-tarief in één cel.</strong> "
                  "Elke formule kijkt dan naar diezelfde cel, en wijzigt het tarief, dan pas je één cel aan en "
                  "volgen alle formules."),
            ("p", "<strong>Dollartekens in een formule betekenen niet dat het om geld gaat.</strong> Ze zetten "
                  "een verwijzing vast; geld maak je met de muntnotatie."),
        ]),
    ])


# ───────────────────────── 13. Grafieken maken en lezen
zet("grafieken-maken-en-lezen",
    titel="Grafieken maken en lezen",
    onder="Welke grafiek bij welke boodschap past, de onderdelen van een grafiek, en hoe je een grafiek leest zonder je te laten misleiden.",
    secties=[
        dict(kop="De grafiek bij je boodschap", blokken=[
            ("p", "<strong>Het nut van een grafiek is cijfers in beeld brengen</strong>: een beeld laat een "
                  "verschil of een verloop sneller zien dan een rij getallen. <strong>Je kiest het "
                  "grafiektype naar je boodschap</strong>, niet naar wat mooi staat."),
            ("kader", tabel(["grafiek", "waarvoor", "voorbeeld"],
                            [["<strong>de lijngrafiek</strong>", "<strong>een evolutie in de tijd</strong>: de lijn laat zien of iets stijgt, daalt of gelijk blijft", "<strong>de omzet per maand over een jaar</strong>"],
                             ["<strong>de kolomgrafiek</strong>", "<strong>waarden naast elkaar vergelijken</strong>, met staande balken", "<strong>twee jaren naast elkaar, twee kolommen per categorie</strong>"],
                             ["<strong>de staafgrafiek</strong>", "<strong>hetzelfde met liggende balken</strong>, handig bij lange namen naast de as", "<strong>de omzet per product</strong>"],
                             ["<strong>het cirkeldiagram</strong>", "<strong>delen van een geheel</strong>: alle schijfjes samen zijn honderd procent", "<strong>het aandeel per kostensoort</strong>"]])),
            ("p", "<strong>Een cirkeldiagram is niet geschikt voor twintig categorieën</strong>: met te veel "
                  "schijfjes leest niemand het nog, dus houd het bij een handvol. En <strong>een cirkeldiagram "
                  "kan geen percentages boven honderd tonen</strong>: de hele cirkel ís honderd procent, dus "
                  "komt je som hoger uit, dan zit er een fout in."),
            ("p", "<strong>De vakfiche noemt de kolomgrafiek, de lijngrafiek en het cirkeldiagram.</strong> "
                  "Een organogram is geen grafiek van cijfers maar een schema."),
            ("fig", svg.staafdiagram([("jan", 12), ("feb", 15), ("mrt", 14), ("apr", 19), ("mei", 22)],
                                     breedte=400, hoogte=190, stap=5, waarden=True),
             "Een kolomgrafiek van vijf maanden: de maanden staan op de horizontale as, de waarden op de "
             "verticale, en de as begint bij nul."),
        ]),
        dict(kop="De onderdelen van een grafiek", blokken=[
            ("p", "<strong>Een grafiekelement is een onderdeel van de grafiek</strong>: de titel, de assen, de "
                  "legende, de rasterlijnen en de labels. <strong>De titel, de legende en de gegevenslabels "
                  "kan je aan en uit zetten</strong>; formules staan in het blad, niet in de grafiek."),
            ("kader", tabel(["onderdeel", "wat het is"],
                            [["<strong>de verticale as</strong>", "<strong>de waarden</strong>: daar lees je de hoogte van de kolom af"],
                             ["<strong>de horizontale as</strong>", "<strong>de categorieën</strong>: de maanden, de producten of de afdelingen"],
                             ["<strong>de astitel</strong>", "<strong>wat de as meet</strong>, bijvoorbeeld omzet in euro of aantal stuks"],
                             ["<strong>de legende</strong>", "<strong>welke kleur bij welke reeks hoort</strong>"],
                             ["<strong>een gegevensreeks</strong>", "<strong>één rij met waarden</strong>, bijvoorbeeld de omzet van 2026; een tweede reeks is die van 2027"],
                             ["<strong>een gegevenslabel</strong>", "<strong>de waarde bij de balk geschreven</strong>, voor als de precieze waarde telt"],
                             ["<strong>de rasterlijnen</strong>", "<strong>de lijnen achter de grafiek</strong> die je oog naar de as leiden"]])),
            ("p", "<strong>Een grafiek in een rekenblad verandert mee als je de cijfers aanpast</strong>: ze "
                  "kijkt naar het bereik, dus wijzigt een cel, dan beweegt de balk. <strong>Ze bewaart geen "
                  "eigen kopie van de cijfers</strong>, en dat is net het nut ervan."),
            ("p", "<strong>Om een grafiek leesbaar te houden geef je ze een duidelijke titel, zet je de "
                  "eenheid bij de as en toon je niet te veel reeksen.</strong> Veel kleuren maken het drukker, "
                  "niet duidelijker. <strong>Een grafiek zonder titel laat de lezer gissen waarover ze "
                  "gaat</strong>; de titel zegt wat er gemeten is en over welke periode."),
        ]),
        dict(kop="Een grafiek eerlijk en kritisch lezen", blokken=[
            ("p", "<strong>De verticale as hoort meestal bij nul te beginnen</strong>, anders lijkt het "
                  "verschil groter dan het is: een as die bij 90 begint, maakt van een klein verschil een hoge "
                  "berg."),
            ("kader", tabel(["wat een grafiek misleidend maakt", "wat een grafiek betrouwbaar maakt"],
                            [["<strong>een as die niet bij nul begint</strong>", "<strong>de bron vermelden</strong>, met het jaar erbij"],
                             ["<strong>een as met ongelijke stappen</strong>", "<strong>de eenheid bij de as zetten</strong>"],
                             ["<strong>een stuk uit de reeks weglaten</strong>", "<strong>de hele reeks tonen</strong>"]])),
            ("p", "<strong>Bij cijfers van iemand anders zet je de bron erbij</strong>: waar ze vandaan komen "
                  "en van welk jaar ze zijn. <strong>De maker hoeft er niet op</strong>, de bron wel."),
            ("p", "<strong>Een grafiek maakt de cijfers niet nauwkeuriger dan een tabel.</strong> Een grafiek "
                  "toont een beeld, een tabel de exacte waarden. Daarom: <strong>zijn twee kolommen bijna even "
                  "hoog, kijk dan naar de labels voor het echte verschil</strong>."),
            ("p", "<strong>Wat je uit een omzetgrafiek kan lezen</strong>: in welke maanden het goed ging, of "
                  "de omzet stijgt of daalt, en welke maand het hoogst is. <strong>Een piek is een maand met "
                  "veel verkoop</strong>, en daar hoort een verklaring bij: een actie, een feestdag, een grote "
                  "klant. <strong>Winst zie je er niet in</strong>: daarvoor moet je ook de kosten kennen."),
            ("weetje", "In een jaarverslag staan grafieken naast de tabellen, en dat is geen opsmuk: een "
                       "evolutie over vijf jaar zie je in één oogopslag, terwijl je ze in een tabel moet "
                       "uitrekenen."),
        ]),
    ])


# ───────────────────────── 14. Afdrukken, kopiëren en scannen
zet("afdrukken-kopieren-en-scannen",
    titel="Afdrukken, kopiëren en scannen",
    onder="Het multifunctionele toestel en zijn onderdelen, de instellingen die je vooraf kiest, veelvoorkomende meldingen, en scannen met tekenherkenning.",
    secties=[
        dict(kop="Het toestel en zijn onderdelen", blokken=[
            ("p", "<strong>Een multifunctioneel toestel is printer, scanner en copier in één</strong>: het "
                  "drukt af, kopieert en scant."),
            ("kader", tabel(["onderdeel", "waarvoor"],
                            [["<strong>de papierlade</strong>", "<strong>de bak met blad erin</strong>; vaak zijn er meerdere laden, één per formaat"],
                             ["<strong>de inkt- of tonercassette</strong>", "<strong>waar de inkt of het poeder in zit</strong>"],
                             ["<strong>het bedieningsscherm</strong>", "<strong>waar je de instellingen kiest en de meldingen leest</strong>"],
                             ["<strong>de glasplaat</strong>", "<strong>waar je een blad legt</strong>, met de bedrukte zijde naar beneden tegen de hoek; enkel een toestel dat ook scant of kopieert heeft er een"],
                             ["<strong>de doorvoer bovenaan</strong>", "<strong>bladen één per één nemen</strong>, zodat je een hele stapel in één keer kopieert of scant"]])),
            ("p", "<strong>Een inkjetprinter werkt met vloeibare inkt, een laserprinter met poeder</strong>, "
                  "dat toner heet. Daarom is een laserprinter per blad goedkoper zodra je veel afdrukt."),
        ]),
        dict(kop="Instellen voor je op start drukt", blokken=[
            ("p", "<strong>De printereigenschappen zijn de instellingen vooraf</strong>: het venster waar je "
                  "lade, kwaliteit, kleur en dubbelzijdig kiest. <strong>Met het afdrukbereik kies je welke "
                  "bladzijden</strong> eruit komen, bijvoorbeeld enkel blad 2 tot 5."),
            ("kader", tabel(["instelling", "wat ze doet"],
                            [["<strong>dubbelzijdig</strong>", "<strong>op beide zijden afdrukken</strong>, ook recto verso of duplex genoemd; twintig bladzijden passen dan op tien bladen"],
                             ["<strong>zwart-wit of kleur</strong>", "<strong>kleur gebruikt meerdere cassettes</strong> en is per blad duurder"],
                             ["<strong>het aantal exemplaren</strong>", "<strong>hoeveel kopieën</strong> je van hetzelfde blad wil"],
                             ["<strong>verkleinen of vergroten</strong>", "<strong>kleiner of groter op het blad</strong>: twee A4 op één A4 heet ook twee op één"]])),
            ("p", "<strong>Druk een eerste blad als proef af om fouten te zien.</strong> Honderd flyers met "
                  "een fout erin zijn honderd flyers verloren."),
            ("p", "<strong>Afdrukken naar pdf maakt een bestand</strong>: er komt geen blad uit en er wordt "
                  "geen inkt gebruikt. <strong>Een pdf open je op elke computer</strong>, ook zonder het "
                  "programma waarin hij gemaakt is, en daarom is het de gewoonte voor een factuur of een "
                  "contract. <strong>Een drukker stuur je liever een pdf, omdat de opmaak dan juist "
                  "blijft</strong>: een lettertype dat de drukker niet heeft wordt anders vervangen, maar in "
                  "een pdf zit het mee."),
        ]),
        dict(kop="Als er iets misloopt", blokken=[
            ("kader", tabel(["melding of situatie", "wat ze betekent en wat je doet"],
                            [["<strong>papierstoring</strong>", "<strong>een blad zit vast</strong>: open de klep en trek het blad voorzichtig mee met de richting van de doorvoer"],
                             ["<strong>geen verbinding</strong>", "<strong>de printer is onbereikbaar</strong>: kijk de kabel of het netwerk na, en of hij wel aan staat"],
                             ["<strong>geen papier</strong>", "<strong>de opdracht blijft in de wachtrij staan</strong> tot je papier bijvult; afdrukken zonder papier gaat niet"],
                             ["<strong>de afdrukwachtrij</strong>", "<strong>de lijst met opdrachten</strong>; daar annuleer je een opdracht die je per ongeluk startte"]])),
            ("p", "<strong>Doet een printer niets, kijk dan eerst of hij aan staat, of er papier in zit, en "
                  "wat er in de wachtrij staat.</strong> Eerst het eenvoudigste nakijken, daarna pas het "
                  "netwerk."),
        ]),
        dict(kop="Scannen en tekenherkenning", blokken=[
            ("p", "<strong>Een scanner maakt papier digitaal</strong>: van een blad maakt hij een bestand op "
                  "de computer. <strong>De vakfiche noemt de leespen, de handscanner en de "
                  "vlakbedscanner.</strong>"),
            ("kader", tabel(["soort scanner", "hoe hij werkt"],
                            [["<strong>de vlakbedscanner</strong>", "<strong>een glasplaat met een deksel</strong>: je legt het blad op het glas"],
                             ["<strong>de handscanner</strong>", "<strong>je sleept hem zelf over het blad</strong>"],
                             ["<strong>de leespen</strong>", "<strong>je schuift hem over één regel tekst</strong>, en die komt op de computer"]])),
            ("p", "<strong>Bij een scan stel je kleur of zwart-wit, de resolutie en het bestandstype in.</strong> "
                  "<strong>Een hoge resolutie geeft meer detail</strong>, meer puntjes per duim, maar ook een "
                  "zwaarder bestand. Exemplaren horen bij afdrukken, niet bij scannen."),
            ("p", "<strong>OCR staat voor optische tekenherkenning</strong>: tekst herkennen in een beeld. "
                  "<strong>Zonder OCR is een scan een foto van tekst</strong>, een afbeelding waarin je niet "
                  "kan zoeken, want de computer ziet er enkel puntjes en geen letters. <strong>Met OCR kan je "
                  "erin zoeken en eruit kopiëren.</strong>"),
            ("p", "<strong>Tekenherkenning werkt niet altijd foutloos</strong>, zeker niet bij een slecht "
                  "leesbaar handschrift. <strong>Kijk een herkende tekst dus altijd na, vooral de "
                  "cijfers.</strong>"),
            ("p", "<strong>Een factuur scan je in om ze digitaal te bewaren</strong>: zo zit ze in de "
                  "boekhouding en vind je ze later terug. <strong>Gescande documenten nemen geen plaats in, "
                  "je vindt ze terug met zoeken en je kan ze doorsturen</strong> — maar bewaren moet wel, want "
                  "de wet zegt hoe lang je je boekhouding moet bijhouden."),
        ]),
    ])


# ───────────────────────── 15. Bestanden beheren en bewaren
zet("bestanden-beheren-en-bewaren",
    titel="Bestanden beheren en bewaren",
    onder="Mappen, bestandsnamen en extensies, de back-up en de cloud, en hoe je documenten van klanten veilig bewaart.",
    secties=[
        dict(kop="Mappen en namen", blokken=[
            ("p", "<strong>Een map is een plaats voor bestanden</strong>, en <strong>een map kan ook andere "
                  "mappen bevatten</strong>: een map in een map heet een submap. <strong>Submappen dienen om "
                  "orde te houden</strong>, zodat je een bestand terugvindt zonder te zoeken."),
            ("p", "<strong>Een logische mappenstructuur werkt per onderwerp</strong>: bijvoorbeeld "
                  "boekhouding, dan het jaar, dan aankoop en verkoop. <strong>Wat zo'n structuur werkbaar "
                  "maakt, zijn een vaste indeling, duidelijke namen en niet te veel niveaus.</strong> Een "
                  "bureaublad vol losse bestanden is geen structuur."),
            ("p", "<strong>Het pad van een bestand zegt waar het staat</strong>: de rij mappen van de schijf "
                  "tot het bestand zelf. <strong>Twee bestanden in dezelfde map mogen niet dezelfde naam "
                  "hebben</strong>; in een andere map mag het wel, want dan is het pad verschillend."),
            ("p", "<strong>Achter de punt in een bestandsnaam staat de extensie</strong>, die zegt welk soort "
                  "bestand het is. <strong>Een bestandsnaam mag tegenwoordig ruim lang zijn</strong>; de "
                  "oude grens van acht tekens bestaat niet meer. <strong>Gebruik wel geen spaties en rare "
                  "tekens</strong>: bij doorsturen of op een website gaat het soms mis. Streepjes werken "
                  "altijd."),
            ("kader", tabel(["extensie", "wat het is"],
                            [["<strong>.docx</strong>", "<strong>een document</strong> van een tekstverwerker"],
                             ["<strong>.xlsx</strong>", "<strong>een rekenblad</strong>"],
                             ["<strong>.pptx</strong>", "<strong>een presentatie</strong>"],
                             ["<strong>.pdf</strong>", "<strong>een vast opgemaakt document</strong>, dat er op elk toestel hetzelfde uitziet"],
                             ["<strong>.exe</strong>", "<strong>een programma</strong>, geen document"]])),
            ("p", "<strong>Een goede naam voor een factuur is 2027-03-factuur-vermeulen</strong>: de datum "
                  "vooraan, dan waarover het gaat en voor wie. Zo staat alles vanzelf op datum in de map."),
            ("p", "<strong>Een bestand kan je hernoemen, verplaatsen en kopiëren.</strong> <strong>Kopiëren "
                  "laat het origineel staan, verplaatsen niet.</strong> <strong>Een gewist bestand komt eerst "
                  "in de prullenbak of prullenmand</strong> en kan je daar nog terugzetten; pas als je de prullenbak "
                  "leegmaakt, is het echt weg."),
        ]),
        dict(kop="De back-up", blokken=[
            ("p", "<strong>Een back-up is een tweede kopie</strong>, een veiligheidskopie op een andere plaats "
                  "dan het origineel. <strong>Je maakt er een om niets te verliezen</strong>: een schijf die "
                  "stuk gaat, een diefstal of een verkeerde klik, alles kan."),
            ("kader", tabel(["soort", "waar ze staat"],
                            [["<strong>een offline back-up</strong>", "<strong>op een externe schijf</strong> of een usb-stick, die je daarna losmaakt"],
                             ["<strong>een online back-up</strong>", "<strong>op een server elders</strong>, in de cloud, dus buiten je gebouw"]])),
            ("p", "<strong>Een back-up op dezelfde computer helpt niet als die computer stuk gaat.</strong> "
                  "Daarom hoort ze op een ander toestel of op een andere plaats. En <strong>één back-up per "
                  "jaar is veel te weinig voor een boekhouding</strong>: je verliest dan alles van dat jaar, "
                  "dus bewaar je ze best dagelijks."),
        ]),
        dict(kop="De cloud", blokken=[
            ("p", "<strong>Cloudopslag is opslag op een server</strong>: je bestanden staan op een computer "
                  "elders, die je via het internet bereikt. <strong>Uploaden is iets naar het internet zetten, "
                  "downloaden is iets van het internet halen.</strong>"),
            ("p", "<strong>Het voordeel van de cloud: je kan overal aan je bestanden, je hebt een kopie buiten "
                  "je huis, en je kan samen in één bestand werken.</strong> Het nadeel zit in dezelfde zin: "
                  "zonder internet geraak je er net niet aan."),
            ("p", "<strong>Synchroniseren is een bestand op twee plaatsen gelijk houden</strong>: pas je het "
                  "op je laptop aan, dan verandert het ook in de cloud. <strong>Wijzigt iemand een gedeeld "
                  "bestand, dan ziet iedereen die wijziging</strong>, want er is één bestand en geen kopie per "
                  "persoon. Dat is precies waarom samen werken werkt."),
            ("p", "<strong>Een bestand in de cloud is niet automatisch beveiligd.</strong> Een deellink die "
                  "rondgaat, geeft iedereen toegang, dus deel per persoon. <strong>Delen kan met alleen lezen "
                  "of ook met bewerken</strong>: geef alleen lezen als de ander niets hoeft te wijzigen."),
        ]),
        dict(kop="Documenten van klanten", blokken=[
            ("p", "<strong>Op een bestand met persoonsgegevens zet je een wachtwoord</strong>: gegevens van "
                  "klanten of werknemers mogen niet bij wie ze niet nodig heeft."),
            ("kader", tabel(["wat je afspreekt in een zaak", "waarom"],
                            [["<strong>waar de documenten bewaard worden</strong>", "<strong>zo zoekt niemand</strong> en staat niets op een los bureaublad"],
                             ["<strong>wie eraan mag</strong>", "<strong>enkel wie het nodig heeft</strong>; een openbare schijf is het tegendeel van beveiligen"],
                             ["<strong>hoe lang ze bijgehouden worden</strong>", "<strong>voor een boekhouding legt de wet die bewaartermijn vast</strong>"]])),
            ("p", "<strong>Veilig bewaren is dus drie dingen tegelijk</strong>: enkel wie het nodig heeft "
                  "erbij laten, een back-up op een andere plaats, en een wachtwoord op de gevoelige bestanden."),
        ]),
    ])


# ───────────────────────── 16. Presenteren en gegevens in een databank
zet("presenteren-en-gegevens-in-een-databank",
    titel="Presenteren en gegevens in een databank",
    onder="Een presentatie die je verhaal steunt in plaats van voorleest, en de opbouw van een databank met tabellen, records, velden, formulieren, query's en rapporten.",
    secties=[
        dict(kop="Een presentatie opbouwen", blokken=[
            ("p", "<strong>Een dia is één scherm met inhoud</strong>, en de dia's volgen elkaar op terwijl je "
                  "spreekt. <strong>Een presentatie is een steun bij je verhaal, niet je verhaal zelf</strong>: "
                  "het publiek moet naar jou luisteren en niet je dia's zitten lezen."),
            ("p", "<strong>Daarom zet je niet je hele tekst op de dia om die voor te lezen</strong>: het "
                  "publiek leest sneller dan jij spreekt en haakt af. <strong>Het KISS-principe zegt: houd het "
                  "eenvoudig</strong>, keep it short and simple — <strong>één idee per dia</strong>, weinig "
                  "tekst, grote letters."),
            ("p", "<strong>Een dia is van ver leesbaar door grote letters, veel contrast en weinig "
                  "tekst.</strong> Een drukke achtergrond maakt de tekst juist moeilijker leesbaar."),
            ("kader", tabel(["begrip", "wat het is"],
                            [["<strong>een overgang</strong>, ook een transitie", "<strong>de wissel tussen twee dia's</strong>"],
                             ["<strong>een animatie</strong>", "<strong>beweging binnen één dia</strong>, zoals een opsomming die regel per regel verschijnt"],
                             ["<strong>de notities</strong>", "<strong>je spiekblad</strong>: enkel jij ziet ze, het publiek ziet de dia zelf"],
                             ["<strong>een hand-out</strong>", "<strong>de dia's op papier</strong>, meerdere per blad, soms met lijnen om bij te schrijven"],
                             ["<strong>een storyboard</strong>", "<strong>een plan per beeld</strong>: je tekent eerst ruw wat op elke dia komt, voor je begint op te maken"],
                             ["<strong>de diavoorstelling</strong>", "<strong>de presentatie tonen</strong>: de dia's vullen het scherm en je klikt ze door"]])),
            ("p", "<strong>Hoe meer animaties, hoe sterker je presentatie? Net niet</strong>: te veel beweging "
                  "leidt af van wat je zegt. <strong>Een sjabloon gebruik je wél</strong>, want dan ziet alles "
                  "er hetzelfde uit: dezelfde kleuren, lettertypes en plaats van de titel op elke dia."),
            ("p", "<strong>In een presentatie kan je een afbeelding, een filmpje en een geluid "
                  "invoegen</strong>, en ook een tabel of een grafiek uit een rekenblad overnemen. <strong>In "
                  "een zakelijke presentatie horen een titeldia met het onderwerp, cijfers in een grafiek en "
                  "een slot met je besluit.</strong>"),
            ("p", "<strong>Een mindmap is een schema met takken</strong>: het onderwerp in het midden, met "
                  "takken naar de onderdelen. <strong>Een infographic brengt informatie in beeld met cijfers "
                  "en tekeningen</strong>: één beeld dat een verhaal vertelt, in plaats van een bladzijde "
                  "tekst."),
        ]),
        dict(kop="Wat een databank is", blokken=[
            ("p", "<strong>Een databank is een geordende verzameling gegevens</strong>, zo geordend dat je ze "
                  "kan opvragen en combineren. <strong>Waarom werkt een zaak ermee in plaats van met een "
                  "rekenblad? Omdat de gegevens er maar één keer in staan</strong>: een adres dat wijzigt pas "
                  "je op één plaats aan en overal verandert het mee."),
            ("kader", tabel(["onderdeel", "wat het is"],
                            [["<strong>een tabel</strong>", "<strong>de plaats van de gegevens</strong>; de rest van de databank kijkt ernaar"],
                             ["<strong>een record</strong>", "<strong>één rij met gegevens</strong>: één klant, één factuur, één leerling"],
                             ["<strong>een veld</strong>", "<strong>één soort gegeven</strong>, bijvoorbeeld het veld naam of het veld postcode"],
                             ["<strong>een formulier</strong>", "<strong>een invulscherm</strong>, veel vriendelijker dan rechtstreeks in de tabel typen"],
                             ["<strong>een query</strong>, een zoekvraag", "<strong>een vraag aan de databank</strong> om bepaalde gegevens te krijgen"],
                             ["<strong>een rapport</strong>", "<strong>een overzicht om netjes af te drukken</strong>, met koppen, groepen en totalen"]])),
            ("p", "<strong>De vakfiche noemt tabellen, formulieren, rapporten en query's</strong> als de "
                  "onderdelen van een databank. Dia's horen bij een presentatie."),
        ]),
        dict(kop="Velden en sleutels", blokken=[
            ("p", "<strong>Het gegevenstype van een veld zegt wat erin mag</strong>: tekst, een getal, een "
                  "datum, ja of nee, of een bedrag. <strong>Voor een geboortedatum kies je het type "
                  "datum</strong>: zet je het als tekst, dan kan je er niet mee rekenen of op sorteren."),
            ("p", "<strong>Een veldeigenschap hoort bij een veld</strong>, niet bij de tabel: de veldlengte, "
                  "of het veld verplicht is, en een standaardwaarde."),
            ("p", "<strong>De primaire sleutel is het veld dat elk record uniek maakt.</strong> <strong>Ze is "
                  "in elk record anders</strong>, en <strong>twee records mogen dus niet dezelfde primaire "
                  "sleutel hebben</strong>: de databank weigert dat, want dan weet ze niet meer welk record je "
                  "bedoelt. <strong>Daarmee herken je een record</strong>: twee klanten kunnen dezelfde naam "
                  "hebben, geen twee hetzelfde klantnummer."),
        ]),
        dict(kop="Gegevens opvragen", blokken=[
            ("p", "<strong>Met een query vraag je gegevens op</strong>: enkel de klanten uit Limburg, "
                  "gesorteerd op naam, of velden uit twee tabellen samengebracht. <strong>Een selectiequery "
                  "wijzigt niets aan de gegevens</strong>, ze haalt ze enkel op."),
            ("p", "<strong>Een filter toont minder records</strong>: enkel die aan je voorwaarde voldoen "
                  "blijven zichtbaar."),
            ("weetje", "Het verschil tussen een query en een rapport zit in waar het naartoe gaat: een query "
                       "zoekt de gegevens bij elkaar, een rapport zet ze netjes op papier.")
        ]),
    ])
