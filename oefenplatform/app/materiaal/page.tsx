import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { materiaalGroepen, materiaalTekst } from "@/inhoud/materiaal";

export const metadata = {
  title: "Handig materiaal — Oefenplatform Connectopia",
  description:
    "Gratis verzameling links naar vakfiches, naslagwerken en oefensites, bijeengebracht door Connectopia vzw.",
};

export default async function MateriaalPage() {
  const session = await getSessionProfile();
  /* Een groep zonder links tonen we wel, met een regeltje eronder, zodat je
     ziet dat er nog iets komt. Alleen als álles leeg is, zeggen we dat één keer. */
  const iets = materiaalGroepen.some((g) => g.linken.length > 0);

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {materiaalTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">{materiaalTekst.titel}</h1>
        <p className="mt-4 text-sm text-ink-dim">{materiaalTekst.intro}</p>

        {!iets && (
          <p className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            We zijn deze lijst aan het samenstellen. Kom binnenkort nog eens kijken.
          </p>
        )}

        <div className="mt-8 space-y-9">
          {materiaalGroepen.map((groep) => (
            <section key={groep.kop}>
              <h2 className="font-display text-lg font-semibold text-ink">{groep.kop}</h2>
              {groep.uitleg && <p className="mt-1 text-sm text-ink-dim">{groep.uitleg}</p>}

              {groep.linken.length === 0 ? (
                <p className="mt-3 text-sm text-ink-dim">{materiaalTekst.leegTekst}</p>
              ) : (
                <ul className="mt-3 space-y-2">
                  {groep.linken.map((l) => (
                    <li key={l.link}>
                      <a
                        href={l.link}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="block rounded-xl border border-border bg-surface p-4 transition hover:border-forest hover:shadow-sm"
                      >
                        <span className="font-medium text-forest-dark">{l.titel} ↗</span>
                        {l.omschrijving && (
                          <span className="mt-1 block text-sm text-ink-dim">{l.omschrijving}</span>
                        )}
                        {l.opmerking && (
                          <span className="mt-1 block text-xs text-ink-dim">{l.opmerking}</span>
                        )}
                      </a>
                    </li>
                  ))}
                </ul>
              )}
            </section>
          ))}
        </div>

        <p className="mt-10 rounded-xl border border-border bg-surface px-5 py-4 text-sm text-ink-dim">
          {materiaalTekst.externNota}
        </p>

        <p className="mt-6 text-sm text-ink-dim">{materiaalTekst.nota}</p>

        {materiaalTekst.oproepLink && (
          <p className="mt-4">
            <Link
              href={materiaalTekst.oproepLink}
              className="inline-block rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark"
            >
              {materiaalTekst.oproepTekst}
            </Link>
          </p>
        )}
      </main>
    </>
  );
}
