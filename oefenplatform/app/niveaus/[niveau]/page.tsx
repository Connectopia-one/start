import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { heeftVolledigeToegang, hoofdstukToegankelijk } from "@/lib/toegang";
import { createClient } from "@/lib/supabase/server";
import { PRIJS_SCHOOLJAAR_EUR } from "@/lib/mollie";
import { schooljaarEindeLabel } from "@/lib/schooljaar";
import { vindNiveau } from "@/lib/niveaus";

type Hoofdstuk = { id: string; titel: string; volgnummer: number; gratis: boolean; niveau: string };
type Vak = { id: string; naam: string; slug: string; hoofdstukken: Hoofdstuk[] };

export default async function NiveauPage({
  params,
}: {
  params: Promise<{ niveau: string }>;
}) {
  const { niveau: niveauSlug } = await params;
  const niveau = vindNiveau(niveauSlug);
  if (!niveau) notFound();

  const session = await getSessionProfile();
  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select("id, naam, slug, hoofdstukken(id, titel, volgnummer, gratis, niveau)")
    .order("volgorde", { ascending: true });

  const volledigeToegang = heeftVolledigeToegang(session?.profile ?? null);

  const vakkenInNiveau = ((vakken as Vak[] | null) ?? [])
    .map((vak) => ({ ...vak, hoofdstukken: vak.hoofdstukken.filter((h) => h.niveau === niveau.slug) }))
    .filter((vak) => vak.hoofdstukken.length > 0);

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <Link href="/" className="text-sm text-ink-dim hover:text-ink">
          &larr; Alle categorieën
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {niveau.emoji} {niveau.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">{niveau.omschrijving}</p>

        {!volledigeToegang && (
          <div className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            Volledige toegang tot alle hoofdstukken kost{" "}
            <strong>€{PRIJS_SCHOOLJAAR_EUR} per schooljaar</strong>, geldig tot en met{" "}
            {schooljaarEindeLabel()} — de opbrengsten gaan volledig naar vzw Connectopia.{" "}
            <Link href={session ? "/betalen" : "/registreren"} className="font-medium text-forest-dark underline-offset-2 hover:underline">
              {session ? "Nu vrijgeven" : "Account maken en starten"}
            </Link>
          </div>
        )}

        <div className="mt-8 space-y-8">
          {vakkenInNiveau.map((vak) => (
            <section key={vak.id}>
              <h2 className="font-display text-lg font-semibold text-forest-dark">{vak.naam}</h2>
              <ul className="mt-3 space-y-2">
                {vak.hoofdstukken
                  .sort((a, b) => a.volgnummer - b.volgnummer)
                  .map((h) => {
                    const mag = hoofdstukToegankelijk(h.gratis, session?.profile ?? null);
                    return (
                      <li key={h.id}>
                        <Link
                          href={`/vakken/${vak.slug}/${h.volgnummer}`}
                          className="flex items-center justify-between rounded-lg border border-border bg-surface px-4 py-3 text-sm hover:border-forest"
                        >
                          <span className="text-ink">{h.titel}</span>
                          {h.gratis ? (
                            <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                              Gratis
                            </span>
                          ) : mag ? (
                            <span className="rounded-full bg-forest/10 px-2.5 py-0.5 text-xs font-medium text-forest-dark">
                              Vrijgegeven
                            </span>
                          ) : (
                            <span className="rounded-full bg-ink-dim/10 px-2.5 py-0.5 text-xs font-medium text-ink-dim">
                              Op slot
                            </span>
                          )}
                        </Link>
                      </li>
                    );
                  })}
              </ul>
            </section>
          ))}
          {!vakkenInNiveau.length && (
            <p className="text-sm text-ink-dim">Er is nog geen inhoud voor deze categorie.</p>
          )}
        </div>
      </main>
    </>
  );
}
