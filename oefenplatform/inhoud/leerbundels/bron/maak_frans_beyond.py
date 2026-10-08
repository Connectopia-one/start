# -*- coding: utf-8 -*-
"""De leerbundels en oefenbundels voor Frans op 🌍 Beyond-niveau.

Gebaseerd op de vakfiches Frans 1 en Frans 2 van de derde graad
doorstroomfinaliteit, geldig vanaf 1 januari 2027. Allebei gelden ze voor
humane wetenschappen, Latijn-wiskunde met extra wetenschappen,
wiskunde-wetenschappen en economie-wiskunde. Het ERK-niveau is B1+, een stap
hoger dan de B1 van 🚀 Boost.

Frans 1 is een digitaal examen van 120 minuten, half lezen en half luisteren.
Frans 2 bestaat uit een spreekopdracht die je thuis opneemt, twee
schrijfopdrachten op het digitale examen en een gesprek van tien minuten;
schrijven en schriftelijke interactie wegen daar elk 29 %, literatuurbeleving
4 %.

Deze bundels dragen wat een platform met tekstvragen kán dragen: lezen,
schrijven, schriftelijke interactie, literatuurbeleving, en de woordenschat en
de grammatica die daarachter liggen. Luisteren, spreken en het gesprek staan er
niet in, en daarom staat in elke bundel achteraan hetzelfde kader dat de
leerling daar zelf naartoe stuurt.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde
leerstof met andere vragen, dus Kim laadt dezelfde bundel twee keer op.

De bundelsleutels eindigen op "-beyond", de naam van de categorie. Dat
achtervoegsel is nodig omdat de themanamen van Beyond botsen met die van
🚀 Boost.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Frans"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
NA = "-beyond"
tabel = bundel.tabel

BUNDELS = {}


def spreken(opdracht):
    """Het vaste slotkader over wat je niet achter een scherm leert."""
    return dict(kop="Oefen dit ook buiten het scherm", blokken=[
        ("p", "Op dit platform oefen je lezen, woordenschat en grammatica. Maar <strong>luisteren</strong> "
              "is de helft van het examen Frans 1, en Frans 2 bestaat uit <strong>een spreekopdracht die "
              "je thuis opneemt</strong>, twee schrijfopdrachten en <strong>een gesprek van tien "
              "minuten</strong>. Luisteren en spreken leer je niet achter een scherm. Je leert ze door te "
              "luisteren naar mensen die echt Frans spreken, en door zelf je mond open te doen, ook als "
              "het hakkelt."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer, en let daarna op wat je "
                  "miste of niet gezegd kreeg. Dat is precies je volgende oefening."),
    ])


def zet(sleutel, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    BUNDELS[sleutel + NA] = b


# ───────────────────────── 1. Een Franse tekst analyseren
zet("een-franse-tekst-analyseren",
    titel="Een Franse tekst analyseren",
    onder="Onderwerp, hoofdgedachte en hoofdpunten, gericht zoeken, de signaalwoorden en de verwijswoorden, en een onbekend woord uit de context halen.",
    secties=[
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Drie woorden die op elkaar lijken en die je uit elkaar moet houden. "
                  "<strong>De hoofdgedachte van een tekst is niet hetzelfde als het onderwerp.</strong>"),
            ("p", tabel(["", "hoe lang", "voorbeeld"],
                        [["het onderwerp", "enkele woorden", "uitleenfietsen in Lyon"],
                         ["de hoofdgedachte", "een hele zin", "Te weinig slaap is slecht voor het hart."],
                         ["de hoofdpunten", "de zinnen eronder", "wat de hoofdgedachte ondersteunt"]])),
            ("p", "Lees: <em>Depuis janvier, la ville de Lyon prête des vélos électriques aux habitants "
                  "qui n'ont pas de voiture. Mille personnes ont déjà fait la demande.</em> Het onderwerp "
                  "in enkele woorden: <strong>uitleenfietsen in Lyon</strong>."),
            ("p", "Lees: <em>Dormir moins de six heures par nuit augmente le risque de maladies du cœur. "
                  "Les chercheurs conseillent donc de se coucher plus tôt.</em> De hoofdgedachte is een "
                  "hele zin: <strong>te weinig slaap is slecht voor het hart</strong>."),
            ("p", "Lees: <em>Ce roman raconte l'histoire d'une famille belge pendant la guerre. L'auteur "
                  "s'est inspiré du journal de sa grand-mère.</em> De hoofdpunten: <strong>het boek gaat "
                  "over een Belgisch gezin</strong>, <strong>het verhaal speelt tijdens de oorlog</strong> "
                  "en <strong>de schrijver gebruikte een dagboek</strong>."),
            ("kader", "<strong>Bij een leesvraag mag je het antwoord niet halen uit wat je zelf al over "
                      "het onderwerp weet, zeker niet als het de tekst tegenspreekt.</strong> En "
                      "<strong>de titel, de tussentitels en de foto bij een tekst mag je niet "
                      "overslaan</strong>: ze horen er wel degelijk bij."),
            ("p", "Vooraf stel je met het communicatiemodel drie vragen: <strong>van wie is de "
                  "tekst?</strong>, <strong>waarom is hij gemaakt?</strong> en <strong>voor wie is hij "
                  "bedoeld?</strong>"),
        ]),
        dict(kop="Gericht zoeken", blokken=[
            ("p", tabel(["de zin", "de vraag", "het antwoord"],
                        [["Le musée est fermé le mardi.", "welke dag gesloten?", "mardi"],
                         ["Le colis arrivera entre 14 h et 16 h.", "ten vroegste?", "14 h"],
                         ["L'entrée est gratuite pour les moins de 12 ans.", "tot welke leeftijd?", "12"],
                         ["Il ne reste plus que deux places.", "hoeveel plaatsen vrij?", "nog maar twee"]])),
            ("p", "Lees: <em>Le train de 7 h 12 a été supprimé. Les voyageurs doivent prendre le bus de "
                  "remplacement devant la gare.</em> Drie dingen staan er: <strong>de trein rijdt "
                  "niet</strong>, <strong>er staat een vervangbus klaar</strong> en <strong>de bus "
                  "vertrekt voor het station</strong>."),
            ("p", "Lees: <em>Les élèves de terminale passent le bac en juin.</em> Dat gaat over "
                  "<strong>leerlingen van het laatste jaar</strong>: <em>la terminale</em> is in Frankrijk "
                  "het laatste jaar van het middelbaar."),
            ("p", "Lees: <em>Ce guide s'adresse aux parents d'enfants à haut potentiel.</em> De gids is "
                  "bedoeld <strong>voor ouders van hoogbegaafde kinderen</strong>. En <em>Attention : ce "
                  "produit contient des arachides</em> is vooral belangrijk <strong>voor wie allergisch is "
                  "aan noten</strong>."),
        ]),
        dict(kop="Tussen de regels lezen", blokken=[
            ("p", tabel(["de zin", "wat ze zegt"],
                        [["Il n'a pas été nécessaire d'annuler le concert.", "het concert ging door"],
                         ["La bibliothèque sera exceptionnellement ouverte dimanche.", "bij uitzondering"],
                         ["Faute de bénévoles, la fête n'aura pas lieu.",
                          "er zijn te weinig vrijwilligers"],
                         ["Le film, pourtant primé à Cannes, n'a attiré que peu de spectateurs.",
                          "een prijs, maar weinig volk"],
                         ["Les travaux dureront jusqu'à la fin du mois, sauf en cas de pluie.",
                          "bij regen kan het langer duren"]])),
            ("p", "Let op <em>faute de</em> (bij gebrek aan) en <em>sauf en cas de</em> (behalve bij). "
                  "Twee kleine uitdrukkingen die het hele antwoord dragen."),
            ("p", "Lees: <em>Selon l'auteur, les réseaux sociaux ne sont pas responsables de tout.</em> "
                  "Het standpunt: <strong>sociale media krijgen te veel de schuld</strong>."),
            ("p", "Lees: <em>Je vous écris afin de vous signaler une erreur dans ma facture et de demander "
                  "un remboursement.</em> Drie dingen kloppen: <strong>de schrijver meldt een "
                  "fout</strong>, <strong>de schrijver vraagt geld terug</strong> en <strong>de mail gaat "
                  "over een factuur</strong>."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", tabel(["signaalwoord", "verband"],
                        [["pourtant, en revanche, alors que", "een tegenstelling"],
                         ["donc, par conséquent, c'est pourquoi, du coup", "een gevolg"],
                         ["car, parce que", "een reden"],
                         ["bien que", "een toegeving"],
                         ["d'abord, ensuite, enfin", "een volgorde in de tijd"],
                         ["par exemple, notamment, ainsi", "een voorbeeld"],
                         ["en effet", "een onderbouwing van wat er net stond"]])),
            ("p", "Een gevolg kondigen <strong>donc</strong>, <strong>par conséquent</strong> en "
                  "<strong>c'est pourquoi</strong> aan. Het woord van twee letters dat dus betekent, is "
                  "<strong>donc</strong>."),
            ("p", "<strong>Het woord <em>car</em> kondigt geen gevolg aan maar een reden</strong>: het is "
                  "hetzelfde als <em>parce que</em>. Verwar het niet met <em>donc</em>, dat precies de "
                  "andere kant op wijst."),
            ("p", "<em>Pourtant</em> legt <strong>een tegenstelling</strong>, en <em>alors que</em> in "
                  "<em>Alors que le Nord connaît la sécheresse, le Sud est inondé</em> ook. <em>En "
                  "revanche</em> zegt <strong>daar staat iets tegenover</strong>, en <em>bien que</em> in "
                  "<em>Bien qu'il soit fatigué, il continue à travailler</em> legt <strong>een "
                  "toegeving</strong>. Let op: na <em>bien que</em> staat altijd de subjonctif."),
            ("p", "<em>D'abord, on prépare la pâte. Ensuite, on ajoute les œufs. Enfin, on met le plat au "
                  "four.</em> Die woorden leggen <strong>een volgorde in de tijd</strong>. <strong>De "
                  "woorden <em>par exemple</em>, <em>notamment</em> en <em>ainsi</em> kondigen een "
                  "voorbeeld aan.</strong>"),
            ("p", "Lees: <em>Les jeunes lisent moins qu'avant. En effet, une enquête montre que…</em> De "
                  "tweede zin <strong>onderbouwt de eerste</strong>. En <em>Il a raté son train. Du coup, "
                  "il est arrivé en retard</em>: <em>du coup</em> betekent hier <strong>daardoor</strong>."),
            ("p", "<strong>Een alinea in een argumentatieve tekst kan de functie hebben om een "
                  "tegenargument te weerleggen.</strong> Zo'n alinea begint vaak met <em>certes</em> of "
                  "<em>on pourrait objecter que</em>, en draait daarna met <em>mais</em>."),
        ]),
        dict(kop="Verwijswoorden", blokken=[
            ("p", tabel(["de zinnen", "het woordje", "waarnaar"],
                        [["Marie a appelé son frère. Il n'a pas répondu.", "il", "naar de broer van Marie"],
                         ["Je n'aime pas les épinards. Mon frère, lui, en mange tous les jours.", "en",
                          "naar de spinazie"],
                         ["Ce que je retiens surtout, c'est son courage.", "ce que",
                          "naar de moed verder in de zin"]])),
            ("p", "Het woordje <strong>en</strong> vervangt iets met <em>de</em> erbij: <em>il en mange</em> "
                  "is <em>il mange des épinards</em>. Het is klein en makkelijk over het hoofd te zien, en "
                  "juist daarom vaak de sleutel van een leesvraag."),
        ]),
        dict(kop="Een onbekend woord", blokken=[
            ("p", "De fiche geeft drie manieren om een onbekend woord aan te pakken: <strong>de betekenis "
                  "uit de context afleiden</strong>, <strong>letten op hoe het woord gevormd is</strong>, "
                  "en <strong>je voorkennis en andere talen gebruiken</strong>."),
            ("p", "Lees: <em>Ce livre est illisible.</em> Je leidt het af <strong>uit <em>lire</em> plus de "
                  "ontkenning <em>il-</em></strong>: niet te lezen. En <em>Le réchauffement climatique "
                  "s'accélère</em>: <em>réchauffement</em> betekent <strong>opwarming</strong>, van "
                  "<em>chaud</em>."),
            ("p", tabel(["deel", "wat het doet", "voorbeeld"],
                        [["in-, im-, il-, ir-", "maakt het tegendeel", "incorrect, impossible, illisible"],
                         ["re-, ré-", "opnieuw", "refaire, réchauffer"],
                         ["-able, -ible", "het kan gedaan worden", "faisable, lisible"],
                         ["-ment", "maakt er een bijwoord van", "lentement"],
                         ["-eur, -euse", "de persoon die het doet", "chanteur, chanteuse"]])),
        ]),
        spreken("luister vijftien minuten naar een Franstalige podcast of radiozender over iets wat je "
                "toch al interesseert, en vertel daarna in het Frans waar het over ging."),
    ])


# ───────────────────────── 2. Tekstsoorten en de bedoeling van een tekst
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    titel="Tekstsoorten en de bedoeling van een tekst",
    onder="De zeven tekstsoorten van de fiche, feit tegenover mening, formeel tegenover informeel, en voor wie een tekst gemaakt is.",
    secties=[
        dict(kop="De zeven tekstsoorten", blokken=[
            ("p", tabel(["soort", "wat hij doet", "voorbeeld"],
                        [["informatief", "informatie geven", "een krantenartikel, een interview"],
                         ["prescriptief", "zeggen wat je moet doen", "een recept, een handleiding"],
                         ["persuasief", "je gedrag veranderen", "een reclamespot, een campagne"],
                         ["argumentatief", "een stelling met argumenten staven", "een opiniestuk"],
                         ["narratief", "feiten verhalend weergeven", "een reisverslag, een getuigenis"],
                         ["opiniërend", "zeggen wat de schrijver vindt", "een recensie"],
                         ["literair", "iets maken met taal", "een roman, een gedicht, een strip"]])),
            ("p", "De tekst die vooral informatie wil geven, is <strong>een informatieve tekst</strong>. "
                  "Een tekst die je van iets wil overtuigen of je gedrag wil veranderen, is "
                  "<strong>persuasief</strong>. Een tekst die feiten en gebeurtenissen verhalend weergeeft, "
                  "is <strong>narratief</strong>."),
            ("p", "<strong>Een argumentatieve tekst voert argumenten aan om een stelling te "
                  "ondersteunen.</strong> <strong>Eén tekst kan tot meer dan één van de zeven soorten "
                  "horen</strong>: een reisverslag is narratief en informatief tegelijk."),
            ("p", tabel(["de tekst", "de soort"],
                        [["Mélangez la farine et le beurre, puis laissez reposer la pâte.", "prescriptief"],
                         ["Ce restaurant est une véritable déception : service lent et plats froids.",
                          "opiniërend"],
                         ["Et soudain, le silence. La pluie avait cessé de tomber…", "literair"],
                         ["Avis aux habitants : la collecte des déchets est reportée à jeudi.",
                          "een informatieve mededeling"],
                         ["Interdire les voitures en ville ? Trois raisons de ne pas le faire.",
                          "argumentatief"]])),
            ("p", "Volgens de fiche zijn <strong>een reisverslag</strong>, <strong>een getuigenis</strong> "
                  "en <strong>een videoblog</strong> narratief, en zijn <strong>een krantenartikel</strong>, "
                  "<strong>een interview</strong> en <strong>een nieuwsitem</strong> informatief. "
                  "<strong>Een strip en een cartoon horen bij de literaire teksten.</strong>"),
            ("p", "<strong>Een reclamespot is geen informatieve tekst</strong>, al geeft hij informatie "
                  "over een product: zijn bedoeling is je iets te doen kopen, dus hij is persuasief."),
            ("p", "Een prescriptieve tekst herken je snel <strong>aan de imperatief</strong>, <strong>aan "
                  "de stappen in volgorde</strong> en <strong>soms aan een infinitief</strong> "
                  "(<em>mélanger, laisser reposer</em>, zoals in veel Franse recepten)."),
        ]),
        dict(kop="De bedoeling", blokken=[
            ("p", tabel(["de tekst", "de bedoeling"],
                        [["Roulez moins vite. Chaque année, la vitesse tue 300 personnes.",
                          "je gedrag veranderen"],
                         ["Ce documentaire montre comment vivent les derniers bergers des Pyrénées.",
                          "je iets laten zien en bijbrengen"],
                         ["À mon avis, l'école devrait commencer plus tard. Les adolescents dorment trop peu.",
                          "een mening met een reden geven"],
                         ["Comment réussir son entretien d'embauche en cinq étapes.", "een stappenplan"],
                         ["Vous êtes nombreux à nous avoir écrit. Voici nos réponses.",
                          "antwoorden op lezersvragen"]])),
            ("p", "Een <strong>avis</strong> is een aankondiging of mededeling, zoals in <em>avis aux "
                  "habitants</em>. En <em>Chers voyageurs, veuillez composter votre billet avant de "
                  "monter</em> betekent: <strong>je ticket afstempelen</strong> voor je opstapt."),
            ("p", "De elementen die je helpen de soort te bepalen: <strong>de titel en de "
                  "tussentitels</strong>, <strong>de plaats waar hij verscheen</strong> en <strong>de "
                  "werkwoordstijden erin</strong>. <strong>De passé simple kom je in het Frans vooral "
                  "tegen in verhalende en literaire teksten</strong>, bijna nooit in spreektaal."),
        ]),
        dict(kop="Feit of mening", blokken=[
            ("p", "<strong>Het verschil tussen een feit en een mening: een feit kan je nagaan.</strong>"),
            ("p", "Lees: <em>Le musée a accueilli 120 000 visiteurs. C'est un succès incroyable.</em> "
                  "<strong>De eerste zin is een feit</strong>, <strong>de tweede zin is een mening</strong>, "
                  "en <strong>het cijfer kan je nagaan</strong>. Twee zinnen naast elkaar, twee heel "
                  "verschillende soorten uitspraak."),
            ("p", tabel(["uitdrukking", "wat ze aankondigt"],
                        [["à mon avis, selon moi", "een persoonlijke mening"],
                         ["il est prouvé que", "een feit"],
                         ["le gouvernement aurait décidé", "nog niet bevestigd: de conditionnel"]])),
            ("p", "De uitdrukking van drie woorden die naar mijn mening betekent, is <strong>à mon "
                  "avis</strong>. De uitdrukking die een feit aankondigt, is <strong>il est prouvé "
                  "que</strong>."),
            ("p", "Lees: <em>Le gouvernement aurait décidé de reporter la réforme.</em> Die conditionnel "
                  "zegt <strong>het is nog niet bevestigd</strong>. Dat is in de Franse pers een vaste "
                  "manier om iets te melden waar nog geen bevestiging van is: <em>le conditionnel "
                  "journalistique</em>."),
            ("p", "<strong>In een krantenartikel kan naast feiten ook de mening van de journalist "
                  "staan.</strong> En <strong>een tekst met veel cijfers en bronvermeldingen is daarom "
                  "niet automatisch objectief</strong>: ook een selectie van ware cijfers kan sturen."),
            ("p", "Lees: <em>Ni l'un ni l'autre candidat ne convainc vraiment.</em> De schrijver vindt "
                  "<strong>dat geen van beide kandidaten overtuigt</strong>."),
        ]),
        dict(kop="Formeel of informeel", blokken=[
            ("p", "<strong>Tegen een onbekende volwassene gebruik je <em>vous</em>.</strong> Dat is in het "
                  "Frans geen beleefdheidsdetail maar de regel."),
            ("p", "Je merkt dat een tekst formeel is <strong>aan de vous-vorm</strong>, <strong>aan de "
                  "volledige zinnen</strong> en <strong>aan vaste beleefdheidsformules</strong>. <em>Monsieur "
                  "le Directeur, je me permets de vous écrire au sujet de…</em> zegt meteen: <strong>het "
                  "is een formele brief</strong>."),
            ("p", "Lees: <em>Salut ! T'as vu le match hier soir ? C'était dingue !</em> Daaraan valt op "
                  "dat <strong>het spreektaal is</strong>: <em>salut</em>, de weggelaten <em>ne</em>, "
                  "<em>t'as</em> in plaats van <em>tu as</em>, en <em>dingue</em>. <strong>Het woord "
                  "<em>dingue</em> past niet in een formele brief.</strong>"),
            ("p", "Het is nuttig te weten voor wie een tekst bedoeld is, <strong>omdat dat de toon en de "
                  "woordkeuze verklaart</strong>. De lezer of hoorder voor wie een tekst bedoeld is, heet "
                  "in het Frans de <strong>destinataire</strong>."),
            ("p", "Lees: <em>Ce téléphone ? Le meilleur de tous les temps, à un prix imbattable !</em> Wat "
                  "de bedoeling verraadt, zijn <strong>de overdreven superlatieven</strong>."),
        ]),
        spreken("lees één Franstalig opiniestuk en zeg daarna hardop in het Frans, in drie zinnen, wat de "
                "schrijver vindt en of je het ermee eens bent."),
    ])


# ───────────────────────── 3. De Franstalige wereld: omgangsvormen en gewoontes
zet("de-franstalige-wereld-omgangsvormen-en-gewoontes",
    titel="De Franstalige wereld: omgangsvormen en gewoontes",
    onder="Tutoyeren of vousvoyeren, hoffelijk vragen, de Franstalige wereld, en de gewoontes die je tekst of gesprek doen kloppen.",
    secties=[
        dict(kop="Tu of vous", blokken=[
            ("p", "<strong>Tegen een onbekende volwassene gebruik je <em>vous</em>.</strong> In een Franse "
                  "winkel spreek je een verkoopster die je niet kent dus aan met <em>vous</em>, en "
                  "<strong>in een mail aan een leraar met wie je geen nauwe band hebt gebruik je ook de "
                  "vous-vorm</strong>. Iemand met <em>vous</em> aanspreken heet <strong>vouvoyer</strong>."),
            ("p", "<strong>Zeg altijd eerst <em>bonjour</em></strong> als je een onbekende om een "
                  "inlichting vraagt. In Frankrijk is dat geen beleefd extraatje maar het minimum: wie "
                  "zonder bonjour begint, komt onbeschoft over, hoe correct zijn Frans verder ook is."),
            ("p", "Zegt een Fransman <em>on se tutoie ?</em>, dan <strong>stelt hij voor om <em>tu</em> te "
                  "gebruiken</strong>. Dat voorstel komt van de oudste of de hoogste in rang; jij wacht "
                  "het af."),
            ("p", "Onder vrienden hoort bij een Franse begroeting <strong>la bise, een kus op de "
                  "wang</strong>, <strong><em>salut</em> of <em>coucou</em> zeggen</strong> en <strong>van "
                  "bij de eerste keer tutoyeren</strong>. <strong>Mensen die elkaar goed kennen geven "
                  "elkaar bij het begroeten vaak een kus op de wang.</strong>"),
        ]),
        dict(kop="Hoffelijk vragen", blokken=[
            ("p", "De <strong>conditionnel de politesse</strong> is <strong>een hoffelijke vorm met "
                  "<em>voudrais</em> of <em>pourriez</em></strong>. Hij maakt van een eis een vraag."),
            ("p", tabel(["te direct", "hoffelijk"],
                        [["Je veux un café.", "Je voudrais un café, s'il vous plaît."],
                         ["Aidez-moi.", "Pourriez-vous m'aider ?"],
                         ["Vous avez un instant ?", "Est-ce que vous auriez un instant ?"],
                         ["Dites-moi si…", "Je voudrais savoir si…"]])),
            ("p", "<strong><em>Je veux un café</em> is in een Frans café niet de meest hoffelijke manier "
                  "om iets te vragen.</strong> <em>Je veux</em> klinkt als een bevel; <em>je voudrais</em> "
                  "is de gewone vorm."),
            ("p", "Bel je een Frans bedrijf, dan zeg je: <strong>Bonjour, pourrais-je parler à madame "
                  "Leroy ?</strong> Begrijp je iemand niet, dan zeg je <strong>Pardon, pourriez-vous "
                  "répéter ?</strong> Op <em>merci</em> antwoord je met <strong>de rien</strong> of "
                  "<em>pas de quoi</em>."),
            ("p", "Een gewone zakelijke mail sluit je af met <strong>cordialement</strong>; een formele "
                  "brief met <strong>Veuillez agréer mes salutations distinguées.</strong> De aanhef aan "
                  "een directeur die je niet kent, is <strong>Monsieur le Directeur,</strong>"),
        ]),
        dict(kop="In gesprek blijven", blokken=[
            ("p", "Bij hoffelijke lichaamstaal in een Frans gesprek hoort <strong>de ander aankijken "
                  "terwijl hij spreekt</strong>, <strong>een hand geven bij een eerste ontmoeting</strong> "
                  "en <strong>knikken om te laten zien dat je volgt</strong>."),
            ("p", "Naar iemands mening vraag je met <strong>Qu'en pensez-vous ?</strong>, en je toont "
                  "interesse met <strong>Et vous, qu'est-ce que vous en pensez ?</strong> Een gesprek is "
                  "geen beurtrol van twee monologen: de vraag terug is wat het gaande houdt."),
            ("kader", "<strong>Zit je vast in het Frans, dan is stoppen met spreken juist het slechtste "
                      "wat je kan doen.</strong> Zeg <em>comment dire…</em>, <em>c'est-à-dire…</em> of "
                      "<em>je cherche le mot</em>, omschrijf het woord dat je niet vindt, of vraag "
                      "<em>comment on dit… ?</em> Doorpraten met een omweg levert op een examen punten op; "
                      "zwijgen niet."),
        ]),
        dict(kop="Waar wordt Frans gesproken", blokken=[
            ("p", "In België is het Frans de taal van <strong>Wallonië en Brussel</strong>. Daarnaast is "
                  "het een officiële taal in onder meer <strong>Canada</strong>, <strong>Zwitserland</strong> "
                  "en <strong>Senegal</strong>. <strong>Het Frans wordt op meerdere continenten als "
                  "officiële taal gebruikt.</strong>"),
            ("p", "Het Franstalige gewest van Canada is <strong>Québec</strong>. <strong>La "
                  "Francophonie</strong> is <strong>de samenwerking van Franstalige landen</strong>."),
            ("p", "<strong>Het verschil tussen <em>la Wallonie</em> en <em>la Flandre</em> is in een "
                  "Franse tekst een geografisch én een talig verschil.</strong>"),
            ("p", tabel(["België", "Frankrijk"],
                        [["septante, nonante", "soixante-dix, quatre-vingt-dix"],
                         ["déjeuner = het ontbijt", "petit déjeuner = het ontbijt"],
                         ["dîner = het middagmaal", "déjeuner = het middagmaal"],
                         ["souper = het avondmaal", "dîner = het avondmaal"],
                         ["bourgmestre", "maire"]])),
            ("p", "Belgische Franstaligen zeggen <strong>septante</strong> voor zeventig, en de drie "
                  "verschillen die de fiche noemt zijn: <strong>België zegt septante en nonante</strong>, "
                  "<strong>België zegt déjeuner voor het ontbijt</strong> en <strong>België gebruikt "
                  "bourgmestre voor burgemeester</strong>. Let dus op bij de maaltijden: hetzelfde woord "
                  "betekent aan weerszijden van de grens een ander uur van de dag."),
        ]),
        dict(kop="School en werk in Frankrijk", blokken=[
            ("p", "<strong>Le bac</strong> is <strong>het eindexamen van het secundair</strong>; het "
                  "laatste jaar heet <strong>la terminale</strong>. <strong>La rentrée</strong> is "
                  "<strong>het begin van het schooljaar</strong>, en dat woord gebruikt men in Frankrijk "
                  "voor veel meer dan school: het hele land begint in september opnieuw."),
            ("p", "Het Franse schooljaar verschilt van het onze doordat <strong>de jaren omgekeerd geteld "
                  "worden</strong>: na la sixième komt la cinquième, en zo verder tot la première en "
                  "daarna la terminale."),
            ("p", "<strong>Le smic</strong> is <strong>het wettelijk minimumloon</strong>, en <strong>een "
                  "Franse werknemer heeft wel degelijk recht op betaalde vakantie</strong>: vijf weken, "
                  "wettelijk vastgelegd."),
        ]),
        dict(kop="Aan tafel", blokken=[
            ("p", "Bij een Franse maaltijd horen <strong>l'entrée</strong>, <strong>le plat "
                  "principal</strong> en <strong>le dessert</strong>. Een <strong>entrée</strong> is "
                  "<strong>het voorgerecht</strong>, niet het hoofdgerecht; in het Amerikaans Engels "
                  "betekent <em>entrée</em> juist wél het hoofdgerecht, en daar gaat het vaak mis."),
            ("p", "Het ontbijt heet in Frankrijk <strong>le petit déjeuner</strong>."),
            ("p", "<strong>De middagpauze is in Frankrijk traditioneel niet kort.</strong> Een echte "
                  "maaltijd aan tafel, vaak een uur of meer, hoort er nog altijd bij, ook al eet men in de "
                  "grote steden vaker snel."),
            ("p", "De nationale feestdag van Frankrijk is <strong>14 juli</strong>."),
            ("p", "De fiche vraagt dat je culturele verschillen kan benoemen <strong>om beter te begrijpen "
                  "wat je leest</strong>. Wie niet weet wat <em>la rentrée</em> of <em>le bac</em> is, "
                  "leest een krantenartikel maar half."),
        ]),
        spreken("spreek een Franstalige aan met een vraag om inlichting, met bonjour vooraan en de "
                "conditionnel de politesse erin, en let op het verschil tussen tu en vous."),
    ])


# ───────────────────────── 4. Literaire teksten en literatuurbeleving
zet("literaire-teksten-en-literatuurbeleving",
    titel="Literaire teksten en literatuurbeleving",
    onder="De bouw van een verhaal, de woorden om erover te spreken, en hoe je zegt wat een tekst met je deed.",
    secties=[
        dict(kop="Wat is een literaire tekst", blokken=[
            ("p", "De fiche noemt literair: <strong>een gedicht en een lied</strong>, <strong>een strip en "
                  "een cartoon</strong>, en <strong>een kortverhaal of romanfragment</strong>."),
            ("p", tabel(["Frans", "Nederlands"],
                        [["un roman", "een roman"],
                         ["un poème", "een gedicht"],
                         ["une nouvelle", "een kortverhaal"],
                         ["une bande dessinée", "een strip"],
                         ["un chapitre", "een hoofdstuk"],
                         ["la couverture", "de kaft"],
                         ["un résumé", "een korte samenvatting"]])),
            ("p", "<strong><em>Une nouvelle</em> kan in het Frans zowel een kortverhaal als een nieuwtje "
                  "betekenen.</strong> De context beslist, en in een literatuurvraag is het bijna altijd "
                  "het kortverhaal."),
            ("p", "<strong>Een cartoon kan je wel degelijk als een literaire tekst lezen</strong>, ook al "
                  "staan er weinig woorden in: het beeld, de verhouding tussen tekst en tekening en de "
                  "ironie dragen er de betekenis."),
        ]),
        dict(kop="De bouw van een verhaal", blokken=[
            ("p", "Om over de bouw van een verhaal te spreken gebruik je <strong>le personnage</strong>, "
                  "<strong>l'intrigue</strong> en <strong>le dénouement</strong>."),
            ("p", tabel(["Frans", "Nederlands"],
                        [["un personnage", "een personage"],
                         ["l'auteur, l'écrivain", "de schrijver"],
                         ["l'intrigue", "de verhaallijn"],
                         ["le dénouement", "de ontknoping"],
                         ["une strophe", "een strofe, een groepje regels"],
                         ["un vers", "een versregel"]])),
            ("p", "<strong>In een Franse roman staat het verhaal vaak in de passé simple en de "
                  "imparfait.</strong> Lees: <em>Il entra dans la pièce. Le feu brûlait encore.</em> De "
                  "tweede zin staat in <strong>de imparfait</strong>: die geeft de achtergrond, terwijl de "
                  "passé simple de handeling draagt."),
        ]),
        dict(kop="Beeldspraak", blokken=[
            ("p", "Een literaire tekst gebruikt vaker dan een krantenartikel <strong>beeldspraak</strong>, "
                  "<strong>vergelijkingen</strong> en <strong>klank en ritme</strong>."),
            ("p", "Lees: <em>Le temps passe et moi, je reste.</em> Die regel gebruikt het beeld van "
                  "<strong>de tijd als iets dat wandelt</strong>. En <em>Elle avait les yeux de la mer "
                  "après la tempête</em> doet maar één ding: <strong>een beeld oproepen</strong>. Je kan "
                  "zo'n zin niet nagaan en niet uitleggen in cijfers; je moet hem zien."),
            ("kader", "<strong>Bij een literaire tekst moet je niet elk woord kennen om de tekst te kunnen "
                      "beleven.</strong> Dat is het verschil met een leesvraag over een treinbericht. Een "
                      "gedicht waarvan je drie woorden mist, kan je nog altijd raken, en dat mag je ook "
                      "zo zeggen."),
        ]),
        dict(kop="Literatuurbeleving", blokken=[
            ("p", "<strong>Literatuurbeleving</strong> is <strong>zeggen wat een tekst met je doet</strong>. "
                  "Het is geen samenvatting en geen analyse: het is jouw reactie, met de tekst erbij."),
            ("p", "<strong>Je onderbouwt je mening het best met een stukje uit de tekst.</strong> Zonder "
                  "zo'n stukje is het een smaakoordeel; mét is het literatuurbeleving."),
            ("p", tabel(["uitdrukking", "wat ze zegt"],
                        [["j'ai aimé ce passage", "ik vond dit stuk goed"],
                         ["ce personnage m'a surpris", "dit personage verraste me"],
                         ["la fin m'a déçu", "het einde stelde me teleur"],
                         ["ce qui m'a frappé, c'est…", "wat me opviel, is…"],
                         ["je n'ai pas pu le lâcher", "ik kon het niet wegleggen"]])),
            ("p", "Het werkwoord dat raken of ontroeren betekent, is <strong>toucher</strong>: <em>ce livre "
                  "m'a touché</em>. <em>Ce qui m'a frappé, c'est le silence du père</em>: daarmee "
                  "<strong>zegt de schrijver wat hem opviel</strong>."),
            ("p", "Woorden om een boek positief te beoordelen: <strong>émouvant</strong>, "
                  "<strong>captivant</strong> en <strong>bien écrit</strong>. <strong>Passionnant</strong> "
                  "betekent boeiend of meeslepend, van <em>passionner</em>. En <strong>décevant</strong> "
                  "betekent <strong>ontgoochelend</strong>."),
            ("p", "<strong>Je mag bij literatuurbeleving zeggen dat je een boek niet goed vond.</strong> "
                  "Een eerlijk en onderbouwd mishagen is evenveel waard als lof; wat telt is dat je zegt "
                  "waarom, met een passage erbij."),
            ("p", "<strong>Over een boek spreek je in het Frans niet altijd in een verleden tijd.</strong> "
                  "De inhoud beschrijf je gewoon in de présent: <em>Le roman raconte l'histoire d'une "
                  "famille…</em> Je eigen leeservaring staat wel in de passé composé: <em>j'ai aimé</em>."),
        ]),
        dict(kop="Je beoordeling voorbereiden", blokken=[
            ("p", "Het is nuttig om bij het lezen notities te maken, <strong>want dan vind je je passages "
                  "snel terug</strong>. Op het moment dat je je mening moet staven, heb je geen tijd meer "
                  "om een boek door te bladeren."),
            ("p", "Drie vragen helpen je om over een gelezen tekst te spreken: <strong>wat raakte mij, en "
                  "waarom?</strong>, <strong>wat begreep ik niet meteen?</strong> en <strong>aan wie zou "
                  "ik dit aanraden?</strong>"),
            ("p", "<strong>Een citaat uit een Franse tekst moet je bij een beoordeling niet naar het "
                  "Nederlands vertalen.</strong> Je spreekt of schrijft in het Frans, dus het citaat "
                  "blijft in het Frans staan."),
            ("p", "<em>Recommander un livre</em> betekent <strong>een boek aanraden</strong>, en een "
                  "passende slotzin onder je eigen beoordeling is <strong>Je le recommande "
                  "vivement.</strong>"),
            ("p", "<strong>Een strip of een lied kan even goed dienen om je literatuurbeleving te laten "
                  "zien als een roman.</strong> De fiche vraagt niet om dikke boeken, maar om wat een "
                  "tekst met je doet."),
        ]),
        spreken("vertel in het Frans over een boek, een lied of een strip die je echt raakte, met één "
                "passage erbij en de reden waarom hij bleef hangen."),
    ])


# ───────────────────────── 5. Schrijven en schriftelijke interactie
zet("schrijven-en-schriftelijke-interactie",
    titel="Schrijven en schriftelijke interactie",
    onder="Het communicatiemodel en het schrijfplan, de opbouw van een formele mail, en hoe je echt op iemands bericht ingaat.",
    secties=[
        dict(kop="Voor je begint", blokken=[
            ("p", "De eerste vraag van het communicatiemodel is <strong>waarom schrijf ik?</strong> Daarna "
                  "volgen: <strong>voor wie is mijn boodschap?</strong> en <strong>welk kanaal gebruik "
                  "ik?</strong> Een mail aan een directeur, een berichtje aan een vriend en een blogpost "
                  "zijn drie verschillende teksten, ook al gaat het over hetzelfde."),
            ("p", "Het lijstje kernwoorden dat je maakt voor je begint te schrijven, is je "
                  "<strong>schrijfplan</strong>. Tien woorden op een kladblad kosten je twee minuten en "
                  "sparen je een tekst die halfweg verdwaalt."),
            ("p", "<strong>De fiche vraagt dat de opbouw van je tekst herkenbaar is, met een titel en "
                  "alinea's.</strong> Je verdeelt je tekst in alinea's <strong>omdat elke alinea één "
                  "gedachte draagt</strong>."),
        ]),
        dict(kop="De formele mail", blokken=[
            ("p", tabel(["deel", "wat er staat"],
                        [["Objet", "waarover het gaat, boven de mail"],
                         ["de aanhef", "Madame, of Monsieur le Directeur,"],
                         ["de eerste zin", "Je vous écris au sujet de…"],
                         ["de kern", "één gedachte per alinea"],
                         ["de laatste alinea", "wat je van de ander verwacht"],
                         ["de slotformule", "Je vous remercie d'avance."]])),
            ("p", "Boven de onderwerpregel van een formele mail staat <strong>Objet</strong>, en "
                  "<strong>in een mail aan een bedrijf vermeld je het best waarover het gaat in de "
                  "onderwerpregel</strong>. Aan een onbekende mevrouw schrijf je <strong>Madame,</strong>"),
            ("p", "Eerste zinnen die passen: <strong>Je vous écris au sujet de…</strong>, <strong>Je me "
                  "permets de vous contacter…</strong> en <strong>Suite à votre annonce, je…</strong> De "
                  "uitdrukking die naar aanleiding van betekent en vaak een formele mail opent, is "
                  "<strong>suite à votre</strong>."),
            ("p", "<strong>Een formele Franse mail begint niet het best met een lange inleiding over "
                  "jezelf.</strong> Je zegt meteen waarover het gaat; wie je bent, blijkt onderweg of "
                  "staat in één bijzin."),
            ("p", "<strong>In een Franse brief zet je een komma na de aanhef en begin je daarna met een "
                  "hoofdletter op een nieuwe regel.</strong>"),
            ("p", "<em>Je vous serais reconnaissant de bien vouloir me répondre</em> doet één ding: "
                  "<strong>hoffelijk om een antwoord vragen</strong>. <em>Je reste à votre disposition "
                  "pour tout renseignement</em> zegt: <strong>je mag me altijd nog vragen stellen</strong>. "
                  "En <em>Je vous remercie de votre réponse rapide</em> schrijf je <strong>nadat iemand je "
                  "snel antwoordde</strong>."),
            ("p", "Aan een Franse vriend schrijf je gewoon <strong>Salut Léo, ça va ?</strong> Dat is "
                  "een ander register, en dat mag."),
        ]),
        dict(kop="De draad in je tekst", blokken=[
            ("p", "Woorden die je alinea's tot één verhaal verbinden: <strong>d'abord en ensuite</strong>, "
                  "<strong>de plus en par ailleurs</strong>, en <strong>enfin en pour conclure</strong>."),
            ("p", "Je slotalinea open je met <strong>pour conclure</strong>, of met <em>en conclusion</em> "
                  "of <em>pour finir</em>."),
            ("p", "<strong>In een formele tekst gebruik je volledige zinnen omdat dat bij het register "
                  "hoort.</strong> Afkortingen en weggelaten woorden horen in een chatbericht, niet in een "
                  "brief aan een bedrijf. <strong>De zin <em>Mdr, c'était trop drôle</em> hoort niet in "
                  "een formele mail.</strong>"),
            ("p", "<strong>Spelfouten maken wel degelijk uit, ook als je boodschap duidelijk is.</strong> "
                  "Ze kosten punten op het examen, en buiten school kosten ze je geloofwaardigheid."),
            ("p", "Ken je het Franse woord niet dat je zoekt, dan <strong>zeg je het met andere "
                  "woorden</strong>. Een omweg is altijd beter dan een gat of een Nederlands woord met "
                  "een Franse klank eraan."),
            ("p", "Een passende titel boven een blogbericht over een schoolreis naar Parijs is bijvoorbeeld "
                  "<strong>Trois jours à Paris avec ma classe</strong>: concreet, kort, en hij zegt "
                  "waarover het gaat."),
        ]),
        dict(kop="Schriftelijke interactie", blokken=[
            ("p", "<strong>Schriftelijke interactie</strong> is <strong>schrijven en antwoorden op "
                  "elkaar</strong>. Het verschil met gewoon schrijven is dat er iets van de ander ligt "
                  "waar je op moet ingaan."),
            ("p", "<strong>Bij schriftelijke interactie mag je de vraag van de ander niet onbeantwoord "
                  "laten omdat je iets anders interessanter vindt.</strong> Juist dat ingaan op de ander "
                  "is wat beoordeeld wordt."),
            ("p", "Lees: <em>Pourriez-vous me dire si la réunion est reportée ?</em> Een gepast antwoord "
                  "is <strong>Oui, elle est reportée à jeudi.</strong> Kort, en het beantwoordt precies "
                  "wat er gevraagd werd."),
            ("p", "Zinnen die laten zien dat je inspeelt op wat de ander schreef: <strong>Je comprends "
                  "votre inquiétude.</strong>, <strong>Vous avez raison sur ce point.</strong> en "
                  "<strong>Pour répondre à votre question…</strong>"),
            ("p", "Begrijp je iets niet, dan vraag je <strong>pourriez-vous préciser</strong>. Heb je de "
                  "indruk dat de ander jou niet begreep, dan <strong>formuleer je het anders</strong>: "
                  "hetzelfde nog eens herhalen helpt niet."),
            ("p", "Antwoord je op een klacht van een klant, dan past een toon die <strong>hoffelijk is en "
                  "met begrip</strong>. Spijt betuig je met <strong>je regrette</strong>, of <em>nous "
                  "regrettons</em> namens een bedrijf."),
        ]),
        dict(kop="Tu en vous door elkaar", blokken=[
            ("p", "Lees: <em>Je t'écris pour te demander un service.</em> Wat opvalt: <strong>de schrijver "
                  "tutoyeert</strong>. <strong>Binnen één mail mag je niet afwisselen tussen tu en "
                  "vous.</strong> Je kiest er één en houdt die vol."),
            ("p", "De woordjes die het makkelijkst verkeerd blijven staan als je van tu naar vous "
                  "overstapt: <strong>ton in plaats van votre</strong>, <strong>tes in plaats van "
                  "vos</strong> en <strong>toi in plaats van vous</strong>. Het werkwoord pas je bij het "
                  "herlezen vanzelf aan; de bezittelijke woordjes glippen erdoor."),
        ]),
        dict(kop="Nalezen", blokken=[
            ("p", "Bij het nalezen let je volgens de fiche op drie dingen: <strong>is de boodschap "
                  "helder?</strong>, <strong>is de toon gepast?</strong> en <strong>leest het "
                  "vlot?</strong> <strong>Een gepaste lay-out hoort volgens de fiche ook bij wat er op "
                  "het schrijfexamen beoordeeld wordt.</strong>"),
            ("p", "Naast een eenvoudig woordenboek mag je op het schrijfexamen de "
                  "<strong>spellingcontrole</strong> gebruiken. <strong>Die is geen volledige oplossing, "
                  "want ze ziet een fout woord niet</strong>: <em>ces</em> in plaats van <em>ses</em>, "
                  "<em>a</em> in plaats van <em>à</em>, <em>ou</em> in plaats van <em>où</em>. Allemaal "
                  "bestaande woorden, allemaal fout op die plaats."),
        ]),
        spreken("schrijf een korte mail in het Frans aan een Franstalige organisatie met een echte vraag, "
                "en lees hem daarna hardop na: wat je niet vlot kan uitspreken, leest meestal ook niet "
                "vlot."),
    ])


# ───────────────────────── 6. Woordvelden: de mens, gezondheid, eten en wonen
zet("woordvelden-de-mens-gezondheid-eten-en-wonen",
    titel="Woordvelden: de mens, gezondheid, eten en wonen",
    onder="Je lichaam en je gevoelens, naar de dokter, de dagelijkse routine, eten en een Franse woningadvertentie lezen.",
    secties=[
        dict(kop="Gezondheid", blokken=[
            ("p", "<strong>La santé</strong> is de gezondheid; <strong>la pharmacie</strong> is de "
                  "apotheek; een <strong>ordonnance</strong> is <strong>een voorschrift</strong>."),
            ("p", tabel(["Frans", "Nederlands"],
                        [["J'ai mal à la tête depuis deux jours.", "ik heb al twee dagen hoofdpijn"],
                         ["être fatigué", "moe zijn"],
                         ["avoir de la fièvre", "koorts hebben"],
                         ["tomber malade", "ziek worden"],
                         ["elle est enrhumée", "zij is verkouden"],
                         ["se remettre", "herstellen van iets"],
                         ["il est en pleine forme", "hij voelt zich uitstekend"]])),
            ("p", "Bij de dokter zeg je <em>J'ai mal à la tête</em>, met <em>à la</em>, <em>au</em> of "
                  "<em>aux</em> naargelang het lichaamsdeel: <em>j'ai mal au ventre</em>, <em>j'ai mal aux "
                  "dents</em>."),
            ("p", "<strong>La fatigue</strong> is vermoeidheid. Let op het paar <strong>fatigué</strong> "
                  "en <strong>fatigant</strong>: <strong>de eerste is moe, de tweede vermoeiend</strong>. "
                  "<em>Je suis fatigué</em> gaat over jou, <em>c'est fatigant</em> over het werk."),
        ]),
        dict(kop="Gevoelens en karakter", blokken=[
            ("p", "Woorden die bij gevoelens horen: <strong>la joie</strong>, <strong>la tristesse</strong> "
                  "en <strong>la colère</strong>. Iemand die snel zenuwachtig wordt, is "
                  "<strong>stressé</strong>."),
            ("p", tabel(["Frans", "Nederlands"],
                        [["je me sens mal à l'aise", "ik voel me niet op mijn gemak"],
                         ["avoir le moral", "goed in je vel zitten"],
                         ["il s'entend bien avec sa sœur", "hij kan goed overweg met zijn zus"],
                         ["rendre service à quelqu'un", "iemand een dienst bewijzen"]])),
            ("kader", "<strong>Het Franse woord <em>sensible</em> betekent niet verstandig maar "
                      "gevoelig.</strong> Verstandig is <em>raisonnable</em>, en het Engelse "
                      "<em>sensible</em> betekent juist wél verstandig. Drie talen, drie betekenissen voor "
                      "bijna hetzelfde woord."),
            ("p", "<strong><em>Un voisin</em> betekent geen neef maar een buur.</strong> Een neef is "
                  "<em>un cousin</em>, en dat lijkt er net genoeg op om mis te gaan."),
        ]),
        dict(kop="De dagelijkse routine", blokken=[
            ("p", "Een dagelijkse routine beschrijf je met wederkerende werkwoorden: <strong>se lever "
                  "tôt</strong>, <strong>prendre une douche</strong> en <strong>se coucher vers dix "
                  "heures</strong>. <strong>Dormir</strong> is slapen."),
            ("p", "<em>Faire la grasse matinée</em> betekent <strong>uitslapen</strong>, met het woord "
                  "<strong>grasse</strong> erin. <strong>Het betekent dus niet het huis poetsen</strong>: "
                  "dat is <em>faire le ménage</em>. Twee uitdrukkingen met <em>faire</em>, en precies "
                  "tegenovergesteld van sfeer."),
        ]),
        dict(kop="Eten", blokken=[
            ("p", "Een <strong>boulangerie</strong> is een bakkerij, een <strong>boucherie</strong> een "
                  "slagerij. Op een Franse menukaart staan <strong>l'entrée</strong>, <strong>le plat du "
                  "jour</strong> en <strong>la carte des vins</strong>. Afrekenen vraag je met "
                  "<strong>L'addition, s'il vous plaît.</strong>"),
            ("p", "Ontbijten is <strong>prendre le petit-déjeuner</strong>."),
            ("p", "<strong><em>Je suis plein</em> is niet de gewone manier om te zeggen dat je genoeg "
                  "gegeten hebt.</strong> Het betekent in spreektaal dronken, en over een dier zwanger. Je "
                  "zegt <em>je n'ai plus faim</em> of <em>c'était délicieux, merci</em>."),
            ("p", "<strong>Het verschil tussen <em>c'est bon</em> en <em>c'est bien</em>: bon gaat over "
                  "smaak, bien over kwaliteit.</strong> Een gerecht is <em>bon</em>, een film of een idee "
                  "is <em>bien</em>."),
        ]),
        dict(kop="Wonen", blokken=[
            ("p", "Woorden die bij wonen horen: <strong>le loyer</strong>, <strong>le propriétaire</strong> "
                  "en <strong>le locataire</strong>. De huur die je maandelijks betaalt, is het "
                  "<strong>loyer</strong>; <em>le propriétaire</em> is de eigenaar en <em>le locataire</em> "
                  "de huurder."),
            ("p", tabel(["in de advertentie", "wat het is"],
                        [["un immeuble", "een gebouw met appartementen"],
                         ["un studio", "een woning met één kamer"],
                         ["un T3", "drie kamers naast de keuken en het bad"],
                         ["meublé", "gemeubeld"],
                         ["charges comprises", "kosten inbegrepen"]])),
            ("p", "<strong>In een Franse advertentie betekent <em>T3</em> een woning met drie kamers naast "
                  "de keuken en het bad.</strong> De T staat voor <em>type</em>, en het cijfer telt enkel "
                  "de leefruimtes: woonkamer en slaapkamers, niet de keuken, niet de badkamer."),
        ]),
        dict(kop="Sport en vrije tijd", blokken=[
            ("p", "<strong><em>Faire du vélo</em> betekent fietsen</strong>, en <strong>s'entraîner</strong> "
                  "betekent <strong>trainen voor een sport</strong>."),
            ("p", "<strong>Je gebruikt <em>jouer à</em> bij een spel met een bal</strong>, en <em>faire "
                  "de</em> bij de andere sporten: <em>jouer au football</em>, <em>jouer au tennis</em>, "
                  "maar <em>faire du vélo</em>, <em>faire de la natation</em>, <em>faire du judo</em>."),
            ("p", "Woorden die bij vrije tijd horen: <strong>un loisir</strong>, <strong>une sortie</strong> "
                  "en <strong>un spectacle</strong>."),
            ("p", "Lees: <em>Un ciné ce soir, ça te dit ?</em> <em>Ça te dit</em> betekent <strong>heb je "
                  "daar zin in?</strong> Een uitdrukking die je nooit uit de losse woorden zou afleiden, "
                  "en die je in elk Frans gesprek hoort."),
        ]),
        spreken("vertel in het Frans hoe een gewone dag van jou verloopt, van opstaan tot slapengaan, en "
                "gebruik daarin minstens vijf wederkerende werkwoorden."),
    ])


# ───────────────────────── 7. Woordvelden: school, werk, reizen en de samenleving
zet("woordvelden-school-werk-reizen-en-de-samenleving",
    titel="Woordvelden: school, werk, reizen en de samenleving",
    onder="Het Franse schoolsysteem, werk en geld, de trein en het verkeer, en de woorden van milieu, politiek en internet.",
    secties=[
        dict(kop="School", blokken=[
            ("p", "Het Franse secundair valt in twee stukken: <strong>le collège</strong> voor de eerste "
                  "jaren, <strong>le lycée</strong> voor <strong>de laatste jaren van het "
                  "secundair</strong>."),
            ("p", tabel(["Frans", "Nederlands"],
                        [["un bulletin", "een rapport"],
                         ["une interrogation", "een toets"],
                         ["un emploi du temps", "een lessenrooster"],
                         ["une matière", "een vak"],
                         ["un stage", "een stage of een cursus"],
                         ["redoubler", "een jaar overdoen"]])),
            ("kader", "<strong><em>Passer un examen</em> betekent niet dat je geslaagd bent.</strong> Het "
                      "betekent enkel dat je het examen aflegt. Geslaagd zijn is <em>réussir</em>, en "
                      "<em>réussir son année</em> betekent <strong>zijn jaar halen</strong>. Dit is de "
                      "valse vriend die op elk examen Frans terugkomt."),
        ]),
        dict(kop="Werk", blokken=[
            ("p", "Bij het zoeken van werk horen <strong>une offre d'emploi</strong>, <strong>un entretien "
                  "d'embauche</strong> en <strong>un curriculum vitae</strong>. <strong>Emploi</strong> is "
                  "werk of betrekking, en <em>être au chômage</em> betekent <strong>werkloos zijn</strong>."),
            ("p", "<strong><em>Un cadre</em> kan in een tekst over werk een leidinggevende "
                  "betekenen.</strong> Hetzelfde woord betekent elders een kader of een omlijsting; de "
                  "context beslist."),
            ("p", "<strong><em>Le salaire net</em> is niet het loon vóór er belastingen en bijdragen "
                  "afgaan.</strong> Dat is <em>le salaire brut</em>. Net is wat er op je rekening komt."),
        ]),
        dict(kop="Geld en economie", blokken=[
            ("p", tabel(["Frans", "Nederlands"],
                        [["une hausse", "een stijging"],
                         ["une baisse", "een daling"],
                         ["le pouvoir d'achat", "de koopkracht"],
                         ["une facture", "een factuur"],
                         ["un remboursement", "een terugbetaling"],
                         ["une promotion", "een korting of promotie"],
                         ["les soldes", "de solden, twee keer per jaar"]])),
            ("p", "<strong><em>Une promotion</em> kan in een Franse winkel een korting betekenen</strong>, "
                  "en op het werk een bevordering. <strong>Les soldes</strong> zijn in Frankrijk wettelijk "
                  "vastgelegd: twee periodes per jaar, winter en zomer."),
            ("p", "<em>Une enquête</em> in een krantenartikel is <strong>een onderzoek of een "
                  "enquête</strong>: zowel het journalistieke speurwerk als de rondvraag."),
        ]),
        dict(kop="Reizen en verkeer", blokken=[
            ("p", "Aan het loket is <strong>un aller-retour</strong> <strong>een heen-en-terugticket</strong>, "
                  "en <strong>un aller simple</strong> een enkele reis."),
            ("p", "Bij een treinreis horen <strong>le quai</strong> (het perron), <strong>la voie</strong> "
                  "(het spoor) en <strong>le guichet</strong> (het loket). <em>Composter votre billet</em> "
                  "betekent <strong>je ticket afstempelen</strong> voor je opstapt."),
            ("p", "<strong><em>Les embouteillages</em> zijn files op de weg</strong>, en <strong>un "
                  "bouchon</strong> in een verkeersbericht is <strong>een file</strong>. Hetzelfde woord "
                  "betekent een kurk: een file is letterlijk een prop in de weg."),
        ]),
        dict(kop="Milieu", blokken=[
            ("p", "Woorden die bij het milieu horen: <strong>le réchauffement</strong>, <strong>les "
                  "déchets</strong> en <strong>le gaspillage</strong>. <strong>Les déchets</strong> is "
                  "afval, altijd in het meervoud."),
            ("p", "<strong>Le développement durable</strong> is <strong>duurzame ontwikkeling</strong>. "
                  "<strong><em>Le gaspillage alimentaire</em> betekent niet de productie van voedsel</strong>, "
                  "maar voedselverspilling: wat er weggegooid wordt."),
            ("p", "<strong>Une espèce menacée</strong> is <strong>een bedreigde diersoort</strong>; "
                  "<strong>une espèce</strong> is een soort."),
        ]),
        dict(kop="Politiek en samenleving", blokken=[
            ("p", "Woorden die bij politiek en maatschappij horen: <strong>une élection</strong>, "
                  "<strong>un sondage</strong> en <strong>une manifestation</strong>."),
            ("p", "<strong>Une manifestation</strong> in een Franse krant is <strong>een betoging</strong>. "
                  "<strong><em>Un sondage</em> is geen betoging maar een peiling.</strong> Die twee staan "
                  "vaak in hetzelfde artikel en betekenen iets heel anders."),
        ]),
        dict(kop="Internet en techniek", blokken=[
            ("p", tabel(["Frans", "Nederlands"],
                        [["le réseau", "het netwerk"],
                         ["les réseaux sociaux", "de sociale media"],
                         ["un ordinateur portable", "een laptop"],
                         ["télécharger", "downloaden"],
                         ["une panne", "een defect"]])),
            ("p", "<strong><em>Télécharger</em> betekent een bestand downloaden.</strong> Uploaden is "
                  "<em>téléverser</em> of <em>mettre en ligne</em>. En <strong>une panne</strong> is een "
                  "defect: <em>la voiture est en panne</em>, <em>une panne de courant</em> is een "
                  "stroomonderbreking."),
        ]),
        spreken("lees een Franstalig krantenartikel over het milieu of de politiek en vat het daarna in "
                "het Frans samen in vijf zinnen, hardop."),
    ])


# ───────────────────────── 8. Naamwoorden, lidwoorden en determinanten
zet("naamwoorden-lidwoorden-en-determinanten",
    titel="Naamwoorden, lidwoorden en determinanten",
    onder="De lidwoorden en hun samentrekkingen, het deelaanduidende lidwoord, de aanwijzende en bezittelijke bepalers, quel, en de onregelmatige meervouden.",
    secties=[
        dict(kop="De lidwoorden", blokken=[
            ("p", "De bepaalde lidwoorden zijn <strong>le, la, les</strong>; de onbepaalde zijn <em>un, "
                  "une, des</em>. <em><strong>La</strong> voiture de mon père</em>: <em>voiture</em> is "
                  "vrouwelijk."),
            ("p", "<strong>Niet alle Franse woorden die op <em>-e</em> eindigen zijn vrouwelijk.</strong> "
                  "<em>Le problème</em>, <em>le système</em>, <em>le musée</em>, <em>le lycée</em>: "
                  "allemaal mannelijk. Bij <em>problème</em> hoort dus <strong>le</strong>."),
            ("p", "Voor een klinker of een stomme h wordt <em>le</em> of <em>la</em> gewoon <em>l'</em>: "
                  "<strong>l'hôpital</strong>, niet <em>le hôpital</em>."),
        ]),
        dict(kop="Samentrekkingen", blokken=[
            ("p", tabel(["", "wordt", "voorbeeld"],
                        [["à + le", "au", "au cinéma"],
                         ["à + les", "aux", "aux enfants"],
                         ["de + le", "du", "je viens du Portugal"],
                         ["de + les", "des", "la fin des vacances"]])),
            ("p", "Er staat <strong>au cinéma</strong> en niet <em>à le cinéma</em> <strong>omdat à en le "
                  "samentrekken tot au</strong>. Met <em>la</em> en <em>l'</em> gebeurt dat niet: <em>Je "
                  "vais <strong>à la</strong> piscine.</em>"),
            ("p", "<strong><em>Je viens du Portugal</em> is juist, want <em>de + le</em> wordt "
                  "<em>du</em>.</strong>"),
            ("p", "Bij landen hangt het voorzetsel van het geslacht af: <strong>en Italie</strong> bij een "
                  "vrouwelijk land, <strong>Je vais au Canada</strong> bij een mannelijk."),
            ("p", tabel(["land", "naar", "uit"],
                        [["la France, l'Italie", "en France, en Italie", "de France, d'Italie"],
                         ["le Canada, le Portugal", "au Canada, au Portugal", "du Canada, du Portugal"],
                         ["les Pays-Bas", "aux Pays-Bas", "des Pays-Bas"]])),
        ]),
        dict(kop="Het deelaanduidende lidwoord", blokken=[
            ("p", "Het deelaanduidende lidwoord zegt dat het om een onbepaalde hoeveelheid gaat: "
                  "<em>du</em>, <em>de la</em>, <em>de l'</em>, <em>des</em>. In <em>je bois de l'eau</em> "
                  "is dat <strong>de l'</strong>."),
            ("p", "Juist gebruikt: <strong>Je mange du pain.</strong>, <strong>Elle boit de la "
                  "limonade.</strong> en <strong>Il achète des pommes.</strong>"),
            ("kader", "<strong>Na een ontkenning blijft <em>du</em>, <em>de la</em> of <em>des</em> niet "
                      "onveranderd staan: het wordt <em>de</em>.</strong> <em>J'ai des frères</em> wordt "
                      "<strong>Je n'ai pas de frères.</strong> en <em>Il n'y a plus "
                      "<strong>de</strong> lait.</em> Eén regel die bijna elke oefening van dit hoofdstuk "
                      "draagt."),
            ("p", "<strong>Na een hoeveelheid staat <em>de</em> of <em>d'</em></strong>, zonder lidwoord: "
                  "<strong>beaucoup de travail</strong>, <strong>un peu de patience</strong>, <strong>trop "
                  "de bruit</strong>."),
            ("p", "<strong>In <em>de bons amis</em> staat <em>de</em> omdat het bijvoeglijk naamwoord vóór "
                  "het meervoudige naamwoord komt.</strong> Daarom is het <strong>de grandes "
                  "maisons</strong>, niet <em>des grandes maisons</em>."),
        ]),
        dict(kop="De aanwijzende bepalers", blokken=[
            ("p", "De aanwijzende bepalers zijn <strong>ce, cet, cette, ces</strong>."),
            ("p", tabel(["vorm", "wanneer", "voorbeeld"],
                        [["ce", "mannelijk enkelvoud", "ce matin"],
                         ["cet", "mannelijk, voor een klinker of stomme h", "cet arbre, cet homme"],
                         ["cette", "vrouwelijk enkelvoud", "cette semaine"],
                         ["ces", "meervoud", "ces jours-ci"]])),
            ("p", "<strong>Je gebruikt <em>cet</em> in plaats van <em>ce</em> voor een klinker of een "
                  "stomme h</strong>: <em><strong>Cet</strong> arbre est très vieux.</em> Dat is dezelfde "
                  "reden als bij <em>l'</em>: twee klinkers na elkaar klinken niet."),
        ]),
        dict(kop="De bezittelijke bepalers", blokken=[
            ("kader", "<strong>Het Franse bezittelijk voornaamwoord volgt niet het geslacht van de "
                      "bezitter maar dat van het bezit.</strong> Daarom is <strong>zijn zus</strong> én "
                      "<strong>haar zus</strong> allebei <strong>sa sœur</strong>. Wie uit het Nederlands "
                      "of het Engels komt, wil hier <em>son</em> schrijven voor een man, en dat is fout."),
            ("p", tabel(["", "mannelijk", "vrouwelijk", "meervoud"],
                        [["mijn", "mon", "ma", "mes"],
                         ["jouw", "ton", "ta", "tes"],
                         ["zijn, haar", "son", "sa", "ses"],
                         ["ons", "notre", "notre", "nos"],
                         ["jullie, uw", "votre", "votre", "vos"],
                         ["hun", "leur", "leur", "leurs"]])),
            ("p", "<em>Paul cherche <strong>ses</strong> clés.</em> Meervoud, dus <em>ses</em>, hoe dan "
                  "ook."),
            ("p", "<strong>Voor een vrouwelijk woord dat met een klinker begint, wordt <em>ma</em> "
                  "<em>mon</em>.</strong> Dus <strong>mon amie</strong>, niet <em>ma amie</em>. Hetzelfde "
                  "bij <em>ton école</em> en <em>son histoire</em>."),
        ]),
        dict(kop="Quel en de onbepaalde bepalers", blokken=[
            ("p", "<em>Quel</em> richt zich naar het naamwoord erachter: <strong>quel, quelle, quels, "
                  "quelles</strong>."),
            ("p", tabel(["zin", "waarom"],
                        [["Quel âge as-tu ?", "âge is mannelijk enkelvoud"],
                         ["Quelle heure est-il ?", "heure is vrouwelijk enkelvoud"],
                         ["Quelle est votre adresse ?", "adresse is vrouwelijk"],
                         ["Quels livres préfères-tu ?", "livres is mannelijk meervoud"],
                         ["Quelles couleurs préfères-tu ?", "couleurs is vrouwelijk meervoud"]])),
            ("p", "Onbepaalde bepalers zeggen hoeveel zonder te tellen. <strong>Quelques</strong> betekent "
                  "<strong>enkele</strong>, en <strong>plusieurs</strong> (verscheidene) is er ook een."),
            ("p", "<strong>Na <em>chaque</em> staat het naamwoord altijd in het enkelvoud</strong>: "
                  "<em>chaque jour</em>, <em>chaque élève</em>, nooit <em>chaque jours</em>."),
        ]),
        dict(kop="Het meervoud", blokken=[
            ("p", tabel(["uitgang", "meervoud", "voorbeeld"],
                        [["-al", "-aux", "un journal — des journaux, un cheval — des chevaux"],
                         ["-ail (soms)", "-aux", "un travail — des travaux"],
                         ["-eu, -eau", "-x", "un cheveu — des cheveux, un bateau — des bateaux"],
                         ["-s, -x, -z", "blijft gelijk", "un prix — des prix"]])),
            ("p", "<em>Un journal</em> wordt <strong>des journaux</strong>, en <em>un cheval</em> wordt "
                  "<strong>des chevaux</strong>. Juist zijn ook <strong>des animaux</strong>, <strong>des "
                  "cheveux</strong> en <strong>des travaux</strong>."),
            ("p", "<strong>Een Frans woord dat al op een <em>-s</em> of een <em>-x</em> eindigt, krijgt er "
                  "in het meervoud geen s bij.</strong> Bij <strong>un prix</strong> verandert de vorm "
                  "dus niet: <em>des prix</em>. Enkel het lidwoord verraadt het aantal."),
        ]),
        spreken("beschrijf in het Frans je eigen kamer en de spullen van je huisgenoten, en let bij elk "
                "woord op het lidwoord en de bezittelijke bepaler."),
    ])


# ───────────────────────── 9. Voornaamwoorden: COD, COI, y en en
zet("voornaamwoorden-cod-coi-y-en-en",
    titel="Voornaamwoorden: COD, COI, y en en",
    onder="Lijdend en meewerkend voorwerp, y en en, de toniques, de betrekkelijke voornaamwoorden en de onbepaalde.",
    secties=[
        dict(kop="COD en COI", blokken=[
            ("p", "Het <strong>lijdend voorwerp</strong> (COD) hangt rechtstreeks aan het werkwoord; het "
                  "<strong>meewerkend voorwerp</strong> (COI) hangt eraan met <em>à</em>."),
            ("p", tabel(["", "COD", "COI"],
                        [["ik, jij", "me, te", "me, te"],
                         ["hij, zij", "le, la", "lui"],
                         ["wij, jullie", "nous, vous", "nous, vous"],
                         ["zij (meervoud)", "les", "leur"]])),
            ("p", "De rij van de COD is dus <strong>me, te, le, la, nous, vous, les</strong>. <em>Je vois "
                  "Marie</em> wordt <em>Je <strong>la</strong> vois.</em>"),
            ("p", "<strong>In <em>elle nous a téléphoné</em> is <em>nous</em> een COI en geen COD, want je "
                  "telefoneert <em>à quelqu'un</em>.</strong> De werkwoorden die een COI met <em>à</em> "
                  "vragen: <strong>téléphoner</strong>, <strong>parler</strong> en <strong>répondre</strong>. "
                  "<strong><em>Je lui parle</em> betekent dat je tegen hem of tegen haar spreekt</strong>: "
                  "<em>lui</em> dient voor allebei."),
            ("p", "Staan er twee voornaamwoorden, dan komt het COD eerst bij le, la en les, en het COI "
                  "eerst bij me, te, nous en vous. <em>Je donne le livre à Paul</em> wordt <strong>Je le "
                  "lui donne.</strong>, en <em>Je donne les clés à mes parents</em> wordt <em>Je "
                  "<strong>les leur</strong> donne.</em>"),
        ]),
        dict(kop="Y en en", blokken=[
            ("p", tabel(["woordje", "vervangt", "voorbeeld"],
                        [["y", "een plaats of een woord met à", "Nous allons à la mer. → Nous y allons."],
                         ["en", "een woord met de of des", "J'ai deux frères. → J'en ai deux."]])),
            ("p", "<strong><em>Y</em> vervangt meestal een plaats of een woord met <em>à</em></strong>, en "
                  "<strong><em>en</em> vervangt een woord met <em>de</em> of <em>des</em></strong>. "
                  "<strong><em>J'en ai deux</em> betekent dus niet dat je er naartoe gaat</strong>, maar "
                  "dat je er twee van hebt."),
            ("p", "<strong>De zin <em>Je y vais demain</em> is fout geschreven.</strong> Het is <em>J'y "
                  "vais demain</em>: <em>je</em> verliest zijn e voor een klinker."),
        ]),
        dict(kop="Waar staat het voornaamwoord", blokken=[
            ("p", "In een gewone zin staat het voornaamwoord vóór het werkwoord: <em>Je la vois.</em>, "
                  "<em>Je ne la vois pas.</em>"),
            ("p", "<strong>In een bevestigend bevel staat het erachter, met een streepje: "
                  "<em>donne-le</em>.</strong> Juist geschreven zijn <strong>Donne-moi ça !</strong>, "
                  "<strong>Dis-lui la vérité !</strong> en <strong>Ne me parle pas !</strong>"),
            ("p", "<strong>In een ontkennend bevel staat het voornaamwoord niet achter maar vóór het "
                  "werkwoord</strong>, net als in een gewone zin: <em>Ne me parle pas !</em>, <em>Ne le "
                  "donne pas !</em> Alleen het bevestigend bevel zet het erachter."),
        ]),
        dict(kop="De toniques", blokken=[
            ("p", "De toniques zijn <em>moi, toi, lui, elle, nous, vous, eux, elles</em>. Ze staan alleen, "
                  "of waar een gewoon voornaamwoord niet kan."),
            ("p", "In <em>c'est moi qui ai raison</em> is <em>moi</em> <strong>een tonique</strong>, die "
                  "nadruk legt. Juist gebruikt: <strong>Viens avec moi.</strong>, <strong>C'est pour "
                  "toi.</strong> en <strong>Lui, il ne sait rien.</strong>"),
            ("p", "<strong>Na een voorzetsel zoals <em>avec</em> of <em>pour</em> gebruik je de "
                  "tonique.</strong> Je zegt nooit <em>avec je</em>."),
        ]),
        dict(kop="De wederkerende werkwoorden", blokken=[
            ("p", "<em>Ik was me</em> is <strong>Je me lave.</strong> <strong>Het verschil tussen <em>je "
                  "lave la voiture</em> en <em>je me lave</em>: in het tweede slaat de handeling op "
                  "jezelf.</strong> Hetzelfde werkwoord, met en zonder het wederkerende woordje, en twee "
                  "heel andere zinnen."),
        ]),
        dict(kop="De betrekkelijke voornaamwoorden", blokken=[
            ("p", tabel(["woord", "wanneer", "voorbeeld"],
                        [["qui", "het onderwerp van de bijzin", "l'ami qui m'a écrit"],
                         ["que", "het lijdend voorwerp van de bijzin", "le film que j'ai vu"],
                         ["dont", "als er een de bij hoort", "le livre dont je parle"],
                         ["où", "een plaats of een tijd", "la ville où je suis né"]])),
            ("p", "<strong><em>Qui</em> vervangt het onderwerp van de bijzin</strong>: <em>La fille "
                  "<strong>qui</strong> habite à côté s'appelle Léa.</em> <em>Que</em> staat waar het "
                  "lijdend voorwerp zou staan: <strong>Le film que j'ai vu était long.</strong>"),
            ("p", "<strong><em>Dont</em> gebruik je als het werkwoord of het naamwoord in de bijzin een "
                  "<em>de</em> bij zich heeft.</strong> <em>Parler <strong>de</strong> quelque chose</em> "
                  "wordt dus <strong>le livre dont je parle</strong>, niet <em>le livre que je parle</em>."),
            ("p", "<strong><em>Où</em> kan in een bijzin voor een plaats én voor een tijd staan</strong>: "
                  "<em>Voilà la maison <strong>où</strong> je suis né.</em> en <em>le jour où nous nous "
                  "sommes rencontrés</em>."),
            ("p", "<em>Ce que</em> in <em>je ne comprends pas ce que tu dis</em> betekent "
                  "<strong>wat</strong>. <strong>In <em>ce qui m'intéresse, c'est l'histoire</em> is "
                  "<em>ce qui</em> niet het lijdend voorwerp maar het onderwerp van <em>intéresse</em></strong>: "
                  "dat wat mij interesseert."),
        ]),
        dict(kop="Celui, le mien en de vraagwoorden", blokken=[
            ("p", "<em>Celui</em> betekent <strong>die van</strong>: <em>celui de mon frère</em> is "
                  "<strong>die van mijn broer</strong>. De vormen zijn <em>celui, celle, ceux, celles</em>: "
                  "<em>Ma veste et <strong>celle</strong> de ma sœur.</em>"),
            ("p", "Het bezittelijk voornaamwoord dat alleen staat, draagt een lidwoord: <strong>le "
                  "mien</strong>, <strong>la tienne</strong>, <strong>les nôtres</strong>. <strong>Het "
                  "verschil met <em>mon livre</em>: <em>mon</em> staat bij een naamwoord</strong>, "
                  "<em>le mien</em> staat in de plaats ervan."),
            ("p", "<strong>In een vraag gebruik je <em>qui</em> voor personen en <em>quoi</em> voor "
                  "dingen.</strong> <em>À <strong>quoi</strong> penses-tu ?</em> is: aan wat denk je? "
                  "<em>À qui penses-tu ?</em> is: aan wie."),
        ]),
        dict(kop="De onbepaalde voornaamwoorden", blokken=[
            ("p", "<strong>Chacun</strong> betekent <strong>ieder of elk</strong>. Juist gebouwd zijn: "
                  "<strong>Personne n'est venu.</strong>, <strong>Chacun a son avis.</strong> en "
                  "<strong>Quelqu'un a sonné.</strong>"),
            ("p", "<strong><em>Personne</em> betekent in het Frans niet altijd een persoon.</strong> Als "
                  "zelfstandig naamwoord wel (<em>une personne</em>), maar als voornaamwoord met "
                  "<em>ne</em> betekent het juist niemand: <em>Personne n'est venu.</em> Let op de "
                  "<em>ne</em>, die het verschil maakt."),
            ("p", "<em>Il n'y a rien à faire</em> betekent <strong>er is niets aan te doen</strong>."),
        ]),
        spreken("vertel in het Frans wat je gisteren voor iemand gedaan hebt, en vervang daarbij bewust de "
                "namen door voornaamwoorden tot het vlot klinkt."),
    ])


# ───────────────────────── 10. Bijvoeglijke naamwoorden, bijwoorden en de trappen
zet("bijvoeglijke-naamwoorden-bijwoorden-en-de-trappen",
    titel="Bijvoeglijke naamwoorden, bijwoorden en de trappen",
    onder="De vrouwelijke en meervoudsvormen, waar het bijvoeglijk naamwoord staat, de bijwoorden op -ment en de trappen van vergelijking.",
    secties=[
        dict(kop="De vrouwelijke vorm", blokken=[
            ("p", "De gewone regel: <strong>je zet er een <em>e</em> achter</strong>. <em>grand — "
                  "grande</em>. Maar een aantal uitgangen doet het anders."),
            ("p", tabel(["mannelijk", "vrouwelijk", "regel"],
                        [["long", "longue", "-g wordt -gue"],
                         ["heureux", "heureuse", "-x wordt -se"],
                         ["sportif", "sportive", "-f wordt -ve"],
                         ["blanc", "blanche", "onregelmatig"],
                         ["bon", "bonne", "de medeklinker verdubbelt"],
                         ["vieux", "vieille", "onregelmatig"],
                         ["nouveau", "nouvelle", "onregelmatig"]])),
            ("p", "<em>Une réponse <strong>longue</strong></em>, <em>une fille "
                  "<strong>heureuse</strong></em>, <em>une <strong>bonne</strong> amie</em>, <em>C'est une "
                  "<strong>bonne</strong> idée.</em> De vrouwelijke vorm van <em>vieux</em> is "
                  "<strong>vieille</strong>, en <em>les <strong>nouvelles</strong> maisons</em>."),
            ("p", "<strong>Een bijvoeglijk naamwoord dat al op een <em>-e</em> eindigt, krijgt er in het "
                  "vrouwelijk geen tweede e bij.</strong> <em>Une voiture <strong>rouge</strong></em>, "
                  "<em>un homme jeune</em> en <em>une femme jeune</em>: dezelfde vorm."),
        ]),
        dict(kop="Het meervoud en de congruentie", blokken=[
            ("p", "Het meervoud is meestal een <em>-s</em>: <em>des <strong>grandes</strong> maisons</em>, "
                  "<em>des yeux <strong>bleus</strong></em>."),
            ("p", "<strong>Sommige krijgen in het mannelijk meervoud <em>-x</em> in plaats van "
                  "<em>-s</em></strong>: <strong>beau wordt beaux</strong>, <strong>nouveau wordt "
                  "nouveaux</strong> en <strong>général wordt généraux</strong>."),
            ("p", "<strong>Een bijvoeglijk naamwoord na het werkwoord <em>être</em> komt overeen met het "
                  "onderwerp.</strong> <strong>Les filles sont contentes.</strong> En bij een gemengde "
                  "groep wint het mannelijk meervoud: <em>Paul et Marie sont "
                  "<strong>fatigués</strong>.</em>"),
            ("p", "<strong>In <em>une chemise bleu clair</em> blijft <em>bleu clair</em> "
                  "onveranderd.</strong> Zodra een kleur uit twee woorden bestaat, verandert er niets meer: "
                  "<em>des yeux bleu clair</em>, <em>des chaussures vert foncé</em>."),
        ]),
        dict(kop="Waar staat het bijvoeglijk naamwoord", blokken=[
            ("p", "In het Frans staat het bijvoeglijk naamwoord meestal <strong>achter</strong> het "
                  "naamwoord: <strong>une voiture rouge</strong>. Een kleine groep gaat ervoor: "
                  "<strong>grand en petit</strong>, <strong>beau en joli</strong>, <strong>jeune en "
                  "vieux</strong>, en ook bon, mauvais, nouveau en gros."),
            ("kader", "<strong>Bij een handvol woorden bepaalt de plaats de betekenis.</strong> <em>Un "
                      "ancien élève</em> is een oud-leerling; <em>un bâtiment ancien</em> is een oud "
                      "gebouw. En <strong><em>un grand homme</em> betekent geen grote man in lengte</strong> "
                      "maar een groot man, iemand van betekenis; wie lang is, is <em>un homme grand</em>."),
        ]),
        dict(kop="Het bijwoord", blokken=[
            ("p", "<strong>Een bijwoord op <em>-ment</em> maak je uit de vrouwelijke vorm plus "
                  "<em>-ment</em>.</strong> <em>doux — douce — <strong>doucement</strong></em>, <em>lent "
                  "— lente — lentement</em>, <em>heureux — heureuse — heureusement</em>."),
            ("p", "<strong>Het verschil tussen <em>il est bon</em> en <em>il chante bien</em>: bon is "
                  "bijvoeglijk, bien is bijwoord.</strong> Daarom is <strong><em>Elle parle bon "
                  "français</em> fout</strong>: het moet <em>Elle parle <strong>bien</strong> "
                  "français</em> zijn, want het zegt iets over <em>parler</em>."),
            ("p", "Bijwoorden die zeggen hoe vaak iets gebeurt: <strong>souvent</strong>, "
                  "<strong>quelquefois</strong> en <strong>rarement</strong>. <strong>Quelquefois</strong> "
                  "betekent soms, net als <em>parfois</em>."),
            ("p", "<strong>Néanmoins</strong> betekent <strong>nochtans</strong>: een van die woorden die "
                  "je in een geschreven tekst tegenkomt en zelden hoort."),
        ]),
        dict(kop="De trappen van vergelijking", blokken=[
            ("p", "De vergrotende trap maak je met <strong>plus … que</strong>: <em>Marie est "
                  "<strong>plus</strong> grande <strong>que</strong> Paul.</em>"),
            ("p", tabel(["vorm", "betekenis", "voorbeeld"],
                        [["plus … que", "meer dan", "plus cher que"],
                         ["moins … que", "minder dan", "moins rapide que"],
                         ["aussi … que", "even als", "aussi grand que"]])),
            ("p", "Twee onregelmatige: <strong>de vergrotende trap van <em>bon</em> is "
                  "<em>meilleur</em></strong>, en <strong>die van het bijwoord <em>bien</em> is "
                  "<em>mieux</em></strong>. Daarom is <strong><em>Il joue meilleur que moi</em> "
                  "fout</strong>: spelen is een handeling, dus <em>Il joue <strong>mieux</strong> que "
                  "moi</em>."),
            ("p", "De overtreffende trap maak je met <strong>le plus</strong> of <strong>le moins</strong> "
                  "plus het woord. <strong>In <em>c'est la plus belle ville du pays</em> komt het "
                  "lidwoord <em>la</em> overeen met <em>ville</em></strong>, niet met iets anders."),
            ("p", "De overtreffende trappen van de onregelmatige: <strong>le meilleur élève de la "
                  "classe</strong>, <strong>le mieux</strong> bij het bijwoord, en <strong>le pire "
                  "résultat</strong> voor het slechtste."),
            ("p", "<strong>Na een overtreffende trap gebruik je in het Frans <em>de</em> of <em>du</em>, "
                  "waar wij in zeggen.</strong> De beste van de klas is <em>le meilleur <strong>de</strong> "
                  "la classe</em>, de mooiste stad van het land <em>la plus belle ville "
                  "<strong>du</strong> pays</em>."),
        ]),
        spreken("vergelijk hardop in het Frans drie mensen of drie plaatsen die je kent, met telkens een "
                "andere trap, en let op meilleur tegenover mieux."),
    ])


# ───────────────────────── 11. De verleden tijden en de accord van het deelwoord
zet("de-verleden-tijden-en-de-accord-van-het-deelwoord",
    titel="De verleden tijden en de accord van het deelwoord",
    onder="Passé composé tegenover imparfait, de plus-que-parfait en de passé récent, en wanneer het deelwoord meegaat.",
    secties=[
        dict(kop="De passé composé", blokken=[
            ("p", "Een passé composé bestaat uit <strong>een hulpwerkwoord plus een deelwoord</strong>: "
                  "<em>Hier, j'<strong>ai</strong> mangé au restaurant.</em>"),
            ("p", "De meeste werkwoorden nemen <em>avoir</em>. Een kleine groep neemt <strong>être</strong>: "
                  "<strong>aller</strong>, <strong>venir</strong> en <strong>partir</strong>, en hun "
                  "soortgenoten (entrer, sortir, monter, descendre, naître, mourir, rester, tomber). "
                  "<strong>Elk wederkerend werkwoord neemt in de passé composé ook être.</strong>"),
            ("p", "<strong><em>Je suis allé</em> en <em>j'ai allé</em> zijn niet allebei juist.</strong> "
                  "<em>Aller</em> neemt altijd <em>être</em>: <em>j'ai allé</em> bestaat niet."),
            ("p", "Met <em>être</em> komt het deelwoord overeen met het onderwerp: <strong>Elle est allée "
                  "à Paris.</strong> en <strong>Ils sont tombés.</strong>"),
            ("p", tabel(["infinitief", "deelwoord"],
                        [["prendre", "pris"], ["faire", "fait"], ["voir", "vu"],
                         ["mettre", "mis"], ["écrire", "écrit"], ["être", "été"], ["avoir", "eu"]])),
            ("p", "In een ontkenning staan <strong>ne en pas rond het hulpwerkwoord</strong>: <em>Je "
                  "<strong>n'</strong>ai <strong>pas</strong> mangé.</em> Het deelwoord komt erachter."),
        ]),
        dict(kop="De imparfait", blokken=[
            ("p", "<strong>De stam van de imparfait vind je uit de nous-vorm van het présent</strong>: "
                  "<em>nous allons</em> wordt <em>all-</em>, dus <em>j'<strong>allais</strong></em>. De "
                  "uitgangen zijn -ais, -ais, -ait, <strong>-ions</strong>, -iez, -aient."),
            ("p", "<strong>Être is het enige werkwoord met een onregelmatige stam in de imparfait</strong>: "
                  "<em>j'étais</em>, <strong>Nous étions fatigués.</strong>"),
            ("p", "<em>Quand j'étais petit, je <strong>allais</strong> souvent au parc</em> wordt natuurlijk "
                  "<em>j'allais</em>, met de elisie."),
        ]),
        dict(kop="Welke tijd wanneer", blokken=[
            ("p", tabel(["tijd", "waarvoor"],
                        [["passé composé", "een afgeronde gebeurtenis"],
                         ["imparfait", "een gewoonte, een beschrijving, het decor van een verhaal"],
                         ["plus-que-parfait", "wat nog eerder gebeurde"],
                         ["passé récent", "wat net gebeurd is"]])),
            ("p", "Voor <em>elke zomer gingen we naar de zee</em> gebruik je de <strong>imparfait</strong>. "
                  "Woorden die een imparfait aankondigen: <strong>souvent</strong>, <strong>chaque "
                  "jour</strong> en <strong>toujours</strong>."),
            ("p", "<strong>In <em>il lisait quand le téléphone a sonné</em> staat de achtergrond in de "
                  "imparfait.</strong> Wat er plots tussenkomt, staat in de passé composé: <em>soudain, "
                  "quelqu'un <strong>a frappé</strong> à la porte</em>."),
            ("p", "Juist gebruikt: <strong>J'ai vu ce film hier.</strong>, <strong>Il faisait froid ce "
                  "matin.</strong> en <strong>Nous venons de rentrer.</strong>"),
            ("p", "<strong>In gesproken Frans en in een mail gebruik je voor het verleden niet de passé "
                  "simple</strong>, maar de passé composé. De passé simple staat enkel in verhalende en "
                  "literaire teksten."),
            ("p", "Lees: <em>Je n'ai pas compris ce qu'il a dit.</em> Daar staat twee keer <strong>de "
                  "passé composé</strong>."),
        ]),
        dict(kop="Plus-que-parfait en passé récent", blokken=[
            ("p", "De <strong>plus-que-parfait</strong> vorm je met <strong>avoir of être in de imparfait "
                  "plus het deelwoord</strong>: <em>Quand je suis arrivé, il <strong>était</strong> déjà "
                  "parti.</em> In <em>il avait déjà mangé</em> staat dus de "
                  "<strong>plus-que-parfait</strong>."),
            ("p", "Lees: <em>Il avait travaillé toute la nuit, alors il était épuisé.</em> Het verband: "
                  "<strong>de eerste zin verklaart de tweede</strong>. Dat is precies waarvoor de "
                  "plus-que-parfait dient."),
            ("p", "De <strong>passé récent</strong> is <strong>venir de plus een infinitief</strong>. "
                  "<strong><em>Elle vient de partir</em> betekent niet dat ze op het punt staat te "
                  "vertrekken</strong>, maar dat ze net vertrokken is. Op het punt staan is <em>elle va "
                  "partir</em>: precies de andere richting."),
            ("p", "In een verhaal over je vakantie gebruik je alle drie: <strong>passé composé voor wat "
                  "gebeurde</strong>, <strong>imparfait voor het weer en het decor</strong>, en "
                  "<strong>plus-que-parfait voor wat eerder was</strong>."),
        ]),
        dict(kop="De accord van het deelwoord", blokken=[
            ("p", "<strong>Met être komt het deelwoord overeen met het onderwerp.</strong> <strong>Met "
                  "avoir komt het niet overeen met het onderwerp</strong>, maar met het lijdend voorwerp, "
                  "en enkel als dat vóór het werkwoord staat."),
            ("p", tabel(["zin", "accord?"],
                        [["Elle est allée à Paris.", "ja: être, met het onderwerp"],
                         ["Elle a mangé une pomme.", "nee: het COD staat erachter"],
                         ["La lettre que j'ai écrite est partie.", "ja: que verwijst naar la lettre, vooraan"],
                         ["Les photos que j'ai prises sont belles.", "ja: les photos staat vooraan"],
                         ["Elle nous a téléphoné.", "nee: nous is hier een COI"]])),
            ("p", "<strong>Het deelwoord blijft in <em>elle nous a téléphoné</em> onveranderd omdat "
                  "<em>nous</em> hier een COI is</strong>: je telefoneert <em>à quelqu'un</em>. Enkel een "
                  "lijdend voorwerp dat vooropstaat, trekt het deelwoord mee."),
            ("p", "<strong>Bij een wederkerend werkwoord komt het deelwoord overeen met het voornaamwoord "
                  "als dat het lijdend voorwerp is.</strong> <em>Elle s'est lavée</em> met accord, maar "
                  "<strong>Elle s'est lavé les mains.</strong> zonder: daar is <em>les mains</em> het "
                  "lijdend voorwerp, en het staat erachter."),
        ]),
        spreken("vertel in het Frans over een dag die je bijbleef: wat er gebeurde in de passé composé, "
                "hoe het eruitzag in de imparfait."),
    ])


# ───────────────────────── 12. Futur, conditionnel, subjonctif en de gérondif
zet("futur-conditionnel-subjonctif-en-de-gerondif",
    titel="Futur, conditionnel, subjonctif en de gérondif",
    onder="De toekomst, de hoffelijke en voorwaardelijke vormen, wanneer de subjonctif moet, en de gérondif voor twee dingen tegelijk.",
    secties=[
        dict(kop="Wijs en tijd", blokken=[
            ("p", "<strong>Het verschil tussen een wijs en een tijd: een wijs zegt hoe, een tijd zegt "
                  "wanneer.</strong> De indicatif stelt vast, de conditionnel veronderstelt, de subjonctif "
                  "staat na een gevoel of een wil, de impératif beveelt. Binnen elke wijs liggen dan de "
                  "tijden."),
            ("p", "De frequente semi-auxiliaires die de fiche noemt: <strong>vouloir en pouvoir</strong>, "
                  "<strong>devoir en savoir</strong>, en <strong>aller en venir</strong>. <strong>Na "
                  "vouloir, pouvoir en devoir volgt een infinitief</strong>: <strong>Ils ne peuvent pas "
                  "venir.</strong> En <em>Nous <strong>allons</strong> à l'école à pied.</em>"),
            ("p", "Een <strong>onpersoonlijk werkwoord</strong> is <strong>een werkwoord dat enkel "
                  "<em>il</em> bij zich heeft</strong>: <em>il pleut</em>, <em>il neige</em>, en vooral "
                  "<strong>il faut</strong>, dat het moet of men moet betekent."),
        ]),
        dict(kop="De impératif", blokken=[
            ("p", "<strong>De impératif van <em>parler</em> voor <em>tu</em> is <em>parle</em>, zonder s "
                  "en zonder <em>tu</em>.</strong> Bij werkwoorden op -er valt de s weg; bij de andere "
                  "blijft hij: <em>finis</em>."),
            ("p", "Juist gevormd: <strong>Écoute bien !</strong>, <strong>Finis ton assiette !</strong> en "
                  "<strong>Prenons le bus.</strong>"),
            ("p", "<strong>In een Frans bevel zet je het persoonlijk voornaamwoord niet voor het "
                  "werkwoord.</strong> Het onderwerp verdwijnt helemaal, en een voorwerpsvoornaamwoord "
                  "komt erachter met een streepje: <em>donne-le</em>."),
        ]),
        dict(kop="De toekomst", blokken=[
            ("p", "De <strong>futur proche</strong> is <strong>aller plus een infinitief</strong>: "
                  "<em>Demain, je <strong>vais travailler</strong>.</em> Hij klinkt dichterbij en staat "
                  "vaker in spreektaal."),
            ("p", "De <strong>futur simple</strong> plakt uitgangen aan de infinitief: -rai, <strong>-ras</strong>, "
                  "-ra, -rons, -rez, -ront. Voor <em>je</em> is dat <strong>-rai</strong>."),
            ("p", tabel(["infinitief", "futur simple"],
                        [["aller", "j'irai"], ["être", "je serai"], ["avoir", "j'aurai"],
                         ["faire", "je ferai — il fera"], ["venir", "je viendrai"],
                         ["pouvoir", "je pourrai"]])),
            ("p", "<strong>De futur simple en de conditionnel présent hebben dezelfde stam.</strong> Enkel "
                  "de uitgangen verschillen, en dat scheelt je het halve werk."),
            ("kader", "<strong>Na <em>quand</em> gebruikt het Frans voor de toekomst niet de tegenwoordige "
                      "tijd, anders dan het Nederlands.</strong> Wij zeggen <em>als ik groot ben</em>, het "
                      "Frans zegt <strong>Quand je serai grand, je serai médecin.</strong> Twee keer de "
                      "toekomende tijd. Dit is de fout die Nederlandstaligen hier het vaakst maken."),
            ("p", "In <em>quand j'aurai fini, je t'appellerai</em> staan <strong>de futur antérieur en de "
                  "futur simple</strong>: eerst wat af moet zijn, dan wat daarna komt."),
            ("p", "<em>Être en train de</em> plus een infinitief betekent <strong>juist bezig zijn met "
                  "iets</strong>: <em>je suis en train de lire</em>."),
        ]),
        dict(kop="De conditionnel", blokken=[
            ("p", "De <strong>conditionnel présent</strong> gebruik je <strong>voor een hoffelijke vraag "
                  "of een veronderstelling</strong>: <em>Je <strong>voudrais</strong> un café, s'il vous "
                  "plaît.</em>"),
            ("p", tabel(["zin met si", "welke tijden", "wat ze zegt"],
                        [["Si j'ai le temps, je viendrai.", "présent + futur", "goed mogelijk"],
                         ["Si j'avais le temps, je viendrais.", "imparfait + conditionnel",
                          "onwaarschijnlijk"],
                         ["Si j'avais eu le temps, je serais venu.",
                          "plus-que-parfait + conditionnel passé", "te laat, het is voorbij"]])),
            ("p", "<strong>Na <em>si</em> mag in het Frans geen conditionnel staan.</strong> Het is nooit "
                  "<em>si je voudrais</em>; het is <em>si je voulais</em>. De conditionnel staat altijd in "
                  "de andere helft van de zin."),
            ("p", "De <strong>conditionnel passé</strong> dient <strong>om spijt uit te drukken over "
                  "vroeger</strong>: <em>J'<strong>aurais</strong> dû partir plus tôt.</em> En <em>tu "
                  "aurais pu me prévenir</em> betekent <strong>je had me kunnen verwittigen</strong>: een "
                  "verwijt, hoffelijk verpakt."),
        ]),
        dict(kop="De subjonctif", blokken=[
            ("p", "<strong>De subjonctif van een regelmatig werkwoord maak je uit de ils-vorm plus -e, "
                  "-es, -e</strong> (en -ions, -iez, -ent): <em>ils parlent</em> wordt <em>que je "
                  "parle</em>."),
            ("p", "Hij volgt na een wil, een gevoel, een noodzaak of een twijfel: <strong>il faut "
                  "que</strong>, <strong>je veux que</strong> en <strong>je suis content que</strong>, en "
                  "ook na <em>bien que</em>, <em>pour que</em> en <em>à moins que</em>."),
            ("p", "Juist gebruikt: <strong>Je veux qu'il vienne.</strong>, <strong>Bien qu'il soit tard, "
                  "je reste.</strong> en <strong>Il faut que nous partions.</strong> De subjonctif van "
                  "<em>être</em> is <strong>sois</strong>, en <em>Il faut que tu <strong>fasses</strong> "
                  "tes devoirs.</em>"),
            ("p", "Twee plaatsen waar hij juist níét staat. <strong>Na <em>après que</em> staat geen "
                  "subjonctif</strong> maar de indicatif: wat na iets komt, is al gebeurd, dus er valt "
                  "niets te betwijfelen (anders dan na <em>avant que</em>). En <strong>na <em>je pense "
                  "que</em> staat in een bevestigende zin geen subjonctif</strong>: <em>je pense qu'il "
                  "vient</em>. Pas in de ontkenning of de vraag kan hij opduiken."),
        ]),
        dict(kop="De gérondif", blokken=[
            ("p", "<strong>Het participe présent maak je uit de nous-vorm plus -ant</strong>: <em>nous "
                  "lisons</em> wordt <em>lisant</em>. De <strong>gérondif</strong> is dat met "
                  "<strong>en</strong> ervoor."),
            ("p", "<strong>Je gebruikt de gérondif voor twee handelingen tegelijk</strong>, door dezelfde "
                  "persoon: <strong>En lisant le journal, elle buvait du café.</strong> En <em>en sortant, "
                  "il a fermé la porte</em> betekent <strong>bij het buitengaan sloot hij de deur</strong>."),
            ("p", "<strong>In <em>c'est un livre intéressant</em> is <em>intéressant</em> een participe "
                  "présent dat als bijvoeglijk naamwoord gebruikt wordt.</strong> Dan komt het ook "
                  "overeen in geslacht en getal: <em>une histoire intéressante</em>. Als gérondif, met "
                  "<em>en</em>, verandert het nooit."),
        ]),
        spreken("zeg in het Frans drie dingen die je zou doen als je een maand vrij had, en drie dingen "
                "die moeten gebeuren voor je examen, met il faut que erbij."),
    ])


# ───────────────────────── 13. Zinsbouw, indirecte rede en de passieve zin
zet("zinsbouw-indirecte-rede-en-de-passieve-zin",
    titel="Zinsbouw, indirecte rede en de passieve zin",
    onder="De zinsdelen, drie manieren om een vraag te stellen, de ontkenningen, iemands woorden weergeven en de passieve zin.",
    secties=[
        dict(kop="De zinsdelen", blokken=[
            ("p", "De fiche vraagt dat je <strong>het onderwerp</strong>, <strong>de persoonsvorm</strong> "
                  "en <strong>het lijdend en het meewerkend voorwerp</strong> kan aanwijzen."),
            ("p", "In <em>Marie lit un livre</em> is <strong>un livre</strong> het lijdend voorwerp. Het "
                  "Frans kort dat af als <strong>COD</strong>, complément d'objet direct; het meewerkend "
                  "voorwerp is de COI."),
        ]),
        dict(kop="Soorten zinnen", blokken=[
            ("p", "<strong>De vakfiche noemt zes soorten zinnen.</strong>"),
            ("p", tabel(["soort", "voorbeeld"],
                        [["déclarative", "Il pleut."],
                         ["interrogative", "Est-ce qu'il pleut ?"],
                         ["impérative", "Viens ici !"],
                         ["exclamative", "Quelle belle journée !"],
                         ["affirmative", "Je viens."],
                         ["négative", "Je ne viens pas."]])),
            ("p", "<em>Quelle belle journée !</em> is dus <strong>een uitroepende zin</strong>. En "
                  "<strong>een zin kan tegelijk vragend en ontkennend zijn</strong>: de laatste twee zijn "
                  "vormen, geen soorten die elkaar uitsluiten. <em>Tu ne viens pas ?</em> is allebei."),
        ]),
        dict(kop="Drie manieren om een vraag te stellen", blokken=[
            ("p", tabel(["manier", "voorbeeld", "register"],
                        [["met de stem omhoog", "Tu viens ?", "spreektaal"],
                         ["met est-ce que", "Est-ce que tu viens ce soir ?", "gewoon"],
                         ["met omkering", "Viens-tu ? Où habites-tu ?", "schrijftaal"]])),
            ("p", "<strong><em>Tu viens ?</em> is niet formeler dan <em>Viens-tu ?</em></strong>, maar "
                  "juist losser. De omkering is de meest formele van de drie, en in schrijftaal schrijf je "
                  "dus <strong>Où habites-tu ?</strong>"),
            ("p", "<em><strong>Est</strong>-ce que tu viens ce soir ?</em> Het is <em>est-ce que</em>, uit "
                  "<em>est-ce que</em>: letterlijk is het dat dat."),
        ]),
        dict(kop="De ontkenningen", blokken=[
            ("p", "Een gewone ontkenning maak je met <strong>ne en pas rond de persoonsvorm</strong>. In "
                  "een samengestelde tijd staan ze rond het hulpwerkwoord: <strong>Je ne l'ai jamais "
                  "vu.</strong>"),
            ("p", tabel(["ontkenning", "betekenis"],
                        [["ne … pas", "niet"],
                         ["ne … rien", "niets: Je ne vois rien."],
                         ["ne … personne", "niemand: Il n'y a personne."],
                         ["ne … jamais", "nooit: Elle ne vient jamais."],
                         ["ne … plus", "niet meer"],
                         ["ne … que", "maar, slechts"]])),
            ("p", "<strong><em>Je ne bois que de l'eau</em> betekent niet dat je helemaal geen water "
                  "drinkt</strong>, maar juist dat je niets anders dan water drinkt. <em>Ne … que</em> is "
                  "geen ontkenning maar een beperking, en dat is een van de hardnekkigste misverstanden "
                  "van het Frans."),
            ("p", "<em>Il ne reste plus rien</em> betekent <strong>er is niets meer over</strong>. En "
                  "<strong>jamais</strong> is nooit: <em>elle ne vient jamais</em>."),
            ("p", "Op een ontkennende vraag antwoord je bevestigend met <strong>Si.</strong> Niet met "
                  "<em>oui</em>: dat woordje van twee letters bestaat in het Frans precies hiervoor."),
            ("p", "<strong>Een bijwoord van tijd zoals <em>souvent</em> staat meestal achter de "
                  "persoonsvorm</strong>, en <strong>in een samengestelde tijd staat het tussen het "
                  "hulpwerkwoord en het deelwoord</strong>: <em>J'ai <strong>souvent</strong> pensé à "
                  "toi.</em>"),
        ]),
        dict(kop="Nevenschikking en onderschikking", blokken=[
            ("p", "<strong>Het verschil: nevenschikking zet gelijke delen naast elkaar</strong>, "
                  "onderschikking hangt een bijzin onder een hoofdzin."),
            ("p", "De nevenschikkende voegwoorden zijn <strong>et</strong>, <strong>mais</strong> en "
                  "<strong>ou</strong>. <strong>Ou</strong> betekent of, zoals in <em>thé ou café</em>. De "
                  "fiche noemt ook <strong>or</strong>, dat want of echter betekent en een redenering een "
                  "wending geeft."),
            ("p", "<strong>Na <em>pour que</em> en <em>à moins que</em> volgt een subjonctif.</strong>"),
        ]),
        dict(kop="De indirecte rede", blokken=[
            ("p", "Een <strong>indirecte vraag</strong> is <strong>een vraag in een bijzin</strong>. "
                  "<strong><em>Est-ce que</em> wordt daarin <em>si</em></strong>: <em>Est-ce que tu "
                  "viens ?</em> wordt <em>Il me demande <strong>si</strong> je viens.</em>"),
            ("p", "Bij het omzetten verandert er meer: <strong>de persoon van het werkwoord</strong>, "
                  "<strong>de bezittelijke voornaamwoorden</strong> en <strong>de tijd als de inleiding in "
                  "het verleden staat</strong>."),
            ("p", tabel(["directe rede", "indirecte rede, na een inleiding in het verleden"],
                        [["Je viens.", "Il a dit qu'il venait. (présent → imparfait)"],
                         ["J'ai fini.", "Il a dit qu'il avait fini. (passé composé → plus-que-parfait)"],
                         ["Je viendrai demain.", "Elle a dit qu'elle viendrait le lendemain."],
                         ["demain", "le lendemain"],
                         ["hier", "la veille"]])),
            ("p", "<strong>Staat de inleiding in het verleden, dan schuift een présent in de indirecte "
                  "rede naar de imparfait.</strong> En ook de tijdwoorden schuiven mee: <strong>demain "
                  "wordt le lendemain</strong>."),
        ]),
        dict(kop="De passieve zin", blokken=[
            ("p", "Een passieve zin is <em>être</em> plus het deelwoord, met <strong>par</strong> voor de "
                  "handelende persoon. <em>Le facteur apporte le courrier</em> wordt <strong>Le courrier "
                  "est apporté par le facteur.</strong>"),
            ("p", "<strong>In een passieve Franse zin blijft het deelwoord niet onveranderd.</strong> Het "
                  "komt overeen met het onderwerp, want het staat bij <em>être</em>: <em>La lettre est "
                  "<strong>écrite</strong></em>, <em>Les lettres sont <strong>écrites</strong></em>."),
            ("p", "In de passieve vorm staan: <strong>Le pont a été construit en 1920.</strong>, "
                  "<strong>La décision sera prise demain.</strong> en <strong>Ce livre est lu "
                  "partout.</strong>"),
            ("p", "<strong>Krantenartikels gebruiken volgens de fiche vaak de passieve vorm omdat de "
                  "handelende persoon onbekend of onbelangrijk is.</strong> Wat telt, is wat er gebeurd "
                  "is."),
            ("p", "<strong>Het Frans vermijdt <em>on</em> niet en gebruikt in spreektaal juist niet "
                  "altijd de passieve vorm.</strong> Integendeel: waar het Engels een passieve zin "
                  "neerzet, kiest het Frans meestal <em>on</em>. <em>On m'a dit que le musée était "
                  "fermé</em> is <strong>men heeft me gezegd dat het museum dicht was</strong>."),
        ]),
        spreken("vertel in het Frans wat iemand je deze week gezegd heeft, in de indirecte rede, en let "
                "op hoe de tijden een stap terugschuiven."),
    ])
