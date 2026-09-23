import { stopMeekijken } from "@/app/portaal/meekijken-actions";

/*
  De balk die bovenaan het portaal staat zolang je als beheerder meekijkt met
  een gezin. Hij moet opvallen: het is anders zo gebeurd dat je vergeet dat je
  niet naar je eigen scherm kijkt.
*/
export function MeekijkBalk({ naam, terug }: { naam: string; terug?: string }) {
  return (
    <div className="border-b border-amber/40 bg-amber/15">
      <div className="mx-auto flex max-w-4xl flex-wrap items-center justify-between gap-3 px-6 py-2.5 text-sm">
        <span className="text-ink">
          Je kijkt mee met <strong className="font-semibold">{naam}</strong>.
          Dit is wat dit gezin ziet.
        </span>
        <form action={stopMeekijken}>
          <input
            type="hidden"
            name="terug"
            value={terug ?? "/beheer/gezinnen"}
          />
          <button
            type="submit"
            className="rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white transition hover:bg-forest-dark"
          >
            Stoppen met meekijken
          </button>
        </form>
      </div>
    </div>
  );
}
