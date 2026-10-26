import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { extrasTekst, spellen } from "@/inhoud/extras";

export const metadata = {
  title: "Leuke extra's — Oefenplatform Connectopia",
  description:
    "Spelletjes naast de leerstof om begrippen op een andere manier in te oefenen, alleen of met de hele klas.",
};

/*
  Een kaart per spel. Zichtbaar zonder account, net als /tips en /materiaal:
  de spellen bewaren niets van een kind, dus er is niets af te schermen.

  De teksten en de lijst met spellen staan in inhoud/extras.ts.
*/
export default async function ExtrasPage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {extrasTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          {extrasTekst.titel}
        </h1>
        <p className="mt-4 max-w-2xl text-sm text-ink-dim">{extrasTekst.intro}</p>

        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          {spellen.map((spel) => (
            <Link
              key={spel.slug}
              href={`/extras/${spel.slug}`}
              className="flex flex-col rounded-xl border border-border bg-surface px-6 py-5 transition hover:border-forest hover:shadow-sm"
            >
              <span className="font-display text-lg font-semibold text-ink">
                <span aria-hidden>{spel.icoon}</span> {spel.titel}
              </span>
              <span className="mt-1 text-xs font-medium uppercase tracking-wide text-forest">
                {spel.vak} · {spel.voorWie}
              </span>
              <span className="mt-2 block text-sm text-ink-dim">{spel.tekst}</span>
            </Link>
          ))}
        </div>
      </main>
    </>
  );
}
