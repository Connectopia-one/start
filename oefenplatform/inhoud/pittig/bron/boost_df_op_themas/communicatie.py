"""Communiceren en actief luisteren — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_communicatie: verbale en non-verbale communicatie, de fasen
van een gesprek, praten met kinderen en ouderen, oppervlakkig, inhoudelijk en
actief luisteren, en de LSD-methode. Met een zelfgetekend gesprek."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW

GS = Prent("gesprek-woonzorgcentrum", "Stagiair Sara praat met mevrouw Peeters", "vijf tekstballonnen van een gesprek, letters A tot E")
BALLON = [("A", "Goedemiddag, mevrouw Peeters."),
          ("B", "Ik ben Sara, ik loop hier deze maand stage."),
          ("C", "Als ik het goed begrijp, mist u vooral uw tuin?"),
          ("D", "Hoe voelde u zich toen u hier pas aankwam?"),
          ("E", "Dank u voor het babbeltje. Tot morgen!")]
Z = {}
for i, (t, zin) in enumerate(BALLON):
    y = 70 + i * 108
    GS.rect(120, y, 760, 80, "#ffffff", BLAUW, 26, 3)
    GS.pad(f"M 150 {y + 80} L 135 {y + 100} L 180 {y + 80}", "#ffffff", BLAUW, 3)
    GS.letter(170, y + 40, t)
    GS.tekst(210, y + 48, zin, 22, "start")
    Z[t] = [Prent.zone(120, y, 760, 80)]
U = "gesprek-woonzorgcentrum.svg"

WILLEMS = ("Lees de situatie.\n\n"
           "Je loopt stage in een woonzorgcentrum. Meneer Willems (84) hoort slecht. Hij zit met gekruiste armen aan tafel en zegt: 'Het gaat wel.' "
           "Maar hij kijkt naar beneden en eet niets.")

VRAGEN = [
    klik("Bekijk het gesprek. Klik op de zin waarin Sara samenvat.", U, Z["C"], "Ze herhaalt in eigen woorden wat ze begrepen heeft."),
    klik("Klik op de zin waarin Sara doorvraagt met een gevoelsvraag.", U, Z["D"], "Een gevoelsvraag laat de ander zijn gevoel benoemen."),
    klik("Klik op de zin waarin Sara zichzelf voorstelt.", U, Z["B"], "Na het groeten volgt het voorstellen."),
    klik("Klik op de zin waarmee Sara afscheid neemt.", U, Z["E"], "Afscheid nemen sluit het gesprek netjes af."),
    sorteer("Oppervlakkig, inhoudelijk of actief luisteren?", ["oppervlakkig", "inhoudelijk", "actief"],
            [("Je hoort de klank, maar je bent met iets anders bezig.", "oppervlakkig"), ("Je volgt wat er gezegd wordt, maar je laat het niet merken.", "inhoudelijk"), ("Je knikt, vat samen en vraagt door.", "actief"), ("Je onthoudt wat de ander vertelt, zonder te reageren.", "inhoudelijk"), ("Je draait je naar de ander en vraagt: 'Hoe was dat voor jou?'", "actief"), ("Je zit met je gedachten bij je eigen plannen terwijl de ander vertelt.", "oppervlakkig")],
            "Bij actief luisteren merkt de ander dat je er echt bent."),
    sorteer("Open of gesloten vraag?", ["open", "gesloten"],
            [("Hoe was je dag?", "open"), ("Heb je goed geslapen?", "gesloten"), ("Wat vond je het leukst aan de uitstap?", "open"), ("Was het lekker?", "gesloten"), ("Hoe voelde je je toen?", "open")],
            "Op een gesloten vraag antwoord je met ja of nee."),
    casus(WILLEMS, [
        mk("Hoe spreek je meneer Willems het best aan?",
           ["je gaat voor hem zitten, kijkt hem aan en praat rustig en duidelijk", "je roept van achter hem heel luid zijn naam", "je praat snel, zodat je hem niet te lang stoort tijdens het eten aan tafel", "je fluistert, zodat de andere bewoners het niet horen"],
           0, "Zo kan hij meelezen op je lippen en voelt hij zich aangesproken."),
        keuze("Zijn woorden en zijn lichaamstaal [[*zeggen iets anders|zeggen precies hetzelfde]].", "'Het gaat wel', maar gekruiste armen, neerkijken en niet eten."),
        mk("Wat zeg je best?",
           ["'U zegt dat het gaat, maar u eet niets. Klopt dat?'", "'Fijn dat het goed gaat, smakelijk!'", "'Eet nu maar snel op, meneer, anders wordt het allemaal koud.'", "'Waarom doet u zo moeilijk vandaag?'"],
           0, "Als woorden en lichaamstaal niet samengaan, vraag je ernaar."),
        keuze("Een stilte na je vraag laat je best [[*even duren|meteen opvullen]].", "Een stilte geeft hem tijd om verder te denken en te spreken."),
    ]),
    volgorde("Zet de fasen van een gesprek in de juiste volgorde.",
             ["groeten", "jezelf voorstellen", "kennismaken", "het dagelijkse gesprek", "afscheid nemen"],
             "Groeten is meteen ook de eerste indruk."),
    volgorde("Zet de stappen van de LSD-methode in de juiste volgorde.",
             ["luisteren", "samenvatten", "doorvragen"],
             "Luisteren, Samenvatten, Doorvragen."),
    tabel("Hoort dit bij een actieve luisterhouding?",
          [("je draait je naar de ander", J), ("je kijkt op je gsm", F), ("je knikt af en toe", J), ("je kruist je armen en kijkt weg", F)],
          "Gekruiste armen lezen als afstand."),
    mk("Hoe praat je het best met een kleuter die verdrietig is?",
       ["je zakt door je knieën en gebruikt korte zinnen", "je blijft staan en legt het uitgebreid uit", "je praat heel snel om hem af te leiden", "je gebruikt moeilijke woorden zodat hij iets leert"],
       0, "Op ooghoogte, kort en duidelijk."),
    keuze("'Hoe voelde je je toen je dat hoorde?' is een [[*gevoelsvraag|gesloten vraag|samenvatting]].", "Ze peilt naar het gevoel."),
    inv("Waarvoor staat de S in de LSD-methode? Eén woord.", ["samenvatten", "het samenvatten"], "Samenvatten."),
    tabel("Verbaal of non-verbaal?",
          [("de woorden die je kiest", "verbaal"), ("je stemtoon", "non-verbaal"), ("je gezichtsuitdrukking", "non-verbaal"), ("een geschreven briefje", "verbaal"), ("de afstand tot de ander", "non-verbaal")],
          "Verbaal is wat je in woorden zegt of schrijft.", ["verbaal", "non-verbaal"]),
    keuze("'Hm', 'ja' en een knikje zijn [[*kleine aanmoedigingen|gesloten vragen|samenvattingen]].", "Ze laten merken dat je nog mee bent."),
    mk("Een kind zegt: 'Ik wil niet naar huis.' Welke reactie is doorvragen?",
       ["'Wat maakt dat je niet naar huis wil?'", "'Je moet wel, mama staat al te wachten.'", "'Oké, dan blijf je hier slapen.'", "'Dat zeggen alle kinderen, hoor.'"],
       0, "Een open vraag helpt om verder te komen."),
    sleep("Bij actief luisteren [[luister]] je met je houding en je ogen, [[vat]] je samen wat je hoorde en [[vraag]] je door met open vragen.",
          ["onderbreek", "oordeel"],
          "De LSD-methode."),
    keuze("Bij een slechthorende oudere laat je je [[*gezicht|rug|gsm]] goed zien.", "Zo kan hij meelezen op je lippen."),
    tabel("Klopt dit over communiceren?",
          [("Inhoudelijk luisteren betekent dat je toont dat je luistert.", F), ("Een open vraag levert meer uitleg op dan een gesloten vraag.", J), ("Oogcontact toont dat je aandacht hebt.", J), ("Afscheid nemen hoort niet bij een gesprek.", F)],
          "Tonen dat je luistert, is actief luisteren."),
    mk("Welke begroeting is het meest respectvol in een woonzorgcentrum?",
       ["'Goedemorgen, meneer Jansen,' terwijl je hem aankijkt", "'Hé, alles goed?' terwijl je voorbijloopt", "een knikje zonder iets te zeggen", "'Dag allemaal!' vanaf de deur van de grote zaal met iedereen"],
       0, "Groeten, aankijken en iemand bij naam noemen maakt het persoonlijk."),
    keuze("Na het voorstellen volgt in een gesprek het [[*kennismaken|afscheid nemen|groeten]].", "Je vraagt en vertelt om en om."),
    inv("Hoe noem je luisteren waarbij je de klank hoort, maar niet echt opneemt wat er gezegd wordt? Eén woord.", ["oppervlakkig", "oppervlakkig luisteren"], "Oppervlakkig luisteren."),
    mk("Een kind zegt dat alles goed gaat, maar het heeft tranen in de ogen. Wat vertelt je het meest?",
       ["de lichaamstaal", "de woorden", "geen van beide", "de kleur van zijn trui"],
       0, "Lichaamstaal zegt vaak meer dan woorden."),
    tabel("Past dit bij een gesprek met een jong kind?",
          [("op ooghoogte gaan zitten", J), ("korte, duidelijke zinnen", J), ("een lange uitleg met moeilijke woorden", F), ("het kind aankijken", J)],
          "Kort, duidelijk en op ooghoogte."),
    keuze("Samenvatten geeft de ander de kans om je [[*recht te zetten|te negeren|te onderbreken]].", "Zo ga je na of je het goed begreep."),
    keuze("Wie zijn armen kruist en wegkijkt, lijkt [[*afstand te houden|heel geïnteresseerd|actief te luisteren]].", "Lichaamstaal spreekt mee."),
    open_("Een tiener zegt: 'Ik heb echt geen zin meer in school.' Reageer met de LSD-methode: schrijf een samenvatting en een doorvraag.",
          "Samenvatting: 'Als ik je goed begrijp, ben je de school helemaal beu.' Doorvraag: 'Wat maakt het de laatste tijd zo zwaar?'"),
]
