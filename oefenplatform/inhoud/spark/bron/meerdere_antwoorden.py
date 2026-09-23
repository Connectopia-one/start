# -*- coding: utf-8 -*-
"""Meerkeuzevragen van geschiedenis ✨ Spark met méér dan één juist antwoord.

Kim merkte op 23 september 2026 op dat de examencommissie bij meerkeuze vaak
meerdere juiste antwoorden verwacht, zónder dat erbij staat hoeveel het er
zijn. Duidt een kind er één aan terwijl er twee juist waren, dan is de hele
vraag fout. Wie dat nooit oefent, verliest daar punten.

Daarom vervangt `zet_meerdere_antwoorden.py` ongeveer een kwart van de
meerkeuzevragen van geschiedenis door de vragen hieronder. Ze blijven op
dezelfde plaats in hun hoofdstuk staan en gaan over dezelfde leerstof, zodat
de leerbundel elke vraag blijft dekken.

Per hoofdstuk staat er een lijst van (volgnummer, vraag). Het volgnummer telt
vanaf 1 en verwijst naar de vraag die vervangen wordt.

In `antwoord` staan de nummers van álle juiste opties. Het husselen van de
opties bij het tonen (lib/optievolgorde.ts) verschuift die nummers mee, dus de
juiste antwoorden mogen hier gewoon vooraan staan.
"""

VERVANGINGEN = {
    "Het historisch referentiekader — deel 1": [
        (9, dict(
            vraag="Welke van deze horen bij het politieke domein?",
            opties=["Een koning die wetten uitvaardigt", "Een oorlog tussen twee steden",
                    "Een tempel bouwen voor een god", "Graan verkopen op de markt"],
            antwoord=[0, 1],
            uitleg="Macht, bestuur, wetten en oorlog horen bij het politieke domein. De tempel is cultureel, de handel economisch.")),
        (10, dict(
            vraag="Welke van deze horen bij het culturele domein?",
            opties=["Een beeld maken van een god", "Een nieuwe sterrenkundige berekening",
                    "Belastingen innen", "Een kanaal graven naar de akkers"],
            antwoord=[0, 1],
            uitleg="Religie, kunst, wetenschap en taal zijn cultureel. Belastingen innen is politiek, en het kanaal is economisch.")),
        (13, dict(
            vraag="Welke structuurbegrippen passen bij Athene?",
            opties=["maritiem", "stedelijk", "continentaal", "ruraal"],
            antwoord=[0, 1],
            uitleg="Athene leefde van zijn vloot en van handel over zee, en het was een stad. Sparta was juist continentaal.")),
    ],
    "Het historisch referentiekader — deel 2": [
        (2, dict(
            vraag="Welke gebeurtenissen gebruiken historici als scharnierpunt?",
            opties=["De uitvinding van het schrift", "De val van het West-Romeinse Rijk in 476",
                    "De bouw van de piramides", "De eerste Olympische Spelen"],
            antwoord=[0, 1],
            uitleg="Het schrift sluit de prehistorie af en 476 sluit de klassieke oudheid af. De piramides en de Spelen zijn belangrijk, maar laten geen nieuwe periode beginnen.")),
        (9, dict(
            vraag="Waarom past de westerse indeling in zeven periodes niet op de hele wereld?",
            opties=["Ze is gemaakt vanuit de Europese geschiedenis",
                    "In 476 veranderde er voor China of Amerika niets",
                    "Omdat er buiten Europa geen bronnen bestaan",
                    "Omdat andere werelddelen geen geschiedenis hebben"],
            antwoord=[0, 1],
            uitleg="De eerste twee: de indeling is plaatsgebonden. De andere twee kloppen niet — overal zijn bronnen en overal is geschiedenis.")),
        (11, dict(
            vraag="In welke maatschappelijke domeinen situeer je de verovering van Alexander de Grote?",
            opties=["politiek, want het gaat over macht en gezag",
                    "cultureel, want de Griekse taal en kunst verspreidden zich mee",
                    "economisch, want er kwam handel op gang",
                    "in geen enkel domein, een verovering staat daarbuiten"],
            antwoord=[0, 1, 2],
            uitleg="Alle drie. Eén gebeurtenis hoort vaak in meerdere domeinen tegelijk, en dat is juist het punt van die indeling.")),
    ],
    "De prehistorie — deel 1": [
        (6, dict(
            vraag="Waarvoor gebruikten prehistorische mensen het vuur?",
            opties=["om warmte en licht te geven", "om roofdieren op afstand te houden",
                    "om voedsel beter verteerbaar te maken", "om metaal te smelten"],
            antwoord=[0, 1, 2],
            uitleg="De eerste drie. Metaal bewerken komt pas veel later; in de prehistorie werkte men met steen en hout.")),
        (11, dict(
            vraag="Wat vind je terug op prehistorische grotschilderingen?",
            opties=["paarden, bizons en herten", "handafdrukken", "jachttaferelen",
                    "de namen van de schilders"],
            antwoord=[0, 1, 2],
            uitleg="Dieren, handen en jachtscènes. Namen niet: het schrift bestond nog niet, en daarom heet deze periode de prehistorie.")),
        (12, dict(
            vraag="Wat klopt over jagers en verzamelaars?",
            opties=["Ze leefden in kleine groepen van enkele tientallen mensen",
                    "Ze trokken mee met het voedsel", "Er was een taakverdeling in de groep",
                    "Ze woonden in dorpen met voorraadschuren"],
            antwoord=[0, 1, 2],
            uitleg="De eerste drie. Dorpen en voorraden komen er pas met de landbouw, duizenden jaren later.")),
    ],
    "De prehistorie — deel 2": [
        (2, dict(
            vraag="Wat hoort bij de agrarische revolutie?",
            opties=["zelf gewassen telen", "dieren houden", "op een vaste plaats wonen",
                    "in de winter naar warmere streken trekken"],
            antwoord=[0, 1, 2],
            uitleg="Landbouw en veeteelt, en daardoor een vast woonplaats. Rondtrekken is net wat men daarvóór deed.")),
        (6, dict(
            vraag="Welke gevolgen had het voedseloverschot?",
            opties=["Sommigen konden een ander beroep uitoefenen",
                    "Er konden meer mensen op één plek wonen",
                    "Er ontstonden verschillen in rijkdom", "Iedereen werd even rijk"],
            antwoord=[0, 1, 2],
            uitleg="Overschot geeft specialisatie, steden én ongelijkheid. Gelijkheid juist niet: wie grond en voorraden had, stond sterker.")),
        (10, dict(
            vraag="Welke nadelen bracht het sedentaire leven mee?",
            opties=["Ziektes sprongen makkelijker over", "Eén misoogst kon hongersnood betekenen",
                    "Er ontstond ongelijkheid in bezit", "Men kon geen voedsel meer bewaren"],
            antwoord=[0, 1, 2],
            uitleg="De eerste drie. Bewaren kon juist wél, en net dat bewaarde bezit maakte het verschil tussen arm en rijk.")),
        (14, dict(
            vraag="Welke sporen uit het neolithicum liggen er bij ons nog in het landschap?",
            opties=["hunebedden", "grafheuvels", "piramides", "aquaducten"],
            antwoord=[0, 1],
            uitleg="Grote steenzettingen en grafheuvels. Piramides horen bij Egypte en aquaducten bij de Romeinen.")),
    ],
    "Mesopotamië en Egypte — deel 1": [
        (4, dict(
            vraag="Wat hoort bij irrigatielandbouw?",
            opties=["kanalen graven", "dijken aanleggen en onderhouden",
                    "rivierwater tot bij de akkers brengen", "wachten tot het regent"],
            antwoord=[0, 1, 2],
            uitleg="Irrigatie is water zelf naar je akkers brengen. Net omdat het er te weinig regende, was dat nodig.")),
        (6, dict(
            vraag="Welke van deze waren Mesopotamische stadstaten?",
            opties=["Ur", "Uruk", "Babylon", "Athene"],
            antwoord=[0, 1, 2],
            uitleg="Ur, Uruk en Babylon lagen tussen Tigris en Eufraat. Athene is een Griekse polis, duizenden jaren later.")),
        (13, dict(
            vraag="Wat klopt over een ziggurat?",
            opties=["Het is een tempeltoren in trappen", "Hij stond midden in de stad",
                    "Hij was gewijd aan de god van die stad", "Het is het graf van een koning"],
            antwoord=[0, 1, 2],
            uitleg="Een ziggurat is een tempel, geen graf. Het graf van een heerser is in Egypte de piramide.")),
        (14, dict(
            vraag="Wat hadden Mesopotamië en Egypte gemeen?",
            opties=["Ze lagen allebei aan een rivier", "Ze geloofden in meerdere goden",
                    "Ze waren allebei een standenmaatschappij", "Ze schreven allebei met hiërogliefen"],
            antwoord=[0, 1, 2],
            uitleg="Alleen het schrift verschilde: spijkerschrift in Mesopotamië, hiërogliefen in Egypte.")),
    ],
    "Mesopotamië en Egypte — deel 2": [
        (4, dict(
            vraag="Wat klopt over het schrift in deze rijken?",
            opties=["Het ontstond om voorraden en bezit bij te houden",
                    "Maar weinig mensen konden lezen en schrijven",
                    "Schrijvers stonden daardoor hoog in de standenmaatschappij",
                    "Het ontstond om verhalen te bewaren"],
            antwoord=[0, 1, 2],
            uitleg="De oudste kleitabletten zijn boekhouding, geen literatuur. Die kwam pas later.")),
        (7, dict(
            vraag="Wat deed een ambtenaar in deze rijken?",
            opties=["belastingen innen", "akkers opmeten", "de voorraden bijhouden",
                    "het leger aanvoeren in de strijd"],
            antwoord=[0, 1, 2],
            uitleg="Een ambtenaar bestuurt in naam van de heerser. Het leger leiden was de taak van de heerser zelf.")),
        (10, dict(
            vraag="Waarom kon Mesopotamië niet zonder handel?",
            opties=["Er was nauwelijks hout", "Er was nauwelijks steen", "Er was nauwelijks metaal",
                    "Er was nauwelijks graan"],
            antwoord=[0, 1, 2],
            uitleg="Graan en klei waren er juist in overvloed. Bouwhout, steen en erts moesten van ver komen.")),
        (14, dict(
            vraag="Welke taken had een farao?",
            opties=["besturen en rechtspreken", "het leger leiden", "de goden gunstig stemmen",
                    "zelf bij elke boer de belasting ophalen"],
            antwoord=[0, 1, 2],
            uitleg="Zijn taak was politiek én religieus. Het ophalen van belastingen deden de ambtenaren voor hem.")),
    ],
    "Het oude Griekenland — deel 1": [
        (4, dict(
            vraag="Wat deelden de Griekse stadstaten met elkaar?",
            opties=["dezelfde taal", "dezelfde goden en verhalen", "de Olympische Spelen",
                    "hetzelfde bestuur"],
            antwoord=[0, 1, 2],
            uitleg="Cultureel waren ze één, politiek juist niet: elke polis bestuurde zichzelf.")),
        (12, dict(
            vraag="Wat klopt over de Griekse goden?",
            opties=["Ze woonden volgens de verhalen op de Olympus", "Zeus was de oppergod",
                    "Ze werden jaloers, verliefd en kwaad, net als mensen",
                    "De Grieken geloofden in één god"],
            antwoord=[0, 1, 2],
            uitleg="De Grieken waren polytheïstisch: veel goden, elk met een eigen taak en karakter.")),
        (19, dict(
            vraag="Waar stichtten Griekse kolonisten nieuwe steden?",
            opties=["in Zuid-Italië", "in Zuid-Frankrijk", "rond de Zwarte Zee", "in Britannië"],
            antwoord=[0, 1, 2],
            uitleg="Zo kwamen de Romeinen al vroeg met de Griekse cultuur in aanraking. Britannië is Romeins, en veel later.")),
    ],
    "Het oude Griekenland — deel 2": [
        (4, dict(
            vraag="Wie mocht er in Athene niét meestemmen?",
            opties=["vrouwen", "slaven", "vreemdelingen", "vrije mannen met burgerrecht"],
            antwoord=[0, 1, 2],
            uitleg="Enkel vrije mannelijke burgers stemden, ongeveer één op tien van de bevolking. Dat is meteen de grootste beperking van die democratie.")),
        (7, dict(
            vraag="Wat waren gevolgen van de Perzische oorlogen?",
            opties=["De stadstaten werkten uitzonderlijk samen",
                    "Athene werd de leider van een bondgenootschap",
                    "Athene bouwde met dat geld onder meer het Parthenon",
                    "Sparta werd meteen de baas over heel Griekenland"],
            antwoord=[0, 1, 2],
            uitleg="Sparta won pas veel later, in de Peloponnesische oorlog — en toen kwamen alle stadstaten er verzwakt uit.")),
        (13, dict(
            vraag="Wat mocht een Spartaanse vrouw wél en een Atheense niet?",
            opties=["sporten", "zich vrij bewegen", "bezit hebben", "meestemmen over de wetten"],
            antwoord=[0, 1, 2],
            uitleg="Meebeslissen deed een vrouw op geen van beide plaatsen.")),
        (16, dict(
            vraag="Welke zuilstijlen kenden de Grieken?",
            opties=["Dorisch", "Ionisch", "Korintisch", "Romaans"],
            antwoord=[0, 1, 2],
            uitleg="Je herkent ze aan het kapiteel bovenaan: Dorisch sober, Ionisch met krullen, Korintisch met bladeren. Romaans is een bouwstijl uit de middeleeuwen.")),
    ],
    "Het Romeinse Rijk — deel 1": [
        (9, dict(
            vraag="Wat klopt over de Romeinse republiek?",
            opties=["Er stonden twee consuls aan het hoofd, elk voor één jaar",
                    "De senaat was de raad van oud-bestuurders",
                    "De volksvergadering koos de bestuurders",
                    "Aan het hoofd stond een koning"],
            antwoord=[0, 1, 2],
            uitleg="De koningen kwamen net vóór de republiek. De Romeinen joegen hun laatste koning weg en wilden nooit meer één alleenheerser.")),
        (18, dict(
            vraag="Wat namen de Romeinen over van de Grieken?",
            opties=["de goden, maar met eigen namen: Zeus werd Jupiter", "bouwen met zuilen",
                    "theater en filosofie", "het spijkerschrift"],
            antwoord=[0, 1, 2],
            uitleg="Zeus werd Jupiter, Ares werd Mars en Aphrodite werd Venus. Het spijkerschrift hoort bij Mesopotamië; de Romeinen schreven in het Latijn.")),
        (20, dict(
            vraag="Welke sporen van de Romeinen zie je vandaag nog?",
            opties=["de maandnamen juli en augustus", "onze letters",
                    "duizenden woorden in onze taal", "onze cijfers 0 tot 9"],
            antwoord=[0, 1, 2],
            uitleg="Onze cijfers niet: die komen uit India en kwamen via de Arabische wereld bij ons. De Romeinen schreven I, V, X.")),
    ],
    "Het Romeinse Rijk — deel 2": [
        (5, dict(
            vraag="Wat waren gevolgen van de Punische oorlogen?",
            opties=["Rome werd de baas over de westelijke Middellandse Zee",
                    "Carthago werd uiteindelijk volledig verwoest",
                    "Er kwamen zoveel krijgsgevangenen dat slavenarbeid spotgoedkoop werd",
                    "Rome verloor de macht over Italië"],
            antwoord=[0, 1, 2],
            uitleg="Italië had Rome al vóór die oorlogen in handen. Net door die goedkope slavenarbeid kon de kleine boer niet meer mee.")),
        (12, dict(
            vraag="Wat maakte tijdens de Pax Romana handel over het hele rijk mogelijk?",
            opties=["veilige wegen en zeeën", "één munt", "één rechtssysteem",
                    "een tolmuur rond elke provincie"],
            antwoord=[0, 1, 2],
            uitleg="Goederen konden van Britannië tot Egypte reizen. Tolmuren zouden dat net onmogelijk gemaakt hebben.")),
        (14, dict(
            vraag="Wat klopt over het christendom in het Romeinse Rijk?",
            opties=["Christenen weigerden de keizer te vereren", "Ze werden eerst vervolgd",
                    "Onder Constantijn werd het christendom toegelaten",
                    "Het was vanaf het begin de staatsgodsdienst"],
            antwoord=[0, 1, 2],
            uitleg="Staatsgodsdienst werd het pas op het einde. Daarvóór botste het net op de keizerscultus.")),
        (15, dict(
            vraag="Wat voegden de Romeinen toe aan de Griekse bouwkunst?",
            opties=["de boog", "het gewelf", "de koepel en het beton", "de zuil"],
            antwoord=[0, 1, 2],
            uitleg="De zuil hadden ze net van de Grieken. Met boog, gewelf, koepel en beton konden ze veel grotere ruimtes overspannen.")),
        (17, dict(
            vraag="Wat waren oorzaken van de crisis van de 3de eeuw?",
            opties=["invallen aan de grenzen", "munten met steeds minder zilver",
                    "keizers die elkaar in hoog tempo afzetten", "de verwoesting van Carthago"],
            antwoord=[0, 1, 2],
            uitleg="Carthago was al eeuwen eerder verwoest, in de Punische oorlogen.")),
    ],
    "Bronnen, kunst en beeldvorming — deel 1": [
        (2, dict(
            vraag="Wat kan een historische bron zijn?",
            opties=["een muntje", "een afvalhoop", "kinderspeelgoed",
                    "enkel een geschreven tekst"],
            antwoord=[0, 1, 2],
            uitleg="Alles uit het verleden waaruit je iets kan afleiden, is een bron. Juist een afvalhoop vertelt veel over het gewone leven.")),
        (8, dict(
            vraag="In welke soorten deelt men historische bronnen in naar hun vorm?",
            opties=["geschreven", "mondeling", "materieel", "audiovisueel"],
            antwoord=[0, 1, 2, 3],
            uitleg="Alle vier. Die indeling gaat over de vorm van de bron, niet over haar waarde.")),
        (14, dict(
            vraag="Waarom wil een historicus weten wie een bron gemaakt heeft?",
            opties=["Elke maker vertelt vanuit zijn eigen positie en belang",
                    "Wie de bron betaalde, kan bepalen wat erin komt",
                    "De winnaar beschrijft een slag anders dan de verliezer",
                    "Omdat een bron zonder naam altijd onbruikbaar is"],
            antwoord=[0, 1, 2],
            uitleg="Een bron zonder naam kan nog altijd veel vertellen. De eerste drie zijn juist de reden waarom je altijd naar de maker kijkt.")),
        (19, dict(
            vraag="Wat kan een kunst- of cultuuruiting zijn?",
            opties=["een schilderij", "een gebouw", "een film of een game",
                    "enkel werk dat in een museum hangt"],
            antwoord=[0, 1, 2],
            uitleg="Ook graffiti en wat vandaag gemaakt wordt, is voor latere historici een bron over onze tijd.")),
    ],
    "Bronnen, kunst en beeldvorming — deel 2": [
        (5, dict(
            vraag="Wie of wat is er standplaatsgebonden?",
            opties=["de maker van een bron", "de historicus die ze leest",
                    "jij, als je naar het verleden kijkt",
                    "niemand, als je je best doet om neutraal te zijn"],
            antwoord=[0, 1, 2],
            uitleg="Niemand kijkt van nergens. Je kan je standplaats niet uitschakelen, maar je kan ze wel kennen — en dat is al de halve oplossing.")),
        (11, dict(
            vraag="Welke van deze zijn historische redeneerwijzen?",
            opties=["oorzaak en gevolg benoemen", "meerdere perspectieven hanteren",
                    "continuïteit en verandering benoemen", "afgaan op je gevoel"],
            antwoord=[0, 1, 2],
            uitleg="De vijf redeneerwijzen zijn: oorzaak en gevolg, meerdere perspectieven, continuïteit en verandering, bewijs gebruiken en verbanden leggen. Je gevoel hoort er niet bij.")),
        (17, dict(
            vraag="Wat weten we uit de vondsten over de neanderthalers?",
            opties=["Ze maakten samengestelde werktuigen", "Ze verzorgden zieken en gewonden",
                    "Ze begroeven hun doden", "Ze kenden geen vuur"],
            antwoord=[0, 1, 2],
            uitleg="Vuur en kleding kenden ze wél. Het beeld van de domme, lompe holbewoner is mythevorming.")),
        (19, dict(
            vraag="Waardoor kan het beeld dat historici van het verleden hebben, veranderen?",
            opties=["door nieuwe bronnen", "door nieuwe onderzoekstechnieken zoals DNA-onderzoek",
                    "door nieuwe vragen te stellen", "doordat het verleden zelf verandert"],
            antwoord=[0, 1, 2],
            uitleg="Het verleden ligt vast; geschiedenis is het verhaal erover, en dat kan wél herschreven worden.")),
    ],
}
