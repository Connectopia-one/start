# -*- coding: utf-8 -*-
"""Een Duitse tekst lezen: onderwerp, hoofdgedachte, hoofdpunten en informatie.

Uit de vakfiche Duits van de 2de graad doorstroom (richting moderne talen),
onderdeel "Lezen en luisteren". Alleen het lezen: luisteren vraagt geluid.
Lezen en luisteren tellen elk voor 30 % van het examen. Het ERK-niveau voor
lezen is A2: korte, eenvoudige teksten over het dagelijkse leven.

Elke leesvraag staat op een echt Duits tekstje.

Deel 1: onderwerp, hoofdgedachte en losse gegevens.
Deel 2: hoofdpunten, informatie selecteren en woorden afleiden uit de context.
"""
from de_hulp import M, W, I

FLOHMARKT = ("Jeden ersten Samstag im Monat gibt es auf dem Marktplatz in Aachen einen Flohmarkt. "
             "Dort kann man alte Kleidung, Bücher und Spielzeug kaufen. Die Sachen sind billig und man "
             "wirft weniger weg. Der Markt beginnt um 8 Uhr und endet um 14 Uhr.")
LENA = ("Hallo, ich heiße Lena und ich bin 15 Jahre alt. Ich wohne mit meiner Mutter und meinem "
        "kleinen Bruder in Köln. Mein Vater wohnt in Bonn. Ich besuche ihn jedes Wochenende. "
        "In meiner Freizeit spiele ich Volleyball und ich lese gern.")
SCHWIMMBAD = ("Das Hallenbad ist vom 1. bis 15. Juli geschlossen. Wir bauen eine neue Rutsche. "
              "Ab dem 16. Juli sind wir wieder für Sie da: montags bis freitags von 7 bis 21 Uhr, "
              "am Wochenende von 9 bis 18 Uhr. Kinder unter 6 Jahren schwimmen gratis.")
HANDY = ("Viele Schüler haben ihr Handy immer bei sich. An unserer Schule ist das Handy im Unterricht "
         "jetzt verboten. Die Lehrer sagen: Die Schüler sind ruhiger und lernen besser. Aber in der "
         "Pause dürfen sie es benutzen.")
REZEPT = ("Pfannkuchen für vier Personen: Du brauchst 250 Gramm Mehl, drei Eier, einen halben Liter "
          "Milch und eine Prise Salz. Zuerst mischst du Mehl und Milch. Dann gibst du die Eier dazu. "
          "Danach lässt du den Teig zehn Minuten stehen. Zum Schluss backst du die Pfannkuchen in einer heißen Pfanne.")
FERIEN = ("Letzten Sommer war ich mit meiner Familie zwei Wochen in Österreich. Wir haben in einem kleinen "
          "Hotel in den Bergen gewohnt. Jeden Tag sind wir gewandert. Das Wetter war meistens schön, nur "
          "am letzten Tag hat es geregnet. Nächstes Jahr wollen wir wieder hinfahren.")
ZUG = ("Achtung, eine Durchsage: Der ICE nach München fährt heute nicht von Gleis 4, sondern von Gleis 7 ab. "
       "Der Zug hat etwa 20 Minuten Verspätung. Wir bitten um Entschuldigung.")
FAHRRAD = ("Ich verkaufe mein Fahrrad. Es ist blau, drei Jahre alt und in gutem Zustand. Die Bremsen sind neu. "
           "Preis: 120 Euro. Bei Interesse ruf mich an: 0176 123 45 67. Bitte nur abends nach 18 Uhr!")

DEEL1 = [
    M(f"{FLOHMARKT}\n\nWaarover gaat de tekst?",
      ["een tweedehandsmarkt", "een nieuwe winkel in Aken", "een kledingwinkel met dure merken", "het weer in Aken"], 0,
      "Flohmarkt is een rommelmarkt: je koopt er tweedehandse spullen. Het onderwerp zeg je in een paar woorden."),
    M(f"{FLOHMARKT}\n\nWat is de hoofdgedachte?",
      ["op de rommelmarkt koop je goedkoop en gooi je minder weg", "de markt begint elke zaterdag al heel vroeg in de ochtend", "in Aken zijn er veel boekenwinkels", "speelgoed is altijd duur"], 0,
      "De hoofdgedachte is de belangrijkste boodschap in één zin: Die Sachen sind billig und man wirft weniger weg."),
    I(f"{FLOHMARKT}\n\nOm hoe laat eindigt de markt? Schrijf het uur als getal.", ["14", "14 uur", "14u", "14 Uhr"],
      "Der Markt ... endet um 14 Uhr. Enden betekent eindigen."),
    W(f"{FLOHMARKT}\n\nDe rommelmarkt is één keer per maand.", True,
      "Jeden ersten Samstag im Monat: elke eerste zaterdag van de maand."),
    M(f"{LENA}\n\nBij wie woont Lena?",
      ["bij haar moeder en haar broertje", "bij haar vader en zijn nieuwe vrouw in Bonn", "alleen", "bij haar grootouders"], 0,
      "Ich wohne mit meiner Mutter und meinem kleinen Bruder in Köln."),
    W(f"{LENA}\n\nLena ziet haar vader elk weekend.", True,
      "Ich besuche ihn jedes Wochenende. Ihn verwijst naar haar vader."),
    M(f"{LENA}\n\nWat doet Lena graag in haar vrije tijd? Duid alles aan wat klopt.",
      ["volleybal spelen", "zwemmen in het meer", "lezen", "voetballen met haar broer"], [0, 2],
      "In meiner Freizeit spiele ich Volleyball und ich lese gern. Gern achter het werkwoord: graag doen."),
    I(f"{LENA}\n\nHoe oud is Lena? Schrijf het getal.", ["15", "vijftien", "fünfzehn"],
      "Ich bin 15 Jahre alt. In het Duits zeg je fünfzehn."),
    M(f"{SCHWIMMBAD}\n\nWaarom is het zwembad gesloten?",
      ["er wordt een nieuwe glijbaan gebouwd", "het water in het bad is veel te koud geworden", "er zijn geen redders", "het is vakantie"], 0,
      "Wir bauen eine neue Rutsche. Eine Rutsche is een glijbaan."),
    W(f"{SCHWIMMBAD}\n\nIn het weekend gaat het zwembad later open dan op weekdagen.", True,
      "Montags bis freitags von 7 Uhr, am Wochenende von 9 Uhr."),
    M(f"{SCHWIMMBAD}\n\nWie mag gratis zwemmen?",
      ["kinderen jonger dan zes jaar", "alle kinderen tijdens de hele maand juli", "leerlingen met een kaart", "iedereen op zondag"], 0,
      "Kinder unter 6 Jahren schwimmen gratis. Unter betekent onder, dus jonger dan."),
    W(f"{SCHWIMMBAD}\n\nOp 16 juli is het zwembad nog gesloten.", False,
      "Geschlossen vom 1. bis 15. Juli. Ab dem 16. Juli sind wir wieder für Sie da."),
    M(f"{HANDY}\n\nWat is het onderwerp van de tekst?",
      ["een gsm-verbod op school", "een nieuwe gsm kopen", "leraren die te veel bellen", "een computerles"], 0,
      "Das Handy is de gsm. Het verbod in de les is het onderwerp."),
    M(f"{HANDY}\n\nWat zeggen de leraren? Duid alles aan wat klopt.",
      ["de leerlingen zijn rustiger", "de leerlingen zijn boos op de directie", "de leerlingen leren beter", "de pauze is te kort"], [0, 2],
      "Die Schüler sind ruhiger und lernen besser."),
    W(f"{HANDY}\n\nDe leerlingen mogen hun gsm nooit gebruiken op school.", False,
      "Aber in der Pause dürfen sie es benutzen. Aber leidt een tegenstelling in."),
    I(f"{HANDY}\n\nWelk Duits woord in de tekst betekent verboden?", ["verboten"],
      "Im Unterricht ist das Handy jetzt verboten. Verbieten, verbot, verboten."),
    M(f"{ZUG}\n\nWaar moet je de trein naar München nemen?",
      ["aan spoor 7", "aan spoor 4", "aan spoor 20", "er rijdt geen trein"], 0,
      "Nicht von Gleis 4, sondern von Gleis 7. Nicht ..., sondern ...: niet ..., maar ..."),
    M(f"{ZUG}\n\nWat betekent Verspätung?",
      ["vertraging", "vertrek", "kaartje", "aankomst"], 0,
      "Der Zug hat 20 Minuten Verspätung: de trein heeft twintig minuten vertraging. Spät betekent laat."),
    W(f"{ZUG}\n\nDe trein naar München rijdt vandaag niet.", False,
      "Hij vertrekt van een ander spoor en heeft vertraging, maar hij rijdt wel."),
    M(f"{ZUG}\n\nWelk soort tekst is dit?",
      ["een omroepbericht in een station", "een reclamefolder", "een persoonlijke brief aan een goede vriend", "een recept"], 0,
      "Achtung, eine Durchsage: een mededeling die je hoort in het station. Een informatieve tekst."),
]

DEEL2 = [
    M(f"{REZEPT}\n\nWat doe je eerst?",
      ["meel en melk mengen", "de eieren erbij doen", "het deeg laten rusten", "de pan heet maken"], 0,
      "Zuerst mischst du Mehl und Milch. Zuerst, dann, danach, zum Schluss: zo volg je de stappen."),
    M(f"{REZEPT}\n\nWelke ingrediënten heb je nodig? Duid alles aan wat klopt.",
      ["meel", "melk", "suiker", "eieren", "boter"], [0, 1, 3],
      "250 Gramm Mehl, drei Eier, einen halben Liter Milch und eine Prise Salz. Suiker en boter staan er niet in."),
    I(f"{REZEPT}\n\nHoeveel minuten moet het deeg rusten? Schrijf het getal.", ["10", "tien", "zehn"],
      "Danach lässt du den Teig zehn Minuten stehen."),
    W(f"{REZEPT}\n\nDe tekst legt uit hoe je iets moet doen.", True,
      "Een recept is een prescriptieve tekst: het zegt wat je moet doen, stap voor stap."),
    M(f"{REZEPT}\n\nWelk woord geeft de laatste stap aan?",
      ["zum Schluss", "zuerst", "dann", "danach"], 0,
      "Zum Schluss betekent tot slot. Zulke signaalwoorden helpen je de volgorde te volgen."),
    M(f"{FERIEN}\n\nWat klopt over de vakantie? Duid alles aan wat klopt.",
      ["ze logeerden in een klein hotel", "ze waren aan zee", "ze waren in de bergen", "ze waren drie weken weg"], [0, 2],
      "In einem kleinen Hotel in den Bergen, zwei Wochen lang. Niet aan zee en geen drie weken."),
    W(f"{FERIEN}\n\nHet heeft de hele vakantie geregend.", False,
      "Das Wetter war meistens schön, nur am letzten Tag hat es geregnet. Meistens is meestal."),
    M(f"{FERIEN}\n\nWat deed de familie elke dag?",
      ["wandelen", "zwemmen", "fietsen", "skiën"], 0,
      "Jeden Tag sind wir gewandert. Gewandert is het voltooid deelwoord van wandern."),
    M(f"{FERIEN}\n\nWat is het plan voor volgend jaar?",
      ["opnieuw naar daar gaan", "de hele zomer gewoon thuis blijven", "naar zee gaan", "met de trein reizen"], 0,
      "Nächstes Jahr wollen wir wieder hinfahren. Wieder betekent opnieuw."),
    W(f"{FERIEN}\n\nDe vakantie duurde twee weken.", True,
      "Zwei Wochen: twee weken. Eine Woche, zwei Wochen."),
    M(f"{FAHRRAD}\n\nWat voor tekst is dit?",
      ["een zoekertje om iets te verkopen", "een verslag van een fietstocht", "een reclame voor een fietsenwinkel", "een klacht over een fiets"], 0,
      "Ich verkaufe mein Fahrrad: een zoekertje. Een typisch voorbeeld van een tekst die informatie geeft en vraagt."),
    M(f"{FAHRRAD}\n\nWelke informatie staat in de tekst? Duid alles aan wat klopt.",
      ["de kleur van de fiets", "waar de fiets gekocht is", "de prijs", "het merk van de fiets", "wanneer je mag bellen"], [0, 2, 4],
      "Kleur (blau), prijs (120 Euro) en het uur (abends nach 18 Uhr) staan er. Waar hij gekocht is en het merk, niet."),
    W(f"{FAHRRAD}\n\nJe mag de verkoper 's morgens bellen.", False,
      "Bitte nur abends nach 18 Uhr: alleen 's avonds na zes uur."),
    I(f"{FAHRRAD}\n\nHoeveel jaar is de fiets? Schrijf het getal.", ["3", "drie", "drei"],
      "Es ist drei Jahre alt."),
    M(f"{FAHRRAD}\n\nWat betekent Bremsen?",
      ["remmen", "banden", "lichten", "pedalen"], 0,
      "Die Bremsen sind neu: de remmen zijn nieuw. Je kan het afleiden: een fiets in goede staat met nieuwe ..."),
    M("Je leest: Der Kühlschrank ist leer. Wir müssen einkaufen.\n\nWat betekent leer, als je let op de tweede zin?",
      ["leeg", "vol", "kapot", "koud"], 0,
      "Als je moet gaan winkelen, is de koelkast leeg. Zo leid je een woord af uit de context."),
    M("Je leest: Meine Oma ist krank. Sie muss im Bett bleiben und der Arzt kommt heute.\n\nWat betekent krank?",
      ["ziek", "oud", "boos", "moe"], 0,
      "In bed blijven en een dokter die komt: krank is ziek. Das Krankenhaus is het ziekenhuis."),
    W("Bij een leestekst zoek je best elk onbekend woord meteen op in het woordenboek.", False,
      "Bepaal eerst of het woord belangrijk is om de tekst te begrijpen. Vaak kan je het afleiden uit de context."),
    M("Een tekst heeft als titel: Fünf Tipps für einen gesunden Schlaf. Waar gaat de tekst waarschijnlijk over?",
      ["hoe je beter slaapt", "hoe je gezond kookt", "hoe je vijf talen leert", "hoe je sneller loopt"], 0,
      "Schlaf is slaap, gesund is gezond. De titel helpt je voorspellen waarover een tekst gaat."),
    M("Welke informatie is een hoofdpunt in een tekst over de voordelen van fietsen naar school?",
      ["fietsen is gezond", "de fiets van Tom is rood", "de school begint om 8.30 uur", "het regende gisteren"], 0,
      "Hoofdpunten ondersteunen de hoofdgedachte. Details zoals een kleur of een uur zijn bijzaken."),
]
