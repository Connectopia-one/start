# -*- coding: utf-8 -*-
"""De wisselende woorden bij de taalhoofdstukken van Nederlands, 🚀 Boost.

Vier thema's, elk deel 1 en deel 2: de woordsoorten, de werkwoorden en de
woordvorming, de zinsdelen en de spelling. Daar zit de leerstof in de **regel**
en niet in het woord, dus mag het woord wisselen. Bij de tekst-, literatuur- en
communicatiethema's blijft alles staan zoals het staat: daar verandert een
ander woord de vraag zelf.

Dit bestand wordt twee keer gebruikt. De vragen van Nederlands zijn bij
doorstroom en bij dubbele finaliteit dezelfde (beide bouwscripts lezen
dezelfde `nl_*.py`), dus dezelfde lijst gaat in allebei de vragenbestanden.
Zie `varianten_boost_doorstroom.py` en `varianten_boost_df.py`.

Een variant noemt alleen wat verandert. Waar de uitleg het woord zelf noemt,
schrijft de variant ook een eigen uitleg.
"""

HOOFDSTUKKEN = {
    "De woordsoorten op een rij — deel 1": {
        "In 'De oude molen draaide traag', welke woordsoort is 'oude'?": [
            {
                "vraag": "In 'De nieuwe brug ging gisteren open', welke woordsoort is 'nieuwe'?",
                "uitleg": "'Nieuwe' zegt iets over het zelfstandig naamwoord 'brug'. Dat is precies wat een bijvoeglijk naamwoord doet.",
            },
            {
                "vraag": "In 'Het koude water deed hem schrikken', welke woordsoort is 'koude'?",
                "uitleg": "'Koude' zegt iets over het zelfstandig naamwoord 'water'. Dat is precies wat een bijvoeglijk naamwoord doet.",
            },
            {
                "vraag": "In 'Zij droeg een rode jas', welke woordsoort is 'rode'?",
                "uitleg": "'Rode' zegt iets over het zelfstandig naamwoord 'jas'. Dat is precies wat een bijvoeglijk naamwoord doet.",
            },
        ],
        "Welke woorden zijn lidwoorden?": [
            {
                "opties": ["het", "een", "geen", "deze"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het Nederlands heeft er drie soorten: bepaald (de, het), onbepaald (een) en ontkennend (geen). 'Deze' is een aanwijzend voornaamwoord.",
            },
            {
                "opties": ["de", "het", "geen", "dat"],
                "antwoord": [0, 1, 2],
                "uitleg": "De en het zijn bepaald, geen is ontkennend. 'Dat' wijst iets aan en is dus een aanwijzend voornaamwoord.",
            },
            {
                "opties": ["een", "het", "geen", "zulke"],
                "antwoord": [0, 1, 2],
                "uitleg": "Een is onbepaald, het is bepaald, geen is ontkennend. 'Zulke' wijst een soort aan en is een aanwijzend voornaamwoord.",
            },
        ],
        "'De' en 'het' zijn bepaalde lidwoorden.": [
            {
                "vraag": "'Een' is een onbepaald lidwoord.",
                "uitleg": "'Een' laat open om welke het gaat. 'De' en 'het' wijzen naar iets dat de lezer al kent.",
            },
            {
                "vraag": "'Geen' is een ontkennend lidwoord.",
                "uitleg": "Het Nederlands heeft drie soorten lidwoorden: bepaald, onbepaald en ontkennend. 'Geen' is de derde.",
            },
            {
                "vraag": "'Het' wijst naar iets dat de lezer al kent.",
                "uitleg": "Daarom heet het een bepaald lidwoord, net als 'de'. 'Een' laat het juist open.",
            },
        ],
        "In 'Oei, dat deed pijn!' is 'oei' een:": [
            {"vraag": "In 'Hè, wat jammer nu!' is 'hè' een:"},
            {"vraag": "In 'Bah, wat ruikt dat vies!' is 'bah' een:"},
            {"vraag": "In 'Hoera, we hebben gewonnen!' is 'hoera' een:"},
        ],
        "In 'De sleutel lag onder de mat', welk woord is het voorzetsel?": [
            {
                "vraag": "In 'De kat sprong over het hek', welk woord is het voorzetsel?",
                "opties": ["over", "het", "kat", "sprong"],
                "uitleg": "Een voorzetsel geeft een verhouding aan in plaats, tijd of richting: over, na, door, tegen.",
            },
            {
                "vraag": "In 'Hij zat tussen zijn twee zussen', welk woord is het voorzetsel?",
                "opties": ["tussen", "zijn", "zussen", "zat"],
                "uitleg": "Een voorzetsel geeft een verhouding aan in plaats, tijd of richting: tussen, na, door, tegen.",
            },
            {
                "vraag": "In 'Het pakje lag achter de deur', welk woord is het voorzetsel?",
                "opties": ["achter", "de", "pakje", "lag"],
                "uitleg": "Een voorzetsel geeft een verhouding aan in plaats, tijd of richting: achter, na, door, tegen.",
            },
        ],
        "Een bijvoeglijk naamwoord zegt altijd iets over een werkwoord.": [
            {
                "vraag": "Een bijwoord zegt altijd iets over een zelfstandig naamwoord.",
                "uitleg": "Een bijwoord zegt iets over een werkwoord, een bijvoeglijk naamwoord over een zelfstandig naamwoord.",
            },
            {
                "vraag": "In 'de snelle loper' is 'snelle' een bijwoord.",
                "uitleg": "Het zegt iets over 'loper', een zelfstandig naamwoord. Dus is het bijvoeglijk.",
            },
            {
                "vraag": "Een bijvoeglijk naamwoord en een bijwoord zijn hetzelfde.",
                "uitleg": "Het ene zegt iets over een zelfstandig naamwoord, het andere over een werkwoord of over de hele zin.",
            },
        ],
        "Welke woorden zijn voorzetsels?": [
            {
                "opties": ["in", "naast", "achter", "graag"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Graag' is een bijwoord: het zegt hoe iets gebeurt, niet waar iets zich bevindt.",
            },
            {
                "opties": ["door", "tegen", "boven", "vaak"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Vaak' is een bijwoord van tijd. Een voorzetsel geeft een verhouding aan in plaats, tijd of richting.",
            },
            {
                "opties": ["voor", "achter", "naast", "traag"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Traag' zegt hoe iets gebeurt en is dus een bijwoord, geen voorzetsel.",
            },
        ],
        "In 'Hij loopt snel', welke woordsoort is 'snel'?": [
            {
                "vraag": "In 'Zij zingt mooi', welke woordsoort is 'mooi'?",
                "uitleg": "Het zegt iets over het werkwoord 'zingt'. In 'een mooi lied' zegt hetzelfde woord iets over een naamwoord en is het bijvoeglijk.",
            },
            {
                "vraag": "In 'De motor draait stil', welke woordsoort is 'stil'?",
                "uitleg": "Het zegt iets over het werkwoord 'draait'. In 'een stille motor' is hetzelfde woord bijvoeglijk.",
            },
            {
                "vraag": "In 'Hij schrijft netjes', welke woordsoort is 'netjes'?",
                "uitleg": "Het zegt iets over het werkwoord 'schrijft', niet over een naamwoord.",
            },
        ],
        "In 'Gelukkig regende het niet', welke woordsoort is 'gelukkig'?": [
            {
                "vraag": "In 'Waarschijnlijk komt hij later', welke woordsoort is 'waarschijnlijk'?",
                "uitleg": "Het zegt iets over de hele zin, niet over een naamwoord. Zo'n woord is een bijwoord.",
            },
            {
                "vraag": "In 'Misschien regent het morgen', welke woordsoort is 'misschien'?",
                "uitleg": "Het zegt iets over de hele zin, niet over één naamwoord. Dat maakt het een bijwoord.",
            },
            {
                "vraag": "In 'Hopelijk lukt het deze keer', welke woordsoort is 'hopelijk'?",
                "uitleg": "Het zegt iets over de hele zin. Een woord dat dat doet, is een bijwoord.",
            },
        ],
        "Welk woord in 'Er stonden veertien fietsen in het rek' is een telwoord?": [
            {
                "vraag": "Welk woord in 'Er lagen zeventien brieven op de tafel' is een telwoord?",
                "opties": ["zeventien", "brieven", "tafel", "lagen"],
            },
            {
                "vraag": "Welk woord in 'Hij bestelde drie broodjes aan de kassa' is een telwoord?",
                "opties": ["drie", "broodjes", "kassa", "bestelde"],
            },
            {
                "vraag": "Welk woord in 'De zaal telde tachtig stoelen' is een telwoord?",
                "opties": ["tachtig", "stoelen", "zaal", "telde"],
            },
        ],
        "Welke van deze woorden zijn bijwoorden?": [
            {
                "opties": ["straks", "hier", "nauwelijks", "rood"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bijwoorden zeggen iets over tijd, plaats, mate of manier. 'Rood' hoort bij een naamwoord en is bijvoeglijk.",
            },
            {
                "opties": ["morgen", "ginder", "amper", "blauw"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bijwoorden zeggen iets over tijd, plaats, mate of manier. 'Blauw' hoort bij een naamwoord en is bijvoeglijk.",
            },
            {
                "opties": ["vaak", "overal", "erg", "geel"],
                "antwoord": [0, 1, 2],
                "uitleg": "Bijwoorden zeggen iets over tijd, plaats, mate of manier. 'Geel' hoort bij een naamwoord en is bijvoeglijk.",
            },
        ],
        "In 'Ik wacht al een half uur op de bus', welk woord is een voorzetsel?": [
            {
                "vraag": "In 'Zij kijkt al een uur naar het scherm', welk woord is een voorzetsel?",
                "opties": ["naar", "al", "uur", "kijkt"],
                "uitleg": "'Naar het scherm' is een voorzetselgroep. 'Al' is hier een bijwoord.",
            },
            {
                "vraag": "In 'Hij denkt de hele week aan die wedstrijd', welk woord is een voorzetsel?",
                "opties": ["aan", "hele", "week", "denkt"],
                "uitleg": "'Aan die wedstrijd' is een voorzetselgroep. 'Hele' is hier een bijvoeglijk naamwoord.",
            },
            {
                "vraag": "In 'We praatten gisteren lang over die film', welk woord is een voorzetsel?",
                "opties": ["over", "lang", "gisteren", "praatten"],
                "uitleg": "'Over die film' is een voorzetselgroep. 'Lang' en 'gisteren' zijn hier bijwoorden.",
            },
        ],
        "Welke woordsoort ontbreekt in 'kat sliep op mat'?": [
            {
                "vraag": "Welke woordsoort ontbreekt in 'hond blafte naar postbode'?",
                "uitleg": "'De hond blafte naar de postbode' is de gewone Nederlandse zin. Zonder lidwoorden klinkt hij als telegramstijl.",
            },
            {
                "vraag": "Welke woordsoort ontbreekt in 'jongen fietste door straat'?",
                "uitleg": "'De jongen fietste door de straat' is de gewone Nederlandse zin. Zonder lidwoorden klinkt hij als telegramstijl.",
            },
            {
                "vraag": "Welke woordsoort ontbreekt in 'trein stopte in station'?",
                "uitleg": "'De trein stopte in het station' is de gewone Nederlandse zin. Zonder lidwoorden klinkt hij als telegramstijl.",
            },
        ],
    },
    "De woordsoorten op een rij — deel 2": {
        "In 'Hij wast zich elke ochtend', wat is 'zich'?": [
            {
                "vraag": "In 'Zij vergist zich vaak', wat is 'zich'?",
                "uitleg": "De handeling keert terug naar het onderwerp zelf: zij vergist zichzelf.",
            },
            {
                "vraag": "In 'De kat likt zich schoon', wat is 'zich'?",
                "uitleg": "De handeling keert terug naar het onderwerp zelf: de kat likt zichzelf.",
            },
            {
                "vraag": "In 'Hij scheert zich elke dag', wat is 'zich'?",
                "uitleg": "De handeling keert terug naar het onderwerp zelf: hij scheert zichzelf.",
            },
        ],
        "In 'De twee broers groetten elkaar', wat is 'elkaar'?": [
            {
                "vraag": "In 'De twee ploegen feliciteerden elkaar', wat is 'elkaar'?",
                "uitleg": "Wederkerig betekent over en weer: de ene feliciteert de andere én omgekeerd.",
            },
            {
                "vraag": "In 'Mijn zussen helpen elkaar altijd', wat is 'elkaar'?",
                "uitleg": "Wederkerig betekent over en weer: de ene helpt de andere én omgekeerd.",
            },
            {
                "vraag": "In 'De buren zwaaien naar elkaar', wat is 'elkaar'?",
                "uitleg": "Wederkerig betekent over en weer: de ene zwaait naar de andere én omgekeerd.",
            },
        ],
        "Hoe noem je woorden als 'mijn', 'jouw' en 'hun'?": [
            {
                "vraag": "Hoe noem je woorden als 'ons', 'jullie' en 'haar'?",
                "uitleg": "Ze zeggen bij wie iets hoort: ons huis, jullie boeken, haar fiets.",
            },
            {
                "vraag": "Hoe noem je woorden als 'mijn', 'zijn' en 'onze'?",
                "uitleg": "Ze zeggen bij wie iets hoort: mijn jas, zijn tas, onze klas.",
            },
            {
                "vraag": "Hoe noem je woorden als 'uw', 'zijn' en 'hun'?",
                "uitleg": "Ze zeggen bij wie iets hoort. Let op: 'hun' als bezittelijk voornaamwoord is correct, 'hun' als onderwerp niet.",
            },
        ],
        "'Deze' en 'die' zijn aanwijzende voornaamwoorden.": [
            {
                "vraag": "'Dit' en 'dat' zijn aanwijzende voornaamwoorden.",
                "uitleg": "Ze wijzen iets aan: dit voor wat dichtbij is, dat voor wat verder weg staat.",
            },
            {
                "vraag": "'Zulke' is een aanwijzend voornaamwoord.",
                "uitleg": "Het wijst een soort aan: zulke schoenen, zulke verhalen.",
            },
            {
                "vraag": "'Deze' wijst naar iets wat dichtbij is.",
                "uitleg": "Deze en dit staan voor wat dichtbij is, die en dat voor wat verder weg staat.",
            },
        ],
        "Welke woorden zijn persoonlijke voornaamwoorden?": [
            {
                "opties": ["jij", "hem", "zij", "jouw"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Jouw' zegt van wie iets is en is dus bezittelijk. De drie andere vervangen een persoon.",
            },
            {
                "opties": ["wij", "hen", "u", "onze"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Onze' zegt van wie iets is en is dus bezittelijk. De drie andere vervangen een persoon.",
            },
            {
                "opties": ["ik", "mij", "hij", "mijn"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Mijn' zegt van wie iets is en is dus bezittelijk. De drie andere vervangen een persoon.",
            },
        ],
        "In 'Het boek dat ik gisteren las, was spannend', wat is 'dat'?": [
            {
                "vraag": "In 'De film die we zagen, duurde drie uur', wat is 'die'?",
                "uitleg": "Het verwijst terug naar 'de film' én begint tegelijk een bijzin. Dat dubbele werk doet alleen een betrekkelijk voornaamwoord.",
            },
            {
                "vraag": "In 'De man die daar woont, is leraar', wat is 'die'?",
                "uitleg": "Het verwijst terug naar 'de man' én begint tegelijk een bijzin. Dat dubbele werk doet alleen een betrekkelijk voornaamwoord.",
            },
            {
                "vraag": "In 'Het huis dat leegstaat, wordt verkocht', wat is 'dat'?",
                "uitleg": "Het verwijst terug naar 'het huis' én begint tegelijk een bijzin. Dat dubbele werk doet alleen een betrekkelijk voornaamwoord.",
            },
        ],
        "'Men' is een persoonlijk voornaamwoord.": [
            {
                "vraag": "'Iemand' is een persoonlijk voornaamwoord.",
                "uitleg": "'Iemand' is onbepaald, net als niemand, iedereen, alles en men. Het noemt geen bepaalde persoon.",
            },
            {
                "vraag": "'Niemand' is een persoonlijk voornaamwoord.",
                "uitleg": "'Niemand' is onbepaald, net als iemand, iedereen, alles en men. Het noemt geen bepaalde persoon.",
            },
            {
                "vraag": "'Alles' is een persoonlijk voornaamwoord.",
                "uitleg": "'Alles' is onbepaald, net als iemand, niemand, iedereen en men. Het noemt geen bepaalde persoon.",
            },
        ],
        "In 'Wie heeft dat raam opengezet?', wat is 'wie'?": [
            {
                "vraag": "In 'Wat staat daar in de gang?', wat is 'wat'?",
                "uitleg": "Het begint een vraag en vervangt datgene waarnaar je vraagt. Dus is het vragend.",
            },
            {
                "vraag": "In 'Welke trein moeten we hebben?', wat is 'welke'?",
                "uitleg": "Het begint een vraag en vervangt datgene waarnaar je vraagt. Dus is het vragend.",
            },
            {
                "vraag": "In 'Wie belde er daarnet aan?', wat is 'wie'?",
                "uitleg": "In 'de man wie ik zag' zou 'wie' betrekkelijk zijn. Hier begint het een vraag, dus is het vragend.",
            },
        ],
        "Hoe noem je 'me' in de zin 'Ik was me elke ochtend'?": [
            {
                "vraag": "Hoe noem je 'je' in de zin 'Jij vergist je'?",
                "uitleg": "In de eerste en tweede persoon zien wederkerende voornaamwoorden eruit als persoonlijke: me, je, ons. Kijk naar wat ze doen, niet naar hun vorm.",
            },
            {
                "vraag": "Hoe noem je 'ons' in de zin 'Wij haasten ons'?",
                "uitleg": "In de eerste en tweede persoon zien wederkerende voornaamwoorden eruit als persoonlijke: me, je, ons. Kijk naar wat ze doen, niet naar hun vorm.",
            },
            {
                "vraag": "Hoe noem je 'me' in de zin 'Ik schaam me een beetje'?",
                "uitleg": "De handeling keert terug naar het onderwerp: ik schaam mezelf. Dat maakt het wederkerend.",
            },
        ],
        "In 'Die van mij is groter', hoe is 'die' gebruikt?": [
            {
                "vraag": "In 'Deze van mij is nieuwer', hoe is 'deze' gebruikt?",
                "opties": [
                    "zelfstandig, want het vervangt een naamwoord",
                    "bijvoeglijk, want het staat bij een naamwoord",
                    "als voegwoord, want het verbindt twee zinnen",
                    "als bijwoord, want het zegt iets over 'nieuwer'",
                ],
            },
            {
                "vraag": "In 'Dat van jou is ouder', hoe is 'dat' gebruikt?",
                "opties": [
                    "zelfstandig, want het vervangt een naamwoord",
                    "bijvoeglijk, want het staat bij een naamwoord",
                    "als voegwoord, want het verbindt twee zinnen",
                    "als bijwoord, want het zegt iets over 'ouder'",
                ],
            },
            {
                "vraag": "In 'Die van ons is sneller', hoe is 'die' gebruikt?",
                "opties": [
                    "zelfstandig, want het vervangt een naamwoord",
                    "bijvoeglijk, want het staat bij een naamwoord",
                    "als voegwoord, want het verbindt twee zinnen",
                    "als bijwoord, want het zegt iets over 'sneller'",
                ],
            },
        ],
        "In welke zinnen staat een aanwijzend voornaamwoord?": [
            {
                "opties": [
                    "Dit boek lees ik al een week.",
                    "Die daar wil ik graag hebben.",
                    "Zulke verhalen geloof ik niet.",
                    "Wat doe jij hier zo laat?",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Dit, die en zulke wijzen aan. 'Wat' stelt een vraag en is dus vragend.",
            },
            {
                "opties": [
                    "Dat gebouw staat er al eeuwen.",
                    "Deze neem ik mee naar huis.",
                    "Zulke dagen vergeet je niet.",
                    "Welke wil jij hebben?",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Dat, deze en zulke wijzen aan. 'Welke' stelt een vraag en is dus vragend.",
            },
            {
                "opties": [
                    "Die fiets is van mijn zus.",
                    "Dit vind ik veel mooier.",
                    "Zulke schoenen draagt niemand nog.",
                    "Wie heeft dat gezegd?",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Die, dit en zulke wijzen aan. 'Wie' stelt een vraag en is dus vragend.",
            },
        ],
        "In 'Er staat iemand aan de deur', wat is 'iemand'?": [
            {
                "vraag": "In 'Er is niemand thuis', wat is 'niemand'?",
                "uitleg": "Het gaat om een persoon die niet nader bepaald wordt. Net als iemand, iedereen, alles en men.",
            },
            {
                "vraag": "In 'Iedereen was op tijd', wat is 'iedereen'?",
                "uitleg": "Het gaat om personen die niet nader bepaald worden. Net als iemand, niemand, alles en men.",
            },
            {
                "vraag": "In 'Er ligt iets op de trap', wat is 'iets'?",
                "uitleg": "Het gaat om een ding dat niet nader bepaald wordt. Net als iemand, niemand, iedereen en alles.",
            },
        ],
    },
    "Werkwoorden, tijden en woordvorming — deel 1": {
        "In welke tijd staat 'Ik had de hele dag gelopen'?": [
            {
                "vraag": "In welke tijd staat 'Zij had haar huiswerk al gemaakt'?",
                "uitleg": "Voltooid omdat er een deelwoord staat, verleden omdat het hulpwerkwoord 'had' in de verleden tijd staat.",
            },
            {
                "vraag": "In welke tijd staat 'Wij hadden de trein net gemist'?",
                "uitleg": "Voltooid omdat er een deelwoord staat, verleden omdat het hulpwerkwoord 'hadden' in de verleden tijd staat.",
            },
            {
                "vraag": "In welke tijd staat 'Hij was al vertrokken toen ik aankwam'?",
                "uitleg": "Voltooid omdat er een deelwoord staat, verleden omdat het hulpwerkwoord 'was' in de verleden tijd staat.",
            },
        ],
        "De imperatief is de aanvoegende wijs.": [
            {
                "vraag": "De imperatief is de aantonende wijs.",
                "uitleg": "De imperatief is de gebiedende wijs: 'Kom hier', 'Let op'. Hij heeft geen onderwerp bij zich.",
            },
            {
                "vraag": "De gebiedende wijs heeft altijd een onderwerp bij zich.",
                "uitleg": "'Kom hier' en 'Let op' hebben er geen. Dat is net wat de gebiedende wijs kenmerkt.",
            },
            {
                "vraag": "De infinitief is hetzelfde als de gebiedende wijs.",
                "uitleg": "De infinitief is 'lopen', de gebiedende wijs is 'loop'. Dat zijn twee verschillende vormen.",
            },
        ],
        "In 'Zij wordt verpleegkundige', welk soort werkwoord is 'wordt'?": [
            {
                "vraag": "In 'Hij blijft altijd rustig', welk soort werkwoord is 'blijft'?",
                "uitleg": "Het koppelt het onderwerp aan een woord dat iets over dat onderwerp zegt. Samen heet dat een naamwoordelijk gezegde.",
            },
            {
                "vraag": "In 'Die soep lijkt koud', welk soort werkwoord is 'lijkt'?",
                "uitleg": "Het koppelt het onderwerp aan een woord dat iets over dat onderwerp zegt. Samen heet dat een naamwoordelijk gezegde.",
            },
            {
                "vraag": "In 'Mijn zus is dierenarts', welk soort werkwoord is 'is'?",
                "uitleg": "Het koppelt het onderwerp aan een naamwoord dat iets over dat onderwerp zegt. Samen heet dat een naamwoordelijk gezegde.",
            },
        ],
        "In 'Hij heeft zijn boterhammen opgegeten', wat is 'heeft'?": [
            {
                "vraag": "In 'Zij heeft de brief geschreven', wat is 'heeft'?",
                "uitleg": "'Heeft' helpt hier de voltooide tijd vormen. In 'Zij heeft een fiets' is hetzelfde woord wel zelfstandig werkwoord.",
            },
            {
                "vraag": "In 'Wij hebben de film al gezien', wat is 'hebben'?",
                "uitleg": "'Hebben' helpt hier de voltooide tijd vormen. In 'Wij hebben een hond' is hetzelfde woord wel zelfstandig werkwoord.",
            },
            {
                "vraag": "In 'Hij is naar huis gefietst', wat is 'is'?",
                "uitleg": "'Is' helpt hier de voltooide tijd vormen. In 'Hij is ziek' is hetzelfde woord koppelwerkwoord.",
            },
        ],
        "De stam van een werkwoord is hetzelfde als de infinitief.": [
            {
                "vraag": "De stam van 'wandelen' is 'wandelen'.",
                "uitleg": "De stam krijg je door -en van de infinitief te halen: wandelen wordt wandel. Daarop bouw je de vervoeging.",
            },
            {
                "vraag": "De stam van 'werken' is 'werkt'.",
                "uitleg": "De stam is 'werk'. 'Werkt' is de stam plus de uitgang -t.",
            },
            {
                "vraag": "De stam van 'lopen' is 'lopen'.",
                "uitleg": "De stam is 'loop'. Je krijgt hem door -en van de infinitief te halen.",
            },
        ],
        "In welke tijd staat 'Wij werkten de hele zomer'?": [
            {
                "vraag": "In welke tijd staat 'Zij fietste elke dag naar school'?",
                "uitleg": "Er staat geen deelwoord bij, dus onvoltooid. De vorm 'fietste' is verleden tijd.",
            },
            {
                "vraag": "In welke tijd staat 'Hij las het hele boek uit'?",
                "uitleg": "Er staat geen deelwoord bij, dus onvoltooid. De vorm 'las' is verleden tijd.",
            },
            {
                "vraag": "In welke tijd staat 'Wij zongen het hele lied mee'?",
                "uitleg": "Er staat geen deelwoord bij, dus onvoltooid. De vorm 'zongen' is verleden tijd.",
            },
        ],
        "Het voltooid deelwoord van een zwak werkwoord eindigt op -d of -t.": [
            {
                "vraag": "Het voltooid deelwoord van 'werken' is 'gewerkt'.",
                "uitleg": "Werken is zwak, dus komt er -t bij: gewerkt, net als gehoord en gebeld.",
            },
            {
                "vraag": "Sterke werkwoorden veranderen van klinker in het voltooid deelwoord.",
                "uitleg": "Gelopen, gezongen, gevonden. Zwakke werkwoorden krijgen gewoon -d of -t.",
            },
            {
                "vraag": "Het voltooid deelwoord van 'horen' is 'gehoord'.",
                "uitleg": "Horen is zwak, dus komt er -d bij: gehoord, net als gewerkt en gebeld.",
            },
        ],
        "In welke tijd staat 'Zij zal morgen komen'?": [
            {
                "vraag": "In welke tijd staat 'Wij zullen volgende week verhuizen'?",
                "uitleg": "'Zullen' plus infinitief maakt de toekomende tijd. Er staat geen deelwoord bij, dus onvoltooid.",
            },
            {
                "vraag": "In welke tijd staat 'Hij zal het straks uitleggen'?",
                "uitleg": "'Zullen' plus infinitief maakt de toekomende tijd. Er staat geen deelwoord bij, dus onvoltooid.",
            },
            {
                "vraag": "In welke tijd staat 'Ik zal je morgen bellen'?",
                "uitleg": "'Zullen' plus infinitief maakt de toekomende tijd. Er staat geen deelwoord bij, dus onvoltooid.",
            },
        ],
        "Welke vormen zijn voltooide deelwoorden?": [
            {
                "opties": ["gehoord", "gezongen", "gevonden", "horen"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Horen' is de infinitief. De drie andere beginnen met ge- en horen bij een voltooide tijd.",
            },
            {
                "opties": ["gebeld", "geschreven", "gedronken", "bellen"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Bellen' is de infinitief. De drie andere beginnen met ge- en horen bij een voltooide tijd.",
            },
            {
                "opties": ["gemaakt", "gekregen", "geweest", "maken"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Maken' is de infinitief. De drie andere beginnen met ge- en horen bij een voltooide tijd.",
            },
        ],
        "Welke zin is correct gespeld?": [
            {
                "opties": [
                    "Zij vindt dat geen probleem.",
                    "Zij vind dat geen probleem.",
                    "Zij vindt dat geen probleem gevonden.",
                    "Zij vinden dat geen probleem.",
                ],
                "uitleg": "Derde persoon enkelvoud krijgt stam plus t: vind plus t wordt 'vindt'.",
            },
            {
                "opties": [
                    "Hij houdt van aardappelen.",
                    "Hij houd van aardappelen.",
                    "Hij houdt van aardappelen gehouden.",
                    "Hij houden van aardappelen.",
                ],
                "uitleg": "Derde persoon enkelvoud krijgt stam plus t: houd plus t wordt 'houdt'.",
            },
            {
                "opties": [
                    "Zij rijdt elke dag naar het werk.",
                    "Zij rijd elke dag naar het werk.",
                    "Zij rijdt elke dag naar het werk gereden.",
                    "Zij rijden elke dag naar het werk.",
                ],
                "uitleg": "Derde persoon enkelvoud krijgt stam plus t: rijd plus t wordt 'rijdt'.",
            },
        ],
        "Welke vraagzin is correct gespeld?": [
            {
                "opties": [
                    "Vind je dat niet vervelend?",
                    "Vindt je dat niet vervelend?",
                    "Vindt jou dat niet vervelend?",
                    "Vind jou dat niet vervelend?",
                ],
                "uitleg": "Bij 'je' of 'jij' achter de persoonsvorm valt de -t weg. Dat heet inversie.",
            },
            {
                "opties": [
                    "Houd jij van pannenkoeken?",
                    "Houdt jij van pannenkoeken?",
                    "Houdt jou van pannenkoeken?",
                    "Houd jou van pannenkoeken?",
                ],
                "uitleg": "Bij 'je' of 'jij' achter de persoonsvorm valt de -t weg. Dat heet inversie.",
            },
            {
                "opties": [
                    "Rijd je zelf naar huis?",
                    "Rijdt je zelf naar huis?",
                    "Rijdt jou zelf naar huis?",
                    "Rijd jou zelf naar huis?",
                ],
                "uitleg": "Bij 'je' of 'jij' achter de persoonsvorm valt de -t weg. Dat heet inversie.",
            },
        ],
        "In 'Ik heb het boek helemaal uitgelezen', welk werkwoord is het zelfstandig werkwoord?": [
            {
                "vraag": "In 'Zij heeft de brief zorgvuldig geschreven', welk werkwoord is het zelfstandig werkwoord?",
                "opties": ["geschreven", "heeft", "de", "zorgvuldig"],
                "uitleg": "'Heeft' is hier alleen hulpwerkwoord. De betekenis van de zin zit in 'geschreven'.",
            },
            {
                "vraag": "In 'Wij hebben de hele avond gewerkt', welk werkwoord is het zelfstandig werkwoord?",
                "opties": ["gewerkt", "hebben", "de", "avond"],
                "uitleg": "'Hebben' is hier alleen hulpwerkwoord. De betekenis van de zin zit in 'gewerkt'.",
            },
            {
                "vraag": "In 'Hij is naar de winkel gefietst', welk werkwoord is het zelfstandig werkwoord?",
                "opties": ["gefietst", "is", "naar", "winkel"],
                "uitleg": "'Is' is hier alleen hulpwerkwoord. De betekenis van de zin zit in 'gefietst'.",
            },
        ],
    },
    "Werkwoorden, tijden en woordvorming — deel 2": {
        "Wat voor woord is 'boekenkast'?": [
            {
                "vraag": "Wat voor woord is 'tafelpoot'?",
                "uitleg": "Twee bestaande woorden, tafel en poot, worden aan elkaar geschreven. Dat is een samenstelling.",
            },
            {
                "vraag": "Wat voor woord is 'regenjas'?",
                "uitleg": "Twee bestaande woorden, regen en jas, worden aan elkaar geschreven. Dat is een samenstelling.",
            },
            {
                "vraag": "Wat voor woord is 'schoolbord'?",
                "uitleg": "Twee bestaande woorden, school en bord, worden aan elkaar geschreven. Dat is een samenstelling.",
            },
        ],
        "Wat voor woord is 'onvriendelijk'?": [
            {
                "vraag": "Wat voor woord is 'onduidelijk'?",
                "uitleg": "'On-' is geen zelfstandig woord maar een voorvoegsel. Een woord dat met een voor- of achtervoegsel gevormd is, heet een afleiding.",
            },
            {
                "vraag": "Wat voor woord is 'leesbaar'?",
                "uitleg": "'-baar' is geen zelfstandig woord maar een achtervoegsel. Een woord dat met een voor- of achtervoegsel gevormd is, heet een afleiding.",
            },
            {
                "vraag": "Wat voor woord is 'schoonheid'?",
                "uitleg": "'-heid' is geen zelfstandig woord maar een achtervoegsel. Een woord dat met een voor- of achtervoegsel gevormd is, heet een afleiding.",
            },
        ],
        "Bij een samenstelling zet je twee bestaande woorden aan elkaar.": [
            {
                "vraag": "'Voetbalveld' is een samenstelling.",
                "uitleg": "Voetbal en veld kunnen allebei los bestaan. Dat maakt het een samenstelling.",
            },
            {
                "vraag": "Allebei de delen van een samenstelling kunnen los bestaan.",
                "uitleg": "Tafel en poot, voetbal en veld. Bij een afleiding kan één deel dat net niet.",
            },
            {
                "vraag": "'Regenjas' is een samenstelling.",
                "uitleg": "Regen en jas kunnen allebei los bestaan. Dat maakt het een samenstelling.",
            },
        ],
        "Welke woorden zijn samenstellingen?": [
            {
                "opties": ["schoolbord", "deurklink", "raamkozijn", "leesbaar"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Leesbaar' is gevormd met het achtervoegsel -baar en is dus een afleiding.",
            },
            {
                "opties": ["boekenkast", "pannenkoek", "fietspad", "schoonheid"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Schoonheid' is gevormd met het achtervoegsel -heid en is dus een afleiding.",
            },
            {
                "opties": ["tandarts", "keukentafel", "krantenwinkel", "onmogelijk"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Onmogelijk' is gevormd met het voorvoegsel on- en is dus een afleiding.",
            },
        ],
        "Wat is het voorvoegsel in 'herlezen'?": [
            {
                "vraag": "Wat is het voorvoegsel in 'verdwalen'?",
                "opties": ["ver-", "-dwalen", "-en", "dw-"],
                "uitleg": "'Ver-' kan niet alleen staan, dus het is een voorvoegsel en geen woord.",
            },
            {
                "vraag": "Wat is het voorvoegsel in 'ontdekken'?",
                "opties": ["ont-", "-dekken", "-en", "de-"],
                "uitleg": "'Ont-' kan niet alleen staan, dus het is een voorvoegsel en geen woord.",
            },
            {
                "vraag": "Wat is het voorvoegsel in 'bespreken'?",
                "opties": ["be-", "-spreken", "-en", "sp-"],
                "uitleg": "'Be-' kan niet alleen staan, dus het is een voorvoegsel en geen woord.",
            },
        ],
        "'Onmogelijk' is een samenstelling.": [
            {
                "vraag": "'Onduidelijk' is een samenstelling.",
                "uitleg": "Het is een afleiding: er komt een voorvoegsel bij een bestaand woord. Bij een samenstelling zijn allebei de delen zelfstandige woorden.",
            },
            {
                "vraag": "'Schoonheid' is een samenstelling.",
                "uitleg": "Het is een afleiding: er komt een achtervoegsel bij een bestaand woord. Bij een samenstelling zijn allebei de delen zelfstandige woorden.",
            },
            {
                "vraag": "'Leesbaar' is een samenstelling.",
                "uitleg": "Het is een afleiding: '-baar' is geen zelfstandig woord. Bij een samenstelling zijn allebei de delen dat wel.",
            },
        ],
        "Welke meervouden zijn correct?": [
            {
                "opties": ["schepen", "steden", "eieren", "tafelens"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het meervoud van tafel is tafels. Een meervoud krijgt nooit twee uitgangen tegelijk.",
            },
            {
                "opties": ["musea", "koeien", "bladeren", "ramens"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het meervoud van raam is ramen. Een meervoud krijgt nooit twee uitgangen tegelijk.",
            },
            {
                "opties": ["runderen", "kalveren", "liederen", "deurens"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het meervoud van deur is deuren. Een meervoud krijgt nooit twee uitgangen tegelijk.",
            },
        ],
        "Wat is het verkleinwoord van 'koning'?": [
            {
                "vraag": "Wat is het verkleinwoord van 'woning'?",
                "opties": ["woninkje", "woningje", "woningtje", "woningetje"],
                "uitleg": "Na -ing wordt de g een k en volgt -je. Dezelfde regel geldt bij koning en leerling.",
            },
            {
                "vraag": "Wat is het verkleinwoord van 'leerling'?",
                "opties": ["leerlinkje", "leerlingje", "leerlingtje", "leerlingetje"],
                "uitleg": "Na -ing wordt de g een k en volgt -je. Dezelfde regel geldt bij koning en woning.",
            },
            {
                "vraag": "Wat is het verkleinwoord van 'ketting'?",
                "opties": ["kettinkje", "kettingje", "kettingtje", "kettingetje"],
                "uitleg": "Na -ing wordt de g een k en volgt -je. Dezelfde regel geldt bij koning en woning.",
            },
        ],
        "In welk woord zit een tussenklank?": [
            {
                "opties": ["zonnebloem", "deurklink", "fietspad", "tandarts"],
                "uitleg": "Tussen zon en bloem staat -ne-. De drie andere samenstellingen plakken de twee delen rechtstreeks aan elkaar.",
            },
            {
                "opties": ["krantenwinkel", "schoolbord", "regenjas", "keukentafel"],
                "uitleg": "Tussen krant en winkel staat -en-. De drie andere samenstellingen plakken de twee delen rechtstreeks aan elkaar.",
            },
            {
                "opties": ["paardenstal", "raamkozijn", "fietspad", "tandarts"],
                "uitleg": "Tussen paard en stal staat -en-. De drie andere samenstellingen plakken de twee delen rechtstreeks aan elkaar.",
            },
        ],
        "Welke woorden zijn afleidingen?": [
            {
                "opties": ["vriendelijk", "onmogelijk", "verdwalen", "tafelpoot"],
                "antwoord": [0, 1, 2],
                "uitleg": "Tafelpoot is een samenstelling van twee echte woorden. De drie andere gebruiken een voor- of achtervoegsel.",
            },
            {
                "opties": ["bruikbaar", "onduidelijk", "herlezen", "schoolbord"],
                "antwoord": [0, 1, 2],
                "uitleg": "Schoolbord is een samenstelling van twee echte woorden. De drie andere gebruiken een voor- of achtervoegsel.",
            },
            {
                "opties": ["duidelijkheid", "bespreken", "ongeduldig", "fietspad"],
                "antwoord": [0, 1, 2],
                "uitleg": "Fietspad is een samenstelling van twee echte woorden. De drie andere gebruiken een voor- of achtervoegsel.",
            },
        ],
        "Wat is het meervoud van 'lid'?": [
            {
                "vraag": "Wat is het meervoud van 'schip'?",
                "opties": ["schepen", "schippen", "schips", "schipperen"],
                "uitleg": "Een handvol woorden verandert van klinker in het meervoud: schip wordt schepen, lid wordt leden, stad wordt steden.",
            },
            {
                "vraag": "Wat is het meervoud van 'stad'?",
                "opties": ["steden", "stadden", "stads", "stadderen"],
                "uitleg": "Een handvol woorden verandert van klinker in het meervoud: stad wordt steden, lid wordt leden, schip wordt schepen.",
            },
            {
                "vraag": "Wat is het meervoud van 'smid'?",
                "opties": ["smeden", "smidden", "smids", "smidderen"],
                "uitleg": "Een handvol woorden verandert van klinker in het meervoud: smid wordt smeden, lid wordt leden, schip wordt schepen.",
            },
        ],
        "Welk woord is géén samenstelling?": [
            {
                "opties": ["onmogelijk", "schoolbord", "tafelpoot", "fietspad"],
                "uitleg": "Onmogelijk is een afleiding: on- plus mogelijk. Er komt geen tweede woord bij.",
            },
            {
                "opties": ["leesbaar", "deurklink", "raamkozijn", "tandarts"],
                "uitleg": "Leesbaar is een afleiding: lees plus -baar. '-baar' is geen zelfstandig woord.",
            },
            {
                "opties": ["schoonheid", "keukentafel", "zonnebril", "krantenwinkel"],
                "uitleg": "Schoonheid is een afleiding: schoon plus -heid. Er komt geen tweede woord bij.",
            },
        ],
    },
    "Zinsdelen en samengestelde zinnen — deel 1": {
        "In 'De postbode bracht mijn oma een pakje', wat is het lijdend voorwerp?": [
            {
                "vraag": "In 'De juf gaf de leerlingen een opdracht', wat is het lijdend voorwerp?",
                "opties": ["een opdracht", "de leerlingen", "de juf", "gaf"],
                "uitleg": "Vraag: wie of wat gaf de juf? Een opdracht. 'De leerlingen' zijn de ontvangers en dus meewerkend voorwerp.",
            },
            {
                "vraag": "In 'Mijn buurman leende mij zijn ladder', wat is het lijdend voorwerp?",
                "opties": ["zijn ladder", "mijn buurman", "mij", "leende"],
                "uitleg": "Vraag: wie of wat leende mijn buurman? Zijn ladder. 'Mij' is de ontvanger en dus meewerkend voorwerp.",
            },
            {
                "vraag": "In 'De trainer beloofde de ploeg een beker', wat is het lijdend voorwerp?",
                "opties": ["een beker", "de ploeg", "de trainer", "beloofde"],
                "uitleg": "Vraag: wie of wat beloofde de trainer? Een beker. 'De ploeg' is de ontvanger en dus meewerkend voorwerp.",
            },
        ],
        "Wat is het gezegde in 'De kinderen zijn moe'?": [
            {
                "vraag": "Wat is het gezegde in 'De soep is koud'?",
                "opties": [
                    "is koud, een naamwoordelijk gezegde",
                    "is, een werkwoordelijk gezegde",
                    "koud, een bijwoordelijke bepaling",
                    "de soep is, een onderwerp met persoonsvorm",
                ],
            },
            {
                "vraag": "Wat is het gezegde in 'Mijn broer wordt leraar'?",
                "opties": [
                    "wordt leraar, een naamwoordelijk gezegde",
                    "wordt, een werkwoordelijk gezegde",
                    "leraar, een bijwoordelijke bepaling",
                    "mijn broer wordt, een onderwerp met persoonsvorm",
                ],
            },
            {
                "vraag": "Wat is het gezegde in 'Het weer blijft slecht'?",
                "opties": [
                    "blijft slecht, een naamwoordelijk gezegde",
                    "blijft, een werkwoordelijk gezegde",
                    "slecht, een bijwoordelijke bepaling",
                    "het weer blijft, een onderwerp met persoonsvorm",
                ],
            },
        ],
        "Het gezegde van 'Zij is verpleegkundige' is naamwoordelijk.": [
            {
                "vraag": "Het gezegde van 'Mijn broer wordt leraar' is naamwoordelijk.",
                "uitleg": "'Wordt' is een koppelwerkwoord en 'leraar' zegt iets over het onderwerp. Samen vormen ze een naamwoordelijk gezegde.",
            },
            {
                "vraag": "Het gezegde van 'De soep blijft warm' is naamwoordelijk.",
                "uitleg": "'Blijft' is een koppelwerkwoord en 'warm' zegt iets over het onderwerp. Samen vormen ze een naamwoordelijk gezegde.",
            },
            {
                "vraag": "Bij een koppelwerkwoord is het gezegde naamwoordelijk.",
                "uitleg": "Zijn, worden en blijven koppelen het onderwerp aan een woord dat er iets over zegt.",
            },
        ],
        "In 'Hij wacht al een uur op de trein', wat is 'op de trein'?": [
            {
                "vraag": "In 'Zij rekent op haar vrienden', wat is 'op haar vrienden'?",
                "uitleg": "Het voorzetsel ligt vast bij het werkwoord: je rekent óp iemand. Je kan het niet vervangen door 'onder' of 'naast'.",
            },
            {
                "vraag": "In 'Wij twijfelen aan zijn verhaal', wat is 'aan zijn verhaal'?",
                "uitleg": "Het voorzetsel ligt vast bij het werkwoord: je twijfelt áán iets. Je kan het niet zomaar vervangen.",
            },
            {
                "vraag": "In 'Hij denkt vaak aan die zomer', wat is 'aan die zomer'?",
                "uitleg": "Het voorzetsel ligt vast bij het werkwoord: je denkt áán iets. Je kan het niet zomaar vervangen.",
            },
        ],
        "Een bijwoordelijke bepaling is altijd verplicht in de zin.": [
            {
                "vraag": "Een bijwoordelijke bepaling kan je nooit weglaten.",
                "uitleg": "'Gisteren fietste ze naar school' blijft een zin zonder 'gisteren'. Ze is juist meestal weglaatbaar.",
            },
            {
                "vraag": "Elke zin moet een bijwoordelijke bepaling bevatten.",
                "uitleg": "'De hond blaft' is een volledige zin zonder bepaling.",
            },
            {
                "vraag": "Zonder bijwoordelijke bepaling is een zin onvolledig.",
                "uitleg": "Ze is juist meestal weglaatbaar. De persoonsvorm is het zinsdeel dat nooit mag ontbreken.",
            },
        ],
        "Hoeveel bijwoordelijke bepalingen staan er in 'Gisteren fietste ze door de regen naar school'?": [
            {
                "vraag": "Hoeveel bijwoordelijke bepalingen staan er in 'Vanmorgen liep hij door het park naar het station'?",
                "uitleg": "Vanmorgen (tijd), door het park (omstandigheid) en naar het station (richting). Alle drie kan je weglaten.",
            },
            {
                "vraag": "Hoeveel bijwoordelijke bepalingen staan er in 'Straks rijdt zij met de bus naar de markt'?",
                "uitleg": "Straks (tijd), met de bus (middel) en naar de markt (richting). Alle drie kan je weglaten.",
            },
            {
                "vraag": "Hoeveel bijwoordelijke bepalingen staan er in 'Gisteravond wandelden we in de regen naar huis'?",
                "uitleg": "Gisteravond (tijd), in de regen (omstandigheid) en naar huis (richting). Alle drie kan je weglaten.",
            },
        ],
        "Je vindt het onderwerp door te vragen: wie of wat plus de persoonsvorm.": [
            {
                "vraag": "In 'De hond blaft' vind je het onderwerp met de vraag: wie of wat blaft?",
                "uitleg": "Het antwoord is 'de hond'. Dat is het onderwerp.",
            },
            {
                "vraag": "Het onderwerp bepaalt de vorm van de persoonsvorm.",
                "uitleg": "Dat heet congruentie: 'de doos staat', 'de dozen staan'.",
            },
            {
                "vraag": "In 'De trein vertrekt' is 'de trein' het onderwerp.",
                "uitleg": "Wie of wat vertrekt? De trein. Diezelfde vraag met het onderwerp erachter geeft het lijdend voorwerp.",
            },
        ],
        "In 'De brief werd door de directeur ondertekend', wat is 'door de directeur'?": [
            {
                "vraag": "In 'Het raam werd door de wind opengeblazen', wat is 'door de wind'?",
                "uitleg": "Het onderwerp is 'het raam'. Wie of wat de handeling écht uitvoert, staat in de door-groep.",
            },
            {
                "vraag": "In 'De taart werd door mijn oma gebakken', wat is 'door mijn oma'?",
                "uitleg": "Het onderwerp is 'de taart'. Wie de handeling écht uitvoert, staat in de door-groep.",
            },
            {
                "vraag": "In 'Het plein werd door de gemeente heraangelegd', wat is 'door de gemeente'?",
                "uitleg": "Het onderwerp is 'het plein'. Wie de handeling écht uitvoert, staat in de door-groep.",
            },
        ],
        "Elk zinsdeel bestaat uit precies één woord.": [
            {
                "vraag": "Een zinsdeel bestaat altijd uit één woord.",
                "uitleg": "'De hond van de buren' is één zinsdeel van vijf woorden.",
            },
            {
                "vraag": "Een zinsdeel verplaats je woord per woord.",
                "uitleg": "Je verplaatst een zinsdeel altijd in zijn geheel. Daarmee toon je net aan dat het één zinsdeel is.",
            },
            {
                "vraag": "'De hond van de buren' zijn twee zinsdelen.",
                "uitleg": "Het is één zinsdeel van vijf woorden. Je verplaatst het altijd in zijn geheel.",
            },
        ],
        "In 'Mijn broer geeft zijn beste vriend een boek', wat is 'zijn beste vriend'?": [
            {
                "vraag": "In 'De juf geeft de nieuwe leerling een schrift', wat is 'de nieuwe leerling'?",
                "uitleg": "Je kan er 'aan' voor zetten: de juf geeft een schrift aan de nieuwe leerling. Dat is de proef voor het meewerkend voorwerp.",
            },
            {
                "vraag": "In 'Ik stuur mijn oma een kaartje', wat is 'mijn oma'?",
                "uitleg": "Je kan er 'aan' voor zetten: ik stuur een kaartje aan mijn oma. Dat is de proef voor het meewerkend voorwerp.",
            },
            {
                "vraag": "In 'Hij leent zijn buurman de ladder', wat is 'zijn buurman'?",
                "uitleg": "Je kan er 'aan' voor zetten: hij leent de ladder aan zijn buurman. Dat is de proef voor het meewerkend voorwerp.",
            },
        ],
        "Welke woordgroepen zijn bijwoordelijke bepalingen in 'Morgen ga ik met de fiets naar de markt'?": [
            {
                "vraag": "Welke woordgroepen zijn bijwoordelijke bepalingen in 'Straks rijdt hij met de auto naar het station'?",
                "opties": ["straks", "met de auto", "naar het station", "hij"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Hij' is het onderwerp. De drie andere zeggen wanneer, hoe en waarheen.",
            },
            {
                "vraag": "Welke woordgroepen zijn bijwoordelijke bepalingen in 'Vanavond loop ik met mijn hond door het park'?",
                "opties": ["vanavond", "met mijn hond", "door het park", "ik"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Ik' is het onderwerp. De drie andere zeggen wanneer, hoe en waarheen.",
            },
            {
                "vraag": "Welke woordgroepen zijn bijwoordelijke bepalingen in 'Morgen vertrekken wij met de trein naar zee'?",
                "opties": ["morgen", "met de trein", "naar zee", "wij"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Wij' is het onderwerp. De drie andere zeggen wanneer, hoe en waarheen.",
            },
        ],
        "In 'De hond van de buren blaft de hele nacht', wat is het onderwerp?": [
            {
                "vraag": "In 'De fiets van mijn zus staat buiten', wat is het onderwerp?",
                "opties": ["de fiets van mijn zus", "de fiets", "mijn zus", "buiten"],
                "uitleg": "Wie of wat staat buiten? De fiets van mijn zus. Dat hele stuk is het onderwerp.",
            },
            {
                "vraag": "In 'De buren van hiernaast verhuizen morgen', wat is het onderwerp?",
                "opties": ["de buren van hiernaast", "de buren", "hiernaast", "morgen"],
                "uitleg": "Wie of wat verhuist morgen? De buren van hiernaast. Dat hele stuk is het onderwerp.",
            },
            {
                "vraag": "In 'Het boek van de bibliotheek ligt op tafel', wat is het onderwerp?",
                "opties": ["het boek van de bibliotheek", "het boek", "de bibliotheek", "op tafel"],
                "uitleg": "Wie of wat ligt op tafel? Het boek van de bibliotheek. Dat hele stuk is het onderwerp.",
            },
        ],
    },
    "Zinsdelen en samengestelde zinnen — deel 2": {
        "In welke vorm staat 'De brief wordt door de secretaresse getypt'?": [
            {"vraag": "In welke vorm staat 'Het plein wordt door de gemeente heraangelegd'?"},
            {"vraag": "In welke vorm staat 'De ramen werden door de glazenwasser gelapt'?"},
            {"vraag": "In welke vorm staat 'Het pakje werd door de postbode bezorgd'?"},
        ],
        "Wat is de lijdende vorm van 'De hond bijt de postbode'?": [
            {
                "vraag": "Wat is de lijdende vorm van 'De kat vangt de muis'?",
                "opties": [
                    "De muis wordt door de kat gevangen.",
                    "De kat wordt door de muis gevangen.",
                    "De muis vangt de kat niet.",
                    "Door de kat vangt de muis.",
                ],
                "uitleg": "Het lijdend voorwerp 'de muis' wordt onderwerp, en het oude onderwerp komt in een door-groep te staan.",
            },
            {
                "vraag": "Wat is de lijdende vorm van 'De juf verbetert de toets'?",
                "opties": [
                    "De toets wordt door de juf verbeterd.",
                    "De juf wordt door de toets verbeterd.",
                    "De toets verbetert de juf niet.",
                    "Door de juf verbetert de toets.",
                ],
                "uitleg": "Het lijdend voorwerp 'de toets' wordt onderwerp, en het oude onderwerp komt in een door-groep te staan.",
            },
            {
                "vraag": "Wat is de lijdende vorm van 'De bakker bakt het brood'?",
                "opties": [
                    "Het brood wordt door de bakker gebakken.",
                    "De bakker wordt door het brood gebakken.",
                    "Het brood bakt de bakker niet.",
                    "Door de bakker bakt het brood.",
                ],
                "uitleg": "Het lijdend voorwerp 'het brood' wordt onderwerp, en het oude onderwerp komt in een door-groep te staan.",
            },
        ],
        "In een bijzin staat de persoonsvorm altijd op de tweede plaats.": [
            {
                "vraag": "In een bijzin staat de persoonsvorm op dezelfde plaats als in een hoofdzin.",
                "uitleg": "In een bijzin schuift de persoonsvorm juist naar achteren: 'omdat het de hele dag regende'.",
            },
            {
                "vraag": "In 'omdat het de hele dag regende' staat de persoonsvorm op plaats twee.",
                "uitleg": "Ze staat helemaal achteraan. Dat is net het kenmerk van een bijzin.",
            },
            {
                "vraag": "De persoonsvorm staat in elke zin op de tweede plaats.",
                "uitleg": "Dat geldt voor de hoofdzin. In een bijzin schuift ze naar achteren.",
            },
        ],
        "'Kom onmiddellijk hier!' Wat voor zin is dat?": [
            {"vraag": "'Let nu eens goed op!' Wat voor zin is dat?"},
            {"vraag": "'Doe die deur alsjeblieft dicht!' Wat voor zin is dat?"},
            {"vraag": "'Ga onmiddellijk naar boven!' Wat voor zin is dat?"},
        ],
        "In 'Ik blijf thuis omdat het regent', wat voor verband is er tussen de twee delen?": [
            {
                "vraag": "In 'Hij kwam te laat omdat de trein vertraging had', wat voor verband is er tussen de twee delen?",
                "uitleg": "'Omdat' is een onderschikkend voegwoord: het maakt van het tweede deel een bijzin.",
            },
            {
                "vraag": "In 'Wij wachten tot iedereen er is', wat voor verband is er tussen de twee delen?",
                "uitleg": "'Tot' is een onderschikkend voegwoord: het maakt van het tweede deel een bijzin.",
            },
            {
                "vraag": "In 'Zij zwijgt hoewel ze het beter weet', wat voor verband is er tussen de twee delen?",
                "uitleg": "'Hoewel' is een onderschikkend voegwoord: het maakt van het tweede deel een bijzin.",
            },
        ],
        "Welke woorden zijn nevenschikkende voegwoorden?": [
            {
                "opties": ["en", "of", "dus", "hoewel"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Hoewel' is onderschikkend. Een geheugensteun voor de nevenschikkende: en, maar, of, want, dus.",
            },
            {
                "opties": ["maar", "of", "want", "als"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Als' is onderschikkend. Een geheugensteun voor de nevenschikkende: en, maar, of, want, dus.",
            },
            {
                "opties": ["en", "want", "dus", "dat"],
                "antwoord": [0, 1, 2],
                "uitleg": "'Dat' is onderschikkend. Een geheugensteun voor de nevenschikkende: en, maar, of, want, dus.",
            },
        ],
        "Inversie betekent dat het onderwerp achter de persoonsvorm komt te staan.": [
            {
                "vraag": "In 'Morgen ga ik naar de markt' staat er inversie.",
                "uitleg": "Zodra er iets anders dan het onderwerp vooraan staat, draait de volgorde om.",
            },
            {
                "vraag": "Bij inversie draait de volgorde van onderwerp en persoonsvorm om.",
                "uitleg": "'Ik ga morgen' wordt 'Morgen ga ik'.",
            },
            {
                "vraag": "In 'Straks komt hij langs' staat er inversie.",
                "uitleg": "'Straks' staat vooraan, dus schuift het onderwerp achter de persoonsvorm.",
            },
        ],
        "Waarom zeg je 'Morgen ga ik naar de markt' en niet 'Morgen ik ga naar de markt'?": [
            {
                "vraag": "Waarom zeg je 'Straks komt hij langs' en niet 'Straks hij komt langs'?",
                "opties": [
                    "omdat de persoonsvorm in een hoofdzin op de tweede plaats blijft",
                    "omdat 'straks' een bijzin inleidt",
                    "omdat het onderwerp nooit vooraan mag staan",
                    "omdat de zin anders in de verleden tijd zou staan",
                ],
            },
            {
                "vraag": "Waarom zeg je 'Gisteren las ik dat boek' en niet 'Gisteren ik las dat boek'?",
                "opties": [
                    "omdat de persoonsvorm in een hoofdzin op de tweede plaats blijft",
                    "omdat 'gisteren' een bijzin inleidt",
                    "omdat het onderwerp nooit vooraan mag staan",
                    "omdat de zin anders in de toekomende tijd zou staan",
                ],
            },
            {
                "vraag": "Waarom zeg je 'Daarna gingen we naar huis' en niet 'Daarna we gingen naar huis'?",
                "opties": [
                    "omdat de persoonsvorm in een hoofdzin op de tweede plaats blijft",
                    "omdat 'daarna' een bijzin inleidt",
                    "omdat het onderwerp nooit vooraan mag staan",
                    "omdat de zin anders vragend zou worden",
                ],
            },
        ],
        "Elke vragende zin begint met een vragend voornaamwoord.": [
            {
                "vraag": "Een vraag begint altijd met een vraagwoord.",
                "uitleg": "'Ga jij mee?' begint met de persoonsvorm. Vragen met en zonder vraagwoord bestaan allebei.",
            },
            {
                "vraag": "'Ga jij mee?' is geen vragende zin, want er staat geen vraagwoord.",
                "uitleg": "Het is wel degelijk een vraag. Ze begint alleen met de persoonsvorm in plaats van met een vraagwoord.",
            },
            {
                "vraag": "Zonder vraagwoord kan een zin geen vraag zijn.",
                "uitleg": "'Kom je mee?' en 'Heb je dat gezien?' zijn vragen zonder vraagwoord.",
            },
        ],
        "Welke van deze zinnen zijn samengesteld?": [
            {
                "opties": [
                    "Hij kwam te laat omdat de trein vertraging had.",
                    "Zij belde aan en ik deed open.",
                    "Toen de film begon, was de zaal vol.",
                    "De fiets van mijn zus staat buiten.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "De eerste drie hebben twee persoonsvormen. De laatste heeft er maar één en is dus enkelvoudig.",
            },
            {
                "opties": [
                    "Wij wachten tot iedereen er is.",
                    "Hij zwijgt maar zij praat door.",
                    "Hoewel het goot, gingen we buiten spelen.",
                    "Het boek van de bibliotheek ligt op tafel.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "De eerste drie hebben twee persoonsvormen. De laatste heeft er maar één en is dus enkelvoudig.",
            },
            {
                "opties": [
                    "Zij zwijgt hoewel ze het beter weet.",
                    "Ik kook en hij dekt de tafel.",
                    "Als het morgen regent, blijven we thuis.",
                    "De buren van hiernaast verhuizen morgen.",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "De eerste drie hebben twee persoonsvormen. De laatste heeft er maar één en is dus enkelvoudig.",
            },
        ],
        "In 'Hoewel hij doodmoe was, ging hij toch trainen', welk deel is de bijzin?": [
            {
                "vraag": "In 'Omdat het regende, bleven we binnen', welk deel is de bijzin?",
                "opties": ["Omdat het regende", "bleven we binnen", "we binnen", "het regende"],
            },
            {
                "vraag": "In 'Toen de bel ging, stond iedereen op', welk deel is de bijzin?",
                "opties": ["Toen de bel ging", "stond iedereen op", "iedereen op", "de bel ging"],
            },
            {
                "vraag": "In 'Als je klaar bent, mag je gaan', welk deel is de bijzin?",
                "opties": ["Als je klaar bent", "mag je gaan", "je gaan", "klaar bent"],
            },
        ],
        "Wat voor zin is 'Wat is dat mooi!'?": [
            {"vraag": "Wat voor zin is 'Wat loopt die hond hard!'?"},
            {"vraag": "Wat voor zin is 'Hoe mooi is dat toch!'?"},
            {"vraag": "Wat voor zin is 'Wat zie jij er goed uit!'?"},
        ],
    },
    "Spelling, leestekens en klanken — deel 1": {
        "In welke woorden verandert het woordbeeld als je er een meervoud van maakt?": [
            {
                "opties": ["muis", "duif", "wolf", "stoel"],
                "antwoord": [0, 1, 2],
                "uitleg": "Muizen, duiven, wolven. Bij stoelen blijft de l gewoon staan.",
            },
            {
                "opties": ["hoes", "neef", "druif", "fiets"],
                "antwoord": [0, 1, 2],
                "uitleg": "Hoezen, neven, druiven. Bij fietsen blijft de s gewoon staan.",
            },
            {
                "opties": ["gans", "wolf", "graf", "deur"],
                "antwoord": [0, 1, 2],
                "uitleg": "Ganzen, wolven, graven. Bij deuren blijft de r gewoon staan.",
            },
        ],
        "Hoe noem je de twee puntjes op de i in 'ruïne'?": [
            {
                "vraag": "Hoe noem je de twee puntjes op de u in 'reünie'?",
                "uitleg": "Een trema zegt: begin hier een nieuwe klank. Zonder trema zou je 'reu' lezen als één klank.",
            },
            {
                "vraag": "Hoe noem je de twee puntjes op de e in 'zeeën'?",
                "uitleg": "Een trema zegt: begin hier een nieuwe klank. Zonder trema zou je drie e's na elkaar lezen.",
            },
            {
                "vraag": "Hoe noem je de twee puntjes op de e in 'knieën'?",
                "uitleg": "Een trema zegt: begin hier een nieuwe klank. Zonder trema zou je 'ie' en 'e' aan elkaar plakken.",
            },
        ],
        "Namen van talen krijgen in het Nederlands een hoofdletter.": [
            {
                "vraag": "'Frans' en 'Nederlands' krijgen een hoofdletter.",
                "uitleg": "De taalnaam is afgeleid van een aardrijkskundige naam en houdt de hoofdletter.",
            },
            {
                "vraag": "Namen van landen krijgen in het Nederlands een hoofdletter.",
                "uitleg": "België, Frankrijk, Spanje. Talen en plaatsnamen krijgen er ook een.",
            },
            {
                "vraag": "Feestdagen zoals Kerstmis en Pasen krijgen een hoofdletter.",
                "uitleg": "Feestdagen wel, dagen van de week en maanden niet.",
            },
        ],
        "Welke zin gebruikt de hoofdletters correct?": [
            {
                "opties": [
                    "In maart leert zij Italiaans in Rome.",
                    "In Maart leert zij italiaans in Rome.",
                    "In maart leert zij italiaans in rome.",
                    "In Maart leert zij Italiaans in rome.",
                ],
            },
            {
                "opties": [
                    "In juli studeert hij Duits in Berlijn.",
                    "In Juli studeert hij duits in Berlijn.",
                    "In juli studeert hij duits in berlijn.",
                    "In Juli studeert hij Duits in berlijn.",
                ],
            },
            {
                "opties": [
                    "In oktober spreekt zij Engels in Londen.",
                    "In Oktober spreekt zij engels in Londen.",
                    "In oktober spreekt zij engels in londen.",
                    "In Oktober spreekt zij Engels in londen.",
                ],
            },
        ],
        "Waarom schrijf je 'zee-eend' met een koppelteken?": [
            {
                "vraag": "Waarom schrijf je 'na-apen' met een koppelteken?",
                "opties": [
                    "om te vermijden dat je de twee a's als één klank leest",
                    "omdat samenstellingen altijd een koppelteken krijgen",
                    "omdat het een leenwoord uit het Duits is",
                    "omdat het woord uit drie delen bestaat",
                ],
            },
            {
                "vraag": "Waarom schrijf je 'auto-ongeval' met een koppelteken?",
                "opties": [
                    "om te vermijden dat je de o en de o als één klank leest",
                    "omdat samenstellingen altijd een koppelteken krijgen",
                    "omdat het een leenwoord uit het Duits is",
                    "omdat het woord uit drie delen bestaat",
                ],
            },
            {
                "vraag": "Waarom schrijf je 'zo-even' met een koppelteken?",
                "opties": [
                    "om te vermijden dat je de o en de e als één klank leest",
                    "omdat samenstellingen altijd een koppelteken krijgen",
                    "omdat het een leenwoord uit het Duits is",
                    "omdat het woord uit drie delen bestaat",
                ],
            },
        ],
        "Hoe noem je het teken in 'Anna's fiets'?": [
            {
                "vraag": "Hoe noem je het teken in 'oma's koekjes'?",
                "uitleg": "De apostrof houdt de klank van de a open. Zonder apostrof zou je 'omas' lezen met een korte a.",
            },
            {
                "vraag": "Hoe noem je het teken in 'Lisa's jas'?",
                "uitleg": "De apostrof houdt de klank van de a open. Zonder apostrof zou je 'Lisas' lezen met een korte a.",
            },
            {
                "vraag": "Hoe noem je het teken in 'auto's'?",
                "uitleg": "De apostrof houdt de klank van de o open. Zonder apostrof zou je 'autos' lezen met een korte o.",
            },
        ],
        "In welke woorden staat terecht een trema?": [
            {
                "opties": ["knieën", "geëerd", "coördinatie", "na-apen"],
                "antwoord": [0, 1, 2],
                "uitleg": "Binnen één woorddeel gebruik je een trema. Tussen twee delen van een samenstelling een koppelteken.",
            },
            {
                "opties": ["ideeën", "beëindigen", "ruïne", "auto-ongeval"],
                "antwoord": [0, 1, 2],
                "uitleg": "Binnen één woorddeel gebruik je een trema. Tussen twee delen van een samenstelling een koppelteken.",
            },
            {
                "opties": ["zeeën", "reünie", "geïnteresseerd", "zo-even"],
                "antwoord": [0, 1, 2],
                "uitleg": "Binnen één woorddeel gebruik je een trema. Tussen twee delen van een samenstelling een koppelteken.",
            },
        ],
        "De namen van de dagen en de maanden krijgen in het Nederlands een hoofdletter.": [
            {
                "vraag": "'Maandag' en 'januari' krijgen een hoofdletter.",
                "uitleg": "Maandag en januari schrijf je klein. Feestdagen zoals Kerstmis en Pasen krijgen er wel een.",
            },
            {
                "vraag": "De maanden van het jaar krijgen een hoofdletter.",
                "uitleg": "Januari, februari en maart schrijf je klein. Talen en landen krijgen wel een hoofdletter.",
            },
            {
                "vraag": "'Woensdag' schrijf je met een hoofdletter.",
                "uitleg": "Dagen van de week schrijf je klein. Feestdagen zoals Kerstmis krijgen wel een hoofdletter.",
            },
        ],
        "Wat is de juiste verleden tijd van 'bereiden'?": [
            {
                "vraag": "Wat is de juiste verleden tijd van 'antwoorden'?",
                "opties": ["ik antwoordde", "ik antwoorde", "ik antwoordte", "ik antwoord"],
                "uitleg": "De stam is 'antwoord' en eindigt op d. Daar komt -de bij, dus krijg je twee keer d.",
            },
            {
                "vraag": "Wat is de juiste verleden tijd van 'redden'?",
                "opties": ["ik redde", "ik rede", "ik redte", "ik red"],
                "uitleg": "De stam is 'red' en eindigt op d. Daar komt -de bij, dus krijg je twee keer d.",
            },
            {
                "vraag": "Wat is de juiste verleden tijd van 'branden'?",
                "opties": ["ik brandde", "ik brande", "ik brandte", "ik brand"],
                "uitleg": "De stam is 'brand' en eindigt op d. Daar komt -de bij, dus krijg je twee keer d.",
            },
        ],
        "In welke zin staan de hoofdletters juist?": [
            {
                "opties": [
                    "Met Kerstmis gaan we naar de Alpen.",
                    "Met kerstmis gaan we naar de alpen.",
                    "Met Kerstmis gaan we naar de alpen.",
                    "Met kerstmis gaan we naar de Alpen.",
                ],
            },
            {
                "opties": [
                    "Met Nieuwjaar rijden we naar de Kempen.",
                    "Met nieuwjaar rijden we naar de kempen.",
                    "Met Nieuwjaar rijden we naar de kempen.",
                    "Met nieuwjaar rijden we naar de Kempen.",
                ],
            },
            {
                "opties": [
                    "Met Pinksteren gaan we naar de Vogezen.",
                    "Met pinksteren gaan we naar de vogezen.",
                    "Met Pinksteren gaan we naar de vogezen.",
                    "Met pinksteren gaan we naar de Vogezen.",
                ],
            },
        ],
        "Welke woorden krijgen een hoofdletter?": [
            {
                "opties": ["Frans", "Frankrijk", "Pasen", "januari"],
                "antwoord": [0, 1, 2],
                "uitleg": "Talen, landen en feestdagen wel; maanden niet.",
            },
            {
                "opties": ["Duits", "Italië", "Nieuwjaar", "maandag"],
                "antwoord": [0, 1, 2],
                "uitleg": "Talen, landen en feestdagen wel; dagen van de week niet.",
            },
            {
                "opties": ["Engels", "Spanje", "Pinksteren", "augustus"],
                "antwoord": [0, 1, 2],
                "uitleg": "Talen, landen en feestdagen wel; maanden niet.",
            },
        ],
        "Welke verleden tijd van 'verhuizen' is correct?": [
            {
                "vraag": "Welke verleden tijd van 'blozen' is correct?",
                "opties": ["bloosde", "blooste", "blozde", "blozte"],
                "uitleg": "De stam eindigt op een z, en die hoort niet bij 't kofschip, dus komt er -de bij. Aan het eind van een lettergreep schrijf je die z als s.",
            },
            {
                "vraag": "Welke verleden tijd van 'reizen' is correct?",
                "opties": ["reisde", "reiste", "reizde", "reizte"],
                "uitleg": "De stam eindigt op een z, en die hoort niet bij 't kofschip, dus komt er -de bij. Aan het eind van een lettergreep schrijf je die z als s.",
            },
            {
                "vraag": "Welke verleden tijd van 'verven' is correct?",
                "opties": ["verfde", "verfte", "vervde", "vervte"],
                "uitleg": "De stam eindigt op een v, en die hoort niet bij 't kofschip, dus komt er -de bij. Aan het eind van een lettergreep schrijf je die v als f.",
            },
        ],
    },
    "Spelling, leestekens en klanken — deel 2": {
        "Welke van deze tekens zijn interpunctietekens?": [
            {
                "opties": ["de komma", "de dubbele punt", "het vraagteken", "het trema"],
                "antwoord": [0, 1, 2],
                "uitleg": "Een trema is een uitspraakteken, geen leesteken. Die twee horen in aparte lijstjes.",
            },
            {
                "opties": ["de punt", "de puntkomma", "het uitroepteken", "het accentteken"],
                "antwoord": [0, 1, 2],
                "uitleg": "Een accentteken is een uitspraakteken, geen leesteken. Die twee horen in aparte lijstjes.",
            },
            {
                "opties": ["het aanhalingsteken", "de komma", "het gedachtestreepje", "het trema"],
                "antwoord": [0, 1, 2],
                "uitleg": "Een trema is een uitspraakteken, geen leesteken. Die twee horen in aparte lijstjes.",
            },
        ],
        "Een komma kan de betekenis van een zin veranderen.": [
            {
                "vraag": "'We eten, oma' betekent iets anders dan 'We eten oma'.",
                "uitleg": "Eén komma maakt van oma de aangesprokene in plaats van het lijdend voorwerp.",
            },
            {
                "vraag": "Een komma voor een bijzin kan de betekenis van de zin veranderen.",
                "uitleg": "Vergelijk 'Hij kwam niet omdat het regende' met 'Hij kwam niet, omdat het regende'.",
            },
            {
                "vraag": "Leestekens kunnen de betekenis van een zin veranderen.",
                "uitleg": "Vergelijk 'We eten, oma' met 'We eten oma'. Eén komma volstaat.",
            },
        ],
        "In welke zin staat de komma correct?": [
            {
                "opties": [
                    "Toen de film begon, was de zaal vol.",
                    "Toen de film begon was de zaal, vol.",
                    "Toen, de film begon was de zaal vol.",
                    "Toen de film, begon was de zaal vol.",
                ],
            },
            {
                "opties": [
                    "Omdat het regende, bleven we binnen.",
                    "Omdat het regende bleven we, binnen.",
                    "Omdat, het regende bleven we binnen.",
                    "Omdat het, regende bleven we binnen.",
                ],
            },
            {
                "opties": [
                    "Als je klaar bent, mag je gaan.",
                    "Als je klaar bent mag je, gaan.",
                    "Als, je klaar bent mag je gaan.",
                    "Als je, klaar bent mag je gaan.",
                ],
            },
        ],
        "Welke van deze letters zijn klinkers?": [
            {
                "opties": ["a", "i", "o", "m"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het Nederlands heeft zes klinkerletters: a, e, i, o, u en y. Alle andere zijn medeklinkers.",
            },
            {
                "opties": ["e", "o", "y", "k"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het Nederlands heeft zes klinkerletters: a, e, i, o, u en y. Alle andere zijn medeklinkers.",
            },
            {
                "opties": ["i", "u", "y", "t"],
                "antwoord": [0, 1, 2],
                "uitleg": "Het Nederlands heeft zes klinkerletters: a, e, i, o, u en y. Alle andere zijn medeklinkers.",
            },
        ],
        "In 'boot' staat een korte klinker.": [
            {
                "vraag": "In 'maan' staat een korte klinker.",
                "uitleg": "De aa is lang. In 'man' staat de korte a.",
            },
            {
                "vraag": "In 'deur' staat een korte klinker.",
                "uitleg": "De eu is lang. Korte klinkers hoor je in woorden als man, bot en pit.",
            },
            {
                "vraag": "In 'buur' staat een korte klinker.",
                "uitleg": "De uu is lang. In 'bus' staat de korte u.",
            },
        ],
        "Hoe noem je de e-klank in 'de' en in de laatste lettergreep van 'lopen'?": [
            {
                "vraag": "Hoe noem je de e-klank in 'het' en in de laatste lettergreep van 'werken'?",
                "uitleg": "Hij is nooit beklemtoond, en daarom hoor je hem amper terwijl hij overal zit.",
            },
            {
                "vraag": "Hoe noem je de onbeklemtoonde e in 'kamer' en in 'vader'?",
                "uitleg": "Hij is nooit beklemtoond, en daarom hoor je hem amper terwijl hij overal zit.",
            },
            {
                "vraag": "Hoe noem je de e-klank in 'de' en in de laatste lettergreep van 'wandelen'?",
                "uitleg": "Hij is nooit beklemtoond, en daarom hoor je hem amper terwijl hij overal zit.",
            },
        ],
        "Achter een indirecte vraag zoals 'Hij vroeg of ik meekwam' hoort een vraagteken.": [
            {
                "vraag": "Achter 'Zij vroeg wanneer de trein vertrok' hoort een vraagteken.",
                "uitleg": "Er wordt niets gevraagd, er wordt verteld dát er iets gevraagd werd. Dus komt er een punt.",
            },
            {
                "vraag": "Elke zin met het woord 'vroeg' erin eindigt op een vraagteken.",
                "uitleg": "'Hij vroeg of ik meekwam' vertelt alleen dát er gevraagd werd. Dus komt er een punt.",
            },
            {
                "vraag": "Achter 'Ik weet niet of hij komt' hoort een vraagteken.",
                "uitleg": "Er wordt niets gevraagd, er wordt iets meegedeeld. Dus komt er een punt.",
            },
        ],
        "In welke zin staan de aanhalingstekens correct?": [
            {
                "opties": [
                    "Zij zei: “Ik bel je straks.”",
                    "Zij zei dat: “ze me straks zou bellen.”",
                    "Zij zei “dat ze belde” volgens mij.",
                    "Zij zei: ik bel je “straks”.",
                ],
            },
            {
                "opties": [
                    "De juf zei: “Neem je boek.”",
                    "De juf zei dat: “we ons boek moesten nemen.”",
                    "De juf zei “dat we moesten beginnen” denk ik.",
                    "De juf zei: neem je “boek”.",
                ],
            },
            {
                "opties": [
                    "Hij riep: “Wacht op mij!”",
                    "Hij riep dat: “we moesten wachten.”",
                    "Hij riep “dat we wachtten” meen ik.",
                    "Hij riep: wacht op “mij”.",
                ],
            },
        ],
        "Waarvoor kan je een dubbele punt gebruiken?": [
            {
                "opties": [
                    "een lijstje aankondigen",
                    "een uitleg inleiden",
                    "de woorden van iemand aankondigen",
                    "een vraag stellen",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Vragen doet een vraagteken. De dubbele punt kondigt aan wat er volgt.",
            },
            {
                "opties": [
                    "een opsomming aankondigen",
                    "een reden inleiden",
                    "een letterlijk citaat aankondigen",
                    "een tussenzin afbakenen",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Een tussenzin baken je af met komma's, haakjes of gedachtestreepjes.",
            },
            {
                "opties": [
                    "een reeks voorbeelden aankondigen",
                    "een verklaring inleiden",
                    "een uitspraak aankondigen",
                    "een woord afbreken",
                ],
                "antwoord": [0, 1, 2],
                "uitleg": "Een woord breek je af met een koppelteken aan het einde van de regel.",
            },
        ],
        "Wat is het verschil tussen de klinker in 'maan' en die in 'man'?": [
            {"vraag": "Wat is het verschil tussen de klinker in 'boot' en die in 'bot'?"},
            {"vraag": "Wat is het verschil tussen de klinker in 'buur' en die in 'bus'?"},
            {"vraag": "Wat is het verschil tussen de klinker in 'peer' en die in 'pet'?"},
        ],
        "Waarom staat er een komma in 'Hoewel het goot, gingen we toch buiten spelen'?": [
            {"vraag": "Waarom staat er een komma in 'Toen de bel ging, stond iedereen op'?"},
            {"vraag": "Waarom staat er een komma in 'Omdat het regende, bleven we binnen'?"},
            {"vraag": "Waarom staat er een komma in 'Als je klaar bent, mag je gaan'?"},
        ],
        "Hoe maak je van 'Je komt mee' hoorbaar een vraag, zonder de woorden te veranderen?": [
            {"vraag": "Hoe maak je van 'Hij is thuis' hoorbaar een vraag, zonder de woorden te veranderen?"},
            {"vraag": "Hoe maak je van 'Dat is jouw fiets' hoorbaar een vraag, zonder de woorden te veranderen?"},
            {"vraag": "Hoe maak je van 'Zij komt morgen' hoorbaar een vraag, zonder de woorden te veranderen?"},
        ],
    },
}
