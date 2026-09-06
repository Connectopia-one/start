import Link from "next/link";
import { requireStaff } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";

export default async function TeamPage() {
  const session = await requireStaff();
  const naam = session.profile?.full_name ?? session.email ?? "";
  const rol = session.profile?.role ?? "ouder";

  const supabase = await createClient();
  const { data: klasjes } = await supabase.from("klasjes").select("id, naam, slug").order("naam");

  return (
    <>
      <Header naam={naam} rol={rol} terugHref="/portaal" terugLabel="Overzicht" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">Team</h1>
        <p className="mt-1 text-sm text-ink-dim">
          Foto&apos;s toevoegen per klasje, en de inlichtingenfiches van de kinderen bekijken.
          Klasjes en lesmateriaal beheert enkel Kim.
        </p>

        <section className="mt-8">
          <h2 className="font-display text-lg font-semibold text-ink">Klasjes</h2>
          <ul className="mt-3 space-y-2">
            {(klasjes ?? []).map((k) => (
              <li
                key={k.id}
                className="flex items-center justify-between rounded-lg border border-border bg-surface p-4"
              >
                <span className="font-medium text-ink">{k.naam}</span>
                <Link href={`/beheer/klasjes/${k.slug}/fotos`} className="text-sm font-medium text-forest-dark hover:underline">
                  Foto&apos;s toevoegen &rarr;
                </Link>
              </li>
            ))}
            {(klasjes ?? []).length === 0 && (
              <li className="text-sm text-ink-dim">Nog geen klasjes aangemaakt.</li>
            )}
          </ul>
        </section>

        <section className="mt-8">
          <h2 className="font-display text-lg font-semibold text-ink">Kinderen</h2>
          <p className="mt-1 text-sm text-ink-dim">
            Contactgegevens, allergieën, diagnoses en noodcontact per kind.
          </p>
          <Link
            href="/team/kinderen"
            className="mt-3 inline-block rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
          >
            Fiches bekijken &rarr;
          </Link>
        </section>
      </main>
    </>
  );
}
