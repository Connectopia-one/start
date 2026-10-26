import type { Metadata } from "next";
import Link from "next/link";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import {
  leerkrachtenSlot,
  leerkrachtenTekst,
  tips,
  tipsTitel,
  uitleg,
  uitlegTitel,
} from "@/content/leerkrachten";

export const metadata: Metadata = {
  title: leerkrachtenTekst.titel,
  description: leerkrachtenTekst.tekst,
};

/* De kleur van het rondje bij elk blok, zoals overal op de site. */
const rondjeKleur = {
  green: "bg-sage-soft",
  purple: "bg-purple-soft",
  orange: "bg-orange-soft",
  blue: "bg-blue-soft",
} as const;

export default function LeerkrachtenPagina() {
  return (
    <>
      <PaginaKop
        label={leerkrachtenTekst.label}
        titel={leerkrachtenTekst.titel}
        handgeschreven={leerkrachtenTekst.handgeschreven}
        tekst={leerkrachtenTekst.tekst}
      />

      <Sectie className="py-6">
        <h2 className="text-2xl text-green">{uitlegTitel}</h2>
        <div className="mt-4 grid gap-4 md:grid-cols-3">
          {uitleg.map((blok) => (
            <Kaart key={blok.titel}>
              <span
                aria-hidden
                className={`flex h-12 w-12 items-center justify-center rounded-full text-2xl ${rondjeKleur[blok.kleur]}`}
              >
                {blok.icoon}
              </span>
              <h3 className="mt-3 text-xl text-green">{blok.titel}</h3>
              <p className="mt-2 text-[16px] text-ink-dim">{blok.tekst}</p>
            </Kaart>
          ))}
        </div>
      </Sectie>

      <Sectie className="py-4">
        <h2 className="text-2xl text-green">{tipsTitel}</h2>
        <ol className="mt-4 flex flex-col gap-4">
          {tips.map((tip, i) => (
            <li key={tip.titel}>
              <Kaart>
                <div className="sm:flex sm:items-start sm:gap-4">
                  <span
                    aria-hidden
                    className="mb-3 flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-orange sm:mb-0 text-lg font-extrabold text-cream"
                  >
                    {i + 1}
                  </span>
                  <div className="min-w-0">
                    <h3 className="text-xl text-green">{tip.titel}</h3>
                    {tip.tekst.map((alinea) => (
                      <p key={alinea} className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">
                        {alinea}
                      </p>
                    ))}
                    {tip.zin ? (
                      <blockquote className="mt-4 rounded-[16px] bg-sage-soft px-5 py-4">
                        <p className="font-hand text-2xl leading-snug text-green">
                          &ldquo;{tip.zin}&rdquo;
                        </p>
                      </blockquote>
                    ) : null}
                  </div>
                </div>
              </Kaart>
            </li>
          ))}
        </ol>
      </Sectie>

      <Sectie className="py-6">
        <div className="rounded-[20px] border border-border bg-surface px-6 py-5">
          <h2 className="text-xl text-green">{leerkrachtenSlot.titel}</h2>
          <p className="mt-2 max-w-[68ch] text-[16px] text-ink-dim">{leerkrachtenSlot.tekst}</p>
          <div className="mt-4 flex flex-wrap gap-2">
            {leerkrachtenSlot.links.map((link, i) => (
              <Link
                key={link.href}
                href={link.href}
                className={`rounded-full px-4 py-2 text-[15px] font-extrabold ${
                  i === 0
                    ? "bg-green text-cream"
                    : "border border-border bg-cream text-green hover:border-green"
                }`}
              >
                {link.tekst}
              </Link>
            ))}
          </div>
        </div>
      </Sectie>
    </>
  );
}
