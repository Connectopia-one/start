# -*- coding: utf-8 -*-
"""De leerbundels van Frans voor 🌍 Beyond dubbele finaliteit.

    python3 -I maak_alles.py frans

Zestien bundels, één per thema van `inhoud/beyond-dubbele-finaliteit/frans.json`.

Gebaseerd op de twee vakfiches Frans 1 en Frans 2 van de derde graad dubbele
finaliteit, geldig vanaf 1 januari 2027, voor de basisvorming van de dubbele
finaliteit en voor commerciële organisatie. Het niveau is **ERK A2+**, een
trapje onder de B1 van de doorstroomrichtingen.

Wat deze fiche níét vraagt, en hier dus ook niet staat: de **subjonctif**, de
**gérondif**, de **plus-que-parfait**, de **passieve vorm** en de
**literatuurbeleving**.

De bundels van 🚀 Boost dubbele finaliteit liggen hieraan de basis, want die
volgen dezelfde thematische indeling en bijna hetzelfde niveau. Wat deze fiche
er bovenop vraagt, krijgt een eigen sectie: de woordvelden kunst, geschiedenis
en samenleving, de woordvelden wetenschap, techniek en taal, de natuur en het
milieu, en de betrekkelijke bijzin met qui, que, où en dont.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De sleutels eindigen op "-beyond-dubbele-finaliteit". Frans bestaat ook op
🌱 Start, ✨ Spark, 🚀 Boost (doorstroom en DF) en 🌍 Beyond doorstroom, en daar
komen thematitels in voor die hier bijna gelijk klinken.
"""
import copy
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import bundel
import maak_frans_df as bdf

VAK = "Frans"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
NA = "-beyond-dubbele-finaliteit"
OUD = "-boost-dubbele-finaliteit"
tabel = bundel.tabel

BUNDELS = {}


def sectie(sleutel, kop, extra=()):
    """Eén sectie uit een bundel van 🚀 Boost dubbele finaliteit."""
    for s in bdf.BUNDELS[sleutel + OUD]["secties"]:
        if s["kop"] == kop:
            s = copy.deepcopy(s)
            s["blokken"] = list(s["blokken"]) + list(extra)
            return s
    raise KeyError(f"{sleutel}: {kop}")


def secties(sleutel, weglaten=()):
    uit = [copy.deepcopy(s) for s in bdf.BUNDELS[sleutel + OUD]["secties"]
           if s["kop"] not in weglaten]
    assert len(uit) + len(weglaten) == len(bdf.BUNDELS[sleutel + OUD]["secties"]), sleutel
    return uit


def zet(sleutel, titel, onder, secties_):
    BUNDELS[sleutel + NA] = dict(vak=VAK, niveau=DF, titel=titel,
                                 onder=onder, secties=secties_)


# ───────────────────── 1. Een Franse tekst lezen
zet("een-franse-tekst-lezen",
    "Een Franse tekst lezen",
    "De vier vragen bij elke tekst, teksten uit het dagelijkse leven, en gericht informatie opzoeken.",
    secties("een-franse-tekst-begrijpen"))


# ───────────────────── 2. Tekstsoorten en de bedoeling van een tekst
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    "Tekstsoorten en de bedoeling van een tekst",
    "Welke soort tekst je voor je hebt, de signaalwoorden en de verwijswoorden, en een onbekend woord "
    "raden in plaats van opzoeken.",
    secties("tekstsoorten-tekstverbanden-en-leesstrategieen"))


# ───────────────────── 3. De Franstalige wereld: gewoontes en reizen
zet("de-franstalige-wereld-gewoontes-en-reizen",
    "De Franstalige wereld: gewoontes en reizen",
    "Begroeten, tu of vous, waar Frans gesproken wordt, en de woorden die je op reis nodig hebt.",
    secties("de-franstalige-wereld-omgangsvormen-en-gewoontes")
    + [sectie("woordvelden-tijd-weer-reizen-en-vervoer", "Reizen en vervoer"),
       sectie("woordvelden-tijd-weer-reizen-en-vervoer", "Landen en nationaliteiten")])


# ───────────────────── 4. Schrijven en spreken in het Frans
zet("schrijven-en-spreken-in-het-frans",
    "Schrijven en spreken in het Frans",
    "Wat je moet kunnen schrijven, waarop je beoordeeld wordt, en hoe je een gesprek begint en gaande "
    "houdt.",
    secties("schrijven-schriftelijke-interactie-en-leesbeleving",
            weglaten=("Je leesbeleving in het Frans verwoorden",))
    + secties("spreken-gesprekken-klank-en-spelling", weglaten=("Zo ziet je examen eruit",)))


# ───────────────────── 5. Woordvelden: dagelijks leven, eten en wonen
zet("woordvelden-dagelijks-leven-eten-en-wonen",
    "Woordvelden: dagelijks leven, eten en wonen",
    "Eten en drinken, hoeveelheden en de kassa, kleding, de woning en een dag thuis.",
    secties("woordvelden-eten-kleding-wonen-en-winkelen")
    + [sectie("woordvelden-mens-familie-gevoelens-en-gezondheid",
              "De familie en je persoonlijke gegevens")])


# ───────────────────── 6. Woordvelden: gezondheid, natuur en milieu
zet("woordvelden-gezondheid-natuur-en-milieu",
    "Woordvelden: gezondheid, natuur en milieu",
    "Het lichaam en de gezondheid, hoe je je voelt, en de woorden voor de natuur, het weer en het "
    "milieu.",
    [
        sectie("woordvelden-mens-familie-gevoelens-en-gezondheid", "Het lichaam en de gezondheid"),
        sectie("woordvelden-mens-familie-gevoelens-en-gezondheid", "Gevoelens"),
        sectie("woordvelden-tijd-weer-reizen-en-vervoer", "Het weer"),
        sectie("woordvelden-mens-familie-gevoelens-en-gezondheid",
               "Instructietaal: de opdracht zelf begrijpen"),
    ])


# ───────────────────── 7. Woordvelden: school, werk, geld en verkeer
zet("woordvelden-school-werk-geld-en-verkeer",
    "Woordvelden: school, werk, geld en verkeer",
    "Op school, de beroepen, stage en solliciteren, betalen, en het verkeer.",
    secties("woordvelden-school-werk-en-de-professionele-wereld")
    + [sectie("woordvelden-eten-kleding-wonen-en-winkelen", "Hoeveelheden, maten en de kassa")])


# ───────────────────── 10. Lidwoorden, aanwijzers, bezitters en getallen
zet("lidwoorden-aanwijzers-bezitters-en-getallen",
    "Lidwoorden, aanwijzers, bezitters en getallen",
    "Mannelijk of vrouwelijk, bepaald of onbepaald, du en de la, ce en mon, en de telwoorden.",
    secties("zelfstandige-naamwoorden-lidwoorden-en-determinanten"))


# ───────────────────── 13. De tegenwoordige tijd en de gebiedende wijs
zet("de-tegenwoordige-tijd-en-de-gebiedende-wijs",
    "De tegenwoordige tijd en de gebiedende wijs",
    "De présent van de drie groepen en van de onregelmatige werkwoorden, de impératif, en de "
    "wederkerende werkwoorden.",
    secties("present-imperatif-en-de-wederkerende-werkwoorden"))


# ───────────────────── 14. De verleden tijden
zet("de-verleden-tijden",
    "De verleden tijden",
    "De passé composé met avoir en met être, de imparfait, en wanneer je welke van de twee neemt.",
    secties("passe-compose-imparfait-en-passe-recent"))


# ───────────────────── 15. De toekomende tijd en de conditionnel
zet("de-toekomende-tijd-en-de-conditionnel",
    "De toekomende tijd en de conditionnel",
    "De futur proche en de futur simple, welke van de twee je neemt, en de conditionnel om hoffelijk "
    "te vragen.",
    secties("futur-proche-futur-simple-en-de-conditionnel-de-politesse"))


# ───────────────────── 16. Zinsbouw, zinsdelen en congruentie
zet("zinsbouw-zinsdelen-en-congruentie",
    "Zinsbouw, zinsdelen en congruentie",
    "De soorten zinnen, de drie manieren om een vraag te stellen, de ontkenning in twee delen, de "
    "voegwoorden en de overeenkomst.",
    secties("zinsbouw-zinsdelen-voegwoorden-en-de-overeenkomst"))


# ───────────────────── 8. Woordvelden: kunst, geschiedenis en de samenleving
zet("woordvelden-kunst-geschiedenis-en-de-samenleving",
    "Woordvelden: kunst, geschiedenis en de samenleving",
    "Het boek en het theater, de woorden van de geschiedenis, de politiek, de samenleving en het recht.",
    [
        dict(kop="Het boek en het museum", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>un roman</strong>", "een <strong>roman</strong>; een Romein is <em>un Romain</em>"],
                ["<strong>un auteur</strong>", "de <strong>schrijver</strong> van een boek"],
                ["<strong>un chapitre</strong>", "een <strong>hoofdstuk</strong>"],
                ["<strong>la fiction</strong>", "de <strong>verzonnen verhalen</strong>; waargebeurd is <em>la non-fiction</em>"],
                ["<strong>une biographie</strong>", "het verhaal van <strong>iemands leven</strong>"],
                ["<strong>une intrigue</strong>", "de <strong>verhaallijn</strong> van een verhaal"],
                ["<strong>une rime</strong>", "een <strong>rijm</strong>; het ritme in de muziek is <em>le rythme</em>"],
            ])),
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>un tableau</strong>", "een <strong>schilderij</strong> (en op school ook het bord)"],
                ["<strong>une sculpture</strong>, <strong>une statue</strong>", "een <strong>beeldhouwwerk</strong>"],
                ["<strong>un chef-d'œuvre</strong>", "een <strong>meesterwerk</strong>"],
                ["<strong>une exposition</strong>", "een tentoonstelling"],
                ["<strong>une salle</strong>", "een zaal"],
                ["<strong>le prix d'entrée</strong>", "het inkomgeld"],
            ])),
            ("p", "<em>Un arbitre</em> hoort hier niet bij: dat is de scheidsrechter, en die staat op "
                  "een sportveld."),
        ]),
        dict(kop="Het theater", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>la scène</strong>", "het <strong>podium</strong> (en ook een scène uit een stuk)"],
                ["<strong>le public</strong>", "het <strong>publiek</strong>, de zaal"],
                ["<strong>une pièce</strong>", "een <strong>toneelstuk</strong> (en ook een kamer of een muntstuk)"],
                ["<strong>répéter</strong>", "<strong>repeteren</strong>, dus oefenen vóór de voorstelling (en ook herhalen)"],
                ["<strong>un chef d'orchestre</strong>", "een <strong>dirigent</strong>; een componist is <em>un compositeur</em>"],
            ])),
            ("p", "<em>Une bouilloire</em> is een waterkoker en hoort in de keuken."),
        ]),
        dict(kop="Geschiedenis", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>un siècle</strong>", "een <strong>eeuw</strong>"],
                ["<strong>ancien</strong>", "<strong>vroeger of oud</strong>: <em>un ancien élève</em> is een oud-leerling"],
                ["<strong>un empire</strong>", "een <strong>rijk</strong>"],
                ["<strong>un héritier</strong>", "een <strong>erfgenaam</strong>"],
                ["<strong>une guerre</strong>", "een oorlog"],
                ["<strong>un traité</strong>", "een verdrag"],
                ["<strong>une révolution</strong>", "een omwenteling"],
            ])),
            ("p", "<em>Une soucoupe</em> is het schoteltje onder je kopje, en hoort dus niet bij de "
                  "geschiedenis."),
        ]),
        dict(kop="Politiek en bestuur", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>une élection</strong>", "een <strong>verkiezing</strong>"],
                ["<strong>un parti</strong>", "een partij"],
                ["<strong>un ministre</strong>", "een minister"],
                ["<strong>le parlement</strong>", "het parlement"],
                ["<strong>le premier ministre</strong>", "de <strong>regeringsleider</strong>, ook in België"],
                ["<strong>une loi</strong>", "een <strong>wet</strong>"],
                ["<strong>un citoyen</strong>", "een <strong>burger</strong> van een land"],
                ["<strong>manifester</strong>", "<strong>betogen</strong>"],
                ["<strong>le conseil communal</strong>", "de <strong>gemeenteraad</strong>"],
                ["<strong>un sondage</strong>", "een <strong>opiniepeiling</strong>"],
            ])),
            ("p", "<em>Une affaire</em> is een zaak of een koopje, geen woord uit de politiek in de "
                  "enge zin."),
        ]),
        dict(kop="De samenleving en het recht", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>la pauvreté</strong>", "de armoede"],
                ["<strong>l'égalité</strong>", "de gelijkheid"],
                ["<strong>la solidarité</strong>", "de solidariteit"],
                ["<strong>la discrimination</strong>", "<strong>ongelijke behandeling</strong>"],
                ["<strong>une majorité</strong>", "een <strong>meerderheid</strong>; een minderheid is <em>une minorité</em>"],
                ["<strong>un réfugié</strong>", "een <strong>vluchteling</strong>"],
                ["<strong>un impôt</strong>, les impôts", "een <strong>belasting</strong>"],
                ["<strong>une association caritative</strong>", "een <strong>goed doel</strong>"],
                ["<strong>faire du bénévolat</strong>", "<strong>vrijwillig helpen</strong>"],
                ["<strong>un syndicat</strong>", "een <strong>vakbond</strong>; een handelsbeurs is <em>un salon</em>"],
                ["<strong>les médias</strong>", "<strong>de pers en de omroepen</strong>"],
                ["<strong>les droits de l'homme</strong>", "de <strong>mensenrechten</strong>"],
                ["<strong>le contrôle à la frontière</strong>", "de <strong>grenscontrole</strong>"],
            ])),
            ("p", "Bij het <strong>recht</strong> horen <strong>un juge</strong> (een rechter), "
                  "<strong>un tribunal</strong> (een rechtbank) en <strong>un avocat</strong> (een "
                  "advocaat). <em>Un propriétaire</em> is een eigenaar of een huisbaas, en hoort bij "
                  "het wonen. <em>Un ticket</em> is een kaartje of een kasticket."),
        ]),
    ])


# ───────────────────── 9. Woordvelden: wetenschap, techniek en taal
zet("woordvelden-wetenschap-techniek-en-taal",
    "Woordvelden: wetenschap, techniek en taal",
    "De computer, het labo, sport en vrije tijd, en hoe het Frans zelf in elkaar zit: voorvoegsels, "
    "valse vrienden en het Frans van België en Québec.",
    [
        dict(kop="De computer en het internet", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>un ordinateur</strong>", "een <strong>computer</strong>"],
                ["<strong>l'écran</strong>", "het <strong>scherm</strong>"],
                ["<strong>un écran tactile</strong>", "een <strong>aanraakscherm</strong>"],
                ["<strong>la souris</strong>", "de <strong>muis</strong>"],
                ["<strong>le clavier</strong>", "het <strong>toetsenbord</strong>"],
                ["<strong>un mot de passe</strong>", "een <strong>wachtwoord</strong>"],
                ["<strong>un logiciel</strong>", "een <strong>programma</strong> op een computer"],
                ["<strong>télécharger</strong>", "<strong>downloaden</strong>"],
                ["<strong>enregistrer</strong>, <strong>sauvegarder</strong>", "<strong>opslaan</strong>: <em>enregistrer le fichier</em>"],
                ["<strong>un réseau social</strong>", "een <strong>sociaal netwerk</strong>"],
                ["<strong>une panne</strong>", "een <strong>defect</strong>, een storing"],
            ])),
            ("p", "<em>Le fauteuil</em> is een zetel en hoort in de woonkamer, niet bij de computer."),
        ]),
        dict(kop="Onderzoek en het labo", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>une recherche</strong>", "een <strong>onderzoek</strong>"],
                ["<strong>une invention</strong>", "een <strong>uitvinding</strong>"],
                ["<strong>une expérience</strong>", "een proef (en ook een ervaring)"],
                ["<strong>un résultat</strong>", "een resultaat"],
                ["<strong>une mesure</strong>", "een meting"],
                ["<strong>une pile</strong>", "een <strong>batterij</strong> (en ook een stapel)"],
                ["<strong>la durabilité</strong>", "de <strong>duurzaamheid</strong>"],
            ])),
            ("p", "<em>Un abonnement</em> is een abonnement en hoort niet in het labo."),
        ]),
        dict(kop="Sport en vrije tijd", blokken=[
            ("p", tabel(["Frans", "Nederlands"], [
                ["<strong>un terrain</strong>", "een <strong>veld</strong>, een terrein"],
                ["<strong>une équipe</strong>", "een <strong>ploeg</strong>; de uitrusting is <em>l'équipement</em>"],
                ["<strong>un arbitre</strong>", "een <strong>scheidsrechter</strong>; de doelman is <em>le gardien de but</em>"],
                ["<strong>s'entraîner</strong>", "<strong>trainen</strong>"],
                ["<strong>faire du vélo</strong>", "<strong>fietsen</strong>"],
                ["<strong>un loisir</strong>", "een vrijetijdsbesteding"],
                ["<strong>une randonnée</strong>", "een tocht of wandeling"],
                ["<strong>un spectacle</strong>", "een voorstelling"],
            ])),
            ("p", "<em>Un bulletin</em> is een rapport of een bulletin, en hoort bij school of bij het "
                  "nieuws."),
        ]),
        dict(kop="Een woord uit elkaar halen", blokken=[
            ("p", tabel(["Deel", "Wat het doet", "Voorbeeld"], [
                ["<strong>im-</strong>, in-, mal-", "maakt het <strong>tegengestelde</strong>",
                 "possible → <strong>impossible</strong>, utile → inutile"],
                ["<strong>re-</strong>", "<strong>opnieuw</strong>",
                 "faire → <strong>refaire</strong> (opnieuw doen), lire → relire"],
                ["<strong>-eur</strong>", "de naam van <strong>iemand die iets doet</strong>",
                 "chanter → un chanteur, vendre → un vendeur"],
                ["<strong>-ette</strong>", "maakt iets <strong>kleiner</strong>, niet groter",
                 "une maison → une maisonnette, une fille → une fillette"],
                ["<strong>-tion</strong>", "maakt een naamwoord van een werkwoord",
                 "<strong>construire</strong> → <strong>la construction</strong>"],
            ])),
            ("kader", "Zie je een lang woord dat je niet kent, zoek dan eerst het "
                      "<strong>stamwoord</strong> in het midden. In <em>incompréhensible</em> zit "
                      "<em>comprendre</em>: dus iets wat je niet kan begrijpen."),
        ]),
        dict(kop="Valse vrienden en spreektaal", blokken=[
            ("p", "Een <strong>faux ami</strong> of <strong>valse vriend</strong> lijkt op een "
                  "Nederlands woord maar betekent iets anders. Dit zijn de vier die het vaakst "
                  "terugkomen."),
            ("p", tabel(["Frans woord", "Betekent", "Niet"], [
                ["<strong>la journée</strong>", "de <strong>dag</strong>, de hele dag door", "een journaal of een dagboek"],
                ["<strong>actuellement</strong>", "<strong>momenteel, op dit ogenblik</strong>", "eigenlijk (dat is <em>en fait</em>)"],
                ["<strong>une pile</strong>", "een <strong>batterij</strong> of een stapel", "een pil (dat is <em>une pilule</em>)"],
                ["<strong>la location</strong>", "de <strong>huur</strong>", "de locatie (dat is <em>le lieu</em> of <em>l'endroit</em>)"],
                ["<strong>le pot</strong>", "de <strong>pot</strong>, en in spreektaal het <strong>drankje</strong> (<em>prendre un pot</em>)", "een poot"],
            ])),
            ("p", "<em>La table</em>, <em>le train</em>, <em>le bus</em> en <em>le téléphone</em> zijn "
                  "geen valse vrienden: die betekenen gewoon wat je denkt."),
            ("p", "Het <strong>registre</strong> van een tekst is <strong>de toon en de "
                  "woordkeuze</strong>: formeel, neutraal of <strong>familier</strong>, dus spreektaal. "
                  "<strong>Un bouquin</strong> is spreektaal voor een boek; <em>un livre</em> is "
                  "neutraal, <em>un ouvrage</em> en <em>un manuel</em> zijn boekentaal."),
        ]),
        dict(kop="Het Frans van België en van Québec", blokken=[
            ("p", tabel(["Bij ons of in Québec", "In Frankrijk", "Betekenis"], [
                ["<strong>septante</strong> (BE)", "soixante-dix", "zeventig"],
                ["<strong>nonante</strong> (BE)", "quatre-vingt-dix", "negentig"],
                ["<strong>une drache</strong> (BE)", "une grosse averse", "een stortregen"],
                ["<strong>le dîner</strong> (BE)", "le déjeuner", "het <strong>middagmaal</strong>"],
                ["<strong>la fin de semaine</strong> (Québec)", "<strong>le week-end</strong>", "het weekend"],
            ])),
            ("p", "<em>Une baguette</em> is geen Belgisch Frans: dat stokbrood heet overal zo."),
        ]),
        dict(kop="Woorden over woorden", blokken=[
            ("p", tabel(["Frans", "Wat het is"], [
                ["<strong>un synonyme</strong>", "een woord met <strong>bijna dezelfde betekenis</strong>"],
                ["<strong>un antonyme</strong>", "een woord met de tegengestelde betekenis"],
                ["<strong>des homophones</strong>", "woorden die <strong>hetzelfde klinken maar anders geschreven</strong> worden"],
                ["<strong>emprunter un mot</strong>", "een woord <strong>overnemen</strong> uit een andere taal"],
            ])),
            ("p", "Het Frans zit vol homofonen, en daar gaan de meeste schrijffouten over: "
                  "<em>ou</em> en <em>où</em>, <em>a</em> en <em>à</em>, <em>son</em> en <em>sont</em>, "
                  "<em>et</em> en <em>est</em>, <em>mer</em>, <em>mère</em> en <em>maire</em>."),
            ("kader", "<strong>Ou betekent of, où betekent waar.</strong> Dat accent is geen versiering: "
                      "<em>le café ou le thé</em> is een keuze, <em>où est le café</em> is een vraag naar "
                      "de plaats. Accenten op de e hoor je ook: <strong>élève</strong>, "
                      "<strong>père</strong>, <strong>été</strong>. In <em>table</em> staat er geen, "
                      "want die e klinkt anders."),
        ]),
    ])


# ───────────────────── 11. Voornaamwoorden en betrekkelijke bijzinnen
BEKLEMTOOND = dict(kop="De beklemtoonde vormen", blokken=[
    ("p", "Naast <em>je, me, le, lui</em> heeft het Frans een reeks vormen die <strong>alleen "
          "kunnen staan</strong>, na een voorzetsel of om iets te beklemtonen."),
    ("p", bundel.tabel(["Onderwerp", "Beklemtoond", "Voorbeeld"], [
        ["je", "<strong>moi</strong>", "<em>chez moi</em>, <em>Moi, je pense que oui.</em>"],
        ["tu", "<strong>toi</strong>", "<em>avec toi</em>"],
        ["il / elle", "<strong>lui</strong> / <strong>elle</strong>", "<em>plus grand que lui</em>"],
        ["nous / vous", "<strong>nous</strong> / <strong>vous</strong>", "<em>sans nous</em>"],
        ["ils / elles", "<strong>eux</strong> / <strong>elles</strong>", "<em>avec eux</em>"],
    ])),
    ("p", "Maar het is nooit het onderwerp van het werkwoord: <em>Moi parle français</em> bestaat "
          "niet, dat is <em>Moi, je parle français</em>."),
    ("kader", "<strong>In een bevel schuift het voornaamwoord naar achter, en wordt het "
              "beklemtoond.</strong> <em>Tu me donnes le livre</em> wordt in de gebiedende wijs "
              "<em>Donne-<strong>moi</strong> le livre</em>, met een streepje en met <em>moi</em> in "
              "plaats van <em>me</em>. Zo ook <em>Dis-moi</em>, <em>Attends-moi</em>, "
              "<em>Lève-toi</em>."),
])

ONBEPAALD = dict(kop="On, chacun en personne", blokken=[
    ("p", bundel.tabel(["Frans", "Betekenis", "Let op"], [
        ["<strong>on</strong>", "men, we, je (algemeen)",
         "staat bij een vorm in het <strong>enkelvoud</strong>: <em>on va</em>, nooit <em>on vont</em>"],
        ["<strong>chacun</strong>, chacune", "<strong>elk, ieder</strong> afzonderlijk",
         "<em>chacun son tour</em>"],
        ["<strong>quelqu'un</strong>", "iemand", "<em>quelqu'un a téléphoné</em>"],
        ["<strong>personne</strong>", "<strong>niemand</strong>",
         "met <em>ne</em> erbij: <em>je ne vois <strong>personne</strong></em>"],
        ["<strong>rien</strong>", "niets", "ook met <em>ne</em>: <em>je ne dis rien</em>"],
        ["<strong>tout le monde</strong>", "iedereen", "ook enkelvoud: <em>tout le monde est là</em>"],
    ])),
    ("p", "<em>Personne</em> zonder <em>ne</em> betekent gewoon <strong>een persoon</strong>: "
          "<em>une personne gentille</em>. Het is het woordje <em>ne</em> dat er niemand van maakt."),
])

BETREKKELIJK = dict(kop="De betrekkelijke bijzin", blokken=[
    ("p", "Een <strong>betrekkelijke bijzin</strong> hangt aan een woord uit de hoofdzin en zegt er "
          "iets meer over. Welk woordje je nodig hebt, hangt af van de <strong>rol</strong> die het "
          "in die bijzin speelt."),
    ("p", bundel.tabel(["Woord", "Rol in de bijzin", "Voorbeeld"], [
        ["<strong>qui</strong>", "het <strong>onderwerp</strong> van de bijzin",
         "<em>la fille <strong>qui</strong> chante</em>"],
        ["<strong>que</strong>", "het <strong>lijdend voorwerp</strong> van de bijzin",
         "<em>le film <strong>que</strong> j'ai vu</em>"],
        ["<strong>où</strong>", "een <strong>plaats</strong> of een <strong>tijd</strong>",
         "<em>la ville <strong>où</strong> je suis né</em>"],
        ["<strong>dont</strong>", "wat bij een werkwoord met <em>de</em> hoort",
         "<em>le livre <strong>dont</strong> je parle</em> (parler <strong>de</strong>)"],
        ["<strong>à qui</strong>", "een <strong>persoon</strong> na een voorzetsel",
         "<em>l'amie <strong>à qui</strong> j'écris</em>"],
    ])),
    ("p", "<strong>Que</strong> wordt <em>qu'</em> voor een klinker: <em>le film qu'il a vu</em>. "
          "<strong>Qui</strong> doet dat nooit: het blijft <em>qui</em>, ook voor een klinker "
          "(<em>la fille qui arrive</em>)."),
    ("p", "Is er geen woord om aan te hangen, dan zet je er <strong>ce</strong> voor: <em>je ne sais "
          "pas <strong>ce qui</strong> se passe</em> (wat er gebeurt, onderwerp), <em>je ne comprends "
          "pas <strong>ce que</strong> tu dis</em> (wat je zegt, lijdend voorwerp)."),
    ("kader", "<strong>Kijk wat er na het woordje komt.</strong> Volgt er meteen een vervoegd "
              "werkwoord, dan is het <em>qui</em>. Volgt er een nieuw onderwerp, dan is het "
              "<em>que</em>. <em>Le film <strong>qui</strong> commence</em> tegenover <em>le film "
              "<strong>que</strong> j'aime</em>."),
])

AANWIJZEND = dict(kop="Celui en le mien", blokken=[
    ("p", "<strong>Celui</strong> betekent <strong>die</strong> of <strong>degene</strong>, en "
          "vervangt een naamwoord dat je niet herhaalt."),
    ("p", bundel.tabel(["", "enkelvoud", "meervoud"], [
        ["mannelijk", "<strong>celui</strong>", "<strong>ceux</strong>"],
        ["vrouwelijk", "<strong>celle</strong>", "<strong>celles</strong>"],
    ])),
    ("p", "<em>Ce n'est pas mon vélo, c'est <strong>celui</strong> de ma sœur</em>. <em><strong>Ceux"
          "</strong> de ma classe sont partis</em>. Met <em>-ci</em> en <em>-là</em> wijs je verder "
          "aan: <strong>celui-ci</strong> is deze hier, <strong>celui-là</strong> is die daar. "
          "<em>Cellui</em> bestaat niet."),
    ("p", "De <strong>bezittelijke</strong> vorm zegt van wie iets is. Let op het dakje op "
          "<em>nôtre</em> en <em>vôtre</em>: dat is er bij <em>notre vélo</em> niet, en bij "
          "<em>le nôtre</em> wel."),
    ("p", bundel.tabel(["Van wie", "mannelijk", "vrouwelijk", "meervoud"], [
        ["van mij", "<strong>le mien</strong>", "la mienne", "les miens, les miennes"],
        ["van jou", "<strong>le tien</strong>", "la tienne", "les tiens, les tiennes"],
        ["van hem of haar", "<strong>le sien</strong>", "la sienne", "les siens, les siennes"],
        ["van ons", "<strong>le nôtre</strong>", "la nôtre", "les nôtres"],
        ["van jullie", "<strong>le vôtre</strong>", "la vôtre", "les vôtres"],
        ["van hen", "<strong>le leur</strong>", "la leur", "<strong>les leurs</strong>"],
    ])),
    ("p", "<em>Le mon</em> bestaat niet: na een lidwoord gebruik je altijd deze vormen. En "
          "<em>les leurs</em> is van hen, niet van ons: dat is <em>les nôtres</em>."),
])

VRAGEN_PERSOON = dict(kop="Vragen naar een persoon of een ding", blokken=[
    ("p", bundel.tabel(["Je vraagt naar", "Als onderwerp", "Als lijdend voorwerp"], [
        ["een <strong>persoon</strong>", "<strong>qui</strong> of <strong>qui est-ce qui</strong><br><em>Qui vient ?</em>",
         "<strong>qui est-ce que</strong><br><em>Qui est-ce que tu vois ?</em>"],
        ["een <strong>ding</strong>", "<strong>qu'est-ce qui</strong><br><em>Qu'est-ce qui se passe ?</em>",
         "<strong>qu'est-ce que</strong><br><em>Qu'est-ce que tu fais ?</em>"],
    ])),
    ("p", "<em>Qui</em> en <em>qui est-ce qui</em> betekenen dus hetzelfde; de tweede is enkel "
          "langer. En na een <strong>voorzetsel</strong> schrijf je <strong>quoi</strong>, nooit "
          "<em>que</em>: <em>À quoi tu penses ?</em>, <em>De quoi parlez-vous ?</em>"),
])

zet("voornaamwoorden-en-betrekkelijke-bijzinnen",
    "Voornaamwoorden en betrekkelijke bijzinnen",
    "Waar een voornaamwoord naar verwijst, in welke orde ze staan, en hoe qui, que, où en dont "
    "een bijzin vastmaken.",
    secties("voornaamwoorden-sujet-cod-coi-en-de-wederkerende")[:4]
    + [BEKLEMTOOND]
    + secties("voornaamwoorden-sujet-cod-coi-en-de-wederkerende")[4:]
    + [ONBEPAALD, BETREKKELIJK, AANWIJZEND, VRAGEN_PERSOON])


# ───────────────────── 12. Bijvoeglijke naamwoorden, bijwoorden en voorzetsels
MEERVOUD = dict(kop="Het meervoud en de overeenkomst", blokken=[
    ("p", bundel.tabel(["Soort", "Meervoud", "Voorbeeld"], [
        ["gewoon", "een <strong>s</strong> erbij", "petit → petits, blanche → blanches"],
        ["al een <strong>-s</strong> of <strong>-x</strong>", "<strong>verandert niet</strong>",
         "heureux → <strong>heureux</strong> (niet heureuxes), gris → gris"],
        ["op <strong>-al</strong>", "<strong>-aux</strong> in het mannelijk meervoud",
         "national → <strong>nationaux</strong>, principal → principaux, régional → régionaux"],
        ["op <strong>-e</strong>", "vrouwelijk <strong>hetzelfde</strong>, meervoud met s",
         "jeune → jeune, jeunes"],
    ])),
    ("p", "Horen er <strong>twee naamwoorden</strong> bij, dan gaat het bijvoeglijk naamwoord in het "
          "<strong>meervoud</strong>, en is één van de twee mannelijk, dan wordt het "
          "<strong>mannelijk</strong> meervoud: <em>le père et la mère sont <strong>contents</strong>"
          "</em>."),
    ("p", "Een <strong>kleur van twee woorden</strong> verandert helemaal niet mee: <em>des yeux "
          "<strong>bleu clair</strong></em>, <em>une veste vert foncé</em>. Daar staat geen enkele s "
          "op."),
])

VOORZETSELS_LIJST = dict(kop="De voorzetsels die je moet kennen", blokken=[
    ("p", bundel.tabel(["Frans", "Nederlands"], [
        ["<strong>grâce à</strong>", "<strong>dankzij</strong>, dus door iets goeds"],
        ["<strong>à cause de</strong>", "<strong>door toedoen van</strong> iets dat tegenzit: <em>à cause du train</em>"],
        ["<strong>malgré</strong>", "<strong>ondanks</strong>"],
        ["<strong>pendant</strong>", "<strong>tijdens</strong>; sinds is <em>depuis</em>"],
        ["<strong>chez</strong>", "<strong>bij iemand thuis</strong> of in zijn zaak: <em>chez le dentiste</em>"],
        ["<strong>pour</strong> + infinitief", "<strong>om te</strong>: <em>pour gagner de l'argent</em>"],
        ["<strong>sans</strong>", "zonder"],
    ])),
    ("p", "Een <strong>plaats</strong> zeg je met <em>sur</em> (op), <em>sous</em> (onder), "
          "<em>devant</em> (voor), <em>derrière</em> (achter), <em>entre</em> (tussen), <em>à côté "
          "de</em> (naast). <em>Le livre est <strong>sur</strong> la table.</em>"),
    ("p", bundel.tabel(["Waar of waarmee", "Voorzetsel", "Voorbeeld"], [
        ["een vrouwelijk land", "<strong>en</strong>", "<em>en France</em>, <em>en Belgique</em>"],
        ["een mannelijk land", "<strong>au</strong>", "<em>au Portugal</em>, <em>au Canada</em>"],
        ["een meervoudig land", "<strong>aux</strong>", "<em>aux Pays-Bas</em>"],
        ["een stad", "<strong>à</strong>", "<em>à Paris</em>, <em>à Hasselt</em>"],
        ["een vervoermiddel waar je <strong>in</strong> zit", "<strong>en</strong>",
         "<em>en voiture</em>, <em>en train</em>, <em>en bus</em>"],
        ["een vervoermiddel waar je <strong>op</strong> zit", "<strong>à</strong>",
         "<em>à vélo</em>, <em>à pied</em>, <em>à cheval</em>"],
    ])),
    ("kader", "<strong>Sommige uitdrukkingen trekken altijd de mee.</strong> <em>avoir envie "
              "<strong>de</strong></em> (zin hebben om), <em>avoir besoin <strong>de</strong></em> "
              "(nodig hebben), <em>avoir peur <strong>de</strong></em> (bang zijn om). Maar "
              "<em>commencer</em> vraagt <strong>à</strong>: <em>commencer à travailler</em>, nooit "
              "<em>commencer de</em>."),
])

TRAPPEN_EXTRA = dict(kop="Even, minder en het slechtste", blokken=[
    ("p", bundel.tabel(["Wat je zegt", "Frans", "Voorbeeld"], [
        ["groter dan", "<strong>plus … que</strong>", "<em>plus grand <strong>que</strong> moi</em>"],
        ["minder snel dan", "<strong>moins … que</strong>", "<em>moins rapide que moi</em>"],
        ["zo groot als", "<strong>aussi … que</strong>", "<em>aussi grand que son frère</em>"],
        ["de grootste", "<strong>le plus …</strong>", "<em>la plus belle ville</em>, <em>le plus grand de la classe</em>"],
        ["de minst dure", "<strong>le moins …</strong>", "<em>le moins cher</em>"],
    ])),
    ("p", "Na <em>que</em> en <em>comme</em> is er maar één juiste: het is altijd "
          "<strong>que</strong>. <em>Plus grand comme moi</em> en <em>plus grand de moi</em> bestaan "
          "niet."),
    ("p", "Naast <em>bon → meilleur</em> is er nog één onregelmatige: <em>mauvais</em> → "
          "<strong>pire</strong> → <em>le pire</em> (slecht, slechter, het slechtste)."),
    ("p", "In de superlatief blijft het lidwoord bij het naamwoord horen: <em><strong>la</strong> "
          "plus belle ville</em>, niet <em>le plus belle ville</em> en niet <em>la plus belle de "
          "ville</em>."),
])

BIJWOORD_EXTRA = dict(kop="Très of beaucoup", blokken=[
    ("p", "Beide betekenen <strong>veel</strong> of <strong>heel</strong>, maar ze staan niet bij "
          "hetzelfde woord."),
    ("p", bundel.tabel(["", "Hoort bij", "Voorbeeld"], [
        ["<strong>très</strong>", "een <strong>bijvoeglijk naamwoord</strong> of een bijwoord",
         "<em>très grand</em>, <em>très vite</em>"],
        ["<strong>beaucoup</strong>", "een <strong>werkwoord</strong> of een hoeveelheid",
         "<em>j'ai beaucoup travaillé</em>, <em>beaucoup de travail</em>"],
    ])),
    ("p", "<em>Très</em> staat altijd <strong>vóór</strong> het woord dat het versterkt. "
          "<em>Beaucoup grand</em> en <em>très travaillé</em> bestaan niet."),
    ("p", "Een <strong>bijvoeglijk naamwoord</strong> zegt iets over de persoon of de zaak, een "
          "<strong>bijwoord</strong> over de handeling: <em>elle est bonne</em> tegenover <em>elle "
          "chante <strong>bien</strong></em>. Bij <em>bon</em> hoort dus <em>bien</em>, en "
          "<em>bienne</em> of <em>bonment</em> bestaan niet."),
])

zet("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
    "Bijvoeglijke naamwoorden, bijwoorden en voorzetsels",
    "De vorm en de plaats van het bijvoeglijk naamwoord, de drie trappen, de bijwoorden op -ment "
    "en de voorzetsels bij een land, een vervoermiddel en een uitdrukking.",
    secties("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen")[:2]
    + [MEERVOUD]
    + [secties("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen")[2], TRAPPEN_EXTRA,
       secties("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen")[3], BIJWOORD_EXTRA,
       secties("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen")[4], VOORZETSELS_LIJST])


# De bundels in de orde van de thema's van de vakfiche, zodat de pdf's in die
# orde gebouwd worden en Beheer → Leerstof ze zo ook toont.
_ORDE = [
    "een-franse-tekst-lezen",
    "tekstsoorten-en-de-bedoeling-van-een-tekst",
    "de-franstalige-wereld-gewoontes-en-reizen",
    "schrijven-en-spreken-in-het-frans",
    "woordvelden-dagelijks-leven-eten-en-wonen",
    "woordvelden-gezondheid-natuur-en-milieu",
    "woordvelden-school-werk-geld-en-verkeer",
    "woordvelden-kunst-geschiedenis-en-de-samenleving",
    "woordvelden-wetenschap-techniek-en-taal",
    "lidwoorden-aanwijzers-bezitters-en-getallen",
    "voornaamwoorden-en-betrekkelijke-bijzinnen",
    "bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
    "de-tegenwoordige-tijd-en-de-gebiedende-wijs",
    "de-verleden-tijden",
    "de-toekomende-tijd-en-de-conditionnel",
    "zinsbouw-zinsdelen-en-congruentie",
]
assert sorted(_ORDE) == sorted(s[:-len(NA)] for s in BUNDELS), "orde klopt niet met de bundels"
BUNDELS = {s + NA: BUNDELS[s + NA] for s in _ORDE}


# ───────────────────── Wat deze fiche extra vraagt
# De woordvelden van dubbele finaliteit zijn concreter en breder dan die van
# 🚀 Boost: hieronder staat per thema wat de vragen van 🌍 Beyond DF erbij
# vragen en wat in de bundels van Boost nog niet stond.

def erbij(sleutel, *secties_):
    BUNDELS[sleutel + NA]["secties"].extend(secties_)


erbij("een-franse-tekst-lezen",
    dict(kop="Lezen met een plan", blokken=[
        ("p", "Voor je begint te lezen, stel je je drie vragen: <strong>waarover gaat deze "
              "tekst</strong>, <strong>wat wil ik weten</strong>, en <strong>wat weet ik er al "
              "over</strong>. Dat laatste helpt echt: je kennis van het Nederlands en van het "
              "<strong>Engels</strong> levert je gratis woorden op (<em>la nation</em>, "
              "<em>le train</em>, <em>la population</em>)."),
        ("p", "De titel, de <strong>tussentitels</strong>, de foto's, een kader en een "
              "<strong>grafiek</strong> zijn <strong>visuele hulpmiddelen</strong>: die mag je bij "
              "een <strong>leestekst</strong> nooit <strong>overslaan</strong>. Ze zeggen vaak in "
              "één blik waarover de tekst gaat."),
        ("p", "Het <strong>onderwerp</strong> van een tekst <strong>verwoord</strong> je achteraf "
              "in enkele woorden, niet in een hele zin. En je hoeft niet elk "
              "<strong>onbekend</strong> woord op te zoeken: zoek enkel op wat je nodig hebt om de "
              "vraag te kunnen beantwoorden."),
    ]),
    dict(kop="De signaalwoorden op een rij", blokken=[
        ("p", "Een <strong>signaalwoord</strong> <strong>kondigt</strong> aan wat er komt, en zo "
              "kan je de <strong>gedachtegang</strong> volgen. Ze <strong>helpen</strong> je dus "
              "ook als je een woord mist."),
        ("p", bundel.tabel(["Wat het aankondigt", "Franse signaalwoorden"], [
            ["<strong>orde</strong>: eerst, dan, tenslotte",
             "<strong>d'abord</strong>, ensuite, puis, <strong>enfin</strong>"],
            ["een <strong>tegenstelling</strong>",
             "<strong>par contre</strong> (twee woorden), en revanche, cependant, mais, pourtant"],
            ["een reden", "parce que, car, à cause de"],
            ["een gevolg", "donc, alors, c'est pourquoi"],
            ["een voorbeeld", "par exemple, comme"],
            ["erbij", "aussi, de plus, en outre"],
        ])),
        ("p", "<em>Enfin</em> <strong>begint</strong> dus geen nieuwe reden: het sluit af."),
    ]),
    dict(kop="Het communicatiemodel", blokken=[
        ("p", "Bij het <strong>communicatiemodel</strong> vraag je je af <strong>door wie</strong> "
              "een tekst <strong>gemaakt</strong> is en <strong>voor wie</strong> hij "
              "<strong>bedoeld</strong> is. Vijf vragen horen erbij."),
        ("p", bundel.tabel(["Onderdeel", "De vraag"], [
            ["de zender", "wie heeft dit gemaakt?"],
            ["de ontvanger", "voor wie is het bedoeld?"],
            ["de boodschap", "wat staat er?"],
            ["het <strong>kanaal</strong>", "<strong>waarlangs komt het bij je: een krant, een website, de radio?</strong>"],
            ["de bedoeling", "wil het informeren, overtuigen of ontspannen?"],
        ])),
    ]))

erbij("tekstsoorten-en-de-bedoeling-van-een-tekst",
    dict(kop="Een voorbeeld bij elke tekstsoort", blokken=[
        ("p", bundel.tabel(["Tekstsoort", "Franse voorbeelden"], [
            ["informatief", "un article, une <strong>interview</strong>, le <strong>nieuws</strong> op de radio (un journal parlé)"],
            ["persuasief", "une <strong>publicité</strong>, une <strong>campagne</strong> de <strong>sécurité</strong> routière, une affiche pour un <strong>concert</strong>"],
            ["prescriptief", "une recette, un mode d'emploi, un règlement"],
            ["opiniërend", "une lettre de lecteur, un blog, une <strong>boekrecensie</strong> (une critique)"],
            ["narratief", "un conte, un <strong>podcast</strong> met een verhaal"],
            ["literair", "un poème, une <strong>chanson</strong>, une bande <strong>dessinée</strong>"],
        ])),
        ("p", "Een <strong>bande dessinée</strong> is dus <strong>literair</strong> en geen "
              "informatieve tekst, en een <strong>interview</strong> is informatief en niet "
              "literair. Een <strong>podcast</strong> kan allebei zijn: het hangt af van wat erin "
              "verteld wordt."),
        ("p", "Een <strong>prescriptieve</strong> tekst herken je <strong>waaraan</strong>? Aan een "
              "<strong>stappenplan</strong> met genummerde stappen en aan de "
              "<strong>imperatief</strong>: <em>Mélangez</em>, <em>Ajoutez</em>, "
              "<em><strong>d'abord</strong>…, ensuite…</em>"),
        ("p", "<strong>Hoe</strong> noem je een tekst <strong>waarin</strong> <strong>iemand</strong> "
              "zijn <strong>mening</strong> geeft? Met één woord: <strong>opiniërend</strong>. En "
              "een tekst die uitlegt wat of hoe je iets moet doen, is "
              "<strong>prescriptief</strong>."),
        ("p", "Bij elke tekst horen twee vragen: wat is de <strong>bedoeling</strong> "
              "(informeren, overtuigen, voorschrijven, ontspannen) en wat is het "
              "<strong>kanaal</strong>, dus waarlangs de tekst bij je komt: een krant, een website, "
              "de radio, een affiche. Dezelfde boodschap klinkt in een mail anders dan op een "
              "affiche."),
        ("p", "Een tekst kan <strong>feiten en meningen door elkaar bevatten</strong>. Woorden die "
              "een mening <strong>verraden</strong>: <em>à mon <strong>avis</strong></em> (in mijn "
              "opinie), <em>je trouve que</em>, <em>je pense que</em>, en bijvoeglijke naamwoorden "
              "als <em><strong>affreux</strong></em> (afschuwelijk), <em>magnifique</em>, "
              "<em>le <strong>meilleur</strong></em>. Een feit kan je nameten, een mening niet."),
    ]),
    dict(kop="Het register: formeel of informeel", blokken=[
        ("p", "Het <strong>register</strong> is hoe formeel je schrijft. Een "
              "<strong>gepast</strong> register betekent dat je je aanpast aan je lezer, niet dat "
              "je zo <strong>formeel</strong> <strong>mogelijk</strong> schrijft. Aan een vriend "
              "schrijf je <em>tu</em>, aan een <strong>volwassene</strong> die je niet kent "
              "<em>vous</em>."),
        ("p", bundel.tabel(["In een formele mail", "In een bericht aan een vriend"], [
            ["<strong>Bonjour</strong> Madame, Bonjour Monsieur", "Salut !"],
            ["Je <strong>voudrais</strong> vous demander…", "Je veux…"],
            ["Merci <strong>d'avance</strong>", "Merci !"],
            ["<strong>Cordialement</strong>", "À plus !"],
        ])),
        ("p", "<em>Je voudrais un café</em> klinkt dus <strong>hoffelijker</strong> dan <em>je veux "
              "un café</em>: dat is dezelfde vraag, maar met een stap afstand. In een formele mail "
              "<strong>gewoon</strong> <em>tu</em> schrijven kan niet."),
        ("p", "Een goed <strong>opgebouwde</strong> tekst bestaat uit drie delen: een "
              "<strong>inleiding</strong>, een <strong>midden</strong> met je uitleg, en een slot."),
        ("p", "<strong>Zeg eerst bonjour.</strong> In het Frans begint elke vraag aan een "
              "onbekende daarmee; meteen met je vraag beginnen klinkt onbeschoft."),
    ]))

erbij("de-franstalige-wereld-gewoontes-en-reizen",
    dict(kop="Gewoontes en gebruiken", blokken=[
        ("p", bundel.tabel(["Frans", "Wat het is"], [
            ["<strong>le 14 juillet</strong>", "de nationale <strong>feestdag</strong> van <strong>Frankrijk</strong> (bij ons is dat 21 juli)"],
            ["<strong>une baguette</strong>", "het lange witte brood dat <strong>typisch</strong> Frans is"],
            ["<strong>la rentrée</strong>", "het begin van het <strong>schooljaar</strong>, begin september"],
            ["<strong>le bac</strong>", "het <strong>eindexamen</strong> van het secundair in Frankrijk"],
            ["<strong>les soldes</strong>", "de <strong>koopjes</strong>, de solden"],
            ["<strong>le TGV</strong>", "de <strong>snelle</strong> trein van Frankrijk, drie letters"],
            ["<strong>le périphérique</strong>", "de <strong>ringweg</strong> rond <strong>Parijs</strong>"],
            ["<strong>la Francophonie</strong>", "de <strong>Franstalige</strong> wereld samen"],
        ])),
        ("p", "Bij een <strong>maaltijd</strong> horen <strong>l'apéritif</strong>, "
              "<strong>l'entrée</strong> (het voorgerecht), le plat en le dessert. Het "
              "<strong>middagmaal</strong> is in Frankrijk <strong>le déjeuner</strong>; in België "
              "zeggen we daarvoor <em>le dîner</em>."),
        ("p", "Het Frans is officieel in <strong>België</strong>, in Zwitserland, in "
              "<strong>Canada</strong> en in een groot deel van <strong>Afrika</strong> (Senegal, "
              "Congo, Marokko). In <strong>Canada</strong> is het <strong>Engels</strong> de andere "
              "officiële taal. In Zwitserland betaal je met de <strong>frank</strong>, niet met de "
              "euro. In Portugal spreekt men geen Frans."),
        ("p", "<strong>Brussel</strong> is officieel <strong>tweetalig</strong>, Nederlands en "
              "Frans. In Wallonië <strong>liggen</strong> <strong>Luik</strong>, <strong>Namen</strong> "
              "en <strong>Charleroi</strong>; Gent ligt in Vlaanderen."),
        ("p", "<strong>Lichaamstaal</strong> is wat je zegt <strong>zonder woorden</strong>: je "
              "houding, je handen, of je iemand aankijkt. Dat hoort bij een gesprek even goed als "
              "je woorden."),
    ]),
    dict(kop="Op reis", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>un billet</strong>", "een ticket"],
            ["<strong>un aller-retour</strong>", "<strong>heen en terug</strong>"],
            ["<strong>une valise</strong>, <strong>les bagages</strong>", "een koffer, de <strong>bagage</strong>"],
            ["<strong>un passeport</strong>", "een paspoort"],
            ["<strong>un avion</strong>", "een <strong>vliegtuig</strong>"],
            ["<strong>un car</strong>, <strong>un ferry</strong>, <strong>le métro</strong>", "een reisbus, een veerboot, de metro"],
            ["<strong>une frontière</strong>", "de <strong>grens</strong> tussen twee landen"],
            ["<strong>à l'étranger</strong>", "in het <strong>buitenland</strong>"],
            ["<strong>un paysage</strong>", "een <strong>landschap</strong>"],
            ["<strong>la campagne</strong>", "het <strong>platteland</strong>"],
        ])),
        ("p", "Je zegt <em>je vais <strong>en</strong> train</em> of <em>par le train</em>, nooit "
              "<em>avec le train</em>."),
        ("p", bundel.tabel(["Waar je slaapt of blijft", "Wat het is"], [
            ["<strong>réserver une chambre</strong>", "een kamer <strong>boeken</strong>"],
            ["<strong>une chambre d'hôtes</strong>", "een kamer <strong>bij mensen thuis</strong>"],
            ["<strong>un hébergement</strong>", "een <strong>verblijfplaats</strong>, waar je ook slaapt"],
            ["<strong>un séjour</strong>", "een <strong>verblijf</strong>, de tijd dat je blijft"],
            ["<strong>une station balnéaire</strong>", "een <strong>badplaats</strong> aan de zee"],
            ["<strong>un gîte</strong>", "een vakantiehuisje"],
            ["<strong>une visite guidée</strong>", "een <strong>bezoek met gids</strong>"],
        ])),
        ("p", "Loopt het mis, dan heb je deze nodig: <strong>un retard</strong> (vertraging), "
              "<strong>une grève</strong> (een staking), <strong>une déviation</strong> (een "
              "omleiding). <em>Un souvenir</em> is geen <strong>probleem</strong>, dat is een "
              "aandenken."),
        ("kader", "<strong>Twee paren die niet hetzelfde zijn.</strong> "
                  "<em>Un <strong>voyage</strong></em> is de hele reis, <em>un "
                  "<strong>trajet</strong></em> is het stuk weg dat je aflegt, dus "
                  "<strong>niet precies</strong> hetzelfde. En <em>un "
                  "<strong>touriste</strong></em> is iemand op vakantie, <em>un voyageur</em> is "
                  "iedereen die reist, ook voor zijn werk."),
        ("p", "Een <strong>inwoner</strong> van Zwitserland is <em>un <strong>Suisse</strong></em>, "
              "van Frankrijk <em>un Français</em>, van België <em>un Belge</em>. Een landnaam en "
              "een inwoner krijgen in het Frans een hoofdletter, een taal niet: <em>je parle "
              "français</em>."),
    ]))


erbij("schrijven-en-spreken-in-het-frans",
    dict(kop="Je tekst verzorgen", blokken=[
        ("p", "Een goede <strong>lay-out</strong> bestaat uit een titel, "
              "<strong>alinea's</strong> en <strong>witruimte</strong> tussen de delen. Niet uit "
              "veel kleuren. Een alinea heet in het Frans <strong>un paragraphe</strong>, een brief "
              "<strong>une lettre</strong>."),
        ("p", "<strong>Taakvoltooiing</strong> is het eerste waarop je beoordeeld wordt: "
              "<strong>je doel is bereikt</strong>, dus de lezer weet wat hij moest weten. Een "
              "tekst zonder fouten die de vraag niet beantwoordt, haalt daar niets. Je tekst hoeft "
              "trouwens niet <strong>helemaal</strong> <strong>foutloos</strong> te zijn; hij moet "
              "wel begrijpelijk zijn."),
        ("p", "De <strong>opgegeven</strong> lengte respecteer je wel: te kort is een onvolledige "
              "taak. En de <strong>tekststructuur</strong> die de fiche verwacht, is "
              "<strong>inleiding, midden en slot</strong>."),
        ("p", "Een tekst houdt aan <strong>elkaar</strong> met verbindingswoorden: "
              "<em>d'abord</em>, <em>ensuite</em>, <em>enfin</em>, <em>mais</em>, <em>parce que</em>."),
        ("p", bundel.tabel(["Op het schrijfexamen mag", "Niet"], [
            ["een online woordenboek", "je <strong>samenvatting</strong> van thuis"],
            ["een <strong>spellingcontrole</strong>", "een afgewerkte tekst van thuis"],
            ["je schrijfplan op het <strong>kladpapier</strong>", "hulp van iemand anders"],
        ])),
        ("kader", "<strong>Het laatste wat je doet, is nalezen.</strong> Niet nog een alinea "
                  "bijschrijven, en niet alles in het net herschrijven: gewoon <strong>nalezen</strong> "
                  "op de werkwoordsvormen, de overeenkomst en de kleine woordjes."),
    ]),
    dict(kop="Hoffelijk vragen: de conditionnel de politesse", blokken=[
        ("p", "Het <strong>register</strong> is het soort taalgebruik dat bij je lezer past: "
              "<strong>formeel</strong> of <strong>informeel</strong>. De <em>vous</em>-vorm "
              "gebruik je bij een <strong>onbekende</strong>, niet bij een vriend, een broer of een "
              "klasgenoot. En je past je taal aan de <strong>ontvanger</strong> aan."),
        ("p", bundel.tabel(["Hoffelijk (conditionnel de politesse)", "Te direct"], [
            ["Je <strong>voudrais</strong> un café, <strong>s'il vous plaît</strong>.", "Je veux un café."],
            ["<strong>J'aimerais</strong> réserver une chambre.", "Je réserve une chambre."],
            ["<strong>Pourriez-vous</strong> <strong>m'aider</strong> ?", "Aidez-moi."],
        ])),
        ("p", "<strong>S'il vous plaît</strong> betekent <strong>alstublieft</strong>; "
              "<em>merci</em> is dank u wel. Een <strong>formele</strong> mail aan iemand wiens naam "
              "je niet kent, begin je met <strong>Madame, Monsieur,</strong> en je sluit af met "
              "<strong>Cordialement</strong>. <em>Gros bisous</em>, <em>À plus</em> en <em>Salut</em> "
              "horen bij vrienden, en <em>tu</em> schrijf je in een formele mail niet."),
        ("p", "<em>Bonjour Madame, je vous écris pour vous <strong>demander</strong> un "
              "<strong>renseignement</strong></em> is dus <strong>formeel</strong>, en precies hoe "
              "het hoort."),
    ]),
    dict(kop="Wat je in een gesprek zegt", blokken=[
        ("p", bundel.tabel(["Wat je wil", "Frans"], [
            ["een <strong>sociaal</strong> contact leggen",
             "<strong>Bonjour</strong>, <strong>Au revoir</strong>, <strong>Merci beaucoup</strong>"],
            ["<strong>bedanken</strong>", "<strong>Merci</strong> (twee lettergrepen)"],
            ["je <strong>verontschuldigen</strong>", "Je suis <strong>désolé(e)</strong>, Excusez-moi"],
            ["<strong>reageren</strong> op een <strong>verontschuldiging</strong>",
             "<strong>Ce n'est pas grave</strong>"],
            ["<strong>feliciteren</strong> of <strong>waardering</strong> uiten",
             "<strong>Beau travail !</strong>, Bravo !, Félicitations !"],
            ["iemand <strong>uitnodigen</strong>", "<strong>Tu viens samedi ?</strong>, Ça te dit ?"],
        ])),
        ("p", "<strong>Begrijp je iets niet, vraag het.</strong> <em>Pouvez-vous "
              "<strong>répéter</strong>, s'il vous plaît ?</em> of <em>Pouvez-vous "
              "<strong>parler</strong> plus <strong>lentement</strong> ?</em>, dus "
              "<strong>trager</strong> spreken. Gewoon <em>oui</em> antwoorden terwijl je het niet "
              "<strong>begrepen</strong> hebt, is de slechtste keuze; in het Nederlands verdergaan "
              "ook."),
        ("p", "Merk je dat de ander <strong>jou</strong> niet <strong>begrijpt</strong>, dan "
              "<strong>herhaal</strong> je je boodschap of zeg je ze <strong>anders</strong>. En weet "
              "je een woord niet, zeg het dan <strong>met wat je kent</strong>: <em>la chose pour "
              "ouvrir la porte</em> is beter dan zwijgen."),
        ("p", "Een gesprek kan je <strong>niet</strong> altijd op <strong>voorhand</strong> "
              "<strong>voorbereiden</strong>: je gesprekspartner bepaalt de helft. Wat je wel kan "
              "voorbereiden, zijn je vaste zinnen. En je toont <strong>interesse</strong> in de "
              "ander: knikken, doorvragen, aankijken."),
    ]),
    dict(kop="Wat een zin doet", blokken=[
        ("p", bundel.tabel(["Wat de zin doet", "Voorbeeld"], [
            ["<strong>informatie</strong> geven aan een klant", "<em>Le gîte a deux <strong>chambres</strong>.</em>"],
            ["je <strong>mening</strong> geven", "<em>Je <strong>trouve</strong> ça <strong>injuste</strong>.</em>"],
            ["iets <strong>vertellen</strong>", "<em>J'ai vu un <strong>accident</strong>.</em>"],
            ["iets <strong>uitleggen</strong>", "<em><strong>Suivez</strong> le <strong>sentier</strong>.</em>"],
            ["iemand <strong>overtuigen</strong>",
             "<em>C'est moins cher.</em> / <em>Ça fait <strong>gagner</strong> du temps.</em> / <em>Tu <strong>devrais</strong> <strong>essayer</strong>.</em>"],
        ])),
        ("p", "<em>Comment tu t'appelles ?</em> <strong>probeert</strong> niemand te "
              "<strong>overtuigen</strong>: dat is gewoon een vraag."),
    ]))


erbij("woordvelden-dagelijks-leven-eten-en-wonen",
    dict(kop="Familie en de mensen rond je", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>un parent</strong>", "een <strong>familielid</strong>; <em>les parents</em> zijn wel de ouders"],
            ["<strong>une tante</strong>, un oncle", "een tante, een oom"],
            ["<strong>un neveu</strong>, une nièce", "een neef, een nicht (het kind van je tante)"],
            ["<strong>un cousin</strong>, une cousine", "een kozijn, een nicht (het kind van je oom of tante)"],
            ["<strong>un voisin</strong>", "een <strong>buur</strong>"],
            ["<strong>un invité</strong>", "een genodigde"],
        ])),
        ("p", "<em>Un <strong>locataire</strong></em> hoort hier niet bij: dat is een "
              "<strong>huurder</strong>, en dus geen familie."),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>s'entendre bien avec quelqu'un</strong>", "goed <strong>overeenkomen</strong> met iemand"],
            ["<strong>en avoir assez de quelque chose</strong>", "er <strong>genoeg</strong> van hebben"],
            ["<strong>un loisir</strong>", "een <strong>vrijetijdsbesteding</strong>"],
            ["<strong>faire la grasse matinée</strong>", "<strong>uitslapen</strong>"],
            ["<strong>un cadeau</strong>, <strong>une bougie</strong>", "een cadeau, een kaars (bij een <strong>feest</strong>)"],
        ])),
        ("kader", "<strong>Twee vaste combinaties.</strong> Je zegt <em>faire une "
                  "<strong>erreur</strong></em> en nooit <em><strong>donner</strong> une erreur</em>. "
                  "En een raad geven is <em>donner un <strong>conseil</strong></em>: <em>un "
                  "<strong>conseiller</strong></em> is de persoon die raad geeft, een raadgever. "
                  "En je gaat <em>au cinéma <strong>en</strong> bus</em>, nooit <em>avec le bus</em>."),
    ]),
    dict(kop="Eten en drinken", blokken=[
        ("p", bundel.tabel(["Maaltijd", "In Frankrijk", "Bij ons"], [
            ["<strong>ontbijt</strong>", "<strong>le petit déjeuner</strong>", "le petit déjeuner"],
            ["middagmaal", "le déjeuner", "<strong>le dîner</strong>"],
            ["<strong>avondmaal</strong>", "<strong>le dîner</strong>", "<strong>le souper</strong>"],
            ["<strong>vieruurtje</strong>", "<strong>le goûter</strong>", "le goûter, le quatre-heures"],
        ])),
        ("p", "Op het examen zijn voor het avondmaal <em>le dîner</em> én <em>le souper</em> goed: "
              "het hangt af van waar je bent."),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une entrée</strong>", "een <strong>voorgerecht</strong>"],
            ["<strong>épicé</strong>", "<strong>pikant</strong>"],
            ["<strong>à emporter</strong>", "<strong>om mee te nemen</strong>; ter plaatse eten is <em>sur place</em>"],
            ["<strong>une cuillère</strong>", "een <strong>lepel</strong> (ook geschreven <em>une cuiller</em>)"],
            ["<strong>le thé</strong>, <strong>le jus</strong>, <strong>le cidre</strong>", "thee, sap, cider: <strong>dranken</strong>"],
        ])),
        ("p", "<em>Le poivre</em> is peper en dus geen drank, en <em>une armoire</em> is een kast."),
    ]),
    dict(kop="Het huis, de tuin en het huishouden", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une maison jumelée</strong>", "een <strong>halfopen</strong> woning"],
            ["<strong>une villa</strong>", "een <strong>groot, vrijstaand huis</strong>, geen huisje"],
            ["<strong>un appartement</strong>", "een appartement"],
            ["<strong>le rez-de-chaussée</strong>", "het <strong>gelijkvloers</strong>"],
            ["<strong>le couloir</strong>, <strong>le grenier</strong>, la cave",
             "de gang, de <strong>zolder</strong>, de kelder: <strong>ruimtes</strong> in een huis"],
            ["<strong>les toilettes</strong>", "het <strong>toilet</strong>, altijd in het meervoud"],
            ["<strong>les meubles</strong>", "de meubels, ook meervoud, nooit <strong>enkelvoud</strong>"],
            ["<strong>à la maison</strong>", "<strong>thuis</strong>"],
        ])),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>le loyer</strong>", "de <strong>huur</strong> die je elke maand betaalt"],
            ["<strong>un locataire</strong>", "een <strong>huurder</strong>; de eigenaar is <em>le propriétaire</em>"],
            ["<strong>déménager</strong>", "<strong>verhuizen</strong>"],
            ["<strong>douillet</strong>", "<strong>gezellig en warm</strong>"],
            ["<strong>une chaudière</strong>", "een <strong>ketel</strong> voor de verwarming"],
        ])),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une tâche ménagère</strong>", "een <strong>klusje</strong> in huis"],
            ["<strong>faire la vaisselle</strong>", "<strong>afwassen</strong>"],
            ["<strong>ranger sa chambre</strong>", "zijn kamer <strong>opruimen</strong>"],
            ["<strong>un aspirateur</strong>", "een stofzuiger"],
            ["<strong>une bouilloire</strong>", "een waterkoker"],
            ["<strong>un robinet</strong>", "een kraan"],
            ["<strong>une poubelle</strong>", "een <strong>vuilnisbak</strong>"],
            ["<strong>un rideau</strong>", "een <strong>gordijn</strong>"],
        ])),
        ("p", "In de tuin: <strong>la pelouse</strong> (het gras), <strong>la haie</strong> (de "
              "haag), <strong>la terrasse</strong>, les fleurs. <em>L'escalier</em> is de trap, en "
              "die staat binnen."),
    ]))


erbij("woordvelden-gezondheid-natuur-en-milieu",
    dict(kop="Bij de dokter en in de apotheek", blokken=[
        ("p", "<strong>Pijn</strong> zeg je in het Frans met <em>avoir mal à</em>: <em>j'ai mal "
              "à la <strong>gorge</strong></em> is <strong>keelpijn</strong>, <em>j'ai mal à la "
              "tête</em> hoofdpijn, <em>j'ai mal au dos</em> rugpijn. <em>J'ai une douleur dans ma "
              "tête</em> zeggen ze niet."),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>la toux</strong>", "de hoest"],
            ["<strong>la fièvre</strong>", "de <strong>koorts</strong>"],
            ["<strong>une allergie</strong>", "een allergie"],
            ["<strong>une ordonnance</strong>", "een <strong>voorschrift</strong> van de dokter"],
            ["<strong>la pharmacie</strong>", "de <strong>apotheek</strong>"],
            ["<strong>un pansement</strong>", "een <strong>pleister</strong>"],
            ["<strong>un médecin généraliste</strong>", "een <strong>huisarts</strong>"],
            ["<strong>guérir</strong>", "<strong>genezen</strong>"],
            ["<strong>un bilan de santé</strong>", "een <strong>controle</strong> bij de dokter"],
        ])),
        ("p", "In het <strong>ziekenhuis</strong>: <strong>une opération</strong>, "
              "<strong>une ambulance</strong>, <strong>un infirmier</strong> of une infirmière. "
              "<em>Une tondeuse</em> is een grasmachine, en <em>un portefeuille</em> een "
              "portefeuille: geen <strong>klachten</strong>."),
    ]),
    dict(kop="Gevoelens en gezond leven", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>nerveux</strong>", "nervous, gespannen"],
            ["<strong>seul</strong>", "alleen, eenzaam"],
            ["<strong>fier</strong>", "trots"],
            ["<strong>être stressé</strong>", "<strong>gespannen</strong> zijn"],
            ["<strong>épuisé</strong>", "<strong>uitgeput</strong>"],
            ["<strong>avoir le moral à zéro</strong>", "<strong>zich slecht voelen</strong>, in de put zitten"],
        ])),
        ("p", "<em>Bondé</em> gaat niet over een <strong>gevoel</strong>: dat betekent propvol, "
              "over een bus of een zaal."),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une alimentation équilibrée</strong>", "<strong>gevarieerd eten</strong>"],
            ["<strong>prendre du poids</strong>", "<strong>bijkomen</strong>; vermageren is <em>maigrir</em>"],
            ["<strong>le sommeil</strong>", "de <strong>slaap</strong> als naamwoord; slapen is <em>dormir</em>"],
            ["<strong>prendre soin de soi</strong>", "goed <strong>voor jezelf zorgen</strong>"],
            ["<strong>la santé mentale</strong>", "je <strong>geestelijke</strong> gezondheid, dus niet je lichaam"],
        ])),
    ]),
    dict(kop="De natuur, het weer en het milieu", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>la faune sauvage</strong>", "de <strong>wilde dieren</strong>"],
            ["<strong>un hérisson</strong>", "een egel"],
            ["<strong>un hibou</strong>", "een uil"],
            ["<strong>un écureuil</strong>", "een eekhoorn"],
            ["<strong>un arbre</strong>", "een <strong>boom</strong>"],
            ["<strong>une espèce</strong>", "een <strong>soort</strong>"],
            ["<strong>disparaître</strong>", "<strong>verdwijnen</strong>"],
            ["<strong>un ruisseau</strong>", "een <strong>beek</strong>"],
            ["<strong>une récolte</strong>", "een <strong>oogst</strong>"],
            ["<strong>abattre un arbre</strong>", "een boom <strong>omhakken</strong>"],
        ])),
        ("p", "<em>Un érable</em> is ook een boom (een esdoorn) en geen dier. En een boom die zijn "
              "<strong>bladeren verliest</strong> is <em>un <strong>feuillu</strong></em>; <em>un "
              "<strong>conifère</strong></em> is net een naaldboom, die ze houdt."),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une averse</strong>", "een regenbui"],
            ["<strong>une brise</strong>", "een briesje"],
            ["<strong>un orage</strong>", "een onweer"],
            ["<strong>la sécheresse</strong>", "de <strong>droogte</strong>"],
            ["<strong>une inondation</strong>", "een <strong>overstroming</strong>"],
        ])),
        ("p", "<em>Le <strong>climat</strong></em> is het klimaat over vele jaren, <em>le "
              "<strong>temps</strong></em> is het weer van vandaag: dat is dus "
              "<strong>niet hetzelfde</strong>. <em>Un trottoir</em> is een voetpad en hoort bij het "
              "verkeer."),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>l'environnement</strong>", "het <strong>milieu</strong>, de natuur rond ons"],
            ["<strong>les déchets</strong>", "het <strong>afval</strong>"],
            ["<strong>recycler</strong>", "<strong>hergebruiken</strong>, recycleren"],
            ["<strong>la pollution</strong>", "de vervuiling"],
            ["<strong>les émissions</strong>", "de uitstoot"],
            ["<strong>le gaspillage</strong>", "de verspilling"],
            ["<strong>les énergies renouvelables</strong>", "<strong>hernieuwbare energie</strong>: wind, zon, water"],
            ["<strong>l'empreinte carbone</strong>", "de <strong>koolstofvoetafdruk</strong>"],
            ["<strong>durable</strong>", "<strong>duurzaam</strong>, dus lang mee te gaan zonder schade"],
        ])),
    ]))


erbij("woordvelden-school-werk-geld-en-verkeer",
    dict(kop="Op school", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une matière</strong>", "een <strong>vak</strong>"],
            ["<strong>un horaire</strong>", "een uurrooster"],
            ["<strong>un bulletin</strong>", "een rapport"],
            ["<strong>les devoirs</strong>", "het huiswerk"],
            ["<strong>un professeur</strong>, <strong>un enseignant</strong>", "een <strong>leerkracht</strong>"],
            ["<strong>la récréation</strong>", "de <strong>pauze</strong>"],
            ["<strong>prendre des notes</strong>", "<strong>nota's</strong> nemen"],
            ["<strong>un diplôme</strong>", "een <strong>diploma</strong>"],
        ])),
        ("kader", "<strong>Passer of réussir.</strong> <em><strong>Passer</strong> un examen</em> "
                  "betekent een examen <strong>afleggen</strong>, en zegt nog niets over het "
                  "resultaat. <em><strong>Réussir</strong> un examen</em> is <strong>slagen</strong>. "
                  "Dat is een klassieke valse vriend, want <em>passeren</em> klinkt als voorbij."),
        ("p", "<em>Un caddie</em> is een winkelkar en hoort niet op <strong>school</strong>."),
    ]),
    dict(kop="Werk en werk zoeken", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>un plombier</strong>", "een loodgieter"],
            ["<strong>un infirmier</strong>", "een verpleger"],
            ["<strong>un vendeur</strong>", "een verkoper"],
            ["<strong>le salaire</strong>", "het <strong>loon</strong>"],
            ["<strong>un stagiaire</strong>", "<strong>iemand die stage doet</strong>"],
            ["<strong>un collègue</strong>", "een <strong>werkgenoot</strong>, dus niet iemand van je school"],
            ["<strong>une compétence</strong>", "een <strong>vaardigheid</strong>, iets dat je kan"],
            ["<strong>un travail à temps partiel</strong>", "<strong>deeltijds</strong> werk"],
            ["<strong>être licencié</strong>", "<strong>ontslagen worden</strong>, dus net geen promotie"],
            ["<strong>au chômage</strong>, sans emploi", "<strong>werkloos</strong>"],
        ])),
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une offre d'emploi</strong>", "een vacature"],
            ["<strong>une candidature</strong>", "een sollicitatie"],
            ["<strong>postuler pour un emploi</strong>", "<strong>solliciteren</strong>"],
            ["<strong>un entretien</strong>", "een gesprek, ook een sollicitatiegesprek"],
            ["<strong>un CV</strong>", "een <strong>overzicht van je loopbaan</strong>"],
            ["<strong>une date limite</strong>", "een <strong>uiterste</strong> datum"],
        ])),
        ("p", "<em>Une cantine</em> is de refter en hoort niet bij <strong>werk zoeken</strong>."),
    ]),
    dict(kop="Geld en winkelen", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>une bonne affaire</strong>", "een <strong>koopje</strong>"],
            ["<strong>une réduction</strong>, <strong>un rabais</strong>", "een <strong>korting</strong>"],
            ["<strong>un prêt</strong>", "een lening"],
            ["<strong>les intérêts</strong>", "de <strong>intresten</strong>"],
            ["<strong>l'épargne</strong>", "het <strong>sparen</strong>"],
            ["<strong>un ticket de caisse</strong>", "een <strong>kassabon</strong>"],
            ["<strong>payer en espèces</strong>", "<strong>cash</strong> betalen"],
            ["<strong>rembourser</strong>", "<strong>terugbetalen</strong>"],
            ["<strong>la TVA</strong>", "de <strong>belasting op de toegevoegde waarde</strong>, onze btw"],
            ["<strong>se permettre quelque chose</strong>", "iets <strong>kunnen betalen</strong>"],
        ])),
        ("p", "In een <strong>winkel</strong>: <strong>la caisse</strong> (de kassa), "
              "<strong>la file</strong> (de rij), <strong>le rayon</strong> (de afdeling), "
              "<strong>un client</strong> (een <strong>klant</strong>). <em>Le casque</em> is een "
              "helm, <em>un passage</em> een doorgang: die horen er niet bij."),
    ]),
    dict(kop="Onderweg", blokken=[
        ("p", bundel.tabel(["Frans", "Nederlands"], [
            ["<strong>le permis de conduire</strong>", "het <strong>rijbewijs</strong>"],
            ["<strong>un rond-point</strong>", "een rotonde"],
            ["<strong>un embouteillage</strong>", "een file"],
            ["<strong>un piéton</strong>", "een voetganger"],
            ["<strong>un passage pour piétons</strong>", "een <strong>zebrapad</strong>, dus voor mensen en niet voor <strong>dieren</strong>"],
            ["<strong>le trottoir</strong>", "het <strong>voetpad</strong>, niet de rijweg"],
            ["<strong>une autoroute</strong>", "een <strong>snelweg</strong>"],
            ["<strong>l'essence</strong>", "<strong>benzine</strong>; diesel heet <em>le diesel</em>"],
            ["<strong>une amende</strong>", "een <strong>boete</strong>"],
            ["<strong>un camion</strong>", "een <strong>vrachtwagen</strong>"],
            ["<strong>l'heure de pointe</strong>", "het <strong>spitsuur</strong>"],
            ["<strong>faire la navette</strong>", "<strong>pendelen</strong>, elke dag heen en terug naar je werk"],
        ])),
        ("p", "<em>Une casserole</em> is een kookpot en hoort niet bij het "
              "<strong>verkeer</strong>."),
    ]))


erbij("lidwoorden-aanwijzers-bezitters-en-getallen",
    dict(kop="Vier plaatsen waar het Frans anders kiest dan wij", blokken=[
        ("p", bundel.tabel(["Waar", "Frans", "Let op"], [
            ["een <strong>algemene uitspraak</strong>", "<em>J'aime <strong>le</strong> chocolat.</em>",
             "wij zeggen 'ik hou van chocolade', het Frans zet er een lidwoord bij"],
            ["een <strong>landnaam</strong>", "<em><strong>la</strong> France</em>, <em>le Portugal</em>, <em>les Pays-Bas</em>",
             "een land heeft dus <strong>wél</strong> een lidwoord; een stad niet"],
            ["een <strong>beroep</strong>", "<em>Elle est <strong>infirmière</strong>.</em>",
             "na <em>être</em> valt het lidwoord juist <strong>weg</strong>: geen <em>une</em>"],
            ["een <strong>lichaamsdeel</strong>", "<em>Je me lave <strong>les</strong> mains.</em>, <em>J'ai mal à <strong>la</strong> tête.</em>",
             "het bepaald lidwoord in plaats van <em>mes</em> of <em>ma</em>"],
        ])),
        ("p", "En let op waar je heen gaat of waar je van komt: <em>je vais <strong>à la "
              "boulangerie</strong></em> (naar de <strong>bakker</strong>, de winkel) of <em>chez le "
              "boulanger</em> (bij de bakker, de persoon), <em>je vais <strong>au</strong> "
              "<strong>cinéma</strong></em>, en <em>je viens <strong>de la</strong> gare</em> (ik kom "
              "van het <strong>station</strong>), <em>je viens <strong>du</strong> magasin</em>."),
    ]),
    dict(kop="Het meervoud, en wat het lidwoord niet verraadt", blokken=[
        ("p", bundel.tabel(["Uitgang", "Meervoud", "Voorbeeld"], [
            ["<strong>-al</strong>", "<strong>-aux</strong>",
             "un <strong>journal</strong> → des <strong>journaux</strong>, un animal → des animaux, un cheval → des chevaux"],
            ["-eau, -eu", "-eaux, -eux", "un bureau → des bureaux, un jeu → des jeux"],
            ["al een -s of -x", "verandert niet", "un bus → des bus, un prix → des prix"],
            ["gewoon", "-s", "un livre → des livres"],
        ])),
        ("p", "Voor een klinker zegt het lidwoord niets meer over het geslacht: in <em>l'eau</em> "
              "zie je niet dat <em>eau</em> <strong>vrouwelijk</strong> is, al laat die <em>l'</em> "
              "iets anders <strong>vermoeden</strong>. Je merkt het pas verder in de zin: "
              "<em>l'eau est froi<strong>de</strong></em>."),
        ("p", "Een paar uitgangen helpen wel. Woorden op <strong>-age</strong> en "
              "<strong>-ment</strong> zijn meestal <strong>mannelijk</strong>: le "
              "<strong>fromage</strong>, le <strong>village</strong>, le <strong>voyage</strong>, le "
              "gouvernement (maar la page, la plage, l'image zijn vrouwelijk). Woorden op "
              "<strong>-tion</strong> en <strong>-té</strong> zijn vrouwelijk: la question, la "
              "liberté."),
        ("p", "<em>Les livres <strong>des élèves</strong></em> is <strong>de boeken van de "
              "leerlingen</strong>: bezit zeg je met <em>de</em>, en <em>de + les</em> wordt "
              "<em>des</em>."),
    ]),
    dict(kop="Chaque, quelques en de getallen", blokken=[
        ("p", bundel.tabel(["Frans", "Betekenis", "Erna komt"], [
            ["<strong>chaque</strong>", "elk, ieder", "altijd <strong>enkelvoud</strong>: <em>chaque jour</em>"],
            ["<strong>quelques</strong>", "<strong>enkele</strong>, een paar", "meervoud: <em>quelques amis</em>"],
            ["<strong>plusieurs</strong>", "verschillende", "meervoud: <em>plusieurs fois</em>"],
            ["<strong>tout le</strong>, toute la", "heel de", "enkelvoud: <em>toute la journée</em>"],
        ])),
        ("p", "Het vragende woord heeft vier vormen, en ze zijn alle vier juist "
              "<strong>geschreven</strong> als het geslacht en het getal kloppen: "
              "<strong>quel</strong>, <strong>quelle</strong>, <strong>quels</strong>, "
              "<strong>quelles</strong>. En <em>cette <strong>semaine</strong></em> is deze week: "
              "<em>semaine</em> is vrouwelijk, dus <em>cette</em>, terwijl <em>cet arbre</em> "
              "mannelijk is met een klinker."),
        ("p", bundel.tabel(["Getal", "In Frankrijk", "Let op"], [
            ["71", "<strong>soixante et onze</strong>", "met <em>et</em>; bij ons septante et un"],
            ["80", "<strong>quatre-vingts</strong>", "met een <strong>s</strong>, want vier maal twintig"],
            ["81", "quatre-vingt-un", "hier <strong>zonder</strong> s"],
            ["2000", "<strong>deux mille</strong>", "<em>mille</em> krijgt <strong>nooit</strong> een s"],
            ["200", "deux cents", "<em>cent</em> krijgt er wél een, net als vingt"],
        ])),
        ("p", "Rangtelwoorden op <strong>-ième</strong>: <strong>cinquième</strong> (de "
              "<strong>vijfde</strong>, met een u erbij), <strong>neuvième</strong> (de negende, met "
              "een v), dixième. En in een datum staat alleen de eerste in de rangvorm: <em>le "
              "<strong>premier janvier</strong></em> is 1 <strong>januari</strong>, daarna is het "
              "<em>le deux janvier</em>."),
        ("p", "De bezitters bij <em>parents</em> zijn de meervoudsvormen: <strong>mes</strong>, "
              "<strong>tes</strong>, <strong>ses</strong>, <strong>nos</strong>, <strong>vos</strong>, "
              "<strong>leurs parents</strong>. En <strong>jullie school</strong> is <em>votre "
              "école</em>."),
    ]))


def erbij_blok(sleutel, kop, *blokken):
    """Een paar blokken bij een sectie die er al staat."""
    for s in BUNDELS[sleutel + NA]["secties"]:
        if s["kop"] == kop:
            s["blokken"] = list(s["blokken"]) + list(blokken)
            return
    raise KeyError(f"{sleutel}: {kop}")


erbij_blok("lidwoorden-aanwijzers-bezitters-en-getallen", "Een deel van iets: du, de la, des",
    ("p", "Dit lidwoord heet ook het <strong>partitief</strong> lidwoord, en dat is de naam die op "
          "je examen kan staan. Je hebt het nodig zodra je over een hoeveelheid spreekt die je niet "
          "telt: <em>j'achète <strong>de la viande</strong></em>, <em>nous prenons <strong>des "
          "frites</strong></em>, <em>je bois <strong>du</strong> lait</em>. Tel je wel, dan gebruik "
          "je het onbepaalde lidwoord: <em>elle a <strong>un</strong> vélo</em>, <em>je n'ai pas "
          "<strong>de</strong> frères</em>."))

erbij_blok("voornaamwoorden-en-betrekkelijke-bijzinnen", "De wederkerende werkwoorden",
    ("p", "Nog drie die je vaak nodig hebt: <em>s'habiller</em> (zich kleden), <em>se coucher</em> "
          "(gaan slapen) en <em>se souvenir de</em> (zich herinneren). Het voornaamwoord verandert "
          "mee met de persoon: <em>je m'habille</em>, <em>elle <strong>se</strong> couche tard</em>, "
          "<em>nous nous <strong>levons</strong> tôt</em>. <em>Nous se levons</em> bestaat niet."))

erbij_blok("voornaamwoorden-en-betrekkelijke-bijzinnen", "Waar het voornaamwoord staat",
    ("p", "In een <strong>ontkenning</strong> blijft het voornaamwoord bij het werkwoord staan, "
          "dus <strong>tussen</strong> <em>ne</em> en het werkwoord en niet achter <em>pas</em>: "
          "<em>je <strong>ne le</strong> fais <strong>pas</strong></em>, <em>je ne lui parle pas</em>."))

erbij_blok("voornaamwoorden-en-betrekkelijke-bijzinnen", "Celui en le mien",
    ("p", "<em>Celui</em>, <em>celle</em>, <em>ceux</em> en <em>celles</em> heten de "
          "<strong>aanwijzende</strong> voornaamwoorden; <em>le mien</em> en <em>le nôtre</em> de "
          "bezittelijke."))

erbij_blok("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels", "Even, minder en het slechtste",
    ("p", "De drie trappen hebben ook een Franse naam, en die kan in de vraag staan: de "
          "<strong>comparatif</strong> is de vergrotende trap (<em>plus grand</em>, "
          "<em>meilleur</em>, <em>pire</em>), de <strong>superlatif</strong> de overtreffende "
          "(<em>le plus grand</em>, <em>le meilleur</em>)."),
    ("p", "En let op <em><strong>ancien</strong></em>: vóór het naamwoord betekent het "
          "<strong>vroeger</strong>, dus <em>un ancien élève</em> is een <strong>oud-leerling</strong>. "
          "Achter het naamwoord betekent het oud van jaren: <em>un meuble ancien</em> is een antiek "
          "meubel."))


erbij_blok("de-tegenwoordige-tijd-en-de-gebiedende-wijs",
    "De impératif: een bevel, een raad, een instructie",
    ("p", "De impératif is onze <strong>gebiedende</strong> wijs. Bij <em>tu</em> van een "
          "werkwoord op -er valt de s weg: <em>tu parles</em> wordt <strong>Parle !</strong> Bij "
          "<em>vous</em> eindigt hij op <strong>-ez</strong>: <em>Parlez !</em>, <em>Passez-moi le "
          "sel.</em> Van <em>être</em> is het onregelmatig: <strong>Sois !</strong>, "
          "<strong>Soyez !</strong> En bij een wederkerend werkwoord komt het voornaamwoord achteraan "
          "met een streepje: <em>se lever</em> wordt <strong>Lève-toi !</strong>"),
    ("p", "In een <strong>verboden</strong> bevel staat het voornaamwoord weer "
          "<strong>vóór</strong> het werkwoord: <em>Ne te lève pas !</em>, <em>Ne me le donne "
          "pas !</em> Dus niet achter, zoals in het gewone bevel."))

erbij_blok("de-tegenwoordige-tijd-en-de-gebiedende-wijs", "De onpersoonlijke werkwoorden",
    ("p", "<em><strong>Il faut</strong> partir <strong>maintenant</strong></em>: <em>il faut</em> "
          "betekent 'men moet' of 'het is nodig', en bestaat alleen in die ene vorm. Zo ook "
          "<em>il pleut</em>, <em>il neige</em>, <em>il y a</em>. En let op <em>depuis</em>: "
          "<em>j'habite ici <strong>depuis</strong> trois ans</em> staat in het Frans in de "
          "<strong>présent</strong>, waar wij zeggen 'ik woon hier al drie jaar'."))

erbij_blok("de-verleden-tijden", "De imparfait",
    ("p", "Je kiest de imparfait voor een <strong>beschrijving</strong> of een "
          "<strong>gewoonte</strong>: het weer, het decor, hoe iemand eruitzag, wat elke dag "
          "gebeurde. <em>Quand <strong>j'étais</strong> petit, <strong>j'habitais</strong> à "
          "Gand.</em> De passé composé neem je voor wat één keer gebeurde en afgelopen is. "
          "Vaak staan ze in één zin samen: <em>Je <strong>dormais</strong> quand le téléphone "
          "<strong>a sonné</strong>.</em>"))

erbij_blok("de-verleden-tijden", "De passé composé met être",
    ("p", "<strong>Monter, descendre, sortir, passer en rentrer wisselen van hulpwerkwoord.</strong> "
          "Zonder <strong>lijdend voorwerp</strong> nemen ze <em>être</em>: <em>elle "
          "<strong>est</strong> montée</em> (ze is naar boven gegaan). Met een lijdend voorwerp "
          "nemen ze <em>avoir</em>: <em>elle <strong>a</strong> monté la valise</em> (ze heeft de "
          "koffer naar boven gebracht). Dus niet altijd être."))

erbij("de-toekomende-tijd-en-de-conditionnel",
    dict(kop="De conditionnel: hoe je hem maakt", blokken=[
        ("p", "De conditionnel zegt wat er <strong>zou</strong> gebeuren. Je maakt hem met de "
              "<strong>stam van de futur simple</strong> (meestal de infinitief) en de "
              "<strong>uitgangen van de imparfait</strong>: -ais, -ais, -ait, -ions, -iez, -aient."),
        ("p", bundel.tabel(["Werkwoord", "Conditionnel", "Nederlands"], [
            ["parler", "je <strong>parlerais</strong>", "ik zou spreken"],
            ["être", "je <strong>serais</strong>, nous <strong>serions</strong>", "ik zou zijn, wij zouden zijn"],
            ["avoir", "j'aurais, vous <strong>auriez</strong>", "ik zou hebben"],
            ["pouvoir", "je pourrais, <strong>pourriez</strong>-vous", "ik zou kunnen, zou u kunnen"],
            ["vouloir", "je <strong>voudrais</strong>", "ik zou willen"],
            ["aimer", "<strong>j'aimerais</strong>", "ik zou graag <strong>willen</strong>"],
            ["devoir", "tu <strong>devrais</strong>", "jij zou moeten"],
            ["aller", "j'irais", "ik zou gaan"],
            ["faire", "je ferais", "ik zou doen"],
            ["venir", "je <strong>viendrais</strong>", "ik zou komen"],
        ])),
        ("kader", "<strong>Eén letter scheidt twee tijden.</strong> <em>Je "
                  "<strong>parlerai</strong></em> is de futur simple: ik zal spreken, het gebeurt. "
                  "<em>Je <strong>parlerais</strong></em> is de conditionnel: ik zou spreken, als. "
                  "Die s hoor je niet, dus hij valt in een dictee weg en op papier niet."),
        ("p", "Na <strong>si</strong> met een imparfait volgt een conditionnel: <em>Si "
              "<strong>j'étais</strong> riche, <strong>j'achèterais</strong> une "
              "<strong>maison</strong>.</em> En <em>on pourrait aller au <strong>cinéma</strong></em> "
              "betekent: we <strong>zouden</strong> naar de film kunnen gaan, dus een voorstel."),
    ]),
    dict(kop="Hoffelijk zijn met de conditionnel", blokken=[
        ("p", bundel.tabel(["Waar", "Wat je zegt"], [
            ["in een <strong>winkel</strong>", "<em>Je <strong>voudrais</strong> des <strong>croissants</strong>, s'il vous plaît.</em>"],
            ["om hulp <strong>vragen</strong>", "<em><strong>Pourriez</strong>-vous m'aider ?</em>, <em><strong>Pourriez</strong>-vous <strong>fermer</strong> la porte ?</em>"],
            ["om tijd vragen", "<em><strong>Auriez</strong>-vous une <strong>minute</strong> ?</em>"],
            ["iets <strong>reserveren</strong>", "<em>J'aimerais <strong>réserver</strong> une table.</em>"],
            ["een <strong>raad</strong> geven", "<em>Tu <strong>devrais</strong> te <strong>reposer</strong>.</em>"],
            ["in een mail aan een <strong>onbekende</strong>",
             "<em>Je vous serais <strong>reconnaissant</strong> de me répondre.</em>"],
        ])),
        ("p", "Dit is wat de fiche de <strong>conditionnel de politesse</strong> noemt: dezelfde "
              "vraag, maar met een stap afstand. <em>Je veux</em> klinkt als eisen, <em>je "
              "voudrais</em> als vragen."),
    ]))

erbij("zinsbouw-zinsdelen-en-congruentie",
    dict(kop="Elke soort zin met een voorbeeld", blokken=[
        ("p", bundel.tabel(["Soort zin", "Frans voorbeeld"], [
            ["<strong>mededelende</strong> zin", "<em>Nous allons au cinéma.</em>"],
            ["<strong>vraagzin</strong>", "<em>Est-ce que tu viens ?</em>, <em>Tu viens ?</em>, <em>Viens-tu ?</em>"],
            ["<strong>bevelzin</strong>", "<em>Ferme la porte !</em>"],
            ["<strong>uitroepzin</strong>", "<em>Quelle belle <strong>journée</strong> !</em>"],
            ["<strong>wenszin</strong>", "<em>Si <strong>seulement</strong> il <strong>faisait</strong> beau !</em>"],
            ["voorwaardelijke zin", "<em>Si tu viens, je serai content.</em>"],
        ])),
        ("p", "In een <strong>mededelende</strong> zin staat het werkwoord op de "
              "<strong>tweede plaats</strong>, net achter het onderwerp, en blijft het daar ook als "
              "er een bepaling vooraan komt: <em>Demain je <strong>vais</strong> à Paris.</em> Dat is "
              "anders dan bij ons, waar 'morgen ga ik' het onderwerp omwisselt."),
        ("p", "De drie <strong>manieren</strong> om een vraag te stellen: met de stem "
              "<strong>omhoog</strong> (<em>Tu viens ?</em>), met <em>est-ce que</em> ervoor, en door "
              "werkwoord en onderwerp om te <strong>wisselen</strong> (<em>Viens-tu ?</em>). De "
              "<strong>volgorde</strong> veranderen is dus één van de drie. <strong>Si</strong> "
              "leidt géén <strong>vraagzin</strong> in, maar een voorwaarde."),
        ("p", "Een <strong>ontkenning</strong> maak je <strong>af</strong> met pas, "
              "<strong>jamais</strong> (nooit), rien (niets), personne (niemand) of plus (niet meer): "
              "<em>je ne vais <strong>jamais</strong> là</em>."),
    ]),
    dict(kop="Voegwoorden, bijzinnen en de overeenkomst", blokken=[
        ("p", "<strong>Et, ou, mais</strong> en <strong>donc</strong> <strong>verbinden</strong> "
              "twee gelijke delen: dan heb je twee <strong>hoofdzinnen</strong> in één zin "
              "(<em>Je mange et il boit.</em>). <strong>Parce que, quand, si</strong> en "
              "<strong>pendant que</strong> maken van het tweede deel een bijzin."),
        ("p", bundel.tabel(["Voegwoord", "Betekenis"], [
            ["<strong>quand</strong>", "wanneer, toen"],
            ["<strong>pendant que</strong>", "<strong>terwijl</strong>, <strong>tijdens</strong> dat"],
            ["<strong>parce que</strong>", "omdat"],
            ["<strong>pour que</strong>", "zodat; het werkwoord erna verandert van vorm: <em>pour qu'il <strong>comprenne</strong></em>"],
            ["<strong>si</strong>", "als, indien"],
        ])),
        ("p", "Een <strong>bijzin</strong> met <em>quand</em> kan ook <strong>vooraan</strong> "
              "staan: <em><strong>Quand</strong> il pleut, je reste à la maison.</em> Hij hoeft dus "
              "niet achteraan. Een <strong>betrekkelijke</strong> <strong>bijzin</strong> hangt aan "
              "een woord: <em>la fille qui <strong>chante</strong> est ma sœur.</em>"),
        ("p", bundel.tabel(["Zinsdeel", "In de zin", "Voorbeeld"], [
            ["onderwerp", "wie of wat doet het", "<em><strong>Les enfants</strong> jouent.</em>"],
            ["COD", "zonder voorzetsel", "<em>Il donne <strong>le livre</strong>.</em>"],
            ["<strong>COI</strong>", "met <strong>à</strong>", "<em>Il <strong>téléphone</strong> à sa mère.</em>"],
            ["bepaling van tijd", "wanneer", "<em><strong>Demain</strong> je vais à Paris.</em>"],
            ["bepaling van plaats", "waar", "<em>Je vais <strong>à Paris</strong>.</em>"],
        ])),
        ("p", "Werkwoorden die een <strong>COI met à</strong> vragen: <strong>parler</strong> à, "
              "<strong>téléphoner</strong> à, <strong>ressembler</strong> à, écrire à, répondre à, "
              "demander à. In <em>il donne à son frère</em> <strong>ontbreekt</strong> dus het "
              "<strong>COD</strong>: wát geeft hij? Een bepaling van tijd staat niet altijd "
              "achteraan: ze mag ook vooraan."),
        ("p", "De drie soorten <strong>congruentie</strong>: het werkwoord met het onderwerp "
              "(<em>Les <strong>enfants</strong> <strong>sont</strong> contents.</em>), het "
              "<strong>bijvoeglijk</strong> naamwoord met zijn naamwoord (<em>mes "
              "<strong>grandes</strong> <strong>sœurs</strong></em>, dus het <strong>krijgt</strong> "
              "wel een s in het meervoud), en het deelwoord na être. Een onderwerp als <em>ma sœur "
              "et moi</em> is <strong>wij</strong>: <em>ma sœur et moi <strong>allons</strong> au "
              "<strong>cinéma</strong></em>. En <em><strong>beaucoup d'élèves</strong> "
              "<strong>sont</strong> <strong>absents</strong></em> staat in het meervoud, want het "
              "gaat over veel leerlingen."),
    ]))


erbij("de-tegenwoordige-tijd-en-de-gebiedende-wijs",
    dict(kop="Nog een rij werkwoorden die vaak terugkomen", blokken=[
        ("p", bundel.tabel(["Werkwoord", "De vormen die opvallen", "Waarom"], [
            ["<strong>boire</strong>", "je bois, nous <strong>buvons</strong>, ils boivent",
             "de stam verandert helemaal in het meervoud"],
            ["<strong>manger</strong>", "nous <strong>mangeons</strong>",
             "een <strong>e</strong> na de g, anders klinkt het als 'mangons'"],
            ["<strong>commencer</strong>", "nous commençons", "een cedille om de s-klank te houden"],
            ["<strong>acheter</strong>", "j'achète maar nous <strong>achetons</strong>",
             "het <strong>accent</strong> grave staat er net <strong>niet</strong> bij nous en vous"],
            ["<strong>ouvrir</strong>", "j'ouvre, elles <strong>ouvrent</strong>",
             "eindigt op -ir maar vervoegt als een werkwoord op -er"],
            ["<strong>s'asseoir</strong>", "je m'assieds, vous vous <strong>asseyez</strong>",
             "onregelmatig én wederkerend"],
            ["<strong>vouloir</strong>", "je veux, ils <strong>veulent</strong>", "drie stammen"],
            ["<strong>savoir</strong>", "je sais, tu <strong>sais</strong>, nous savons", "geen -t bij tu"],
            ["<strong>venir</strong>", "je viens tegenover nous venons",
             "de klank <strong>verandert</strong> in het enkelvoud: vièn tegenover venons"],
            ["<strong>faire</strong>", "il <strong>fait</strong> du vélo <strong>chaque</strong> jour",
             "<em>faire du vélo</em> is fietsen"],
        ])),
        ("p", "Een vorm bij <em>on</em> is <strong>dezelfde</strong> als bij <em>il</em> en "
              "<em>elle</em>: <em>on va</em>, <em>on fait</em>, <em>on est</em>."),
        ("p", "Vijf werkwoorden zijn in het Frans wederkerend terwijl ze dat bij ons niet zijn: "
              "<em>se <strong>coucher</strong></em> (gaan slapen), <em>se <strong>promener</strong></em> "
              "(wandelen), <em>se lever</em> (opstaan), <em>se reposer</em> (rusten) en <em>se "
              "<strong>souvenir</strong> de</em> (zich <strong>herinneren</strong>)."),
    ]))

erbij("de-verleden-tijden",
    dict(kop="De deelwoorden die je uit het hoofd moet kennen", blokken=[
        ("p", bundel.tabel(["Werkwoord", "Deelwoord", "Werkwoord", "Deelwoord"], [
            ["avoir", "eu", "<strong>pouvoir</strong>", "<strong>pu</strong>"],
            ["être", "été", "vouloir", "voulu"],
            ["faire", "fait", "<strong>ouvrir</strong>", "<strong>ouvert</strong>"],
            ["prendre", "pris", "mettre", "mis"],
            ["voir", "vu", "écrire", "écrit"],
            ["lire", "lu", "dire", "dit"],
            ["venir", "venu", "boire", "bu"],
        ])),
        ("p", "<em>Elle a <strong>ouvert</strong> la porte</em>: met <em>avoir</em> blijft het "
              "deelwoord onveranderd. Met <em>être</em> gaat het mee met het onderwerp: <em>elle est "
              "<strong>partie</strong></em>, <em>ils sont partis</em>."),
        ("p", "Een <strong>voornaamwoord</strong> staat in de passé composé <strong>voor het "
              "hulpwerkwoord</strong>, niet voor het deelwoord: <em>je <strong>l'ai</strong> vu</em>, "
              "<em>il <strong>me l'a</strong> donné</em>."),
    ]),
    dict(kop="De imparfait in vormen", blokken=[
        ("p", "De uitgangen zijn voor élk werkwoord dezelfde: -ais, -ais, -ait, -ions, -iez, "
              "-aient. Je vertrekt van de stam van <em>nous</em> in de présent."),
        ("p", bundel.tabel(["Werkwoord", "nous in de présent", "Imparfait"], [
            ["aller", "nous allons", "nous <strong>allions</strong>, ils <strong>allaient</strong>"],
            ["prendre", "nous prenons", "nous <strong>prenions</strong>"],
            ["faire", "nous faisons", "nous <strong>faisions</strong>"],
            ["avoir", "nous avons", "ils <strong>avaient</strong>, j'avais"],
            ["être", "onregelmatig", "j'étais, nous étions"],
            ["manger", "nous mangeons", "je <strong>mangeais</strong>, met de <strong>e</strong> na de g"],
        ])),
        ("p", "Vier woorden <strong>wijzen</strong> bijna altijd naar de imparfait: "
              "<strong>souvent</strong>, <strong>toujours</strong>, <strong>chaque</strong> jour of "
              "<strong>chaque</strong> <strong>dimanche</strong>, en <em>d'habitude</em>. <em>Nous "
              "<strong>allions</strong> au parc chaque dimanche</em> en <em>je "
              "<strong>jouais</strong> au foot chaque <strong>samedi</strong></em> "
              "<strong>vertellen</strong> dus een gewoonte uit het verleden."),
        ("p", "In een <strong>verhaal</strong> staat het decor in de imparfait en gebeurt de "
              "handeling in de passé composé: <em>il <strong>lisait</strong> quand le téléphone a "
              "sonné</em>. Dat is de goede <strong>plaats</strong> voor de twee "
              "<strong>tijden</strong>: eerst wat bezig was, dan wat gebeurde."),
        ("p", "En <strong>depuis</strong> hoort niet bij een verleden tijd: <em>j'habite ici "
              "<strong>depuis</strong> trois ans</em> staat in de présent, want het duurt nog."),
    ]))

erbij_blok("de-toekomende-tijd-en-de-conditionnel", "De futur simple",
    ("p", bundel.tabel(["Werkwoord", "Onregelmatige stam", "Futur simple"], [
        ["être", "ser-", "je serai"],
        ["avoir", "aur-", "j'aurai"],
        ["aller", "ir-", "j'irai"],
        ["faire", "fer-", "je ferai"],
        ["venir", "viendr-", "je viendrai"],
        ["pouvoir", "pourr-", "je pourrai"],
        ["vouloir", "voudr-", "je voudrai"],
        ["<strong>savoir</strong>", "saur-", "je <strong>saurai</strong>"],
        ["voir", "verr-", "je verrai"],
        ["devoir", "devr-", "je devrai"],
    ])),
    ("p", "Alle andere werkwoorden nemen gewoon de infinitief: <em>parler</em> → <em>je "
          "parlerai</em>, <em>finir</em> → <em>je finirai</em>. Bij een infinitief op -re valt de e "
          "weg: <em>prendre</em> → <em>je prendrai</em>."))


erbij_blok("de-toekomende-tijd-en-de-conditionnel", "De futur proche: aller + infinitief",
    ("p", "<em>Nous <strong>allons</strong> <strong>partir</strong></em>, <em>je vais "
          "<strong>regarder</strong> la télé</em>: dat is een plan voor <strong>straks</strong>, en "
          "dus kies je <strong>eerder</strong> de futur proche dan de futur simple. In de "
          "<strong>ontkenning</strong> staan <em>ne</em> en <em>pas</em> rond <em>aller</em>, niet "
          "rond de infinitief: <em>je <strong>ne</strong> vais <strong>pas</strong> "
          "<strong>sortir</strong></em>."))

erbij_blok("de-toekomende-tijd-en-de-conditionnel", "De futur simple",
    ("p", "Na <strong>si</strong> met een présent volgt de futur: <em>Si tu viens, je "
          "<strong>serai</strong> <strong>content</strong>.</em> Een futur meteen na <em>si</em> "
          "schrijf je niet."),
    ("p", "En een <strong>accent</strong> dat je in de présent hebt, blijft in de futur staan: "
          "<em>j'achète</em> wordt <em>j'<strong>achèterai</strong></em>. Het "
          "<strong>verdwijnt</strong> dus niet."))

erbij_blok("zinsbouw-zinsdelen-en-congruentie", "Voegwoorden, bijzinnen en de overeenkomst",
    ("p", "<em>Parle plus <strong>lentement</strong> pour qu'il <strong>comprenne</strong></em> is "
          "de juiste vorm met <em>pour que</em>: het werkwoord erna krijgt die aparte vorm, en dat "
          "leer je als vaste wending. Een voornaamwoord dat een <strong>COD</strong> "
          "<strong>vervangt</strong>, staat <strong>voor het werkwoord</strong>: <em>je "
          "<strong>le</strong> vois</em>. En <em>mes grandes <strong>sœurs</strong> sont "
          "arrivées</em> klopt qua congruentie: naamwoord, bijvoeglijk naamwoord en deelwoord gaan "
          "alle drie mee."))
