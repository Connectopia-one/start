import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { doelenTekst, doelenBlokken } from "@/inhoud/onderwijsdoelen";

export const metadata = {
  title: "Waarop is dit gebaseerd? — Oefenplatform Connectopia",
  description:
    "Per niveau en per vak: op welke minimumdoelen en op welke vakfiches van de Examencommissie onze oefeningen steunen, met de documenten zelf erbij.",
};

type Doelbestand = {
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

export default async function OnderwijsdoelenPage() {
  const session = await getSessionProfile();
  const supabase = await createClient();

  /* Ook zichtbaar zonder account: de leespolicy op public.doelbestanden staat
     open. Is de tabel er nog niet, dan geeft dit een fout en blijft de pagina
     verder gewoon werken — de uitleg is ook zonder de documenten bruikbaar. */
  const { data } = await supabase
    .from("doelbestanden")
    .select("id, niveau, vak, titel, type, link, bestandspad, geldig_sinds, omschrijving")
    .order("volgnummer", { ascending: true })
    .order("created_at", { ascending: true });

  const bestanden = (data ?? []) as Doelbestand[];

  /* Een pdf staat in een publieke opslagmap, dus een gewoon webadres volstaat. */
  function adres(rij: Doelbestand): string | null {
    if (rij.type === "link") return rij.link;
    if (!rij.bestandspad) return null;
    return supabase.storage.from("materiaal").getPublicUrl(rij.bestandspad).data.publicUrl;
  }

  function Document({ rij }: { rij: Doelbestand }) {
    const href = adres(rij);
    if (!href) return null;
    return (
      <a
        href={href}
        target="_blank"
        rel="noopener noreferrer"
        className="mt-2 block rounded-lg border border-border bg-paper px-4 py-3 transition hover:border-forest"
      >
        <span className="text-sm font-medium text-forest-dark">
          {rij.titel} {rij.type === "pdf" ? "(pdf)" : "↗"}
        </span>
        {rij.geldig_sinds && (
          <span className="mt-0.5 block text-xs text-ink-dim">
            Geldig sinds {rij.geldig_sinds}
          </span>
        )}
        {rij.omschrijving && (
          <span className="mt-0.5 block text-sm text-ink-dim">{rij.omschrijving}</span>
        )}
      </a>
    );
  }

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {doelenTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">{doelenTekst.titel}</h1>
        <p className="mt-4 text-sm text-ink-dim">{doelenTekst.intro}</p>
        <p className="mt-3 text-sm text-ink-dim">{doelenTekst.bestandenUitleg}</p>

        <div className="mt-8 space-y-6">
          {doelenBlokken.map((blok) => {
            const vanNiveau = bestanden.filter((b) => b.niveau === blok.slug);
            const algemeen = vanNiveau.filter((b) => !b.vak);

            return (
              <section
                key={blok.slug}
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
                {algemeen.map((rij) => (
                  <Document key={rij.id} rij={rij} />
                ))}

                <dl className="mt-4 space-y-4 border-t border-border pt-4">
                  {blok.vakken.map((vak) => {
                    const vanVak = vanNiveau.filter((b) => b.vak === vak.naam);
                    return (
                      <div key={vak.naam}>
                        <dt className="text-sm font-medium text-ink">{vak.naam}</dt>
                        <dd className="mt-0.5 text-sm text-ink-dim">
                          {vak.doelen}
                          {vak.stand && (
                            <span className="mt-1 block text-xs text-ink-dim">{vak.stand}</span>
                          )}
                          {vanVak.map((rij) => (
                            <Document key={rij.id} rij={rij} />
                          ))}
                        </dd>
                      </div>
                    );
                  })}
                </dl>
              </section>
            );
          })}
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
