import { notFound } from "next/navigation";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { upsertToegang, verwijderGezin, wijzigWachtwoord } from "../actions";

export default async function GezinDetailPage({
  params,
  searchParams,
}: {
  params: Promise<{ id: string }>;
  searchParams: Promise<{ succes?: string; fout?: string }>;
}) {
  const { id } = await params;
  const { succes, fout } = await searchParams;
  const session = await requireBeheerder();
  const naam = session.profile?.full_name ?? session.email ?? "";

  const supabase = await createClient();
  const [{ data: gezin }, { data: klasjes }, { data: toegangData }] = await Promise.all([
    supabase.from("profiles").select("id, full_name").eq("id", id).single(),
    supabase.from("klasjes").select("id, naam").order("naam"),
    supabase.from("toegang").select("klasje_id, materiaal, fotos").eq("profile_id", id),
  ]);

  if (!gezin) notFound();

  const toegangPerKlasje = new Map(
    (toegangData ?? []).map((t) => [t.klasje_id, { materiaal: t.materiaal, fotos: t.fotos }])
  );

  return (
    <>
      <Header naam={naam} isBeheerder terugHref="/beheer/gezinnen" terugLabel="Gezinnen" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <h1 className="font-display text-2xl font-semibold text-ink">{gezin.full_name}</h1>
        <p className="mt-1 text-sm text-ink-dim">
          Lesmateriaal en foto&apos;s staan hieronder los van elkaar — je kan het ene toestaan
          zonder het andere.
        </p>

        {fout && <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
        {succes && (
          <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{succes}</p>
        )}

        <div className="mt-6 space-y-3">
          {(klasjes ?? []).map((k) => {
            const huidig = toegangPerKlasje.get(k.id) ?? { materiaal: false, fotos: false };
            return (
              <form
                key={k.id}
                action={upsertToegang}
                className="flex flex-wrap items-center justify-between gap-3 rounded-lg border border-border bg-surface p-4"
              >
                <input type="hidden" name="profile_id" value={gezin.id} />
                <input type="hidden" name="klasje_id" value={k.id} />
                <p className="font-medium text-ink">{k.naam}</p>
                <div className="flex items-center gap-4 text-sm">
                  <label className="flex items-center gap-1.5">
                    <input type="checkbox" name="materiaal" defaultChecked={huidig.materiaal} />
                    Lesmateriaal
                  </label>
                  <label className="flex items-center gap-1.5">
                    <input type="checkbox" name="fotos" defaultChecked={huidig.fotos} />
                    Foto&apos;s
                  </label>
                  <button
                    type="submit"
                    className="rounded-md bg-forest px-3 py-1.5 font-medium text-white hover:bg-forest-dark"
                  >
                    Bewaren
                  </button>
                </div>
              </form>
            );
          })}
          {(klasjes ?? []).length === 0 && (
            <p className="text-sm text-ink-dim">Maak eerst een klasje aan onder Beheer.</p>
          )}
        </div>

        <form action={wijzigWachtwoord} className="mt-10 border-t border-border pt-6">
          <input type="hidden" name="profile_id" value={gezin.id} />
          <h2 className="font-display text-lg font-semibold text-ink">Wachtwoord wijzigen</h2>
          <p className="mt-1 text-sm text-ink-dim">
            Stel een nieuw wachtwoord in voor dit gezin en geef dat opnieuw veilig aan hen door.
          </p>
          <div className="mt-3 flex gap-2">
            <input
              name="wachtwoord"
              type="text"
              minLength={8}
              required
              placeholder="Nieuw wachtwoord (min. 8 tekens)"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
            <button
              type="submit"
              className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Bijwerken
            </button>
          </div>
        </form>

        <form
          action={verwijderGezin}
          className="mt-10 border-t border-border pt-6"
        >
          <input type="hidden" name="profile_id" value={gezin.id} />
          <p className="text-sm text-ink-dim">
            Verwijder dit account volledig, bijvoorbeeld als het kind stopt. Dit kan niet ongedaan
            gemaakt worden.
          </p>
          <button
            type="submit"
            className="mt-2 rounded-md border border-danger px-3 py-1.5 text-sm font-medium text-danger hover:bg-danger/10"
          >
            Gezin verwijderen
          </button>
        </form>
      </main>
    </>
  );
}
