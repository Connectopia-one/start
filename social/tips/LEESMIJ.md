# De beelden van de tipspagina

Tien vierkante beelden van 1080 x 1080: een voorblad en de negen stappen van
`oefenplatform.connectopia.one/tips`, elk als een notitieblaadje. Samen zijn ze
één carrousel-post op Facebook of Instagram; de volgorde zit in de
bestandsnaam.

    tips-00-voorblad.png
    tips-01-kies-een-vak-en-open-een-hoofdstuk.png
    ...
    tips-09-rond-af-met-de-oefenbundel.png

## Opnieuw maken

De teksten staan niet hier maar in `oefenplatform/inhoud/tips.ts`, zodat de
beelden niet uit elkaar lopen met de pagina. Pas je daar een stap aan, dan
maak je de beelden zo opnieuw:

    cd social/tips/bron
    PW=$(npm root -g)/playwright node maak.js

Eén blad apart:

    PW=$(npm root -g)/playwright node maak.js tips-02-ga-eerst-door-de-tocht

Het script zegt per blad of de tekst binnen het blaadje past. Staat er
"LET OP" bij, kort die stap dan in op de pagina zelf; dan klopt de pagina en
het beeld allebei.

Een stap bijzetten in `tips.ts` geeft vanzelf een elfde beeld, en het
voorblad telt de bolletjes mee.
