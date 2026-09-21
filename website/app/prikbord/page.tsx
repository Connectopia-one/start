import type { Metadata } from "next";
import Link from "next/link";
import {
  Icoon,
  PaginaKop,
  Sectie,
  tekstKleur,
  vlakKleur,
} from "@/components/ui";
import { PositieveToon } from "@/components/PositieveToon";
import { borden, prikbord } from "@/content/prikbord";

export const metadata: Metadata = {
  title: "Prikbord voor ouders",
  description: prikbord.tekst,
};

export default function PrikbordPagina() {
  return (
    <>
      <PaginaKop
        label={prikbord.label}
        titel={prikbord.titel}
        handgeschreven={prikbord.handgeschreven}
        tekst={prikbord.tekst}
      />

      <Sectie className="pt-6 pb-2">
        <PositieveToon />
      </Sectie>

      <Sectie className="pt-4 pb-8">
        <div className="grid gap-4 sm:grid-cols-2">
          {borden.map((bord) => (
            <Link
              key={bord.slug}
              href={`/prikbord/${bord.slug}`}
              className="flex flex-col gap-3 rounded-[20px] border border-border bg-surface p-6 shadow-[0_2px_10px_rgba(47,74,34,0.07)] transition hover:-translate-y-1"
            >
              <Icoon kleur={bord.kleur}>{bord.icoon}</Icoon>
              <div>
                <h2 className={`text-xl ${tekstKleur[bord.kleur]}`}>
                  {bord.naam}
                </h2>
                <p className="text-[14px] text-ink-dim">{bord.ondertitel}</p>
              </div>
              <p className="text-[15px] text-ink-dim">{bord.uitleg}</p>
              <ul className="mt-auto flex flex-wrap gap-2 pt-2">
                {bord.waarvoor.map((punt) => (
                  <li
                    key={punt}
                    className={`rounded-full px-3 py-1 text-[12.5px] font-bold ${vlakKleur[bord.kleur]} ${tekstKleur[bord.kleur]}`}
                  >
                    {punt}
                  </li>
                ))}
              </ul>
              <span
                className={`pt-2 text-sm font-extrabold ${tekstKleur[bord.kleur]}`}
              >
                Bekijk dit bord →
              </span>
            </Link>
          ))}
        </div>
      </Sectie>

      <Sectie className="pt-0 pb-16">
        <div className="rounded-[20px] bg-sage-soft px-7 py-7">
          <h2 className="text-2xl text-green">{prikbord.spelregels.titel}</h2>
          <ul className="mt-4 grid gap-2.5 sm:grid-cols-2">
            {prikbord.spelregels.punten.map((punt) => (
              <li key={punt} className="text-[15px] text-ink">
                {punt}
              </li>
            ))}
          </ul>
        </div>
      </Sectie>
    </>
  );
}
