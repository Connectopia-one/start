import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { vindNiveau } from "@/lib/niveaus";
import { verwijderDoelbestand } from "./actions";
import { NieuwDoelbestandForm } from "./NieuwDoelbestandForm";

type Rij = {
  id: string;
  niveau: string;
  vak: string | null;
  titel: string;
  type: "link" | "pdf";
  link: string | null;
  bestandspad: string | null;
  geldig_sinds: string | null;
  omschrijving: string | null;
};

export default async function BeheerDoelenPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data, error } = await supabase
    .from("doelbestanden")
    .select("id, niveau, vak, titel, type, link, bestandspad, geldig_sinds, omschrijving")
    .order("niveau", { ascending: true })
    .order("vak", { ascending: true, nullsFirst: true })
    .order("created_at", { ascending: true });

  const rijen = (data ?? []) as Rij[];

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <p className="text-sm font-medium uppercase tracking-wide text-forest">
          Onderwijsdoelen
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          Doelen en vakfiches beheren
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Wat je hier oplaadt, staat meteen bij het juiste vak op{" "}
          <Link href="/onderwijsdoelen" className="text-forest underline">
            de pagina met de doelen
          </Link>
          . Die pagina is voor iedereen zichtbaar, ook zonder account.
        </p>
        <p className="mt-3 rounded-md bg-info/10 px-4 py-3 text-sm text-ink">
          Zet er telkens bij <strong>sinds wanneer</strong> een versie geldt. Zo ziet een ouder
          waarop een hoofdstuk gebouwd is, en zie jij later meteen welk document toe is aan een
          nieuwe versie.
        </p>

        {error && (
          <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
            De lijst kon niet geladen worden: {error.message}. Heb je{" "}
            <code>supabase/doelbestanden.sql</code> al één keer uitgevoerd?
          </p>
        )}

        <ul className="mt-6 space-y-2">
          {rijen.map((d) => {
            const niveau = vindNiveau(d.niveau);
            return (
              <li
                key={d.id}
                className="flex items-start justify-between gap-3 rounded-lg border border-border bg-surface p-3"
              >
                <div className="min-w-0">
                  <p className="text-xs uppercase tracking-wide text-ink-dim">
                    {niveau ? `${niveau.emoji} ${niveau.naam}` : d.niveau}
                    {d.vak ? ` · ${d.vak}` : " · hele niveau"}
                    {d.type === "link" ? " · link" : ""}
                  </p>
                  <p className="font-medium text-ink">{d.titel}</p>
                  {d.geldig_sinds && (
                    <p className="mt-0.5 text-sm text-ink-dim">Geldig sinds {d.geldig_sinds}</p>
                  )}
                  {d.omschrijving && (
                    <p className="mt-0.5 text-sm text-ink-dim">{d.omschrijving}</p>
                  )}
                  {d.link && <p className="mt-0.5 truncate text-xs text-ink-dim">{d.link}</p>}
                </div>
                <form action={verwijderDoelbestand}>
                  <input type="hidden" name="id" value={d.id} />
                  <input type="hidden" name="bestandspad" value={d.bestandspad ?? ""} />
                  <button type="submit" className="shrink-0 text-sm text-danger hover:underline">
                    Verwijderen
                  </button>
                </form>
              </li>
            );
          })}
          {rijen.length === 0 && !error && (
            <li className="text-sm text-ink-dim">Nog niets opgeladen.</li>
          )}
        </ul>

        <section className="mt-10 rounded-xl border border-border bg-surface p-6">
          <h2 className="font-display text-lg font-semibold text-ink">Nieuw document</h2>
          <NieuwDoelbestandForm />
        </section>
      </main>
    </>
  );
}
