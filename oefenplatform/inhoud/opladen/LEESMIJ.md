# De opladpagina

`maak_opladen.py` bouwt de pagina waarmee Kim de vragen en de leerbundels van
de Boost-vakken in Beheer krijgt. Ze staat als artifact op
https://claude.ai/artifact/CZYquvqtGW5JBiJYzvGi8N en wordt daar ter plekke
vervangen, zodat de link en haar vinkjes blijven werken.

    python3 -I maak_opladen.py

Dat schrijft `opladen.html` ernaast, ongeveer 2,5 MB. Publiceer dat bestand op
de bestaande artifact-link; de grens van een artifact is 16 MB.

Twee dingen om te onthouden:

- **De vragen staan in de pagina zelf**, in een `<script type="text/plain">`,
  zodat één klik ze op het klembord zet. Een link naar raw.githubusercontent
  opent een bladzijde, en dan moet Kim bewaren, terugzoeken en alsnog openen.
  Zij vroeg uitdrukkelijk om de kopieerknop. Een link blijft enkel over voor
  wat je niet kan plakken: de zip met leerbundels.
- **De cijfers op de knoppen worden geteld**, niet overgetypt: het script leest
  de hoofdstukken en de vragen uit het json-bestand en de pdf's uit de zip. Zo
  kan er op de knop niets staan wat niet in het bestand zit.

De zip-knoppen wijzen naar de werktak. Staat het werk op een andere tak, pas
dan `TAK` bovenaan het script aan.
