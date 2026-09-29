/*
  Gemaakt door inhoud/prenten/bron/maak_prenten.py — niet met de hand
  aanpassen.

  De prent die boven de vragen van een hoofdstuk staat, voor de vakken
  waar je moet beschrijven wat je ziet. De sleutel is "<vak>/<hoofdstuk>",
  allebei vereenvoudigd zoals lib/slug.ts het doet. Staat een hoofdstuk
  hier niet in, dan staat er gewoon geen prent boven de vragen.
*/

export const PRENTEN: Record<
  string,
  { url: string; breedte: number; hoogte: number }
> = {
  "frans/wat-zie-je-aan-zee": {
    url: "/prenten/frans/wat-zie-je-aan-zee.webp",
    breedte: 1200,
    hoogte: 1200,
  },
  "frans/wat-zie-je-op-de-prent": {
    url: "/prenten/frans/wat-zie-je-op-de-prent.webp",
    breedte: 1200,
    hoogte: 1200,
  },
  "samenleving-en-economie/ik-leef-samen-met-anderen-deel-1": {
    url: "/prenten/samenleving-en-economie/ik-leef-samen-met-anderen-deel-1.webp",
    breedte: 1200,
    hoogte: 1200,
  },
};
