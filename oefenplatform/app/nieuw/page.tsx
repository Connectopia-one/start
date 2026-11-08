import Link from "next/link";
import { Header } from "@/components/Header";
import { getSessionProfile } from "@/lib/auth";
import { nieuwTekst, updates } from "@/inhoud/nieuw";

export const metadata = {
  title: "Wat is er nieuw? — Oefenplatform Connectopia",
  description:
    "Alle aanpassingen aan het oefenplatform van Connectopia, het nieuwste bovenaan.",
};

/*
  Kim, 8 november 2026: elke update in een apart vakje, zodat ouders echt
  zien wat er weer aangepast is. Ook zichtbaar zonder account.
  De tekst staat volledig in inhoud/nieuw.ts.
*/
export default async function NieuwPage() {
  const session = await getSessionProfile();

  return (
    <>
      <Header naam={session?.profile?.full_name} rol={session?.profile?.role} />
      <main className="mx-auto w-full max-w-4xl flex-1 px-6 py-10">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          {nieuwTekst.label}
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">
          {nieuwTekst.titel}
        </h1>
        <p className="mt-4 max-w-2xl text-sm text-ink-dim">{nieuwTekst.intro}</p>

        <ul className="mt-8 grid grid-cols-1 items-start gap-4 sm:grid-cols-2">
          {updates.map((u) => (
            <li
              key={u.datum + u.titel}
              className="flex h-full flex-col rounded-2xl border border-border bg-surface p-5 shadow-[0_2px_10px_rgba(47,93,80,0.06)]"
            >
              <div className="flex flex-wrap items-center gap-2">
                <span className="text-xs font-medium text-ink-dim">{u.datum}</span>
                {u.opVraag && (
                  <span className="rounded-full bg-forest/10 px-2 py-0.5 text-xs font-medium text-forest-dark">
                    {nieuwTekst.labelOpVraag}
                  </span>
                )}
              </div>
              <h2 className="mt-2 font-display text-[17px] font-semibold leading-snug text-ink">
                {u.titel}
              </h2>
              <p className="mt-2 text-[15px] leading-relaxed text-ink">{u.tekst}</p>
              {u.link && (
                <p className="mt-auto pt-3 text-sm">
                  <Link
                    href={u.link.href}
                    className="text-forest-dark underline-offset-2 hover:underline"
                  >
                    {u.link.tekst} &rarr;
                  </Link>
                </p>
              )}
            </li>
          ))}
        </ul>
      </main>
    </>
  );
}
