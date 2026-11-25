"""Waarnemen en observeren — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_observeren: waarnemen en observeren, wat het waarnemen
beïnvloedt, de valkuilen, de criteria van een goede observatie, de
observatiemethoden en de registratie. Met een zelfgetekend observatieverslag."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL

OV = Prent("observatieverslag-tim", "Observatieverslag, dinsdag, les wiskunde", "een blad met vijf zinnen over een leerling, letters A tot E")
OV.rect(60, 60, 880, 540, "#ffffff", DONKER, 8, 3)
OV.rect(60, 60, 880, 50, GEEL, DONKER, 8, 3)
OV.tekst(90, 93, "Leerling: Tim (11)  ·  Waarnemer: stagiair", 19, "start")
ZINNEN = [("A", "Om 10.15 uur duwt Tim zijn stoel achteruit en gaat bij het raam staan."),
          ("B", "Tim is vandaag weer eens lui."),
          ("C", "Hij zegt twee keer: 'Ik snap het niet.'"),
          ("D", "Zoals altijd verpest Tim de les voor iedereen."),
          ("E", "Na vijf minuten gaat hij terug zitten en neemt hij zijn pen.")]
Z = {}
for i, (t, zin) in enumerate(ZINNEN):
    y = 175 + i * 88
    OV.letter(110, y - 7, t)
    OV.tekst(150, y, zin, 21, "start")
    Z[t] = [Prent.zone(85, y - 42, 840, 70)]
U = "observatieverslag-tim.svg"

STAGE = ("Lees de situatie.\n\n"
         "Stagiair Ruben moet observeren hoe Mila (5) samenspeelt. Hij zit in de klas tussen de kinderen en bouwt mee met blokken. "
         "Mila weet niet dat ze geobserveerd wordt. Ruben duidt op een lijst aan hoe vaak ze iets deelt, iets afpakt of om hulp vraagt. "
         "Hij doet dat drie weken lang, op verschillende dagen.")

VRAGEN = [
    klik("Bekijk het verslag. Klik op alle zinnen die niet objectief zijn.", U, Z["B"] + Z["D"], "'Lui' en 'verpest de les' zijn oordelen, geen gedrag dat je ziet."),
    klik("Klik op de zin met een veralgemening.", U, Z["D"], "'Zoals altijd' en 'voor iedereen' trekken één moment door naar alles."),
    klik("Klik op de zin die letterlijk weergeeft wat Tim zegt.", U, Z["C"], "Letterlijke woorden zijn feiten die een collega kan nakijken."),
    tabel("Is dit een psychologische factor bij het waarnemen?",
          [("aandacht", J), ("voorkennis", J), ("de drempelwaarde van je oor", F), ("je emoties", J), ("gewenning aan een geur", F)],
          "Drempelwaarde en gewenning hebben met de zintuigen te maken."),
    sorteer("Welke valkuil is dit?", ["attributiefout", "verwachtingspatroon", "veralgemening"],
            [("Je vindt Sam een lastpost en ziet enkel zijn drukke momenten.", "verwachtingspatroon"), ("Een kind valt in slaap in de klas. Je denkt meteen dat het lui is, terwijl het thuis 's nachts niet kan slapen.", "attributiefout"), ("Eén kind van de groep liegt, dus je besluit dat de hele groep niet te vertrouwen is.", "veralgemening"), ("Je verwacht dat de nieuwe leerling verlegen is en ziet niet dat hij met iedereen praat.", "verwachtingspatroon"), ("Lotte komt te laat. Je denkt dat ze slordig is, maar de bus had panne.", "attributiefout")],
            "Je ziet wat je verwacht, je legt de oorzaak verkeerd, of je besluit over iedereen."),
    casus(STAGE, [
        keuze("Ruben bouwt mee: hij observeert [[*participerend|niet-participerend]].", "Hij neemt deel aan de activiteit."),
        keuze("Mila weet het niet: het is een [[*bedekte|niet-bedekte]] observatie.", "Ze weet niet dat ze bekeken wordt."),
        keuze("Ruben werkt met een [[*observatieschema|observatieverslag]].", "Een lijst met vooraf bepaalde punten om aan te duiden."),
        keuze("Het is een [[*gesloten|open]] observatie.", "Hij weet vooraf waarop hij let."),
        mk("Waarom observeert Ruben drie weken op verschillende dagen?",
           ["zo is het beeld representatief", "omdat één dag observeren verboden is", "omdat Mila elke dag een ander kind is", "zodat hij zelf meer kan spelen"],
           0, "Eén uitzonderlijke dag geeft geen beeld van hoe een kind meestal is."),
        keuze("Ruben observeert in de klas, waar Mila elke dag is. Dat is een [[*natuurlijke|kunstmatige]] observatieomgeving.", "De gewone omgeving van het kind."),
    ]),
    tabel("Is dit een criterium voor een goede observatie?",
          [("objectief", J), ("verrassend", F), ("doelgericht", J), ("opnieuw uitvoerbaar", J), ("zo kort mogelijk", F)],
          "Doelgericht, objectief, nauwkeurig, opnieuw uitvoerbaar en representatief."),
    mk("Welke notitie is objectief?",
       ["Jonas gooit zijn boek op de grond en zegt: 'Stom!'", "Jonas is een agressief kind dat nooit naar iemand luistert", "Jonas had duidelijk weer een slechte bui", "Jonas wilde de juf vandaag expres pesten"],
       0, "Je beschrijft gedrag en woorden, geen oordeel of bedoeling."),
    keuze("Waarnemen gebeurt [[*vanzelf|altijd met een doel|enkel met een schema]]; observeren doe je doelgericht.", "Je zintuigen brengen informatie binnen zonder dat je er iets voor doet."),
    keuze("Je ruikt de soep in de keuken na een tijdje niet meer. Dat is [[*gewenning|contrast|een attributiefout]].", "Een prikkel die blijft duren, valt na een tijd niet meer op."),
    keuze("Een kind met een felrode jas valt meteen op tussen kinderen in donkere jassen. Dat komt door [[*contrast|gewenning|een veralgemening]].", "Een groot verschil valt beter op."),
    inv("Hoe noem je de kleinste sterkte waarbij een zintuig een prikkel opmerkt? Eén woord.", ["drempelwaarde", "de drempelwaarde"], "De drempelwaarde."),
    tabel("Open of gesloten observatie?",
          [("Je noteert alles wat je opvalt tijdens het onthaal.", "open"), ("Je telt hoe vaak een kind de vinger opsteekt.", "gesloten"), ("Je duidt op een lijst aan of een kind zelf zijn jas aantrekt.", "gesloten"), ("Je schrijft op wat er gebeurt op de speelplaats, zonder vooraf iets te kiezen.", "open")],
          "Gesloten: vooraf afgebakend. Open: alles wat opvalt.", ["open", "gesloten"]),
    mk("Wanneer kies je een observatieverslag in plaats van een schema?",
       ["als je in woorden wil beschrijven wat je zag en hoorde", "als je enkel wil turven hoe vaak iets gebeurt op een vaste lijst", "als je de observatie niet wil laten nakijken", "als je geen doel hebt en niets noteert"],
       0, "Een verslag is een tekst met je bevindingen."),
    keuze("Je opvoeding, je cultuur en je ervaringen vormen samen je [[*referentiekader|drempelwaarde|observatieschema]].", "Je eigen bril op de wereld."),
    mk("Je bent moe en geïrriteerd tijdens een observatie. Wat doe je best?",
       ["je beseft dat je emoties je blik kleuren en blijft bij feiten", "je schrijft vooral op hoe jij je voelt", "je besluit dat het kind de schuld is van je slechte bui", "je observeert die dag enkel de kinderen die je zelf sympathiek vindt"],
       0, "Emoties sturen je aandacht; feiten noteren beperkt dat."),
    tabel("Klopt dit over observeren?",
          [("Bij een niet-bedekte observatie kan het gedrag veranderen omdat de persoon het weet.", J), ("Een goede observatie moet een collega kunnen nakijken.", J), ("Eén uitzonderlijke dag geeft een representatief beeld.", F), ("Participerend observeren betekent van ver toekijken.", F)],
          "Participerend is meedoen."),
    sleep("Een goede observatie is [[doelgericht]], [[objectief]] en [[representatief]]: je weet waarom je kijkt, je noteert feiten en je kijkt op gewone momenten.",
          ["verrassend", "gekleurd"],
          "Ook nauwkeurig en opnieuw uitvoerbaar horen erbij."),
    mk("Waarom observeer je liefst in de natuurlijke omgeving van een kind?",
       ["het kind gedraagt zich daar zoals altijd", "het is daar altijd stil en rustig", "je hoeft daar nooit vooraf een doel te kiezen", "het kind weet daar niet wie je bent"],
       0, "In de klas, de leefgroep of thuis zie je het gewone gedrag."),
    inv("Hoe noem je de fout waarbij je gedrag aan de persoon toeschrijft, terwijl de situatie de oorzaak is? Eén woord.", ["attributiefout", "een attributiefout", "de attributiefout"], "Een attributiefout."),
    keuze("Bij een [[*niet-bedekte|bedekte]] observatie weet de persoon dat hij bekeken wordt.", "Hij is op de hoogte."),
    tabel("Feit of interpretatie?",
          [("Hij zucht drie keer.", "feit"), ("Hij heeft geen zin in de les.", "interpretatie"), ("Ze huilt na het telefoontje.", "feit"), ("Ze is jaloers op haar zus.", "interpretatie")],
          "Een feit zie of hoor je; een interpretatie is wat jij ervan denkt.", ["feit", "interpretatie"]),
    keuze("Wie een observatie later op dezelfde manier kan herhalen, maakt ze [[*opnieuw uitvoerbaar|subjectief|bedekt]].", "Een collega kan ze dan overdoen."),
    keuze("Je let vooral op wat jou interesseert. Dat komt door je [[*aandacht|drempelwaarde|gewenning]].", "Aandacht is een psychologische factor."),
    open_("Herschrijf deze notitie zo dat ze objectief is: 'Lina is weer eens verlegen en wil niet meedoen.'",
          "Lina blijft tijdens het kringgesprek op haar stoel zitten, kijkt naar de grond en zegt niets als de juf haar iets vraagt."),
]
