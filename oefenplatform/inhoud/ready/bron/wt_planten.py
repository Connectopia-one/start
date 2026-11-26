# -*- coding: utf-8 -*-
"""Ready wetenschap en techniek: Planten en dieren (delen van een plant, wat een plant
nodig heeft, levenscyclus, dieren groeperen, voedselketen). Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Planten en dieren"
UITLEG_1 = "Wortel, stengel, blad en bloem."
UITLEG_2 = "Dieren groeperen en wie eet wie?"

DEEL_1 = [
    mk("Welk deel van een plant haalt water uit de grond?", ["het blad", "de wortel", "de bloem", "de vrucht"], 1, "De wortels zitten in de grond en zuigen water op. Ze houden de plant ook vast."),
    mk("Wat doet de stengel van een plant?", ["Hij maakt zaadjes.", "Hij brengt water naar boven en houdt de plant recht.", "Hij eet insecten.", "Hij maakt de grond nat."], 1, "Door de stengel gaat het water van de wortels naar de bladeren."),
    wn("Een plant heeft licht nodig om te groeien.", True, "Met zonlicht maken de bladeren voedsel voor de plant."),
    mk("Wat heeft een plant NIET nodig om te groeien?", ["water", "licht", "lucht", "snoep"], 3, "Een plant heeft water, licht, lucht en voedingsstoffen uit de grond nodig."),
    inv("Uit een ___ groeit een nieuwe plant. (z...)", ["zaadje", "zaad", "zaadjes"], "In een zaadje zit een klein plantje dat kan kiemen."),
    mk("Wat komt eerst bij een boon die groeit?", ["bloem", "zaadje", "boon aan de plant", "blad"], 1, "Eerst is er een zaadje. Dat kiemt, groeit, bloeit en maakt nieuwe bonen."),
    wn("De bloem is het deel waar later de vrucht en de zaadjes uit groeien.", True, "Na de bloei ontstaat er een vrucht met zaadjes, zoals een appel met pitjes."),
    mk("Welke dieren helpen bloemen om zaadjes te maken door stuifmeel mee te nemen?", ["bijen", "wormen", "mollen", "vissen"], 0, "Bijen vliegen van bloem naar bloem en nemen stuifmeel mee."),
    wn("Een boom is ook een plant.", True, "Een boom heeft wortels, een stam (dikke stengel), bladeren en bloemen of zaden."),
    inv("Een appel is de ___ van de appelboom. (v...)", ["vrucht"], "In de vrucht zitten de zaadjes, de pitjes."),
    mk("Waarom worden de bladeren van veel bomen in de herfst bruin en vallen ze af?", ["Ze zijn ziek.", "De boom spaart water en rust in de winter.", "De wind trekt ze eraf.", "Dieren eten ze op."], 1, "In de winter is er weinig licht en is het koud. De boom laat zijn bladeren vallen en rust."),
    wn("Een plant zonder water blijft altijd mooi groen.", False, "Zonder water verwelkt een plant: de bladeren hangen slap en worden bruin."),
    mk("Van welke groente eet je de wortel?", ["tomaat", "wortel", "appel", "sla"], 1, "Een wortel groeit onder de grond: je eet de wortel van de plant."),
    mk("Van welke plant eet je de bladeren?", ["aardappel", "sla", "appel", "wortel"], 1, "Sla zijn bladeren. Van een aardappel eet je een knol onder de grond."),
    wn("Een cactus heeft dikke stengels om water in te bewaren.", True, "Daardoor kan een cactus lang zonder regen, in de woestijn."),
    inv("Bomen die in de winter groen blijven, zoals de den, heten ___bomen. (n...)", ["naald", "naaldbomen"], "Naaldbomen hebben naalden in plaats van brede bladeren."),
    mk("Wat gebeurt er als je een plantje in een donkere kast zet?", ["Het groeit sneller.", "Het wordt bleek en zwak.", "Het krijgt meer bloemen.", "Er verandert niets."], 1, "Zonder licht kan het plantje geen voedsel maken."),
    wn("Paddenstoelen zijn dieren.", False, "Paddenstoelen zijn geen dieren en ook geen echte planten: ze horen bij de zwammen."),
    mk("Hoe verspreidt een paardenbloem haar zaadjes?", ["met de wind", "met vissen", "door te springen", "met regenwormen"], 0, "De pluisjes waaien weg met de wind en landen ergens anders."),
    wn("Gras is geen plant.", False, "Gras is wel een plant: het heeft wortels, stengels en bladeren, en bloeit ook."),
]

DEEL_2 = [
    mk("Welk dier is een zoogdier?", ["kip", "kikker", "hond", "haai"], 2, "Een zoogdier drinkt melk bij zijn moeder als het jong is en heeft haar."),
    mk("Waaraan herken je een vogel?", ["schubben", "veren", "haar", "een schelp"], 1, "Alle vogels hebben veren en leggen eieren."),
    wn("Een walvis is een vis.", False, "Een walvis is een zoogdier: hij ademt lucht en de jongen drinken melk."),
    mk("Hoeveel poten heeft een insect?", ["4", "6", "8", "10"], 1, "Insecten zoals mieren en bijen hebben 6 poten."),
    inv("Een spin heeft ___ poten.", "8", "Een spin heeft 8 poten. Daarom is het geen insect.", 8),
    mk("Hoe verandert een rups?", ["Ze wordt een kikker.", "Ze wordt een vlinder.", "Ze wordt een mier.", "Ze wordt een slak."], 1, "Ei, rups, pop, vlinder: dat is de levenscyclus van een vlinder."),
    mk("Wat komt eerst in het leven van een kikker?", ["kikker", "kikkervisje", "kikkerdril (eitjes)", "kikker met staart"], 2, "Eerst het kikkerdril, dan het kikkervisje, dan een kikkertje met pootjes."),
    wn("Een kikker kan zowel in het water als op het land leven.", True, "Kikkers zijn amfibieën: jong in het water, later ook op het land."),
    mk("Wat eet een planteneter?", ["vlees", "planten", "stenen", "andere dieren"], 1, "Een planteneter, zoals een koe of konijn, eet planten."),
    mk("Welk dier is een vleeseter?", ["konijn", "koe", "vos", "schaap"], 2, "Een vos eet andere dieren, zoals muizen."),
    inv("Een dier dat planten én vlees eet, heet een ___eter. (a...)", ["alles", "alleseter"], "Mensen en varkens zijn alleseters."),
    mk("Welke voedselketen klopt?", ["vos → konijn → gras", "gras → konijn → vos", "konijn → gras → vos", "gras → vos → konijn"], 1, "Het konijn eet gras, en de vos eet het konijn. De pijl betekent: wordt opgegeten door."),
    wn("Een egel slaapt in de winter.", True, "Een egel houdt een winterslaap onder bladeren."),
    mk("Waarom trekken zwaluwen in de herfst naar het zuiden?", ["Ze zoeken warmte en insecten om te eten.", "Ze gaan op vakantie.", "Ze vluchten voor de egels.", "Ze willen zwemmen."], 0, "In de winter zijn er hier geen insecten. In het warme zuiden wel."),
    wn("Een vis ademt met kieuwen.", True, "Kieuwen halen zuurstof uit het water."),
    mk("Welk dier heeft schubben?", ["vis", "kat", "mus", "bij"], 0, "Vissen en slangen hebben schubben."),
    inv("Dieren met een ruggengraat heten ___ dieren. (g...)", ["gewervelde", "gewervelde dieren"], "Zoogdieren, vogels, vissen, reptielen en amfibieën hebben een ruggengraat."),
    wn("Een slak is een gewerveld dier.", False, "Een slak heeft geen ruggengraat. Ze is een ongewerveld dier."),
    mk("Hoe beschermt een egel zich?", ["Hij rolt zich op met zijn stekels naar buiten.", "Hij vliegt weg.", "Hij verandert van kleur.", "Hij zwemt snel weg."], 0, "De stekels houden vijanden op afstand."),
    wn("Je mag wilde dieren in het bos gerust meenemen naar huis.", False, "Wilde dieren laat je in de natuur. Vind je een gewond dier, vraag dan hulp aan een volwassene of het dierenasiel."),
]
