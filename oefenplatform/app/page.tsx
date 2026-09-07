import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { NIVEAUS } from "@/lib/niveaus";

export default async function HomePage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">
          Oefenen voor de examencommissie
        </h1>
        <p className="mt-2 max-w-2xl text-sm text-ink-dim">
          Interactieve oefeningen, gemaakt door Connectopia. Kies hieronder een categorie om te
          starten.
        </p>
        <p className="mt-3 max-w-2xl rounded-md bg-info/10 px-4 py-3 text-sm text-ink">
          💡 Kies de categorie die het beste past bij wat je kind <strong>al kan</strong> — niet
          per se het officiële leerjaar of de leeftijd. Een kind mag gerust een categorie hoger of
          lager oefenen dan de klas waarin het zit.
        </p>

        <div className="mt-8 grid gap-4 sm:grid-cols-2">
          {NIVEAUS.map((n) => (
            <Link
              key={n.slug}
              href={`/niveaus/${n.slug}`}
              className="rounded-xl border border-border bg-surface p-6 transition hover:border-forest hover:shadow-sm"
            >
              <span className="text-3xl">{n.emoji}</span>
              <h2 className="mt-2 font-display text-xl font-semibold text-ink">{n.naam}</h2>
              <p className="mt-1 text-sm text-ink-dim">{n.omschrijving}</p>
            </Link>
          ))}
        </div>
      </main>
    </>
  );
}
