"""Zinsdelen en samengestelde zinnen — pittig (🚀 Boost doorstroom, Nederlands).

Eigen vragen strikt binnen nl_zinsdelen, met een zelfgetekende zin in
zinsdelen waarin je op het juiste zinsdeel klikt."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

ZD = Prent("zin-in-zinsdelen", "Een zin in zinsdelen", "de zin 'Gisteren gaf de trainer van ons team elke speler een nieuw shirt' in vijf kaders")
RIJEN = [["Gisteren", "gaf", "de trainer van ons team"], ["elke speler", "een nieuw shirt"]]
POS = {}
y0 = 200
for rij in RIJEN:
    bre = [len(w) * 15 + 40 for w in rij]
    x = (1000 - (sum(bre) + 14 * (len(rij) - 1))) / 2
    for w, b in zip(rij, bre):
        ZD.rect(x, y0, b, 80, "#f3f6fb", DONKER, 12, 2)
        ZD.tekst(x + b / 2, y0 + 51, w, 26)
        POS[w] = Prent.zone(x, y0, b, 80)
        x += b + 14
    y0 += 130
U = "zin-in-zinsdelen.svg"

VRAGEN = [
    klik("Klik op het onderwerp.", U, [POS["de trainer van ons team"]], "Wie of wat gaf? De trainer van ons team: het hele stuk."),
    klik("Klik op het lijdend voorwerp.", U, [POS["een nieuw shirt"]], "Wie of wat gaf de trainer? Een nieuw shirt."),
    klik("Klik op het meewerkend voorwerp.", U, [POS["elke speler"]], "Je kan er 'aan' voor zetten: aan elke speler."),
    klik("Klik op de bijwoordelijke bepaling.", U, [POS["Gisteren"]], "Gisteren zegt iets over de tijd en is weglaatbaar."),
    klik("Klik op de persoonsvorm.", U, [POS["gaf"]], "De persoonsvorm staat in een hoofdzin op de tweede plaats."),
    tabel("Welk zinsdeel is de woordgroep in 'Mijn zus wacht al een uur op de bus'?",
          [("mijn zus", "onderwerp"), ("op de bus", "voorzetselvoorwerp"), ("al een uur", "bijwoordelijke bepaling")],
          "Het voorzetsel ligt vast bij het werkwoord: je wacht óp iets.", ["onderwerp", "voorzetselvoorwerp", "bijwoordelijke bepaling"]),
    mk("Wat onderscheidt 'op de bus' in 'Ze wacht op de bus' van 'op de bank' in 'Ze zit op de bank'?",
       ["bij 'wachten' ligt het voorzetsel vast", "'op de bank' is het lijdend voorwerp", "'op de bus' is het onderwerp van de zin", "er is geen verschil tussen de twee zinsdelen"],
       0, "'Op de bus' is een voorzetselvoorwerp, 'op de bank' een bijwoordelijke bepaling."),
    sorteer("Werkwoordelijk of naamwoordelijk gezegde?", ["werkwoordelijk", "naamwoordelijk"],
            [("De kinderen zijn moe.", "naamwoordelijk"), ("De kinderen lopen naar huis.", "werkwoordelijk"), ("Zij wordt verpleegkundige.", "naamwoordelijk"), ("Hij heeft gelachen.", "werkwoordelijk"), ("Het blijft stil.", "naamwoordelijk")],
            "Bij een koppelwerkwoord hoort een naamwoordelijk gezegde."),
    inv("Hoeveel bijwoordelijke bepalingen staan er in 'Vanochtend liep hij met zijn hond door het park'? Een getal.", ["3", "drie"], "Vanochtend, met zijn hond en door het park."),
    tabel("Klopt dit over zinsdelen?",
          [("Een zinsdeel bestaat altijd uit één woord.", F), ("Een bijwoordelijke bepaling is meestal weglaatbaar.", J), ("De persoonsvorm ontbreekt nooit in een mededelende zin.", J), ("Je verplaatst een zinsdeel altijd in zijn geheel.", J)],
          "'De hond van de buren' is één zinsdeel."),
    mk("Hoe vind je het lijdend voorwerp?",
       ["wie of wat + pv + onderwerp?", "aan wie + persoonsvorm + onderwerp?", "wanneer of waar gebeurt het in de zin?", "wie of wat + de persoonsvorm?"],
       0, "Wie of wat + persoonsvorm geeft het onderwerp."),
    casus("Een bericht van de gemeente: 'Uw aanvraag voor een parkeerkaart werd afgewezen. Het dossier wordt door de dienst mobiliteit verder behandeld.'", [
        keuze("De zinnen staan in de [[*lijdende vorm|bedrijvende vorm|gebiedende wijs]].", "Het lijdend voorwerp is onderwerp geworden."),
        keuze("In de tweede zin is 'door de dienst mobiliteit' het [[*handelend voorwerp|meewerkend voorwerp|onderwerp]].", "Wie de handeling écht uitvoert, staat in de door-groep."),
        mk("Waarom zegt de eerste zin niet wie de aanvraag afwees?",
           ["de lijdende vorm laat dat weg", "de gemeente kent de naam niet", "een parkeerkaart heeft geen naam", "het handelend voorwerp is verplicht"],
           0, "Zo verzwijg je wie besliste."),
        keuze("Het onderwerp van de eerste zin is [[*uw aanvraag voor een parkeerkaart|werd|afgewezen]].", "Wie of wat werd afgewezen?"),
    ]),
    mk("Wat is de lijdende vorm van 'De leerlingen versieren de klas'?",
       ["De klas wordt door de leerlingen versierd.", "De leerlingen worden door de klas versierd.", "De klas versiert de leerlingen.", "De leerlingen hebben de klas versierd."],
       0, "Het lijdend voorwerp wordt onderwerp."),
    sorteer("Enkelvoudig of samengesteld?", ["enkelvoudig", "samengesteld"],
            [("Hij belde aan en zij deed open.", "samengesteld"), ("Gisteren fietste ze naar school.", "enkelvoudig"), ("Ik blijf thuis omdat het regent.", "samengesteld"), ("De hond van de buren blaft.", "enkelvoudig")],
            "Tel de persoonsvormen."),
    sorteer("Nevenschikking of onderschikking?", ["nevenschikking", "onderschikking"],
            [("Ik was moe, maar ik ging toch.", "nevenschikking"), ("Ik ging toch, hoewel ik moe was.", "onderschikking"), ("Het regent, dus we blijven binnen.", "nevenschikking"), ("We blijven binnen omdat het regent.", "onderschikking")],
            "En, maar, of, want en dus zijn nevenschikkend."),
    tabel("Welke zinssoort is het?",
          [("Kom onmiddellijk hier!", "bevelend"), ("Wat is dat mooi!", "uitroepend"), ("Ga jij mee?", "vragend"), ("Het is koud.", "mededelend")],
          "Een uitroepteken maakt een zin nog niet uitroepend.", ["mededelend", "vragend", "bevelend", "uitroepend"]),
    keuze("In 'Morgen ga ik naar de markt' staat het onderwerp achter de persoonsvorm. Dat heet [[*inversie|congruentie|onderschikking]].", "Zodra iets anders vooraan staat, draait de volgorde om."),
    keuze("In 'omdat het de hele dag regende' staat de persoonsvorm [[*achteraan|op de tweede plaats|vooraan]].", "In een bijzin schuift de persoonsvorm naar achteren."),
    mk("In 'Hoewel ze ziek was, speelde ze de match uit', welk deel is de bijzin?",
       ["Hoewel ze ziek was", "speelde ze de match uit", "de match", "ze speelde"],
       0, "Onderschikkend voegwoord vooraan en de persoonsvorm achteraan."),
    sleep("In een hoofdzin staat de [[persoonsvorm]] op de tweede plaats. Staat er iets anders dan het [[onderwerp]] vooraan, dan krijg je [[inversie]].",
          ["bijzin", "lijdend voorwerp"],
          "'Morgen ga ik', niet 'Morgen ik ga'."),
    inv("Hoe noem je het zinsdeel waarop de handeling van het werkwoord overgaat? Hoogstens twee woorden.", ["lijdend voorwerp", "het lijdend voorwerp"], "Het lijdend voorwerp."),
    tabel("Is dit een nevenschikkend voegwoord?",
          [("want", J), ("omdat", F), ("dus", J), ("hoewel", F)],
          "En, maar, of, want, dus."),
    keuze("Een zin met meer dan één persoonsvorm is [[*samengesteld|enkelvoudig|lijdend]].", "Hij bestaat uit meerdere deelzinnen."),
    keuze("In 'Wie heeft het raam gebroken?' begint de vraag met een vraagwoord, maar in 'Ga jij mee?' met de [[*persoonsvorm|bijzin|bijwoordelijke bepaling]].", "Niet elke vragende zin begint met een vragend voornaamwoord."),
    keuze("Een lijdende zin kan het handelend voorwerp weglaten, want het onderwerp is al bezet door het vroegere [[*lijdend voorwerp|meewerkend voorwerp|gezegde]].", "'De ramen werden gelapt' is een volledige zin."),
    inv("Hoe noem je het koppelen van twee gelijkwaardige hoofdzinnen? Eén woord.", ["nevenschikking", "de nevenschikking"], "Nevenschikking."),
    open_("Ontleed de zin 'De buurvrouw gaf mijn broer gisteren een taart' in zinsdelen.",
          "De buurvrouw: onderwerp. Gaf: persoonsvorm en werkwoordelijk gezegde. Mijn broer: meewerkend voorwerp. Gisteren: bijwoordelijke bepaling. Een taart: lijdend voorwerp."),
]
