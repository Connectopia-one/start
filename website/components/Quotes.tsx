import { Label } from "@/components/ui";
import { quotes, quotesTekst } from "@/content/quotes";

/*
  Het blok met quotes van ouders en kinderen.

  Staat er nog geen enkele quote in content/quotes.ts, dan tekent dit blok
  niets. Zo kan het al op de pagina's staan voor de eerste binnen is, zonder
  dat er een leeg kader te zien is.

  Een quote van een kind krijgt een andere kleur dan een quote van een ouder,
  zodat een lezer meteen ziet wie aan het woord is. Ze staan gewoon door
  elkaar in de lijst; de volgorde in het bestand is de volgorde op de pagina.
*/
export function Quotes() {
  if (quotes.length === 0) return null;

  return (
    <section className="bg-cream">
      <div className="mx-auto w-full max-w-5xl px-5 py-12">
        <Label>{quotesTekst.label}</Label>
        <h2 className="mt-1.5 text-3xl text-green">{quotesTekst.titel}</h2>
        <p className="mt-2 max-w-[60ch] text-ink-dim">{quotesTekst.tekst}</p>

        <div className="mt-6 grid gap-4 md:grid-cols-2">
          {quotes.map((quote) => {
            const vanKind = quote.van === "kind";
            return (
              <figure
                key={quote.tekst}
                className={
                  vanKind
                    ? "rounded-[20px] border border-purple-soft bg-purple-soft/50 px-6 py-5"
                    : "rounded-[20px] border border-border bg-surface px-6 py-5"
                }
              >
                <blockquote className="text-[17px] leading-relaxed text-ink">
                  <span
                    aria-hidden
                    className={
                      vanKind
                        ? "mr-1 font-hand text-2xl text-purple"
                        : "mr-1 font-hand text-2xl text-orange"
                    }
                  >
                    “
                  </span>
                  {quote.tekst}
                </blockquote>
                <figcaption
                  className={
                    vanKind
                      ? "mt-3 text-[15px] font-bold text-purple"
                      : "mt-3 text-[15px] font-bold text-green"
                  }
                >
                  {vanKind ? <span aria-hidden>🧒 </span> : null}
                  {quote.naam}
                  {quote.wat ? (
                    <span className="font-normal text-ink-dim">
                      , {quote.wat}
                    </span>
                  ) : null}
                </figcaption>
              </figure>
            );
          })}
        </div>
      </div>
    </section>
  );
}
