import type { Metadata } from "next";
import Link from "next/link";
import { PaginaKop, Penseel, Sectie } from "@/components/ui";
import { prikbord } from "@/content/prikbord";

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

      <Sectie className="py-6">
        <Penseel>{prikbord.status}</Penseel>
      </Sectie>

      <Sectie className="pb-8">
        <h2 className="text-2xl text-green">Wat er komt</h2>
        <ul className="mt-4 grid gap-2.5 sm:grid-cols-2">
          {prikbord.komtEraan.map((punt) => (
            <li
              key={punt}
              className="rounded-2xl border border-border bg-surface px-5 py-4 text-[15px] text-ink"
            >
              {punt}
            </li>
          ))}
        </ul>
      </Sectie>

      <Sectie className="pb-16">
        <div className="rounded-[20px] bg-purple-soft px-7 py-7">
          <h2 className="text-2xl text-purple">{prikbord.oproep.titel}</h2>
          <p className="mt-3 max-w-[58ch] text-ink">{prikbord.oproep.tekst}</p>
          <Link
            href={prikbord.oproep.knopLink}
            className="mt-5 inline-block rounded-full bg-purple px-6 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5"
          >
            {prikbord.oproep.knopTekst} →
          </Link>
        </div>
      </Sectie>
    </>
  );
}
