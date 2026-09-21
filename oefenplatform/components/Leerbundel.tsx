/*
  De leerbundel zoals het kind ze leest: de blokjes onder elkaar, in de
  volgorde die je in het beheer hebt gezet. Tekst en beeld wisselen elkaar af,
  want voor veel kinderen leest dat een pak vlotter dan een lap tekst.
*/

export type LeerbundelBlok = {
  id: string;
  soort: "titel" | "tekst" | "weetje" | "afbeelding";
  tekst: string | null;
  afbeeldingUrl: string | null;
};

export function Leerbundel({ blokken }: { blokken: LeerbundelBlok[] }) {
  if (!blokken.length) return null;

  return (
    <article className="mt-6 rounded-xl border border-border bg-surface px-5 py-5">
      {blokken.map((blok) => {
        if (blok.soort === "titel") {
          return (
            <h3
              key={blok.id}
              className="mt-6 font-display text-lg font-semibold text-ink first:mt-0"
            >
              {blok.tekst}
            </h3>
          );
        }

        if (blok.soort === "weetje") {
          return (
            <div
              key={blok.id}
              className="mt-4 rounded-lg border border-amber/40 bg-amber/10 px-4 py-3 first:mt-0"
            >
              <p className="text-sm font-medium text-ink">💡 Weetje</p>
              <p className="mt-1 whitespace-pre-line text-sm text-ink">{blok.tekst}</p>
            </div>
          );
        }

        if (blok.soort === "afbeelding") {
          if (!blok.afbeeldingUrl) return null;
          return (
            <figure key={blok.id} className="mt-4 first:mt-0">
              {/* eslint-disable-next-line @next/next/no-img-element */}
              <img
                src={blok.afbeeldingUrl}
                alt={blok.tekst || "Afbeelding bij de leerstof"}
                className="w-full rounded-lg border border-border"
              />
              {blok.tekst && (
                <figcaption className="mt-2 text-center text-xs text-ink-dim">{blok.tekst}</figcaption>
              )}
            </figure>
          );
        }

        return (
          <p
            key={blok.id}
            className="mt-3 whitespace-pre-line text-[15px] leading-relaxed text-ink first:mt-0"
          >
            {blok.tekst}
          </p>
        );
      })}
    </article>
  );
}
