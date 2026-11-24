"""Rekenen met mol, massa en concentratie — pittig (🚀 Boost doorstroom, chemie).

Rekenvragen van natuurwetenschappen Boost doorstroom, plus eigen meerstapsvragen over molaire massa, getal van Avogadro, concentratie, verdunnen en stoichiometrie uit ch_rekenen. Atoommassa's op 0,1 afgerond."""
from ..boost_do_nw_themas import water as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [14, 15, 16, 17, 18, 19, 24])
VRAGEN += [
    casus("Een fles bevat 500 ml van een glucoseoplossing (C₆H₁₂O₆) met 45,0 g glucose. Gebruik C 12,0, H 1,0 en O 16,0.", [
        inv("Wat is de molaire massa van glucose in g/mol?", ["180", "180,0", "180 g/mol"],
            "6 · 12,0 + 12 · 1,0 + 6 · 16,0 = 72 + 12 + 96 = 180,0 g/mol."),
        inv("Hoeveel mol glucose zit er in de fles?", ["0,25", "0,250", "0.25"],
            "n = m / M = 45,0 / 180 = 0,250 mol."),
        inv("Wat is de molaire concentratie in mol/l?", ["0,5", "0,50", "0,500", "0.5"],
            "c = n / V = 0,250 mol / 0,500 l = 0,500 mol/l."),
    ]),
    inv("Wat is de molaire massa van CaCO₃ in g/mol? Gebruik Ca 40,1, C 12,0 en O 16,0.", ["100,1", "100.1"],
        "40,1 + 12,0 + 3 · 16,0 = 100,1 g/mol."),
    mk("Hoeveel moleculen zitten er in 2,00 mol water?",
       ["1,20 · 10²⁴", "6,02 · 10²³", "3,01 · 10²³", "36,0"], 0,
       "N = n · Nₐ = 2,00 · 6,02 · 10²³ = 1,204 · 10²⁴."),
    casus("Je hebt 200 ml van een oplossing van 2,0 mol/l keukenzout. Je verdunt ze tot 1,0 l.", [
        inv("Wat is de nieuwe concentratie in mol/l?", ["0,4", "0,40", "0.4"],
            "c₁V₁ = c₂V₂: 2,0 · 0,200 = c₂ · 1,0, dus c₂ = 0,40 mol/l."),
        tabel("Klopt dit over het verdunnen?",
              [("De stofhoeveelheid keukenzout blijft gelijk.", J), ("Het volume wordt vijf keer groter.", J), ("De concentratie wordt vijf keer groter.", F)],
              "Bij verdunnen voeg je enkel water toe: evenveel mol in meer volume."),
    ]),
    casus("Magnesium verbrandt volgens 2 Mg + O₂ → 2 MgO. Je laat 4,86 g magnesium volledig reageren. Gebruik Mg 24,3 en O 16,0.", [
        inv("Hoeveel mol magnesium is dat?", ["0,2", "0,20", "0,200", "0.2"],
            "n = 4,86 / 24,3 = 0,200 mol."),
        inv("Hoeveel mol MgO ontstaat er?", ["0,2", "0,20", "0,200", "0.2"],
            "Volgens de coëfficiënten geeft 2 mol Mg 2 mol MgO: dezelfde stofhoeveelheid."),
        inv("Hoeveel gram MgO ontstaat er?", ["8,06", "8,1", "8.06"],
            "M(MgO) = 24,3 + 16,0 = 40,3 g/mol; m = 0,200 · 40,3 = 8,06 g."),
    ]),
    tabel("Welke formule gebruik je?",
          [("massa omzetten naar mol", "n = m / M"), ("aantal deeltjes omzetten naar mol", "n = N / Nₐ"), ("concentratie berekenen", "c = n / V"), ("verdunnen", "c₁V₁ = c₂V₂")],
          "Vier formules die je moet kunnen kiezen en gebruiken.", ["n = m / M", "n = N / Nₐ", "c = n / V", "c₁V₁ = c₂V₂"]),
    mk("Een leerling berekent de massa van 3,00 mol CO₂ en schrijft 13,2 g op. Hoe weet je zonder narekenen dat dit fout is?",
       ["Eén mol weegt al 44 g, dus drie mol veel meer.", "Een massa schrijf je altijd zonder komma.", "Drie mol is minder dan één mol, dus dat klopt niet zomaar.", "De molaire massa van CO₂ is 3 g/mol."], 0,
       "Een snelle schatting toont dat de komma verschoven is: het moet 132 g zijn."),
    inv("Hoeveel gram NaOH heb je nodig voor 250 ml oplossing van 0,40 mol/l? M(NaOH) = 40,0 g/mol.", ["4", "4,0", "4,00"],
        "n = c · V = 0,40 · 0,250 = 0,10 mol; m = 0,10 · 40,0 = 4,0 g."),
    sorteer("Groter of kleiner dan één mol?", ["Meer dan 1 mol", "Minder dan 1 mol"],
            [("36 g water (M = 18 g/mol)", "Meer dan 1 mol"), ("22 g CO₂ (M = 44 g/mol)", "Minder dan 1 mol"), ("1,2 · 10²⁴ moleculen", "Meer dan 1 mol"), ("3,0 · 10²³ atomen", "Minder dan 1 mol")],
            "Vergelijk met de molaire massa of met het getal van Avogadro."),
    tabel("Klopt dit over de mol?",
          [("Eén mol water en één mol CO₂ bevatten evenveel moleculen.", J), ("Eén mol water en één mol CO₂ hebben dezelfde massa.", F), ("De stofhoeveelheid druk je uit in mol, niet in gram.", J)],
          "Evenveel deeltjes, maar elk deeltje heeft zijn eigen massa."),
    inv("Een oplossing van 0,10 mol/l moet tien keer verdund worden. Hoeveel ml water voeg je toe aan 50 ml oplossing?", ["450", "450 ml"],
        "Tien keer verdunnen: het eindvolume is 500 ml, dus 450 ml water erbij."),
    mk("Bij 2 H₂ + O₂ → 2 H₂O reageert 3,0 mol zuurstofgas volledig. Hoeveel mol water ontstaat er?",
       ["6,0 mol", "3,0 mol", "1,5 mol", "9,0 mol"], 0,
       "Per mol O₂ ontstaan 2 mol water: 2 · 3,0 = 6,0 mol."),
    sleep("De massa van één mol heet de [[molaire massa]], in [[g/mol]]. Het aantal deeltjes in één mol is het getal van [[Avogadro]].",
          ["concentratie", "mol/l"], "Drie begrippen bij het rekenen met de mol."),
    inv("Hoeveel mol zit er in 11,7 g NaCl? M(NaCl) = 58,5 g/mol.", ["0,2", "0,20", "0,200", "0.2"],
        "n = 11,7 / 58,5 = 0,200 mol."),
    mk("Welke oplossing bevat de meeste mol opgeloste stof?",
       ["2,0 l van 0,50 mol/l", "1,0 l van 0,80 mol/l", "0,50 l van 1,0 mol/l", "0,10 l van 5,0 mol/l"], 0,
       "n = c · V: 1,0 mol, 0,80 mol, 0,50 mol en 0,50 mol."),
    inv("Hoeveel mol waterstofatomen zitten er in 0,50 mol H₂O?", ["1", "1,0", "1,00", "één"],
        "Elke watermolecule heeft twee waterstofatomen: 2 · 0,50 = 1,0 mol."),
]
