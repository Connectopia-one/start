import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { materiaalTekst } from "@/inhoud/materiaal";

export const metadata = {
  title: "Handig materiaal — Oefenplatform Connectopia",
  description:
    "Gratis verzameling links naar vakfiches, naslagwerken en oefensites, bijeengebracht door Connectopia vzw.",
};

type Rij = {
  id: string;
  groep: string;
  type: "link" | "pdf";
  titel: string;
  link: string | null;
  bestandspad: string | null;
  omschrijving: string | null;
};

export default async function MateriaalPage() {
  const session = await getSessionProfile();
  const supabase = await createClient();

  /* Ook zichtbaar zonder account: de leespolicy op public.materiaal staat open. */
  const { data } = await supabase
    .from("materiaal")
    .select("id, groep, type, titel, link, bestandspad, omschrijving")
    .order("created_at", { ascending: true });

  const rijen = (data ?? []) as Rij[];

  /* De koppen staan in de volgorde waarin hun eerste item toegevoegd is. */
  const groepen: { kop: string; items: Rij[] }[] = [];
  for (const rij of rijen) {
    const bestaande = groepen.find((g) => g.kop === rij.groep);
    if (bestaande) bestaande.items.push(rij);
    else groepen.push({ kop: rij.groep, items: [rij] });
  }

  /* Een pdf staat in een publieke bucket, dus een gewoon webadres volstaat. */
  function adres(rij: Rij): string | null {
    if (rij.type === "link") return rij.link;
    if (!rij.bestandspad) return null;
    return supabase.storage.from("materiaal").getPublicUrl(rij.bestandspad).data.publicUrl;
  }

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {materiaalTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">{materiaalTekst.titel}</h1>
        <p className="mt-4 text-sm text-ink-dim">{materiaalTekst.intro}</p>

        {groepen.length === 0 ? (
          <p className="mt-6 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            {materiaalTekst.leegTekst}
          </p>
        ) : (
          <div className="mt-8 space-y-9">
            {groepen.map((groep) => (
              <section key={groep.kop}>
                <h2 className="font-display text-lg font-semibold text-ink">{groep.kop}</h2>
                <ul className="mt-3 space-y-2">
                  {groep.items.map((item) => {
                    const href = adres(item);
                    if (!href) return null;
                    return (
                      <li key={item.id}>
                        <a
                          href={href}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="block rounded-xl border border-border bg-surface p-4 transition hover:border-forest hover:shadow-sm"
                        >
                          <span className="font-medium text-forest-dark">
                            {item.titel} {item.type === "pdf" ? "(pdf)" : "↗"}
                          </span>
                          {item.omschrijving && (
                            <span className="mt-1 block text-sm text-ink-dim">
                              {item.omschrijving}
                            </span>
                          )}
                        </a>
                      </li>
                    );
                  })}
                </ul>
              </section>
            ))}
          </div>
        )}

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
