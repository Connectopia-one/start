# -*- coding: utf-8 -*-
"""Uitdaging Samenleving en economie 🌍 Beyond doorstroom (25 november 2026),
in de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Een vereenvoudigde loonbrief en een verdachte
mail om op te klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren,
volgorde, rekenvragen en een korte schrijfopdracht. Geen nieuwe leerstof:
alles staat in de hoofdstukken van Samenleving en economie Beyond doorstroom.
Alle namen en cijfers zijn verzonnen.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_samenleving.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Samenleving en economie"
BESTAND = "beyond-samenleving-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/samenleving-beyond-uitdaging"
LOON = "loonbrief.svg"
MAIL = "mail-bank.svg"


def zin(i, n=6):
    """Klikvak van regel i (vanaf 1), zie uitdaging/_blad.py."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Loonbrief (prent)
    klik("Bekijk de loonbrief. Klik op het bedrag dat Sara echt op haar rekening krijgt.",
         LOON, [zin(5)],
         "Het nettoloon is wat overblijft na de RSZ-bijdrage en de bedrijfsvoorheffing: 2067,90 euro."),
    klik("Klik op de inhouding die de sociale zekerheid financiert.",
         LOON, [zin(2)],
         "De persoonlijke RSZ-bijdrage van 13,07 % gaat naar de sociale zekerheid: pensioenen, ziekteverzekering, werkloosheid, ..."),
    klik("Klik op de regel die Sara later verrekent bij haar jaarlijkse belastingaangifte.",
         LOON, [zin(4)],
         "De bedrijfsvoorheffing is een voorschot op de personenbelasting. Bij de belastingaangifte wordt afgerekend."),
    met_prent(LOON, tabel(
        "Klopt dit over de loonbrief?",
        [
            ("Belastbaar loon = brutoloon − RSZ-bijdrage", J),
            ("Maaltijdcheques zijn een extralegaal voordeel.", J),
            ("De werkgever betaalt geen eigen RSZ-bijdragen bovenop het brutoloon.", F),
            ("Het nettoloon is meestal hoger dan het brutoloon.", F),
        ],
        "3000 − 392,10 = 2607,90. Maaltijdcheques krijg je bovenop het loon. De werkgever betaalt ook nog werkgeversbijdragen; die staan niet op deze vereenvoudigde brief.")),
    met_prent(LOON, inv(
        "Hoeveel procent van haar brutoloon houdt Sara netto over? Rond af op een geheel getal.",
        ["69"],
        "2067,90 / 3000 · 100 ≈ 68,9, afgerond 69 %.")),

    # Mail (prent)
    klik("Bekijk de mail. Klik op de regel die het duidelijkst verraadt dat de mail niet van je bank komt.",
         MAIL, [zin(1)],
         "Het adres 'bankk-be-veilig.com' is vreemd gespeld en is niet het officiële adres van een bank. Dat is een typisch kenmerk van phishing."),
    klik("Klik op de regel die je onder druk wil zetten.",
         MAIL, [zin(3)],
         "Oplichters jagen je op met een dreiging en een korte termijn, zodat je zonder nadenken klikt."),
    met_prent(MAIL, mk(
        "Hoe reageer je het veiligst op deze mail van je zogenaamde bank?",
        ["Niet klikken, de mail melden en verwijderen.", "Op de link klikken en enkel je kaartnummer invullen.", "Antwoorden met de vraag of de mail echt is.", "De mail doorsturen naar al je vrienden als test."],
        0,
        "Een bank vraagt nooit je pincode per mail. Klik niet, meld de mail (bv. bij verdacht@safeonweb.be) en verwijder ze.")),

    # Identiteit en diversiteit
    tabel(
        "Hoort deze factor bij je persoonlijke of bij je sociale identiteit?",
        [
            ("Je karakter en je interesses", "Persoonlijke identiteit"),
            ("Lid zijn van een voetbalclub", "Sociale identiteit"),
            ("Je nationaliteit", "Sociale identiteit"),
            ("Je eigen waarden en dromen", "Persoonlijke identiteit"),
        ],
        "Je persoonlijke identiteit is wat jou uniek maakt. Je sociale identiteit komt van de groepen waartoe je behoort.",
        kolommen=["Persoonlijke identiteit", "Sociale identiteit"]),
    keuze(
        "Iemand beoordelen enkel op basis van een groep waartoe die hoort, is een [[*vooroordeel|ik-boodschap|compromis]]. Iemand daardoor anders behandelen, heet [[*discriminatie|integratie|empathie]].",
        "Een vooroordeel is een mening zonder kennis van de persoon. Discriminatie is ongelijke behandeling op basis van zo'n kenmerk."),
    mk("Welke zin is een ik-boodschap?",
       ["Ik word onrustig als je laat komt, want dan mis ik de bus.", "Jij komt altijd te laat en je denkt nooit eens aan een ander.", "Iedereen hier ergert zich eraan dat jij nooit op tijd bent.", "Waarom kan jij nu eens nooit gewoon op tijd komen, zeg?"],
       0,
       "Een ik-boodschap beschrijft je eigen gevoel, het gedrag en het gevolg, zonder de ander te beschuldigen."),

    # Eerste hulp
    volgorde(
        "Zet de stappen van eerste hulp bij een bewusteloos slachtoffer in de juiste volgorde.",
        ["Zorg voor je eigen veiligheid", "Spreek het slachtoffer aan en schud zacht", "Roep om hulp", "Controleer de ademhaling", "Bel 112"],
        "Eerst veiligheid, dan bewustzijn en ademhaling controleren, en hulp laten komen."),
    tabel(
        "Wat doe je?",
        [
            ("Slachtoffer is bewusteloos maar ademt normaal", "Stabiele zijligging"),
            ("Slachtoffer is bewusteloos en ademt niet normaal", "Reanimeren en AED laten halen"),
            ("Slachtoffer heeft een kleine schaafwonde", "Wonde spoelen en ontsmetten"),
        ],
        "Wie normaal ademt, leg je in stabiele zijligging. Zonder normale ademhaling start je reanimatie. Een schaafwonde spoel je met water.",
        kolommen=["Stabiele zijligging", "Reanimeren en AED laten halen", "Wonde spoelen en ontsmetten"]),
    keuze(
        "Bij reanimatie van een volwassene geef je [[*30|15|5]] borstcompressies en daarna [[*2|5|10]] beademingen.",
        "Het ritme is 30 compressies en 2 beademingen, aan ongeveer 100 tot 120 compressies per minuut."),
    mk("Wat doet een AED?",
       ["Het analyseert het hartritme en geeft zo nodig een schok.", "Het meet de bloeddruk en geeft een pijnstiller via de huid.", "Het neemt de beademing volledig over tot de ambulance er is.", "Het verwittigt automatisch de huisarts van het slachtoffer."],
       0,
       "Een automatische externe defibrillator geeft spraakinstructies, analyseert het ritme en geeft enkel een schok als dat nodig is."),

    # Overheid en sociale zekerheid
    sorteer(
        "Brengt dit geld op voor de overheid of kost het de overheid geld?",
        ["Brengt op", "Kost geld"],
        [
            ["Btw op aankopen", "Brengt op"],
            ["Pensioenen", "Kost geld"],
            ["Personenbelasting", "Brengt op"],
            ["Onderwijs", "Kost geld"],
            ["Accijnzen op brandstof", "Brengt op"],
            ["Rente op de staatsschuld", "Kost geld"],
        ],
        "De overheid haalt geld op via directe en indirecte belastingen en geeft het uit aan diensten, uitkeringen en rente."),
    tabel(
        "Is dit een directe of een indirecte belasting?",
        [
            ("Personenbelasting", "Directe belasting"),
            ("Btw", "Indirecte belasting"),
            ("Onroerende voorheffing", "Directe belasting"),
            ("Accijns op alcohol", "Indirecte belasting"),
        ],
        "Directe belastingen hangen af van je inkomen of bezit. Indirecte belastingen betaal je via de prijs van wat je koopt.",
        kolommen=["Directe belasting", "Indirecte belasting"]),
    koppel(
        "Koppel de tak van de sociale zekerheid aan de situatie.",
        [
            ["werkloosheid", "uitkering na ontslag"],
            ["ziekte- en invaliditeitsverzekering", "terugbetaling van doktersbezoek"],
            ["pensioenen", "inkomen na de loopbaan"],
            ["gezinsbijslag", "Groeipakket voor kinderen"],
        ],
        ["leefloon van het OCMW"],
        "Het leefloon is sociale bijstand van het OCMW, geen tak van de sociale zekerheid die gefinancierd wordt met bijdragen."),

    # Markt
    keuze(
        "Als de vraag naar fietsen stijgt bij een gelijk aanbod, dan [[*stijgt|daalt]] de prijs. Als het aanbod stijgt bij een gelijke vraag, dan [[*daalt|stijgt]] de prijs.",
        "Meer vraag duwt de evenwichtsprijs omhoog; meer aanbod duwt ze omlaag."),
    tabel(
        "Verschuift de vraagcurve of de aanbodcurve van elektrische fietsen?",
        [
            ("De overheid geeft een premie aan kopers.", "Vraagcurve"),
            ("Batterijen worden veel goedkoper om te maken.", "Aanbodcurve"),
            ("Een nieuwe fabriek opent in Europa.", "Aanbodcurve"),
            ("Fietsen wordt erg populair bij jongeren.", "Vraagcurve"),
        ],
        "Wat kopers beïnvloedt (premie, mode) verschuift de vraag. Wat producenten beïnvloedt (kosten, fabrieken) verschuift het aanbod.",
        kolommen=["Vraagcurve", "Aanbodcurve"]),

    # Arbeid
    tabel(
        "Klopt dit over werken?",
        [
            ("Het arbeidsreglement bevat onder meer de werkuren.", J),
            ("De preventieadviseur helpt bij veiligheid en welzijn op het werk.", J),
            ("Een vertrouwenspersoon mag alles wat je vertelt meteen aan je baas doorgeven.", F),
            ("Een studentenjob is altijd vrijgesteld van alle bijdragen, hoeveel uur je ook werkt.", F),
        ],
        "Het arbeidsreglement legt de regels op het werk vast. Een vertrouwenspersoon werkt vertrouwelijk. Voor studenten geldt een maximum aantal uren met verminderde bijdragen."),
    inv("Een werknemer verdient 2500 euro bruto. De persoonlijke RSZ-bijdrage is 13,07 %. Hoeveel bedraagt het belastbaar loon? Enkel het getal in euro.",
        ["2173,25", "2173.25"],
        "RSZ = 2500 · 0,1307 = 326,75 euro. Belastbaar loon = 2500 − 326,75 = 2173,25 euro."),

    # Consumentenkrediet en budget
    mk("Je vergelijkt twee leningen voor een auto. Welk cijfer vergelijk je best?",
       ["Het jaarlijkse kostenpercentage (JKP)", "Het bedrag van de allereerste aflossing", "De naam en het logo van de kredietgever", "Hoe mooi de reclamefolder eruitziet"],
       0,
       "Het JKP bevat de rente en alle kosten van het krediet. Zo kan je leningen eerlijk vergelijken."),
    inv("Een smartphone kost 600 euro contant. Op afbetaling betaal je 24 maanden 28 euro. Hoeveel betaal je meer dan contant? Enkel het getal.",
        ["72"],
        "24 · 28 = 672 euro. Dat is 672 − 600 = 72 euro meer."),
    sorteer(
        "Is dit een vaste of een variabele uitgave in een gezinsbudget?",
        ["Vaste uitgave", "Variabele uitgave"],
        [
            ["Huur", "Vaste uitgave"],
            ["Uit eten gaan", "Variabele uitgave"],
            ["Verzekeringspremie", "Vaste uitgave"],
            ["Kleding", "Variabele uitgave"],
        ],
        "Vaste uitgaven komen regelmatig terug met een vast bedrag. Variabele uitgaven kan je zelf meer sturen."),
    keuze(
        "Een spaarrekening geeft 2 % rente en de inflatie is 3 %. Je koopkracht [[*daalt|stijgt|blijft gelijk]] dan, want de reële rente is ongeveer [[*−1 %|5 %|1 %]].",
        "Reële rente ≈ nominale rente − inflatie = 2 − 3 = −1 %. Je geld wordt minder waard."),
    tabel(
        "Is dit sparen of beleggen?",
        [
            ("Geld op een gereglementeerde spaarrekening", "Sparen"),
            ("Aandelen kopen van een bedrijf", "Beleggen"),
            ("Een termijnrekening met vaste rente", "Sparen"),
            ("Instappen in een beleggingsfonds", "Beleggen"),
        ],
        "Sparen is veilig met een lage opbrengst. Beleggen geeft kans op meer opbrengst, maar met risico op verlies.",
        kolommen=["Sparen", "Beleggen"]),

    # Verzekeringen
    tabel(
        "Welke verzekering komt tussen?",
        [
            ("Je zoon breekt per ongeluk de ruit van de buren.", "Familiale verzekering (BA privéleven)"),
            ("Door een kortsluiting brandt je keuken af.", "Brandverzekering"),
            ("Je rijdt met de auto een geparkeerde wagen aan.", "Autoverzekering (BA auto)"),
        ],
        "De familiale dekt schade die je gezin per ongeluk aan anderen toebrengt, de brandverzekering je woning en de BA auto schade met je auto aan anderen.",
        kolommen=["Familiale verzekering (BA privéleven)", "Brandverzekering", "Autoverzekering (BA auto)"]),
    keuze(
        "Het bedrag dat je bij een schadegeval zelf moet betalen, heet de [[*vrijstelling|premie|polis]]. Het contract met de verzekeraar heet de [[*polis|premie|vrijstelling]].",
        "De premie betaal je om verzekerd te zijn, de vrijstelling (franchise) betaal je zelf bij schade, en de polis is het contract."),

    # Digitale vaardigheden
    mk("Welke formule in Excel telt de waarden in B2 tot B10 op?",
       ["=SOM(B2:B10)", "=GEMIDDELDE(B2:B10)", "=AANTAL(B2:B10)", "=MAX(B2:B10)"],
       0,
       "SOM telt op, GEMIDDELDE berekent het gemiddelde, AANTAL telt hoeveel cellen een getal bevatten en MAX geeft de grootste waarde."),
    keuze(
        "In Excel blijft een celverwijzing als [[*$A$1|A1]] vast staan als je de formule kopieert. Dat heet een [[*absolute|relatieve]] celverwijzing.",
        "Met dollartekens zet je de kolom en de rij vast."),
    tabel(
        "Welke tip past bij een goede presentatie in PowerPoint?",
        [
            ("Weinig tekst per dia, liefst kernwoorden", J),
            ("Zo veel mogelijk animaties op elke dia", F),
            ("Een duidelijk lettertype dat groot genoeg is", J),
            ("Alle tekst van je verhaal letterlijk op de dia", F),
        ],
        "Een dia ondersteunt wat je zegt. Te veel tekst of animaties leiden af."),
    keuze(
        "In Word maak je een inhoudstafel automatisch als je de titels opmaakt met [[*kopstijlen|vette letters|een groter lettertype]].",
        "Word herkent titels via de stijlen Kop 1, Kop 2, ... en bouwt daarmee de inhoudstafel op."),

    # Online recht
    tabel(
        "Mag dit volgens het recht online?",
        [
            ("Een foto van een vriend online zetten zonder zijn toestemming", F),
            ("Een eigen gemaakte tekening op je blog posten", J),
            ("Een volledige film doorsturen die je niet zelf maakte", F),
            ("Een kort citaat gebruiken met bronvermelding in een werkstuk", J),
        ],
        "Iedereen heeft recht op zijn eigen beeld. Werk van anderen is beschermd door auteursrecht; een kort citaat met bron mag wel."),

    mk("Wat is een gevolg van een vergrijzende bevolking voor de sociale zekerheid?",
       ["Meer geld voor pensioenen en zorg, met minder werkenden die bijdragen.", "Er zijn veel meer jongeren die een kinderbijslag nodig hebben dan vroeger.", "De sociale zekerheid heeft vanzelf elk jaar meer geld over.", "Werkloosheidsuitkeringen worden overbodig omdat iedereen werkt."],
       0,
       "Meer ouderen betekent meer uitgaven voor pensioenen en gezondheidszorg, terwijl relatief minder actieven bijdragen betalen."),
    keuze(
        "Als de overheid een minimumprijs boven de evenwichtsprijs vastlegt, ontstaat er een [[*overschot|tekort]]. Bij een maximumprijs onder het evenwicht ontstaat een [[*tekort|overschot]].",
        "Boven het evenwicht willen verkopers meer aanbieden dan kopers vragen. Onder het evenwicht is het omgekeerd."),
    tabel(
        "Is dit een sterk of een zwak wachtwoord?",
        [
            ("Sara2008", "Zwak"),
            ("fiets-Tomaat!lamp-71", "Sterk"),
            ("123456", "Zwak"),
            ("Mijn$hond+Bobby_eet*rijst", "Sterk"),
        ],
        "Een sterk wachtwoord is lang, onvoorspelbaar en mengt tekens. Namen, geboortejaren en reeksen zijn makkelijk te raden.",
        kolommen=["Sterk", "Zwak"]),
    inv("Het jaarlijkse budget van een gezin: inkomen 36 000 euro, vaste uitgaven 22 000 euro, variabele uitgaven 11 000 euro. Hoeveel kan het gezin sparen? Enkel het getal.",
        ["3000", "3 000", "3.000"],
        "36 000 − 22 000 − 11 000 = 3000 euro."),
    sorteer(
        "Is dit verbale of non-verbale communicatie?",
        ["Verbaal", "Non-verbaal"],
        [
            ["De woorden die je kiest", "Verbaal"],
            ["Oogcontact", "Non-verbaal"],
            ["Je lichaamshouding", "Non-verbaal"],
            ["Een geschreven bericht", "Verbaal"],
        ],
        "Verbale communicatie gebruikt woorden, gesproken of geschreven. Non-verbale communicatie gebeurt via lichaamstaal, blik en stem."),

    # Schrijfopdracht
    open_("Een vriend van 18 wil een tweedehandsauto kopen met een lening. Geef hem in 4 à 6 zinnen raad: waar moet hij op letten bij de lening, en welke kosten komen er na de aankoop nog bij?",
          "Vergelijk de leningen op het JKP, want dat bevat de rente en alle kosten. Kijk hoeveel je in totaal terugbetaalt en of de maandelijkse aflossing in je budget past. Leen niet langer dan de auto meegaat. Na de aankoop komen er nog kosten bij: de verplichte autoverzekering, de verkeersbelasting, brandstof, onderhoud en de keuring. Hou ook een buffer opzij voor onverwachte herstellingen.",
          "Een goed antwoord vermeldt het JKP of de totale kost van de lening, de aflossing in het budget, en minstens twee kosten na de aankoop zoals verzekering, verkeersbelasting, brandstof, onderhoud of keuring."),
]
