import type { Metadata } from "next";
import { Kaart, PaginaKop, Sectie } from "@/components/ui";
import { privacy as p, vzw } from "@/content/privacy";

export const metadata: Metadata = {
  title: "Privacy en wettelijke gegevens",
  description: p.tekst,
};

/* De teksten staan in content/privacy.ts. */
export default function Privacy() {
  const gegevens: [string, string][] = [
    ["Naam", vzw.naam],
    ["Rechtsvorm", vzw.rechtsvorm],
    ["Zetel", vzw.zetel],
    ["Ondernemingsnummer", vzw.ondernemingsnummer],
    ["Rechtspersonenregister", vzw.rpr],
    ["Opgericht op", vzw.opgericht],
  ];

  return (
    <>
      <PaginaKop
        label={p.label}
        titel={p.titel}
        handgeschreven={p.handgeschreven}
        tekst={p.tekst}
      />

      <Sectie className="grid gap-5 py-8">
        <Kaart>
          <h2 id="wettelijke-gegevens" className="text-xl text-green">
            {p.wieZijnWe.titel}
          </h2>
          <p className="mt-3 text-[16px] text-ink-dim">{p.wieZijnWe.inleiding}</p>
          <dl className="mt-4 overflow-hidden rounded-[14px] border border-border text-[15px] sm:text-[16px]">
            {gegevens.map(([wat, waarde], i) => (
              <div
                key={wat}
                className={`grid gap-1 px-4 py-3 sm:grid-cols-[14rem_1fr] ${i > 0 ? "border-t border-border" : ""}`}
              >
                <dt className="font-bold text-green">{wat}</dt>
                <dd className="text-ink">{waarde}</dd>
              </div>
            ))}
            <div className="grid gap-1 border-t border-border px-4 py-3 sm:grid-cols-[14rem_1fr]">
              <dt className="font-bold text-green">Contact</dt>
              <dd className="text-ink">
                <a className="font-bold text-green underline" href={`mailto:${vzw.email}`}>
                  {vzw.email}
                </a>{" "}
                · {vzw.telefoon}
              </dd>
            </div>
          </dl>
        </Kaart>

        {p.secties.map((s) => (
          <Kaart key={s.titel}>
            <h2 className="text-xl text-green">{s.titel}</h2>
            {"inleiding" in s && s.inleiding ? (
              <p className="mt-3 text-[16px] text-ink-dim">{s.inleiding}</p>
            ) : null}
            <ul className="mt-3 grid gap-2.5">
              {s.regels.map((regel) => (
                <li key={regel} className="flex gap-2.5 text-[16px] text-ink-dim">
                  <span aria-hidden className="text-green">
                    ●
                  </span>
                  {regel}
                </li>
              ))}
            </ul>
            {"slot" in s && s.slot ? (
              <p className="mt-4 text-[16px] text-ink-dim">{s.slot}</p>
            ) : null}
          </Kaart>
        ))}

        <p className="text-[15px] text-ink-dim">
          Vragen over je gegevens?{" "}
          <a className="font-bold text-green underline" href={`mailto:${vzw.email}`}>
            {vzw.email}
          </a>
          . Laatst bijgewerkt op {p.bijgewerkt}.
        </p>
      </Sectie>
    </>
  );
}
