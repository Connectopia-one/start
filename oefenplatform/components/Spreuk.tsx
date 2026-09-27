"use client";

import { usePathname } from "next/navigation";
import { SPREUKEN } from "@/inhoud/spreuken";
import { zaad } from "@/lib/optievolgorde";

/**
 * Een spreuk onderaan elke pagina.
 *
 * Welke er staat, volgt uit het adres van de pagina. Dat is met opzet: zo
 * staat op elke pagina een andere, maar blijft ze daar wel staan. Een tekst
 * die bij elk bezoek verandert leidt af, en een tekst die per dag wisselt zou
 * op de pagina's die Next.js vooraf opbouwt blijven hangen op de dag van de
 * laatste uitrol.
 *
 * Het pad is tijdens het opbouwen van de pagina al bekend, dus de spreuk staat
 * er meteen, ook voor wie geen javascript laat draaien.
 */
export function Spreuk() {
  const pad = usePathname() ?? "/";
  if (!SPREUKEN.length) return null;

  const spreuk = SPREUKEN[zaad(pad) % SPREUKEN.length];

  return (
    <aside className="niet-afdrukken mt-auto border-t border-border px-6 py-8">
      <figure className="mx-auto max-w-2xl text-center">
        <blockquote className="font-display text-base text-ink-dim">
          &laquo;&nbsp;{spreuk.tekst}&nbsp;&raquo;
        </blockquote>
        {spreuk.van && (
          <figcaption className="mt-1 text-xs text-ink-dim">{spreuk.van}</figcaption>
        )}
      </figure>
    </aside>
  );
}
