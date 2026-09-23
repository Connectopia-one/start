import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { doelenTekst, doelenBlokken } from "@/inhoud/onderwijsdoelen";

export const metadata = {
  title: "Waarop is dit gebaseerd? — Oefenplatform Connectopia",
  description:
    "Per niveau en per vak: op welke minimumdoelen en op welke vakfiches van de Examencommissie onze oefeningen steunen.",
};

export default async function OnderwijsdoelenPage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {doelenTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">{doelenTekst.titel}</h1>
        <p className="mt-4 text-sm text-ink-dim">{doelenTekst.intro}</p>

        <div className="mt-8 space-y-6">
          {doelenBlokken.map((blok) => (
            <section
              key={blok.niveau}
              className="rounded-xl border border-border bg-surface p-6"
            >
              <h2 className="font-display text-lg font-semibold text-ink">
                <span aria-hidden className="mr-2">
                  {blok.emoji}
                </span>
                {blok.niveau}
              </h2>
              <p className="mt-2 text-sm text-ink-dim">{blok.herkomst}</p>
              {blok.bron && (
                <p className="mt-2 text-sm">
                  <a
                    href={blok.bron}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-forest-dark underline-offset-2 hover:underline"
                  >
                    {blok.bronTekst ?? "Bekijk de officiële tekst"} ↗
                  </a>
                </p>
              )}

              <dl className="mt-4 space-y-3 border-t border-border pt-4">
                {blok.vakken.map((vak) => (
                  <div key={vak.naam}>
                    <dt className="text-sm font-medium text-ink">{vak.naam}</dt>
                    <dd className="mt-0.5 text-sm text-ink-dim">
                      {vak.doelen}
                      {vak.stand && (
                        <span className="mt-1 block text-xs text-ink-dim">{vak.stand}</span>
                      )}
                    </dd>
                  </div>
                ))}
              </dl>
            </section>
          ))}
        </div>

        <section className="mt-8 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">
            {doelenTekst.eigenWoordenKop}
          </h2>
          <p className="mt-2 text-sm text-ink-dim">{doelenTekst.eigenWoorden}</p>
          <p className="mt-3 text-sm text-ink-dim">
            {doelenTekst.materiaalTekst}{" "}
            <Link
              href="/materiaal"
              className="text-forest-dark underline-offset-2 hover:underline"
            >
              Naar handig materiaal
            </Link>
          </p>
        </section>

        <section className="mt-6">
          <h2 className="font-display text-lg font-semibold text-ink">{doelenTekst.foutKop}</h2>
          <p className="mt-2 text-sm text-ink-dim">{doelenTekst.foutTekst}</p>
          <p className="mt-2 text-sm">
            📧{" "}
            <a
              href={`mailto:${doelenTekst.foutMail}`}
              className="text-forest-dark underline-offset-2 hover:underline"
            >
              {doelenTekst.foutMail}
            </a>
          </p>
        </section>
      </main>
    </>
  );
}
