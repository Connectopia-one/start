"""Zijnsleer — pittig (🌍 Beyond doorstroom, kunstbeschouwing en filosofie).
Strikt binnen beyond/bron/kfb_zijnsleer.py: schijn en werkelijkheid, worden
en zijn bij Parmenides, Plato en Aristoteles; immanentie en transcendentie
bij Plato, Aristoteles en Kant; noodzakelijkheid (Spinoza), toeval (Hume,
Sartre), doelgerichtheid (Aristoteles, Hegel) en het existentialisme."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL

# Prent: drie schema's van de werkelijkheid ---------------------------------------------
DS = Prent("drie-werkelijkheden", "Drie schema's van de werkelijkheid",
           "A één grote, gesloten bol zonder delen, met daarbuiten vage, doorgestreepte pijlen van verandering; B twee lagen: bovenaan een heldere wereld met volmaakte vormen, onderaan schaduwen ervan, met een stippellijn ertussen; C een eikel met een pijl naar een eik, en de vorm zit in de boom zelf")
SCH = {}


def schema(letter, x):
    DS.rect(x, 70, 290, 470, "#fbfaf5", DONKER, 10, 3)
    DS.letter(x + 145, 590, letter)
    SCH[letter] = (x, 70, 290, 470)


schema("A", 30)
schema("B", 355)
schema("C", 680)
# A
DS.cirkel(175, 300, 95, "#dfe8d4", DONKER, 4)
for (x1, y1, x2, y2) in ((60, 140, 110, 170), (250, 150, 290, 120), (70, 470, 120, 430), (250, 450, 295, 480)):
    DS.pijl(x1, y1, x2, y2, GRIJS, 2)
    DS.lijn(x1 - 5, y2 + 2, x2 + 5, y1 - 2, ORANJE, 3)
# B
DS.rect(375, 95, 250, 170, "#fff8dc", DONKER, 8, 2)
DS.cirkel(440, 180, 32, GEEL, DONKER, 2)
DS.pad("M 520 215 L 560 145 L 600 215 Z", GEEL, DONKER, 2)
DS.lijn(370, 300, 630, 300, DONKER, 2, stippel=True)
DS.rect(375, 330, 250, 190, "#d9d4c4", DONKER, 8, 2)
DS.ellips(445, 440, 34, 12, "#8a8470", "#8a8470", 1)
DS.ellips(560, 440, 40, 10, "#8a8470", "#8a8470", 1)
# C
DS.ellips(740, 470, 18, 24, "#b5651d", DONKER, 2)
DS.pad("M 724 452 Q 740 436 756 452 Z", "#7a5a32", DONKER, 2)
DS.pijl(765, 450, 815, 380, DONKER, 3)
DS.rect(855, 330, 26, 190, "#8a6d4b", DONKER, 0, 2)
DS.cirkel(868, 250, 85, LICHTGROEN, DONKER, 3)
DS.cirkel(830, 290, 45, "#7fae6b", DONKER, 2)
DS.cirkel(905, 285, 48, "#7fae6b", DONKER, 2)


def sz(l):
    return [Prent.zone(*SCH[l])]


VRAGEN = [
    klik("Klik op het schema dat past bij Plato.", DS.bestand, sz("B"),
         "Bij Plato bestaat de ware werkelijkheid in een aparte wereld van ideeën. De zichtbare wereld is daar een schaduw van."),
    klik("Klik op het schema dat past bij Parmenides.", DS.bestand, sz("A"),
         "Voor Parmenides is het zijn één en onveranderlijk. Verandering is schijn: daarom zijn de pijlen doorgestreept."),
    klik("Klik op het schema dat past bij Aristoteles.", DS.bestand, sz("C"),
         "Voor Aristoteles zit de vorm in de dingen zelf. Worden is de overgang van mogelijkheid naar werkelijkheid."),
    met_prent(DS.bestand, keuze("Schema B toont een [[*transcendente|immanente]] visie: de ware werkelijkheid ligt buiten de dingen. Schema C toont een [[*immanente|transcendente]] visie.",
              "Plato plaatst de ideeën los van de dingen, Aristoteles legt de vorm in de dingen.")),
    sorteer("Welke denker past bij deze uitspraak?", ["Parmenides", "Plato", "Aristoteles", "Kant"], [
        ["Verandering is schijn, het zijn is één.", "Parmenides"],
        ["De zichtbare wereld is een afbeelding van de ideeënwereld.", "Plato"],
        ["Een eikel is in mogelijkheid een eik.", "Aristoteles"],
        ["We kennen enkel de verschijnselen, niet het ding op zich.", "Kant"],
        ["Het denken toont dat het zijn niet kan ontstaan of vergaan.", "Parmenides"],
        ["Ons verstand ordent de ervaring met ruimte, tijd en oorzaak.", "Kant"],
    ], "Vier denkers met vier antwoorden op de vraag wat werkelijk is."),
    koppel("Koppel het begrip aan de denker die het in dit thema vertegenwoordigt.", [
        ["noodzakelijkheid", "Spinoza"],
        ["toeval in oorzaak en gevolg", "Hume"],
        ["doelgerichtheid in de geschiedenis", "Hegel"],
        ["het ding op zich", "Kant"],
    ], ["Montesquieu"], "Montesquieu hoort bij de scheiding der machten, niet bij de zijnsleer."),
    tabel("Klopt dit over de zijnsleer?", [
        ("De zijnsleer of ontologie onderzoekt wat de werkelijkheid ten diepste is.", J),
        ("Transcendent betekent: binnen de wereld van de dingen zelf.", F),
        ("Voor Spinoza bestaat er echt toeval in de natuur.", F),
        ("Voor existentialisten heeft het leven niet vanzelf een vaste zin.", J),
    ], "Transcendent is wat erboven of erbuiten ligt. Voor Spinoza is toeval onwetendheid over de oorzaken."),
    casus(
        "Lotte ziet 's avonds op een verlaten weg iets wat op een hond lijkt. Bij nader inzien is het een struik in de wind. "
        "Ze vraagt zich af: 'Hoe weet ik ooit of wat ik zie, echt zo is?'",
        [
            mk("Welk begrippenpaar uit de zijnsleer speelt hier?",
               ["schijn en werkelijkheid", "worden en zijn", "noodzaak en doel", "individu en gemeenschap"], 0,
               "Wat Lotte waarnam, was niet hoe het echt was."),
            keuze("Parmenides zou zeggen dat de [[*zintuigen|rede|ideeën]] ons kunnen bedriegen. Kant zou zeggen dat we het [[*ding op zich|idee van de hond|zijn van Parmenides]] nooit rechtstreeks kennen.",
                  "Voor Parmenides leidt het denken, niet de waarneming, naar de waarheid. Kant trekt een grens aan wat we kunnen kennen."),
            tabel("Wie zegt dit?", [
                ("De echte hond bestaat in een eeuwige wereld van ideeën.", "Plato"),
                ("Ons verstand ordent alles wat we zien.", "Kant"),
                ("De zichtbare struik is maar een afbeelding van iets volmaakters.", "Plato"),
            ], "Plato zoekt de werkelijkheid in de ideeën, Kant in hoe ons verstand de ervaring vormt.",
               kolommen=["Plato", "Kant"]),
        ],
    ),
    mk("Een rups wordt een vlinder. Hoe zou Parmenides dat bekijken?",
       ["de verandering is schijn", "de rups verwerkelijkt haar mogelijkheid",
        "de vlinder is een schaduw van het idee vlinder", "het is puur toeval zonder enige oorzaak"], 0,
       "Voor Parmenides kan het zijn niet echt veranderen. Het tweede antwoord past bij Aristoteles, het derde bij Plato."),
    tabel("Hoort dit bij noodzakelijkheid, toeval of doelgerichtheid?", [
        ("Alles volgt uit God of de natuur, niets kon anders.", "noodzakelijkheid"),
        ("We zien enkel dat het ene op het andere volgt.", "toeval"),
        ("Elk ding streeft naar de verwerkelijking van zijn aard.", "doelgerichtheid"),
        ("Mijn bestaan heeft geen vooraf gegeven plan.", "toeval"),
        ("De geschiedenis gaat naar het besef van vrijheid.", "doelgerichtheid"),
    ], "Spinoza: noodzaak. Hume en Sartre: toeval. Aristoteles en Hegel: doelgerichtheid.",
       kolommen=["noodzakelijkheid", "toeval", "doelgerichtheid"]),
    keuze("Voor Spinoza is vrijheid [[*inzicht in de noodzaak|het ontbreken van oorzaken|kiezen zonder reden]]. Wie begrijpt waarom alles gebeurt, wordt minder gedreven door [[*angst en blinde emoties|de rede|kennis]].",
          "Vrijheid is voor Spinoza inzicht, niet het ontbreken van oorzaken."),
    mk("Waarom noemt men de noodzaak bij Hume eerder een gewoonte van onze geest?",
       ["de noodzakelijke band zien we nooit zelf", "Hume vond dat oorzaken niet bestaan",
        "Hume geloofde dat God elke oorzaak bepaalt", "de geest bepaalt wat er in de natuur gebeurt"], 0,
       "We zien dat vuur en warmte steeds samen gaan, maar de noodzaak zelf nemen we niet waar."),
    sleep("Voor Sartre gaat de [[existentie]] vooraf aan de essentie. Het bestaan van de mens is [[toevallig]] en heeft geen vooraf gegeven doel.",
          ["noodzakelijk", "transcendent"], "De mens moet zelf zin geven aan zijn bestaan."),
    mk("Camus vergelijkt de mens met Sisyphus, die eindeloos een steen de berg op rolt. Wat wil hij daarmee tonen?",
       ["het absurde: zin zoeken in een zwijgende wereld", "dat zwaar werk altijd beloond wordt door de goden",
        "dat alles in de wereld een vast doel heeft", "dat elke oorzaak noodzakelijk een gevolg heeft"], 0,
       "Het absurde is de botsing tussen de mens die naar zin zoekt en een wereld die zwijgt."),
    inv("Hoe heet de leer dat dingen gericht zijn op een doel?", ["teleologie", "doelgerichtheid"],
        "Telos is Grieks voor doel."),
    inv("Hoe heet bij Kant de werkelijkheid zoals ze in zichzelf is, die we niet kunnen kennen? Het ding op ...", ["zich"],
        "Wij kennen enkel de verschijnselen."),
    volgorde("Zet deze denkers in de juiste volgorde in de tijd.", [
        "Parmenides", "Plato", "Aristoteles", "Spinoza", "Hume", "Kant", "Hegel", "Sartre",
    ], "Van de Griekse oudheid via de 17de en 18de eeuw naar de 19de en 20ste eeuw."),
    tabel("Immanent of transcendent?", [
        ("de ideeën van Plato, los van de dingen", "transcendent"),
        ("de vorm in de dingen bij Aristoteles", "immanent"),
        ("wat bij Kant buiten elke mogelijke ervaring ligt", "transcendent"),
    ], "Immanent ligt binnen de wereld, transcendent erbuiten.",
       kolommen=["immanent", "transcendent"]),
    mk("Iemand zegt: 'Alles in mijn leven moest zo gebeuren, en wie alle oorzaken kent, begrijpt het.' Welke denker spreekt zo?",
       ["Spinoza", "Sartre", "Camus", "Aristoteles"], 0,
       "Dat is het idee van noodzakelijkheid."),
    mk("Iemand zegt: 'Er is geen plan voor mij. Ik besta toevallig en moet zelf kiezen wat ik ervan maak.' Bij welke denker past dit?",
       ["Sartre", "Spinoza", "Hegel", "Plato"], 0,
       "Toeval van het bestaan en eigen keuze zijn typisch voor het existentialisme van Sartre."),
    tabel("Klopt dit over Aristoteles en Hegel?", [
        ("Voor Aristoteles is het doel of telos de laatste oorzaak van een ding.", J),
        ("Hegel ziet de geschiedenis als een kring die zich eindeloos herhaalt.", F),
        ("Voor Hegel ontwikkelt de geest zich via tegenstellingen.", J),
    ], "Hegel ziet de geschiedenis als een proces met een richting: naar het bewustzijn van vrijheid."),
    keuze("Waarom zijn zijnsleer en kenleer verbonden? Als de zintuigen [[*kunnen misleiden|nooit misleiden|enkel kunst tonen]], moet je weten hoe je toch tot ware kennis komt.",
          "Wat is er, en hoe kunnen we dat weten: twee vragen die samenhangen."),
    mk("Welke uitspraak past bij het existentialisme?",
       ["de mens moet zelf betekenis geven", "alles in het leven ligt vast in de natuur",
        "de sterren bepalen wie je wordt", "wie niet nadenkt, is het gelukkigst"], 0,
       "Bij Sartre, Camus en De Beauvoir staan eigen keuze en verantwoordelijkheid centraal."),
    mk("Wat bedoelt Aristoteles met worden?",
       ["mogelijkheid die werkelijkheid wordt", "schijn die de zintuigen ons voorspiegelen",
        "het afglijden van ideeën naar schaduwen", "toeval zonder enige richting of oorzaak"], 0,
       "Worden is voor Aristoteles echt en begrijpelijk: wat in mogelijkheid is, wordt werkelijk."),
    tabel("Hoort dit bij worden of bij zijn?", [
        ("wat blijft en onveranderlijk is", "zijn"),
        ("verandering, groei en vergaan", "worden"),
        ("de eeuwige ideeën van Plato", "zijn"),
        ("de zichtbare wereld die voortdurend verandert", "worden"),
    ], "Worden staat voor verandering, zijn voor wat blijft.",
       kolommen=["worden", "zijn"]),
    keuze("Kant trekt een grens: wat buiten de mogelijke [[*ervaring|rede|kunst]] ligt, zoals God of de ziel, kunnen we niet [[*kennen|denken|geloven]].",
          "Kennis blijft voor Kant binnen de grenzen van de ervaring."),
    mk("Waarom past de grotallegorie bij het begrippenpaar schijn en werkelijkheid?",
       ["de schaduwen zijn schijn, het zonlicht is werkelijkheid", "de grot is de echte wereld en buiten is schijn",
        "de gevangenen zien de ideeën rechtstreeks op de wand", "het verhaal gaat vooral over toeval en noodzaak in de grot"], 0,
       "Wie de grot verlaat, ziet de dingen zelf in plaats van hun schaduw."),
    open_("Formuleer een filosofische vraag over de zijnsleer en geef een argument voor en tegen een antwoord.",
          "Vraag: bestaat er toeval, of moest alles zo gebeuren? Argument voor noodzaak: elke gebeurtenis heeft een oorzaak, en wie alle oorzaken kent, kan alles verklaren (Spinoza). Argument tegen: we zien nooit de noodzakelijke band zelf, enkel dat dingen op elkaar volgen (Hume). Ook ons eigen bestaan lijkt toevallig en zonder vooraf gegeven doel (Sartre)."),
]
