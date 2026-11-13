"""Juridische termen en actoren — pittig (🌍 Beyond, filosofie en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, klik
from .prentmaat import pix_zone, s_tekst, s_vak, GROEN, LICHT

# Prent: een vereenvoudigde strafzitting, met enkel actoren uit de gewone hoofdstukken.
PLAATSEN = {
    "parket": (60, 110, 230, 80, "Openbaar ministerie"),
    "rechter": (385, 110, 230, 80, "Rechter"),
    "griffier": (710, 110, 230, 80, "Griffier"),
    "getuige": (385, 270, 230, 80, "Getuige"),
    "burgerlijk": (60, 450, 250, 80, "Burgerlijke partij"),
    "advocaat": (375, 450, 250, 80, "Advocaat"),
    "beklaagde": (690, 450, 250, 80, "Beklaagde"),
}


def _zaal():
    d = ['<rect x="30" y="90" width="940" height="120" rx="18" fill="#efe9d8" stroke="#b9b29c" stroke-width="2"/>']
    for x, y, w, h, t in PLAATSEN.values():
        d.append(s_vak(x, y, w, h, vul=LICHT, rand=GROEN, dikte=3, rond=14))
        d.append(s_tekst(x + w / 2, y + h / 2 + 7, t, 21, vet=True))
    return d


def zone(k):
    x, y, w, h, _ = PLAATSEN[k]
    return pix_zone(x, y, w, h)


PRENTEN_EIGEN = [dict(naam="strafzitting", titel="Een strafzitting (vereenvoudigd)", eigen=_zaal)]
P = "strafzitting.svg"

VRAGEN = [
    klik("Klik op wie op deze zitting de misdrijven vervolgt namens de samenleving.", P, [zone("parket")],
         "Het openbaar ministerie, of parket, vervolgt. Het spreekt zelf geen straf uit."),
    klik("Klik op wie hier het verslag van de zitting bijhoudt en de stukken beheert.", P, [zone("griffier")],
         "De griffier is de administratieve rug van de rechtbank. Hij beslist niet mee over de uitspraak."),
    klik("Klik op wie in deze strafzaak terechtstaat.", P, [zone("beklaagde")],
         "Voor de politierechtbank en de correctionele rechtbank heet die persoon de beklaagde."),
    klik("Klik op het slachtoffer dat zich bij deze strafzaak aansloot om een schadevergoeding te vragen.", P, [zone("burgerlijk")],
         "Als burgerlijke partij rijdt de eis van het slachtoffer mee op de strafzaak."),
    klik("Klik op wie een partij bijstaat, raad geeft en op de zitting pleit.", P, [zone("advocaat")],
         "De advocaat is gebonden aan zijn beroepsgeheim."),
    klik("Klik op wie uiteindelijk oordeelt over schuld en straf.", P, [zone("rechter")],
         "Vervolgen en oordelen zijn met opzet twee verschillende rollen: het parket vervolgt, de rechter oordeelt."),
    sorteer(
        "Kom je deze actor vooral tegen in een burgerlijke zaak of in een strafzaak?",
        ["Burgerlijke zaak", "Strafzaak"],
        [
            ("De eiser", "Burgerlijke zaak"),
            ("De verweerder", "Burgerlijke zaak"),
            ("De beklaagde", "Strafzaak"),
            ("Het openbaar ministerie", "Strafzaak"),
            ("De onderzoeksrechter", "Strafzaak"),
        ],
        "Eiser en verweerder staan tegenover elkaar in een burgerlijke zaak. Parket, onderzoeksrechter en beklaagde horen bij het strafrecht.",
    ),
    koppel(
        "Verbind elke actor met zijn taak.",
        [
            ("Gerechtsdeurwaarder", "Betekent akten en voert vonnissen gedwongen uit"),
            ("Onderzoeksrechter", "Leidt een gerechtelijk onderzoek"),
            ("Griffier", "Houdt het verslag van de zitting bij"),
            ("Volksjury", "Oordeelt bij assisen over de zwaarste misdaden"),
        ],
        ["Vervolgt misdrijven namens de rechter"],
        "Elke actor heeft zijn eigen plaats in de procedure.",
    ),
    tabel(
        "Juist of fout over de actoren?",
        [
            ("De onderzoeksrechter zoekt ook naar wat de verdachte vrijpleit.", J),
            ("Het parket is een rechter die de straf bepaalt.", F),
            ("Voor het Hof van Assisen spreekt men van een beschuldigde.", J),
            ("De verweerder is de partij die een burgerlijke zaak opstart.", F),
            ("De gerechtsdeurwaarder komt zowel aan het begin als aan het einde van een burgerlijke zaak in beeld.", J),
            ("Een getuige is altijd ook een partij in de zaak.", F),
        ],
        "De onderzoeksrechter is een rechter, geen vervolger. Eiser start, verweerder verdedigt zich. Een getuige vertelt wat hij weet, zonder partij te zijn.",
        kolommen=["Juist", "Fout"],
    ),
    casus(
        "In de krant: ‘Na een gewapende overval op een tankstation leidde een onderzoeksrechter het onderzoek. De raadkamer verwees de verdachte naar de correctionele rechtbank. De uitbater van het tankstation stelde zich burgerlijke partij. De rechtbank veroordeelde de man tot drie jaar cel. Zijn advocaat kondigde aan dat hij in beroep gaat.’",
        [
            mk("Om welke rechtstak gaat het?",
               ["Burgerlijk recht", "Strafrecht", "Enkel arbeidsrecht", "Geen enkele, het is een bemiddeling"], 1,
               "Er is een misdrijf, een onderzoeksrechter en een straf: dat is strafrecht."),
            mk("Hoe heet de veroordeelde man voor de correctionele rechtbank?",
               ["De eiser", "De beklaagde", "De verweerder", "De burgerlijke partij"], 1,
               "Voor de correctionele rechtbank staat een beklaagde terecht."),
            mk("Wat vraagt de uitbater van het tankstation als burgerlijke partij?",
               ["Dat hij zelf de straf mag bepalen", "Een vergoeding voor zijn schade", "Dat de zaak geseponeerd wordt", "Dat hij in de volksjury mag zetelen"], 1,
               "Een slachtoffer sluit zich aan voor zijn schade. De straf blijft bij de rechter."),
            mk("Waar komt de zaak terecht als de man in beroep gaat?",
               ["Bij het hof van beroep", "Bij het vredegerecht", "Bij de raadkamer", "Bij de arbeidsrechtbank"], 0,
               "Tegen een vonnis van de correctionele rechtbank ga je in beroep bij het hof van beroep."),
        ],
    ),
    mk(
        "Waarom heet de tegenpartij in een strafzaak geen verweerder?",
        ["Omdat dat woord bij een burgerlijke zaak hoort",
         "Omdat de tegenpartij in een strafzaak zich niet mag verdedigen tegen het parket",
         "Omdat er in een strafzaak geen tegenpartij is",
         "Omdat de verweerder altijd het slachtoffer is"],
        0,
        "Elke procedure heeft haar eigen woorden. Eiser en verweerder in een burgerlijke zaak, beklaagde of beschuldigde in een strafzaak.",
    ),
    mk(
        "Een slachtoffer van een inbraak wil een schadevergoeding. Waarom stelt het zich liever burgerlijke partij dan een aparte burgerlijke zaak te beginnen?",
        ["Omdat het dan zelf de straf mag uitspreken",
         "Omdat zijn eis dan meerijdt op de strafzaak",
         "Omdat een burgerlijke zaak verboden is na een misdrijf",
         "Omdat de dader dan automatisch vrijgesproken wordt"],
        1,
        "Zo hoeft het slachtoffer geen tweede procedure te starten.",
    ),
    sorteer(
        "Is dit een actor of een term?",
        ["Actor", "Term"],
        [
            ("Griffier", "Actor"),
            ("Raadkamer", "Term"),
            ("Burgerlijke partij", "Actor"),
            ("Strafdossier", "Term"),
            ("Getuige", "Actor"),
            ("Minnelijke schikking", "Term"),
        ],
        "Actoren zijn mensen of instanties met een rol. Termen zijn de woorden voor stappen, stukken en beslissingen.",
    ),
    keuze(
        "Een rechtbank spreekt een [[*vonnis|arrest]] uit. Alle stukken uit een strafonderzoek samen vormen het [[*strafdossier|proces-verbaal]]. Alles wat aan het proces voorafgaat, heet het [[*vooronderzoek|onderzoek ter terechtzitting]].",
        "Vonnis, strafdossier en vooronderzoek. Het proces-verbaal is één stuk in dat dossier.",
    ),
    tabel(
        "Juist of fout over de juridische termen?",
        [
            ("Een minnelijke schikking sluit een zaak af zonder vonnis.", J),
            ("Een minnelijke schikking bestaat enkel in het strafrecht.", F),
            ("Een dagvaarding roept iemand voor de rechter.", J),
            ("Beroep betekent in het recht hetzelfde als iemands job.", F),
            ("De kamer van inbeschuldigingstelling zit bij het hof van beroep.", J),
        ],
        "Woorden uit het recht hebben een precieze betekenis, ook als ze in het dagelijks leven iets anders betekenen.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        "Je leest: ‘De kamer van inbeschuldigingstelling verwijst de verdachte naar het Hof van Assisen.’ Wat leid je daaruit af?",
        ["Het gaat om een van de zwaarste misdaden en er komt een volksjury",
         "De zaak is geseponeerd en er komt dus geen enkel proces meer",
         "Het gaat om een burgerlijk geschil tussen buren",
         "De verdachte is al definitief veroordeeld"],
        0,
        "Zo'n verwijzing gebeurt enkel bij de zwaarste misdaden. Het oordeel moet dan nog komen.",
    ),
    volgorde(
        "Zet deze termen in de volgorde waarin je ze in een strafzaak tegenkomt.",
        ["Proces-verbaal", "Vooronderzoek", "Raadkamer", "Onderzoek ter terechtzitting", "Vonnis", "Beroep"],
        "Vaststellen, onderzoeken, de rechtspleging regelen, het proces, het oordeel, en eventueel een tweede behandeling.",
    ),
    sleep(
        "In een burgerlijke zaak roept de [[eiser]] de [[verweerder]] op met een dagvaarding. De [[gerechtsdeurwaarder]] gaat ze betekenen. Op de zitting houdt de [[griffier]] het verslag bij.",
        ["beklaagde", "onderzoeksrechter"],
        "Eiser, verweerder, gerechtsdeurwaarder, griffier. Beklaagde en onderzoeksrechter horen bij een strafzaak.",
    ),
    tabel(
        "Welke rol heeft deze persoon?",
        [
            ("Een buurvrouw zag de inbraak en vertelt het op de zitting.", "Getuige"),
            ("Een man staat terecht voor de correctionele rechtbank.", "Beklaagde"),
            ("De bestolen winkelier vraagt in het strafproces zijn schade terug.", "Burgerlijke partij"),
            ("Een vrouw eist via een dagvaarding achterstallige huur.", "Eiser"),
        ],
        "Getuige, beklaagde, burgerlijke partij of eiser: de rol hangt af van wat iemand in de zaak doet.",
        kolommen=["Getuige", "Beklaagde", "Burgerlijke partij", "Eiser"],
    ),
    mk(
        "Wie beslist over een aanhouding in een gerechtelijk onderzoek?",
        ["De onderzoeksrechter", "De griffier", "De gerechtsdeurwaarder", "De burgerlijke partij"],
        0,
        "Zware dwangmaatregelen liggen bij een rechter, de onderzoeksrechter.",
    ),
    keuze(
        "De procureur leidt het [[*opsporingsonderzoek|gerechtelijk onderzoek]]. Bij assisen oordeelt een [[*volksjury|griffier]] over de schuld.",
        "Procureur en opsporingsonderzoek. Volksjury bij assisen.",
    ),
    inv(
        "Hoe heet het stuk waarmee de politie vastlegt wat ze vaststelde? Het ...",
        ["proces-verbaal", "pv", "p.v."],
        "Het proces-verbaal gaat naar het parket en komt in het strafdossier.",
    ),
    tabel(
        "Juist of fout: wie spreekt welke uitspraak uit?",
        [
            ("Het hof van beroep spreekt een arrest uit.", J),
            ("De correctionele rechtbank spreekt een arrest uit.", F),
            ("Het parket spreekt een vonnis uit.", F),
            ("Het vredegerecht spreekt een vonnis uit.", J),
        ],
        "Rechtbank: vonnis. Hof: arrest. Het parket spreekt geen uitspraken uit, het vervolgt.",
        kolommen=["Juist", "Fout"],
    ),
    mk(
        "Wat is het verschil tussen een beklaagde en een veroordeelde?",
        ["Er is geen verschil",
         "Een beklaagde staat terecht, maar is nog niet schuldig verklaard",
         "Een beklaagde is altijd het slachtoffer",
         "Een veroordeelde staat nog terecht"],
        1,
        "Zolang de rechter niet geoordeeld heeft, geldt het vermoeden van onschuld.",
    ),
    inv(
        "Hoe heet de persoon die voor het Hof van Assisen terechtstaat? De ...",
        ["beschuldigde"],
        "Voor de politierechtbank en de correctionele rechtbank is dat de beklaagde, voor assisen de beschuldigde.",
    ),
    inv(
        "Hoe heet de instantie die ook het parket genoemd wordt? Het ...",
        ["openbaar ministerie"],
        "Het openbaar ministerie vervolgt namens de samenleving, met de procureur aan het hoofd.",
    ),
    mk(
        "Wat bewaakt het beroepsgeheim van de advocaat?",
        ["Dat wat een cliënt hem toevertrouwt, bij hem blijft",
         "Dat de advocaat nooit mag pleiten",
         "Dat de rechter niet mag weten welke advocaat de beklaagde koos",
         "Dat het parket het dossier niet mag lezen"],
        0,
        "Een cliënt moet vrij kunnen spreken met wie hem verdedigt.",
    ),
]
