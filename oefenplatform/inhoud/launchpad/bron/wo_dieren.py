# -*- coding: utf-8 -*-
"""Launchpad WO: dieren en planten (waar wonen ze, wat eten ze, hoe groeien ze)."""
from lp import K, I, W
import lpprent as P

TITEL = "Dieren en planten"
UITLEG_1 = "Huisdieren, boerderijdieren en wilde dieren."
UITLEG_2 = "Wat een plant nodig heeft om te groeien."

DEEL_1 = [
    K("Welk dier geeft melk?", "de koe", ["de kip", "het varken", "de eend"], "Koeien geven melk.", None),
    K("Welk dier legt eieren?", "de kip", ["de koe", "het paard", "de hond"], "Kippen leggen eieren.", None),
    K("Welk dier geeft wol?", "het schaap", ["de koe", "de kip", "de geit"], "Van de wol van een schaap maak je truien.", None),
    K("Welk dier is een huisdier?", "een kat", ["een leeuw", "een olifant", "een wolf"], "Een kat woont bij mensen thuis.", None),
    K("Waar woont een vis?", "in het water", ["in de lucht", "in een nest in de boom", "onder de grond"], "Vissen zwemmen in het water.", None),
    K("Waar woont een vogel vaak?", "in een nest", ["in een hol in het water", "in een kooi op de bodem van de zee", "in een stal met koeien"], "Veel vogels bouwen een nest.", None),
    K("Wat eet een konijn graag?", "wortels en sla", ["vlees", "vis", "chocolade"], "Konijnen eten planten.", None),
    K("Welk dier woont in het bos?", "een vos", ["een koe", "een kip", "een goudvis"], "Vossen leven in het wild, in het bos.", None),
    K("Welk dier heeft veren?", "een eend", ["een hond", "een vis", "een koe"], "Vogels hebben veren.", None),
    K("Welk dier heeft schubben?", "een vis", ["een kat", "een kip", "een paard"], "Een vis heeft schubben.", None),
    W("Een hond is een huisdier.", True, "Veel mensen hebben een hond thuis."),
    W("Een vis kan vliegen.", False, "Een vis zwemt in het water."),
    W("Een koe woont op de boerderij.", True, "Koeien leven op de boerderij en in de wei."),
    W("Een leeuw is een huisdier.", False, "Een leeuw is een wild dier."),
    W("Een jong van een kip heet een kuiken.", True, "Uit het ei komt een kuiken."),
    W("Een jong van een koe heet een veulen.", False, "Een jong van een koe is een kalf. Een veulen is een jong paard."),
    I("Hoeveel poten heeft een hond? ___", 4, "Een hond heeft 4 poten.", 4),
    I("Hoeveel poten heeft een vogel? ___", 2, "Een vogel heeft 2 poten.", 2),
    I("Hoeveel poten heeft een spin? ___", 8, "Een spin heeft 8 poten.", 8),
    K("Wat moet je doen voor je huisdier?", "eten, water en aandacht geven", ["het alleen laten", "het nooit eten geven", "het hard knuffelen tot het pijn doet"], "Een huisdier heeft zorg nodig.", None),
]

DEEL_2 = [
    K("Wat heeft een plant nodig om te groeien?", "water en licht", ["snoep en zand", "enkel een donkere plek", "een laagje plastic"], "Planten hebben water, licht en lucht nodig.", None),
    K("Welk deel van de plant zit onder de grond?", "de wortel", ["de bloem", "het blad", "de stengel"], "De wortel zit in de grond en drinkt water.", None),
    K("Welk deel van de plant is vaak gekleurd en ruikt lekker?", "de bloem", ["de wortel", "de stengel", "het zaadje"], "Bloemen hebben mooie kleuren.", None),
    K("Waaruit groeit een nieuwe plant?", "een zaadje", ["een steentje", "een blaadje plastic", "een druppel melk"], "Uit een zaadje groeit een plantje.", None),
    K("Welk deel van de plant houdt de bloem omhoog?", "de stengel", ["de wortel", "de grond", "de pot"], "De stengel is als een rietje en houdt de bloem recht.", None),
    K("Welke kleur hebben de meeste blaadjes in de zomer?", "groen", ["blauw", "zwart", "paars"], "In de zomer zijn bladeren groen.", None),
    K("Wat groeit aan een appelboom?", "appels", ["peren", "bananen", "aardappelen"], "Aan een appelboom groeien appels.", None),
    K("Welk dier helpt bloemen door van bloem naar bloem te vliegen?", "de bij", ["de vis", "de koe", "de slak"], "Bijen brengen stuifmeel van bloem naar bloem.", None),
    W("Een plant zonder water verdort.", True, "Zonder water gaat een plant dood."),
    W("Een plant groeit het best in een donkere kast.", False, "Een plant heeft licht nodig."),
    W("De wortel drinkt water uit de grond.", True, "De wortels zuigen water op."),
    W("Een boom is geen plant.", False, "Een boom is een grote plant."),
    W("Uit een zaadje kan een bloem groeien.", True, "Zaadje, plantje, bloem."),
    W("Bloemen groeien uit stenen.", False, "Bloemen groeien uit zaadjes."),
    W("Bijen maken honing.", True, "Bijen maken honing van wat ze uit bloemen halen."),
    W("Alle planten hebben bloemen.", False, "Gras en varens hebben geen gewone bloemen."),
    I("Hoeveel delen van een plant kennen we: wortel, stengel, blad en bloem? ___", 4, "Wortel, stengel, blad en bloem.", 4),
    K("Wat doe je om een plant in de klas te laten groeien?", "water geven en bij het raam zetten", ["in een donkere kast zetten en vergeten", "nooit water geven", "alle blaadjes eraf knippen"], "Water en licht.", None),
    K("Wat eet een rups?", "blaadjes", ["vlees", "brood met kaas", "zand"], "Rupsen eten bladeren.", None),
    K("Wat wordt een rups later?", "een vlinder", ["een bij", "een spin", "een vogel"], "Een rups wordt een pop en dan een vlinder.", None),
]

PRENT_1 = [
    I("Hoeveel kuikens zie je bij de kip?", 3, "Er lopen 3 kuikens bij de kip.", 3, prent=P.een("dieren-kip-kuikens", "lp-kip-kuikens")),
    K("Welk dier zie je?", "een egel", ["een muis", "een vos", "een eekhoorn"], "Een egel heeft stekels.", None, prent=P.een("dieren-egel", "lp-egel")),
    W("Dit dier woont bij het water.", True, "Een kikker woont in en bij het water.", prent=P.een("dieren-kikker", "lp-kikker")),
    K("Hoe heet het jonge dier naast de koe?", "een kalf", ["een veulen", "een lam", "een kuiken"], "Het jong van een koe is een kalf.", None, prent=P.een("dieren-koe-kalf", "koe-kalf")),
]
PRENT_2 = [
    K("Wat wordt een kikkervisje later?", "een kikker", ["een vis", "een eend", "een slak"], "Een kikkervisje krijgt pootjes en wordt een kikker.", None, prent=P.rij("dieren-kikkervisje", ["lp-kikkervisjes", "lp-kikker"])),
    K("Welk deel van deze plant is geel?", "de bloem", ["de wortel", "de stengel"], "De grote gele bloem van de zonnebloem.", None, prent=P.een("dieren-zonnebloem", "lp-zonnebloem")),
    W("De pijl wijst naar de bloem.", False, "De pijl wijst naar de wortel, onder de grond.", prent="/examenvormen/ready/planten-pijl-wortel.webp"),
    W("Een vlinder was eerst een rups.", True, "Een rups wordt een pop en dan een vlinder.", prent=P.rij("dieren-rups-vlinder", ["lp-rups", "lp-vlinder"])),
]
