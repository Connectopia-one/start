# -*- coding: utf-8 -*-
from _basis import *
import _proef
TITEL = "Lectuur: de Belgen in de ogen van Caesar"
_t = _proef.LEESTEKST_BELGAE.split("\n\n")
_bron = _t[-1].replace("Bronnen: ", "")
BRON = "Een eigen tekst van Connectopia over het thema van de lectuuropdracht. Gebaseerd op " + _bron + " Wil je meer lezen, dan is de biografie Caesar van Adrian Goldsworthy uit de vakfiche een goede volgende stap."
INLEIDING = "Deze tekst is geen Latijn. Hij helpt je bij de lectuuropdracht over Caesar en de Belgen. Lees hem rustig en beantwoord dan de vragen."
ALINEAS = _t[:-1]
WOORDEN = Wl(("proconsul", "een gewezen consul die een provincie bestuurt"), ("Remi", "een Belgisch volk rond het huidige Reims"), ("Eburonen", "een Belgisch volk tussen Maas en Rijn"))
VRAGEN = _proef.LEESVRAGEN
VRAGEN = VRAGEN + [
    mk("Bij welke rivier vochten de Romeinen tegen de Nerviërs?",
       ["de Sabis", "de Rijn", "de Seine", "de Garonne"], 0,
       "De slag aan de Sabis (57 voor Christus). Over welke rivier het vandaag gaat, is niet helemaal zeker: vaak denkt men aan de Selle of de Samber."),
    mk("Wat doet Caesar na de nederlaag van Sabinus en Cotta?",
       ["hij verwoest het gebied van de Eburonen", "hij sluit vrede met Ambiorix", "hij keert terug naar Rome", "hij laat de Remi voortaan het gebied besturen"], 0,
       "Caesar neemt wraak en laat het gebied van de Eburonen verwoesten. Ambiorix zelf kon ontsnappen."),
    keuze("Volgens Caesar stammen de meeste Belgen af van de [[*Germanen|Grieken|Romeinen]]. Ze wonen tussen de Seine, de Marne en de [[*Rijn|Donau|Loire]].",
          "Dat schrijft Caesar in boek II, 4, waar de Remi hem informatie geven over de andere Belgische stammen."),
    tabel("Klopt dit over Caesar als bron?",
          [("Veel van wat we over de Belgen weten, komt van Caesar zelf.", J),
           ("Caesar had belang bij een bepaald beeld van zijn vijanden.", J),
           ("De Belgen hebben zelf een geschiedenis van de oorlog geschreven.", F),
           ("Caesar schreef zijn verslag pas als oude man, lang na de feiten.", F)],
          "De Belgen hebben geen eigen geschreven verslag nagelaten. Caesar schreef zijn commentarii tijdens of kort na de oorlog."),
]
