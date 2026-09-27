"use client";

import { usePathname } from "next/navigation";
import { spreuken } from "@/content/spreuken";

/**
 * Een spreuk onderaan elke pagina, net boven de voettekst.
 *
 * Welke er staat, volgt uit het adres van de pagina. Dat is met opzet: zo
 * staat op elke pagina een andere, maar blijft ze daar wel staan. Een tekst
 * die bij elk bezoek verandert leidt af, en een tekst die per dag wisselt zou
 * hier blijven hangen op de dag van de laatste uitrol — bijna elke pagina van
 * deze site wordt vooraf opgebouwd.
 *
 * Het pad is tijdens dat opbouwen al bekend, dus de spreuk staat er meteen,
 * ook voor wie geen javascript laat draaien.
 */
export function Spreuk() {
  const pad = usePathname() ?? "/";
  if (!spreuken.length) return null;

  const spreuk = spreuken[zaad(pad) % spreuken.length];

  return (
    <aside className="niet-afdrukken border-t border-border bg-sage-soft">
      <figure className="mx-auto w-full max-w-5xl px-5 py-9 text-center">
        <blockquote className="font-hand text-2xl text-green sm:text-[26px]">
          {spreuk.tekst}
        </blockquote>
        {spreuk.van && (
          <figcaption className="mt-1 text-[15px] font-bold text-ink-dim">
            {spreuk.van}
          </figcaption>
        )}
      </figure>
    </aside>
  );
}

/** Een klein, voorspelbaar getal uit een tekst (FNV-1a). */
function zaad(tekst: string): number {
  let h = 0x811c9dc5;
  for (let i = 0; i < tekst.length; i++) {
    h ^= tekst.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return h >>> 0;
}
