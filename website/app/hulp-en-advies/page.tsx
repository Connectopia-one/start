import type { Metadata } from "next";
import Link from "next/link";
import {
  Icoon,
  Kaart,
  Knop,
  PaginaKop,
  Sectie,
  tekstKleur,
} from "@/components/ui";
import { hulpSlot, hulpTegels, hulpTekst } from "@/content/hulp";

export const metadata: Metadata = {
  title: "Hulp, advies en tips",
  description: hulpTekst.tekst,
};

export default function HulpEnAdviesPagina() {
  return (
    <>
      <PaginaKop
        label={hulpTekst.label}
        titel={hulpTekst.titel}
        handgeschreven={hulpTekst.handgeschreven}
        tekst={hulpTekst.tekst}
      />

      <Sectie>
        <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
          {hulpTegels.map((tegel) => (
            <Link
              key={tegel.link}
              href={tegel.link}
              className="flex flex-col gap-2.5 rounded-[20px] border border-border bg-surface p-6 shadow-[0_2px_10px_rgba(47,74,34,0.07)] transition hover:-translate-y-1 hover:shadow-[0_8px_20px_rgba(47,74,34,0.12)]"
            >
              <Icoon kleur={tegel.kleur}>{tegel.icoon}</Icoon>
              <h2 className={`text-xl ${tekstKleur[tegel.kleur]}`}>
                {tegel.titel}
              </h2>
              <p className="text-[16px] text-ink-dim">{tegel.tekst}</p>
              <span
                className={`mt-auto pt-3 text-[15px] font-extrabold ${tekstKleur[tegel.kleur]}`}
              >
                Bekijken →
              </span>
            </Link>
          ))}
        </div>

        <Kaart className="mt-6">
          <h2 className="text-xl text-green">{hulpSlot.titel}</h2>
          <p className="mt-2 max-w-[62ch] text-ink-dim">{hulpSlot.tekst}</p>
          <div className="mt-5">
            <Knop href={hulpSlot.link}>{hulpSlot.knop}</Knop>
          </div>
        </Kaart>
      </Sectie>
    </>
  );
}
