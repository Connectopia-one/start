"""De socio-emotionele ontwikkeling — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_socio_emotioneel: de soorten spel, vriendschappen, de
peergroep en groepsdruk, gehechtheid, scheidingsangst, angst voor vreemden
en sensitieve responsiviteit. Met een zelfgetekende speelhoek."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, BLAUW, ORANJE, ROOD, GEEL, LICHTGROEN, PAARS

SH = Prent("speelhoek", "In de speelhoek", "vier plekken in een speelhoek met kinderen die spelen, letters A tot D")
HUID = "#f3dcc2"


def kind(p, x, y, kleur):
    p.cirkel(x, y, 22, HUID, DONKER, 2)
    p.rect(x - 22, y + 22, 44, 60, kleur, DONKER, 10, 2)


def toren(p, x, y, n, kleur):
    for i in range(n):
        p.rect(x, y - (i + 1) * 26, 40, 26, kleur, DONKER, 2, 2)


for x in (40, 520):
    for y in (70, 345):
        SH.rect(x, y, 440, 255, "#ffffff", GRIJS, 16, 2)
# A: één kind alleen met een toren
kind(SH, 170, 150, BLAUW); toren(SH, 260, 260, 4, GEEL)
# B: twee kinderen naast elkaar, elk een eigen toren
kind(SH, 600, 150, ORANJE); toren(SH, 650, 260, 3, ROOD)
kind(SH, 800, 150, PAARS); toren(SH, 850, 260, 3, LICHTGROEN)
SH.lijn(745, 90, 745, 300, GRIJS, 2, True)
# C: een kind kijkt naar twee spelende kinderen
kind(SH, 110, 430, LICHTGROEN)
SH.cirkel(103, 425, 3, DONKER, DONKER, 1); SH.cirkel(117, 425, 3, DONKER, DONKER, 1)
SH.pijl(140, 440, 230, 450, GRIJS, 2)
kind(SH, 290, 430, BLAUW); kind(SH, 390, 430, ORANJE)
SH.cirkel(340, 545, 22, ROOD, DONKER, 2)
# D: twee kinderen bouwen samen één groot kasteel
kind(SH, 590, 430, GEEL); kind(SH, 860, 430, PAARS)
for i, h in enumerate((3, 4, 5, 4, 3)):
    toren(SH, 630 + i * 40, 560, h, GRIJS)
LET = {"A": (70, 100), "B": (550, 100), "C": (70, 375), "D": (550, 375)}
for t, (x, y) in LET.items():
    SH.letter(x, y, t)
Z = {t: [Prent.zone(x - 30, y - 30, 440, 255)] for t, (x, y) in LET.items()}
U = "speelhoek.svg"

OPVANG = ("Lees de situatie.\n\n"
          "In de kinderopvang komen drie ouders hun kind van twee ophalen. Emma loopt meteen naar haar mama, krijgt een knuffel en speelt daarna rustig verder. "
          "Liam kijkt even op, maar speelt gewoon door en negeert zijn papa. Noor huilt, klampt zich vast aan haar mama en duwt haar tegelijk weg.")

VRAGEN = [
    klik("Bekijk de speelhoek. Klik op de plek met solospel.", U, Z["A"], "Eén kind speelt op zichzelf, zonder de anderen nodig te hebben."),
    klik("Klik op de plek met parallel spel.", U, Z["B"], "Naast elkaar, maar elk aan een eigen toren."),
    klik("Klik op de plek met toekijkend spel.", U, Z["C"], "Het kind kijkt hoe anderen spelen en doet zelf nog niet mee."),
    klik("Klik op de plek met coöperatief spel.", U, Z["D"], "Samen aan één kasteel: één doel."),
    sorteer("Directe of indirecte groepsdruk?", ["direct", "indirect"],
            [("'Kom op, neem er ook eentje, anders ben je een watje.'", "direct"), ("Iedereen in de klas draagt dezelfde sneakers, en jij wil ze ook.", "indirect"), ("Je vrienden zeggen: 'Doe mee met de sponsorloop!'", "direct"), ("Niemand in je groep zegt iets, maar ze roken allemaal.", "indirect")],
            "Direct is wat de groep zegt, indirect is wat je voelt dat de groep verwacht."),
    sorteer("Positieve of negatieve groepsdruk?", ["positief", "negatief"],
            [("Je ploeg studeert samen voor de examens, en jij doet mee.", "positief"), ("Je vrienden dagen je uit om iets te stelen in een winkel.", "negatief"), ("Iedereen in je groep fietst naar school, dus jij ook.", "positief"), ("De groep lacht een klasgenoot uit, en jij lacht mee.", "negatief")],
            "De groep kan je ook meetrekken in iets goeds."),
    casus(OPVANG, [
        tabel("Welk hechtingspatroon past het best?",
              [("Emma", "veilig"), ("Liam", "angstig-vermijdend"), ("Noor", "angstig-ambivalent")],
              "Troost zoeken, geen troost zoeken, of troost zoeken en wegduwen.", ["veilig", "angstig-vermijdend", "angstig-ambivalent"]),
        mk("Waarom durft Emma daarna rustig verder te spelen?",
           ["haar mama is een veilige basis", "ze houdt niet echt van haar mama", "ze is nog te jong om iets te voelen", "ze is bang voor de begeleiders"],
           0, "Wie weet dat zijn ouder er is, durft op verkenning."),
        keuze("Liam lijkt onverschillig, maar [[*heeft wellicht wel troost nodig|heeft nooit troost nodig|is net het best gehecht]].", "Een angstig-vermijdend kind vraagt geen hulp, ook al heeft het die nodig."),
    ]),
    koppel("Koppel het soort spel aan het voorbeeld.",
           [("doen-alsof-spel", "een kleuter maakt van de zetel een boot"), ("samenspel met regels", "kinderen van tien spelen tikkertje met afspraken"), ("solospel", "een baby speelt met zijn eigen tenen")],
           ["een volwassene leest de krant"],
           "Vanaf de lagere school worden regels heel belangrijk."),
    tabel("Klopt dit over gehechtheid?",
          [("Scheidingsangst rond één jaar is normaal.", J), ("Een veilig gehecht kind huilt nooit.", F), ("Angst voor vreemden begint meestal rond acht maanden.", J), ("Gehechtheid groeit met wie dagelijks voor de baby zorgt.", J), ("Sensitieve responsiviteit betekent een baby lang laten huilen.", F)],
          "Een veilig gehecht kind huilt wel, maar zoekt dan troost."),
    volgorde("Zet de stappen van sensitieve responsiviteit in de juiste volgorde.",
             ["de signalen van de baby opmerken", "ze juist begrijpen", "er snel en passend op ingaan"],
             "Zien, begrijpen, reageren."),
    mk("Een baby huilt. Welke reactie is sensitief responsief?",
       ["kijken wat hij nodig heeft en hem dat snel geven", "hem laten huilen tot hij vanzelf stopt", "de radio luider zetten zodat je hem niet hoort", "wachten tot het volgende vaste voedingsuur op het schema"],
       0, "Zo bouwt een baby vertrouwen en een veilige hechting op."),
    keuze("Een baby van negen maanden huilt als een onbekende tante hem vastneemt. Dat is [[*angst voor vreemden|scheidingsangst|angstig-vermijdend gedrag]].", "Hij maakt onderscheid tussen vertrouwde en onbekende gezichten."),
    keuze("Een peuter huilt hard als zijn papa vertrekt aan de poort van de opvang. Dat is [[*scheidingsangst|angst voor vreemden|groepsdruk]].", "Het kind mist iemand in het bijzonder."),
    tabel("Welk soort spel past het best bij deze leeftijd?",
          [("een baby", "solospel"), ("een kleuter", "doen-alsof-spel"), ("een kind van tien", "samenspel met regels")],
          "Samenspelen leert een kind pas later.", ["solospel", "doen-alsof-spel", "samenspel met regels"]),
    mk("Twee vriendinnen hebben ruzie en maken het de volgende dag weer goed. Waarom is dat waardevol?",
       ["ze leren conflicten oplossen en goedmaken", "ze leren dat ruzie altijd slecht afloopt", "ze leren dat vriendschappen niet belangrijk zijn", "ze leren dat je beter alleen speelt"],
       0, "Ruzie maken én goedmaken horen bij de sociale ontwikkeling."),
    inv("Hoe noem je spel waarbij kinderen rollen verdelen en samen naar één doel werken? Eén woord.", ["coöperatief", "cooperatief", "coöperatief spel", "cooperatief spel"], "Coöperatief spel."),
    keuze("In de adolescentie krijgt de [[*peergroep|kinderopvang|babytijd]] een grote invloed op kleding, taal en keuzes.", "De leeftijdsgenoten worden de grote spiegel."),
    mk("Een nieuwe leerling begint te lopen omdat iedereen in zijn klas na school gaat joggen. Wat is dat?",
       ["positieve, indirecte groepsdruk", "negatieve, directe groepsdruk", "een angstig-vermijdende hechting", "scheidingsangst bij een tiener"],
       0, "Niemand zegt het, maar de groep trekt hem mee in iets gezonds."),
    sleep("Bij [[parallel]] spel spelen kinderen naast elkaar, elk met hun eigen ding. Bij [[solitair]] spel speelt een kind alleen. Bij [[coöperatief]] spel werken ze samen aan één doel.",
          ["magisch", "moreel"],
          "Solitair spel heet ook solospel."),
    tabel("Is dit een teken van een veilige hechting?",
          [("het kind durft op verkenning", J), ("het kind zoekt troost als het bang is", J), ("het kind duwt zijn ouder weg terwijl het huilt", F), ("het kind negeert zijn ouder altijd", F)],
          "Wegduwen en negeren passen bij de angstige patronen."),
    keuze("Het gedesorganiseerde patroon is een vorm van [[*gehechtheid|groepsdruk|spel]].", "Naast veilig, angstig-vermijdend en angstig-ambivalent."),
    inv("Hoe noem je spel waarbij een kind kijkt hoe anderen spelen, zonder zelf mee te doen? Eén woord.", ["toekijkend", "toekijkend spel", "het toekijkend spel"], "Toekijkend spel."),
    mk("Waarom zijn angst voor vreemden en scheidingsangst eigenlijk goed nieuws?",
       ["het kind weet wie zijn vertrouwde mensen zijn", "het kind zal later nooit meer bang zijn", "het kind is dan klaar om alleen te wonen", "het kind heeft vanaf dan geen ouders meer nodig"],
       0, "Ze tonen dat er een band is."),
    tabel("Is dit groepsdruk?",
          [("een vriend die zegt 'doe nu toch mee'", J), ("iedereen draagt hetzelfde merk en jij voelt dat je moet volgen", J), ("je kiest in de bib zelf een boek, zonder dat iemand iets zegt", F), ("klasgenoten die je aanmoedigen om te studeren", J)],
          "Groepsdruk kan direct of indirect, positief of negatief zijn."),
    keuze("Een begeleider merkt dat een baby moe wordt en legt hem rustig in bed. Dat is [[*sensitieve responsiviteit|groepsdruk|centratie]].", "Signalen zien, begrijpen en erop ingaan."),
    mk("Een tiener draagt plots dezelfde kleren en gebruikt dezelfde woorden als zijn vrienden. Wat zie je?",
       ["de invloed van de peergroep", "een angstig-vermijdende hechting", "een babyreflex die terugkomt", "scheidingsangst"],
       0, "In de adolescentie stuurt de groep sterk mee."),
    keuze("Rond het [[*eerste levensjaar|tiende levensjaar|vijftiende levensjaar]] begint een baby te protesteren als zijn vertrouwde figuur weggaat.", "Scheidingsangst."),
    open_("Een mama vertelt dat haar dochter van één jaar huilt als ze haar naar de opvang brengt. Ze is ongerust. Wat zeg je haar?",
          "Dat is scheidingsangst en die is normaal rond één jaar. Ze toont net dat uw dochter een sterke band met u heeft. Een vast afscheidsritueel en een knuffel van thuis kunnen helpen."),
]
