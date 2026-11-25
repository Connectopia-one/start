"""Sociale instituties — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_instituties: gezin, familie, peergroep, school,
buurt, (massa)media, verenigingen, rechtssysteem en religieuze instituties,
het niveau van socialisatie en hun rol in tijd en ruimte. Met een
zelfgetekend stadje."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, ROOD, BLAUW, LICHTGROEN, ORANJE

ST = Prent("stadje-instituties", "Een stadje met zes gebouwen", "zes gebouwen naast elkaar, letters A tot F")
ST.rect(0, 470, 1000, 170, "#e4ecd8", "none", 0, 0); ST.lijn(0, 470, 1000, 470, DONKER, 2)
# A: woonhuis
ST.rect(40, 340, 120, 130, "#f6e3c4", DONKER, 0, 3); ST.pad("M 30 340 L 100 280 L 170 340 Z", ROOD, DONKER, 3)
ST.rect(88, 410, 26, 60, ORANJE, DONKER, 0, 2); ST.rect(55, 365, 26, 26, "#cfe3f0", DONKER, 0, 2); ST.rect(122, 365, 26, 26, "#cfe3f0", DONKER, 0, 2)
# B: school met klok en speelplaats
ST.rect(200, 300, 160, 170, "#ffffff", DONKER, 0, 3); ST.pad("M 190 300 L 280 250 L 370 300 Z", BLAUW, DONKER, 3)
ST.cirkel(280, 280, 14, "#ffffff", DONKER, 2)
for i in range(3):
    for j in range(2):
        ST.rect(215 + i * 48, 320 + j * 50, 32, 30, "#cfe3f0", DONKER, 0, 1)
# C: sportveld met doel en vlaggetje (club)
ST.rect(400, 400, 150, 70, LICHTGROEN, DONKER, 0, 2); ST.lijn(475, 400, 475, 470, "#ffffff", 3)
ST.rect(400, 420, 18, 30, "none", "#ffffff", 0, 3); ST.rect(532, 420, 18, 30, "none", "#ffffff", 0, 3)
ST.lijn(560, 470, 560, 360, DONKER, 3); ST.pad("M 560 360 L 600 375 L 560 390 Z", GEEL, DONKER, 2)
# D: gerechtsgebouw met zuilen
ST.rect(620, 330, 150, 140, "#ffffff", DONKER, 0, 3); ST.pad("M 610 330 L 695 280 L 780 330 Z", GRIJS, DONKER, 3)
for i in range(4):
    ST.rect(635 + i * 36, 345, 14, 115, GRIJS, DONKER, 0, 2)
# E: gebedshuis met toren
ST.rect(800, 360, 90, 110, "#ffffff", DONKER, 0, 3); ST.rect(820, 250, 50, 110, "#ffffff", DONKER, 0, 3)
ST.pad("M 815 250 L 845 200 L 875 250 Z", GRIJS, DONKER, 3); ST.pad("M 832 470 L 832 430 Q 845 410 858 430 L 858 470 Z", ORANJE, DONKER, 2)
ST.cirkel(845, 290, 12, "#cfe3f0", DONKER, 2)
# F: zendmast met golven
ST.lijn(940, 470, 955, 230, DONKER, 4); ST.lijn(970, 470, 955, 230, DONKER, 4); ST.lijn(945, 380, 966, 380, DONKER, 2); ST.lijn(948, 320, 962, 320, DONKER, 2)
ST.pad("M 925 215 Q 955 190 985 215", "none", BLAUW, 3); ST.pad("M 915 200 Q 955 165 995 200", "none", BLAUW, 3)
POS = {"A": (100, 530), "B": (280, 530), "C": (475, 530), "D": (695, 530), "E": (845, 530), "F": (955, 530)}
for t, (x, y) in POS.items():
    ST.letter(x, y, t)
U = "stadje-instituties.svg"
Z = {"A": [Prent.zone(25, 270, 150, 290)], "B": [Prent.zone(185, 240, 190, 320)], "C": [Prent.zone(395, 350, 215, 210)],
     "D": [Prent.zone(605, 270, 180, 290)], "E": [Prent.zone(795, 190, 105, 370)], "F": [Prent.zone(905, 160, 95, 400)]}

LOUIS = ("Lees het verhaal.\n\n"
         "Louis (15) leerde thuis dat je altijd eerlijk zegt wat je denkt. Zijn vrienden vinden dat je soms beter zwijgt om geen ruzie te maken. "
         "Op TikTok ziet hij elke dag filmpjes van influencers die zeggen dat je 'gewoon jezelf' moet zijn. In de jeugdbeweging leert hij als hulpleider rekening te houden met de jongste kinderen. "
         "Zijn grootvader vertelt dat hij vroeger elke zondag naar de kerk ging, en dat de pastoor toen in het dorp zei wat wel en niet kon.")

VRAGEN = [
    klik("Bekijk het stadje. Klik op het gebouw van de institutie die normen afdwingbaar maakt.", U, Z["D"], "Het rechtssysteem: een norm wordt een wet."),
    klik("Klik op het gebouw van de religieuze institutie.", U, Z["E"], "Een gebedshuis."),
    klik("Klik op wat het best past bij een vereniging.", U, Z["C"], "Een sportclub met een eigen vlag."),
    klik("Klik op de institutie die mensen bereikt zonder rechtstreeks contact.", U, Z["F"], "De (massa)media: tertiaire socialisatie."),
    casus(LOUIS, [
        sorteer("Welke institutie werkt hier?", ["gezin", "peergroep", "media", "vereniging"],
                [("altijd eerlijk zeggen wat je denkt", "gezin"), ("soms beter zwijgen om ruzie te vermijden", "peergroep"), ("filmpjes van influencers", "media"), ("rekening houden met de jongste kinderen", "vereniging")],
                "Elke institutie geeft eigen normen door."),
        mk("Thuis en bij zijn vrienden hoort Louis andere normen. Wat gebeurt er dan volgens dit thema?",
           ["hij moet zelf kiezen", "hij verliest al zijn waarden en normen", "de primaire socialisatie stopt dan helemaal", "hij moet altijd de norm van het gezin volgen"],
           0, "In die ruimte ontstaat zelfbepaling."),
        keuze("Het verhaal van de grootvader toont dat de rol van instituties [[*verschuift in de tijd|altijd dezelfde blijft|enkel per land verschilt]].", "De kerk woog vroeger zwaarder."),
        keuze("De filmpjes op TikTok werken op het [[*tertiaire|primaire|secundaire]] niveau.", "Zonder rechtstreeks contact met een persoon."),
    ]),
    sorteer("Op welk niveau van socialisatie werkt deze institutie vooral?", ["primair", "secundair", "tertiair"],
            [("het gezin", "primair"), ("de school", "secundair"), ("de krant", "tertiair"), ("de peergroep", "secundair"), ("de televisie", "tertiair")],
            "Het gezin raakt je het diepst, de media het breedst."),
    koppel("Koppel de institutie aan het voorbeeld.",
           [("familie", "oma leert je een oud recept"), ("buurt", "een kind speelt met de kinderen van de straat"), ("school", "je leert je beurt afwachten in de klas"), ("rechtssysteem", "wie te snel rijdt, krijgt een boete")],
           ["je krijgt bruine ogen"], "Negen instituties in totaal."),
    tabel("Klopt dit over instituties?",
          [("Gezin en familie zijn twee aparte instituties.", J), ("De peergroep weegt het zwaarst in de babytijd.", F), ("De buurt heeft geen invloed op socialisatie.", F), ("Een institutie kan op meer dan één niveau werken.", J)],
          "De peergroep weegt het zwaarst in de adolescentie."),
    mk("Wat leert een kind op school naast de leerstof?",
       ["regels en samenwerken", "enkel de namen van zijn klasgenoten", "alleen de normen van zijn eigen gezin", "niets, want de school geeft enkel kennis door"],
       0, "Op tijd komen, je beurt afwachten, met anderen werken."),
    keuze("Wat je in je eerste jaren leert, voelt later vanzelfsprekend. Daarom is de invloed van het [[*gezin|rechtssysteem|krant]] zo groot.", "Het komt eerst en duurt lang."),
    keuze("Een jongere verandert van kledij om bij zijn vrienden te horen. Hier werkt de [[*peergroep|familie|religieuze institutie]].", "Leeftijdsgenoten geven normen door."),
    tabel("Is dit een van de negen instituties uit dit thema?",
          [("de buurt", J), ("de verenigingen", J), ("het weer", F), ("de religieuze instituties", J), ("de (massa)media", J)],
          "Negen instituties, van het gezin tot de religie."),
    mk("Lisa (14) kijkt van 's morgens tot 's avonds filmpjes op haar gsm. Waarom wegen die zwaar in haar socialisatie?",
       ["ze lopen de hele dag mee", "omdat ze enkel door ouders gemaakt worden", "omdat ze rechtstreeks contact vragen", "omdat ze de primaire socialisatie zijn"],
       0, "Een kanaal dat de hele dag meeloopt, geeft veel normen door."),
    keuze("In sommige landen weegt de familie zwaarder dan in Vlaanderen. Dat is een verandering in [[*ruimte|tijd|rijping]].", "Verschillen tussen plaatsen."),
    keuze("De familie is een bredere institutie dan het gezin, want ze omvat meer [[*generaties|scholen|wetten]].", "Grootouders, tantes, neven en nichten."),
    sleep("Een sociale institutie is een [[duurzaam]] verband met een [[taak]] in de samenleving. Instituties geven [[waarden]] en normen door.",
          ["toevallig", "kleur"], "Zoals het gezin, de school of het recht."),
    inv("Welke institutie staat voor de primaire socialisatie? Schrijf het met één woord, zonder lidwoord.", ["gezin", "het gezin"], "Daar begint de socialisatie."),
    tabel("Werkt deze institutie vooral op het tertiaire niveau?",
          [("de televisie", J), ("de krant", J), ("de sociale media", J), ("de buurman", F)],
          "Media bereiken je op afstand."),
    mk("Een groepje mensen wacht samen op de bus. Waarom is dat geen institutie, en het rechtssysteem wel?",
       ["het rechtssysteem is duurzaam en heeft een taak", "omdat er in een bus te weinig mensen samen zitten", "omdat een bus geen eigen gebouw heeft zoals een rechtbank", "omdat wachten op de bus verboden is door de wet"],
       0, "Een duurzaam verband met een rol in de samenleving."),
    keuze("Kinderen zitten vandaag langer op school dan vroeger, en de school neemt meer taken op. De rol van de school is [[*gegroeid|verdwenen|gelijk gebleven]].", "Ze duurt langer en doet meer."),
    keuze("Instituties geven [[*niet altijd|altijd]] dezelfde boodschap door.", "Thuis, op school en online gelden soms andere normen."),
    keuze("Een kind leert in de jeugdbeweging samenwerken en leiding nemen. Dat is de institutie [[*vereniging|familie|rechtssysteem]].", "Verenigingen zijn een eigen institutie."),
    tabel("Werkt deze institutie vooral op het secundaire niveau?",
          [("de school", J), ("de peergroep", J), ("de vereniging", J), ("het gezin", F)],
          "Alles buiten het gezin waarmee je in rechtstreeks contact komt."),
    keuze("Een jong kind speelt op straat en ziet wat buren doen. Daarom is de [[*buurt|krant|rechtbank]] voor jonge kinderen belangrijk.", "Wie je tegenkomt, bepaalt mee wat normaal lijkt."),
    mk("Een leerkracht vraagt: zet bij elke institutie of ze primair, secundair of tertiair werkt. Waarom is dat zinvol?",
       ["elke institutie werkt anders door", "omdat elke institutie maar één keer in je leven werkt", "omdat instituties nooit tegelijk werken", "omdat het niveau de grootte van het gebouw toont"],
       0, "Het gezin raakt je het diepst, de media het breedst."),
    keuze("Een vereniging kan normen doorgeven in rechtstreeks contact én via haar website. Ze werkt dan op [[*meer dan één niveau|geen enkel niveau]].", "Een institutie is niet aan één niveau gebonden."),
    open_("Kies twee instituties en leg uit hoe hun rol in de socialisatie veranderd is sinds de tijd van je grootouders.",
          "Bijvoorbeeld: de religieuze instituties wogen vroeger zwaar; de pastoor bepaalde mee wat wel en niet kon. Nu is hun rol in Vlaanderen kleiner. De media wogen vroeger licht (een krant, een radio), nu lopen sociale media de hele dag mee en geven ze veel normen door."),
]
