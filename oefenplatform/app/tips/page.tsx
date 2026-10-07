import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { tipsTekst } from "@/inhoud/tips";

export const metadata = {
  title: "Zo gebruiken wij het — Oefenplatform Connectopia",
  description:
    "Hoe wij zelf met het oefenplatform werken: een vak kiezen, door de tocht gaan, notities nemen, en dan de oefeningen van deel 1 en deel 2.",
};

/*
  Een tipspagina, geen handleiding.

  Ook zichtbaar zonder account, net als /materiaal: wie nog twijfelt of dit
  iets voor zijn kind is, mag eerst zien hoe ermee gewerkt wordt. Er staat
  geen gegeven van een kind op, dus er is niets af te schermen.

  De tekst staat volledig in inhoud/tips.ts, zodat aanpassen geen code vraagt.
*/
export default async function TipsPage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {tipsTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          {tipsTekst.titel}
        </h1>
        <p className="mt-4 text-sm text-ink-dim">{tipsTekst.intro}</p>

        <ol className="mt-8 space-y-4">
          {tipsTekst.stappen.map((stap, i) => (
            <li
              key={stap.kop}
              className="flex gap-4 rounded-xl border border-border bg-surface px-5 py-4"
            >
              <span
                aria-hidden
                className="mt-0.5 flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-forest/10 font-display text-sm font-semibold text-forest-dark"
              >
                {i + 1}
              </span>
              <div>
                <h2 className="font-display text-base font-semibold text-ink">
                  {stap.kop}
                </h2>
                <p className="mt-1 text-sm text-ink-dim">{stap.tekst}</p>
              </div>
            </li>
          ))}
        </ol>

        {tipsTekst.nota && (
          <p className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            {tipsTekst.nota}
          </p>
        )}

        {tipsTekst.oproepLink && (
          <p className="mt-8">
            <Link
              href={tipsTekst.oproepLink}
              className="inline-block rounded-md bg-forest px-4 py-2 text-sm font-semibold text-white transition hover:bg-forest-dark"
            >
              {tipsTekst.oproepTekst}
            </Link>
          </p>
        )}
      </main>
    </>
  );
}
