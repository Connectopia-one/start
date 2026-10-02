# -*- coding: utf-8 -*-
"""De leerbundels voor geschiedenis op 🌍 Beyond dubbele finaliteit.

Gebaseerd op de vakfiche geschiedenis 3de graad dubbele finaliteit, geldig vanaf
1 januari 2027. Eenentwintig thema's, met de gewichten van het examen als
leidraad: de samenlevingen in de moderne en de hedendaagse tijd samen bijna zes
op de tien, het werken met bronnen één op vijf.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde woorden
als de vraag. `python3 dekking.py ../../beyond-dubbele-finaliteit/geschiedenis.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond-dubbele-finaliteit", de naam van de
categorie. Dat is nodig en niet alleen netjes: Beyond doorstroom en Boost hebben
thema's met bijna dezelfde titels, en zonder de categorie in de bestandsnaam
weet noch dekking.py noch het uploadscherm welke bedoeld is.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Geschiedenis"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

BUNDELS["het-historisch-referentiekader-tijd-ruimte-en-domeinen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het historisch referentiekader: tijd, ruimte en domeinen",
    onder="Het gereedschap van het vak: perioden, plaatsen en de vier maatschappelijke domeinen.",
    secties=[
        dict(kop="De zeven periodes", blokken=[
            ("p", "Het <strong>historisch referentiekader</strong> is <strong>het geheel van tijd, ruimte "
                  "en maatschappelijke domeinen waarmee je een gebeurtenis plaatst</strong>. Het is "
                  "<strong>een hulpmiddel om nieuwe informatie een plaats te geven</strong>: wie de "
                  "periodes, de schalen en de domeinen kent, kan een bron meteen ergens hangen. Het "
                  "<strong>courante westerse referentiekader telt zeven periodes</strong>."),
            ("p", tabel(["Periode", "Loopt van", "Tot"], [
                ["De prehistorie", "het ontstaan van de mens", "het eerste schrift"],
                ["Het oude nabije oosten", "het eerste schrift", "ongeveer 800 voor Christus"],
                ["De klassieke oudheid", "de Griekse stadstaten", "ongeveer 500 na Christus"],
                ["De middeleeuwen", "ongeveer 500", "ongeveer 1500"],
                ["De vroegmoderne tijd", "ongeveer 1500", "1789 of 1815"],
                ["De moderne tijd", "1789 of 1815", "1945"],
                ["De hedendaagse tijd", "1945", "vandaag"],
            ])),
            ("p", "De volgorde na de middeleeuwen is dus: <strong>de vroegmoderne tijd, daarna de moderne "
                  "tijd, daarna de hedendaagse tijd</strong>, de laatste van de zeven. De "
                  "<strong>Reformatie situeer je in de vroegmoderne tijd</strong> (1517), de "
                  "<strong>industriële revolutie en het Congres van Wenen in de moderne tijd</strong>, en "
                  "<strong>de naoorlogse periode in de hedendaagse tijd</strong>."),
            ("p", "Een <strong>eeuw</strong> loopt niet gelijk met haar getal: <strong>het jaar 1789 ligt in "
                  "de achttiende eeuw</strong>. Een <strong>decennium</strong> is tien jaar, een "
                  "<strong>millennium</strong> duizend jaar. <strong>Een verschil tussen twee jaartallen "
                  "bereken je door af te trekken</strong>: van 1830 tot 1914 liggen <strong>vierentachtig "
                  "jaar</strong>. Jaartallen voor Christus lopen aflopend."),
        ]),
        dict(kop="Wat een periodisering is, en wat ze niet is", blokken=[
            ("p", "Een <strong>periodisering</strong> is <strong>een indeling van het verleden in periodes, "
                  "achteraf gemaakt</strong>. Drie dingen horen daarbij: <strong>een periode wordt "
                  "afgebakend op basis van een selectie van kenmerken en gebeurtenissen</strong>, "
                  "<strong>een periode krijgt een symbolische begin- en einddatum</strong>, en "
                  "<strong>een periode is een constructie die achteraf gemaakt wordt</strong>. Wat niet "
                  "klopt, is dat een periode in elke beschaving even lang zou duren: de lengtes verschillen "
                  "sterk, en elders ligt de indeling anders."),
            ("p", "Dat een <strong>begin- en einddatum symbolisch</strong> is, betekent dat het gekozen "
                  "moment staat voor een verandering die veel langer duurde; op de dag zelf veranderde voor "
                  "de meeste mensen niets. Daarom werkt een <strong>tijdlijn</strong> met zulke "
                  "<strong>ijkpunten</strong>."),
            ("p", "Een <strong>periodisering is nooit volledig neutraal, want ze hangt af van welke "
                  "kenmerken je kiest</strong>: <strong>een periodisering met politieke scharnierpunten "
                  "geeft andere grenzen dan een met economische scharnierpunten</strong>. Kies je het "
                  "bestuur, dan liggen de grenzen elders dan wanneer je de techniek of de kunst kiest. "
                  "Dat zijn de <strong>principes en de beperkingen</strong> van elk referentiekader."),
            ("p", "Een <strong>scharnierpunt</strong> is <strong>een gebeurtenis of evolutie die de overgang "
                  "vormt tussen twee historische periodes</strong>, zoals de Franse Revolutie of het einde "
                  "van de Tweede Wereldoorlog. Op een tijdlijn met 1517, 1789, 1815 en 1945 zijn "
                  "<strong>1789 of 1815 het scharnierpunt aan het begin van de moderne tijd</strong> en "
                  "<strong>1945 dat aan het begin van de hedendaagse tijd</strong>; 1517 hoort in de "
                  "vroegmoderne tijd en begint geen nieuwe periode. Het einde van de Tweede Wereldoorlog "
                  "laat een nieuwe periode beginnen omdat de machtsverhoudingen in de wereld toen grondig "
                  "veranderden: twee supermachten, dekolonisatie en nieuwe internationale organisaties."),
            ("p", "Zo'n keuze heeft een <strong>beperking</strong>. Het Congres van Wenen als scharnierpunt "
                  "is <strong>een westers en vooral politiek ijkpunt, dat elders weinig betekent</strong>: "
                  "voor China of Afrika zegt 1815 niets, en in het economische of culturele domein lag het "
                  "keerpunt ergens anders. Daarom <strong>past de westerse periodisering in zeven periodes "
                  "niet even goed op de geschiedenis van China</strong>, dat vaak per dynastie wordt "
                  "ingedeeld."),
        ]),
        dict(kop="Structuurbegrippen rond tijd", blokken=[
            ("p", "<strong>Structuurbegrippen</strong> zijn de woorden waarmee je tijd en ruimte ordent."),
            ("p", tabel(["Begrip", "Wat het betekent"], [
                ["Continuïteit", "wat over een lange tijd hetzelfde blijft"],
                ["Verandering", "de breuk in die lijn"],
                ["Evolutie", "een trage, geleidelijke verandering"],
                ["Breuk of revolutie", "een plotse, diepe verandering op korte tijd"],
                ["Chronologie", "de ordening van gebeurtenissen in de tijd"],
                ["Tijdrekening", "het stelsel waarmee je jaren nummert"],
                ["Gelijktijdigheid", "twee gebeurtenissen in dezelfde periode op verschillende plaatsen"],
                ["Ongelijktijdigheid", "een ontwikkeling die ergens al begon en elders nog niet"],
            ])),
            ("p", "<strong>Tijdrekening en chronologie betekenen dus niet hetzelfde.</strong> En "
                  "<strong>een breuk en een continuïteit kunnen in dezelfde periode naast elkaar "
                  "bestaan</strong>: de fabriek verandert het werk, en toch blijft het gezin lang de plaats "
                  "waar geld en zorg verdeeld worden. De industriële revolutie is een mooi voorbeeld van "
                  "<strong>ongelijktijdigheid</strong>: ze begint in Engeland, daarna in België, en pas veel "
                  "later elders. <strong>De val van de Berlijnse Muur in 1989 wijst op verandering in de "
                  "naoorlogse periode in Europa.</strong>"),
            ("p", "Een <strong>gebeurtenis</strong> duurt kort, <strong>een ontwikkeling</strong> duurt lang. "
                  "De val van de Muur is een gebeurtenis, de verstedelijking een ontwikkeling."),
        ]),
        dict(kop="Structuurbegrippen rond ruimte", blokken=[
            ("p", "Om een gebeurtenis <strong>in de ruimte te situeren</strong> gebruik je een ander stel "
                  "begrippen: <strong>continentaal en maritiem</strong>, stedelijk en <strong>ruraal</strong>, "
                  "lokaal, regionaal, nationaal, <strong>Europees</strong> en <strong>mondiaal</strong>. "
                  "Evolutie, revolutie, chronologie en tijdrekening horen bij tijd, niet bij ruimte."),
            ("p", tabel(["Begrip", "Wat het betekent"], [
                ["Maritiem", "vooral op zee gericht"],
                ["Continentaal", "vooral op het vasteland gericht"],
                ["Ruraal", "landelijk, op het platteland; het tegengestelde van stedelijk"],
                ["Mondiaal", "wereldwijd, dus Europa inbegrepen"],
                ["Westers", "Europa en bijvoorbeeld de Verenigde Staten"],
                ["Niet-westers", "samenlevingen buiten Europa en de westerse wereld"],
            ])),
            ("p", "<strong>Een gebeurtenis die je mondiaal situeert, raakt Europa dus wél</strong>: mondiaal "
                  "is geen tegenstelling met Europees maar een ruimere <strong>schaal</strong>. Lees je in "
                  "bronnen dat <strong>Wilhelm II een vloot bouwt en kolonies zoekt in Afrika en Azië</strong>, "
                  "dan situeer je zijn <strong>ambities mondiaal</strong>: wie overzee kolonies wil en een "
                  "vloot bouwt, kijkt verder dan Europa."),
            ("p", "Ook de ligging zelf verklaart iets. <strong>De eerste industriële revolutie situeer je in "
                  "de regio's met steenkool en ijzererts</strong>, want <strong>steenkool en ijzererts waren "
                  "nodig voor stoom en staal</strong>; transport was duur, dus de industrie kwam naar de "
                  "grondstof. Let er ten slotte op dat <strong>grenzen en namen veranderen</strong>: het "
                  "gebied dat wij België noemen, heette in 1800 anders en lag in een ander staatsverband."),
            ("p", "Een <strong>anachronisme</strong> is <strong>iets uit een andere tijd in een verkeerde "
                  "tijd plaatsen</strong>. Spreken over de Belgen in de Romeinse tijd zoals wij het woord nu "
                  "gebruiken, is er een voorbeeld van."),
        ]),
        dict(kop="De vier maatschappelijke domeinen", blokken=[
            ("p", tabel(["Domein", "Waarover het gaat", "Voorbeeld"], [
                ["Het politieke domein", "bestuur, macht, wetten, oorlog", "een grondwet, een verkiezing"],
                ["Het economische domein", "handel, productie, grondstoffen, werk, geld", "een fabriek, invoerrechten"],
                ["Het sociale domein", "groepen, wonen, gezin, gezondheid", "kinderarbeid, een arbeiderswijk"],
                ["Het culturele domein", "religie, kunst, taal, onderwijs, denken", "een kerk, een school, een roman"],
            ])),
            ("p", "<strong>Kijk je naar handel, productie en werk, dan onderzoek je het economische "
                  "domein</strong>; <strong>kijk je naar kunst, religie en onderwijs, dan het culturele "
                  "domein</strong>."),
            ("p", "<strong>Je kan dezelfde gebeurtenis in meer dan één maatschappelijk domein "
                  "situeren.</strong> <strong>Een wet die kinderarbeid verbiedt, situeer je in het sociale "
                  "domein, want het raakt de arbeidersgezinnen, en in het politieke domein, want het is een "
                  "beslissing van de staat.</strong> Dat de domeinen samenhangen is net de reden: een "
                  "economische verandering, zoals de fabriek met haar werkomstandigheden, brengt sociale en "
                  "politieke eisen mee, zoals de invoering van het algemeen enkelvoudig stemrecht. Een "
                  "<strong>staking</strong> is economisch en sociaal, en vaak ook politiek."),
            ("p", "<strong>Moet je een gebeurtenis situeren in tijd, ruimte en domein, dan lever je drie "
                  "dingen af: wanneer, waar en op welk terrein het speelde.</strong> Geen beoordeling of het "
                  "goed of slecht was, en geen lijst van alle aanwezigen: dat is iets anders dan situeren."),
        ]),
    ],
    onthoud=[
        "Zeven periodes: prehistorie, oude nabije oosten, klassieke oudheid, middeleeuwen, vroegmoderne, moderne en hedendaagse tijd.",
        "Een periodisering is een constructie achteraf, met symbolische data en een selectie van kenmerken.",
        "Een scharnierpunt vormt de overgang tussen twee periodes; 1789 of 1815 en 1945 zijn er twee.",
        "Tijd: continuïteit, evolutie, breuk, chronologie, tijdrekening, gelijktijdigheid. Ruimte: maritiem, continentaal, ruraal, mondiaal, westers.",
        "Vier domeinen: politiek, economisch, sociaal en cultureel. De meeste onderwerpen horen in meer dan één.",
        "Situeren = wanneer, waar en op welk terrein. Geen oordeel.",
    ],
)

BUNDELS["kenmerken-van-samenlevingen-vergelijken-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kenmerken van samenlevingen vergelijken",
    onder="Hoe je twee samenlevingen naast elkaar zet zonder appelen met peren te vergelijken.",
    secties=[
        dict(kop="Vier soorten kenmerken", blokken=[
            ("p", "Een <strong>kenmerk van een samenleving</strong> is <strong>een eigenschap waarmee je ze "
                  "met een andere kan vergelijken</strong>. Je sorteert ze in vier soorten, één per "
                  "maatschappelijk domein."),
            ("p", tabel(["Soort kenmerken", "Wat eronder valt"], [
                ["Politieke kenmerken", "de staatsvorm, de bestuurlijke organisatie, mensenrechten, "
                                        "imperialisme en kolonialisme, een breuklijn in een samenleving"],
                ["Economische kenmerken", "industrialisering en kapitalisme, arbeidsorganisatie en "
                                          "productiemethoden, handel, een consumptiemaatschappij"],
                ["Sociale kenmerken", "een gelaagde samenleving, onderdrukking en emancipatie, "
                                      "migratie en minderheden"],
                ["Culturele kenmerken", "mens- en wereldbeelden, wetenschappen en technologie, religie, "
                                        "propaganda, een multiculturele samenleving"],
            ])),
            ("p", "<strong>De vier soorten kenmerken moet je niet apart houden, want ze hangen samen</strong>: "
                  "<strong>een verandering in het economische domein kan gevolgen hebben in het sociale "
                  "domein</strong>, en <strong>een transportrevolutie verandert ook de manier waarop er "
                  "geproduceerd wordt</strong>. Een <strong>kenmerk kan ook in de ene periode aanwezig zijn "
                  "en in de andere niet.</strong>"),
        ]),
        dict(kop="Begrippen voor het bestuur en de economie", blokken=[
            ("p", tabel(["Begrip", "Wat het betekent"], [
                ["Een totalitaire staat", "een staat waarin de overheid elk deel van het leven wil controleren"],
                ["Een dictatuur", "een staat waarin één man of één partij alle macht heeft"],
                ["Een rechtsstaat", "een staat waarin ook de overheid zelf aan de wet gebonden is"],
                ["Kapitalisme", "het economische systeem waarin privébezit en winst centraal staan"],
                ["Een postindustriële samenleving", "een samenleving waarin niet de industrie maar de "
                                                    "diensten de grootste werkgever zijn"],
                ["Mondialisering", "economieën over de hele wereld raken meer met elkaar verbonden"],
                ["Wij-zij-denken", "het denken in een eigen groep tegenover een andere groep"],
            ])),
            ("p", "<strong>Een dictatuur en een totalitaire staat betekenen niet precies hetzelfde</strong>: "
                  "een dictatuur houdt de politieke macht vast, een totalitaire staat wil ook het denken, "
                  "het gezin, de jeugd en de vrije tijd beheersen. En <strong>een democratie is niet "
                  "automatisch ook een rechtsstaat</strong>: een verkozen meerderheid kan zich boven de wet "
                  "plaatsen, en dan ontbreekt de bescherming van wie in de minderheid is."),
            ("p", "Bij internationale samenwerking scheid je twee soorten organisaties. "
                  "<strong>Het verschil tussen een supranationale en een intergouvernementele organisatie "
                  "is dat een supranationale organisatie beslissingen kan opleggen aan de lidstaten</strong>; "
                  "in een intergouvernementele organisatie beslissen de regeringen samen en houdt elk land "
                  "zijn vetorecht."),
        ]),
        dict(kop="Vergelijken: hoe en waarom", blokken=[
            ("p", "<strong>Vergelijken doe je per domein en met dezelfde vraag voor beide samenlevingen</strong>. "
                  "Wie voor de ene naar het bestuur kijkt en voor de andere naar de kunst, vergelijkt niets."),
            ("p", tabel(["Vraag", "Domein"], [
                ["Wie beslist, en op welke grond?", "het politieke domein"],
                ["Waarvan leven de mensen?", "het economische domein"],
                ["Welke groepen zijn er, en wie staat waar?", "het sociale domein"],
                ["Wat gelooft men, en wat leert men?", "het culturele domein"],
            ])),
            ("p", "Drie regels houden een vergelijking eerlijk. <strong>Wie twee samenlevingen vergelijkt, "
                  "moet niet enkel de verschillen opnoemen</strong>, maar ook de gelijkenissen, en ze "
                  "verklaren. <strong>Een vergelijking tussen periodes moet niet altijd over alle vier de "
                  "soorten kenmerken gaan</strong>: je kiest de kenmerken die bij je vraag passen. En "
                  "<strong>bij het vergelijken beoordeel je niet welke van de twee de betere was</strong>: "
                  "dat is een waardeoordeel, geen vergelijking."),
            ("p", "<strong>Waarom gebruik je bij het beschrijven van een samenleving de begrippen die bij "
                  "die samenleving horen? Anders leg je er woorden op die er niet bij passen.</strong> "
                  "Spreken over een parlement in het oude Egypte zegt meer over ons dan over Egypte."),
            ("p", "Je kan <strong>twee periodes</strong> vergelijken of <strong>twee samenlevingen uit "
                  "dezelfde periode</strong>. <strong>Twee samenlevingen in dezelfde periode kunnen een heel "
                  "andere bestuurlijke organisatie hebben</strong>, en dat is net de winst van die tweede "
                  "vergelijking: <strong>je ziet dat eenzelfde tijd heel verschillende samenlevingen kan "
                  "dragen</strong>, iets wat een vergelijking tussen periodes niet oplevert."),
            ("p", "Welke kenmerken je gebruikt om <strong>een samenleving uit de oudheid met een samenleving "
                  "uit de moderne tijd</strong> te vergelijken? <strong>De staatsvorm en de gelaagdheid van "
                  "de samenleving</strong>, en <strong>de handel en de arbeidsorganisatie</strong>: "
                  "kenmerken die in beide bestaan, zodat de vergelijking ergens op steunt."),
        ]),
        dict(kop="Drie vergelijkingen uitgewerkt", blokken=[
            ("p", "<strong>Een standenmaatschappij en een klassenmaatschappij</strong>: <strong>in de eerste "
                  "ligt je plaats bij je geboorte vast</strong>, <strong>in de tweede hangt ze af van je "
                  "bezit en je positie in de productie</strong>."),
            ("p", "<strong>Slavernij in de vroegmoderne tijd en arbeid in de fabrieken van de negentiende "
                  "eeuw</strong>: beide zijn zware uitbuiting, maar er is een verschil. <strong>Een slaaf is "
                  "iemands bezit, een arbeider sluit een arbeidsovereenkomst.</strong> Die overeenkomst was "
                  "in de praktijk ongelijk, maar ze bestond, en ze kon opgezegd worden."),
            ("p", "<strong>De staatsvorm onder Mao en de staatsvorm in China vandaag</strong>: de economie "
                  "veranderde grondig, maar de belangrijkste gelijkenis blijft dat <strong>in beide gevallen "
                  "één partij de macht in handen heeft</strong>."),
            ("p", "<strong>Het moderne imperialisme en het imperialisme uit de vroegmoderne tijd</strong>: "
                  "een duidelijk verschil is dat <strong>het moderne imperialisme het binnenland bezet, niet "
                  "enkel de kust</strong>. In de vroegmoderne tijd ging het vooral om handelsposten aan de "
                  "kust."),
        ]),
        dict(kop="De aard van een intercultureel contact", blokken=[
            ("p", "Komen twee samenlevingen met elkaar in contact, dan beschrijf je dat contact met vier "
                  "woordenparen: <strong>vreedzaam contact en gewelddadig contact</strong>, en "
                  "<strong>wederzijdse perceptie en wederzijdse impact</strong>."),
            ("p", tabel(["Begrip", "Wat het betekent"], [
                ["Wederzijdse perceptie", "het beeld dat twee groepen van elkaar hebben na een contact"],
                ["Wederzijdse impact", "beide samenlevingen veranderen door het contact"],
                ["Uitbuiting", "de ene groep haalt voordeel ten koste van de andere"],
                ["Cultuurvermenging", "elementen van twee culturen groeien samen tot iets nieuws"],
                ["Cultuurdominantie", "de ene legt zijn taal, geloof en school op aan de andere"],
            ])),
            ("p", "<strong>Handelen twee groepen met elkaar en nemen ze beide iets van de ander over, zonder "
                  "dwang, dan passen de woorden vreedzaam contact en cultuurvermenging.</strong> "
                  "<strong>Legt een kolonisator zijn taal, geloof en school op aan de bevolking, dan noem je "
                  "dat cultuurdominantie.</strong> Die twee sluiten elkaar niet volledig uit: ook onder dwang "
                  "ontstaat vermenging, in taal, muziek en keuken."),
        ]),
    ],
    onthoud=[
        "Vier soorten kenmerken: politiek, economisch, sociaal, cultureel. Ze hangen samen.",
        "Totalitaire staat, dictatuur, rechtsstaat, kapitalisme, postindustrieel, mondialisering, wij-zij-denken.",
        "Supranationaal kan beslissingen opleggen aan de lidstaten; intergouvernementeel niet.",
        "Vergelijk gelijkenissen én verschillen, met dezelfde vraag voor beide, en zonder te beoordelen wie beter was.",
        "Intercultureel contact: vreedzaam of gewelddadig, met wederzijdse perceptie en wederzijdse impact.",
        "Uitbuiting, cultuurvermenging en cultuurdominantie beschrijven elk een andere aard van contact.",
    ],
)

BUNDELS["restauratie-en-revolutie-het-congres-van-wenen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Restauratie en revolutie: het Congres van Wenen",
    onder="Hoe de grootmachten de kaart van Europa hertekenden, en waarom dat niet hield.",
    secties=[
        dict(kop="Wie en waar", blokken=[
            ("p", "<strong>Na de nederlaag van Napoleon Bonaparte</strong> kwamen de Europese grootmachten "
                  "<strong>in 1814 en 1815 in Wenen</strong> samen om de kaart van Europa te hertekenen. "
                  "<strong>De Oostenrijkse staatsman Metternich leidde het congres.</strong> "
                  "<strong>Oostenrijk, Pruisen, Rusland en Groot-Brittannië gaven de toon aan</strong>, en "
                  "<strong>Frankrijk mocht als verslagen land wél aan de onderhandelingen deelnemen</strong>: "
                  "Talleyrand kreeg een plaats aan de tafel, omdat een vernederd Frankrijk een bron van "
                  "nieuwe onrust zou zijn."),
            ("p", "<strong>Je situeert het congres aan het begin van de moderne tijd.</strong> Men noemt het "
                  "<strong>een scharnierpunt omdat het een tijdperk afsluit en een nieuw opent</strong>. "
                  "<strong>De beperking van 1815 als begin van de moderne tijd: het is een politieke en "
                  "westerse keuze, die elders weinig betekent.</strong> En het congres zelf "
                  "<strong>situeer je vooral politiek, met gevolgen in het sociale en culturele "
                  "domein</strong>."),
        ]),
        dict(kop="Drie beginselen", blokken=[
            ("p", tabel(["Beginsel", "Wat het betekent"], [
                ["Legitimiteit", "de vorstenhuizen van voor Napoleon krijgen hun troon terug"],
                ["Machtsevenwicht", "geen enkele staat mag zo sterk worden dat hij Europa overheerst"],
                ["Compensatie", "een staat die gebied afstaat, krijgt er elders iets voor terug"],
            ])),
            ("p", "Daaruit volgen de <strong>doelstellingen die de grootmachten in Wenen nastreefden</strong>: "
                  "<strong>het herstel van de oude vorstenhuizen</strong> en <strong>een evenwicht tussen de "
                  "grootmachten</strong>. Het woord voor dat herstel is <strong>de restauratie</strong>: "
                  "<strong>het herstel van de toestand van voor de Franse Revolutie en Napoleon</strong>. "
                  "Het <strong>machtsevenwicht</strong> is het <strong>streven dat geen enkele staat in "
                  "Europa te machtig mag worden</strong>."),
            ("p", "<strong>Het congres voerde in heel Europa géén democratie in</strong>: het "
                  "<strong>politieke gevolg was juist dat de vorsten hun absolute macht grotendeels "
                  "terugkregen</strong>. <strong>De grootmachten beslisten over de grenzen zonder de "
                  "bevolking te vragen wat zij wilde</strong>, en <strong>ze hielden geen rekening met de "
                  "taal en de cultuur van de bevolking bij het tekenen van de grenzen</strong>."),
        ]),
        dict(kop="De nieuwe kaart", blokken=[
            ("p", tabel(["Beslissing", "Wat er gebeurde"], [
                ["Het Verenigd Koninkrijk der Nederlanden",
                 "de nieuwe staat als buffer tegen Frankrijk: hij verenigde de noordelijke en de "
                 "zuidelijke Nederlanden en moest Frankrijk in het noorden insluiten. Willem I werd koning"],
                ["Pruisen", "gebieden langs de Rijn, met steenkool en ijzer"],
                ["Oostenrijk", "Lombardije en Venetië in Noord-Italië"],
                ["De Duitse Bond", "in de plaats van het oude Heilige Roomse Rijk: een losse Duitse Bond "
                                   "van zelfstandige staten. De aangesloten staten bleven zelfstandig en "
                                   "Oostenrijk had er een leidende rol in"],
                ["Zwitserland", "als neutrale staat erkend"],
                ["Frankrijk", "geen republiek zonder koning, maar de Bourbons terug op de troon"],
            ])),
        ]),
        dict(kop="De orde bewaken", blokken=[
            ("p", "In 1815 sloten <strong>de vorsten van Rusland, Oostenrijk en Pruisen de Heilige "
                  "Alliantie</strong> om de orde te bewaken. Daarna <strong>hielden de grootmachten "
                  "regelmatig congressen om samen op te treden tegen opstanden en revoluties</strong>: dat "
                  "<strong>congressysteem was bedoeld om revoluties in de kiem te smoren</strong>."),
            ("p", "<strong>Een bron uit 1820 noemt de Heilige Alliantie een verbond tegen de volkeren. Het "
                  "argument daarvoor: het verbond trad op tegen opstanden voor meer vrijheid.</strong> Wie "
                  "de alliantie verdedigde, zei dat ze de vrede bewaarde; beide uitspraken gaan over "
                  "dezelfde feiten met een ander belang erachter."),
        ]),
        dict(kop="Wat hield, en wat niet", blokken=[
            ("p", "<strong>Na 1815 bleef Europa tientallen jaren zonder een grote oorlog tussen de "
                  "grootmachten</strong>, en dat is de verdienste van het machtsevenwicht. Maar "
                  "<strong>de beslissingen van Wenen hielden niet tot het einde van de negentiende eeuw "
                  "ongewijzigd stand</strong>, en <strong>de ideeën van de Franse Revolutie verdwenen niet "
                  "volledig uit Europa</strong>: ze leefden bij de burgerij en bij de intellectuelen voort."),
            ("p", "<strong>Twee gevolgen werkten op langere termijn tegen het congres zelf: het "
                  "nationalisme bij volken die over staten verdeeld waren, en het liberalisme bij burgers "
                  "die grondrechten eisten.</strong> <strong>De Belgische revolutie van 1830 bewijst dat de "
                  "beslissingen van Wenen niet overal gedragen werden.</strong>"),
            ("p", "<strong>Leg je een kaart van Europa in 1815 naast een kaart in 1914, dan valt vooral op "
                  "dat Duitsland en Italië één staat geworden zijn.</strong> Precies wat Wenen had willen "
                  "verhinderen."),
            ("p", "<strong>Moet je beoordelen in welke mate de doelstellingen van Wenen bereikt zijn, dan is "
                  "dit het meest verdedigbare besluit: het machtsevenwicht hield een tijd, het herstel van "
                  "de oude orde niet.</strong> Een oordeel in geschiedenis klinkt dus zelden als een volmondig "
                  "ja of neen."),
        ]),
    ],
    onthoud=[
        "Wenen, 1814-1815, na Napoleon; Metternich leidt, Oostenrijk, Pruisen, Rusland en Groot-Brittannië beslissen, Frankrijk zit mee aan tafel.",
        "Drie beginselen: legitimiteit, machtsevenwicht en compensatie. De restauratie is het herstel van de toestand van voor 1789.",
        "Nieuw op de kaart: het Verenigd Koninkrijk der Nederlanden met Willem I, Pruisen aan de Rijn, Oostenrijk in Lombardije en Venetië, de Duitse Bond, een neutraal Zwitserland.",
        "De Heilige Alliantie en het congressysteem moesten revoluties in de kiem smoren.",
        "Het machtsevenwicht hield een tijd, het herstel van de oude orde niet: liberalisme en nationalisme werkten ertegen.",
    ],
)

BUNDELS["liberalisme-en-nationalisme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Liberalisme en nationalisme",
    onder="Twee ideologieën die de orde van Wenen onderuit haalden.",
    secties=[
        dict(kop="Het politieke liberalisme", blokken=[
            ("p", "Bij het <strong>liberalisme</strong> staat <strong>de vrijheid en de rechten van het "
                  "individu</strong> centraal. Het komt op bij de <strong>gegoede burgerij</strong>, die "
                  "bezit en kennis had maar geen politieke macht, en het bouwt op de "
                  "<strong>Verlichting</strong> en de <strong>Franse Revolutie</strong>."),
            ("p", "De eisen: <strong>vrijheid van meningsuiting en van pers</strong>, <strong>vrijheid van "
                  "vereniging en van godsdienst</strong>, <strong>gelijkheid voor de wet</strong>, een "
                  "<strong>grondwet die de macht van de vorst aan vaste regels bindt</strong>, een "
                  "<strong>parlement dat de regering controleert</strong> en beslist over de belastingen, en "
                  "de <strong>scheiding der machten</strong>, ook <strong>machtenscheiding</strong> genoemd: "
                  "<strong>wetgeven, besturen en rechtspreken liggen in verschillende handen</strong>."),
            ("p", "Over het stemrecht dachten zij smal: <strong>alleen wie genoeg belasting betaalt, mag "
                  "kiezen</strong>. Dat heet <strong>cijnskiesrecht</strong>. Het <strong>algemeen "
                  "enkelvoudig stemrecht was hun eis niet</strong>; dat werd de eis van de arbeidersbeweging."),
        ]),
        dict(kop="Het economisch liberalisme", blokken=[
            ("p", "<strong>Economisch liberalisme</strong> betekent dat <strong>de overheid de economie "
                  "zoveel mogelijk aan zichzelf overlaat</strong>. Die houding heet <strong>laissez-faire</strong>: "
                  "laat maar doen. <strong>Vraag en aanbod bepalen de prijzen en de lonen</strong>, en de "
                  "staat houdt zich beperkt tot <strong>orde, recht en veiligheid</strong>, de "
                  "<strong>nachtwachtstaat</strong>."),
            ("p", "Daar hoort vrije handel bij: <strong>invoerrechten, bijvoorbeeld op graan, moeten "
                  "weg</strong>. Voor de fabrikanten betekende dat <strong>de vrije hand</strong>: geen regels "
                  "over lonen, uren of kinderarbeid. Voor de arbeiders betekende het <strong>lange werkdagen "
                  "en lage lonen zonder bescherming</strong>. Een liberaal van 1830 vond dat de staat de "
                  "lonen <strong>niet</strong> moest vastleggen."),
        ]),
        dict(kop="Het nationalisme", blokken=[
            ("p", "Een <strong>natie</strong> is volgens het negentiende-eeuwse <strong>nationalisme</strong> "
                  "<strong>een gemeenschap met een eigen taal, cultuur en geschiedenis</strong>, en zo'n "
                  "natie hoort <strong>een eigen staat</strong> te krijgen. De <strong>romantiek</strong> "
                  "voedde dat met haar belangstelling voor eigen taal, volksverhalen en verleden; "
                  "woordenboeken en geschiedschrijving waren politiek werk."),
            ("p", tabel(["Vorm", "Streven", "Voorbeeld"], [
                ["Eenmaking", "verdeelde gebieden samenvoegen", "de Duitse Bond, Italië"],
                ["Onafhankelijkheid", "zich losmaken van een vreemde heerser", "Griekenland, Polen, België"],
            ])),
            ("p", "Het nationalisme <strong>botste met het Congres van Wenen</strong>, waar de grenzen "
                  "zonder de volken waren getekend. In het begin was het vooral bevrijdend bedoeld; "
                  "<strong>de uitsluitende en agressieve vorm kwam later, tegen 1900</strong>."),
        ]),
        dict(kop="Samen tegen de oude orde", blokken=[
            ("p", "<strong>Liberalisme en nationalisme werkten vaak samen</strong>: beide wilden af van een "
                  "vorst die alleen beslist. In 1830 kon een liberaal dezelfde opstand steunen als een "
                  "nationalist, <strong>elk om zijn eigen reden</strong>: de ene voor grondrechten en een "
                  "parlement, de andere voor een eigen staat."),
            ("p", "Beide zijn <strong>ideologieën</strong>: <strong>samenhangende stelsels van ideeën over de "
                  "samenleving</strong>. Uit zulke stelsels groeien partijen, en daarmee ook de "
                  "breuklijnen van de politiek."),
        ]),
        dict(kop="De liberale eisen in de praktijk", blokken=[
            ("p", "<strong>De vrijheden die de liberalen in de negentiende eeuw eisten</strong>: "
                  "<strong>de vrijheid van meningsuiting en van pers</strong> en <strong>de vrijheid van "
                  "vereniging en van godsdienst</strong>. <strong>Persvrijheid</strong> situeer je "
                  "<strong>in het politieke domein, met een culturele kant</strong>: ze gaat over macht en "
                  "controle, maar ook over wat je mag denken, schrijven en lezen. <strong>Lees je in een "
                  "bron uit 1840 een pleidooi voor persvrijheid, een grondwet en stemrecht voor wie bezit "
                  "heeft, dan herken je het liberalisme.</strong>"),
            ("p", "De <strong>grondwet</strong> is <strong>de wet die boven alle andere wetten staat en de "
                  "rechten van de burger vastlegt</strong>; de <strong>machtenscheiding</strong> is het "
                  "<strong>beginsel dat wetgeven, besturen en rechtspreken in verschillende handen "
                  "liggen</strong>. Over het bezit: het <strong>cijnskiesrecht</strong> is het stemrecht "
                  "dat <strong>enkel geldt voor wie genoeg belasting betaalt</strong>."),
            ("p", "<strong>De opkomst van het liberalisme</strong> verklaar je zo: <strong>de burgerij had "
                  "bezit en kennis, maar weinig politieke macht</strong>, en <strong>de ideeën van de "
                  "Verlichting lagen eraan ten grondslag</strong>. Daarom <strong>bleven de liberale eisen "
                  "na 1815 een halve eeuw terugkomen: de restauratie nam de onvrede en de ideeën niet "
                  "weg.</strong> <strong>De vorsten van de Heilige Alliantie steunden het liberalisme en het "
                  "nationalisme niet</strong>, maar traden er juist tegen op."),
            ("p", "In de economie heet die houding <strong>laissez-faire</strong> of <strong>economisch "
                  "liberalisme</strong>: <strong>de overheid moet de economie zoveel mogelijk aan zichzelf "
                  "overlaten</strong>. <strong>De rol die de economische liberalen aan de staat gaven, was "
                  "beperkt: orde, recht en veiligheid bewaken.</strong> Het <strong>verband met de "
                  "industrialisering</strong> is dan ook rechtlijnig: <strong>het economisch liberalisme gaf "
                  "de fabrikanten de vrije hand</strong>. <strong>Een liberaal uit 1830 vond dus niet dat de "
                  "staat de lonen in de fabrieken moest vastleggen</strong>; het <strong>gevolg voor de "
                  "arbeiders waren lange werkdagen en lage lonen zonder bescherming</strong>. Een "
                  "<strong>bron die pleit voor de afschaffing van de invoerrechten op graan</strong> is "
                  "daarmee ook economisch liberaal."),
        ]),
        dict(kop="Twee vormen van nationalisme", blokken=[
            ("p", "<strong>Het nationalisme kon in de negentiende eeuw twee vormen aannemen: het streven "
                  "naar eenmaking van verdeelde gebieden, en het streven naar onafhankelijkheid van een "
                  "vreemde heerser.</strong> <strong>In de Duitse gebieden hield het vooral een streven naar "
                  "eenmaking in</strong>: <strong>een bron uit 1848 die oproept om alle Duitse staten samen "
                  "te voegen tot één rijk, is nationalistisch</strong>."),
            ("p", "<strong>Waarom botste het nationalisme met de beslissingen van het Congres van Wenen? In "
                  "Wenen werden grenzen getekend zonder naar de volken te kijken.</strong> De argumenten van "
                  "de nationalisten kwamen uit het culturele domein: <strong>een eigen taal gold als een "
                  "argument voor een eigen staat</strong> en <strong>het eigen verleden werd als "
                  "gemeenschappelijke band gebruikt</strong>. Zo zit het <strong>verband met het culturele "
                  "domein</strong>: <strong>taal, verhalen en geschiedenis vormen de band van de "
                  "natie</strong>. De <strong>kunststroming die het nationalisme voedde met belangstelling "
                  "voor eigen taal en verleden, is de romantiek</strong>."),
            ("p", "<strong>Nationalisme betekende in de negentiende eeuw niet altijd vijandigheid tegenover "
                  "andere volken.</strong> In het begin ging het vooral om zelfbestuur en eigen taal; de "
                  "agressieve vorm, die andere volken minderwaardig noemt, komt later en wordt dan met het "
                  "imperialisme verbonden."),
        ]),
    ],
    onthoud=[
        "Liberalisme: individuele vrijheid, grondrechten, grondwet, parlement, scheiding der machten - maar cijnskiesrecht.",
        "Economisch liberalisme = laissez-faire: de staat blijft erbuiten, de nachtwachtstaat.",
        "Nationalisme: een natie met eigen taal, cultuur en geschiedenis hoort een eigen staat te krijgen.",
        "Twee vormen: eenmaking (Duitsland, Italië) en onafhankelijkheid (Griekenland, Polen, België).",
    ],
)

BUNDELS["het-ontstaan-van-belgie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het ontstaan van België",
    onder="Van het Verenigd Koninkrijk der Nederlanden over de revolutie van 1830 naar een eigen staat.",
    secties=[
        dict(kop="Het Verenigd Koninkrijk der Nederlanden", blokken=[
            ("p", "In <strong>1815</strong> besliste het Congres van Wenen dat <strong>de Zuidelijke "
                  "Nederlanden met het Noorden één koninkrijk zouden vormen</strong>, <strong>om een sterke "
                  "buffer tegen Frankrijk te vormen</strong>. <strong>Willem I</strong> werd koning, en hij "
                  "hield de beslissingen graag bij zichzelf."),
            ("p", tabel(["Grief", "Wie het aanging"], [
                ["De koning bemoeide zich met de benoeming van bisschoppen", "de katholieken"],
                ["Priesters moesten aan een rijksschool worden opgeleid", "de katholieken"],
                ["De persvrijheid werd beperkt en journalisten vervolgd", "de liberalen"],
                ["De ministers waren niet aan het parlement verantwoording verschuldigd", "de liberalen"],
                ["Vanaf 1823 werd het Nederlands de taal van bestuur en rechtspraak", "de Franstalige burgerij"],
                ["Het Zuiden had meer inwoners maar niet meer zetels", "beide"],
            ])),
            ("p", "Daar komt het economische verschil bij: <strong>het Noorden leefde van handel, het Zuiden "
                  "van industrie</strong>. Handelaars wilden lage invoerrechten, fabrikanten hoge; één tarief "
                  "kon niet beide dienen."),
            ("p", "Vanaf <strong>1828</strong> bundelden <strong>katholieken en liberalen hun krachten tegen "
                  "de koning</strong>. Dat heet het <strong>unionisme</strong>, door tijdgenoten ook een "
                  "<strong>monsterverbond</strong> genoemd."),
        ]),
        dict(kop="De revolutie van 1830", blokken=[
            ("p", "In augustus 1830 begonnen de onlusten in Brussel <strong>met rellen na een opvoering in "
                  "de Muntschouwburg</strong>. Honger, werkloosheid en duur brood na de mislukte oogsten van "
                  "<strong>1829 en 1830</strong> deden de rest; <strong>de julirevolutie in Parijs</strong> "
                  "van diezelfde zomer gaf het gevoel dat het kon lukken."),
            ("p", "In september vochten vrijwilligers in het <strong>Warandepark</strong>: "
                  "<strong>zij verdreven de Nederlandse troepen uit de stad</strong>. Willem I had "
                  "<strong>geaarzeld en dan zijn leger gestuurd</strong>, en die aarzeling heeft hem het "
                  "Zuiden gekost. Op <strong>4 oktober 1830</strong> riep het <strong>Voorlopig Bewind de "
                  "onafhankelijkheid van België uit</strong>."),
            ("p", "<strong>De revolutie was niet uitsluitend het werk van de arbeiders</strong>: de straat "
                  "was van hen, maar het Voorlopig Bewind en het Nationaal Congres waren zaken van de "
                  "burgerij."),
        ]),
        dict(kop="De grondwet van 1831", blokken=[
            ("p", "Het <strong>Nationaal Congres</strong> kwam in november 1830 samen om <strong>een "
                  "grondwet te schrijven en een staatsvorm te kiezen</strong>. Het koos <strong>een erfelijke "
                  "monarchie met een grondwet</strong>, en niet voor een republiek: dat laatste leek de "
                  "mogendheden te veel op Frankrijk, en België had hun erkenning nodig."),
            ("p", "De grondwet van <strong>1831</strong>: <strong>de macht van de koning wordt door de "
                  "grondwet begrensd</strong>, <strong>de ministers zijn verantwoording verschuldigd aan het "
                  "parlement</strong>, en er staan grondrechten in: <strong>vrijheid van pers en van "
                  "vereniging</strong>, <strong>vrijheid van godsdienst en van onderwijs</strong>, "
                  "<strong>gelijkheid voor de wet</strong>. <strong>Sociale rechten, zoals een recht op werk "
                  "of een uitkering bij ziekte, staan er niet in</strong>, en over loon of werktijd in de "
                  "fabrieken evenmin."),
            ("p", "Daarom heet ze <strong>voor haar tijd liberaal</strong>: ze bond de vorst aan regels en "
                  "gaf burgers grondrechten. <strong>Een democratie was België in 1831 niet</strong>: door "
                  "het cijnskiesrecht mocht <strong>ongeveer één op de honderd inwoners</strong> stemmen. De "
                  "<strong>vrijheid van onderwijs kwam zowel de katholieken als de liberalen gelegen</strong>, "
                  "en het unionisme hield tot <strong>1847</strong>, waarna de schoolstrijd kwam. De grondwet "
                  "liet de taal vrij, maar <strong>in de praktijk werd het Frans de taal van het bestuur</strong>."),
        ]),
        dict(kop="Erkenning en grenzen", blokken=[
            ("p", "Het Congres zocht <strong>een vorst uit het buitenland om de nieuwe staat erkend te "
                  "krijgen</strong>. <strong>Leopold I</strong> legde op <strong>21 juli 1831</strong> de eed "
                  "af op de grondwet; die dag is nog de nationale feestdag. Kort daarna <strong>viel Willem I "
                  "België opnieuw binnen</strong>: de <strong>Tiendaagse Veldtocht</strong> liep slecht af "
                  "voor België, en een Frans leger maakte er een einde aan."),
            ("p", "Op de <strong>Conferentie van Londen</strong> regelden <strong>de mogendheden de "
                  "erkenning en de grenzen</strong>, en legden zij België <strong>neutraliteit</strong> op: "
                  "<strong>het mocht geen partij kiezen in een oorlog</strong>. Die neutraliteit werd ook "
                  "door hen gewaarborgd; in 1914 bleek wat zo'n waarborg waard was."),
            ("p", "<strong>Willem I erkende de onafhankelijkheid pas in 1839</strong>, acht jaar na de "
                  "eedaflegging van Leopold I. Bij dat verdrag werden <strong>Limburg en Luxemburg "
                  "gesplitst</strong>, en België verloor een deel van beide."),
        ]),
        dict(kop="Van Wenen tot de opstand", blokken=[
            ("p", "<strong>Wat de grote mogendheden in 1815 over de Zuidelijke Nederlanden beslisten: ze "
                  "werden samengevoegd met het Noorden tot één koninkrijk</strong>, als buffer tegen "
                  "Frankrijk. <strong>Het Zuiden voelde zich in het parlement tekortgedaan omdat het meer "
                  "inwoners had maar niet meer zetels dan het Noorden.</strong>"),
            ("p", "<strong>De grieven van de katholieken in het Zuiden tegen Willem I: hij bemoeide zich met "
                  "de benoeming van bisschoppen</strong> en <strong>hij liet priesters aan een rijksschool "
                  "opleiden</strong>. <strong>De grieven van de liberalen: hij beperkte de persvrijheid en "
                  "liet journalisten vervolgen</strong>, en <strong>hij liet de ministers niet door het "
                  "parlement controleren</strong>. Daaruit groeide <strong>het unionisme</strong>, "
                  "<strong>de samenwerking van katholieken en liberalen tegen Willem I</strong>, ook het "
                  "monsterverbond genoemd."),
            ("p", "<strong>Vanaf 1823 maakte Willem I het Nederlands de taal van bestuur en rechtspraak in "
                  "Vlaanderen en Brabant.</strong> <strong>Dat taalbesluit werd niet in heel het Zuiden met "
                  "vreugde onthaald</strong>: de Franstalige burgerij en een deel van de geestelijkheid "
                  "zagen hun positie bedreigd, en veel bestuurstaal stond ver van het dialect dat de mensen "
                  "spraken."),
            ("p", "<strong>De honger en de werkloosheid van 1829 en 1830 maakten de onvrede in de steden "
                  "groter</strong>, en <strong>de julirevolutie in Parijs van diezelfde zomer gaf de "
                  "opstand van 1830 in Europa de wind in de zeilen</strong>: die gebeurtenis bewees dat een "
                  "vorst wél kon vallen. <strong>Willem I gaf de Zuidelijke Nederlanden in augustus 1830 "
                  "geen zelfbestuur</strong>; hij stuurde troepen, en na de Septemberdagen in Brussel was de "
                  "breuk onherstelbaar. <strong>De Belgische revolutie brak uit in 1830</strong>, en "
                  "<strong>daarmee werden de beslissingen van het Congres van Wenen doorbroken</strong>."),
        ]),
        dict(kop="De grondwet en de erkenning", blokken=[
            ("p", "<strong>De taak van het Nationaal Congres dat in november 1830 bijeenkwam: een grondwet "
                  "schrijven en een staatsvorm kiezen.</strong> <strong>De kenmerken van de Belgische "
                  "grondwet van 1831: de macht van de koning werd door de grondwet begrensd</strong> en "
                  "<strong>de ministers werden verantwoording verschuldigd aan het parlement</strong>. "
                  "<strong>De grondrechten die erin stonden: de vrijheid van pers en van vereniging</strong> "
                  "en <strong>de vrijheid van godsdienst en van onderwijs</strong>. Toch "
                  "<strong>gaf de grondwet van 1831 het stemrecht niet aan alle mannen van het land</strong>: "
                  "enkel wie genoeg belasting betaalde, mocht kiezen."),
            ("p", "<strong>De neutraliteit die de mogendheden aan België oplegden, betekende dat België geen "
                  "partij mocht kiezen in een oorlog.</strong> <strong>Willem I erkende de Belgische "
                  "onafhankelijkheid met een verdrag in 1839.</strong>"),
            ("p", "<strong>Over het unionisme na 1830: katholieken en liberalen bestuurden het land "
                  "samen</strong>, maar <strong>hun samenwerking hield geen halve eeuw lang stand</strong>. "
                  "Zodra de gemeenschappelijke tegenstander weg was, kwam de schoolkwestie boven, en zo "
                  "ontstonden de eerste partijen."),
            ("p", "<strong>De ideologieën van het vorige thema zie je in 1830 aan het werk: het liberalisme, "
                  "in de eis voor grondrechten en een grondwet, en het nationalisme, in het streven naar een "
                  "eigen staat.</strong>"),
        ]),
    ],
    onthoud=[
        "1815: Zuiden en Noorden samen onder Willem I. Grieven over godsdienst, pers, ministers, taal, economie en zetels.",
        "Unionisme 1828: katholieken en liberalen samen tegen de koning.",
        "Augustus 1830 rellen na de opera, september het Warandepark, 4 oktober de onafhankelijkheid.",
        "Grondwet 1831: grondrechten, ministeriële verantwoordelijkheid, maar cijnskiesrecht (één op honderd).",
        "Leopold I eed op 21 juli 1831; Willem I erkent België pas in 1839.",
    ],
)

BUNDELS["de-eerste-en-de-tweede-industriele-revolutie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De eerste en de tweede industriële revolutie",
    onder="Van de stoommachine in Engeland tot elektriciteit, aardolie en de grote onderneming.",
    secties=[
        dict(kop="De eerste industriële revolutie", blokken=[
            ("p", "De eerste industriële revolutie begon <strong>in Engeland</strong>, in de tweede helft van "
                  "de achttiende eeuw. <strong>Niet in Duitsland</strong>, dat volgde veel later. Waarom "
                  "daar? <strong>Steenkool en ijzererts lagen er dicht bij elkaar in de bodem</strong>, "
                  "<strong>kapitaal uit de handel en de kolonies kon er belegd worden</strong>, en de "
                  "<strong>bevolking groeide</strong>, wat zowel werkvolk als kopers opleverde."),
            ("p", "De <strong>landbouw</strong> was een voorwaarde: <strong>meer opbrengst per akker voedde "
                  "de groeiende steden</strong> en maakte handen vrij voor de fabriek. De landbouw "
                  "<strong>verdween niet</strong>."),
            ("p", "De <strong>stoommachine</strong>, verbeterd door <strong>James Watt</strong>, maakte van "
                  "<strong>steenkool de motor van de industrie</strong>: warmte werd beweging, en een fabriek "
                  "hoefde niet meer aan een rivier te staan. De <strong>textielnijverheid</strong> werd als "
                  "eerste gemechaniseerd. De <strong>spoorweg</strong> zorgde ervoor dat "
                  "<strong>grondstoffen en goederen snel en goedkoop vervoerd konden worden</strong>, zodat "
                  "een fabriek voor een markt ver buiten haar streek kon werken."),
            ("p", "<strong>Voor de industriële revolutie werd er thuis of in kleine werkplaatsen "
                  "geproduceerd</strong>. <strong>De eerste fabrieken stonden bij een steenkoolbekken of bij "
                  "een waterloop</strong>, want brandstof vervoeren was duur. In de fabriek "
                  "<strong>bepaalde de klok wanneer een arbeider begon en stopte</strong>, met een boete voor "
                  "wie te laat kwam. Voor plattelandsmensen was dat vaste ritme volkomen nieuw."),
        ]),
        dict(kop="België als eerste op het vasteland", blokken=[
            ("p", "<strong>België industrialiseerde als eerste land op het Europese vasteland</strong>. De "
                  "eerste industriegebieden lagen in <strong>de steenkoolbekkens van Luik, Henegouwen en de "
                  "Borinage</strong>, dus <strong>Wallonië was de streek van de steenkool en het staal</strong>, "
                  "en in <strong>de textielstad Gent met haar spinnerijen en weverijen</strong>. "
                  "<strong>De Kempense mijnen openden pas na 1900</strong>; <strong>Vlaanderen "
                  "industrialiseerde later dan Wallonië</strong> en kende rond 1845 nog grote armoede in de "
                  "linnennijverheid."),
            ("p", "<strong>Lieven Bauwens</strong> bracht rond 1800 <strong>een Engelse spinmachine</strong> "
                  "naar Gent; Engeland verbood de uitvoer, dus smokkelde hij ze in stukken binnen. "
                  "<strong>John Cockerill</strong> bouwde in Seraing machines en later locomotieven: België "
                  "industrialiseerde grotendeels <strong>met machines en vaklui uit Engeland</strong>."),
            ("p", "In <strong>1835</strong> opende <strong>de lijn tussen Brussel en Mechelen</strong>, de "
                  "<strong>eerste spoorlijn van het vasteland</strong>. De jonge Belgische staat legde zelf "
                  "een spoornet aan, <strong>om de handel niet van de Nederlandse waterwegen af te laten "
                  "hangen</strong>."),
        ]),
        dict(kop="De tweede industriële revolutie", blokken=[
            ("p", "De tweede industriële revolutie wordt gesitueerd <strong>vanaf ongeveer 1870</strong>, tot "
                  "de Eerste Wereldoorlog. De nieuwe energiebronnen zijn <strong>elektriciteit</strong> en "
                  "<strong>aardolie</strong>; steenkool en waterkracht dreven de eerste golf al aan."),
            ("p", "Nieuwe bedrijfstakken: <strong>de chemische nijverheid met kunstmest en verfstoffen</strong> "
                  "en <strong>de elektrotechniek met lampen, dynamo's en motoren</strong>. De "
                  "<strong>verbrandingsmotor</strong> maakte <strong>vervoer over de weg met auto's en "
                  "vrachtwagens</strong> mogelijk: het nieuwe was dat een voertuig zijn brandstof meenam. "
                  "<strong>De wetenschap kwam de fabriek binnen</strong>: bedrijven richtten "
                  "<strong>eigen laboratoria voor onderzoek</strong> op."),
            ("p", "<strong>De nieuwe machines en labo's vroegen heel veel kapitaal</strong>, en daarom werden "
                  "de bedrijven groot. Men bundelde geld in een <strong>naamloze vennootschap</strong>, "
                  "<strong>een onderneming waarvan het kapitaal in aandelen verdeeld is</strong>, met banken "
                  "ernaast. Een <strong>kartel</strong> is <strong>een afspraak tussen bedrijven over prijzen "
                  "of markten</strong>, waarmee de onderlinge concurrentie uitgeschakeld werd. "
                  "<strong>De grote ondernemingen verdwenen niet</strong>: ze werden reuzen."),
        ]),
        dict(kop="Gevolgen voor wonen, werken en bevolking", blokken=[
            ("p", "De <strong>demografische transitie</strong> betekent dat <strong>het sterftecijfer eerst "
                  "daalde en het geboortecijfer pas later</strong>; tussen die twee dalingen groeide de "
                  "bevolking snel. <strong>De industrialisering ging in Europa samen met een snelle groei van "
                  "de bevolking</strong>, en met <strong>verstedelijking</strong>, ook "
                  "<strong>urbanisatie</strong> genoemd: <strong>de trek van mensen van het platteland naar "
                  "de stad</strong>. Het aantal inwoners van steden als Gent, Luik en Verviers steeg sterk, "
                  "<strong>vooral in de tweede helft van de eeuw</strong>."),
            ("p", "Arbeiders woonden vaak <strong>in kleine huisjes rond een gesloten koer, met weinig "
                  "licht</strong>: de beluiken, met <strong>één pomp en één toilet voor veel gezinnen</strong>, "
                  "waar <strong>tyfus en cholera</strong> om zich heen grepen. <strong>Kinderarbeid</strong> "
                  "betekende dat <strong>kinderen lange dagen voor een laag loon werkten</strong>; "
                  "<strong>in België was dat in 1850 bij geen enkele wet beperkt</strong>, de eerste wet kwam "
                  "er in <strong>1889</strong>."),
            ("p", "Rond 1880 <strong>duurde de werkdag vaak twaalf uur of langer</strong> en was er "
                  "<strong>geen vergoeding bij een arbeidsongeval</strong>. <strong>Vakantie en een "
                  "minimumloon zijn verworvenheden van de twintigste eeuw</strong>. De spoorwegen en de "
                  "stoomschepen maakten <strong>de wereldhandel veel groter</strong>. De gevolgen situeer je "
                  "<strong>in het economische domein, met de fabriek en de handel</strong>, en <strong>in het "
                  "sociale domein, met het wonen en het werken</strong>."),
        ]),
        dict(kop="Waar het begon, en waar in België", blokken=[
            ("p", "<strong>De voorwaarden die Engeland hielpen als eerste te industrialiseren: steenkool en "
                  "ijzererts lagen er dicht bij elkaar in de bodem</strong>, en <strong>kapitaal uit de "
                  "handel en de kolonies kon er belegd worden</strong>. <strong>De uitvinding die van "
                  "steenkool de motor van de industrie maakte, is de stoommachine.</strong> <strong>De "
                  "eerste industriële revolutie begon dus niet in de negentiende eeuw in Duitsland</strong>, "
                  "maar in de achttiende eeuw in Engeland; Duitsland volgde pas later."),
            ("p", "<strong>De eerste industriegebieden in België waren de steenkoolbekkens van Luik, "
                  "Henegouwen en de Borinage</strong>, en <strong>de textielstad Gent met haar spinnerijen "
                  "en weverijen</strong>. Dat waren de streken met kolen, of met een haven en een traditie "
                  "van textiel. <strong>De Gentse ondernemer Lieven Bauwens bracht rond 1800 een Engelse "
                  "spinmachine naar hier</strong>, buiten de Engelse uitvoerverboden om. <strong>In 1835 "
                  "werd de lijn tussen Brussel en Mechelen geopend, de eerste spoorlijn van het "
                  "vasteland.</strong>"),
        ]),
        dict(kop="Het leven in de negentiende-eeuwse industriestad", blokken=[
            ("p", "<strong>Wat de fabriek voor de werktijd van een arbeider betekende: de klok van de "
                  "fabriek bepaalde wanneer hij begon en stopte.</strong> Niet het daglicht, niet het "
                  "seizoen en niet hij zelf."),
            ("p", "<strong>Hoe arbeiders in de negentiende-eeuwse industriesteden vaak woonden: in kleine "
                  "huisjes rond een gesloten koer, met weinig licht.</strong> <strong>Kinderarbeid in de "
                  "negentiende-eeuwse fabriek betekent dat kinderen lange dagen werkten voor een laag "
                  "loon</strong>, omdat ze goedkoop waren en in kleine ruimtes pasten."),
            ("p", "<strong>De spoorwegen en de stoomschepen maakten de wereldhandel in de negentiende eeuw "
                  "veel groter.</strong> <strong>De gevolgen van de industriële revolutie situeer je in het "
                  "economische domein, met de fabriek en de handel, en in het sociale domein, met het wonen "
                  "en het werken</strong>, en via de sociale wetten ook in het politieke."),
            ("p", "Twee bronnen om te lezen. <strong>Zie je een prent van een fabriek met hoge schoorstenen, "
                  "naast rijen kleine huisjes, dan herken je de negentiende eeuw, tijdens de "
                  "industrialisering.</strong> En <strong>een grafiek met het aantal inwoners van Gent "
                  "tussen 1800 en 1900 laat een stijging zien, vooral in de tweede helft van de eeuw</strong>, "
                  "want de fabrieken trokken mensen van het platteland."),
        ]),
    ],
    onthoud=[
        "Eerste industriële revolutie: Engeland, steenkool, stoommachine (Watt), textiel, spoorweg.",
        "België als eerste op het vasteland: Wallonië steenkool en staal, Gent textiel, Bauwens en Cockerill, spoorlijn Brussel-Mechelen 1835.",
        "Tweede industriële revolutie vanaf 1870: elektriciteit en aardolie, chemie en elektrotechniek, labo's, naamloze vennootschappen en kartels.",
        "Gevolgen: verstedelijking, demografische transitie, beluiken, kinderarbeid, twaalfurige werkdag.",
    ],
)

BUNDELS["ongelijkheden-klassenmaatschappij-en-sociale-strijd-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Ongelijkheden: klassenmaatschappij en sociale strijd",
    onder="Van standen naar klassen, en van het coalitieverbod naar het algemeen stemrecht.",
    secties=[
        dict(kop="Van standen naar klassen", blokken=[
            ("p", "In een <strong>standenmaatschappij ligt je plaats bij je geboorte vast</strong>, met "
                  "<strong>voorrechten bij de wet</strong> voor de adel en eigen rechtbanken voor de "
                  "geestelijkheid. In een <strong>klassenmaatschappij hangt je plaats af van je bezit en je "
                  "positie in de productie</strong>: bezit je een fabriek, of enkel je arbeid?"),
            ("p", tabel(["Klasse", "Wie", "Wat zij bezitten"], [
                ["De grote burgerij", "fabrikanten, bankiers, grote handelaars", "kapitaal en productiemiddelen"],
                ["De kleine burgerij", "winkeliers, ambachtslui, lagere bedienden", "wat bezit, soms wat personeel"],
                ["De arbeidersklasse", "mijnwerkers, spinners, dagloners", "enkel hun arbeidskracht"],
            ])),
            ("p", "De <strong>arbeidersklasse</strong> heet bij Marx het <strong>proletariaat</strong>. De "
                  "<strong>grote burgerij had zowel het geld als de politieke macht</strong>, want door het "
                  "cijnskiesrecht mochten juist zij kiezen. Voor de wet waren alle burgers gelijk; "
                  "<strong>in de praktijk bleven de verschillen tussen arm en rijk erg groot</strong> en kon "
                  "slechts een enkeling opklimmen."),
        ]),
        dict(kop="De sociale kwestie", blokken=[
            ("p", "De <strong>sociale kwestie</strong> is <strong>de vraag wat er met de armoede van de "
                  "arbeiders moest gebeuren</strong>. Rond 1880 was er <strong>geen enkele wettelijke "
                  "bescherming bij ziekte of een ongeval</strong>: wie niet kon werken, kreeg niets, en een "
                  "ongeval kon een gezin in één dag tot de bedelstaf brengen."),
            ("p", "<strong>Kinderen en vrouwen werkten in de fabrieken en de mijnen omdat hun loon lager was "
                  "en het gezin dat geld nodig had</strong>. <strong>Uitbetaling in natura</strong> betekende "
                  "dat <strong>het loon in bonnen voor de winkel van de fabriek werd betaald</strong>, waar de "
                  "prijzen hoger lagen; een wet van <strong>1887</strong> verplichtte uitbetaling in geld."),
            ("p", "Ook <strong>in de landbouw en in de huisnijverheid was de armoede groot</strong>: de "
                  "crisis in de Vlaamse vlasnijverheid rond 1845 bracht honger en tyfus op het platteland. "
                  "Een verslag uit <strong>1843</strong> over kinderen van negen jaar die twaalf uur in een "
                  "spinnerij werken, toont dat <strong>kinderarbeid toen gewoon en wettelijk toegelaten "
                  "was</strong>."),
        ]),
        dict(kop="De middelen van de arbeidersbeweging", blokken=[
            ("p", "Het <strong>coalitieverbod</strong> betekende dat <strong>arbeiders zich niet mochten "
                  "verenigen om loon te eisen</strong>. In België werd het <strong>in 1866 opgeheven</strong>; "
                  "<strong>van 1830 tot 1866 was zo'n vereniging dus niet wettig</strong>. Het stond in de "
                  "strafwet, dus <strong>in het politieke domein, met gevolgen in het sociale</strong>."),
            ("p", "De middelen: <strong>de staking, om het werk stil te leggen</strong>, en <strong>de "
                  "vakbond, om samen sterker te staan</strong>. Een <strong>weerstandskas of mutualiteit</strong> "
                  "was <strong>een kas waar arbeiders samen geld in legden voor slechte dagen</strong>; "
                  "daaruit groeiden de ziekenfondsen en de stakingskassen. Een <strong>coöperatie</strong> is "
                  "<strong>een winkel of bakkerij die de arbeiders samen bezitten</strong>, zoals Vooruit in "
                  "Gent. <strong>De beweging bestond dus niet enkel uit vakbonden</strong>, en ook "
                  "<strong>katholieken richtten arbeidersverenigingen op</strong>."),
            ("p", "In <strong>1885</strong> werd de <strong>Belgische Werkliedenpartij</strong> opgericht om "
                  "de arbeiders politiek te vertegenwoordigen."),
        ]),
        dict(kop="Van onrust naar wetten en stemrecht", blokken=[
            ("p", "In <strong>1886</strong> brak in de Waalse industriegebieden <strong>een golf van "
                  "stakingen en onlusten</strong> uit; het leger werd ingezet en er vielen doden. Het gevolg: "
                  "<strong>de eerste sociale wetten van het land</strong>, na een onderzoekscommissie. "
                  "<strong>De wet van 1889 regelde de arbeid van vrouwen en kinderen in de fabrieken</strong>: "
                  "kinderen onder de twaalf mochten er niet meer werken. <strong>De eerste sociale wetten "
                  "kwamen er dus niet kort na de onafhankelijkheid</strong>, maar meer dan een halve eeuw "
                  "later, <strong>onder druk van stakingen en onrust</strong>."),
            ("p", "<strong>Zonder stemrecht kon de beweging geen sociale wetten laten stemmen</strong>; "
                  "daarom was het algemeen stemrecht de kerneis. De <strong>algemene staking van 1893</strong> "
                  "leverde het <strong>algemeen meervoudig stemrecht voor mannen</strong> op: <strong>elke man "
                  "stemt, en sommigen krijgen extra stemmen</strong> op grond van bezit, diploma of gezin. "
                  "<strong>Elke stem had dus niet hetzelfde gewicht</strong>."),
            ("p", "Pas in <strong>1919</strong> mochten de Belgische mannen met <strong>één stem per "
                  "man</strong> kiezen, dus <strong>het algemeen enkelvoudig stemrecht kwam er niet al in "
                  "1893</strong>. De <strong>vrouwen</strong> mochten voor het parlement pas in "
                  "<strong>1948</strong> stemmen, na de Tweede Wereldoorlog; voor de gemeente mochten zij "
                  "eerder. <strong>De sociale zekerheid zoals wij die kennen, bestond in 1900 nog niet</strong>: "
                  "die werd vanaf 1944 opgebouwd."),
            ("p", "De sociale strijd is <strong>een gevolg van de industriële revolutie</strong>: <strong>de "
                  "fabriek bracht veel arbeiders met dezelfde belangen samen</strong>. Wie thuis alleen weeft, "
                  "staat alleen; wie met duizend anderen in één zaal staat, kan samen handelen."),
        ]),
        dict(kop="De klassen van de negentiende-eeuwse samenleving", blokken=[
            ("p", "<strong>De klassen die men in de negentiende-eeuwse samenleving onderscheidt: de grote "
                  "burgerij van fabrikanten, bankiers en handelaars</strong>, en <strong>de arbeidersklasse "
                  "van wie van zijn loon moet leven</strong>. Daartussen zit de kleine burgerij: "
                  "<strong>winkeliers, ambachtslui en lagere bedienden behoorden tot die groep</strong>. "
                  "<strong>De grote burgerij had in de negentiende eeuw zowel het geld als de politieke "
                  "macht</strong>, want het cijnskiesrecht gaf de stem aan wie belasting betaalde."),
            ("p", "<strong>In een klassenmaatschappij bepaalt je geboorte niet voorgoed je plaats in de "
                  "samenleving</strong>: voor de wet is iedereen gelijk, en opklimmen kan, al blijft het "
                  "voor wie arm geboren wordt heel moeilijk. <strong>Met de sociale kwestie van de "
                  "negentiende eeuw bedoelt men de vraag wat er met de armoede van de arbeiders moest "
                  "gebeuren.</strong> <strong>Ook in de landbouw en in de huisnijverheid was de armoede in "
                  "de negentiende eeuw groot</strong>; de fabriek maakte ze zichtbaar, niet nieuw."),
            ("p", "<strong>Hoe een arbeidersgezin rond 1880 beschermd was tegen ziekte of een ongeval: er "
                  "was geen enkele wettelijke bescherming voorzien.</strong> Wie niet kon werken, viel "
                  "terug op familie, op een ziekenkas of op de armenzorg. <strong>Over de arbeidersbuurten "
                  "van de negentiende eeuw: veel gezinnen deelden één waterpomp en één toilet</strong>, en "
                  "<strong>besmettelijke ziekten als tyfus en cholera grepen er om zich heen</strong>, want "
                  "het drinkwater stond dicht bij de beerput."),
            ("p", "<strong>Uitbetaling in natura, waar arbeiders zich tegen verzetten, is loon dat in bonnen "
                  "voor de winkel van de fabriek betaald werd</strong>: de arbeider kon zijn geld dan enkel "
                  "bij zijn eigen werkgever besteden, aan diens prijzen."),
        ]),
        dict(kop="De strijd en de eerste wetten", blokken=[
            ("p", "<strong>De middelen die de arbeiders in hun sociale strijd gebruikten: de staking, om het "
                  "werk stil te leggen</strong>, en <strong>de vakbond, om samen sterker te staan</strong>. "
                  "Een <strong>staking</strong> is <strong>het samen stilleggen van het werk om eisen af te "
                  "dwingen</strong>. Dat was lang verboden: <strong>arbeiders mochten in België van 1830 tot "
                  "1866 niet wettig een vakbond oprichten</strong>, want het coalitieverbod verbood zich te "
                  "verenigen. <strong>Het coalitieverbod situeer je in het politieke domein, met gevolgen in "
                  "het sociale.</strong>"),
            ("p", "<strong>Het gevolg van de onrust van 1886 op de wetgeving: er kwamen de eerste sociale "
                  "wetten van het land.</strong> <strong>Ook katholieken richtten in de negentiende eeuw "
                  "arbeidersverenigingen op</strong>, naast de socialistische, elk met eigen ziekenkassen en "
                  "cooperaties."),
            ("p", "<strong>Na de invoering van het algemeen meervoudig stemrecht had niet elke stem "
                  "hetzelfde gewicht</strong>: wie bezit, diploma's of een gezin had, kreeg een of twee "
                  "stemmen extra. Pas in 1919 kwam er één stem per man. <strong>Lees je een pamflet uit 1890 "
                  "dat één man één stem en een werkdag van tien uur eist, dan komt het van de "
                  "arbeidersbeweging.</strong>"),
        ]),
    ],
    onthoud=[
        "Standenmaatschappij: geboorte. Klassenmaatschappij: bezit en positie in de productie.",
        "Sociale kwestie: geen bescherming bij ziekte of ongeval, kinder- en vrouwenarbeid, uitbetaling in natura tot 1887.",
        "Coalitieverbod opgeheven in 1866; middelen: staking, vakbond, weerstandskas, coöperatie, partij (BWP 1885).",
        "1886 onrust → eerste sociale wetten (1889 vrouwen- en kinderarbeid). 1893 meervoudig, 1919 enkelvoudig, vrouwen 1948.",
    ],
)

BUNDELS["marxisme-sociaaldemocratie-christendemocratie-en-migratie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Marxisme, sociaaldemocratie, christendemocratie en migratie",
    onder="Drie antwoorden op de sociale kwestie, en de mensen die voor werk verhuisden.",
    secties=[
        dict(kop="Het marxisme", blokken=[
            ("p", "<strong>Karl Marx</strong> schreef samen met <strong>Friedrich Engels</strong> het "
                  "<strong>Communistisch Manifest</strong>, in 1848. Volgens het <strong>marxisme</strong> is "
                  "<strong>de strijd tussen de klassen om de productiemiddelen de motor van de "
                  "geschiedenis</strong>: <strong>de geschiedenis is een opeenvolging van klassenstrijden</strong>."),
            ("p", "De <strong>meerwaarde</strong> is <strong>het verschil tussen wat de arbeid opbrengt en "
                  "wat het loon kost</strong>; die houdt de eigenaar in zijn zak, en daarin zag Marx de "
                  "uitbuiting. Zijn eisen: <strong>de productiemiddelen moeten gemeenschappelijk bezit "
                  "worden</strong> en <strong>een revolutie van de arbeiders is onvermijdelijk</strong>. "
                  "<strong>Dat de fabrieken eigendom van hun fabrikanten blijven, is juist de liberale "
                  "stelling</strong>, niet de zijne."),
            ("p", "Het eindpunt is <strong>een samenleving zonder klassen en zonder privé-bezit</strong> van "
                  "fabrieken; op weg daarnaartoe voorzag Marx een tussenfase, de <strong>dictatuur van het "
                  "proletariaat</strong>. Hij verwachtte dat <strong>het kapitalisme aan zijn eigen "
                  "tegenstellingen ten onder zou gaan</strong>. Omdat <strong>de arbeiders van elk land "
                  "hetzelfde belang hadden</strong>, riep hij hen op zich over de grenzen te verenigen; "
                  "daarvoor werden internationales opgericht. Het marxisme situeer je <strong>in het "
                  "economische domein, met het bezit van de fabrieken</strong>, en <strong>in het politieke "
                  "domein, met de macht in de staat</strong>."),
        ]),
        dict(kop="De sociaaldemocratie", blokken=[
            ("p", "Rond 1900 verschilden de socialisten <strong>over de weg: revolutie of hervorming</strong>. "
                  "Wie voor hervormingen koos, werd <strong>sociaaldemocraat</strong>; wie bij de revolutie "
                  "bleef, werd later communist. De <strong>sociaaldemocratie wil de samenleving stap voor "
                  "stap hervormen</strong>, met <strong>een partij in het parlement, met verkozen "
                  "afgevaardigden</strong> en <strong>vakbonden die met de werkgevers onderhandelen</strong>. "
                  "Die stroming heet ook <strong>het reformisme</strong>."),
            ("p", "<strong>Zij had het algemeen stemrecht nodig om haar plannen te kunnen uitvoeren</strong>. "
                  "Na 1945 werd <strong>een stelsel van sociale zekerheid voor iedereen</strong> de kern van "
                  "haar programma: pensioen, kinderbijslag, ziekteverzekering en werkloosheidsuitkering, de "
                  "welvaartsstaat. <strong>Over het doel waren marxisme en sociaaldemocratie het eens, over "
                  "de weg niet.</strong>"),
        ]),
        dict(kop="De christendemocratie", blokken=[
            ("p", "De pauselijke brief <strong>Rerum Novarum</strong> van <strong>1891</strong> gaf de "
                  "christelijke arbeidersbeweging haar grondslag. Daarin staat dat <strong>de arbeider recht "
                  "heeft op een rechtvaardig loon</strong> en dat <strong>arbeiders zich in eigen "
                  "verenigingen mogen organiseren</strong>."),
            ("p", "Zij <strong>wijst aan het economisch liberalisme af dat de markt alleen de lonen en de "
                  "werktijden bepaalt</strong>: een loon moest een gezin kunnen onderhouden. Aan het marxisme "
                  "wijst zij <strong>de klassenstrijd en de afschaffing van het privé-bezit</strong> af: "
                  "<strong>het privé-bezit blijft, met plichten tegenover de werknemers erbij</strong>, en "
                  "klassen zijn geen vijanden maar groepen die moeten samenwerken."),
            ("p", "In België organiseerde zij zich <strong>met eigen vakbonden, ziekenkassen en "
                  "verenigingen</strong>. Zo groeide naast de socialistische een tweede <strong>zuil</strong>: "
                  "<strong>een netwerk van verenigingen, scholen, vakbonden en ziekenkassen van één "
                  "strekking</strong>. Men noemt dat de <strong>verzuiling</strong>."),
        ]),
        dict(kop="Migratie", blokken=[
            ("p", "In de negentiende eeuw trokken miljoenen Europeanen naar Amerika: <strong>armoede en "
                  "honger dreven hen weg, werk en grond lokten hen</strong>. Die oorzaken heten "
                  "<strong>duwfactoren</strong> (ook pushfactoren) en trekfactoren. <strong>Ook Belgen "
                  "trokken als landverhuizer weg</strong>, vooral uit arme streken in Vlaanderen. Bij de "
                  "industrialisering zelf hoort <strong>de trek van het platteland naar de "
                  "industriesteden</strong>."),
            ("p", "Na 1945 sloot België akkoorden <strong>omdat er voor de mijnen en de heropbouw te weinig "
                  "arbeiders waren</strong>: met <strong>Italië in 1946</strong>, later met Spanje en "
                  "Griekenland, en in <strong>1964 met Marokko en Turkije</strong>. In <strong>1956</strong> "
                  "kostte <strong>een brand in de steenkoolmijn van Marcinelle 262 mensen het leven</strong>, "
                  "veel van hen Italiaanse mijnwerkers."),
            ("p", "<strong>De gastarbeiders werden gehaald voor werk dat hier bleef liggen</strong>, in de "
                  "mijnen, de bouw en de staalnijverheid. In <strong>1974 legde de regering de aanwerving van "
                  "nieuwe arbeiders stil</strong>, de migratiestop. <strong>Dat was geen einde van alle "
                  "migratie</strong>: gezinshereniging bleef mogelijk."),
        ]),
        dict(kop="Drie antwoorden op de sociale kwestie", blokken=[
            ("p", "<strong>De klassenstrijd</strong> is volgens Marx <strong>de strijd tussen de bezittende "
                  "en de werkende klasse</strong>. <strong>Lees je een tekst uit 1870 die oproept de "
                  "fabrieken aan de gemeenschap te geven en de staat van de burgerij af te breken, dan "
                  "herken je die ideologie: het marxisme.</strong> <strong>Het marxisme situeer je in het "
                  "economische domein, met het bezit van de fabrieken, en in het politieke domein, met de "
                  "macht in de staat.</strong>"),
            ("p", "<strong>Waarover de socialisten rond 1900 onderling van mening gingen verschillen: over "
                  "de weg, revolutie of hervorming.</strong> <strong>Wat de sociaaldemocratie kenmerkt: zij "
                  "wil de samenleving stap voor stap hervormen.</strong> <strong>De middelen die ze "
                  "gebruikte om haar doelen te bereiken: een partij in het parlement, met verkozen "
                  "afgevaardigden</strong>, en <strong>vakbonden die met de werkgevers onderhandelen</strong>. "
                  "<strong>Na 1945 werd een stelsel van sociale zekerheid voor iedereen de kern van het "
                  "sociaaldemocratische programma.</strong> <strong>Lees je een programma uit 1900 dat "
                  "stemrecht, een wet op de werkdag en een ziekenkas eist, dan herken je de "
                  "sociaaldemocratie.</strong>"),
            ("p", "<strong>De standpunten van Rerum Novarum: de arbeider heeft recht op een rechtvaardig "
                  "loon</strong>, en <strong>arbeiders mogen zich in eigen verenigingen organiseren</strong>. "
                  "<strong>Rerum Novarum verdedigde dus het recht van arbeiders om zich te verenigen</strong>, "
                  "maar wees de klassenstrijd af: werkgever en werknemer hadden volgens de encycliek plichten "
                  "tegenover elkaar."),
        ]),
        dict(kop="Migratie van en naar België", blokken=[
            ("p", "<strong>Duwfactoren</strong> zijn <strong>de oorzaken die iemand uit zijn eigen streek "
                  "wegduwen</strong>, zoals armoede, oorlog of werkloosheid; trekfactoren zijn wat elders "
                  "aantrekt, zoals werk en veiligheid. <strong>In de negentiende eeuw trokken ook Belgen als "
                  "landverhuizer naar andere werelddelen.</strong>"),
            ("p", "<strong>Waarom België na 1945 akkoorden sloot om arbeiders uit het buitenland te halen: "
                  "er waren voor de mijnen en de heropbouw te weinig arbeiders.</strong> <strong>De "
                  "gastarbeiders van de jaren vijftig en zestig werden naar België gehaald voor werk dat "
                  "hier bleef liggen.</strong> Eerst kwamen Italianen, en <strong>in 1964 sloot België "
                  "akkoorden over arbeidsmigratie met Marokko en Turkije</strong>. <strong>In 1974 legde de "
                  "regering de aanwerving van nieuwe arbeiders stil.</strong>"),
            ("p", "<strong>Samengevat over de arbeidsmigratie naar België: ze begon met akkoorden voor de "
                  "steenkoolmijnen</strong>, en <strong>ze werd in 1974 officieel stilgelegd voor nieuwe "
                  "arbeiders</strong>. Gezinshereniging en studie bleven wel mogelijk, dus de migratie "
                  "stopte niet, ze veranderde van vorm."),
        ]),
    ],
    onthoud=[
        "Marxisme: klassenstrijd, meerwaarde, productiemiddelen gemeenschappelijk, revolutie, klasseloze samenleving.",
        "Sociaaldemocratie: hervormen langs parlement en vakbond; na 1945 de sociale zekerheid.",
        "Rerum Novarum 1891: rechtvaardig loon en eigen verenigingen, maar geen klassenstrijd en privé-bezit blijft.",
        "Migratie: duw- en trekfactoren; akkoorden met Italië 1946, Marokko en Turkije 1964, migratiestop 1974.",
    ],
)

BUNDELS["modern-imperialisme-en-de-wedloop-om-afrika-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Modern imperialisme en de wedloop om Afrika",
    onder="Waarom Europa na 1870 hele werelddelen bezette, en wat daarvan overblijft.",
    secties=[
        dict(kop="Wat is imperialisme?", blokken=[
            ("p", "<strong>Imperialisme</strong> betekent dat <strong>een staat zijn macht uitbreidt over "
                  "andere gebieden en volken</strong>: militair, politiek en economisch. Nieuw aan het "
                  "<strong>modern imperialisme vanaf ongeveer 1870</strong> is dat <strong>hele gebieden "
                  "bezet en door Europa zelf bestuurd werden</strong>; vroeger ging het vooral om kustposten "
                  "voor de handel. <strong>Rond 1870 hield Europa nog niet het hele binnenland van "
                  "Afrika</strong>."),
            ("p", tabel(["Vorm", "Wat het betekent"], [
                ["Een kolonie", "een gebied dat door een vreemde staat bestuurd wordt"],
                ["Een protectoraat", "een gebied dat zijn eigen vorst houdt onder vreemd toezicht"],
                ["Een invloedssfeer", "een gebied waarin één mogendheid de handel beheerst"],
            ])),
            ("p", "In een protectoraat <strong>bleef het plaatselijke bestuur op papier bestaan</strong>, "
                  "maar de beslissingen vielen elders."),
        ]),
        dict(kop="Oorzaken", blokken=[
            ("p", "<strong>Economisch</strong>: <strong>Europa had grondstoffen nodig voor zijn nieuwe "
                  "nijverheden</strong> (rubber, palmolie, katoen, erts) en <strong>zocht markten om zijn "
                  "fabrieksgoederen te verkopen</strong>, plus plaatsen om kapitaal te beleggen. Dat hangt "
                  "rechtstreeks samen met <strong>de tweede industriële revolutie</strong>."),
            ("p", "<strong>Politiek</strong>: <strong>een grote mogendheid wilde niet achterblijven bij haar "
                  "rivalen</strong>, want kolonies golden als bewijs van macht en prestige. Het "
                  "<strong>nationalisme</strong> voedde dat mee."),
            ("p", "<strong>Ideologisch</strong>: <strong>Europeanen vonden hun eigen beschaving hoger en dus "
                  "voorbeeldig</strong>. Die gedachte heet de <strong>beschavingsmissie</strong>: Europa zou "
                  "de plicht hebben andere volken te beschaven. Dat verhaal diende als rechtvaardiging van "
                  "de overheersing. <strong>Missionarissen verspreidden het geloof en richtten scholen en "
                  "hospitalen op</strong>; zij waren deel van het koloniale gezag en soms de enigen die "
                  "misbruiken aanklaagden."),
            ("p", "<strong>Techniek</strong>: <strong>stoomschepen, geweren en geneesmiddelen maakten het "
                  "binnenland bereikbaar</strong>, met kinine tegen malaria en repeteergeweren. Het "
                  "<strong>Suezkanaal</strong>, geopend in <strong>1869</strong>, <strong>verkortte de zeeweg "
                  "tussen Europa en Azië</strong> en maakte Egypte strategisch."),
        ]),
        dict(kop="De wedloop om Afrika", blokken=[
            ("p", "Op de <strong>Conferentie van Berlijn</strong> van <strong>1884 en 1885</strong>, "
                  "voorgezeten door Bismarck, <strong>maakten de mogendheden afspraken over de verdeling van "
                  "Afrika</strong>. <strong>Er zat geen enkele Afrikaanse vertegenwoordiger aan tafel.</strong> "
                  "De regel: <strong>wie een gebied echt bezet, mag het ook opeisen</strong>, de effectieve "
                  "bezetting. Die regel <strong>versnelde de verdeling</strong>. Het Congobekken werd "
                  "toegewezen aan <strong>koning Leopold II als persoonlijk bezit</strong>."),
            ("p", "In <strong>1914 was bijna het hele werelddeel in Europese handen, op twee staten na</strong>: "
                  "<strong>Ethiopië en Liberia</strong>. In <strong>1896 versloeg een Ethiopisch leger bij "
                  "Adwa een Italiaans invasieleger</strong>, wat in Europa als een schok aankwam. "
                  "<strong>Er was wel verzet</strong>: <strong>gewapende opstanden tegen de koloniale "
                  "legers</strong> en <strong>weigeren te werken of belasting te betalen</strong>. Een beroep "
                  "op een parlement of op de Verenigde Naties was onmogelijk: die laatste bestonden nog niet."),
        ]),
        dict(kop="Gevolgen", blokken=[
            ("p", "<strong>Veel grenzen lopen dwars door gebieden van één volk</strong>, want ze werden met "
                  "een lat op een kaart in Europa getrokken; <strong>na 1960 zijn ze niet opnieuw "
                  "getekend</strong>. De economie van een kolonie was gericht <strong>op de uitvoer van "
                  "enkele grondstoffen naar het moederland</strong>, wat een land kwetsbaar maakt; "
                  "<strong>eigen industrie paste daar niet in</strong>."),
            ("p", "Rond 1900 werden op wereldtentoonstellingen <strong>mensen uit de kolonies aan het publiek "
                  "tentoongesteld</strong>, ook in Tervuren in 1897; een aantal van hen is hier gestorven. "
                  "<strong>Kolonies waren niet altijd een bron van winst</strong> voor de staat: soms kostten "
                  "bestuur en leger meer dan ze opbrachten, en was de winst er voor bedrijven."),
            ("p", "De wedloop zette de mogendheden tegen elkaar op: <strong>Frankrijk en Groot-Brittannië "
                  "stonden in 1898 bij Fashoda tegenover elkaar</strong>, en <strong>Duitsland en Frankrijk "
                  "kwamen over Marokko tweemaal in botsing</strong>. Zo is het imperialisme <strong>een "
                  "oorzaak van de Eerste Wereldoorlog</strong>: <strong>de wedloop om gebied maakte de "
                  "mogendheden rivalen</strong>."),
        ]),
        dict(kop="Oorzaken, techniek en rechtvaardiging", blokken=[
            ("p", "<strong>De oorzaken van het imperialisme</strong> liggen in twee hoeken: "
                  "<strong>economische redenen: grondstoffen, markten en belegging</strong>, en "
                  "<strong>politieke redenen: prestige en strategische steunpunten</strong>. "
                  "<strong>Het modern imperialisme hangt samen met de behoefte aan grondstoffen van de "
                  "tweede industriële revolutie</strong>, en <strong>het nationalisme van de negentiende "
                  "eeuw voedde het ook</strong>: een groot volk hoorde kolonies te hebben. <strong>Het "
                  "imperialisme situeer je in het economische domein, met grondstoffen en markten, en in het "
                  "politieke domein, met macht en bestuur over gebied.</strong>"),
            ("p", "<strong>De rol van de techniek van de tweede industriële revolutie bij de verovering van "
                  "Afrika: stoomschepen, geweren en geneesmiddelen maakten het binnenland "
                  "bereikbaar.</strong> <strong>De betekenis van het Suezkanaal voor het imperialisme: het "
                  "verkortte de zeeweg tussen Europa en Azië aanzienlijk</strong>, en maakte van de route "
                  "naar Indië een belang dat met vloot en steunpunten verdedigd werd."),
            ("p", "De rechtvaardiging heette de <strong>beschavingsmissie</strong> of "
                  "<strong>civilisatiemissie</strong>: <strong>de gedachte dat Europa de plicht had andere "
                  "volken te beschaven</strong>. <strong>Lees je een tekst uit 1890 over de plicht van de "
                  "blanke man om andere volken te leiden, dan lees je dat als een rechtvaardiging van de "
                  "overheersing van die tijd</strong>, niet als een beschrijving van die volken. "
                  "<strong>De rol van de missionarissen in de kolonies: zij verspreidden het geloof en "
                  "richtten scholen en hospitalen op</strong>, en waren daarmee ook een onderdeel van het "
                  "koloniale bestuur."),
        ]),
        dict(kop="De verdeling en haar gevolgen", blokken=[
            ("p", "<strong>In Berlijn legden de mogendheden in 1884 en 1885 de regels voor de verdeling van "
                  "Afrika vast.</strong> <strong>Zie je een kaart van Afrika uit 1914 met rechte grenzen en "
                  "kleurvlakken per mogendheid, dan besluit je: de grenzen zijn in Europa getekend, niet "
                  "door de volken ter plaatse.</strong>"),
            ("p", "Een <strong>kolonie</strong> is <strong>een gebied dat door een vreemde staat bestuurd "
                  "wordt en dat grondstoffen moet leveren</strong>. <strong>Hoe de economie van een kolonie "
                  "meestal ingericht werd: op de uitvoer van enkele grondstoffen naar het "
                  "moederland.</strong> <strong>De koloniale economie liet de kolonies dus niet zelf hun "
                  "industrie uitbouwen</strong>: verwerken gebeurde in Europa, want daar lag de winst."),
            ("p", "<strong>De spanningen tussen de mogendheden die uit de wedloop om Afrika kwamen: "
                  "Frankrijk en Groot-Brittannië stonden in 1898 bij Fashoda tegenover elkaar</strong>, en "
                  "<strong>Duitsland en Frankrijk kwamen over Marokko tweemaal in botsing</strong>. Die "
                  "wrijvingen voedden mee de bondgenootschappen van 1914."),
            ("p", "<strong>De inwoners van de kolonies hebben zich wel tegen het Europese bestuur "
                  "verzet</strong>, met opstanden en met politieke eisen. <strong>Ethiopië slaagde erin een "
                  "Europees invasieleger te verslaan</strong> en bleef zelfstandig."),
            ("p", "<strong>De menselijke tentoonstellingen op de wereldtentoonstellingen rond 1900 waren "
                  "mensen uit de kolonies die aan het publiek tentoongesteld werden.</strong> Ze maakten van "
                  "de koloniale beeldvorming een vertoning voor het grote publiek."),
        ]),
    ],
    onthoud=[
        "Imperialisme: macht over andere gebieden en volken. Modern imperialisme vanaf 1870: hele gebieden bezetten en besturen.",
        "Oorzaken: grondstoffen en markten, prestige, superioriteitsdenken en beschavingsmissie, nieuwe techniek.",
        "Berlijn 1884-1885: verdeling van Afrika, effectieve bezetting, Congo aan Leopold II persoonlijk.",
        "1914: alleen Ethiopië en Liberia onafhankelijk. Gevolgen: willekeurige grenzen en een economie op uitvoer.",
    ],
)

BUNDELS["congo-van-congo-vrijstaat-tot-belgisch-congo-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Congo: van Congo-Vrijstaat tot Belgisch Congo",
    onder="Het imperialisme van dichtbij: rubber, dwangarbeid, overname en modelkolonie.",
    secties=[
        dict(kop="De Congo-Vrijstaat", blokken=[
            ("p", "Na de Conferentie van Berlijn was <strong>koning Leopold II in persoon de eigenaar van de "
                  "Congo-Vrijstaat</strong>; <strong>het was geen kolonie van de Belgische staat</strong> en "
                  "het parlement had er geen zeg in. <strong>Henry Morton Stanley</strong> verkende het gebied "
                  "in zijn opdracht en liet plaatselijke leiders verdragen ondertekenen die zij vaak niet "
                  "konden lezen. <strong>Leopold II heeft Congo nooit zelf bezocht.</strong>"),
            ("p", "Tegenover Europa rechtvaardigde hij zijn onderneming <strong>met de strijd tegen de "
                  "slavenhandel en met de beschaving</strong>. De grootste winsten kwamen van "
                  "<strong>rubber uit de wilde lianen van het regenwoud</strong> en <strong>ivoor uit de jacht "
                  "op olifanten</strong>; de vraag naar rubber kwam van de fietsen en de auto's van de tweede "
                  "industriële revolutie."),
            ("p", "Het rubber werd ingezameld doordat <strong>dorpen onder dwang een vastgelegde hoeveelheid "
                  "moesten leveren</strong>; <strong>van instemming was geen sprake</strong>. De "
                  "<strong>Force Publique</strong>, <strong>het leger en de politie van de Vrijstaat</strong>, "
                  "dwong die quota af. De wandaden: <strong>dwangarbeid met zweepslagen en gijzelingen als "
                  "straf</strong> en <strong>het afhakken van handen van wie het quotum niet haalde</strong>, "
                  "omdat soldaten elke kogel met een hand moesten verantwoorden. De <strong>chicotte</strong> "
                  "was <strong>een zweep van gedroogde huid, gebruikt om te straffen</strong>, en kon dodelijk "
                  "zijn."),
            ("p", "<strong>De bevolking werd zwaar getroffen door geweld, honger en ziekte</strong>; "
                  "schattingen van het dodental lopen uiteen en gaan tot in de miljoenen. "
                  "<strong>De kritiek kwam vooral uit het buitenland</strong>: de Britse journalist "
                  "<strong>Edmund Dene Morel</strong> en de Britse consul <strong>Roger Casement met zijn "
                  "verslag</strong> brachten de feiten naar buiten, samen met missionarissen die foto's "
                  "maakten. Onder die druk <strong>nam de Belgische staat de kolonie in 1908 van de koning "
                  "over</strong>."),
        ]),
        dict(kop="Belgisch Congo", blokken=[
            ("p", "Belgisch Congo werd bestuurd door drie machten samen, het koloniale drieluik: <strong>de "
                  "koloniale staat met haar ambtenaren</strong>, <strong>de kerk met haar missies en haar "
                  "scholen</strong>, en de grote vennootschappen. Een <strong>gouverneur-generaal</strong> "
                  "werd <strong>door Brussel aangesteld</strong> en voerde uit wat de minister van Koloniën "
                  "besliste."),
            ("p", "<strong>Koper</strong> maakte <strong>Katanga</strong> zo waardevol; de Union Minière du "
                  "Haut-Katanga werd een van de grootste mijnbedrijven ter wereld. In de Tweede Wereldoorlog "
                  "speelde <strong>uranium uit de mijn van Shinkolobwe</strong> een bijzondere rol: het werd "
                  "gebruikt voor de eerste atoombommen."),
            ("p", "De <strong>missies verzorgden het grootste deel van het onderwijs</strong>, dus het lager "
                  "onderwijs bereikte veel kinderen; <strong>de eerste universiteiten kwamen er pas in de "
                  "jaren vijftig</strong>, kort voor de onafhankelijkheid. Daardoor had Congo in "
                  "<strong>1960 amper eigen artsen, ingenieurs en hoge ambtenaren</strong>."),
            ("p", "<strong>De Congolezen hadden geen stemrecht en geen eigen volksvertegenwoordiging</strong>, "
                  "niet in Congo en niet in België. In de steden leefden Belgen en Congolezen "
                  "<strong>gescheiden, in eigen wijken met eigen voorzieningen</strong>, met een avondklok "
                  "voor Congolezen in de Europese stad. De <strong>évolués</strong> waren "
                  "<strong>Congolezen met een opleiding en een baan in het bestuur</strong> of de handel: een "
                  "kleine middengroep, en juist uit hun rangen kwam de eis voor onafhankelijkheid."),
            ("p", "Het bestuur was <strong>paternalistisch</strong>: <strong>men behandelde de bevolking als "
                  "kinderen die geleid moeten worden</strong>. Zorg voor scholen en hospitalen hoorde erbij, "
                  "zeggenschap niet. In Europa heette Congo een <strong>modelkolonie</strong>, <strong>omdat "
                  "er scholen en hospitalen waren en de mijnen winst maakten</strong>; dat beeld hield geen "
                  "rekening met het ontbreken van rechten. <strong>De overname van 1908 maakte geen einde aan "
                  "alle dwangarbeid</strong>: verplichte arbeid en verplichte teelten bleven bestaan."),
            ("p", "Belgisch Congo is <strong>een voorbeeld van het modern imperialisme</strong>: gebied, "
                  "grondstoffen en een bestuur van buiten, met een economie die <strong>op uitvoer gericht "
                  "bleef in plaats van op eigen industrie</strong>."),
        ]),
        dict(kop="De Vrijstaat: rubber, ivoor en geweld", blokken=[
            ("p", "<strong>De ontdekkingsreiziger die Congo in opdracht van Leopold II verkende, is Henry "
                  "Morton Stanley.</strong> <strong>De producten die de Vrijstaat zijn grootste winsten "
                  "brachten: rubber uit de wilde lianen van het regenwoud</strong> en <strong>ivoor uit de "
                  "jacht op olifanten in het binnenland</strong>. <strong>Rubber</strong>, ook "
                  "<strong>caoutchouc</strong> genoemd, is het <strong>product uit het regenwoud dat het "
                  "meeste geld opbracht</strong>: de niewe fietsen en auto's in Europa vroegen rubber."),
            ("p", "<strong>De wandaden die onder het bestuur van de Vrijstaat vastgesteld werden: "
                  "dwangarbeid met zweepslagen en gijzelingen als straf</strong>, en <strong>het afhakken "
                  "van handen van wie het quotum niet haalde</strong>. <strong>De Vrijstaat van Leopold II "
                  "situeer je in het economische domein, met rubber en ivoor als winst, en in het politieke "
                  "domein, met de macht over een gebied.</strong>"),
            ("p", "Twee bronnen om te beoordelen. <strong>Lees je een verslag van een Britse consul uit 1904 "
                  "over verminkingen in Congo, dan toets je het aan andere bronnen, zoals missieverslagen en "
                  "foto's</strong>: de consul had ook een belang, want Groot-Brittannië had zelf kolonies en "
                  "concurrenten. <strong>Zie je een foto uit 1904 van een Congolese man met een verminkte "
                  "hand, dan zegt die bron dat verminking als straf of als bewijsstuk werd gebruikt</strong>: "
                  "de hand moest bewijzen dat een kogel niet verspild was."),
        ]),
        dict(kop="Belgisch Congo: besturen en beeldvorming", blokken=[
            ("p", "<strong>De drie machten die Belgisch Congo in de praktijk bestuurden: de koloniale staat "
                  "met haar ambtenaren</strong>, <strong>de kerk met haar missies en haar scholen</strong>, "
                  "en de grote bedrijven met hun concessies. Samen heet dat de koloniale drie-eenheid."),
            ("p", "<strong>Paternalisme</strong> is <strong>de houding waarbij een bestuur de bevolking als "
                  "onmondige kinderen behandelt</strong>: goed voor hen zorgen, maar hen nooit laten "
                  "meebeslissen. <strong>Het lager onderwijs in Belgisch Congo was grotendeels in handen van "
                  "de missies</strong>, en <strong>in 1960 had Congo géén ruime groep van eigen artsen, "
                  "ingenieurs en hoge ambtenaren</strong>. <strong>De grondstof uit Katanga die voor de "
                  "Belgische mijnbedrijven het belangrijkst was, is koper</strong>; later kwam daar uranium "
                  "bij."),
            ("p", "<strong>Zie je een schoolboek uit 1950 waarin Congo als een geschenk van België wordt "
                  "beschreven, dan lees je dat als beeldvorming van de kolonisator over zichzelf.</strong> "
                  "Het boek is een goede bron over België in 1950, en een slechte over Congo."),
        ]),
    ],
    onthoud=[
        "1885-1908 Congo-Vrijstaat: persoonlijk bezit van Leopold II, rubber en ivoor, dwangarbeid, chicotte, afgehakte handen.",
        "Morel en Casement klaagden het aan; in 1908 nam de Belgische staat de kolonie over.",
        "Belgisch Congo: staat, kerk en bedrijven samen; koper in Katanga, uranium uit Shinkolobwe.",
        "Geen politieke rechten, gescheiden wijken, paternalisme, hoger onderwijs pas in de jaren vijftig.",
    ],
)

BUNDELS["de-eerste-wereldoorlog-en-de-vrede-van-versailles-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De Eerste Wereldoorlog en de Vrede van Versailles",
    onder="Van Sarajevo tot de loopgraven aan de IJzer, en van de wapenstilstand tot het dictaat.",
    secties=[
        dict(kop="Oorzaken en aanleiding", blokken=[
            ("p", "Als oorzaken worden aangewezen: <strong>de bondgenootschappen tussen de mogendheden</strong>, "
                  "die Europa in twee kampen verdeelden, <strong>de wapenwedloop tussen de grote "
                  "legers</strong>, het <strong>nationalisme</strong> en de <strong>wedloop om "
                  "kolonies</strong>. <strong>Eén oorzaak alleen verklaart niets.</strong>"),
            ("p", "De <strong>Balkan</strong> heet het kruitvat van Europa omdat <strong>staten en "
                  "mogendheden er over hetzelfde gebied botsten</strong>: het Ottomaanse rijk viel er terug, "
                  "en Rusland en Oostenrijk-Hongarije wilden er beide invloed. De aanleiding was <strong>de "
                  "moord op de Oostenrijkse troonopvolger in Sarajevo</strong>, in juni 1914. Binnen vijf "
                  "weken stond half Europa in oorlog."),
        ]),
        dict(kop="België in de oorlog", blokken=[
            ("p", "Het Duitse leger viel België binnen op <strong>4 augustus 1914</strong>, "
                  "<strong>om Frankrijk langs het noorden snel te kunnen verslaan</strong>. De Belgische regering <strong>wees het ultimatum af en liet het leger "
                  "zich verzetten</strong>; die weigering bracht Groot-Brittannië in de oorlog, dat "
                  "<strong>de Belgische neutraliteit gewaarborgd</strong> had. <strong>België werd dus "
                  "binnengevallen hoewel zijn neutraliteit door verdragen gewaarborgd was.</strong>"),
            ("p", "In het najaar van 1914 kwam het front tot stilstand <strong>achter de IJzer, in de "
                  "Westhoek</strong>: de Belgen <strong>zetten de vlakte achter de rivier onder water</strong>, "
                  "met de sluizen bij Nieuwpoort en het getij. Zo <strong>bleef een klein deel van België "
                  "onbezet</strong>, met de koning en het leger; de regering week uit naar Frankrijk."),
            ("p", "Daarna volgde een <strong>loopgravenoorlog</strong>: <strong>de legers lagen maanden in "
                  "stellingen zonder veel te vorderen</strong>, want <strong>de verdediging was sterker dan "
                  "de aanval</strong>. <strong>De oorlog was dus niet na enkele maanden beslist</strong>, maar "
                  "duurde vier jaar. De soldaten leefden <strong>maanden in loopgraven met modder en "
                  "ratten</strong>, en <strong>Ieper werd bijna volledig verwoest</strong>."),
            ("p", "Nieuwe wapens: <strong>gifgas en de mitrailleur</strong>, <strong>de tank en het "
                  "vliegtuig</strong>; de atoombom en de raket horen bij de volgende oorlog. "
                  "<strong>Bij Ieper werd in april 1915 voor het eerst op grote schaal gifgas gebruikt</strong>; "
                  "mosterdgas heet daarom ook yperiet."),
            ("p", "Het heet een <strong>wereldoorlog</strong> omdat <strong>er ook buiten Europa gevochten "
                  "werd en kolonies ingezet werden</strong>, niet omdat alle landen meededen."),
        ]),
        dict(kop="Totale oorlog en bezet land", blokken=[
            ("p", "Een <strong>totale oorlog</strong> betekent dat <strong>de hele samenleving en economie "
                  "op de oorlog gericht werden</strong>: fabrieken maakten wapens, de staat regelde het "
                  "voedsel, de pers werd gecensureerd. <strong>Vrouwen namen in de fabrieken het werk van de "
                  "soldaten over</strong> en <strong>werkten in de hospitalen en de hulpdiensten achter het "
                  "front</strong>; <strong>stemrecht kregen zij tijdens de oorlog niet</strong>, maar hun werk "
                  "versterkte het pleidooi erna. De <strong>burgerbevolking was een doelwit</strong> van de "
                  "oorlogsvoering."),
            ("p", "<strong>Propaganda</strong> zijn <strong>berichten die de eigen zaak mooi voorstellen</strong> "
                  "en de vijand lelijk. In bezet België leefde de bevolking <strong>met voedselschaarste, "
                  "opeisingen en gedwongen arbeid</strong>: duizenden werklozen werden naar Duitsland "
                  "gedeporteerd. <strong>Er waren geen vrije verkiezingen en geen vrije pers</strong>; daarom "
                  "ontstond de sluikpers."),
            ("p", "De <strong>Flamenpolitik</strong> van de bezetter betekende <strong>de Vlaamse eisen "
                  "steunen om België te verdelen</strong>; wie meewerkte, heette <strong>activist</strong>. "
                  "Aan het front eisten <strong>Vlaamse soldaten met taaleisen in het leger</strong> "
                  "gelijkheid: de <strong>Frontbeweging</strong>."),
        ]),
        dict(kop="Het einde en de vrede", blokken=[
            ("p", "In <strong>1917</strong> veranderde de loop van de oorlog: <strong>de Verenigde Staten "
                  "kwamen in de oorlog</strong> aan de kant van de Entente, en <strong>in Rusland brak een "
                  "revolutie uit</strong> die het land uit de oorlog haalde. De wapenstilstand volgde op "
                  "<strong>11 november 1918</strong>."),
            ("p", "Het vredesverdrag met Duitsland werd in <strong>1919 in Versailles, bij Parijs</strong> "
                  "gesloten. <strong>Duitsland mocht niet onderhandelen, enkel ondertekenen</strong>; daarom "
                  "sprak men daar van een <strong>dictaat</strong>. Voorwaarden: <strong>het moest "
                  "herstelbetalingen doen voor de aangerichte schade</strong>, <strong>het mocht enkel nog een "
                  "klein leger op de been houden</strong>, en <strong>zijn kolonies werden als mandaatgebied "
                  "onder de overwinnaars verdeeld</strong>. Het zwaarst woog <strong>het artikel dat Duitsland "
                  "de schuld van de oorlog gaf</strong>; daarop steunden de herstelbetalingen. "
                  "<strong>Het verdrag heeft in Duitsland wrok nagelaten die later politiek gebruikt "
                  "werd.</strong>"),
            ("p", "<strong>België kreeg Eupen en Malmedy, en het mandaat over Ruanda-Urundi</strong>; de "
                  "<strong>Elzas en Lotharingen</strong> gingen naar Frankrijk en het Rijnland bleef Duits, "
                  "maar zonder leger. De <strong>Volkenbond</strong> werd opgericht om oorlog te voorkomen, "
                  "met zetel in Genève; <strong>de Verenigde Staten waren er geen lid van</strong>, want hun "
                  "senaat weigerde het verdrag."),
            ("p", "Door de oorlog verdwenen <strong>het Oostenrijks-Hongaarse en het Ottomaanse rijk</strong> "
                  "en <strong>het Russische en het Duitse keizerrijk</strong>. <strong>De grenzen in "
                  "Midden-Europa bleven dus niet dezelfde</strong>: er kwamen nieuwe staten als Polen, "
                  "Tsjechoslowakije en Joegoslavië bij, vaak met minderheden binnen hun grenzen."),
        ]),
        dict(kop="Van Sarajevo tot de IJzer", blokken=[
            ("p", "<strong>De oorzaken van de Eerste Wereldoorlog die doorgaans aangewezen worden: de "
                  "bondgenootschappen tussen de mogendheden</strong> en <strong>de wapenwedloop tussen de "
                  "grote legers</strong>, naast het nationalisme en de spanningen op de Balkan. De "
                  "aanleiding was de moord <strong>in Sarajevo</strong>, waar <strong>in juni 1914 de "
                  "Oostenrijkse troonopvolger doodgeschoten werd</strong>."),
            ("p", "<strong>Het Belgische leger vocht in de Eerste Wereldoorlog niet aan de zijde van "
                  "Duitsland</strong>, maar tegen de inval. <strong>De IJzer werd de frontlijn in het "
                  "onbezette stukje België</strong>: <strong>de Belgen hielden het Duitse leger aan de IJzer "
                  "tegen door de vlakte achter de rivier onder water te zetten.</strong>"),
            ("p", "<strong>Wat een loopgravenoorlog kenmerkt: de legers liggen maanden in stellingen zonder "
                  "veel te vorderen.</strong> <strong>De nieuwe wapens maakten de aanval niet gemakkelijker "
                  "dan de verdediging</strong>, juist omgekeerd: machinegeweer, prikkeldraad en zwaar "
                  "geschut maakten een aanval over open terrein bijna onmogelijk. <strong>Zie je een foto "
                  "van soldaten in een loopgraaf met gasmaskers op, dan komt die uit de Eerste "
                  "Wereldoorlog.</strong>"),
        ]),
        dict(kop="Het einde en de vrede", blokken=[
            ("p", "<strong>Propaganda in oorlogstijd</strong> zijn <strong>berichten die de eigen zaak mooi "
                  "voorstellen</strong>, en de vijand lelijk. <strong>De gebeurtenissen van 1917 die de loop "
                  "van de oorlog veranderden: de Verenigde Staten kwamen in de oorlog</strong>, en "
                  "<strong>in Rusland brak een revolutie uit</strong>. <strong>Op 11 november 1918 werd de "
                  "wapenstilstand gesloten</strong>, een datum die in België nog elk jaar herdacht wordt "
                  "als 11/11."),
            ("p", "<strong>De voorwaarden die het Verdrag van Versailles aan Duitsland oplegde: het moest "
                  "herstelbetalingen doen voor de aangerichte schade</strong>, en <strong>het mocht enkel "
                  "nog een klein leger op de been houden</strong>. <strong>Het Verdrag van Versailles legde "
                  "Duitsland dus herstelbetalingen op.</strong> <strong>Het artikel dat in Duitsland het "
                  "zwaarst ervaren werd, is het artikel dat Duitsland de schuld van de oorlog gaf.</strong> "
                  "<strong>Duitsland mocht in Versailles niet over de vredesvoorwaarden onderhandelen</strong>: "
                  "het mocht enkel ondertekenen."),
            ("p", "<strong>De internationale organisatie die na de Eerste Wereldoorlog werd opgericht om "
                  "oorlog te voorkomen, is de Volkenbond.</strong> Ze had geen eigen leger, en de Verenigde "
                  "Staten werden nooit lid."),
            ("p", "<strong>Lees je een Duitse krant uit 1920 die over het dictaat van Versailles spreekt, "
                  "dan leer je daaruit hoe het verdrag in Duitsland werd ervaren en gebruikt.</strong> Dat "
                  "woord zelf is al politiek: het zegt dat het verdrag opgelegd werd en dus niet "
                  "rechtsgeldig zou zijn."),
        ]),
    ],
    onthoud=[
        "Oorzaken: bondgenootschappen, wapenwedloop, nationalisme, imperialisme. Aanleiding: Sarajevo, juni 1914.",
        "België 1914: inval ondanks de neutraliteit, front aan de IJzer door de vlakte onder water te zetten.",
        "Totale oorlog: oorlogseconomie, vrouwen in de fabriek, propaganda, censuur, deportaties, Flamenpolitik.",
        "Wapenstilstand 11 november 1918; Versailles 1919: schuldartikel, herstelbetalingen, klein leger, Volkenbond zonder de VS.",
    ],
)

BUNDELS["het-interbellum-de-opkomst-van-het-totalitarisme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het interbellum: de opkomst van het totalitarisme",
    onder="Revolutie in Rusland, fascisme in Italië, crisis in de wereld en een dictatuur in Duitsland.",
    secties=[
        dict(kop="De Sovjet-Unie", blokken=[
            ("p", "Het <strong>interbellum</strong> is de periode <strong>tussen de twee "
                  "wereldoorlogen</strong>, van 1918 tot 1939. In <strong>1917</strong> gebeurde in Rusland "
                  "dit: <strong>de tsaar verdween en de bolsjewieken namen de macht</strong>, onder leiding "
                  "van <strong>Lenin</strong>."),
            ("p", "<strong>Stalin liet de economie door de staat plannen in vijfjarenplannen</strong>: de "
                  "<strong>economie was dus door de staat gepland</strong>, met zware industrie eerst. De "
                  "<strong>collectivisering van de landbouw</strong> betekende dat <strong>de boeren hun grond "
                  "en vee moesten inbrengen</strong> in grote staatsbedrijven; wie zich verzette werd verbannen "
                  "of gedood, en in Oekraïne volgde een hongersnood met miljoenen doden."),
            ("p", "Om zijn macht te verzekeren gebruikte Stalin <strong>een geheime politie die tegenstanders "
                  "oppakte</strong> en <strong>werkkampen waar gevangenen dwangarbeid deden</strong>. "
                  "<strong>Vrije verkiezingen met verschillende partijen waren er niet</strong>, en van een "
                  "vrije pers evenmin: er was één partij. Tijdens de <strong>Grote Terreur</strong> werden "
                  "ook partijleiders en officieren zelf opgepakt. <strong>Groei en terreur liepen daar samen "
                  "op.</strong>"),
        ]),
        dict(kop="Het fascisme in Italië", blokken=[
            ("p", "In <strong>1922</strong> kwam <strong>Benito Mussolini</strong> in Italië aan de macht: "
                  "na een mars van zijn aanhangers naar Rome werd hij <strong>door de koning als "
                  "regeringsleider benoemd</strong>. Het <strong>fascisme</strong> kenmerkt zich door "
                  "<strong>één partij, één leider en geen enkele oppositie</strong>; de staat kwam boven het "
                  "individu, en zijn titel was <strong>Il Duce</strong>, de leider."),
        ]),
        dict(kop="De wereldcrisis", blokken=[
            ("p", "In <strong>oktober 1929</strong> gebeurde op de beurs van New York dit: <strong>de koersen "
                  "stortten in en een wereldcrisis volgde</strong>. Banken vielen om, bedrijven sloten en de "
                  "werkloosheid schoot omhoog. <strong>De crisis bleef niet beperkt tot de Verenigde "
                  "Staten</strong>: door de internationale handel en de leningen sloeg ze meteen over naar "
                  "Europa."),
            ("p", "De gevolgen in Europa: <strong>massale werkloosheid en armoede in de industriesteden</strong> "
                  "en <strong>groei van partijen die de democratie afwezen</strong>. <strong>De crisis maakte "
                  "de democratie dus niet sterker</strong>, integendeel. De <strong>Weimarrepubliek</strong> "
                  "in Duitsland kwam in de problemen door <strong>herstelbetalingen, inflatie en crisis</strong>, "
                  "en werd van het begin af aan belast met <strong>de wrok om het verdrag van Versailles</strong>, "
                  "wat <strong>de nazipartij hielp groeien</strong>."),
        ]),
        dict(kop="Nazi-Duitsland en het totalitarisme", blokken=[
            ("p", "<strong>Hitler werd in januari 1933 rijkskanselier</strong>, langs <strong>een benoeming, "
                  "niet langs een staatsgreep</strong>. Daarna bouwde hij zijn alleenheerschappij uit: "
                  "<strong>hij liet zich volmachten geven om zonder parlement te regeren</strong> en "
                  "<strong>verbood de andere partijen en de vrije vakbonden</strong>. <strong>Die bleven dus "
                  "niet bestaan.</strong>"),
            ("p", "Een <strong>totalitaire staat</strong> is <strong>een staat die greep wil hebben op het "
                  "hele leven van zijn burgers</strong>. Kenmerken: <strong>één partij en één leider met alle "
                  "macht</strong>, en <strong>een geheime politie, terreur en censuur</strong>. Het "
                  "<strong>verschil met een autoritaire staat</strong> is dat <strong>een totalitaire staat "
                  "ook het denken van zijn burgers wil beheersen</strong>: de ene eist gehoorzaamheid, de "
                  "andere ook overtuiging. <strong>Jeugdbewegingen moeten de kinderen vroeg aan de leider "
                  "binden</strong>, en <strong>propaganda moest het volk achter de leider krijgen</strong>, "
                  "met een eigen ministerie, radio, film en massabijeenkomsten."),
            ("p", "De <strong>Neurenberger wetten van 1935 ontnamen de Joden hun rechten als burger</strong>: "
                  "<strong>zo werd de uitsluiting wet</strong>. Tijdens de <strong>Kristalnacht</strong> van "
                  "november 1938 werden <strong>synagogen en Joodse winkels in brand gestoken en "
                  "geplunderd</strong>, aangemoedigd door de staat."),
            ("p", "<strong>Ook in België kwamen er in de jaren dertig partijen op die de democratie "
                  "afwezen</strong>: Rex en het Vlaams Nationaal Verbond haalden zetels."),
        ]),
        dict(kop="De weg naar 1939", blokken=[
            ("p", "Frankrijk en Groot-Brittannië <strong>gaven toe in de hoop zo een oorlog te vermijden</strong>. "
                  "Die politiek heet <strong>appeasement</strong>, de verzoeningspolitiek; het hoogtepunt was "
                  "<strong>de conferentie van München in 1938</strong>, waar Tsjechoslowakije gebied moest "
                  "afstaan. <strong>Die conferentie heeft de oorlog niet afgewend</strong>: enkele maanden "
                  "later nam Duitsland de rest van Tsjechoslowakije."),
            ("p", "Hitler <strong>liet zijn leger het Rijnland opnieuw bezetten</strong> en <strong>lijfde "
                  "Oostenrijk bij Duitsland in</strong>; elke stap bleef zonder gevolg. In augustus 1939 "
                  "spraken Duitsland en de Sovjet-Unie af dat <strong>zij elkaar niet zouden aanvallen</strong>, "
                  "en in een geheim deel verdeelden zij Polen. Een week later viel Duitsland Polen binnen."),
        ]),
        dict(kop="Drie regimes, drie machtsovernames", blokken=[
            ("p", "<strong>Vladimir Lenin leidde in 1917 de bolsjewieken bij de machtsovername in "
                  "Rusland.</strong> In Italië ging het anders: <strong>Mussolini werd door de Italiaanse "
                  "koning als regeringsleider benoemd</strong>, na de mars op Rome. En Hitler werd in 1933 "
                  "kanselier, langs de grondwet om, waarna hij de democratie van binnenuit afbrak."),
            ("p", "<strong>Over de Sovjet-Unie onder Stalin: de zware industrie groeide snel onder de "
                  "vijfjarenplannen</strong>, en <strong>de collectivisering kostte miljoenen mensen het "
                  "leven</strong>, vooral door de hongersnood op het platteland. <strong>Zie je een affiche "
                  "uit de Sovjet-Unie van 1931 met gespierde arbeiders bij een hoogoven, dan lees je die als "
                  "propaganda voor de vijfjarenplannen van de staat</strong>, niet als een beeld van het "
                  "werkelijke leven in de fabriek."),
            ("p", "<strong>Wat de Neurenberger wetten van 1935 regelden: zij ontnamen de Joden hun rechten "
                  "als burger.</strong> <strong>De rol van jeugdbewegingen in een totalitaire staat: zij "
                  "moeten de kinderen vroeg aan de leider binden.</strong> <strong>Zie je een foto van een "
                  "massabijeenkomst met vlaggen, rijen en één spreker op een podium, dan herken je de "
                  "propaganda van een totalitair regime.</strong>"),
        ]),
        dict(kop="Naar een nieuwe oorlog", blokken=[
            ("p", "<strong>Het verband tussen de Vrede van Versailles en het interbellum: de wrok om het "
                  "verdrag hielp de nazipartij groeien.</strong> En <strong>het verband tussen de "
                  "wereldcrisis en de opkomst van het nazisme: de werkloosheid maakte de partij voor veel "
                  "kiezers aantrekkelijk.</strong> Samen leverden ze het verhaal en de nood."),
            ("p", "<strong>De politiek die Frankrijk en Groot-Brittannië tegenover Hitler volgden voor 1939: "
                  "zij gaven toe in de hoop zo een oorlog te vermijden.</strong> Die politiek van "
                  "<strong>toegeven aan Hitler om een oorlog te vermijden</strong> heet "
                  "<strong>appeasement</strong> of de <strong>appeasementpolitiek</strong>. <strong>De "
                  "conferentie van München in 1938 heeft de oorlog niet voorgoed afgewend</strong>: een jaar "
                  "later viel Duitsland Polen binnen."),
            ("p", "<strong>De stappen die Hitler voor september 1939 zette: hij liet zijn leger het Rijnland "
                  "opnieuw bezetten</strong>, en <strong>hij lijfde Oostenrijk bij Duitsland in</strong>, "
                  "daarna Tsjechoslowakije. <strong>Wat Duitsland en de Sovjet-Unie in augustus 1939 "
                  "afspraken: zij beloofden elkaar niet aan te vallen</strong>, en in een geheim deel van "
                  "dat pact verdeelden ze Polen."),
        ]),
    ],
    onthoud=[
        "1917 revolutie in Rusland; Stalin: vijfjarenplannen, collectivisering, geheime politie, werkkampen, Grote Terreur.",
        "Mussolini 1922: één partij, één leider, geen oppositie.",
        "Beurskrach oktober 1929 → werkloosheid en groei van antidemocratische partijen.",
        "Hitler januari 1933 benoemd; volmachten, partijverbod, propaganda, Neurenberger wetten 1935, Kristalnacht 1938.",
        "Appeasement en München 1938 hielden de oorlog niet tegen; pact met de Sovjet-Unie in augustus 1939.",
    ],
)

BUNDELS["de-tweede-wereldoorlog-en-de-holocaust-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De Tweede Wereldoorlog en de Holocaust",
    onder="Blitzkrieg en bezetting, vernietiging en vervolging, en wat erna in het recht veranderde.",
    secties=[
        dict(kop="Het verloop van de oorlog", blokken=[
            ("p", "De oorlog begon in Europa met <strong>de Duitse inval in Polen in september 1939</strong>; "
                  "twee dagen later verklaarden Frankrijk en Groot-Brittannië Duitsland de oorlog. Een "
                  "<strong>blitzkrieg</strong> is <strong>een snelle aanval met tanks, vliegtuigen en "
                  "motorvoertuigen</strong>: <strong>deze oorlog was er een van beweging, geen "
                  "loopgravenoorlog zoals de eerste</strong>."),
            ("p", "Op <strong>10 mei 1940</strong> viel het Duitse leger België binnen, samen met Nederland "
                  "en Luxemburg. <strong>Ook nu was België neutraal verklaard</strong>, en ook nu hielp dat "
                  "niet. De Belgische veldtocht duurde <strong>achttien dagen</strong>. Daarna botsten koning "
                  "en regering: <strong>de koning bleef in het bezette land, de regering week uit naar "
                  "Londen</strong>. Die breuk werd na de oorlog de <strong>koningskwestie</strong>."),
            ("p", "In <strong>juni 1941 viel Duitsland de Sovjet-Unie binnen</strong> en verbrak zo zijn "
                  "eigen pact. In <strong>december 1941</strong> traden de Verenigde Staten in de oorlog, "
                  "want <strong>Japan had hun vloot in Pearl Harbor aangevallen</strong>. De <strong>slag om "
                  "Stalingrad</strong> geldt als keerpunt aan het oostfront."),
            ("p", "Op <strong>6 juni 1944</strong>, D-day, landden de Geallieerden in Normandië; "
                  "<strong>het grootste deel van België werd in september 1944 bevrijd</strong>, en in "
                  "december volgde nog het Ardennenoffensief. De oorlog tegen Japan eindigde in augustus 1945 "
                  "<strong>met twee atoombommen op Japanse steden</strong>, Hiroshima en Nagasaki. "
                  "<strong>De burgerbevolking was een doelwit</strong>: steden werden gebombardeerd en "
                  "Antwerpen kreeg honderden V-bommen te verwerken."),
        ]),
        dict(kop="Bezet België", blokken=[
            ("p", "<strong>Collaboratie</strong> is <strong>samenwerken met de bezetter van je land</strong>; "
                  "na de oorlog volgde de repressie. Het <strong>verzet</strong> nam de vorm aan van "
                  "<strong>gewapende acties tegen spoorwegen en bezettingstroepen</strong> en van "
                  "<strong>sluikpers die nieuws verspreidde buiten de censuur om</strong>. <strong>Verkiezingen "
                  "en rechtsmiddelen bestonden niet</strong>, dus alles gebeurde in het geheim. "
                  "<strong>Zowel collaboratie als verzet kwamen voor</strong>, en de meeste mensen deden geen "
                  "van beide."),
            ("p", "De <strong>verplichte tewerkstelling</strong> betekende dat <strong>Belgen gedwongen "
                  "werden in Duitsland te gaan werken</strong>; wie zich onttrok, moest onderduiken en kwam "
                  "vaak bij het verzet terecht."),
        ]),
        dict(kop="De Holocaust", blokken=[
            ("p", "De <strong>Holocaust</strong> of <strong>Shoah</strong> is <strong>de systematische "
                  "vernietiging van de Joden van Europa</strong>, gepland door een staat. Eraan vooraf gingen "
                  "<strong>uitsluiting bij wet van beroepen, scholen en openbaar leven</strong> en "
                  "<strong>verplichte kentekens en registratie van wie Joods was</strong>. "
                  "<strong>De vervolging begon dus met uitsluiting bij wet, nog voor de oorlog</strong>, met "
                  "de Neurenberger wetten van 1935."),
            ("p", "Een <strong>getto</strong> was <strong>een afgesloten wijk waar Joden gedwongen moesten "
                  "wonen</strong>; honger en ziekte kostten er al duizenden het leven. Op de conferentie in "
                  "<strong>Wannsee</strong> in januari 1942 werd <strong>de organisatie van de vernietiging "
                  "van de Joden van Europa</strong> besproken. Het verschil tussen een "
                  "<strong>concentratiekamp</strong> en een <strong>vernietigingskamp</strong>: <strong>een "
                  "vernietigingskamp was voor het doden ingericht</strong>, en die lagen in bezet Polen. Het "
                  "bekendste is <strong>Auschwitz</strong>, nu een gedenkplaats."),
            ("p", "Uit België werden de Joden gedeporteerd <strong>uit de Dossinkazerne in Mechelen</strong>, "
                  "het verzamelkamp waar nu Kazerne Dossin staat: <strong>meer dan vijfentwintigduizend "
                  "mensen</strong>, waarvan slechts een kleine minderheid de oorlog overleefde. Joodse "
                  "kinderen werden gered doordat zij <strong>ondergebracht werden bij gezinnen, kloosters en "
                  "instellingen</strong>, met vervalste papieren: <strong>er is dus wel geprobeerd Joden te "
                  "helpen</strong>, en Israël eert die mensen als rechtvaardigen onder de volkeren."),
            ("p", "Ook <strong>Roma en Sinti</strong> en <strong>mensen met een handicap</strong> werden "
                  "vervolgd, naast homoseksuelen, politieke tegenstanders en Jehova's getuigen. In de "
                  "Holocaust kwamen <strong>ongeveer zes miljoen</strong> Joden om het leven. <strong>Het was "
                  "niet het werk van enkele individuen</strong>: er waren registers, treinen, verordeningen en "
                  "ambtenaren voor nodig."),
        ]),
        dict(kop="Na de oorlog", blokken=[
            ("p", "In <strong>Neurenberg</strong> in 1945 en 1946 <strong>stonden leiders van het naziregime "
                  "terecht</strong>, voor het eerst voor <strong>misdaden tegen de menselijkheid</strong>: "
                  "<strong>dat begrip werd pas na de Tweede Wereldoorlog in het recht opgenomen</strong>. Het "
                  "woord <strong>genocide</strong>, het <strong>opzettelijk uitroeien van een volk of een "
                  "groep</strong>, werd kort daarna in het internationaal recht vastgelegd."),
            ("p", "Uit de oorlog kwamen <strong>de Verenigde Naties in 1945</strong> en <strong>de Universele "
                  "Verklaring van de Rechten van de Mens in 1948</strong>. De Volkenbond en Versailles horen "
                  "bij de vorige oorlog."),
            ("p", "Een <strong>getuigenis van een overlevende</strong>, zestig jaar na de feiten, is "
                  "<strong>een waardevolle bron die je naast documenten en cijfers legt</strong>: zij zegt hoe "
                  "iemand het beleefde, en voor de omvang en de organisatie heb je documenten nodig."),
        ]),
        dict(kop="Het verloop van de oorlog", blokken=[
            ("p", "<strong>De gebeurtenis waarmee de Tweede Wereldoorlog in Europa begon: de Duitse inval in "
                  "Polen in september 1939.</strong> <strong>België werd in mei 1940 binnengevallen hoewel "
                  "het zich neutraal had verklaard.</strong> <strong>Waarover koning Leopold III en zijn "
                  "regering in 1940 in botsing kwamen: de koning bleef in het bezette land, de regering week "
                  "uit naar Londen.</strong> Die breuk werd na de oorlog de Koningskwestie."),
            ("p", "<strong>De veldslag die als keerpunt aan het oostfront beschouwd wordt, is de slag om "
                  "Stalingrad.</strong> <strong>De Tweede Wereldoorlog werd niet vooral in loopgraven "
                  "uitgevochten, zoals de Eerste</strong>: tanks, vliegtuigen en snelle doorbraken bepaalden "
                  "het beeld. <strong>De burgerbevolking was in de Tweede Wereldoorlog een doelwit van de "
                  "oorlogsvoering</strong>, door bombardementen op steden, door honger en door vervolging."),
            ("p", "<strong>Zie je een foto uit 1944 van juichende mensen rond een tank in een Belgische "
                  "straat, dan herken je de bevrijding in september 1944.</strong>"),
        ]),
        dict(kop="De Holocaust en wat erna kwam", blokken=[
            ("p", "<strong>Een getto in de bezette gebieden in Oost-Europa was een afgesloten wijk waar "
                  "Joden gedwongen moesten wonen.</strong> <strong>Het bekendste vernietigingskamp in bezet "
                  "Polen is Auschwitz</strong>, ook Auschwitz-Birkenau genoemd. <strong>Genocide</strong> of "
                  "<strong>volkerenmoord</strong> is <strong>het opzettelijk uitroeien van een volk of een "
                  "groep</strong>."),
            ("p", "<strong>Niemand in bezet Europa die probeerde Joden te helpen? Dat is onwaar</strong>: er "
                  "waren mensen die onderdoken kinderen opnamen, valse papieren maakten of lijsten "
                  "doorspeelden, met gevaar voor hun eigen leven."),
            ("p", "<strong>Het begrip misdaad tegen de menselijkheid werd pas na de Tweede Wereldoorlog in "
                  "het recht opgenomen</strong>, bij de processen van Neurenberg. <strong>De internationale "
                  "teksten en instellingen die uit de oorlog kwamen: de Verenigde Naties in 1945</strong> en "
                  "<strong>de Universele Verklaring van de Rechten van de Mens in 1948</strong>."),
            ("p", "<strong>Lees je een getuigenis van een overlevende van Auschwitz, zestig jaar na de "
                  "feiten, dan ga je ermee om als een waardevolle bron, die je naast documenten en cijfers "
                  "legt.</strong> Over de beleving is ze onvervangbaar; over aantallen en data zijn de "
                  "administratieve bronnen scherper."),
        ]),
    ],
    onthoud=[
        "September 1939 Polen, 10 mei 1940 België (achttien dagen), juni 1941 Sovjet-Unie, december 1941 Pearl Harbor.",
        "Stalingrad als keerpunt, D-day 6 juni 1944, bevrijding september 1944, atoombommen augustus 1945.",
        "Bezetting: collaboratie, verzet met sluikpers, verplichte tewerkstelling, geen verkiezingen of vrije pers.",
        "Holocaust: uitsluiting bij wet, kentekens, getto's, Wannsee 1942, vernietigingskampen, zes miljoen doden; uit België meer dan 25 000 via Mechelen.",
        "Neurenberg: misdaden tegen de menselijkheid. 1945 VN, 1948 Universele Verklaring.",
    ],
)

BUNDELS["china-van-keizerrijk-tot-wereldmacht-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="China: van keizerrijk tot wereldmacht",
    onder="Een casus buiten Europa: vernedering, revolutie, Mao en de markt onder één partij.",
    secties=[
        dict(kop="Het keizerrijk onder druk", blokken=[
            ("p", "In de <strong>Opiumoorlogen</strong> <strong>dwong Groot-Brittannië China zijn markt voor "
                  "handel te openen</strong>, opium incluis. China verloor en moest <strong>in 1842 "
                  "Hongkong</strong> afstaan; die stad bleef Brits tot 1997. De <strong>ongelijke "
                  "verdragen</strong> waren <strong>verdragen die westerse mogendheden voorrechten in China "
                  "gaven</strong>: westerse burgers vielen er niet onder de Chinese rechtspraak. "
                  "<strong>Die verdragen hebben een gevoel van vernedering nagelaten</strong>; men spreekt van "
                  "de eeuw van de vernedering, en dat speelt in de Chinese politiek nog mee."),
            ("p", "De <strong>invloedssferen</strong> rond 1900 waren <strong>gebieden waarin één mogendheid "
                  "de handel beheerste</strong>, met haar mijnen en spoorwegen. <strong>China werd dus niet "
                  "volledig de kolonie van één mogendheid</strong>, maar het werd wel in stukken verdeeld. Men "
                  "noemt dat soms informeel imperialisme: <strong>China kreeg het imperialisme in de vorm van "
                  "verdragen</strong> en invloedssferen in plaats van een bestuur van buiten. Een spotprent "
                  "waarin mogendheden een cake met de naam China verdelen, toont <strong>dat tijdgenoten China "
                  "als te verdelen gebied beschouwden</strong>."),
            ("p", "In <strong>1900</strong> kwamen de <strong>boxers</strong> in opstand <strong>tegen de "
                  "westerse invloed in China</strong>; een internationaal leger sloeg die opstand neer. "
                  "<strong>In 1911 en 1912 viel het keizerrijk en kwam er een republiek</strong>, na meer dan "
                  "tweeduizend jaar keizers. <strong>Sun Yat-sen</strong> wordt beschouwd als de stichter van "
                  "die republiek; hij stichtte ook de nationalistische partij, de <strong>Guomindang</strong>. "
                  "<strong>Het keizerrijk bestond dus niet nog na de Tweede Wereldoorlog.</strong>"),
        ]),
        dict(kop="Burgeroorlog en Volksrepubliek", blokken=[
            ("p", "Tussen 1927 en 1949 stonden <strong>de nationalisten van de Guomindang</strong> en <strong>de "
                  "communisten onder leiding van Mao</strong> tegenover elkaar in een burgeroorlog. De "
                  "<strong>Lange Mars</strong> van 1934 en 1935 betekende dat <strong>de communisten duizenden "
                  "kilometers te voet trokken</strong>, weg uit hun belegerde gebied; Mao werd er de leider "
                  "van de partij. <strong>De communisten steunden vooral op de boeren op het platteland</strong>, "
                  "en daarin verschilden zij van Marx."),
            ("p", "Japan <strong>bezette Mantsjoerije en daarna China zelf</strong>, in 1931 en 1937: "
                  "<strong>die oorlog begon dus voor de Duitse inval in Polen</strong> en kostte miljoenen "
                  "Chinezen het leven. Op <strong>1 oktober 1949</strong> riep <strong>Mao Zedong</strong> de "
                  "Volksrepubliek China uit; de nationalisten weken uit <strong>naar het eiland "
                  "Taiwan</strong>."),
        ]),
        dict(kop="Mao", blokken=[
            ("p", "Onder Mao <strong>plande de staat de productie en nam hij de grond in bezit</strong>: de "
                  "<strong>economie was door de staat gepland</strong>, met collectivisering en "
                  "vijfjarenplannen, zoals in de Sovjet-Unie."),
            ("p", "De <strong>Grote Sprong Voorwaarts</strong> van 1958 was <strong>een plan om China in "
                  "enkele jaren te industrialiseren</strong>. Het gevolg was <strong>een hongersnood die "
                  "tientallen miljoenen mensen het leven kostte</strong>: <strong>welvarend heeft die sprong "
                  "China niet gemaakt</strong>. Tijdens de <strong>Culturele Revolutie</strong> vanaf 1966 "
                  "<strong>vielen jongeren leraren en ambtenaren aan</strong> als vijanden; die jongeren "
                  "heetten <strong>Rode Gardisten</strong>, en scholen en universiteiten vielen stil."),
            ("p", "Vergelijk je <strong>China onder Mao met de Sovjet-Unie onder Stalin</strong>, dan valt "
                  "op: <strong>één partij, een geplande economie en terreur tegen tegenstanders</strong>."),
        ]),
        dict(kop="Na 1978", blokken=[
            ("p", "<strong>Deng Xiaoping</strong> zette na de dood van Mao de economische hervormingen in. Het "
                  "Chinese model kenmerkt zich sindsdien als <strong>een markteconomie onder leiding van één "
                  "partij</strong>, socialisme met Chinese kenmerken: <strong>na 1978 kwamen markt en "
                  "buitenlandse bedrijven erbij</strong>, in <strong>speciale economische zones</strong>, "
                  "<strong>streken met gunstige regels voor buitenlandse bedrijven</strong> zoals Shenzhen. "
                  "<strong>De partij verloor haar machtspositie niet</strong>, en <strong>vrije verkiezingen "
                  "kwamen er niet</strong>."),
            ("p", "In <strong>juni 1989</strong> werd op het <strong>Tiananmenplein</strong> in Peking "
                  "<strong>een betoging voor meer vrijheid met geweld beëindigd</strong>. In "
                  "<strong>1997 werd Hongkong opnieuw een deel van China</strong>, met een eigen statuut. De "
                  "<strong>eenkindpolitiek</strong> gold van 1979 tot 2015."),
            ("p", "Vandaag <strong>is China een van de grootste economieën ter wereld</strong> en <strong>een "
                  "van de grootste uitstoters van broeikasgassen</strong>, al ligt de uitstoot per inwoner "
                  "lager dan in sommige rijke landen. De <strong>Nieuwe Zijderoute</strong> is <strong>een plan "
                  "met havens, spoorlijnen en wegen</strong> naar Azië, Afrika en Europa, waarmee ook de "
                  "politieke invloed van China groeit."),
        ]),
        dict(kop="De eeuw van de vernedering", blokken=[
            ("p", "<strong>Waarover de Opiumoorlogen in de negentiende eeuw gingen: Groot-Brittannië dwong "
                  "China zijn markt voor handel te openen.</strong> <strong>De ongelijke verdragen die China "
                  "in de negentiende eeuw moest ondertekenen, zijn verdragen die westerse mogendheden "
                  "voorrechten in China gaven</strong>: havens, lage invoerrechten en eigen rechtspraak voor "
                  "hun burgers."),
            ("p", "<strong>Over China in de negentiende eeuw: het moest havens en voorrechten aan westerse "
                  "mogendheden afstaan</strong>, en <strong>het verloor oorlogen tegen technisch sterkere "
                  "legers</strong>. Toch <strong>werd China in de negentiende eeuw niet volledig een kolonie "
                  "van één Europese mogendheid</strong>: het bleef formeel zelfstandig, maar werd in "
                  "invloedssferen verdeeld. <strong>De boxers kwamen in 1900 in opstand tegen de westerse "
                  "invloed in China.</strong>"),
        ]),
        dict(kop="Mao, Deng en de wereldeconomie", blokken=[
            ("p", "<strong>Waar de Chinese nationalisten in 1949 naartoe uitweken: naar het eiland "
                  "Taiwan.</strong> <strong>Hoe de economie van China onder Mao ingericht werd: de staat "
                  "plande de productie en nam de grond in bezit.</strong> <strong>De jongeren die tijdens "
                  "de Culturele Revolutie de oude orde aanvielen, heetten de Rode Gardisten.</strong>"),
            ("p", "<strong>Vergelijk je China onder Mao met de Sovjet-Unie onder Stalin, dan valt deze "
                  "gelijkenis op: één partij, een geplande economie en terreur tegen tegenstanders.</strong> "
                  "Het verschil zit in de nadruk: Mao mikte eerst op het platteland, Stalin op de zware "
                  "industrie."),
            ("p", "<strong>De eenkindpolitiek</strong> is <strong>de Chinese regel dat een gezin maar één "
                  "kind mocht hebben</strong>, ingevoerd om de bevolkingsgroei af te remmen en later weer "
                  "afgeschaft. <strong>De plaats van China vandaag in de wereldeconomie: het is een van de "
                  "grootste economieën ter wereld.</strong>"),
        ]),
    ],
    onthoud=[
        "Opiumoorlogen, Hongkong 1842, ongelijke verdragen en invloedssferen: de eeuw van de vernedering.",
        "1911-1912 republiek (Sun Yat-sen); 1927-1949 burgeroorlog, Lange Mars, Japanse inval 1931 en 1937.",
        "1 oktober 1949 Volksrepubliek; Grote Sprong Voorwaarts met hongersnood, Culturele Revolutie met Rode Gardisten.",
        "Na 1978 Deng: markt en speciale zones, maar één partij; 1989 Tiananmen, 1997 Hongkong, Nieuwe Zijderoute.",
    ],
)

BUNDELS["een-nieuwe-wereldorde-de-verenigde-naties-en-de-koude-oorlog-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Een nieuwe wereldorde: de Verenigde Naties en de Koude Oorlog",
    onder="Twee blokken, één ijzeren gordijn, en de crisissen tot 1989.",
    secties=[
        dict(kop="De Verenigde Naties", blokken=[
            ("p", "Na 1945 bepaalden <strong>de Verenigde Staten en de Sovjet-Unie</strong> de wereldpolitiek: "
                  "een <strong>bipolaire wereld</strong>. De <strong>Verenigde Naties</strong> werden in "
                  "<strong>1945</strong> opgericht om oorlogen te voorkomen, als opvolger van de Volkenbond."),
            ("p", "De <strong>Veiligheidsraad</strong> kan <strong>dwingende beslissingen nemen</strong>. Vijf "
                  "leden hebben er een vast zitje en een <strong>vetorecht</strong>: <strong>het recht van een "
                  "vast lid om een besluit te blokkeren</strong>. Tijdens de Koude Oorlog lag de raad daardoor "
                  "vaak verlamd. In de <strong>Universele Verklaring van de Rechten van de Mens</strong> van "
                  "1948 staan <strong>rechten die voor alle mensen, overal, gelden</strong>. "
                  "<strong>Bijna elke staat ter wereld is lid</strong> van de Verenigde Naties."),
        ]),
        dict(kop="Twee blokken", blokken=[
            ("p", "Het <strong>ijzeren gordijn</strong> was <strong>de scheidingslijn tussen west en oost in "
                  "Europa</strong>, van de Oostzee tot de Adriatische Zee. <strong>Het westen koos voor een "
                  "markteconomie en verkiezingen</strong>, <strong>het oosten voor een planeconomie en één "
                  "partij</strong>: niet enkel legers stonden tegenover elkaar, maar twee manieren om een "
                  "samenleving in te richten."),
            ("p", "Het <strong>Marshallplan</strong> was <strong>Amerikaanse steun voor de heropbouw van "
                  "West-Europa</strong>; het bond die landen tegelijk aan de Verenigde Staten, en de landen "
                  "van het Oostblok mochten er van Moskou niet op ingaan. Militair stonden <strong>de NAVO in "
                  "het westen</strong> en <strong>het Warschaupact in het oosten</strong> tegenover elkaar; "
                  "<strong>de NAVO kwam er in 1949, het Warschaupact pas in 1955</strong>."),
            ("p", "De <strong>Koude Oorlog</strong> was <strong>geen oorlog waarin beide rechtstreeks tegen "
                  "elkaar vochten</strong>, maar een strijd langs bondgenoten, wapens, spionage en propaganda. "
                  "Een Amerikaanse affiche uit 1950 die het communisme als een dreiging tekent, is "
                  "<strong>propaganda die het eigen kamp moest verenigen</strong>. De "
                  "<strong>afschrikking</strong> betekende dat <strong>wie aanvalt, zelf ook vernietigd "
                  "wordt</strong>: beide kampen hielden zoveel kernwapens dat een aanval zinloos werd."),
        ]),
        dict(kop="Duitsland en Berlijn", blokken=[
            ("p", "Duitsland <strong>werd verdeeld en in 1949 twee staten</strong>: uit de westelijke zones "
                  "kwam de Bondsrepubliek, uit de sovjetzone de Duitse Democratische Republiek. "
                  "<strong>Berlijn lag volledig in de sovjetzone</strong>, en toch werd de stad zelf in vier "
                  "sectoren verdeeld, zodat West-Berlijn als een eiland in het oosten lag."),
            ("p", "Tijdens de <strong>blokkade van Berlijn</strong> in 1948 en 1949 <strong>bracht het westen "
                  "de stad maandenlang per vliegtuig voorraden</strong>: de luchtbrug. In <strong>1961</strong> "
                  "werd de <strong>Berlijnse Muur</strong> gebouwd <strong>om de vlucht van inwoners naar het "
                  "westen te stoppen</strong>."),
        ]),
        dict(kop="Crisissen, ontspanning en einde", blokken=[
            ("p", "In Korea <strong>vochten noord en zuid tussen 1950 en 1953 een oorlog uit</strong>, elk "
                  "gesteund door een van de blokken; de wapenstilstand van 1953 geldt nog. Zo'n oorlog langs "
                  "bondgenoten heet een proxyoorlog: <strong>de grootmachten steunen elk een kant zonder zelf "
                  "te verklaren</strong>."),
            ("p", "In oktober <strong>1962</strong> <strong>plaatste de Sovjet-Unie raketten op Cuba</strong>; "
                  "die <strong>Cubacrisis bracht de wereld dicht bij een kernoorlog</strong> en werd na "
                  "dertien dagen opgelost. In <strong>1956 in Hongarije</strong> en <strong>1968 in "
                  "Tsjechoslowakije</strong> werden <strong>pogingen tot hervorming door sovjettroepen "
                  "beëindigd</strong>: <strong>vrij hun eigen koers kiezen mochten die landen dus niet</strong>."),
            ("p", "De <strong>ontspanning</strong> of <strong>détente</strong> van de jaren zeventig betekende "
                  "dat <strong>de twee blokken afspraken zochten over wapens en handel</strong>, met verdragen "
                  "over kernwapens en de slotakte van Helsinki. De <strong>niet-gebonden landen</strong> waren "
                  "<strong>landen die bij geen van de twee blokken hoorden</strong>, vaak pas onafhankelijke "
                  "staten."),
            ("p", "<strong>Gorbatsjov</strong> voerde na 1985 <strong>glasnost</strong>, <strong>meer "
                  "openheid in het publieke leven</strong>, en <strong>perestrojka</strong>, <strong>een "
                  "hervorming van de economie</strong>, in. In november <strong>1989 ging de Muur open naar "
                  "het westen</strong>, en <strong>Moskou greep deze keer niet in</strong>. In "
                  "<strong>1991 viel de Sovjet-Unie uiteen in vijftien onafhankelijke staten</strong>."),
            ("p", "Gevolgen voor Europa: <strong>Duitsland werd opnieuw één staat</strong> en <strong>landen "
                  "uit het Oostblok sloten later bij de Europese Unie aan</strong>. <strong>Het Warschaupact "
                  "verdween</strong>, dus <strong>de wereld bleef niet in twee militaire blokken "
                  "verdeeld</strong>. Het verband met de vorige oorlog: <strong>de twee overwinnaars werden na "
                  "1945 rivalen om Europa</strong>, en waar hun legers stopten, kwam de scheidingslijn te "
                  "liggen."),
        ]),
        dict(kop="De Verenigde Naties", blokken=[
            ("p", "<strong>De twee mogendheden die na 1945 de wereldpolitiek bepaalden: de Verenigde Staten "
                  "en de Sovjet-Unie.</strong> <strong>De organisatie die in 1945 werd opgericht om oorlogen "
                  "te voorkomen, zijn de Verenigde Naties.</strong> <strong>Over de Verenigde Naties: zij "
                  "werden in 1945 opgericht na de Tweede Wereldoorlog</strong>, en <strong>haar "
                  "Veiligheidsraad kan door een veto geblokkeerd worden</strong>."),
            ("p", "<strong>Het orgaan van de Verenigde Naties dat dwingende beslissingen kan nemen, is de "
                  "Veiligheidsraad</strong>: de Algemene Vergadering spreekt zich uit, de Veiligheidsraad "
                  "kan sancties en een vredesmacht opleggen."),
            ("p", "<strong>Het verband tussen de Tweede Wereldoorlog en de Koude Oorlog: de twee "
                  "overwinnaars werden na 1945 rivalen om Europa.</strong> <strong>Wat er met Duitsland na "
                  "de Tweede Wereldoorlog gebeurde: het werd verdeeld en in 1949 twee staten.</strong>"),
        ]),
        dict(kop="Twee blokken, en hun einde", blokken=[
            ("p", "<strong>De militaire bondgenootschappen die in de Koude Oorlog tegenover elkaar stonden: "
                  "de NAVO in het westen</strong> en <strong>het Warschaupact in het oosten</strong>. "
                  "<strong>Het Marshallplan was bedoeld voor West-Europa en versterkte de band met de "
                  "Verenigde Staten.</strong> <strong>Zie je een kaart van Europa uit 1960 met een dikke "
                  "lijn van de Oostzee tot de Adriatische Zee, dan stelt die het ijzeren gordijn tussen de "
                  "twee blokken voor.</strong>"),
            ("p", "<strong>Een stellingenoorlog langs bondgenoten, zoals in Korea en Vietnam, is een oorlog "
                  "waarin de grootmachten elk een kant steunen zonder zelf te verklaren.</strong> Zo bleven "
                  "ze buiten een rechtstreeks gevecht met elkaar, terwijl het land waar gevochten werd de "
                  "prijs betaalde."),
            ("p", "<strong>Lees je een Amerikaanse affiche uit 1950 waarop het communisme als een dreiging "
                  "wordt getekend, dan lees je die als propaganda die het eigen kamp moest "
                  "verenigen.</strong>"),
            ("p", "<strong>De laatste leider van de Sovjet-Unie, die glasnost en perestrojka invoerde, is "
                  "Michail Gorbatsjov.</strong> <strong>De val van de Berlijnse Muur werd door de "
                  "Sovjet-Unie niet met geweld beantwoord</strong>, en dat verklaart waarom 1989 in "
                  "Midden-Europa grotendeels vreedzaam verliep."),
        ]),
    ],
    onthoud=[
        "1945 Verenigde Naties, Veiligheidsraad met vetorecht; 1948 Universele Verklaring.",
        "Ijzeren gordijn, Marshallplan, NAVO 1949 en Warschaupact 1955; afschrikking met kernwapens.",
        "Duitsland in twee staten (1949), blokkade en luchtbrug van Berlijn, Muur in 1961.",
        "Korea 1950-1953, Cuba 1962, Hongarije 1956 en Praag 1968, détente in de jaren zeventig.",
        "Gorbatsjov: glasnost en perestrojka; Muur open in 1989, Sovjet-Unie uiteen in 1991.",
    ],
)

BUNDELS["de-europese-eenmaking-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De Europese eenmaking",
    onder="Van kolen en staal tot de euro, en de vragen die erover gesteld worden.",
    secties=[
        dict(kop="Waarom samenwerken?", blokken=[
            ("p", "Na 1945 lagen aan de Europese samenwerking twee redenen ten grondslag: <strong>een nieuwe "
                  "oorlog tussen Frankrijk en Duitsland voorkomen</strong> en <strong>de economie van het "
                  "verwoeste werelddeel heropbouwen</strong>, met het zoeken naar gewicht tussen de twee "
                  "blokken erbij. <strong>Twee oorlogen in dertig jaar tussen dezelfde buren</strong> was het "
                  "argument dat de zes over de brug haalde. <strong>Een militair bondgenootschap was de "
                  "eenmaking niet</strong>: dat bestond apart, de NAVO."),
            ("p", "De <strong>Schuman-verklaring van 1950</strong> stelde voor <strong>de kolen en het staal "
                  "van Europa samen te beheren</strong> — juist de grondstoffen van de oorlogsindustrie. "
                  "Daaruit kwam de <strong>Europese Gemeenschap voor Kolen en Staal</strong>, in 1951, met "
                  "<strong>zes landen</strong>: <strong>België, Nederland en Luxemburg</strong> en "
                  "<strong>Frankrijk, Duitsland en Italië</strong>. <strong>Groot-Brittannië hoorde daar niet "
                  "bij</strong>; het trad pas in 1973 toe. <strong>De samenwerking begon dus met kolen en "
                  "staal, niet met een munt</strong>, en met <strong>economische samenwerking, niet met "
                  "politiek</strong>."),
        ]),
        dict(kop="De verdragen", blokken=[
            ("p", tabel(["Jaar", "Verdrag of stap", "Wat het bracht"], [
                ["1951", "de EGKS", "kolen en staal samen beheren, met zes landen"],
                ["1957", "het Verdrag van Rome", "een gemeenschappelijke markt (de EEG)"],
                ["1985", "Schengen", "de grenscontroles afschaffen"],
                ["1992", "het Verdrag van Maastricht", "de Europese Unie, met de munt vastgelegd"],
                ["2002", "de euro als biljet en munt", "één munt in de eurozone"],
            ])),
            ("p", "Een <strong>douane-unie</strong> betekent dat <strong>de leden geen invoerrechten op "
                  "elkaars goederen heffen</strong> en <strong>tegenover de buitenwereld één tarief "
                  "gebruiken</strong>. Het <strong>gemeenschappelijk landbouwbeleid</strong> houdt in dat "
                  "<strong>Europa de landbouw steunt en de prijzen regelt</strong>; lang nam het het grootste "
                  "deel van de begroting in. <strong>Schengen schafte de controles aan de binnengrenzen "
                  "af</strong>, maar <strong>niet elk EU-land doet eraan mee</strong>, en Noorwegen en "
                  "Zwitserland wel zonder lid te zijn. Ook <strong>heeft niet elk land van de Unie de "
                  "euro</strong>: Denemarken, Polen en Zweden hebben hun eigen munt. De euro bestond voor de "
                  "banken al vanaf 1999."),
        ]),
        dict(kop="De instellingen", blokken=[
            ("p", tabel(["Instelling", "Wat ze doet"], [
                ["Het Europees Parlement", "wordt sinds 1979 rechtstreeks door de burgers verkozen"],
                ["De Europese Commissie", "stelt wetgeving voor en voert het beleid uit"],
                ["De Raad", "de ministers van de lidstaten; beslist samen met het Parlement"],
                ["Het Hof van Justitie", "spreekt recht over de verdragen"],
                ["De Europese Centrale Bank", "bepaalt de rentevoet van de euro"],
            ])),
            ("p", "<strong>De Commissie wordt niet rechtstreeks verkozen</strong>: haar leden worden "
                  "voorgedragen door de regeringen en door het Parlement goedgekeurd. <strong>Subsidiariteit</strong> "
                  "betekent dat <strong>wat lager geregeld kan worden, daar blijft</strong>. De <strong>Raad van "
                  "Europa staat los van de Unie</strong>: zij waakt over de mensenrechten, heeft veel meer "
                  "leden en een eigen hof in Straatsburg."),
            ("p", "<strong>België is stichtend lid, met instellingen in Brussel</strong>: de Commissie en de "
                  "Raad zitten er, en het Parlement vergadert in Brussel en in Straatsburg."),
        ]),
        dict(kop="Uitbreiding, crisis en kritiek", blokken=[
            ("p", "Uitbreidingen: <strong>Groot-Brittannië en Ierland in 1973</strong>, samen met Denemarken, "
                  "en <strong>tien landen, waarvan de meeste uit Midden-Europa, in 2004</strong>. Dat laatste "
                  "was het gevolg van de val van het ijzeren gordijn: <strong>landen uit het vroegere Oostblok "
                  "konden lid worden</strong>. De <strong>Brexit</strong> betekent dat <strong>het Verenigd "
                  "Koninkrijk de Europese Unie verliet</strong>, na een volksstemming in 2016 en met de "
                  "uittreding begin 2020: <strong>het is dus lid geweest en er weer uit gestapt</strong>, als "
                  "eerste en tot nu enige lidstaat."),
            ("p", "Tijdens de <strong>eurocrisis</strong> na 2008 <strong>hielp de Unie landen in nood met "
                  "leningen</strong> en scherpte zij de begrotingsregels aan, met harde voorwaarden. Een "
                  "voordeel van de gemeenschappelijke markt: <strong>bedrijven en mensen kunnen vrij over de "
                  "grenzen werken</strong>, met erkende diploma's. De kritiek: <strong>de beslissingen staan te "
                  "ver van de burger af</strong> en <strong>de lidstaten geven te veel bevoegdheid uit "
                  "handen</strong>. Wie dat schrijft, geeft <strong>een standpunt in het debat</strong>, geen "
                  "beschrijving van de feiten."),
            ("p", "<strong>De Unie is geen staat met één regering en één leger</strong>, maar een verbond van "
                  "staten die bevoegdheden samen uitoefenen. Het verschil met de Verenigde Naties: <strong>de "
                  "Unie maakt wetten die in haar lidstaten gelden</strong>, terwijl de Verenigde Naties met "
                  "verdragen en resoluties werken."),
        ]),
        dict(kop="Stap voor stap, van 1951 tot vandaag", blokken=[
            ("p", "<strong>De twee grondstoffen die de zes landen in 1951 samen gingen beheren: steenkool en "
                  "staal.</strong> <strong>Groot-Brittannië hoorde niet bij de zes stichters van de eerste "
                  "Europese gemeenschap</strong>; het sloot pas in 1973 aan. <strong>Het verband tussen de "
                  "twee wereldoorlogen en de Europese eenmaking: de eenmaking moest een nieuwe oorlog "
                  "onmogelijk maken.</strong>"),
            ("p", "<strong>Wat in 1957 in het Verdrag van Rome werd afgesproken: een gemeenschappelijke "
                  "markt tussen de leden.</strong> <strong>In Maastricht werd in 1992 het verdrag gesloten "
                  "dat de Europese Unie oprichtte.</strong> <strong>De eurobiljetten en de euromunten kwamen "
                  "in 2002 in omloop</strong>, tien jaar na dat verdrag. <strong>Samengevat: de eenmaking "
                  "begon met zes landen en groeide stap voor stap</strong>, en <strong>ze begon met "
                  "economische samenwerking, niet met politiek</strong>."),
            ("p", "<strong>Het verband tussen het einde van de Koude Oorlog en de Europese Unie: landen uit "
                  "het vroegere Oostblok konden lid worden.</strong> In 2004 kwamen er tien landen bij. En "
                  "één land ging de andere kant op: <strong>het vertrek van het Verenigd Koninkrijk uit de "
                  "Europese Unie heet de brexit</strong>. <strong>De Europese Commissie en de Raad zitten in "
                  "de Belgische stad Brussel.</strong>"),
        ]),
        dict(kop="Voor en tegen", blokken=[
            ("p", "<strong>Het voordeel dat aan de gemeenschappelijke markt toegeschreven wordt: bedrijven "
                  "en mensen kunnen vrij over de grenzen werken.</strong> <strong>De kritiek die op de "
                  "Europese Unie geformuleerd wordt: de beslissingen staan te ver van de burger af</strong>, "
                  "en <strong>de lidstaten geven te veel bevoegdheid uit handen</strong>."),
            ("p", "<strong>Lees je een opiniestuk dat Europa te ver van de mensen staat en dat de lidstaten "
                  "te weinig te zeggen hebben, dan is dat een standpunt in het debat over de Europese "
                  "Unie.</strong> Geen vaststelling, en ook geen onzin: een standpunt dat je naast het "
                  "andere legt."),
            ("p", "<strong>Vergelijk je de Europese Unie met de Verenigde Naties, dan valt dit verschil op: "
                  "de Unie maakt wetten die in haar lidstaten gelden.</strong> De Verenigde Naties zijn een "
                  "overlegorganisatie tussen regeringen; de Unie is op dat punt supranationaal."),
        ]),
    ],
    onthoud=[
        "Schuman 1950: kolen en staal samen; EGKS 1951 met zes landen, Groot-Brittannië pas in 1973.",
        "Rome 1957: gemeenschappelijke markt en douane-unie. Schengen: geen binnengrenzen. Maastricht 1992: de Unie.",
        "Euro als biljet in 2002, maar niet in elk EU-land.",
        "Parlement verkozen sinds 1979; Commissie stelt voor en voert uit; Raad van ministers beslist mee; subsidiariteit.",
        "2004 uitbreiding naar Midden-Europa, Brexit in 2020.",
    ],
)

BUNDELS["de-dekolonisatie-van-congo-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="De dekolonisatie van Congo",
    onder="Van 30 juni 1960 over de Congocrisis en Mobutu tot het debat in België vandaag.",
    secties=[
        dict(kop="Dekolonisatie na 1945", blokken=[
            ("p", "<strong>Dekolonisatie</strong> betekent dat <strong>kolonies onafhankelijke staten "
                  "worden</strong>. Het grootste deel van Azië en Afrika werd tussen 1945 en 1975 "
                  "onafhankelijk: <strong>de dekolonisatie betrof dus zowel Azië als Afrika</strong>, met "
                  "India in 1947 en Indonesië in 1949. <strong>1960</strong> heet het <strong>Afrikaanse "
                  "jaar</strong>, omdat een hele reeks Afrikaanse staten dat jaar onafhankelijk werd."),
            ("p", "Oorzaken: <strong>de Europese mogendheden waren door de oorlog verzwakt</strong> en "
                  "<strong>in de kolonies groeiden bewegingen die zelfbestuur eisten</strong>. "
                  "<strong>De Tweede Wereldoorlog had het prestige van Europa aangetast</strong>, en "
                  "<strong>soldaten uit de kolonies hadden in Europa meegevochten</strong>. Het handvest van "
                  "de Verenigde Naties sprak van het zelfbeschikkingsrecht van volken. "
                  "<strong>Zonder conflict ging het niet overal</strong>: in Algerije, Indochina en Kenia zijn "
                  "er lange oorlogen aan voorafgegaan. In de Koude Oorlog <strong>dongen de twee blokken naar "
                  "de gunst van de nieuwe staten</strong>."),
        ]),
        dict(kop="De weg naar 30 juni 1960", blokken=[
            ("p", "In België dacht men in de jaren vijftig nog <strong>dat de onafhankelijkheid nog tientallen "
                  "jaren weg was</strong>: een Belgische hoogleraar stelde in 1955 een plan van dertig jaar "
                  "voor, en dat lag toen al gevoelig. <strong>Snel onafhankelijk maken was dus niet het "
                  "plan.</strong>"),
            ("p", "<strong>In Congo waren er voor 1960 politieke bewegingen die zelfbestuur eisten</strong>, "
                  "vooral uit de kringen van de <strong>évolués</strong>, <strong>de Congolezen met een "
                  "opleiding</strong>; het manifest van Conscience africaine uit 1956 is een voorbeeld. De "
                  "eerste voormannen waren <strong>Joseph Kasavubu met zijn beweging in Leopoldstad</strong> en "
                  "<strong>Patrice Lumumba met zijn nationale beweging</strong>."),
            ("p", "In <strong>januari 1959 braken in Leopoldstad zware rellen uit tegen het koloniale "
                  "bestuur</strong>. Op de <strong>Ronde Tafelconferentie</strong> in Brussel werd in 1960 "
                  "beslist dat <strong>Congo op 30 juni van dat jaar onafhankelijk zou worden</strong>: "
                  "<strong>jarenlang voorbereid is die onafhankelijkheid dus niet</strong>, er lag maar "
                  "anderhalf jaar tussen. <strong>Patrice Lumumba</strong> werd de eerste premier, Kasavubu "
                  "staatshoofd. Op de plechtigheid <strong>sprak Lumumba openlijk over het onrecht van de "
                  "koloniale tijd</strong>, wat niet in het programma stond."),
            ("p", "Congo stond er slecht voor om zichzelf te besturen, want <strong>er waren amper Congolezen "
                  "met een universitair diploma</strong>: lager onderwijs was er ruim, hoger onderwijs amper."),
        ]),
        dict(kop="De Congocrisis en Mobutu", blokken=[
            ("p", "In juli 1960 <strong>kwam het leger in opstand en scheidde Katanga zich af</strong>: "
                  "<strong>een rustig en stabiel land was Congo vanaf 1960 niet</strong>. Die afscheiding woog "
                  "zwaar <strong>omdat daar de mijnen van het land lagen</strong>, met het koper van Katanga, "
                  "en Belgische belangen speelden mee. De <strong>Verenigde Naties stuurden troepen om de orde "
                  "te bewaren</strong> en de eenheid van het land te bewaken."),
            ("p", "Begin <strong>1961 werd Lumumba afgezet, gevangengenomen en vermoord</strong>. "
                  "<strong>Een Belgische parlementaire onderzoekscommissie stelde in 2001 een Belgische "
                  "betrokkenheid vast</strong>, veertig jaar na de feiten."),
            ("p", "In <strong>1965 nam Mobutu Sese Seko met een staatsgreep de macht over</strong>: "
                  "<strong>met vrije verkiezingen kwam hij er dus niet</strong>. In <strong>1971</strong> gaf "
                  "hij het land de naam <strong>Zaïre</strong>, die het tot 1997 hield. Zijn bestuur "
                  "kenmerkte zich door <strong>één partij, geen vrije pers en geen vrije verkiezingen</strong> "
                  "en <strong>grote rijkdom voor hemzelf en zijn omgeving</strong>: men spreekt van een "
                  "kleptocratie. <strong>Het westen hield hem lang de hand boven het hoofd omdat hij in de "
                  "Koude Oorlog een bondgenoot tegen het communisme was</strong>."),
            ("p", "In <strong>1997 werd Mobutu afgezet en heette het land weer Congo</strong>, als "
                  "Democratische Republiek Congo. Daarna volgden oorlogen, vooral in het oosten: daar "
                  "<strong>vechten gewapende groepen om gebied en om mijnen</strong> en zijn "
                  "<strong>miljoenen mensen op de vlucht geweest</strong>. <strong>De grondstoffen van Congo "
                  "spelen nog altijd een rol in de wereldeconomie</strong>: kobalt en coltan zitten in "
                  "batterijen en elektronica."),
        ]),
        dict(kop="Het debat in België", blokken=[
            ("p", "<strong>Het koloniale verleden wordt in België vandaag onderzocht en besproken.</strong> In "
                  "<strong>2020 richtte het Belgische parlement een commissie op om dat verleden te "
                  "onderzoeken</strong>; de werkzaamheden leverden veel materiaal op, maar geen gezamenlijk "
                  "besluit. <strong>Koning Filip sprak in 2020 in een brief zijn diepste spijt uit</strong> en "
                  "herhaalde die spijt bij zijn bezoek in 2022; een formele verontschuldiging was het niet."),
            ("p", "Vergelijk <strong>Belgisch Congo van 1950 met Congo van 1965</strong>: <strong>het bestuur "
                  "lag eerst in Brussel en daarna bij één man in het land</strong>. Dat de koloniale tijd "
                  "doorwerkt, blijkt daaruit dat <strong>grenzen, economie en bestuur er nog de sporen van "
                  "dragen</strong>."),
        ]),
        dict(kop="Het Afrikaanse jaar", blokken=[
            ("p", "<strong>1960 wordt het Afrikaanse jaar genoemd</strong>, omdat zeventien Afrikaanse "
                  "landen in dat ene jaar onafhankelijk werden. <strong>De eerste Congolese voormannen die "
                  "zelfbestuur eisten: Joseph Kasavubu met zijn beweging in Leopoldstad</strong>, en "
                  "<strong>Patrice Lumumba met zijn nationale beweging</strong>. Eerder al vroegen "
                  "<strong>de évolués</strong>, <strong>de Congolezen met een opleiding</strong>, als "
                  "eersten politieke rechten."),
            ("p", "<strong>Congo werd onafhankelijk op 30 juni 1960.</strong> <strong>De onafhankelijkheid "
                  "van Congo werd niet jarenlang zorgvuldig voorbereid</strong>: tussen de rellen van "
                  "januari 1959 en de machtsoverdracht lag ruim een jaar. <strong>Over de toespraak van "
                  "Lumumba op de plechtigheid van 30 juni 1960: hij sprak openlijk over het onrecht van de "
                  "koloniale tijd</strong>, tegen de verwachtingen van de plechtigheid in. <strong>Zie je een "
                  "foto van 30 juni 1960 met de Belgische koning en Congolese leiders samen, dan stelt die de "
                  "plechtigheid van de onafhankelijkheid voor.</strong>"),
        ]),
        dict(kop="Wat erna kwam", blokken=[
            ("p", "<strong>Congo was vanaf 1960 niet meteen een rustig en stabiel land</strong>: het leger "
                  "kwam in opstand, Katanga scheidde zich af, en in januari 1961 werd Lumumba vermoord."),
            ("p", "<strong>De problemen die het oosten van Congo tot vandaag kent: gewapende groepen vechten "
                  "er om gebied en om mijnen</strong>, en <strong>miljoenen mensen zijn er op de vlucht "
                  "geweest</strong>."),
            ("p", "<strong>Waarom gezegd wordt dat de koloniale tijd in Congo tot vandaag doorwerkt: "
                  "grenzen, economie en bestuur dragen er nog de sporen van.</strong> De grenzen zijn in "
                  "Berlijn getekend, de economie draait nog op de uitvoer van enkele grondstoffen, en het "
                  "bestuur erfde een apparaat dat nooit voor zelfbestuur was gemaakt."),
        ]),
    ],
    onthoud=[
        "Dekolonisatie: kolonies worden staten; 1960 het Afrikaanse jaar, Congo op 30 juni.",
        "Januari 1959 rellen in Leopoldstad, Ronde Tafel in Brussel, Lumumba premier en Kasavubu staatshoofd.",
        "Juli 1960 muiterij en afscheiding van Katanga, VN-troepen, moord op Lumumba in 1961 met Belgische betrokkenheid.",
        "Mobutu 1965-1997, Zaïre vanaf 1971, kleptocratie met westerse steun; daarna oorlogen in het oosten.",
        "2020: parlementaire commissie en de spijt van koning Filip.",
    ],
)

BUNDELS["belgie-na-1945-breuklijnen-federale-staat-en-emancipatie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="België na 1945: breuklijnen, federale staat en emancipatie",
    onder="Drie breuklijnen, zes staatshervormingen en een halve eeuw emancipatie.",
    secties=[
        dict(kop="De drie breuklijnen", blokken=[
            ("p", "Door de Belgische politiek lopen <strong>drie breuklijnen</strong>: <strong>tussen "
                  "gelovigen en vrijzinnigen</strong>, <strong>tussen arbeid en kapitaal</strong>, en de "
                  "<strong>communautaire breuklijn tussen Nederlandstaligen en Franstaligen</strong>. Zij "
                  "verklaren ook de <strong>verzuiling</strong>: rond elke strekking groeiden eigen scholen, "
                  "ziekenfondsen, vakbonden en verenigingen."),
            ("p", "De <strong>koningskwestie</strong> ging <strong>over de houding van Leopold III tijdens de "
                  "bezetting</strong>. Na een volksraadpleging en zware onrust <strong>deed Leopold III in "
                  "1951 troonsafstand</strong> ten gunste van zijn zoon Boudewijn: <strong>koning tot zijn "
                  "dood is hij dus niet gebleven</strong>."),
            ("p", "De <strong>schoolstrijd</strong> van de jaren vijftig ging <strong>over het geld voor het "
                  "katholieke onderwijs</strong>, <strong>niet over de taal van het onderwijs</strong>. Het "
                  "<strong>Schoolpact</strong> van <strong>1958</strong> maakte er een einde aan: vrij en "
                  "officieel onderwijs worden beide door de overheid betaald, met vrije schoolkeuze."),
            ("p", "In <strong>1962 en 1963 werd de taalgrens vastgelegd</strong> en de bestuurstaal per gebied "
                  "bepaald; over Voeren en de Brusselse rand is nog lang getwist. <strong>Leuven Vlaams</strong> "
                  "in 1968 ging <strong>over het Franstalige deel van de universiteit</strong>, dat naar "
                  "Louvain-la-Neuve verhuisde; die affiche hoort <strong>bij de communautaire breuklijn</strong>."),
        ]),
        dict(kop="Van unitaire naar federale staat", blokken=[
            ("p", "Er waren <strong>vier staatshervormingen, tussen 1970 en 1993</strong>, nodig voor België "
                  "een federale staat werd; daarna volgden nog twee. <strong>Sinds 1993 staat in de grondwet "
                  "dat België een federale staat is.</strong>"),
            ("p", "Er zijn twee soorten deelstaten: <strong>de gemeenschappen, bevoegd voor taal, cultuur en "
                  "onderwijs</strong>, en <strong>de gewesten, bevoegd voor grondgebied en economie</strong>, "
                  "drie van elk. <strong>Het onderwijs en de cultuur</strong> en <strong>het leefmilieu en de "
                  "economie van een gewest</strong> gingen dus naar de deelstaten; <strong>defensie, justitie "
                  "en het buitenlands beleid bleven federaal</strong>, en de munt is Europees geworden."),
            ("p", "<strong>Brussel is tweetalig en hoort bij twee gemeenschappen</strong>: het is een eigen "
                  "gewest, en zowel de Vlaamse als de Franse Gemeenschap zijn er bevoegd. Het verband met de "
                  "breuklijnen: <strong>de communautaire breuklijn dreef de hervormingen vooruit</strong>, en "
                  "elke hervorming was een antwoord op een spanning, zelden het einde ervan. Vandaag "
                  "<strong>weegt de communautaire breuklijn nog, de godsdienstige minder</strong>, en er kwamen "
                  "nieuwe strijdpunten bij."),
        ]),
        dict(kop="Welvaart en werk", blokken=[
            ("p", "In het <strong>sociaal pact van 1944</strong> werd <strong>een stelsel van sociale "
                  "zekerheid met overleg</strong> tussen werkgevers en vakbonden afgesproken: pensioen, "
                  "kinderbijslag, ziekte en werkloosheid. De <strong>wereldtentoonstelling van 1958</strong> in "
                  "Brussel staat <strong>voor het geloof in de vooruitgang na de oorlog</strong>; het Atomium "
                  "is er nog van over."),
            ("p", "De jaren vijftig en zestig kenmerkten zich door <strong>een sterke groei van de welvaart en "
                  "van het verbruik</strong>, met auto, koelkast, televisie en vakantie, en <strong>meer vrije "
                  "tijd</strong> door betaalde vakantie en een kortere werkweek."),
            ("p", "De <strong>steenkoolmijnen sloten één na één, de laatste in de jaren negentig</strong>: de "
                  "Waalse eerst, <strong>de Limburgse later</strong>, met Zolder in 1992 als laatste. De crisis "
                  "van de jaren zeventig bracht <strong>een sterke stijging van de werkloosheid</strong> en "
                  "<strong>achteruitgang van de zware industrie in Wallonië</strong>; het economische "
                  "zwaartepunt verschoof naar Vlaanderen."),
        ]),
        dict(kop="Emancipatie en ontzuiling", blokken=[
            ("p", "De Belgische vrouwen mochten <strong>in 1948</strong> voor het eerst voor het parlement "
                  "stemmen, dertig jaar na de mannen: <strong>voor de Eerste Wereldoorlog hadden zij dat recht "
                  "dus niet</strong>. In <strong>1966</strong> staakten de vrouwen van de wapenfabriek in "
                  "<strong>Herstal</strong> <strong>voor gelijk loon voor gelijk werk</strong>, drie maanden "
                  "lang."),
            ("p", "Bij de emancipatie van de vrouw horen <strong>gelijkheid van man en vrouw in het "
                  "huwelijksrecht</strong> en <strong>het recht op informatie over voorbehoedsmiddelen</strong>; "
                  "tot in de jaren zeventig had de man wettelijk het laatste woord in een huwelijk. In "
                  "<strong>1990 werd abortus onder voorwaarden uit het strafrecht gehaald</strong>, en in "
                  "<strong>2003 mochten koppels van hetzelfde geslacht huwen</strong> — België was het tweede "
                  "land ter wereld, en adoptie volgde in 2006. <strong>Die emancipatiewetten zijn dus niet van "
                  "de negentiende eeuw</strong>, maar van na 1960 en soms van na 2000."),
            ("p", "<strong>Mei 1968</strong> kenmerkte zich doordat <strong>jongeren het gezag van school en "
                  "kerk betwistten</strong>, en dat van hun ouders. <strong>Ontzuiling</strong> betekent dat "
                  "<strong>de greep van de zuilen afnam</strong>: men kiest zijn ziekenfonds, zijn school en "
                  "zijn vereniging niet meer vanzelf binnen één strekking."),
            ("p", "Vergelijk een Belgisch gezin van 1950 met een gezin van 2020: <strong>veel meer vrouwen "
                  "werken buitenshuis</strong>, en de gezinsvormen zijn veelzijdiger geworden."),
        ]),
        dict(kop="De drie breuklijnen en de staatshervormingen", blokken=[
            ("p", "<strong>De drie breuklijnen die de Belgische politiek na 1945 verdeelden: de breuklijn "
                  "tussen gelovigen en vrijzinnigen</strong>, <strong>de breuklijn tussen arbeid en "
                  "kapitaal</strong>, en de communautaire breuklijn tussen Vlamingen en Franstaligen."),
            ("p", "<strong>Hoe de koningskwestie eindigde: Leopold III deed in 1951 troonsafstand.</strong> "
                  "<strong>Het Schoolpact beëindigde in 1958 de schoolstrijd.</strong> <strong>Wat in 1962 "
                  "en 1963 met de taalwetten geregeld werd: de taalgrens werd vastgelegd</strong>, en ook "
                  "per gebied de taal van het bestuur en het onderwijs. <strong>Zie je een affiche uit 1968 "
                  "met de leuze Leuven Vlaams, dan hoort die bij de communautaire breuklijn.</strong>"),
            ("p", "<strong>In 1993 werd in de grondwet geschreven dat België een federale staat is.</strong> "
                  "<strong>De bevoegdheden die naar de deelstaten zijn overgegaan: het onderwijs en de "
                  "cultuur</strong>, en <strong>het leefmilieu en de economie van een gewest</strong>. "
                  "<strong>Waarom Brussel in de Belgische staat een bijzondere plaats heeft: het is "
                  "tweetalig en hoort bij twee gemeenschappen.</strong>"),
        ]),
        dict(kop="Crisis, emancipatie en ontzuiling", blokken=[
            ("p", "<strong>De gevolgen van de economische crisis van de jaren zeventig voor België: de "
                  "werkloosheid steeg sterk</strong>, en <strong>de zware industrie in Wallonië ging "
                  "achteruit</strong>. In Limburg sloten later de steenkoolmijnen, met een zware "
                  "omschakeling als gevolg."),
            ("p", "<strong>Wat mei 1968 en de jaren erna in West-Europa kenmerkte: jongeren betwistten het "
                  "gezag van school en kerk.</strong> <strong>Ontzuiling in de Belgische samenleving "
                  "betekent dat de greep van de zuilen afnam</strong>: mensen kozen hun school, ziekenkas, "
                  "vakbond en vereniging minder vanzelf binnen één strekking."),
            ("p", "<strong>De veranderingen die bij de emancipatie van de vrouw in België horen: gelijkheid "
                  "van man en vrouw in het huwelijksrecht</strong>, en <strong>het recht op informatie over "
                  "voorbehoedsmiddelen</strong>. <strong>In 2003 besliste België dat koppels van hetzelfde "
                  "geslacht mochten huwen.</strong> <strong>De emancipatiewetten in België zijn dus niet "
                  "allemaal in de negentiende eeuw gestemd</strong>: de meeste komen uit de tweede helft van "
                  "de twintigste eeuw en later."),
        ]),
    ],
    onthoud=[
        "Drie breuklijnen: gelovig/vrijzinnig, arbeid/kapitaal, Nederlandstalig/Franstalig; daaruit de verzuiling.",
        "Koningskwestie: troonsafstand 1951. Schoolpact 1958. Taalgrens 1962. Leuven Vlaams 1968.",
        "Vier staatshervormingen 1970-1993; sinds 1993 federale staat, met drie gemeenschappen en drie gewesten.",
        "Sociaal pact 1944, Expo 58, welvaartsgroei, mijnsluitingen tot 1992, crisis van de jaren zeventig.",
        "Vrouwenstemrecht 1948, Herstal 1966, abortus 1990, huwelijk voor iedereen 2003; mei 68 en ontzuiling.",
    ],
)

BUNDELS["kunst-en-cultuur-een-kunstwerk-analyseren-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kunst en cultuur: een kunstwerk analyseren",
    onder="Een werkwijze om een werk te lezen, en de stijlen van twee eeuwen.",
    secties=[
        dict(kop="De werkwijze", blokken=[
            ("p", "Je begint met <strong>beschrijven wat je werkelijk ziet</strong>: eerst vaststellen, dan "
                  "verklaren. Wie met zijn mening begint, ziet de helft niet meer."),
            ("p", tabel(["Vraag", "Waar het over gaat"], [
                ["Welke kleuren, lijnen en compositie?", "de vormkenmerken"],
                ["Welk materiaal en welke techniek?", "de vormkenmerken"],
                ["Waarvoor is het gemaakt, waar hing het?", "de functie"],
                ["Wie heeft het laten maken?", "de opdrachtgever"],
                ["In welke tijd en samenleving?", "de context"],
            ])),
            ("p", "De <strong>compositie</strong> is <strong>de manier waarop de delen over het vlak verdeeld "
                  "zijn</strong>; wat in het midden staat en waar het licht valt, stuurt je blik. "
                  "<strong>De opdrachtgever hoort bij de analyse omdat wie betaalt vaak bepaalt wat er te zien "
                  "is.</strong> De <strong>context</strong> is <strong>de tijd waarin het gemaakt is</strong>, "
                  "en de samenleving errond: <strong>zonder context blijft een werk een plaatje</strong>. Ook "
                  "<strong>het materiaal doet mee</strong>, want marmer, beton, staal of fotopapier vragen elk "
                  "geld en techniek. <strong>Ook een gebouw of een affiche kan je als kunstwerk "
                  "analyseren</strong>: <strong>je leest er materiaal en stijl uit</strong>, en de bedoeling "
                  "van de bouwer."),
            ("p", "Voor een historicus is een kunstwerk vooral een bron <strong>over de ideeën en de smaak van "
                  "zijn eigen tijd</strong>. <strong>Een historisch schilderij is geen betrouwbaar verslag van "
                  "de gebeurtenis</strong>, want <strong>het is vaak later gemaakt en met een bedoeling</strong>: "
                  "de maker kiest wat hij toont en wie groot in beeld komt. Daarom <strong>zet een historicus "
                  "een kunstwerk naast andere bronnen</strong>, <strong>om te toetsen wat het wel en niet kan "
                  "aantonen</strong>. Bij een propaganda-affiche vraag je <strong>wie ze heeft laten maken en "
                  "voor wie ze bedoeld was</strong> en <strong>welk beeld van de vijand wordt opgeroepen</strong>."),
            ("p", "Een portret van een negentiende-eeuwse fabrikant in zijn salon zegt <strong>dat hij zijn "
                  "rijkdom en zijn stand wilde laten zien</strong>: boeken, meubels en kledij zijn geen toeval."),
        ]),
        dict(kop="Stijlen van de negentiende eeuw", blokken=[
            ("p", "De <strong>romantiek</strong> kenmerkt zich door <strong>gevoel, verbeelding en het eigen "
                  "verleden</strong>; <strong>zij gaf veel aandacht aan het eigen verleden en de eigen "
                  "taal</strong> en heeft zo het nationalisme gevoed. Het <strong>realisme</strong> toont "
                  "<strong>het gewone leven en de arbeid zonder opsmuk</strong>: <strong>het bracht het leven "
                  "van arbeiders en boeren in beeld</strong>, wat nieuw was. Het "
                  "<strong>impressionisme</strong> gaat over <strong>licht en kleur op het moment van het "
                  "kijken</strong>, met een zichtbare toets."),
            ("p", "Nieuwe kunstvormen van deze twee eeuwen zijn <strong>de fotografie</strong> en <strong>de "
                  "film</strong>; fresco's en glasramen bestonden al eeuwen. De fotografie had als gevolg dat "
                  "<strong>schilders op zoek gingen naar wat een foto niet kon</strong>."),
            ("p", "<strong>Victor Horta</strong> staat <strong>voor de art nouveau in de Brusselse "
                  "architectuur</strong>: <strong>de bouwstijl rond 1900 met gebogen lijnen, ijzer en "
                  "glas</strong>, in Duitsland <strong>jugendstil</strong> genoemd. <strong>René "
                  "Magritte</strong> is de Belgische kunstenaar die wereldberoemd is om zijn surrealistische "
                  "schilderijen. De nieuwe materialen <strong>staal en gewapend beton</strong> en <strong>glas in "
                  "grote vlakken</strong> maakten <strong>nieuwe bouwstijlen mogelijk</strong>: stations, "
                  "hallen, de Eiffeltoren en later wolkenkrabbers."),
        ]),
        dict(kop="De twintigste eeuw en de macht", blokken=[
            ("p", "Het <strong>expressionisme</strong> kenmerkt zich doordat <strong>het gevoel sterker wordt "
                  "dan de juiste weergave</strong>: vormen vervormd, kleuren overdreven. <strong>Abstracte "
                  "kunst</strong> geeft <strong>niets herkenbaars uit de werkelijkheid weer</strong>: "
                  "<strong>zij beeldt de werkelijkheid dus niet nauwkeurig af</strong>, kleur en vorm zijn "
                  "zelf het onderwerp. Vergelijk je een realistisch werk uit 1870 met een abstract werk uit "
                  "1930, dan valt op: <strong>het eerste toont mensen, het tweede vorm en kleur</strong>."),
            ("p", "Een totalitair regime gebruikte de kunst <strong>als propaganda, met een voorgeschreven "
                  "stijl en inhoud</strong>: <strong>vrij was de kunstenaar daar niet</strong>. Het naziregime "
                  "<strong>bestempelde kunst die het afwees als ontaard</strong> en haalde ze uit de musea, met "
                  "in 1937 zelfs een spottentoonstelling. Het <strong>socialistisch realisme</strong> in de "
                  "Sovjet-Unie was <strong>een voorgeschreven stijl die arbeid verheerlijkt</strong>: een "
                  "schilderij van heldhaftige arbeiders bij een hoogoven uit 1935 lees je <strong>als kunst in "
                  "dienst van het regime en zijn plannen</strong>."),
            ("p", "Het verband met de samenleving: <strong>de kunst volgde de breuken van haar tijd</strong> "
                  "en gaf er commentaar op. Oorlog, techniek, stad en massamedia zijn er allemaal in terug te "
                  "vinden."),
        ]),
        dict(kop="De stappen van een analyse", blokken=[
            ("p", "<strong>Met welke stap je begint als je een kunstwerk onderzoekt: beschrijven wat je "
                  "werkelijk ziet.</strong> <strong>Bij de analyse van een kunstwerk komt beschrijven dus "
                  "voor besluiten.</strong> Wie omgekeerd werkt, zoekt in het werk de bevestiging van wat "
                  "hij al dacht."),
            ("p", "De <strong>compositie</strong> is <strong>de manier waarop de delen van een werk over het "
                  "vlak verdeeld zijn</strong>, ook de <strong>opbouw</strong> genoemd. De "
                  "<strong>context</strong> is <strong>het geheel van de tijd en de samenleving waarin een "
                  "werk gemaakt is</strong>. <strong>De opdrachtgever van een werk kan de inhoud ervan "
                  "bepalen</strong>: wie betaalt, zegt vaak wat erop moet komen. <strong>In een totalitaire "
                  "staat was de kunstenaar niet volledig vrij in zijn keuzes</strong>: wat niet in de lijn "
                  "lag, heette ontaarde kunst en werd verboden."),
            ("p", "<strong>Een kunstwerk is voor een historicus vooral bruikbaar als bron over de ideeën en "
                  "de smaak van zijn eigen tijd.</strong> <strong>Krijg je een portret van een "
                  "negentiende-eeuwse fabrikant in zijn salon, dan besluit je uit de keuze van die omgeving "
                  "dat hij zijn rijkdom en zijn stand wilde laten zien.</strong>"),
        ]),
        dict(kop="Nieuwe technieken, nieuwe stijlen", blokken=[
            ("p", "<strong>Wat het realisme in de kunst van de negentiende eeuw kenmerkt: het gewone leven "
                  "en de arbeid worden zonder opsmuk getoond.</strong> <strong>Wat abstracte kunst kenmerkt: "
                  "er wordt niets herkenbaars uit de werkelijkheid weergegeven.</strong>"),
            ("p", "<strong>De nieuwe kunstvormen die in de negentiende en twintigste eeuw opkwamen: de "
                  "fotografie</strong> en <strong>de film</strong>. <strong>Het gevolg van de fotografie "
                  "voor de schilderkunst: schilders gingen op zoek naar wat een foto niet kon</strong>, zoals "
                  "licht, beweging, gevoel en abstractie."),
            ("p", "<strong>De nieuwe materialen die de architectuur van de negentiende en twintigste eeuw "
                  "veranderden: staal en gewapend beton</strong>, en <strong>glas in grote vlakken</strong>. "
                  "<strong>Nieuwe bouwmaterialen uit de industrie maakten nieuwe bouwstijlen "
                  "mogelijk.</strong> Een voorbeeld is de <strong>art nouveau</strong>, ook "
                  "<strong>jugendstil</strong> genoemd: <strong>de bouwstijl rond 1900 met gebogen lijnen, "
                  "ijzer en glas, waarvan Victor Horta een meester was.</strong>"),
        ]),
    ],
    onthoud=[
        "Eerst beschrijven, dan verklaren: vorm, inhoud, functie, opdrachtgever, context.",
        "Een kunstwerk is vooral een bron over de ideeën en de smaak van zijn eigen tijd.",
        "Romantiek, realisme, impressionisme, expressionisme, abstracte kunst; art nouveau (Horta) en surrealisme (Magritte).",
        "Fotografie en film als nieuwe kunstvormen; staal, beton en glas als nieuwe bouwmaterialen.",
        "Totalitaire regimes schreven stijl en inhoud voor: ontaarde kunst en socialistisch realisme.",
    ],
)

BUNDELS["redeneren-met-bronnen-bruikbaarheid-en-betrouwbaarheid-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Redeneren met bronnen: bruikbaarheid en betrouwbaarheid",
    onder="Het zwaarste onderdeel van het vak: welke bron je nodig hebt, en wat ze waard is.",
    secties=[
        dict(kop="Soorten bronnen", blokken=[
            ("p", "Een <strong>primaire bron</strong> is <strong>een bron uit de tijd van de gebeurtenis "
                  "zelf</strong>: een brief, een foto, een register, een voorwerp. Een <strong>secundaire "
                  "bron</strong> is <strong>een werk dat later over de gebeurtenis geschreven is</strong>, "
                  "zoals een handboek of een studie. <strong>Een primaire bron is niet automatisch "
                  "betrouwbaarder</strong>: een ooggetuige kan zich vergissen of belang hebben, en een latere "
                  "studie kan juist alles naast elkaar leggen."),
            ("p", "Een historicus gebruikt <strong>schriftelijke bronnen, zoals brieven, kranten en "
                  "registers</strong> en <strong>materiële bronnen, zoals gebouwen, werktuigen en "
                  "munten</strong>, plus beeldbronnen, mondelinge getuigenissen en digitale bronnen. "
                  "<strong>Een gebouw of een werktuig is dus ook een historische bron.</strong>"),
        ]),
        dict(kop="Bruikbaarheid", blokken=[
            ("p", "Je begint met <strong>een historische vraag</strong>, want <strong>zonder vraag kan je niet "
                  "beoordelen wat je nodig hebt</strong>: <strong>of een bron bruikbaar is, hangt af van de "
                  "vraag die je stelt</strong>. Een bron is bruikbaar <strong>als ze over thema, tijd en plaats "
                  "van je vraag gaat</strong>. Een betrouwbare bron over de verkeerde plaats of tijd blijft "
                  "onbruikbaar."),
            ("p", "Onderzoek je het dagelijks leven van mijnwerkers in Limburg rond 1950, dan is <strong>een "
                  "dagboek van een mijnwerker uit Zolder</strong> bruikbaar: thema, tijd en plaats kloppen. "
                  "Onderzoek je hoe de bezetter in 1942 over het verzet sprak, dan is <strong>een krant die "
                  "onder censuur van de bezetter verscheen</strong> juist de beste bron: <strong>ze toont wat "
                  "de bezetter wilde laten lezen</strong>. Een onbetrouwbare bron over de feiten kan een "
                  "uitstekende bron over de bedoelingen zijn."),
            ("p", "Een <strong>anachronisme</strong> is <strong>iets uit een andere tijd in een verkeerde tijd "
                  "plaatsen</strong>. Een bron <strong>in haar context lezen</strong> betekent dat <strong>je ze "
                  "leest met de tijd en de omstandigheden erbij</strong>: <strong>het best met de kennis van "
                  "haar eigen tijd</strong>, want woorden betekenden in 1850 niet hetzelfde als vandaag. "
                  "<strong>Representativiteit</strong> is <strong>de vraag of ze voor een hele groep "
                  "geldt</strong>: één dagboek vertelt over één mijnwerker."),
            ("p", "Je vermeldt waar je een bron gevonden hebt <strong>zodat anderen je werk kunnen nagaan en "
                  "controleren</strong>. Overnemen zonder vermelden heet <strong>plagiaat</strong>; ook hulp van "
                  "een computerprogramma vermeld je. <strong>Eén enkele bron is niet genoeg</strong> om een "
                  "besluit te onderbouwen."),
        ]),
        dict(kop="Betrouwbaarheid", blokken=[
            ("p", "Om de betrouwbaarheid te beoordelen kijk je naar <strong>wie de auteur is en welk belang "
                  "hij kan hebben</strong> en naar <strong>hoe dicht de bron bij de gebeurtenis staat</strong>, "
                  "en of andere bronnen hetzelfde zeggen. Daarom <strong>vermeldt een historicus altijd de "
                  "datum</strong>: <strong>de afstand tot de gebeurtenis telt mee</strong>. <strong>Een bron "
                  "met een duidelijk belang bij haar verhaal lees je kritischer</strong>, en dat maakt haar "
                  "niet waardeloos."),
            ("p", "Bij elke bron horen vier vragen: <strong>wie heeft ze gemaakt, en wanneer</strong>, en "
                  "<strong>voor wie was ze bedoeld, en met welk doel</strong>. Is de auteur onbekend, dan "
                  "<strong>gebruik je ze voorzichtig en toets je ze</strong> aan andere bronnen, en zeg je wat "
                  "je niet weet."),
            ("p", "<strong>Standplaatsgebondenheid</strong> betekent dat <strong>iemand naar de wereld kijkt "
                  "van waar hij zelf staat</strong>: afkomst, tijd, geloof en belang bepalen mee wat hij ziet. "
                  "<strong>Ook een historicus van vandaag is standplaatsgebonden</strong>; daarom legt hij zijn "
                  "werkwijze open."),
            ("p", "Een <strong>feit is te controleren, een mening is een standpunt</strong>, en <strong>die "
                  "twee staan vaak in dezelfde zin</strong>. Een <strong>waardeoordeel</strong> is <strong>een "
                  "uitspraak die iets goed of slecht noemt</strong>. Spreken twee bronnen elkaar tegen, dan "
                  "<strong>zoek je uit wie welk belang had</strong> en zoek je bronnen bij: een tegenspraak is "
                  "een aanwijzing dat er iets uit te leggen valt."),
            ("p", "Een getuigenis van vijftig jaar later is over details minder betrouwbaar, want <strong>het "
                  "geheugen verandert met de tijd</strong> en met wat men later hoorde; <strong>over de "
                  "beleving blijft ze juist waardevol</strong>. Memoires van een generaal over zijn eigen "
                  "veldslag lees je met de wetenschap dat <strong>hij belang heeft bij zijn eigen rol</strong>."),
        ]),
        dict(kop="Bronnen op het internet", blokken=[
            ("p", "Om na te gaan of een website betrouwbaar is, <strong>kijk je wie erachter zit en van "
                  "wanneer ze is</strong>. <strong>Bovenaan de zoekresultaten staan zegt niets over "
                  "juistheid</strong>: dat gaat over techniek en geld. Bij een opvallend bericht op sociale "
                  "media <strong>zoek je of onafhankelijke bronnen hetzelfde melden</strong>."),
            ("p", "Een beeld is vandaag <strong>geen bewijs op zichzelf</strong>, want <strong>beelden kunnen "
                  "bewerkt of volledig gemaakt worden</strong>. Ook vroeger werden foto's geretoucheerd en in "
                  "scène gezet; de techniek maakt het nu veel eenvoudiger."),
            ("p", "Heb je een affiche, een dagboek en een studie over dezelfde staking, dan <strong>leg je ze "
                  "naast elkaar en vergelijk je ze</strong>: elk zegt iets anders, de bedoeling, de beleving en "
                  "het overzicht. Dit alles is niet enkel voor de les nuttig: <strong>dezelfde vragen helpen je "
                  "bij nieuws en bij sociale media</strong>."),
        ]),
        dict(kop="Nog vier vaste vragen", blokken=[
            ("p", "<strong>Plagiaat</strong> is <strong>het overnemen van het werk van iemand anders zonder "
                  "dat te vermelden</strong>; het werkwoord is <strong>plagiëren</strong>. Een bronvermelding "
                  "kost een regel en lost het probleem op."),
            ("p", "<strong>Waarom een gecensureerde krant uit 1942 toch een waardevolle bron is: ze toont "
                  "wat de bezetter wilde laten lezen.</strong> Voor de feiten is ze onbruikbaar, voor de "
                  "bedoelingen van de bezetter is ze uitstekend."),
            ("p", "<strong>Waarnaar je kijkt om de betrouwbaarheid van een bron te beoordelen: wie de auteur "
                  "is en welk belang hij kan hebben</strong>, en <strong>hoe dicht de bron bij de "
                  "gebeurtenis staat</strong>. <strong>Wat je doet als twee bronnen elkaar tegenspreken: je "
                  "zoekt uit wie welk belang had</strong>, en je zoekt bronnen bij. <strong>Wat je doet met "
                  "een opvallend bericht dat je op sociale media tegenkomt: je zoekt of onafhankelijke "
                  "bronnen hetzelfde melden.</strong>"),
            ("p", "<strong>Standplaatsgebondenheid</strong> is <strong>het verschijnsel dat iemand de wereld "
                  "bekijkt van de plaats waar hij zelf staat</strong>. <strong>Een historicus heeft zelf ook "
                  "een standplaats die zijn werk beïnvloedt</strong>, en daarom legt hij zijn werkwijze en "
                  "zijn bronnen open."),
        ]),
    ],
    onthoud=[
        "Primair = uit de tijd zelf, secundair = later. Primair is niet automatisch betrouwbaarder.",
        "Bruikbaarheid hangt af van je vraag: thema, tijd en plaats moeten kloppen.",
        "Betrouwbaarheid: wie, wanneer, voor wie, met welk doel, en wat zeggen andere bronnen?",
        "Standplaatsgebondenheid geldt ook voor de historicus; scheid feit, mening en waardeoordeel.",
        "Online: wie staat erachter, van wanneer is het, wie bevestigt het? Een beeld is geen bewijs.",
    ],
)

BUNDELS["beeldvorming-standplaatsgebondenheid-en-betekenisgeving-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Beeldvorming, standplaatsgebondenheid en betekenisgeving",
    onder="Hoe een beeld van het verleden ontstaat, en wat een samenleving ermee doet.",
    secties=[
        dict(kop="Beeldvorming", blokken=[
            ("p", "<strong>Beeldvorming</strong> over het verleden is <strong>het beeld dat mensen van een tijd "
                  "of een groep hebben</strong>. Dat beeld wordt gevormd <strong>door handboeken, films en "
                  "reeksen</strong> en <strong>door verhalen in je gezin en je omgeving</strong>, niet enkel "
                  "door onderzoek. Wie zich dat niet bewust is, houdt zijn eigen beeld voor de geschiedenis "
                  "zelf."),
            ("p", "De blik van een mens is <strong>standplaatsgebonden</strong>: <strong>zijn tijd, zijn "
                  "afkomst, zijn geloof en zijn belang</strong> bepalen mee wat hij ziet. Daarom beschrijven "
                  "twee ooggetuigen dezelfde gebeurtenis anders: <strong>elk van hen stond elders en had een "
                  "ander belang</strong>. <strong>Twee eerlijke getuigen kunnen dus verschillen</strong> zonder "
                  "dat een van beide liegt. <strong>Ook een historicus van vandaag is standplaatsgebonden.</strong>"),
            ("p", "<strong>Multiperspectiviteit</strong> is <strong>het bekijken van een gebeurtenis vanuit "
                  "verschillende standpunten</strong>: een staking door de ogen van de arbeider, de fabrikant "
                  "en de burgemeester. <strong>Eurocentrisme</strong> is <strong>Europa als maatstaf voor het "
                  "hele verhaal nemen</strong>, waardoor de dekolonisatie het verhaal wordt van Europa dat "
                  "weggaat in plaats van volken die zichzelf bevrijden."),
            ("p", "Een <strong>stereotype</strong> is <strong>een vast, vereenvoudigd beeld van een hele "
                  "groep</strong>; komt er een waardeoordeel bij, dan spreekt men van een vooroordeel. "
                  "<strong>Beelden van groepen mensen kunnen stereotypen versterken</strong>, en <strong>wie "
                  "beelden maakt, kiest wat je te zien krijgt</strong>."),
            ("p", "<strong>Historische empathie</strong> betekent dat <strong>je probeert te begrijpen waarom "
                  "mensen toen zo handelden</strong> en <strong>hun keuzes in de kennis en de normen van hun "
                  "tijd plaatst</strong>. <strong>Begrijpen is niet goedkeuren</strong>: je kan iets verklaren "
                  "en het tegelijk scherp afkeuren."),
            ("p", "Het beeld van een periode verandert, want <strong>nieuwe vragen en nieuwe bronnen leveren "
                  "een ander beeld</strong>; <strong>het verleden zelf verandert niet</strong>. Over het "
                  "koloniale verleden wordt vandaag anders geschreven dan vijftig jaar geleden. "
                  "<strong>Een handboek maakt keuzes over wat er in en uit gaat</strong> en <strong>is "
                  "geschreven in een bepaalde tijd met bepaalde vragen</strong>: <strong>volledig en neutraal "
                  "is het dus niet</strong>. Een Belgisch en een Congolees handboek over 1960 geven "
                  "<strong>dezelfde feiten met een andere nadruk</strong> en andere hoofdrollen. Een film over "
                  "de Tweede Wereldoorlog uit 1960 is vooral een bron <strong>voor de manier waarop men in "
                  "1960 naar die oorlog keek</strong>."),
        ]),
        dict(kop="Betekenisgeving", blokken=[
            ("p", "<strong>Betekenisgeving</strong> is <strong>de waarde die een samenleving aan haar verleden "
                  "toekent</strong>. Je ziet ze <strong>aan haar feestdagen en herdenkingen</strong> en "
                  "<strong>aan haar standbeelden en straatnamen</strong>, en aan het erfgoed dat beschermd "
                  "wordt. <strong>11 november</strong> is in België een feestdag omdat <strong>het de dag van "
                  "de wapenstilstand van 1918</strong> is."),
            ("p", "Het verschil tussen <strong>geschiedenis en herinnering</strong>: <strong>geschiedenis "
                  "onderzoekt, herinnering wordt beleefd</strong>. Een herdenking is geen onderzoek, maar "
                  "herinnering is zelf een onderwerp voor onderzoek. <strong>Een herdenking kiest wie en wat "
                  "herdacht wordt</strong>, en <strong>wat een land herdenkt, kan in de tijd veranderen</strong>: "
                  "de slachtoffers van de kolonisatie komen pas sinds kort in de Belgische herdenkingen voor."),
            ("p", "<strong>Erfgoed</strong> is <strong>wat uit het verleden bewaard en doorgegeven wordt</strong>: "
                  "gebouwen, voorwerpen, landschappen, maar ook gebruiken en ambachten."),
        ]),
        dict(kop="Omstreden monumenten en misbruik", blokken=[
            ("p", "Sommige standbeelden liggen onder vuur omdat <strong>de persoon nu anders beoordeeld wordt "
                  "dan vroeger</strong>. Mogelijke oplossingen: <strong>een bord met uitleg bij het beeld "
                  "plaatsen</strong> of <strong>het beeld naar een museum verplaatsen</strong>. Zo'n bord is "
                  "<strong>een poging om het beeld in zijn context te plaatsen</strong>. <strong>Een monument "
                  "zegt evenveel over de tijd waarin het geplaatst werd als over wie het eert</strong>, en "
                  "<strong>het debat erover gaat vooral over hoe wij vandaag naar het verleden kijken</strong>."),
            ("p", "De vraag naar <strong>teruggave</strong> uit koloniale musea gaat <strong>over voorwerpen "
                  "die in de koloniale tijd zijn weggehaald</strong>; België heeft daarvoor een wettelijk kader "
                  "gemaakt, en elk stuk vraagt onderzoek naar zijn herkomst."),
            ("p", "<strong>Negationisme</strong> is <strong>het ontkennen van de Holocaust</strong>, en dat is "
                  "<strong>in België bij wet strafbaar</strong> sinds 1995: het is geen mening, maar het "
                  "ontkennen van vastgestelde feiten. Geschiedenis wordt politiek misbruikt <strong>door het "
                  "verleden te vervormen om een eis te onderbouwen</strong>, bijvoorbeeld met een uitgezochte "
                  "gouden eeuw."),
        ]),
        dict(kop="Verleden, heden en toekomst", blokken=[
            ("p", "We studeren geschiedenis <strong>om te begrijpen hoe het heden geworden is wat het is</strong>: "
                  "grenzen, instellingen, ongelijkheden en gevoeligheden van nu hebben een voorgeschiedenis. "
                  "<strong>De gebeurtenissen van de toekomst voorspellen kan geschiedenis niet.</strong>"),
            ("p", "<strong>Continuïteit</strong> is <strong>wat over een lange periode hetzelfde blijft</strong>; "
                  "naast de breuken zie je lijnen die doorlopen. En dit thema staat niet apart: <strong>bronnen, "
                  "standpunten en beeldvorming horen samen</strong> bij elk thema van het vak, van Wenen tot "
                  "Congo."),
        ]),
        dict(kop="De woorden nog even samen", blokken=[
            ("p", "<strong>Multiperspectiviteit</strong>, ook <strong>multiperspectivisme</strong> of werken "
                  "met <strong>meerdere perspectieven</strong>, is <strong>het bekijken van een gebeurtenis "
                  "vanuit verschillende standpunten</strong>. <strong>Eurocentrisme in de geschiedschrijving "
                  "is Europa als maatstaf voor het hele verhaal nemen.</strong> Een "
                  "<strong>stereotype</strong>, bijvoeglijk <strong>stereotiep</strong>, is <strong>een vast "
                  "en vereenvoudigd beeld van een hele groep mensen</strong>."),
            ("p", "<strong>Historische empathie betekent niet dat je het gedrag van mensen uit het verleden "
                  "goedkeurt</strong>, maar dat je probeert te begrijpen waarom ze zo handelden, met de "
                  "kennis en de normen van hun tijd erbij."),
            ("p", "<strong>Waarom het nuttig is te weten wie een geschiedenis geschreven heeft: de auteur "
                  "kiest wat hij vertelt en van welke kant.</strong> <strong>Lees je twee handboeken over de "
                  "onafhankelijkheid van Congo, een Belgisch en een Congolees, dan verwacht je dezelfde "
                  "feiten met een andere nadruk.</strong> <strong>Over beeldvorming in de reclame en de "
                  "media: beelden van groepen mensen kunnen stereotypen versterken</strong>, en <strong>wie "
                  "beelden maakt, kiest wat je te zien krijgt</strong>."),
            ("p", "<strong>Waaraan je ziet hoe een samenleving haar verleden waardeert: aan haar feestdagen "
                  "en herdenkingen</strong>, en <strong>aan haar standbeelden en straatnamen</strong>. "
                  "<strong>Zie je een standbeeld van een koloniale figuur met een nieuw bord met uitleg "
                  "erbij, dan is dat een poging om het beeld in zijn context te plaatsen.</strong> "
                  "<strong>Negationisme</strong> of <strong>holocaustontkenning</strong> is <strong>het "
                  "ontkennen van de Holocaust, dat in België strafbaar is</strong>."),
            ("p", "<strong>Waarom we geschiedenis studeren als het over voorbije tijden gaat: om te "
                  "begrijpen hoe het heden geworden is wat het is.</strong>"),
        ]),
    ],
    onthoud=[
        "Beeldvorming komt uit handboeken, films en verhalen; iedereen kijkt van zijn eigen standplaats.",
        "Multiperspectiviteit, eurocentrisme, stereotype en historische empathie: begrijpen is niet goedkeuren.",
        "Betekenisgeving zie je in feestdagen, monumenten, straatnamen en erfgoed; herinnering is geen onderzoek.",
        "Omstreden monumenten: uitleg of museum; teruggave van koloniale voorwerpen; negationisme is strafbaar sinds 1995.",
        "Geschiedenis verklaart het heden, ze voorspelt de toekomst niet.",
    ],
)
