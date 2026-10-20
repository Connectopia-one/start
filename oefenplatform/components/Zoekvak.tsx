/*
  Het zoekvak boven de vakken van een niveau en boven de hoofdstukken van een
  vak. Een gewoon formulier zonder JavaScript: het stuurt naar /zoeken, met
  het niveau (en eventueel het vak) erbij, zodat je enkel vindt wat bij jouw
  niveau hoort.
*/
export function Zoekvak({
  niveau,
  vak,
  vakNaam,
  waarde = "",
}: {
  niveau: string;
  vak?: string;
  vakNaam?: string;
  waarde?: string;
}) {
  return (
    <form action="/zoeken" method="get" role="search" className="mt-6 flex gap-2">
      <input type="hidden" name="niveau" value={niveau} />
      {vak && <input type="hidden" name="vak" value={vak} />}
      <label htmlFor="zoekterm" className="sr-only">
        Zoeken
      </label>
      <input
        id="zoekterm"
        name="q"
        type="search"
        defaultValue={waarde}
        minLength={3}
        required
        placeholder={
          vakNaam
            ? `Zoek in ${vakNaam}, bv. een woord uit je boek`
            : "Zoek een onderwerp, bv. een woord uit je boek"
        }
        className="w-full rounded-full border border-border bg-surface px-4 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
      />
      <button
        type="submit"
        className="shrink-0 rounded-full bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
      >
        Zoeken
      </button>
    </form>
  );
}
