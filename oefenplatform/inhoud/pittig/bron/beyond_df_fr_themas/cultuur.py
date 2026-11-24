"""De Franstalige wereld: gewoontes en reizen — pittig (Frans, Beyond dubbele finaliteit), A2+."""
from ..beyond_fr_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Lis le message de Lien.\n\n« Coucou maman ! Je suis arrivée à Lyon hier en TGV. Je loge dans une chambre d'hôtes très propre, petit déjeuner compris. "
        "Ce matin, j'ai fait une visite guidée de la vieille ville. Ici, tout le monde fait la bise, même pour dire bonjour à des amis d'amis ! "
        "Demain, je pars à la campagne pour deux jours. Mon train de retour a un peu de retard à cause d'une grève, mais ce n'est pas grave. Bisous ! »",
        [
            keuze("Lien reisde met [[*de snelle trein|het vliegtuig|de bus]].", "Le TGV."),
            keuze("Lien slaapt [[*bij mensen thuis|in een jeugdherberg|in een groot hotel]].", "Une chambre d'hôtes."),
            keuze("« faire la bise » is [[*kussen op de wang geven|handen schudden]].", "La bise."),
            mk("Waar gaat Lien morgen naartoe?",
               ["naar het platteland", "naar het buitenland met de trein", "naar het centrum van Parijs", "naar de kust aan zee"], 0,
               "La campagne: het platteland."),
            keuze("Haar trein terug heeft vertraging door [[*een staking|het weer|een ongeval]].", "Une grève."),
        ],
    ),
    tabel("Klopt dit over de Franstalige wereld?", [
        ("In Zwitserland betaal je met de frank.", J), ("Brussel is officieel enkel Franstalig.", F),
        ("Frankrijk viert zijn nationale feestdag op 14 juli.", J), ("In Afrika spreekt men nergens Frans.", F),
    ], "Brussel is tweetalig; in Senegal, Congo en Marokko spreekt men Frans."),
    sorteer("Hoort het bij reizen of bij een maaltijd?", ["reizen", "maaltijd"], [
        ["un billet", "reizen"], ["l'entrée", "maaltijd"], ["une valise", "reizen"], ["le dessert", "maaltijd"], ["un aller-retour", "reizen"], ["l'apéritif", "maaltijd"],
    ], "Een ticket en een koffer tegenover voorgerecht, nagerecht en aperitief."),
    koppel("Koppel elk Frans reiswoord aan zijn betekenis.", [
        ["un retard", "een vertraging"], ["la frontière", "de grens"], ["un séjour", "een verblijf"], ["à l'étranger", "in het buitenland"],
    ], ["een pan"], "Une poêle is een pan."),
    koppel("Koppel elk woord aan zijn betekenis.", [
        ["la rentrée", "het begin van het schooljaar"], ["le bac", "het eindexamen"], ["les soldes", "de koopjes"], ["le périphérique", "de ringweg rond Parijs"],
    ], ["het middagmaal"], "Het middagmaal is le déjeuner."),
    mk("Je wil van Brussel naar Parijs en weer terug. Welk ticket vraag je?",
       ["un aller-retour", "un aller simple", "un séjour de trois jours", "une visite guidée de Paris"], 0, "Heen en terug."),
    mk("Hoe zeg je « We gaan met de trein naar Parijs »?",
       ["Nous allons à Paris en train.", "Nous allons à Paris avec le train.", "Nous allons à Paris par le train.", "Nous allons en Paris à train."], 0,
       "En train, zonder lidwoord."),
    mk("Hoe zeg je « Ik ga te voet »?",
       ["Je vais à pied.", "Je vais en pied.", "Je vais avec les pieds.", "Je vais par pied."], 0, "À pied, niet en."),
    mk("Je komt een bakkerij in Parijs binnen. Wat zeg je eerst?",
       ["Bonjour !", "Une baguette, vite !", "Salut, ça va ?", "Donne-moi du pain !"], 0, "Zonder bonjour klinkt een vraag onbeschoft."),
    mk("Je spreekt een onbekende oudere dame aan op straat. Hoe spreek je haar aan?",
       ["met vous", "met tu", "met haar voornaam en tu", "met salut en tu"], 0, "Een onbekende volwassene: vous."),
    mk("Welke stad ligt in Wallonië?",
       ["Namen", "Gent", "Antwerpen", "Brugge"], 0, "Namen is de hoofdstad van het Waalse Gewest."),
    inv("Hoe zeg je koffer in het Frans? Eén woord.", ["valise", "une valise", "la valise"], "Une valise."),
    inv("Hoe zeg je vliegveld in het Frans? Eén woord.", ["aéroport", "l'aéroport", "aeroport"], "L'aéroport."),
    inv("Hoe zeg je staking in het Frans? Eén woord.", ["grève", "une grève", "la grève", "greve"], "Une grève."),
    inv("Op welke dag viert Frankrijk zijn nationale feestdag? Schrijf als 14 juli.", ["14 juli"], "Le quatorze juillet."),
    keuze("« Nous avons [[*réservé|visité]] une chambre pour trois nuits. »", "Réserver: boeken."),
    keuze("« Cet été, je pars [[*à l'étranger|en étranger]]. »", "À l'étranger."),
    keuze("« Le [[*paysage|séjour]] est magnifique : des montagnes et des lacs. »", "Un paysage: een landschap."),
    keuze("« Il habite au Canada, dans la province de [[*Québec|Wallonie]], où on parle surtout français. »", "Québec is Franstalig."),
    keuze("In Canada zijn het Frans en [[*het Engels|het Duits]] officieel.", "Frans en Engels."),
    tabel("Is dit een land waar Frans een officiële taal is?", [
        ("Luxemburg", J), ("Portugal", F), ("Senegal", J), ("Zwitserland", J),
    ], "In Portugal spreekt men Portugees."),
    tabel("Hoort dit bij lichaamstaal?", [
        ("iemand aankijken als je spreekt", J), ("de woorden die je kiest", F), ("la bise bij een begroeting", J),
    ], "Lichaamstaal zegt iets zonder woorden."),
    inv("Hoe heet een vakantiehuisje op het Franse platteland? Eén woord.", ["gîte", "un gîte", "gite"], "Un gîte."),
    volgorde("Zet de gangen van een Franse maaltijd in de juiste volgorde.", [
        "l'apéritif", "l'entrée", "le plat principal", "le dessert",
    ], "Aperitief, voorgerecht, hoofdgerecht, nagerecht."),
    sleep("Nous avons pris [[le ferry]] pour aller en Corse. À l'arrivée, nous avons pris [[un car]] jusqu'à l'hôtel.",
          ["un gîte", "une poêle"], "Een veerboot en een reisbus."),
    open_("Noem in het Nederlands één verschil tussen Frankrijk en Vlaanderen dat je in deze les leerde.",
          "In Frankrijk geeft men elkaar vaak la bise, ook bij mensen die men nog niet goed kent.",
          "Bijvoorbeeld la bise, le bac of de vaste soldenperiodes."),
]
