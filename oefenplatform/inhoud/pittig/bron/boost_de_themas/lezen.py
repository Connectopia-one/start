"""Een Duitse tekst lezen — pittig (🚀 Boost doorstroom, Duits).

Eigen teksten en vragen binnen de leerstof van boost-doorstroom/bron/de_lezen.py:
onderwerp, hoofdgedachte, hoofdpunten, gericht informatie zoeken en woorden
afleiden uit de context. Enkel schriftelijk."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus("Lies den Text.\n\nJugendzentrum \"Blauer Punkt\" – neue Öffnungszeiten\n\nAb dem 1. März ist das Jugendzentrum nicht mehr am Montag, sondern am Dienstag geschlossen. "
          "Von Mittwoch bis Freitag öffnen wir um 15 Uhr, am Samstag schon um 11 Uhr. Der Eintritt bleibt frei. "
          "Neu: Jeden ersten Freitag im Monat gibt es einen Kochabend. Wer mitkochen will, meldet sich bis Mittwoch an. "
          "Jugendliche unter 14 Jahren dürfen nur bis 19 Uhr bleiben.", [
        mk("Lena (13) will am Freitag zum Kochabend und bis 21 Uhr bleiben. Was stimmt?",
           ["Sie muss um 19 Uhr nach Hause, weil sie unter 14 ist.", "Sie darf bleiben, weil der Kochabend eine Ausnahme ist.", "Sie kann nicht kommen, weil freitags geschlossen ist.", "Sie muss Eintritt zahlen, weil es ein Kochabend ist."], 0,
           "Jongeren onder 14 mogen maar tot 19 uur blijven. Er staat nergens een uitzondering voor de kookavond."),
        tabel("Klopt dit over het jeugdhuis Blauer Punkt?",
              [("Op maandag is het jeugdhuis voortaan open.", J), ("Op zaterdag gaat het later open dan op woensdag.", F), ("Voor de kookavond schrijf je je in.", J), ("De toegang wordt betalend.", F)],
              "Nicht mehr am Montag, sondern am Dienstag geschlossen: maandag is nu open. Zaterdag opent om 11 uur, vroeger dan 15 uur. Der Eintritt bleibt frei: gratis."),
        keuze("De hoofdgedachte van de tekst: het jeugdhuis [[*heeft nieuwe openingsuren en een nieuwe activiteit|sluit binnenkort de deuren|zoekt nieuwe medewerkers]].",
              "De titel zegt het al: neue Öffnungszeiten. Daarnaast is de kookavond nieuw."),
    ]),
    casus("Lies die E-Mail.\n\nHallo Sam,\nwie geht's? Ich bin jetzt seit zwei Wochen in Freiburg. Die Schule ist größer als in Gent, aber die Lehrer sind sehr nett. "
          "Leider habe ich noch nicht viele Freunde. Am Wochenende gehe ich meistens mit meiner Gastfamilie wandern, das ist nicht so mein Ding. "
          "Nächste Woche beginnt aber ein Theaterkurs, und da mache ich mit! Schreib mir bald.\nLiebe Grüße\nJana", [
        mk("Hoe voelt Jana zich op dit moment het best samengevat?",
           ["Ze is tevreden over de school, maar mist nog vrienden.", "Ze wil zo snel mogelijk terug naar Gent.", "Ze vindt de leerkrachten streng en de school te groot.", "Ze heeft al veel vrienden dankzij de toneelles."], 0,
           "Die Lehrer sind sehr nett, maar Leider habe ich noch nicht viele Freunde. De toneelcursus begint pas volgende week."),
        inv("Wat betekent 'das ist nicht so mein Ding' hier? Vul aan: Jana vindt wandelen niet zo ...", ["leuk", "fijn", "plezant", "tof"],
            "Ze zegt het na meistens gehe ich wandern: het is niet echt iets voor haar."),
        keuze("Waarom kijkt Jana uit naar volgende week? Er begint dan [[*een cursus waaraan ze meedoet|een vakantie met haar gastgezin|een nieuw schooljaar]].",
              "Nächste Woche beginnt ein Theaterkurs, und da mache ich mit."),
    ]),
    sorteer("Hoofdzaak of bijzaak in een tekst over een schoolreis naar Berlijn met als hoofdgedachte 'de reis was leerrijk en leuk'?", ["hoofdpunt", "detail"],
            [("We hebben veel geleerd over de Muur.", "hoofdpunt"), ("De bus was blauw.", "detail"), ("Iedereen vond de reis geslaagd.", "hoofdpunt"), ("We vertrokken om 6.12 uur.", "detail"), ("Het museum was erg boeiend.", "hoofdpunt"), ("Mijn kamergenoot heette Ruben.", "detail")],
            "Een hoofdpunt ondersteunt de hoofdgedachte. Een kleur, een uur of een naam licht hoogstens iets toe."),
    volgorde("In welke volgorde lees je best een tekst als je een bepaalde informatie zoekt?",
             ["de titel en de foto bekijken", "de vraag lezen", "de juiste plaats in de tekst zoeken", "die plaats grondig lezen"],
             "Eerst voorspellen waarover het gaat, dan weten wat je zoekt, dan pas gericht zoeken en lezen."),
    koppel("Wat betekent het vetgedrukte woord? Leid het af uit de zin.",
           [("Ich bin müde, ich gehe ins Bett.", "moe"), ("Das Brot ist frisch, es kommt direkt vom Bäcker.", "vers"), ("Wir warten schon eine Stunde auf den Bus.", "wachten"), ("Der Film war so lustig, wir haben viel gelacht.", "grappig")],
           ["boos", "duur"], "Kijk wat er errond staat: naar bed gaan, recht van de bakker, al een uur, veel gelachen."),
    mk("In een advertentie staat: 'Fahrrad zu verkaufen, nur zwei Jahre alt, neue Reifen, 80 Euro. Anrufen nur abends.' Wanneer bel je best?",
       ["om acht uur 's avonds", "om tien uur 's morgens", "op zaterdagmiddag", "meteen na school om vier uur"], 0,
       "Nur abends: alleen 's avonds."),
    mk("'Nicht der Zug nach Köln, sondern der Zug nach Bonn hat Verspätung.' Welke trein is te laat?",
       ["de trein naar Bonn", "de trein naar Keulen", "allebei de treinen", "geen van beide treinen"], 0,
       "Nicht ..., sondern ...: niet het eerste, maar het tweede."),
    tabel("Is dit het onderwerp of de hoofdgedachte van de tekst 'Handys in der Schule'?",
          [("gsm's op school", "onderwerp"), ("Een gsm-verbod helpt leerlingen beter te concentreren.", "hoofdgedachte"), ("het gebruik van gsm's tijdens de les", "onderwerp")],
          "Het onderwerp zijn enkele woorden. De hoofdgedachte is een volledige zin met de boodschap.", kolommen=["onderwerp", "hoofdgedachte"]),
    sleep("Op een bordje staat 'Rauchen [[verboten]]': je mag hier niet roken. Op de deur van de winkel staat '[[geschlossen]]': je kan niet binnen.",
          ["geöffnet", "erlaubt"], "Verboten = verboden, geschlossen = gesloten. Geöffnet en erlaubt betekenen net het omgekeerde."),
    casus("Lies den Text.\n\nTipps für den Schulweg mit dem Fahrrad\n\nTrag immer einen Helm, auch wenn der Weg kurz ist. "
          "Im Winter ist es morgens noch dunkel: Mach das Licht an! Fahr nicht nebeneinander, sondern hintereinander. "
          "Und das Handy? Das bleibt in der Tasche, bis du angekommen bist.", [
        mk("Welke soort tekst is dit?",
           ["een tekst die zegt hoe je iets moet doen", "een verhaal over een ongeval", "een reclame voor een fietsenwinkel", "een krantenbericht over het verkeer"], 0,
           "Telkens een gebiedende wijs: trag, mach, fahr. Dat zijn tips: een prescriptieve tekst."),
        tabel("Mag dit volgens de tips?",
              [("Zonder helm fietsen als je dicht bij school woont.", F), ("Naast je vriend fietsen.", F), ("Je gsm gebruiken als je op school aangekomen bent.", J)],
              "Immer einen Helm, auch wenn der Weg kurz ist. Hintereinander, niet nebeneinander. Het handy blijft in de tas tot je aangekomen bent."),
    ]),
    inv("'Die Bibliothek bleibt wegen Bauarbeiten bis Ende Mai geschlossen.' Tot welke maand is de bibliotheek dicht? Schrijf de maand in het Nederlands.", ["mei", "eind mei"],
        "Bis Ende Mai: tot eind mei. Bauarbeiten zijn bouwwerken."),
    mk("Je leest: 'Das Konzert beginnt um 20 Uhr. Einlass ab 19.30 Uhr.' Wat betekent Einlass?",
       ["het moment dat je binnen mag", "het einde van het concert", "de prijs van een kaartje", "de pauze halverwege"], 0,
       "Ein-lassen: binnenlaten. De zaal gaat een halfuur voor het begin open."),
    open_("Lies: 'Viele Jugendliche schlafen zu wenig. Sie gehen spät ins Bett, weil sie lange am Handy sind. Am Morgen sind sie dann müde in der Schule.' Schrijf de hoofdgedachte in één Nederlandse zin.",
          "Veel jongeren slapen te weinig door hun gsm en zijn daardoor moe op school.",
          "Een hoofdgedachte is één volledige zin die de boodschap van de hele tekst samenvat."),
    koppel("Welke vraag hoort bij welk tekstje?",
           [("Wann fährt der Bus?", "Abfahrt: 7.45 Uhr"), ("Was kostet die Karte?", "Preis: 12 Euro"), ("Wo ist das Treffen?", "Treffpunkt: vor dem Rathaus"), ("Wer darf mitmachen?", "Für alle ab 12 Jahren")],
           ["Dauer: zwei Stunden"], "Wann vraagt naar een tijd, was kostet naar een prijs, wo naar een plaats, wer naar personen."),
    mk("'Ich habe meinen Schlüssel verloren. Jetzt kann ich nicht in die Wohnung.' Wat is er met de sleutel gebeurd?",
       ["Hij is kwijt.", "Hij is gebroken.", "Hij ligt in de woning.", "Hij is gestolen door een buur."], 0,
       "Verloren: kwijtgeraakt. Daarom kan de schrijver niet binnen."),
    keuze("'Am Wochenende arbeite ich in einem Café. Das Geld spare ich für eine Reise nach Spanien.' De schrijver [[*legt geld opzij|geeft alles meteen uit|krijgt zakgeld van zijn ouders]].",
          "Sparen betekent sparen, geld opzij leggen."),
    sorteer("Waar lees je deze zin?", ["in een station", "in een restaurant"],
            [("Gleis 4: Abfahrt in zwei Minuten", "in een station"), ("Die Speisekarte, bitte!", "in een restaurant"), ("Der Zug hat zehn Minuten Verspätung.", "in een station"), ("Das Tagesgericht kostet 9 Euro.", "in een restaurant")],
            "Gleis, Abfahrt, Zug en Verspätung horen bij de trein. Speisekarte en Tagesgericht bij het eten."),
    mk("'Der Kurs findet jeden zweiten Mittwoch statt.' Hoe vaak is de cursus?",
       ["om de twee weken op woensdag", "elke woensdag", "twee keer per week", "op de tweede woensdag van het jaar"], 0,
       "Jeden zweiten Mittwoch: elke tweede woensdag, dus om de veertien dagen."),
    casus("Lies den Text.\n\nDer Supermarkt \"Frischmarkt\" sucht Schüler für den Sommer. Du bist mindestens 16 Jahre alt und kannst im Juli oder im August vier Wochen arbeiten. "
          "Du hilfst beim Einräumen und an der Kasse. Wir zahlen 11 Euro pro Stunde. Schick uns eine kurze E-Mail mit deinem Namen, deinem Alter und wann du Zeit hast.", [
        tabel("Kan deze leerling solliciteren?",
              [("Tom is 15 en kan de hele zomer werken.", F), ("Sara is 17 en heeft in juli vier weken tijd.", J), ("Mehmet is 16 maar kan maar één week.", F)],
              "Je moet minstens 16 zijn én vier weken kunnen werken in juli of augustus."),
        mk("Wat moet er niet in je mail staan?",
           ["je rapportcijfers", "je leeftijd", "wanneer je tijd hebt", "je naam"], 0,
           "Gevraagd zijn naam, leeftijd en wanneer je tijd hebt. Over punten staat niets."),
        keuze("Het onderwerp van de tekst is [[*een vakantiejob in een supermarkt|de openingsuren van een supermarkt|een reclame voor verse groenten]].",
              "Der Supermarkt sucht Schüler für den Sommer: een zomerjob."),
    ]),
    mk("'Fast alle Schüler finden den neuen Schulhof toll. Nur die Älteren vermissen die alten Bänke.' Wie is minder tevreden?",
       ["de oudere leerlingen", "de jongste leerlingen", "alle leerlingen", "de leerkrachten"], 0,
       "Nur die Älteren vermissen die alten Bänke: alleen de ouderen missen de oude banken."),
    inv("'Wegen Schnee fällt der Unterricht morgen aus.' Wat gebeurt er morgen met de les? Vul aan: de les gaat niet ...", ["door"],
        "Ausfallen: niet doorgaan. Wegen Schnee: door de sneeuw."),
    keuze("'Die Wohnung ist hell, ruhig und liegt nah am Bahnhof. Leider gibt es keinen Aufzug.' Het nadeel is dat er [[*geen lift is|veel lawaai is|weinig licht binnenkomt]].",
          "Leider (helaas) kondigt het nadeel aan: kein Aufzug. Hell en ruhig zijn net voordelen."),
    sleep("Na een tegenstelling met [[aber]] volgt vaak het belangrijkste. Na een opsomming met [[zuerst]], dann en zum Schluss volgt een volgorde.",
          ["denn", "auch"], "Aber leidt een tegenstelling in, zuerst begint een rij stappen."),
]
