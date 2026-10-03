import type { Metadata } from "next";
import { PaginaKop, Sectie } from "@/components/ui";
import { kijkje } from "@/content/kijkje";

export const metadata: Metadata = {
  title: kijkje.label,
  description: kijkje.tekst,
};

export default function KijkjePagina() {
  return (
    <>
      <PaginaKop
        label={kijkje.label}
        titel={kijkje.titel}
        handgeschreven={kijkje.handgeschreven}
        tekst={kijkje.tekst}
      />

      {/*
        De foto's staan in een raster dat van één kolom op een gsm naar drie
        gaat op een breed scherm. Elke foto houdt zijn eigen verhouding, want
        bijsnijden tot een vierkant zou net het deel wegnemen waar het om gaat.
      */}
      <Sectie className="py-6">
        <ul className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {kijkje.fotos.map((foto) => (
            <li key={foto.bestand}>
              <figure className="h-full overflow-hidden rounded-[20px] border border-border bg-surface shadow-[0_2px_10px_rgba(47,74,34,0.07)]">
                {/* eslint-disable-next-line @next/next/no-img-element */}
                <img
                  src={`/kijkje/${foto.bestand}`}
                  alt={foto.alt}
                  /*
                    Alleen de eerste foto's worden meteen geladen. De rest komt
                    pas als iemand naar beneden scrolt, zodat de pagina op een
                    gsm niet eerst vier megabyte moet binnenhalen.
                  */
                  loading="lazy"
                  className="w-full object-cover"
                />
                <figcaption className="px-5 py-4 text-[16px] text-ink-dim">
                  {foto.bijschrift}
                </figcaption>
              </figure>
            </li>
          ))}
        </ul>
      </Sectie>

      <Sectie className="py-4">
        <div className="rounded-[20px] bg-sage-soft px-6 py-5">
          <h2 className="text-2xl text-green">{kijkje.slotTitel}</h2>
          {kijkje.slot.map((regel) => (
            <p key={regel} className="mt-3 max-w-[62ch] text-[16px] text-ink">
              {regel}
            </p>
          ))}
        </div>
      </Sectie>
    </>
  );
}
