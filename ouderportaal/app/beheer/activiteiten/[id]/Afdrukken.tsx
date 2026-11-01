"use client";

/* De fiches van deze lijst op papier of als pdf. In het afdrukvenster kies je
   "Opslaan als pdf" om ze te downloaden; de knoppen gaan niet mee. */
export function Afdrukken() {
  return (
    <button
      type="button"
      onClick={() => window.print()}
      className="rounded-md border border-forest px-3 py-2 text-sm font-medium text-forest-dark hover:bg-forest/10"
    >
      Fiches afdrukken of als pdf bewaren
    </button>
  );
}
