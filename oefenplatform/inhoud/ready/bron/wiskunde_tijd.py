# -*- coding: utf-8 -*-
"""Ready wiskunde: Tijd en temperatuur (klok lezen tot op de minuut, analoog en
digitaal, kalender, tijdsduur berekenen, temperatuur in °C). Doel einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Tijd en temperatuur"
UITLEG_1 = 'Klok lezen: de kleine en de grote wijzer.'
UITLEG_2 = 'Kalender, hoe lang iets duurt en graden.'

DEEL_1 = [
    mk("De kleine wijzer staat op 3 en de grote wijzer op 12. Hoe laat is het?", ["12 uur", "drie uur", "kwart over drie", "half drie"], 1, "Grote wijzer op 12 betekent een vol uur. De kleine wijzer wijst het uur aan: drie uur."),
    mk("De grote wijzer staat op 6. Hoeveel minuten na het uur is dat?", ["6 minuten", "15 minuten", "30 minuten", "60 minuten"], 2, "Elk cijfer op de klok is 5 minuten verder: 6 × 5 = 30 minuten. Dat is half."),
    inv("1 uur = ___ minuten", "60", "Een uur heeft 60 minuten.", 60),
    mk("Hoe laat is het als de digitale klok 14.30 toont?", ["half drie 's middags", "half twee 's middags", "vier uur", "kwart over twee"], 0, "14.30 is 30 minuten na 14 uur, dus na twee uur 's middags. Dat noem je half drie."),
    wn("Kwart over vijf is 5.15 uur.", True, "Een kwartier is 15 minuten na het uur."),
    mk("Wat toont een digitale klok om kwart voor acht 's avonds?", ["7.45", "8.15", "19.45", "20.45"], 2, "Kwart voor acht is 7.45 uur. 's Avonds tel je 12 erbij: 19.45."),
    wn("Om 13.00 uur is het 1 uur 's nachts.", False, "13.00 uur is 1 uur 's middags. 1 uur 's nachts is 1.00 uur."),
    inv("Een half uur = ___ minuten", "30", "De helft van 60 minuten is 30 minuten.", 30),
    mk("De grote wijzer staat op 9 en de kleine net voor 4. Hoe laat is het?", ["kwart over vier", "kwart voor vier", "negen uur", "half vier"], 1, "Grote wijzer op 9 is 45 minuten na het uur, of nog 15 minuten tot het volgende uur: kwart voor vier."),
    inv("De grote wijzer staat op 2. Dat is ___ minuten na het uur.", "10", "2 × 5 = 10 minuten.", 10),
    wn("Een minuut heeft 100 seconden.", False, "Een minuut heeft 60 seconden."),
    mk("Hoe laat is het: 10 minuten na half zes?", ["5.40", "6.10", "5.20", "6.40"], 0, "Half zes is 5.30 uur. 10 minuten later is het 5.40."),
    inv("Hoeveel minuten zijn 2 uur? ___", "120", "2 × 60 = 120 minuten.", 120),
    wn("Om 23.59 uur is het bijna middernacht.", True, "Na 23.59 komt 0.00 uur: middernacht."),
    mk("Hoeveel uur heeft een dag?", ["12", "24", "60", "100"], 1, "Een dag en een nacht samen duren 24 uur."),
    mk("Welke tijd is het vroegst?", ["8.05", "8.50", "7.55", "9.00"], 2, "7.55 is nog voor acht uur."),
    inv("Hoeveel minuten duurt een kwartier? ___", "15", "Een kwart van 60 minuten is 15 minuten.", 15),
    wn("Vijf voor half drie is 2.25 uur.", True, "Half drie is 2.30. Vijf minuten eerder is 2.25."),
    mk("Hoe laat is het: 20 over 9 's ochtends?", ["9.20", "8.40", "21.20", "9.40"], 0, "20 minuten na 9 uur 's ochtends is 9.20."),
    wn("De kleine wijzer gaat sneller rond dan de grote wijzer.", False, "De grote wijzer gaat elk uur een keer rond. De kleine doet daar 12 uur over."),
]

DEEL_2 = [
    mk("Hoeveel maanden heeft een jaar?", ["10", "12", "30", "52"], 1, "Januari tot december: 12 maanden."),
    inv("Hoeveel dagen heeft een week? ___", "7", "Maandag tot en met zondag: 7 dagen.", 7),
    mk("Welke maand komt na april?", ["maart", "mei", "juni", "juli"], 1, "Maart, april, mei, juni."),
    wn("De maand juni heeft 31 dagen.", False, "Juni heeft 30 dagen. Juli heeft er 31."),
    mk("Vandaag is het dinsdag. Welke dag is het over 3 dagen?", ["donderdag", "vrijdag", "zaterdag", "woensdag"], 1, "Woensdag, donderdag, vrijdag."),
    inv("Hoeveel dagen hebben 3 weken? ___", "21", "3 × 7 = 21 dagen.", 21),
    wn("Februari is de kortste maand van het jaar.", True, "Februari heeft 28 dagen, of 29 in een schrikkeljaar."),
    mk("De film begint om 14.15 en eindigt om 15.45. Hoe lang duurt de film?", ["1 uur", "1 uur en 15 minuten", "1 uur en 30 minuten", "2 uur"], 2, "Van 14.15 tot 15.15 is 1 uur. Van 15.15 tot 15.45 is 30 minuten. Samen 1 uur en 30 minuten."),
    inv("De les begint om 8.30 en duurt 50 minuten. Om ___ is de les gedaan.", ["9.20", "9u20", "9:20"], "Van 8.30 tot 9.00 is 30 minuten. Nog 20 minuten erbij: 9.20."),
    mk("Tom vertrekt om 9.40 en komt aan om 10.05. Hoe lang was hij onderweg?", ["25 minuten", "35 minuten", "65 minuten", "45 minuten"], 0, "Van 9.40 tot 10.00 is 20 minuten. Nog 5 minuten erbij: 25 minuten."),
    wn("Van 11.50 tot 12.10 duurt 20 minuten.", True, "10 minuten tot 12.00 en dan nog 10 minuten."),
    inv("Het zwembad gaat open om 13.00 en sluit om 17.30. Hoeveel uur is het open? ___ uur en 30 minuten", "4", "Van 13.00 tot 17.00 is 4 uur, en dan nog 30 minuten.", 4),
    mk("Bij welke temperatuur bevriest water?", ["0 °C", "10 °C", "100 °C", "−10 °C"], 0, "Bij 0 °C wordt water ijs."),
    mk("Welke temperatuur past bij een warme zomerdag in België?", ["−5 °C", "8 °C", "28 °C", "80 °C"], 2, "Op een warme zomerdag is het rond de 25 tot 30 °C."),
    wn("−3 °C is warmer dan 2 °C.", False, "Onder nul is het kouder dan boven nul."),
    inv("Het is 's morgens 5 °C. 's Middags is het 7 graden warmer. Hoe warm is het 's middags? ___ °C", "12", "5 + 7 = 12 °C.", 12),
    mk("De thermometer zakt van 3 °C naar −2 °C. Hoeveel graden is het kouder geworden?", ["1 graad", "3 graden", "5 graden", "2 graden"], 2, "Van 3 naar 0 is 3 graden, van 0 naar −2 nog 2 graden. Samen 5 graden."),
    wn("Een gezond mens heeft een lichaamstemperatuur van ongeveer 37 °C.", True, "Ongeveer 37 °C is normaal. Bij koorts is het hoger."),
    wn("Water kookt bij 50 °C.", False, "Water kookt bij 100 °C."),
    inv("Kerstmis valt op 25 december. Nieuwjaar valt ___ dagen later.", "7", "Van 25 tot 31 december is 6 dagen, en 1 januari is de 7de dag.", 7),
]

# Prentvragen (vraag 21 tot 24), Kim 26/11.
import prent as P
PRENT_1 = [
    inv("Kijk naar de klok. Hoe laat is het?", ["3 uur", "drie uur", "3.00", "3:00", "15 uur", "15.00", "15:00", "3u", "15u"], "De grote wijzer staat op 12, de kleine op 3: het is 3 uur.", prent=P.p_klok("tijd-klok-3-00", 3, 0)),
    mk("Welk uur wijst deze klok aan?", ["half acht", "half zeven", "zeven uur", "kwart over zeven"], 0, "De grote wijzer staat op 6 (half). De kleine staat tussen 7 en 8: half acht.", prent=P.p_klok("tijd-klok-7-30", 7, 30)),
    mk("Hoe laat is het op deze klok?", ["kwart over twee", "kwart voor twee", "kwart over drie", "half drie"], 0, "De grote wijzer staat op 3 (kwart over). De kleine staat net voorbij de 2.", prent=P.p_klok("tijd-klok-2-15", 2, 15)),
    wn("De klok wijst kwart voor tien aan.", True, "De grote wijzer staat op 9 (kwart voor), de kleine staat bijna op 10.", prent=P.p_klok("tijd-klok-9-45", 9, 45)),
]
PRENT_2 = [
    mk("Hoe zeg je dit uur?", ["half zeven 's avonds", "half zes 's avonds", "zes uur 's morgens", "half negen 's avonds"], 0, "18.30 is 's avonds. 18 uur is 6 uur, en 30 minuten erbij: half zeven.", prent=P.p_digitaal("tijd-digitaal-1830", "18:30")),
    inv("Hoeveel graden wijst de thermometer aan?", ["20", "20 °C", "20 graden"], "Het rood komt tot aan 20 graden.", 20, prent=P.p_thermometer("tijd-thermo-20", 20)),
    inv("De film begint en eindigt op deze uren. Hoe lang duurt de film? (in minuten)", ["150", "150 minuten"], "Van 2 uur tot half vijf is 2 uur en 30 minuten: 60 + 60 + 30 = 150 minuten.", 150, prent=P.p_twee_klokken("tijd-film", 2, 0, 4, 30)),
    wn("Bij deze temperatuur kan water bevriezen.", True, "De thermometer staat op 0 graden. Bij 0 graden begint water te bevriezen.", prent=P.p_thermometer("tijd-thermo-0", 0)),
]
