import Link from "next/link";

/*
  De weg terug naar de hoofdstukken van dit vak, onderaan de pagina.

  De mama van Febe meldde op 6 oktober 2026: "Het is misschien handig dat er
  een knop verschijnt na het afwerken van een oefening of een stukje leerstof,
  onderaan die pagina, om terug te keren naar het overzicht van dat vak. Het
  staat er wel, bovenaan, maar we moesten ernaar zoeken."

  Het is dezelfde link als bovenaan, maar als knop en op de plaats waar een
  kind uitkomt wanneer het klaar is.
*/
export function TerugNaarVak({ href, label }: { href: string; label: string }) {
  return (
    <div className="mt-10 border-t border-border pt-6">
      <Link
        href={href}
        className="flex items-center gap-3 rounded-xl border border-forest/40 bg-forest/5 px-5 py-4 transition hover:border-forest"
      >
        <span className="shrink-0 text-forest-dark">&larr;</span>
        <span>
          <span className="block font-display text-base font-semibold text-ink">
            Terug naar {label}
          </span>
          <span className="mt-0.5 block text-sm text-ink-dim">
            Daar staan alle hoofdstukken van dit vak, met wat je al maakte.
          </span>
        </span>
      </Link>
      {/* En in één klik helemaal terug naar het begin, met "Verder waar je
          was" bovenaan (Marjolein en Linda, enquête november 2026). */}
      <Link
        href="/"
        className="mt-3 inline-flex items-center gap-2 text-sm text-ink-dim hover:text-ink"
      >
        <span aria-hidden>🏠</span> Naar de startpagina
      </Link>
    </div>
  );
}
