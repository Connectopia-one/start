# De kalender als pdf

`social-media-kalender.pdf` is de hele kalender van dertig dagen, in de huisstijl,
op A4. Die kan je gewoon doorsturen of in de Google Drive-map zetten. De
bestandsnamen van de beelden staan erin als link.

## Opnieuw maken

De tekst komt uit het kalenderdocument. Als dat verandert:

1. exporteer het document als markdown en zet het over `bron/kalender.md`;
2. `python3 bron/naar-html.py` zet dat om naar `bron/kalender.html`;
3. `PW=$(npm root -g)/playwright node bron/render.js` drukt daar de pdf van af.

`bron/sjabloon.html` is het blad waarop gedrukt wordt: daar staan de kleuren,
de fonts en de paginawissels in. `bron/naar-html.py` zet de markdown om en past
onderweg een paar dingen aan die alleen in de pdf anders moeten staan, zoals de
datum in het Nederlands.
