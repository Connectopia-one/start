"""De filosofische vaardigheden — pittig (🚀 Boost doorstroom, kunstbeschouwing en filosofie).

Eigen vragen strikt binnen fi_vaardigheden: een filosofische vraag stellen,
argumenteren met de AUB-methode en het stappenplan voor een filosofische
tekst. Met een zelfgetekend briefje met vier tekstblokjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, LICHTGROEN

BR = Prent("briefje-met-argument", "Een briefje over gsm's in de klas", "een briefje met vier genummerde tekstblokjes")
BR.rect(80, 60, 840, 560, "#fffdf5", DONKER, 10, 3)
BLOK = [("1", 110, 85, ["Stel je voor: je zit midden in een moeilijke toets", "en een gsm trilt drie keer op de bank naast je."]),
        ("2", 110, 215, ["Mijn argument is dat gsm's tijdens de les", "beter in de kast blijven."]),
        ("3", 110, 345, ["Iedereen weet dat. Het is gewoon zo."]),
        ("4", 110, 475, ["Want een melding trekt je aandacht weg,", "en wie zich niet kan concentreren, leert minder."])]
for t, x, y, regels in BLOK:
    BR.rect(x, y, 780, 110, "#ffffff", "#8a8470", 8, 2)
    for i, r in enumerate(regels):
        BR.tekst(x + 80, y + 50 + i * 32, r, 22, "start")
    BR.letter(x + 40, y + 55, t)
U = "briefje-met-argument.svg"
Z = {t: [Prent.zone(x, y, 780, 110)] for t, x, y, r in BLOK}

TEKST = ("Lees het begin van een korte filosofische tekst.\n\n"
         "(1) Veel mensen denken dat geld gelukkig maakt. Wie meer verdient, kan meer kopen en heeft minder zorgen.\n\n"
         "(2) Toch is dat maar de halve waarheid. Wie genoeg heeft om rustig te leven, wordt van nog meer geld nauwelijks gelukkiger. "
         "Bovendien gaan rijke mensen zich vaak vergelijken met wie nog rijker is.\n\n"
         "(3) Kortom: geluk zit niet in het geld zelf, maar in wat je ermee doet en met wie je het deelt.")

VRAGEN = [
    klik("Bekijk het briefje. Klik op het blokje dat de U van de AUB-methode is.", U, Z["4"], "De uitleg begint met want of omdat."),
    klik("Klik op het blokje dat de B van de AUB-methode is.", U, Z["1"], "Stel je voor: een voorbeeld dat het argument concreet maakt."),
    klik("Klik op het blokje dat de A van de AUB-methode is.", U, Z["2"], "Mijn argument is dat ..."),
    klik("Klik op het blokje dat niets toevoegt aan een goed argument.", U, Z["3"], "Dat is gewoon zo, is een bewering zonder uitleg of voorbeeld."),
    casus(TEKST, [
        keuze("In stap 1 van het stappenplan duid je per alinea een [[*kernzin|tussentitel|voetnoot]] aan.", "Zo zie je de rode draad."),
        tabel("Welk verband geeft dit signaalwoord aan?",
              [("'Toch' in alinea 2", "tegenstelling"), ("'Bovendien' in alinea 2", "opsomming"), ("'Kortom' in alinea 3", "besluit")],
              "Signaalwoorden tonen hoe de delen samenhangen.", ["tegenstelling", "opsomming", "besluit"]),
        mk("Welke zin is de stelling van de auteur?",
           ["geluk zit niet in het geld zelf", "veel mensen denken dat geld gelukkig maakt en dat is ook zo", "wie meer verdient, kan meer kopen en heeft minder zorgen", "rijke mensen vergelijken zich nooit met wie nog rijker is"],
           0, "De stelling staat hier in het besluit, na 'kortom'."),
        keuze("Je bedenkt: 'Maar wie arm is, heeft wel zorgen door geldgebrek.' Dat is een [[*tegenvoorbeeld|kernzin|signaalwoord]] dat in stap 3 hoort.", "In de reflectie zoek je tegenvoorbeelden."),
        keuze("De auteur had je bezwaar al voorzien: hij schrijft 'wie genoeg heeft om rustig te leven'. Je vraagt in stap 3 dus ook [[*hoe de auteur zou antwoorden|hoeveel woorden de tekst telt|wie de tekst drukte]].", "Zo toets je je eigen kritiek."),
    ]),
    volgorde("Zet de stappen van het stappenplan in de juiste volgorde.",
             ["globaal en oriënterend lezen", "grondig lezen en samenvatten", "reflectie: wat vind je er zelf van?"],
             "Eerst de grote lijn, dan de details, dan je eigen oordeel."),
    sorteer("In welke stap hoort dit?", ["stap 1", "stap 2", "stap 3"],
            [("per alinea een kernzin aanduiden", "stap 1"), ("een moeilijke zin ontleden", "stap 2"), ("een samenvatting in enkele zinnen schrijven", "stap 2"), ("kritiek formuleren", "stap 3"), ("letten op de indeling in alinea's", "stap 1"), ("je eigen overtuiging misschien bijstellen", "stap 3")],
            "Oriënterend lezen, grondig lezen, reflectie."),
    koppel("Koppel de zinaanzet aan de letter van de AUB-methode.",
           [("Mijn argument is dat ...", "A"), ("... omdat ...", "U"), ("Neem nu het geval van ...", "B")],
           ["Kortom ..."], "Argument, uitleg, bijvoorbeeld."),
    tabel("Klopt dit over de AUB-methode?",
          [("Ze zegt welk standpunt het juiste is.", F), ("Een zelfbedacht voorbeeld mag.", J), ("Ze werkt ook bij een ethisch vraagstuk.", J), ("Het voorbeeld moet altijd uit onderzoek komen.", F)],
          "Ze geeft de vorm, niet het standpunt."),
    mk("Een leerling schrijft: 'Mijn argument is dat huiswerk zinloos is.' Wat moet er nog bij?",
       ["een uitleg en een voorbeeld", "een tweede argument dat precies hetzelfde zegt", "een tegenargument dat zijn eigen argument weerlegt", "de naam van de leerkracht die het huiswerk gaf"],
       0, "Zonder U en B blijft het een bewering."),
    keuze("De U van de AUB-methode heeft twee stappen: eerst waarom het zo is, daarna waarom dat [[*goed of slecht is|waar of onwaar is|oud of nieuw is]].", "Zo wordt de uitleg volledig."),
    mk("Waarom is het slim om ook argumenten tegen je eigen standpunt te bedenken?",
       ["dan weet je wat je moet weerleggen", "dan verander je meteen van standpunt en kies je het andere", "dan lijkt je tekst langer en krijg je meer punten", "dan hoef je zelf geen argumenten meer te geven"],
       0, "Een standpunt dat de tegenargumenten niet kent, staat zwak."),
    sorteer("Filosofische vraag bij het thema sport, of niet?", ["filosofisch", "niet filosofisch"],
            [("Is winnen het belangrijkste in sport?", "filosofisch"), ("Hoeveel spelers telt een voetbalploeg?", "niet filosofisch"), ("Is doping altijd oneerlijk?", "filosofisch"), ("Welke sport kijk jij het liefst?", "niet filosofisch")],
            "De eerste vaardigheid: zelf een filosofische vraag stellen bij een thema."),
    tabel("Is dit een filosofische vaardigheid?",
          [("een filosofische vraag stellen", J), ("argumenteren met de AUB-methode", J), ("een filosofische tekst analyseren", J), ("een domein bepalen", F)],
          "Domeinen onderscheiden staat apart."),
    sleep("Bij stap 2 zoek je onbekende [[woorden]] op, [[ontleed]] je moeilijke zinnen en maak je op het einde een [[samenvatting]].",
          ["kernzin", "tegenvoorbeeld"], "Grondig lezen."),
    keuze("Je leest een tekst maar één keer. Volgens het stappenplan is dat [[*te weinig|genoeg|net goed]].", "Minstens twee keer: oriënterend en grondig."),
    inv("Welke letter van AUB staat voor de uitleg? Eén letter.", ["U", "u"], "Want of omdat."),
    tabel("Welke zinaanzet hoort bij de B?",
          [("Stel je voor ...", J), ("Het is onderzocht dat ...", J), ("Mijn argument is dat ...", F), ("Een voorbeeld hiervan is ...", J)],
          "Mijn argument is dat hoort bij de A."),
    mk("Waarom duid je in stap 2 ook de stelling en de argumenten aan?",
       ["om te zien hoe de auteur verdedigt", "om te tellen hoeveel argumenten er in de tekst staan", "om de moeilijke woorden in de tekst te vinden", "om de tekst daarna niet meer te moeten lezen"],
       0, "Je moet achteraf met eigen woorden kunnen uitleggen hoe de auteur zijn stelling verdedigt."),
    keuze("De filosofische vaardigheden pas je toe op [[*elk thema|enkel de ethiek|enkel kunst]], ook op lichaam en geest en op mens en dier.", "Vraag, argument en tekstanalyse."),
    keuze("Iemand zegt in een discussie: 'Dat is gewoon zo.' Volgens de AUB-methode ontbreken [[*de uitleg en het voorbeeld|enkel de titel|het signaalwoord kortom]].", "Hij beweert zonder te onderbouwen."),
    tabel("Hoort deze vraag bij stap 3, de reflectie?",
          [("Welke kritiek heb ik?", J), ("Welke tegenvoorbeelden vind ik?", J), ("Hoeveel alinea's telt de tekst?", F), ("Moet ik mijn overtuiging bijstellen?", J)],
          "In de reflectie denk je na over wat je zelf vindt."),
    inv("Hoeveel stappen heeft het stappenplan voor een filosofische tekst? Schrijf het getal.", ["3", "drie"], "Oriënterend lezen, grondig lezen, reflectie."),
    mk("Waarom zijn de beginletters A, U en B handig?",
       ["je onthoudt de volgorde makkelijk", "ze tonen welke kant van de discussie juist is", "ze zijn de namen van drie bekende filosofen", "ze geven aan hoeveel bladzijden je moet schrijven"],
       0, "Een geheugensteun voor argument, uitleg, bijvoorbeeld."),
    sorteer("A, U of B?", ["A", "U", "B"],
            [("Mijn argument is dat lezen je wijzer maakt.", "A"), ("Omdat je in boeken andere levens leert kennen.", "U"), ("Neem nu iemand die door een roman een vluchteling beter begrijpt.", "B")],
            "Argument, uitleg, bijvoorbeeld."),
    open_("Schrijf een argument volgens de AUB-methode bij de vraag: 'Moeten dieren in een zoo kunnen leven?'",
          "A: Mijn argument is dat een zoo bedreigde dieren kan redden. U: want sommige soorten bestaan in het wild bijna niet meer, en zo blijven ze bewaard. Dat is goed omdat een soort die uitsterft niet terugkomt. B: Een voorbeeld hiervan is een diersoort die in een zoo werd gekweekt en later weer werd uitgezet."),
]
