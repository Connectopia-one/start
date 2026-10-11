import type { Categorienoot as Noot } from "@/inhoud/categorienoten";

/**
 * Het kadertje bovenaan een categorie: voor wie deze vakken zijn.
 *
 * Het stond er eerst als één alinea van tien regels, en Kim las het op
 * 11 oktober 2026 terug met "dit is heel veel tekst maar vind het echt niet
 * duidelijk". Er zaten vier boodschappen in. Nu staat elke boodschap apart:
 * één zin bovenaan, de weetjes eronder met hun onderwerp in het vet, de lange
 * lijst richtingen dichtgeklapt achter een klikje, en wat er nog niet is in
 * kleine letters helemaal onderaan.
 *
 * De tekst zelf staat in inhoud/categorienoten.ts, zodat aanpassen geen code
 * vraagt.
 */
export function Categorienoot({ noot }: { noot: Noot }) {
  return (
    <section className="mt-4 rounded-xl border border-border bg-surface px-5 py-4 text-sm">
      <p className="text-ink">{noot.kop}</p>

      {noot.punten?.length ? (
        <dl className="mt-3 space-y-2">
          {noot.punten.map((punt) => (
            <div key={punt.kop}>
              <dt className="font-medium text-ink">{punt.kop}</dt>
              <dd className="text-ink-dim">{punt.tekst}</dd>
            </div>
          ))}
        </dl>
      ) : null}

      {noot.richtingen && (
        <details className="mt-3 border-t border-border pt-3">
          <summary className="cursor-pointer text-ink-dim hover:text-ink">
            {noot.richtingen.klik}
          </summary>
          <div className="mt-2 space-y-2">
            {noot.richtingen.groepen.map((groep) => (
              <div key={groep.kop}>
                <p className="font-medium text-ink">{groep.kop}</p>
                <ul className="mt-1 space-y-0.5 text-ink-dim">
                  {groep.lijst.map((richting) => (
                    <li key={richting}>{richting}</li>
                  ))}
                </ul>
              </div>
            ))}
            {noot.richtingen.slot && (
              <p className="text-ink-dim">{noot.richtingen.slot}</p>
            )}
          </div>
        </details>
      )}

      {noot.komtNog && (
        <p className="mt-3 border-t border-border pt-3 text-xs text-ink-dim">
          {noot.komtNog}
        </p>
      )}
    </section>
  );
}
