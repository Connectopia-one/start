import { lijstZin } from "@/lib/kind";

/*
  Het groene of rode balkje dat zegt of een fiche in orde is.

  Kim wou in één oogopslag zien wie ze nog moet achternabellen voor het kamp
  begint, zonder elk kind apart open te klikken. Het staat daarom op de lijst
  van de gezinnen én op het gezin zelf, met dezelfde kleuren.

  Rood zegt altijd wát er ontbreekt. Een kleur zonder reden laat iemand zoeken
  in een formulier van twintig velden.
*/
export function FicheStand({
  ontbreekt,
  klein,
}: {
  ontbreekt: string[];
  klein?: boolean;
}) {
  const maat = klein ? "px-2 py-0.5 text-xs" : "px-2.5 py-1 text-xs";

  if (ontbreekt.length === 0) {
    return (
      <span
        className={`inline-block shrink-0 rounded-full bg-forest/10 font-medium text-forest-dark ${maat}`}
      >
        Fiche in orde
      </span>
    );
  }

  return (
    <span
      className={`inline-block rounded-full bg-danger/10 font-medium text-danger ${maat}`}
    >
      Nog nodig: {lijstZin(ontbreekt)}
    </span>
  );
}
