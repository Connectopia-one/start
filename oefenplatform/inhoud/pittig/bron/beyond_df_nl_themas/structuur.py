"""Structuuraanduiders: verwijswoorden en signaalwoorden — pittig (Beyond dubbele finaliteit, Nederlands).

Enkele pittige vragen Nederlands Beyond doorstroom over signaalwoorden, verder eigen vragen binnen nl_structuur."""
from ..beyond_nederlands_themas import tekstopbouw as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [1, 5, 9]) + [
    casus(
        "Lees de tekst.\n\n"
        "« De gemeente wil een nieuw zwembad bouwen. Dat kost veel geld, maar volgens de burgemeester is het nodig. "
        "Het oude bad is immers vijftig jaar oud. Bovendien lekt het dak. De oppositie is het daar niet mee eens: zij wil het oude bad liever renoveren. "
        "Dat zou de helft kosten. Toch kiest de meerderheid voor nieuwbouw, want die gaat langer mee. »",
        [
            keuze("« Dat » in de tweede zin verwijst naar [[*een nieuw zwembad bouwen|de burgemeester|het oude bad]].", "Een verwijswoord kan naar een hele handeling verwijzen."),
            keuze("« zij » verwijst naar [[*de oppositie|de burgemeester|de gemeente]].", "Het laatst genoemde passende woord."),
            tabel("Welk verband geeft elk signaalwoord in de tekst aan?", [
                ("maar", "tegenstelling"), ("immers", "reden"), ("bovendien", "opsomming"), ("want", "reden"),
            ], "Immers en want geven een reden, bovendien voegt iets toe.", kolommen=["tegenstelling", "reden", "opsomming"]),
            keuze("« Dat zou de helft kosten » verwijst met « dat » naar [[*het renoveren van het oude bad|het nieuwe zwembad|het lekkende dak]].", "Het gaat over het voorstel van de oppositie."),
            mk("Welk signaalwoord kondigt de beslissing aan?",
               ["toch", "bovendien", "immers", "maar"], 0, "« Toch » zet de beslissing tegenover het argument van de oppositie."),
        ],
    ),
    koppel("Koppel elk signaalwoord aan het verband dat het aankondigt.", [
        ["kortom", "samenvatting"], ["daardoor", "gevolg"], ["mits", "voorwaarde"], ["ten slotte", "laatste stap"],
    ], ["vergelijking met een autoriteit"], "Elk signaalwoord kondigt een ander verband aan."),
    sleep("Ik had geen tijd, [[dus]] heb ik het niet gedaan. Ik deed het niet, [[want]] ik had geen tijd. [[Hoewel]] ik moe was, ging ik toch.",
          ["bovendien", "ten eerste"], "Dus geeft een gevolg, want een reden, hoewel een toegeving."),
    mk("Welke zin is dubbelzinnig door het verwijswoord?",
       ["Tom vertelde Bram dat hij gewonnen had.", "Tom vertelde dat hij zelf gewonnen had.", "De leerlingen kregen hun rapport.", "Sara las het boek en vond het mooi."], 0,
       "« Hij » kan op Tom en op Bram slaan."),
    tabel("Is dit een verwijswoord of een signaalwoord?", [
        ("deze", "verwijswoord"), ("daarom", "signaalwoord"), ("hun", "verwijswoord"), ("enerzijds", "signaalwoord"), ("die", "verwijswoord"),
    ], "Verwijswoorden wijzen terug, signaalwoorden kondigen een verband aan.", kolommen=["verwijswoord", "signaalwoord"]),
    keuze("In « De ministers vergaderden lang. Uiteindelijk bereikten [[*ze|hij|het]] een akkoord. » past het verwijswoord in getal bij de ministers.", "Meervoud vraagt een meervoudig verwijswoord."),
    mk("« Het plan is duur. Daarentegen levert het veel op. » Welk verband legt « daarentegen »?",
       ["een tegenstelling", "een opsomming", "een voorwaarde", "een tijdsvolgorde"], 0, "Daarentegen zet twee zaken tegenover elkaar."),
    volgorde("Zet de zinnen in een logische volgorde met behulp van de signaalwoorden.", [
        "Ten eerste spaart een fietsstraat geld uit.", "Daarnaast wordt de buurt veiliger.", "Tot slot is het goed voor het klimaat.", "Kortom: de fietsstraat is een goed plan.",
    ], "Ten eerste, daarnaast, tot slot en kortom tonen de gedachtegang."),
    tabel("Verwijst « dat » naar één woord of naar een hele zin?", [
        ("« Hij kocht een fiets. Dat was duur. »", "hele zin"), ("« Ik zag dat huis. Dat stond leeg. »", "één woord"),
        ("« De trein had vertraging. Dat ergerde haar. »", "hele zin"),
    ], "Een verwijswoord kan naar een woord of naar een hele gebeurtenis wijzen.", kolommen=["één woord", "hele zin"]),
    mk("Een luistertekst gebruikt vaak « ten eerste », « ten tweede » en « tot slot ». Waarom helpt dat vooral bij luisteren?",
       ["Je kan niet terugbladeren, dus de spreker toont waar je zit.", "Luisteraars begrijpen anders geen enkele andere woorden of zinnen.", "Zonder die woorden mag een spreker niet beginnen.", "Het maakt de luistertekst korter en dus ook sneller voorbij."], 0,
       "Signaalwoorden zijn wegwijzers, zeker als je niet kan teruglezen."),
    keuze("« Als » in « Als het regent, blijven we thuis » kondigt een [[*voorwaarde|tijd|vergelijking]] aan, maar in « Als kind woonde ik in Gent » betekent het [[*toen ik ... was|indien|omdat]].", "Hetzelfde signaalwoord kan een ander verband aanduiden."),
    sorteer("Kondigt dit signaalwoord een reden of een gevolg aan?", ["reden", "gevolg"], [
        ["omdat", "reden"], ["dus", "gevolg"], ["want", "reden"], ["bijgevolg", "gevolg"], ["zodat", "gevolg"], ["immers", "reden"],
    ], "Reden: waarom. Gevolg: wat eruit volgt."),
    open_("Herschrijf: « Lisa en Emma gingen naar de winkel. Lisa kocht brood. Lisa en Emma gingen daarna naar huis. Emma was moe. » Gebruik verwijswoorden en minstens één signaalwoord.",
          "Lisa en Emma gingen naar de winkel. Daar kocht Lisa brood. Daarna gingen ze naar huis, want Emma was moe.",
          "Verwijswoorden vermijden herhaling, signaalwoorden tonen het verband."),
    mk("« Hoewel de film lang was, verveelde ik me niet. » Wat zegt « hoewel »?",
       ["Er is iets dat je zou verwachten, maar het gebeurt niet.", "De film was eigenlijk heel kort en daarom niet saai.", "Ik verveelde me omdat de film lang was.", "De film eindigde veel te vroeg voor de meeste kijkers."], 0,
       "Hoewel geeft een toegeving."),
    tabel("Klopt dit over structuuraanduiders?", [
        ("Een verwijswoord staat bijna altijd na het woord waarnaar het verwijst.", J),
        ("Signaalwoorden kunnen de tekststructuur verraden.", J),
        ("Een tekst zonder signaalwoorden is altijd onbegrijpelijk.", F),
        ("Je gebruikt ze bij het lezen én bij het schrijven.", J),
    ], "Zonder signaalwoorden moet de lezer de verbanden zelf zoeken."),
    keuze("Een tekst met veel « enerzijds » en « anderzijds » heeft waarschijnlijk een [[*vergelijkingsstructuur|chronologische structuur|IMS-structuur]].", "Twee kanten tegen elkaar afwegen."),
    inv("Welk verwijswoord past: « De school kocht nieuwe laptops. ... worden maandag uitgedeeld. »", ["Ze", "ze", "Die", "die", "Deze", "deze"], "Meervoud: ze, die of deze."),
    mk("In welke zin past « bovendien » het best?",
       ["De fiets is goedkoop. ... is hij licht.", "De fiets is duur. ... koop ik hem niet.", "Het regent. ... blijf ik thuis.", "Hij is ziek. ... gaat hij naar school."], 0,
       "Bovendien voegt nog een argument in dezelfde richting toe."),
    tabel("Welke soort signaalwoord is het?", [
        ("eerst", "tijd"), ("vergeleken met", "vergelijking"), ("bijvoorbeeld", "voorbeeld"), ("daarna", "tijd"), ("net zoals", "vergelijking"),
    ], "Signaalwoorden horen bij soorten verbanden.", kolommen=["tijd", "vergelijking", "voorbeeld"]),
    mk("« Het weer was slecht. Daardoor ging de wedstrijd niet door. » Welk verband legt « daardoor »?",
       ["een gevolg", "een reden", "een voorwaarde", "een tegenstelling"], 0, "De tweede zin is het gevolg van de eerste."),
    keuze("In « Mijn broer en zijn vriend gingen vissen. Hij ving niets. » is « hij » [[*dubbelzinnig|duidelijk]].", "Hij kan op de broer en op de vriend slaan."),
    inv("Geef een signaalwoord dat een voorbeeld aankondigt.", ["bijvoorbeeld", "zoals", "zo", "onder andere", "bv."], "Bijvoorbeeld en zoals zijn de bekendste."),
    tabel("Is het verwijswoord correct gebruikt?", [
        ("« Het team won. Ze vierden het feest. »", J), ("« De leerling vergat zijn boek. Ze moest terug naar huis. »", F),
        ("« De meisjes kwamen binnen. Ze gingen zitten. »", J),
    ], "Het verwijswoord moet in getal en geslacht passen bij waarnaar het verwijst."),
]
