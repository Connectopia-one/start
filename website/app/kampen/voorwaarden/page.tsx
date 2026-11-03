import type { Metadata } from "next";
import Link from "next/link";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { kampVoorwaarden as v } from "@/content/kampvoorwaarden";
import { site } from "@/content/site";

export const metadata: Metadata = {
  title: "Voorwaarden vakantiekampen",
  description: v.tekst,
};

/* De teksten staan in content/kampvoorwaarden.ts. */
export default function KampVoorwaarden() {
  return (
    <>
      <PaginaKop
        label={v.label}
        titel={v.titel}
        handgeschreven={v.handgeschreven}
        tekst={v.tekst}
      />

      <Sectie className="grid gap-5 py-8">
        <Kaart>
          <h2 className="text-xl text-green">{v.waarom.titel}</h2>
          {v.waarom.alineas.map((a) => (
            <p key={a} className="mt-3 text-[16px] text-ink-dim">
              {a}
            </p>
          ))}
        </Kaart>

        <Kaart>
          <h2 className="text-xl text-green">{v.inschrijving.titel}</h2>
          <ul className="mt-3 grid gap-2.5">
            {v.inschrijving.regels.map((regel) => (
              <li key={regel} className="flex gap-2.5 text-[16px] text-ink-dim">
                <span aria-hidden className="text-green">
                  ●
                </span>
                {regel}
              </li>
            ))}
          </ul>
        </Kaart>

        <Kaart>
          <h2 className="text-xl text-green">{v.annulering.titel}</h2>
          <p className="mt-3 text-[16px] text-ink-dim">{v.annulering.inleiding}</p>
          <div className="mt-4 overflow-hidden rounded-[14px] border border-border">
            <table className="w-full text-left text-[15px] sm:text-[16px]">
              <thead className="bg-sage-soft text-green">
                <tr>
                  {v.annulering.kolommen.map((k) => (
                    <th key={k} scope="col" className="px-4 py-3 font-extrabold">
                      {k}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {v.annulering.rijen.map(([wanneer, wat]) => (
                  <tr key={wanneer} className="border-t border-border align-top">
                    <td className="px-4 py-3 text-ink">{wanneer}</td>
                    <td className="px-4 py-3 font-bold text-ink">{wat}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <p className="mt-4 text-[16px] text-ink-dim">{v.annulering.slot}</p>
          <p className="mt-3 text-[16px] text-ink-dim">
            <a className="font-bold text-green underline" href={`mailto:${site.email}`}>
              {site.email}
            </a>{" "}
            · {site.telefoon}
          </p>
        </Kaart>

        <div>
          <Link
            href="/kampen/inschrijven"
            className="inline-block rounded-full bg-green px-7 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
          >
            Naar de inschrijving →
          </Link>
        </div>
      </Sectie>
    </>
  );
}
