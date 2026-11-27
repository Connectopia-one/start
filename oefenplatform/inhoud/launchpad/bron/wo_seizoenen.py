# -*- coding: utf-8 -*-
"""Launchpad WO: de vier seizoenen en het weer."""
from lp import K, I, W
import lpprent as P

TITEL = "Seizoenen en weer"
UITLEG_1 = "Lente, zomer, herfst en winter."
UITLEG_2 = "Zon, regen, wind en sneeuw: wat trek je aan?"

DEEL_1 = [
    K("In welk seizoen komen de eerste bloemen en blaadjes?", "de lente", ["de zomer", "de herfst", "de winter"], "In de lente komt alles weer tot leven.", None),
    K("In welk seizoen is het meestal het warmst?", "de zomer", ["de lente", "de herfst", "de winter"], "In de zomer is het het warmst.", None),
    K("In welk seizoen vallen de blaadjes?", "de herfst", ["de lente", "de zomer", "de winter"], "In de herfst kleuren en vallen de bladeren.", None),
    K("In welk seizoen kan het sneeuwen?", "de winter", ["de zomer", "de lente", "de herfst"], "In de winter is het koud en kan het sneeuwen.", None),
    K("Welk seizoen komt na de lente?", "de zomer", ["de winter", "de herfst", "nog eens de lente"], "Lente, zomer, herfst, winter.", None),
    K("Welk seizoen komt na de herfst?", "de winter", ["de lente", "de zomer", "nog eens de herfst"], "Na de herfst komt de winter.", None),
    K("Wanneer heb je de lange zomervakantie?", "in de zomer", ["in de winter", "in de herfst", "in de lente"], "Juli en augustus: zomervakantie.", None),
    K("Wat raap je in de herfst in het bos?", "kastanjes", ["sneeuwballen", "paaseieren", "aardbeien"], "In de herfst vallen kastanjes en eikels.", None),
    K("In welk seizoen is Kerstmis?", "de winter", ["de zomer", "de lente", "de herfst"], "Kerstmis is op 25 december, in de winter.", None),
    K("In welk seizoen komen de lammetjes?", "de lente", ["de herfst", "de winter", "de zomer"], "In de lente worden veel jonge dieren geboren.", None),
    I("Hoeveel seizoenen zijn er? ___", 4, "Lente, zomer, herfst en winter.", 4),
    W("In de winter zijn de dagen kort.", True, "In de winter wordt het vroeg donker."),
    W("In de zomer sneeuwt het vaak.", False, "In de zomer is het warm. Sneeuw zie je in de winter."),
    W("Na de winter komt de lente.", True, "Winter, lente, zomer, herfst."),
    W("In de herfst krijgen de bomen nieuwe blaadjes.", False, "In de herfst vallen ze. Nieuwe blaadjes komen in de lente."),
    W("Sommige vogels vliegen in de herfst naar het warme zuiden.", True, "Zwaluwen vliegen naar Afrika."),
    W("De egel slaapt in de zomer een winterslaap.", False, "De egel slaapt in de winter."),
    W("In de zomer zijn de dagen lang.", True, "In de zomer blijft het lang licht."),
    W("De lente begint in december.", False, "De lente begint in maart."),
    K("Wat zie je in de winter vaak op het water van een vijver?", "ijs", ["bloemen", "zand", "blaadjes die groeien"], "Als het vriest, wordt water ijs.", None),
]

DEEL_2 = [
    K("Het regent. Wat neem je mee?", "een paraplu", ["een zonnebril", "een zwempak", "een slee"], "Een paraplu houdt je droog.", None),
    K("Het sneeuwt. Wat trek je aan?", "een warme jas en handschoenen", ["een korte broek en een T-shirt", "slippers", "een zwempak"], "In de sneeuw is het koud.", None),
    K("De zon schijnt fel. Wat smeer je op je huid?", "zonnecrème", ["boter", "tandpasta", "zeep"], "Zonnecrème beschermt tegen verbranden.", None),
    K("Wat trek je aan als het regent?", "laarzen en een regenjas", ["sandalen en een dun T-shirt", "een badmuts", "pantoffels"], "Zo blijf je droog.", None),
    K("Waarmee meet je hoe warm het is?", "een thermometer", ["een meetlat", "een weegschaal", "een klok"], "Een thermometer toont de temperatuur.", None),
    K("Wat zie je soms als de zon schijnt terwijl het regent?", "een regenboog", ["sneeuw", "de volle maan", "sterren"], "Zon en regen samen geven een regenboog.", None),
    K("Wat kan je doen als het hard waait?", "vliegeren", ["sneeuwballen gooien", "een zandkasteel bouwen in de regen", "schaatsen op het gras"], "De wind duwt de vlieger omhoog.", None),
    K("Wat valt uit de wolken als het regent?", "waterdruppels", ["zand", "blaadjes", "kleine steentjes"], "Regen is water uit de wolken.", None),
    W("Bij onweer zie je bliksem en hoor je donder.", True, "Eerst zie je de flits, dan hoor je de knal."),
    W("Als het vriest, wordt water warm.", False, "Als het vriest, wordt water ijs."),
    W("Sneeuw is koud.", True, "Sneeuw is bevroren water."),
    W("Met een zonnebril blijf je droog in de regen.", False, "Een zonnebril beschermt je ogen tegen fel licht."),
    W("Wolken kunnen regen brengen.", True, "Uit grijze wolken komt vaak regen."),
    W("Bij mist kan je heel ver kijken.", False, "Bij mist zie je maar een klein stukje."),
    W("Het weerbericht vertelt welk weer het wordt.", True, "Op tv, radio of gsm."),
    W("Een regenboog heeft maar één kleur.", False, "Een regenboog heeft veel kleuren."),
    I("Het is 5 graden. Morgen is het 3 graden warmer. Hoeveel graden is het morgen? ___", 8, "5 + 3 = 8.", 8),
    K("Welk weer is goed om een sneeuwman te maken?", "als er sneeuw ligt", ["als het heel warm is", "als het regent", "als het waait zonder sneeuw"], "Zonder sneeuw geen sneeuwman.", None),
    K("Waar schuil je best bij onweer?", "binnen in huis", ["onder een hoge boom", "op een open veld", "in het water"], "Binnen ben je veilig.", None),
    K("Welk weer hoort bij een strandvakantie?", "zon", ["sneeuw", "hagel", "storm"], "Op het strand wil je zon.", None),
]

PRENT_1 = [
    K("Welk seizoen zie je?", "de winter", ["de zomer", "de lente", "de herfst"], "Sneeuw, mutsen en sjaals: het is winter.", None, prent=P.een("seizoen-sneeuw", "lp-sneeuw")),
    K("Wat smeert het meisje op haar huid?", "zonnecrème", ["boter", "tandpasta", "zeep"], "Zonnecrème beschermt je huid tegen de zon.", None, prent=P.een("seizoen-zomer", "lp-zomer")),
    W("Op de prent is het herfst.", True, "De bladeren zijn geel en oranje en vallen.", prent=P.een("seizoen-herfst", "boom-herfst")),
    K("Welk weer is het?", "het waait", ["het sneeuwt", "het is mistig", "het onweert"], "De vlieger vliegt hoog en de blaadjes waaien weg.", None, prent=P.een("seizoen-wind", "lp-wind")),
]
PRENT_2 = [
    K("Wat heeft het kind aan zijn voeten?", "laarzen", ["sandalen", "pantoffels", "slippers"], "Met regenlaarzen kan je in een plas springen.", None, prent=P.een("seizoen-plas", "lp-kind-springt-plas")),
    W("De boom op de prent staat in de winter.", False, "De boom bloeit: het is lente.", prent=P.een("seizoen-lente", "boom-lente")),
    W("Het regent op de prent.", True, "Je ziet regendruppels.", prent=P.een("seizoen-regen", "regen")),
    K("In welk seizoen zie je de egel tussen de gevallen bladeren?", "de herfst", ["de zomer", "de lente", "de winter"], "Gevallen bruine en oranje bladeren: herfst.", None, prent=P.een("seizoen-egel", "lp-egel")),
]
