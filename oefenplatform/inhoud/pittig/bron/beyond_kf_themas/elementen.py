"""Niet-westerse invloeden en kunsthistorische elementen — pittig
(🌍 Beyond doorstroom, kunstbeschouwing en filosofie). Strikt binnen
beyond/bron/kfb_elementen.py: Japanse, Afrikaanse, Moorse, Oosterse en
Egyptische invloeden; schoonheidsidealen, economische waarde,
opdrachtgevers, genderdimensie, het bovennatuurlijke en vakmanschap."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL

# Prent: drie bogen ------------------------------------------------------------------
BO = Prent("drie-bogen", "Drie soorten bogen",
           "drie poorten naast elkaar: A met een halve cirkel als boog, B met een boog die bovenaan in een punt samenkomt, C met een boog die breder is dan de opening, zoals een hoefijzer")
BOOG = {}
STEEN = "#e9e2cf"


def poort(letter, x, boog):
    BO.rect(x - 110, 140, 220, 400, STEEN, DONKER, 0, 3)
    BO.pad(boog, "#ffffff", DONKER, 4)
    BO.letter(x, 595, letter)
    BOOG[letter] = (x - 120, 130, 240, 420)


poort("A", 180, "M 110 540 L 110 330 A 70 70 0 0 1 250 330 L 250 540 Z")
poort("B", 500, "M 430 540 L 430 340 Q 435 240 500 190 Q 565 240 570 340 L 570 540 Z")
poort("C", 820, "M 750 540 L 750 380 A 80 80 0 1 1 890 380 L 890 540 Z")
for (x, kl) in ((820, BLAUW),):
    for i in range(6):
        BO.rect(x - 105 + i * 35, 150, 30, 30, GEEL if i % 2 else kl, DONKER, 2, 1)


def bz(l):
    return [Prent.zone(*BOOG[l])]


VRAGEN = [
    klik("Klik op de hoefijzerboog, typisch voor Moorse architectuur.", BO.bestand, bz("C"),
         "De hoefijzerboog is breder dan de opening eronder. Je ziet hem in de moskee van Córdoba en in het Alhambra."),
    klik("Klik op de boog die je in Romeinse en romaanse bouwwerken ziet.", BO.bestand, bz("A"),
         "De rondboog is een halve cirkel."),
    met_prent(BO.bestand, keuze("Boog B is een [[*spitsboog|rondboog|hoefijzerboog]], typisch voor de [[*gotiek|Romeinse kunst|Moorse kunst]]. Boven poort C zie je [[*tegels met een geometrisch patroon|een fresco met heiligen|een Griekse fries met goden]].",
              "Moorse kunst gebruikt vaak geometrische patronen en sierlijke tegels.")),
    sorteer("Welke niet-westerse invloed zie je?", ["Japans", "Afrikaans", "Moors", "Oosters (gamelan)"], [
        ["vlakke kleuren, contourlijnen en een waaier bij Van Gogh", "Japans"],
        ["hoekige, vereenvoudigde maskergezichten bij Picasso", "Afrikaans"],
        ["hoefijzerbogen en binnentuinen met water", "Moors"],
        ["andere toonladders en klankkleuren bij Debussy", "Oosters (gamelan)"],
        ["een brug over water met een hoge horizon", "Japans"],
        ["fijn stucwerk en geometrische tegels in het Alhambra", "Moors"],
    ], "Niet-westerse kunst beïnvloedde schilderkunst, architectuur en muziek."),
    koppel("Koppel de kunstvorm aan de niet-westerse invloed.", [
        ["schilderkunst", "Afrikaanse en Japanse invloeden"],
        ["architectuur", "Moorse en Oosterse invloeden"],
        ["muziek", "Oosterse en Afrikaanse invloeden"],
        ["beeldhouwkunst", "Egyptische en Griekse invloeden"],
    ], ["Romeinse invloeden in de film"], "Dit is de indeling van de niet-westerse invloeden per kunstvorm."),
    tabel("Klopt dit over niet-westerse invloeden?", [
        ("Blues en jazz hebben sterke Afrikaanse wortels.", J),
        ("Debussy hoorde gamelan op de wereldtentoonstelling van 1889 in Parijs.", J),
        ("Afrikaanse maskers zetten Picasso aan tot realistische kopieën.", F),
        ("Westerse kunstenaars lieten zich nooit door niet-westerse kunst beïnvloeden.", F),
    ], "De maskers inspireerden net tot vereenvoudiging en vervorming."),
    casus(
        "Een westers schilderij uit 1887 toont een brug over een rivier in de regen. De kleuren zijn vlak, zonder schaduw. Elke vorm heeft een dikke contourlijn. "
        "De horizon ligt hoog, en een boom staat schuin afgesneden aan de rand. Rond het schilderij staan tekens die op een vreemd schrift lijken.",
        [
            mk("Welke invloed zie je hier het sterkst?",
               ["Japanse houtsneden", "Afrikaanse maskers", "Egyptische reliëfs", "Moorse tegels"], 0,
               "Vlakke kleuren, contourlijnen, een hoge horizon en ongewone uitsneden komen uit Japanse prenten."),
            inv("Hoe heet deze invloed van Japanse prenten op de westerse kunst?", ["japonisme", "japonaiserie"],
                "Van Gogh kopieerde zelfs Japanse prenten met olieverf."),
            mk("Waarom kwamen zulke prenten na 1850 massaal naar Europa?",
               ["door handel en wereldtentoonstellingen", "door het internet en de televisie thuis",
                "door een bevel van de paus in Rome aan alle schilders", "door een verbod op Europese kunst in musea"], 0,
               "Handel, wereldtentoonstellingen en ook de koloniale overheersing brachten veel niet-westerse voorwerpen naar Europa."),
        ],
    ),
    tabel("Grieks of Romeins schoonheidsideaal?", [
        ("jong, perfect en tijdloos", "Grieks"),
        ("oud, met rimpels en eigen trekken", "Romeins"),
        ("berekende verhoudingen, zoals in de canon van Polykleitos", "Grieks"),
        ("herkenbaar portret van één bepaalde senator", "Romeins"),
    ], "De Grieken zochten het ideaal, de Romeinen het realisme.",
       kolommen=["Grieks", "Romeins"]),
    mk("Een hedendaagse kunstenaar toont een kapotte, vuile stoel in een witte zaal. Wat zegt dat over het schoonheidsideaal van vandaag?",
       ["schoonheid hoeft niet het doel te zijn", "elk werk moet nog altijd de Griekse verhoudingen volgen",
        "enkel mooie, nieuwe voorwerpen mogen in een museum", "de kunstenaar kon geen mooie stoel betalen"], 0,
       "Veel hedendaagse kunst wil vooral doen nadenken. Ze mag ook lelijk of schokkend zijn."),
    tabel("Welk kunsthistorisch element speelt hier vooral?", [
        ("een stad bouwt een groot museum en krijgt veel meer toeristen", "economische waarde"),
        ("een vorst laat zich schilderen met kroon en zwaard", "opdrachtgever"),
        ("een affiche telt hoe weinig vrouwen in een museum hangen", "genderdimensie"),
        ("een heilige met een stralenkrans boven het hoofd", "het bovennatuurlijke"),
    ], "Economische waarde, opdrachtgevers, gender en het bovennatuurlijke zijn kunsthistorische elementen.",
       kolommen=["economische waarde", "opdrachtgever", "genderdimensie", "het bovennatuurlijke"]),
    sorteer("Verhoogt dit meestal de financiële waarde van een werk, of zegt het er weinig over?", ["verhoogt de waarde", "zegt weinig over de waarde"], [
        ["de kunstenaar is wereldberoemd", "verhoogt de waarde"],
        ["er bestaan maar een paar werken van", "verhoogt de waarde"],
        ["het werk hing in een beroemde verzameling", "verhoogt de waarde"],
        ["de kleur van de muur in de veilingzaal", "zegt weinig over de waarde"],
        ["het aantal letters in de titel", "zegt weinig over de waarde"],
    ], "Bekendheid, zeldzaamheid en herkomst spelen mee, net als de staat van het werk en de vraag van verzamelaars."),
    mk("Een kunstacademie in de 19de eeuw laat vrouwen niet toe bij het tekenen naar naaktmodel. Wat verklaart dit mee?",
       ["waarom vrouwen minder in musea hangen", "waarom vrouwen enkel abstracte kunst maakten",
        "waarom vrouwen nooit model stonden voor schilders", "waarom kunstacademies vandaag niet meer bestaan"], 0,
       "Zonder opleiding en opdrachten kregen vrouwen minder kansen. Vrouwen waren wel vaak model of onderwerp."),
    keuze("De [[*Guerrilla Girls|Medici|Vlaamse primitieven]] maken affiches tegen de ongelijkheid van vrouwen in de kunstwereld. Dat is kunst als middel voor [[*genderactivisme|decoratie|restauratie]].",
          "Ze dragen gorillamaskers en werken met cijfers en humor."),
    mk("Welke kunstenares uit de barok schilderde krachtige vrouwen uit de bijbel?",
       ["Artemisia Gentileschi", "Frida Kahlo uit Mexico", "Georgia O'Keeffe", "Berthe Morisot uit Parijs"], 0,
       "Artemisia Gentileschi werkte in de 17de eeuw. De andere kunstenaressen zijn later."),
    tabel("Klopt dit over het bovennatuurlijke?", [
        ("Een stralenkrans of nimbus duidt aan dat een figuur heilig is.", J),
        ("Bovennatuurlijke thema's verdwenen volledig uit de moderne kunst.", F),
        ("Het surrealisme werkt met dromen en bovennatuurlijke beelden.", J),
    ], "Ook moderne kunstenaars zoals Kandinsky zochten het spirituele."),
    casus(
        "Marcel Duchamp zette in 1917 een gewoon urinoir in een tentoonstelling. Hij gaf het de titel Fontein en tekende het met een valse naam. "
        "Hij had het niet zelf gemaakt, maar in een winkel gekocht.",
        [
            mk("Wat stelt Duchamp hiermee vooral in vraag?",
               ["of het idee boven het vakmanschap gaat", "of sanitair wel goed genoeg is voor een museum",
                "of Michelangelo echt beter kon beeldhouwen dan hij", "of een beeld altijd in brons of marmer moet"], 0,
               "Bij conceptuele kunst telt het idee meer dan het maken met de hand."),
            inv("Hoe heet kunst waarbij het idee belangrijker is dan het maken met de hand? ... kunst", ["conceptuele", "conceptueel", "conceptuele kunst"],
                "Bij traditionele kunst staat het vakmanschap net centraal."),
            tabel("Past dit bij traditionele kunst of bij conceptuele kunst?", [
                ("jaren oefenen om marmer te leren houwen", "traditioneel"),
                ("een gewoon voorwerp kiezen en het een nieuwe betekenis geven", "conceptueel"),
                ("het idee achter het werk is het eigenlijke kunstwerk", "conceptueel"),
            ], "Vakmanschap heeft een andere betekenis bij traditionele en bij conceptuele kunst.",
               kolommen=["traditioneel", "conceptueel"]),
        ],
    ),
    mk("Waarom werkt een goede restaurateur liefst met de originele technieken en materialen?",
       ["zo blijft het werk dicht bij het origineel", "omdat nieuwe verf altijd veel duurder is dan oude",
        "omdat musea volgens de wet geen nieuwe verf mogen", "om het werk daarna snel en duur te verkopen"], 0,
       "Een goede restauratie respecteert het origineel."),
    sleep("Een renaissanceschilderij toont de [[opdrachtgever]] knielend naast de heiligen. Zo toont hij zijn vroomheid en zijn [[status]].",
          ["restaurateur", "nimbus"], "Zo'n schenkersportret zie je ook op het Lam Gods."),
    keuze("Een sleutel bij Petrus, een lam voor Christus en een schedel voor de dood: wat zulke figuren en voorwerpen betekenen, bestudeert de [[*iconografie|restauratie|culturele economie]].",
          "Iconografie helpt om symbolen in kunst te lezen."),
    mk("Waarom beeldt men in islamitische religieuze gebouwen liefst geen mensen af?",
       ["dat past niet in de religieuze traditie", "Moorse kunstenaars konden geen mensen tekenen",
        "geometrische patronen waren veel goedkoper", "de koning hield helemaal niet van kunst"], 0,
       "De culturele en religieuze context verklaart hier de vorm: patronen en sierlijke letters."),
    tabel("Klopt dit over opdrachtgevers?", [
        ("Een opdrachtgever bepaalde vaak mee wat er op een werk te zien was.", J),
        ("Kunst kon dienen om de macht van een vorst te tonen.", J),
        ("Opdrachtgevers hadden vroeger geen enkele invloed op het thema.", F),
    ], "Financiering, thema's en het tonen van macht hangen samen met de opdrachtgever."),
    mk("Een museum koopt een werk van een onbekende kunstenaar. Een jaar later zijn zijn werken veel duurder. Welk element zie je?",
       ["economische waarde", "het bovennatuurlijke in de kunst", "het schoonheidsideaal van de Grieken", "vakmanschap bij restauratie"], 0,
       "Wie een werk koopt of toont, beïnvloedt de financiële waarde."),
    keuze("Een rijke familie hangt een duur schilderij in de ontvangstzaal zodat elke bezoeker het ziet. Dat toont het verband tussen kunst en [[*sociale status|restauratie|iconografie]].",
          "Wie dure kunst bezit of laat maken, toont rijkdom en aanzien."),
    tabel("Klopt dit over de afbeelding van genders in oudere westerse kunst?", [
        ("de vrouw vaak als model of naakt onderwerp", J),
        ("de man vaak als held, krijger of vorst", J),
        ("vrouwen meestal als bekende kunstenaar met eigen naam in het museum", F),
    ], "De afbeelding van genders in de kunst is een deel van de genderdimensie."),
    mk("Wat bedoelt men met artistieke vernieuwing?",
       ["een kunstenaar vindt een nieuwe techniek of vorm", "een kunstenaar kopieert precies zijn leraar",
        "een kunstenaar geeft een oud werk een nieuwe lijst", "een kunstenaar verkoopt een oud werk opnieuw"], 0,
       "Van Eyck met olieverf, Monet met licht en Picasso met het kubisme zijn voorbeelden."),
    open_("Leg met een voorbeeld uit hoe niet-westerse kunst een westerse kunstenaar beïnvloedde.",
          "Picasso zag in een museum in Parijs Afrikaanse maskers. De hoekige, vereenvoudigde gezichten inspireerden hem. In Les Demoiselles d'Avignon schilderde hij gezichten die op maskers lijken. Die vereenvoudiging hielp hem op weg naar het kubisme. De maskers kwamen naar Europa via de koloniale handel."),
]
