/*
  De opvolgfiches van de plusklas — /begeleiding

  Hieronder staan enkel de vaste teksten van die schermen. De fiches zelf
  (kinderen, opmerkingen, documenten) staan in de databank, niet in dit
  bestand. Je mag deze teksten gerust aanpassen.

  Wie deze schermen ziet: jij als beheerder, en accounts waarvan je de rol op
  "begeleider" zet via /beheer/begeleiders. Ouders en kinderen zien er niets
  van, ook niet hun eigen fiche.
*/

export const begeleidingTekst = {
  label: "Begeleiding",
  titel: "Opvolging plusklas",
  intro:
    "Hier volg je de kinderen van de plusklas apart op: hoe ver ze staan, wat jullie opvalt, en het werk dat ze thuis maakten. Alleen jij en de begeleiders zien dit scherm.",
  leegTekst:
    "Nog geen kinderen van de plusklas. Een kind verschijnt hier zodra het gezin met een plusklascode geregistreerd is en een kind toegevoegd heeft.",

  /* Het scherm van één kind. */
  fiche: {
    notitiesKop: "Opmerkingen",
    notitiesUitleg:
      "Wat jullie opvalt tijdens een sessie, een afspraak die je maakte, of wat je op een oudercontact wil zeggen. Ouders lezen dit niet mee.",
    notitiesLeeg: "Nog geen opmerkingen genoteerd.",
    documentenKop: "Werk van thuis",
    documentenUitleg:
      "Pdf's van oefeningen of opdrachten die het kind thuis maakte, om er later bij te nemen.",
    documentenLeeg: "Nog geen documenten opgeladen.",
    voortgangKop: "Voortgang op het platform",
    voortgangLeeg: "Dit kind heeft nog geen vragen beantwoord op het platform.",
    stickersKop: "Verdiende stickers",
    afdrukTekst: "Deze fiche afdrukken",
  },

  /*
    De soorten opmerking. De sleutel moet overeenkomen met wat de databank
    toelaat (zie supabase/plusklasfiche.sql), dus voeg er niet zomaar een toe.
  */
  soorten: [
    { waarde: "opmerking", label: "Opmerking" },
    { waarde: "afspraak", label: "Afspraak" },
    { waarde: "oudercontact", label: "Voor het oudercontact" },
  ] as const,
};

export type NotitieSoort = (typeof begeleidingTekst.soorten)[number]["waarde"];
