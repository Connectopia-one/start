# De klikbare leerbundel

Hier staan de leerbundels van 🌱 Start nog eens, maar als gegevens in plaats van
als pdf. Het oefenplatform toont ze op het scherm als losse onderdelen waar een
kind op klikt.

**Dit komt er bij, het vervangt niets.** De pdf om af te drukken blijft gewoon
staan op dezelfde bladzijde, onder de kop "Om af te drukken of mee te nemen".
Kim vroeg dat uitdrukkelijk op 29 september 2026: de bundels om te lezen en af
te drukken blijven, en de klikbare versie is een module ernaast. Wie liever op
papier leest, kan onder de klikbare bundel zeggen dat hij de leerstof al
gelezen heeft; dan komt de puzzel meteen.

**Niet met de hand aanpassen.** De bron blijft
`inhoud/leerbundels/bron/maak_*.py`, dezelfde bestanden waar de pdf uit komt.
Verander je daar iets, draai dan:

    python3 inhoud/leerbundels/bron/maak_interactief.py

Zo kan de tekst op het scherm nooit achterlopen op de pdf.

## Hoe een hoofdstuk zijn bundel vindt

Aan de titel. Het hoofdstuk "Getallenkennis" in het vak wiskunde zoekt de
sleutel `wiskunde/getallenkennis`. Er is dus geen kolom in de databank en geen
SQL voor nodig.

Een pittig hoofdstuk deelt de bundel van het gewone hoofdstuk: " — pittig" wordt
van de titel afgehaald voor er gezocht wordt. Dezelfde leerstof, moeilijkere
vragen.

Heet de bundel net anders dan het hoofdstuk, zet dan de naam van het hoofdstuk
in de bundel zelf, bij `hoofdstukken=[...]`. Dat staat nu bij twee bundels:
"België: landschap en streken" (het hoofdstuk heet gewoon "België") en
"Spelling" (het hoofdstuk draagt nog zijn naam van bij het opzetten).

## Wat er géén bundel heeft

De zes uitdagingshoofdstukken, want die halen alle hoofdstukken door elkaar, en
de twee hoofdstukken begrijpend lezen, want daar staat de leestekst al boven de
vragen. Die hoofdstukken hebben dus ook geen slot.

## Het slot

Zie `components/HoofdstukTabs.tsx`. Heeft een hoofdstuk een klikbare bundel met
minstens drie onderdelen, dan staan de oefeningen achter een sleutel: eerst alle
onderdelen openklikken, dan de volgordepuzzel. Eenmaal open blijft het open,
bewaard in de browser van het kind.
