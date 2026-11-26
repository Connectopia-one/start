# -*- coding: utf-8 -*-
"""Ready wetenschap en techniek: Stoffen en materialen (vast, vloeibaar, gas; smelten,
bevriezen, verdampen; drijven en zinken; magneten; eigenschappen van materialen)."""
from vr import mk, inv, wn

TITEL = "Stoffen en materialen"
UITLEG_1 = "Vast, vloeibaar of gas: ijs, water, damp."
UITLEG_2 = "Drijven, zinken, magneten en materialen."

DEEL_1 = [
    mk("Ijs is water in welke vorm?", ["vast", "vloeibaar", "gas", "poeder"], 0, "IJs is hard en houdt zijn vorm: het is vast."),
    mk("Wat gebeurt er met ijs in de zon?", ["Het smelt.", "Het bevriest.", "Het wordt harder.", "Het wordt zand."], 0, "Door de warmte smelt ijs en wordt het water."),
    inv("Water dat heel heet wordt, verandert in ___. (d...)", ["damp", "waterdamp", "stoom"], "Kokend water wordt waterdamp, een gas."),
    wn("Water bevriest bij 0 °C.", True, "Bij 0 °C en kouder wordt water ijs."),
    mk("Welke stof is vloeibaar?", ["melk", "steen", "hout", "lucht"], 0, "Melk kan je gieten. Het neemt de vorm aan van het glas."),
    mk("Welke stof is een gas?", ["boter", "lucht", "zand", "honing"], 1, "Lucht zie je niet en vult de hele ruimte."),
    wn("Een vloeistof neemt de vorm aan van de beker waarin je ze giet.", True, "Water in een fles heeft de vorm van de fles, in een glas die van het glas."),
    mk("Wat gebeurt er met een plas water na een zonnige dag?", ["Ze verdampt.", "Ze bevriest.", "Ze wordt groter.", "Ze wordt zout."], 0, "Door de warmte verdampt het water en gaat het de lucht in."),
    wn("Chocolade smelt als je ze in je warme hand houdt.", True, "Chocolade smelt al bij lichaamswarmte."),
    inv("Als water ijs wordt, zeg je dat het ___. (b...)", ["bevriest", "bevriezen"], "Bevriezen: van vloeibaar naar vast."),
    mk("Waar komt het waterdruppeltje op een koud glas vandaan?", ["uit de lucht", "uit het glas", "uit de tafel", "uit je hand"], 0, "Waterdamp uit de lucht wordt weer water op het koude glas."),
    wn("Een steen kan je gieten zoals water.", False, "Een steen is vast. Je kan hem niet gieten."),
    mk("Wat zie je boven een pot kokend water?", ["damp", "ijs", "zand", "rook van vuur"], 0, "De damp boven de pot is waterdamp die afkoelt tot kleine druppeltjes."),
    mk("Welke rij bevat alleen vaste stoffen?", ["hout, steen, ijzer", "water, melk, olie", "lucht, damp, hout", "sap, steen, melk"], 0, "Hout, steen en ijzer houden hun vorm."),
    wn("Boter wordt vloeibaar als je ze in een hete pan legt.", True, "Door de warmte smelt de boter."),
    inv("Een ijsblokje in een glas limonade ___ na een tijdje. (s...)", ["smelt"], "Het ijs wordt warmer en smelt."),
    wn("Gas kan je in je hand vasthouden.", False, "Een gas ontsnapt. Je kan het niet vastnemen."),
    mk("Hoe maak je van water ijsblokjes?", ["in de diepvries leggen", "in de zon leggen", "opkoken", "roeren"], 0, "In de diepvries is het kouder dan 0 °C."),
    wn("In een ballon die je opblaast, zit niets.", False, "Er zit lucht in, en lucht is een gas."),
    mk("Wat gebeurt er met de natte was aan de wasdraad?", ["Het water verdampt en de was droogt.", "Het water bevriest altijd.", "De was wordt natter.", "Het water verandert in zand."], 0, "Wind en warmte laten het water verdampen."),
]

DEEL_2 = [
    mk("Wat drijft op water?", ["een kurk", "een sleutel", "een knikker", "een steen"], 0, "Een kurk is licht voor zijn grootte en blijft drijven."),
    wn("Een groot houten blok drijft.", True, "Hout drijft, ook al is het blok groot."),
    wn("Alles wat zwaar is, zinkt.", False, "Een groot schip is zwaar en drijft toch. Het hangt af van de vorm en het materiaal."),
    mk("Wat trekt een magneet aan?", ["een paperclip van ijzer", "een gom", "een houten potlood met een gommetje", "een plastic beker"], 0, "Magneten trekken ijzer en staal aan."),
    wn("Een magneet trekt ook papier aan.", False, "Papier is geen metaal. Een magneet trekt het niet aan."),
    inv("Een magneet heeft een noordpool en een ___pool.", ["zuid", "zuidpool"], "Elke magneet heeft twee polen: noord en zuid."),
    mk("Wat gebeurt er als je twee noordpolen van magneten tegen elkaar houdt?", ["Ze stoten elkaar af.", "Ze kleven aan elkaar.", "Ze smelten.", "Er gebeurt niets."], 0, "Gelijke polen stoten af, verschillende polen trekken aan."),
    mk("Welk materiaal is doorzichtig?", ["glas", "hout", "steen", "karton"], 0, "Door glas kan je kijken."),
    mk("Waarom is een pan van metaal?", ["Metaal geleidt warmte goed.", "Metaal is zacht.", "Metaal drijft altijd op water.", "Metaal is doorzichtig."], 0, "Metaal geeft de warmte van het vuur goed door aan het eten."),
    wn("Het handvat van een pan is vaak van plastic of hout, zodat je je niet verbrandt.", True, "Plastic en hout geleiden warmte slecht."),
    mk("Van welk materiaal maak je best een regenjas?", ["plastic of rubber", "papier", "dikke wollen stof", "karton"], 0, "Plastic en rubber laten geen water door: ze zijn waterdicht."),
    inv("Een stof die geen water doorlaat, noem je water___. (d...)", ["dicht", "waterdicht"], "Waterdicht: het water blijft buiten."),
    wn("Een spons zuigt water op.", True, "Een spons heeft veel gaatjes waarin water blijft zitten."),
    mk("Welk materiaal kan je recycleren in de glasbak?", ["een lege glazen fles", "een plastic zak", "een bruine bananenschil", "een batterij"], 0, "Glazen flessen en bokalen gaan in de glasbak."),
    mk("Welk voorwerp is van een natuurlijk materiaal?", ["een houten stoel", "een plastic emmer", "een nylon touw", "een glazen vaas"], 0, "Hout komt van bomen. Plastic en nylon worden in een fabriek gemaakt."),
    wn("Zout lost op in water.", True, "Roer zout in water: je ziet het niet meer, maar het water smaakt zout."),
    wn("Zand lost op in water.", False, "Zand zakt naar de bodem. Het lost niet op."),
    inv("Suiker verdwijnt in warme thee: de suiker lost ___.", ["op"], "Oplossen: de suiker is er nog, maar je ziet ze niet meer."),
    mk("Een appelsien zinkt niet, maar een gepelde appelsien wel. Wat zorgt ervoor dat ze eerst drijft?", ["de schil met luchtbelletjes", "de pitten in het midden", "het sap", "de kleur"], 0, "In de schil zitten veel luchtbelletjes, die haar laten drijven."),
    wn("Een schip van ijzer kan drijven.", True, "Door zijn holle vorm met veel lucht erin drijft een ijzeren schip."),
]
