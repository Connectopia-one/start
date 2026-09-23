# De beelden voor de social media kalender

Alle beelden zijn **vierkant, 1080 x 1080 px**, in de huisstijl van de website.
Geen schermafbeeldingen: elke post is apart getekend, met grote letters en weinig
op één prent, zodat hij leesbaar blijft op een gsm.

Alles in één keer downloaden: **`connectopia-beelden-kalender.zip`** in deze map.

| Bestand | Hoort bij |
| --- | --- |
| dag-01-winactie | Dag 1, de winactie van het oefenplatform |
| dag-05-wegwijzer | Dag 5, de wegwijzer voor ouders |
| dag-06-blog-autisme | Dag 6, blog over autisme bij begaafde kinderen |
| dag-07-externe-plusklas | Dag 7, de externe plusklas |
| dag-08-observatielijst | Dag 8, de gratis observatielijst |
| dag-11-14-15-young-engineers | Dag 11, 14 en 15, Young Engineers |
| dag-12-extra-kamp-hasselt | Dag 12 extra, het kamp in Hasselt |
| dag-13-blog-leren-leren | Dag 13, blog over leren leren |
| dag-18-prikbord | Dag 18, het prikbord |
| dag-19-blog-diep-gedacht | Dag 19, blog over hoogbegaafde vrouwen |
| dag-19-extra-kamp-genk | Dag 19 extra, het kamp in Genk |
| dag-21-waar-kan-je-terecht | Dag 21, de hele gids |
| dag-24-oefenplatform | Dag 24, het oefenplatform |
| dag-25-blog-zomer | Dag 25, blog over vakanties |
| dag-26-over-ons | Dag 26, het verhaal achter Connectopia |
| dag-29-voor-professionals | Dag 29, de pagina voor professionals |
| kamp-vierkant | Dag 4 extra, dag 25 extra en dag 28, de herfstkampen |
| extra-alles-op-een-plek | Vrij te gebruiken, de hele website in één beeld |

Op twee beelden staan kinderen: `dag-12-extra-kamp-hasselt` (een jongen van
opzij) en `dag-19-extra-kamp-genk` (twee kinderen klein en onscherp op de
achtergrond). Beide foto's komen uit `/mnt/project-files/fotos-werking/`.

## Een post aanpassen

De teksten staan allemaal in **`bron/posts.js`**. Verander daar de tekst en
render opnieuw:

```
cd bron
PW=$(npm root -g)/playwright node render.js                  alles
PW=$(npm root -g)/playwright node render.js dag-18-prikbord  één post
```

Het script zegt zelf "LET OP" als de tekst onder de groene balk schuift. Kort
dan de tekst in of haal er een kaartje uit. `bron/stijl.css` bepaalt de kleuren
en de maten; die komen van de website, dus die hoef je normaal niet aan te raken.

De zip opnieuw maken:

```
cd ..
rm -f connectopia-beelden-kalender.zip
zip -j connectopia-beelden-kalender.zip *.png *.jpg
```
