"""Gedrag en behoeften — pittig (Boost dubbele finaliteit, ontwikkeling en pedagogisch handelen).

Strikt binnen op_behoeften: waarneembaar, niet-waarneembaar en reflexmatig
gedrag, de factoren die gedrag sturen, de piramide van Maslow en de zes
basisbehoeften van Kind en Gezin. Met een zelfgetekende lege piramide."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, GEEL

PI = Prent("piramide-leeg", "Een piramide in vijf lagen", "een lege piramide van vijf lagen, letters A (onderaan) tot E (bovenaan)")
Z = {}
for i, t in enumerate("ABCDE"):
    y0, y1 = 560 - i * 96, 560 - (i + 1) * 96
    w0, w1 = 420 - i * 80, 420 - (i + 1) * 80
    PI.pad(f"M {500 - w0} {y0} L {500 + w0} {y0} L {500 + w1} {y1} L {500 - w1} {y1} Z", LICHTGROEN if i % 2 == 0 else GEEL, DONKER, 3)
    PI.letter(500, (y0 + y1) / 2, t)
    Z[t] = [Prent.zone(500 - w1, y1, 2 * w1, 96)]
U = "piramide-leeg.svg"

KOBE = ("Lees de situatie.\n\n"
        "Kobe (7) is al de hele ochtend lastig in de klas: hij duwt, roept en kan niet stilzitten. "
        "De juf hoort dat hij zonder ontbijt naar school kwam en slecht sliep, omdat zijn ouders 's nachts ruziemaakten.")

VRAGEN = [
    klik("Bekijk de piramide van Maslow. Klik op de laag van een kind dat honger heeft en niet kan slapen van de kou.", U, Z["A"], "Eten, drinken, slapen en warmte vormen de basis."),
    klik("Klik op de laag van een kind dat graag vrienden wil en ergens bij wil horen.", U, Z["C"], "Sociaal contact komt na de fysieke behoeften en zekerheid."),
    klik("Klik op de laag van een kind dat trots is omdat de juf zijn tekening ophangt.", U, Z["D"], "Erkenning: gezien en gewaardeerd worden."),
    klik("Klik op de laag van een jongere die zijn talent voor muziek ten volle wil ontplooien.", U, Z["E"], "Zelfactualisatie: worden wie je kan zijn."),
    sorteer("Waarneembaar, niet-waarneembaar of reflexmatig gedrag?", ["waarneembaar", "niet-waarneembaar", "reflexmatig"],
            [("een kind lacht luid", "waarneembaar"), ("een kind piekert over een toets", "niet-waarneembaar"), ("je knippert als er iets naar je gezicht vliegt", "reflexmatig"), ("een kind duwt een ander weg", "waarneembaar"), ("een kind voelt zich jaloers", "niet-waarneembaar"), ("je trekt je hand weg van een heet strijkijzer", "reflexmatig")],
            "Wat je ziet, wat binnenin blijft, en wat automatisch gebeurt."),
    sorteer("Welke factor stuurt hier het gedrag?", ["biologisch", "psychologisch", "cognitief", "sociaal"],
            [("Lisa is prikkelbaar omdat ze nog niet ontbeten heeft.", "biologisch"), ("Daan zwijgt omdat hij bang is om fouten te maken.", "psychologisch"), ("Ines begint niet aan de opdracht omdat ze ze niet begrijpt.", "cognitief"), ("Bram rookt omdat al zijn vrienden het doen.", "sociaal"), ("Yara is lusteloos omdat ze koorts heeft.", "biologisch")],
            "Het lichaam, de gevoelens, wat je denkt en weet, en de groep."),
    casus(KOBE, [
        mk("Wat doet de juf best eerst?",
           ["zoeken wat er achter het gedrag zit", "hem meteen een strafwerk geven", "zijn gedrag negeren tot het vanzelf stopt", "hem buiten de klas zetten tot de middag"],
           0, "Gedrag is een signaal: eerst kijken wat eronder zit."),
        keuze("Het ontbijt dat ontbreekt, is een [[*fysieke|sociale|cognitieve]] behoefte.", "De onderste laag van Maslow."),
        keuze("Volgens Maslow kan Kobe pas goed leren als [[*zijn lagere behoeften vervuld zijn|hij eerst erkenning krijgt|hij zichzelf ontplooid heeft]].", "De onderste lagen eisen eerst aandacht."),
        keuze("De ruzie thuis raakt zijn behoefte aan [[*veiligheid|zelfactualisatie|erkenning]].", "Een kind heeft vaste, rustige mensen om zich heen nodig."),
        open_("Wat kan de juf concreet doen om Kobe vandaag te helpen? Geef twee dingen.",
              "Ze geeft hem eerst iets te eten uit de klasvoorraad. Daarna biedt ze hem een rustig plekje aan en vraagt ze kort hoe het met hem gaat."),
    ]),
    koppel("Koppel de basisbehoefte van Kind en Gezin aan het voorbeeld.",
           [("affectie", "een knuffel na een val"), ("veiligheid, duidelijkheid en continuïteit", "weten wat er na het eten komt"), ("erkenning en bevestiging", "'Wat heb jij dat goed opgeruimd!'"), ("zichzelf als kundig ervaren", "zelf leren je jas dichtritsen"), ("zingeving en morele waarden", "praten over waarom we elkaar helpen")],
           ["een nieuwe gsm kopen"],
           "Een gsm is een wens, geen basisbehoefte."),
    volgorde("Zet de lagen van de piramide van Maslow van onder naar boven.",
             ["fysieke behoeften", "zekerheid", "sociaal contact", "erkenning", "zelfactualisatie"],
             "Pas als de lagere vervuld zijn, komen de hogere aan de beurt."),
    tabel("Behoefte of wens?",
          [("eten en drinken", "behoefte"), ("een nieuwe spelconsole", "wens"), ("slaap", "behoefte"), ("merkkledij", "wens"), ("warmte en liefde", "behoefte")],
          "Een behoefte is noodzakelijk; een wens is iets wat leuk zou zijn.", ["behoefte", "wens"]),
    mk("Waarom kan een kind dat 's nachts niet geslapen heeft moeilijk samenspelen?",
       ["zijn fysieke behoefte vraagt eerst aandacht", "omdat samenspelen niets met slaap te maken heeft", "omdat het al zelfactualisatie bereikt heeft", "omdat het geen vrienden wil"],
       0, "Een onvervulde lagere behoefte laat weinig ruimte voor de rest."),
    keuze("Een kind dat stil in een hoek zit, kan toch veel [[*niet-waarneembaar|reflexmatig]] gedrag stellen, zoals piekeren.", "Denken en voelen zie je niet, maar het is gedrag."),
    inv("Hoe noem je de behoefte om je talenten ten volle te gebruiken en jezelf te ontplooien? Eén woord.", ["zelfactualisatie", "zelfontplooiing", "de zelfactualisatie"], "Zelfactualisatie."),
    tabel("Klopt dit over gedrag en behoeften?",
          [("Twee kinderen kunnen op dezelfde situatie heel anders reageren.", J), ("Moeilijk gedrag is vaak een signaal van een behoefte.", J), ("Een reflex kies je bewust.", F), ("Erkenning staat onderaan de piramide van Maslow.", F)],
          "Onderaan staan de fysieke behoeften."),
    mk("Een kleuter wil zijn schoenen zelf aandoen. De begeleider laat hem proberen en helpt pas als het echt niet lukt. Welke basisbehoefte steunt ze?",
       ["zichzelf als kundig ervaren", "affectie", "zingeving en morele waarden in de groep", "lichamelijke behoeften"],
       0, "Zelf proberen, met hulp in de buurt, laat een kind zijn eigen kunnen voelen."),
    keuze("Vaste begeleiders en een vast dagritme geven een kind [[*veiligheid en duidelijkheid|zelfactualisatie|affectie]].", "Continuïteit: vaste mensen, vaste afspraken."),
    sleep("Volgens Maslow komen eerst de [[fysieke]] behoeften, dan [[zekerheid]], dan sociaal contact, dan [[erkenning]] en bovenaan [[zelfactualisatie]].",
          ["affectie"],
          "Affectie is een basisbehoefte bij Kind en Gezin, geen laag bij Maslow."),
    keuze("Een tiener die zich gewaardeerd voelt door zijn trainer, krijgt [[*erkenning|zekerheid|voedsel]].", "Gezien en bevestigd worden."),
    tabel("Welke laag van Maslow?",
          [("een dak boven je hoofd", "zekerheid"), ("vrienden op school", "sociaal contact"), ("een prijs voor je tekening", "erkenning"), ("drinken als je dorst hebt", "fysieke behoeften")],
          "Van onder naar boven: fysiek, zekerheid, sociaal contact, erkenning, zelfactualisatie.", ["fysieke behoeften", "zekerheid", "sociaal contact", "erkenning"]),
    keuze("Een kind dat 's avonds vertelt waarom het goed is om een ander te helpen, werkt aan [[*zingeving|affectie|lichamelijke behoeften]].", "Zingeving en morele waarden: weten wat goed is."),
    keuze("Gedrag is alles wat een mens doet, zegt, [[*denkt en voelt|koopt en bezit|erft en krijgt]].", "Ook wat je niet ziet, is gedrag."),
    mk("Twee broers krijgen allebei een slecht rapport. De ene huilt, de andere lacht het weg. Waarom?",
       ["hun biologische, psychologische en sociale factoren verschillen", "een van de twee heeft geen gedrag", "rapporten hebben nooit enige invloed op het gedrag van kinderen of jongeren", "de ene broer heeft geen behoeften meer"],
       0, "Elk kind brengt een ander lichaam, een andere ervaring en een andere omgeving mee."),
    tabel("Is dit een basisbehoefte van een kind volgens Kind en Gezin?",
          [("affectie", J), ("een eigen tablet", F), ("erkenning en bevestiging", J), ("zingeving", J), ("dure merkkledij", F)],
          "Zes basisbehoeften, geen spullen."),
    keuze("Een kind dat zich niet veilig voelt, komt volgens Maslow moeilijk toe aan [[*sociaal contact en erkenning|eten en drinken|slapen]].", "Hogere lagen wachten tot de lagere vervuld zijn."),
    inv("Hoe noem je de behoefte aan vaste mensen, vaste afspraken en duidelijkheid? Eén woord.", ["veiligheid", "de veiligheid"], "Veiligheid."),
    mk("Welke vraag stel je je eerst bij moeilijk gedrag?",
       ["welke behoefte zit hier misschien achter?", "welke straf is hier het zwaarst?", "hoe kan ik dit kind zo snel mogelijk uit de groep halen?", "wie van de ouders is hier schuldig aan?"],
       0, "Honger, moeheid, angst of te weinig aandacht komen vaak als gedrag naar buiten."),
]
