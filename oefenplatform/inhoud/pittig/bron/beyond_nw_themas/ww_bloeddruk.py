"""Welzijnswetenschappen: bloeddruk en lymfestelsel — pittig
(🌍 Beyond doorstroom, natuurwetenschappen).

Eigen vragen en een eigen prent van een haarvat met weefsel en lymfevat:
bloeddruk meten en regelen, renine-angiotensine-aldosteron, hoge en lage
bloeddruk, weefselvocht, lymfe en lymfestelsel, oedeem.
"""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Een haarvat tussen de weefselcellen, met een lymfevaatje ---------------------------
HV = Prent("haarvat-weefsel", "Een haarvat tussen de weefselcellen", "een horizontaal haarvat van links (P, komt van een arteriool) naar rechts (R, gaat naar een venule), met Q in het midden; erboven weefselcellen; eronder een blind beginnend vaatje S")
HV.tekst(80, 330, "van het hart", 16)
HV.tekst(920, 330, "naar het hart", 16)
HV.rect(140, 290, 720, 70, "#f1e4df", DONKER, 35, 3)
for i in range(7):
    HV.cirkel(190 + i * 105, 180, 42, "#eef0e6", DONKER, 2)
HV.pad("M700 640 L700 490 L330 490 Q300 490 300 465 Q300 440 330 440 L725 440 Q750 440 750 465 L750 640", "#eef3f8", DONKER, 3)
for k, (x, y) in {"P": (200, 325), "Q": (500, 325), "R": (800, 325), "S": (520, 465)}.items():
    HV.letter(x, y, k)
ZV = {
    "P": [Prent.zone(140, 285, 200, 80)], "Q": [Prent.zone(400, 285, 200, 80)],
    "R": [Prent.zone(660, 285, 200, 80)], "S": [Prent.zone(290, 430, 470, 210)],
}

EIGEN = [
    klik("Klik op de plaats waar de bloeddruk plasma uit het haarvat perst.", HV.bestand, ZV["P"],
         "Aan het begin van het haarvat, de slagaderlijke kant, is de bloeddruk het hoogst. Daar ontstaat weefselvocht."),
    klik("Klik op de plaats waar het meeste weefselvocht terug het bloed in gaat.", HV.bestand, ZV["R"],
         "Aan het einde is de bloeddruk gezakt. De plasma-eiwitten trekken dan water terug in het bloed."),
    klik("Klik op het vaatje dat het overtollige weefselvocht afvoert.", HV.bestand, ZV["S"],
         "Een lymfecapillair begint blind tussen de cellen en neemt het overschot op. Daarin heet het lymfe."),
    met_prent(HV.bestand, tabel("Kijk naar het haarvat en het vaatje S. Klopt dit?", [
        ("In S zitten kleppen verderop, zodat de lymfe één kant op stroomt.", J),
        ("De bloeddruk is in R hoger dan in P.", F),
        ("De vloeistof in S komt via de borstbuis uiteindelijk terug in het bloed.", J),
    ], "De lymfe komt via de borstbuis in een grote ader onder het sleutelbeen.")),
    casus(
        "Bij Marc (58) meet de huisarts drie keer na elkaar 152/96 mmHg in rust. Marc "
        "eet graag zout, rookt en beweegt weinig. De arts schrijft een middel voor dat "
        "de vorming van angiotensine II remt.",
        [
            keuze("Marc heeft [[*hypertensie|hypotensie|een normale bloeddruk]].",
                  "Vanaf 140/90 mmHg in rust, bij herhaalde metingen, spreekt men van hypertensie."),
            keuze("De 96 mmHg hoort bij [[*de rustfase van het hart|het samentrekken van de kamers]].",
                  "De onderdruk of diastolische druk is de laagste druk, tijdens de rust van het hart."),
            mk("Waarom verlaagt het geneesmiddel zijn bloeddruk?",
               ["De bloedvaten vernauwen minder",
                "Zijn hart gaat sneller en krachtiger kloppen",
                "Zijn nieren houden meer zout en water vast in het bloed",
                "Zijn baroreceptoren melden een veel te lage druk aan de hersenen"], 0,
               "Angiotensine II doet de bloedvaten vernauwen en zet aan tot aldosteron. Minder ervan geeft dus een lagere druk."),
            tabel("Helpt dit Marc om zijn bloeddruk te verlagen?", [
                ("minder zout eten", J),
                ("stoppen met roken", J),
                ("meer bewegen", J),
                ("meer drop met zoethout eten", F),
            ], "Een gezonde levensstijl verlaagt de bloeddruk. Zoethout doet hem net stijgen."),
        ],
    ),
    volgorde("Zet het renine-angiotensine-aldosteronsysteem in de juiste volgorde.", [
        "de bloeddruk daalt en de nieren geven renine af",
        "renine zet angiotensinogeen om in angiotensine I",
        "angiotensine I wordt angiotensine II",
        "angiotensine II vernauwt bloedvaten en zet aan tot aldosteron",
        "de nieren houden meer zout en water vast",
    ], "Zo stijgt de bloeddruk weer."),
    tabel("De bloeddruk is te hoog. Wat doet het negatief feedbacksysteem?", [
        ("het hartritme daalt", J),
        ("de bloedvaten verwijden", J),
        ("de nieren geven meer renine af", F),
        ("het orthosympatisch zenuwstelsel wordt actiever", F),
    ], "Een negatief feedbacksysteem werkt de verandering tegen."),
    koppel("Koppel elk onderdeel aan zijn rol in de regeling van de bloeddruk.", [
        ["baroreceptoren", "meten de druk in de aorta en halsslagaders"],
        ["verlengde merg", "bevat het cardiovasculair centrum"],
        ["orthosympatisch zenuwstelsel", "versnelt het hart en vernauwt bloedvaten"],
        ["parasympatisch zenuwstelsel", "vertraagt het hart"],
    ], ["thymus"], "Receptor, centrum en effectoren vormen samen de regelkring."),
    sorteer("Doet dit de bloeddruk stijgen of dalen?", ["Stijgen", "Dalen"], [
        ["vasoconstrictie", "Stijgen"],
        ["vasodilatatie", "Dalen"],
        ["een groter slagvolume", "Stijgen"],
        ["veel bloedverlies", "Dalen"],
    ], "Smallere vaten en meer bloed per slag verhogen de druk."),
    mk("Iemand staat snel op uit bed en wordt even duizelig. Wat is de beste verklaring?",
       ["Even komt er te weinig bloed in de hersenen",
        "De bovendruk schiet plots ver boven de 140 mmHg uit",
        "De lymfe stroomt plots naar de hersenen terug",
        "De nieren maken op dat ogenblik te veel aldosteron"], 0,
       "Bij snel rechtstaan zakt het bloed even naar de benen. Bij een lage bloeddruk merk je dat het sterkst."),
    tabel("Hoe evolueert de bloeddruk op deze plaats?", [
        ("aorta", "hoog"),
        ("haarvaten", "middelmatig"),
        ("holle aders", "laag"),
    ], "De druk daalt van het hart weg door de weerstand van de bloedvaten.", kolommen=["hoog", "middelmatig", "laag"]),
    sleep("Overtollig weefselvocht in de lymfevaten heet [[lymfe]]. In de [[lymfeklieren]] wordt het gefilterd en ruimen lymfocyten ziektekiemen op.",
          ["plasma", "nierbekken"], "Lymfe lijkt op weefselvocht maar bevat lymfocyten."),
    koppel("Koppel elk orgaan aan zijn taak.", [
        ["thymus", "laat T-lymfocyten rijpen"],
        ["milt", "ruimt versleten rode bloedcellen op"],
        ["lymfeklier", "filtert de lymfe"],
        ["borstbuis", "brengt lymfe terug naar het bloed"],
    ], ["galblaas"], "Samen vormen ze het lymfestelsel."),
    mk("Waarom zwelt bij hongeroedeem de buik op?",
       ["Er is te weinig albumine om water terug te trekken",
        "De lymfevaten maken te veel lymfe aan uit het voedsel",
        "Het hart pompt te krachtig zodat er te veel plasma lekt",
        "De nieren scheiden plots geen enkel zout meer uit"], 0,
       "Zonder genoeg albumine blijft water in het weefsel achter."),
    tabel("Klopt dit over het lymfestelsel?", [
        ("Het lymfestelsel heeft een eigen pomp.", F),
        ("Bewegen helpt de lymfe vooruit.", J),
        ("Lymfevaten hebben kleppen.", J),
        ("Weefselvocht bevat evenveel grote eiwitten als plasma.", F),
    ], "Er is geen lymfepomp; spieren knijpen de vaten samen en kleppen houden de richting."),
    keuze("Na het wegnemen van lymfeklieren kan een arm opzwellen. Dat heet [[*lymfoedeem|hypertensie|agglutinatie]].",
          "Het vocht wordt niet goed afgevoerd. Lymfedrainage en steunkousen helpen."),
    inv("Iemand heeft een bovendruk van 150 mmHg en een onderdruk van 90 mmHg. Hoeveel mmHg is het verschil?",
        ["60", "60 mmHg"], "150 min 90. Dat verschil noemt men de polsdruk."),
    tabel("Is dit een mogelijk gevolg van langdurig te hoge bloeddruk?", [
        ("een beroerte", J),
        ("schade aan de nieren", J),
        ("een hartinfarct", J),
        ("bloedgroep veranderen", F),
    ], "Hoge druk beschadigt op termijn de wand van de bloedvaten."),
    met_prent(HV.bestand, keuze("Het vocht dat bij P naar buiten gaat, bevat [[*bijna geen grote eiwitten|evenveel eiwitten als het plasma|vooral rode bloedcellen]].",
              "Grote plasma-eiwitten en bloedcellen passeren de wand van het haarvat niet.")),
    mk("Waarom stijgt de bloeddruk als de nieren meer zout en water vasthouden?",
       ["Het bloedvolume wordt groter",
        "Het bloed wordt dunner en stroomt trager door de haarvaten",
        "Het aantal witte bloedcellen in het bloed stijgt sterk",
        "De lymfevaten trekken samen en duwen op de aders"], 0,
       "Meer volume in hetzelfde vatenstelsel geeft een hogere druk."),
    tabel("Werkt het orthosympatisch of het parasympatisch zenuwstelsel hier vooral?", [
        ("tijdens een sprint op de atletiekpiste", "orthosympatisch"),
        ("rustig liggen na het sporten", "parasympatisch"),
        ("schrikken van een harde knal", "orthosympatisch"),
    ], "Het orthosympatisch stelsel maakt klaar voor actie; het parasympatisch zorgt voor rust en herstel.",
       kolommen=["orthosympatisch", "parasympatisch"]),
    keuze("Aldosteron laat de nieren meer [[*zout en water|glucose en ureum|rode bloedcellen]] terugnemen.",
          "Zo wordt het bloedvolume groter en stijgt de druk."),
    sleep("Bij een [[negatief]] feedbacksysteem werkt de reactie de verandering tegen. Een te hoge druk wordt zo weer [[lager]].",
          ["positief", "hoger"], "Zo blijft de bloeddruk binnen grenzen."),
    tabel("Is dit een typisch symptoom van een te lage bloeddruk?", [
        ("duizelig worden bij snel rechtstaan", J),
        ("zwart voor de ogen zien", J),
        ("een rood hoofd met bonzende hoofdpijn bij rust", F),
    ], "Bij hypotensie krijgen de hersenen even te weinig bloed."),
    mk("Waarom raadt men bij lymfoedeem aan om te blijven bewegen?",
       ["Werkende spieren duwen de lymfe vooruit",
        "Bewegen verhoogt het aantal lymfeklieren in de arm",
        "Bewegen zet weefselvocht om in rode bloedcellen",
        "Bewegen laat de borstbuis harder pompen dan het hart"], 0,
       "Het lymfestelsel heeft geen eigen pomp."),
    inv("De bloeddruk in een haarvat is aan het begin 35 mmHg en aan het einde 15 mmHg. Hoeveel mmHg daalt de druk over het haarvat?",
        ["20", "20 mmHg"], "35 min 15. Door die daling kan aan het einde water terug het bloed in."),
    open_("Leg uit hoe weefselvocht ontstaat en waar het naartoe gaat.",
          "Aan het begin van een haarvat perst de bloeddruk plasma zonder grote eiwitten naar buiten: weefselvocht. Aan het einde is de druk lager en trekken de eiwitten in het bloed het meeste water terug. Het overschot gaat in de lymfevaten, wordt in lymfeklieren gefilterd en komt via de borstbuis terug in het bloed."),
]

VRAGEN = EIGEN
