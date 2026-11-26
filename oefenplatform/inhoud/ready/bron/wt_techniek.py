# -*- coding: utf-8 -*-
"""Ready wetenschap en techniek: Techniek rondom ons (eenvoudige machines: hefboom,
katrol, wiel; stroomkring met batterij en lampje; geleiders; veilig met elektriciteit;
een techniek stap voor stap ontwerpen)."""
from vr import mk, inv, wn

TITEL = "Techniek rondom ons"
UITLEG_1 = "Wiel, hefboom en katrol maken werk lichter."
UITLEG_2 = "Een lampje laten branden, en veilig blijven."

DEEL_1 = [
    mk("Waarom heeft een kruiwagen een wiel?", ["Zo kan je zware dingen makkelijker duwen.", "Zo ziet hij er veel mooier en sterker uit.", "Zo kan hij een beetje vliegen.", "Zo blijft hij altijd stilstaan."], 0, "Een wiel rolt en maakt duwen veel lichter."),
    mk("Wat is een wip op de speelplaats?", ["een hefboom", "een katrol", "een schroef", "een grote magneet"], 0, "Een wip is een plank die kantelt op een steunpunt: een hefboom."),
    wn("Met een lange hefboom kan je iets zwaars makkelijker optillen.", True, "Hoe langer de hefboom, hoe minder kracht je nodig hebt."),
    mk("Waarmee hijs je een emmer omhoog met een touw over een wiel?", ["een katrol", "een hamer", "een kleine zaag", "een schaar"], 0, "Een katrol is een wiel met een touw. Je trekt naar beneden en de emmer gaat omhoog."),
    inv("Een schaar bestaat uit twee ___s die draaien rond een schroefje. (h...)", ["hefboom", "hefbomen"], "Elk mes van een schaar werkt als een hefboom."),
    mk("Welk werktuig gebruik je om een spijker in hout te slaan?", ["een hamer", "een tang", "een zaag", "een schroevendraaier"], 0, "Met een hamer sla je de spijker in."),
    wn("Een fiets heeft tandwielen en een ketting.", True, "Als je trapt, draait de ketting het achterwiel rond."),
    mk("Waarom zit er een flessenopener aan je keukenlade?", ["Hij werkt als een hefboom.", "Hij koelt de fles in een paar seconden af.", "Hij maakt de fles groter.", "Hij vult de fles opnieuw."], 0, "Met een kleine kracht op de lange kant krijg je de dop eraf."),
    wn("Een helling maakt het makkelijker om een zware kar omhoog te duwen dan een trap.", True, "Langs een helling duw je over een langere weg, maar met minder kracht."),
    mk("Wat is de eerste stap als je iets wil maken, zoals een vogelhuisje?", ["Bedenken en tekenen wat je wil maken.", "Meteen beginnen zagen in de eerste plank die je vindt.", "Alles verven.", "Het weggooien."], 0, "Eerst bedenk en teken je een plan. Dan maak je het en test je het."),
    inv("Na het maken ___ je of het goed werkt. (t...)", ["test", "testen"], "Testen hoort bij elk techniekproject."),
    wn("Een rolschaats heeft wielen om makkelijk te rollen.", True, "Wielen verkleinen de wrijving met de grond."),
    mk("Welk werktuig gebruik je om een schroef in te draaien?", ["een schroevendraaier", "een hamer", "een lijmpot", "een rol plakband"], 0, "Met een schroevendraaier draai je de schroef in het hout."),
    wn("Een vlag hijs je zonder katrol, gewoon door te klimmen.", False, "Bovenaan de vlaggenmast zit een katrol: een wieltje waarover het touw loopt."),
    mk("Waarom heeft een fiets remmen?", ["om veilig te stoppen", "om sneller te gaan", "om licht te geven", "om de banden op te pompen"], 0, "Remmen zorgen dat je op tijd stopt."),
    wn("Een deurklink werkt als een katrol.", False, "Je duwt op de lange klink en het slot draait makkelijk open."),
    mk("Wat maakt een vergrootglas?", ["Het laat dingen groter lijken.", "Het maakt dingen zwaarder.", "Het maakt een zacht geluid.", "Het maakt zelf licht in het donker."], 0, "Met een vergrootglas zie je kleine dingen groter."),
    wn("Een tandenborstel is een machine met wielen.", False, "Een gewone tandenborstel heeft geen wielen. Het is een eenvoudig werktuig."),
    inv("Een lift gaat omhoog met kabels en ___. (k...)", ["katrollen", "katrol"], "Liften gebruiken katrollen en een motor."),
    wn("Hoe korter de hefboom, hoe minder kracht je nodig hebt.", False, "Net omgekeerd: een langere hefboom vraagt minder kracht."),
]

DEEL_2 = [
    mk("Wat heb je nodig om een lampje te laten branden?", ["een batterij, draadjes en een lampje", "enkel een lampje en een beetje zonlicht", "water en een lampje", "een magneet en papier"], 0, "De stroom moet van de batterij door de draadjes naar het lampje en terug."),
    wn("Een lampje brandt enkel als de stroomkring gesloten is.", True, "Als de kring ergens open is, kan de stroom niet rondgaan."),
    mk("Wat doet een schakelaar?", ["Hij opent of sluit de kring.", "Hij maakt de batterij weer helemaal vol.", "Hij maakt het lampje groter.", "Hij maakt lawaai."], 0, "Met de schakelaar zet je het licht aan of uit."),
    mk("Welk voorwerp laat stroom door?", ["een metalen sleutel", "een houten stokje", "een gom", "een lange plastic lat"], 0, "Metaal is een goede geleider."),
    wn("Plastic laat stroom goed door.", False, "Plastic is een isolator: het laat geen stroom door. Daarom zit er plastic rond elektrische draden."),
    inv("Een stof die stroom goed doorlaat, heet een ___. (g...)", ["geleider"], "Metalen zijn geleiders."),
    mk("Waarom zit er een plastic laag rond een elektriciteitsdraad?", ["tegen een schok", "om de draad mooi te maken", "om de draad zwaarder te maken", "om licht te geven"], 0, "Plastic laat geen stroom door en beschermt je."),
    wn("Je mag met natte handen aan een stopcontact komen.", False, "Water geleidt stroom. Met natte handen kan je een gevaarlijke schok krijgen."),
    mk("Wat doe je als een elektrische draad kapot is?", ["Niet aankomen en het zeggen.", "Erop trappen.", "Hem zelf herstellen met een stukje plakband.", "Erin bijten."], 0, "Een kapotte draad is gevaarlijk."),
    wn("Een batterij van 1,5 volt is veilig om mee te experimenteren.", True, "Kleine batterijen zijn veilig. Het stopcontact is dat niet."),
    mk("Welk toestel werkt op elektriciteit?", ["een broodrooster", "een fiets", "een hamer", "een papierschaar"], 0, "Een broodrooster moet je in het stopcontact steken."),
    wn("Een lege batterij mag bij het gewone afval.", False, "Lege batterijen breng je naar een inzamelpunt, bijvoorbeeld in de supermarkt."),
    wn("Als je het licht uitdoet wanneer je een kamer verlaat, bespaar je energie.", True, "Elektriciteit die je niet gebruikt, hoef je niet te betalen en sparen we voor het milieu."),
    mk("Welke energie gebruikt een zonnepaneel?", ["zonlicht", "wind", "stromend water", "benzine"], 0, "Zonnepanelen maken stroom uit zonlicht."),
    mk("Wat draait er bij een windmolen om stroom te maken?", ["de wieken", "de deur", "de trap", "de lamp bovenaan"], 0, "De wind duwt de wieken rond. Zo wordt stroom gemaakt."),
    wn("Steenkool en benzine raken nooit op.", False, "Die raken ooit op. Zon en wind blijven altijd beschikbaar."),
    mk("In een zaklamp zit een batterij. Waarom brandt het lampje niet meer?", ["De batterij is leeg.", "Het is dag.", "De zaklamp is te zwaar.", "De zaklamp is gloednieuw."], 0, "Een lege batterij geeft geen stroom meer."),
    wn("Een metalen paperclip kan een open stroomkring weer sluiten.", True, "Metaal geleidt, dus de stroom kan er weer door."),
    inv("Toestellen die je niet gebruikt, trek je uit het ___. (s...)", ["stopcontact"], "Zo verbruiken ze geen stroom."),
    wn("Een lampje brandt ook als je maar één draadje gebruikt.", False, "Je hebt een kring nodig: van de ene pool van de batterij naar het lampje en terug naar de andere pool."),
]


# Prentvragen (vraag 21 tot 24), Kim 26/11.
from vr import mk, inv, wn
import prent as P
PRENT_1 = [
    mk("Welk werktuig zie je op de prent?", ["een hefboom", "een katrol", "een wiel", "een tandwiel"], 0, "Een wip is een hefboom: een lange plank die op één punt draait.", prent=P.p_wip("techniek-wip")),
    inv("Met dit wiel en touw trek je iets zwaars omhoog. Hoe heet het? Een k...", ["katrol", "een katrol"], "Een katrol maakt omhoog trekken makkelijker.", prent=P.p_katrol("techniek-katrol")),
    wn("Wielen maken het makkelijker om iets te verplaatsen.", True, "Een trein, een fiets en een kar rollen op wielen. Dat gaat veel lichter dan schuiven.", prent=P.p_voorwerp("techniek-trein", "trein")),
    mk("Waarom gaat het makkelijk om met een kruiwagen een zware lading te verplaatsen?", ["door het wiel", "door de groene kleur", "omdat hij nieuw is", "door de bak"], 0, "Het wiel draagt een deel van het gewicht en rolt.", prent=P.p_ding("techniek-kruiwagen", "kruiwagen")),
]
PRENT_2 = [
    wn("Het lampje brandt, want de stroomkring is gesloten.", True, "De draden maken een rondje van de batterij naar het lampje en terug.", prent=P.p_stroomkring("techniek-kring-dicht", True)),
    mk("Waarom brandt het lampje niet?", ["De kring is open.", "De batterij is te groot.", "Het lampje is te klein.", "Er is te veel draad."], 0, "Er zit een opening in de draad. De stroom kan niet rond.", prent=P.p_stroomkring("techniek-kring-open", False)),
    inv("Wat geeft de stroom in deze kring? De b...", ["batterij", "de batterij"], "De batterij duwt de stroom door de draden.", prent=P.p_stroomkring("techniek-kring-batterij", True)),
    wn("Je steekt nooit iets anders dan een stekker in een stopcontact.", True, "Uit een stopcontact komt sterke stroom. Dat is gevaarlijk.", prent=P.p_ding("techniek-stopcontact", "stopcontact")),
]
