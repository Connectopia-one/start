import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { requireIngelogd } from "@/lib/auth";
import { vereisOuderPin } from "@/lib/ouderpin";
import { createClient } from "@/lib/supabase/server";
import { VraagTekst } from "@/components/Figuren";
import { Formule } from "@/components/Formule";
import { variantVoorBeurt } from "@/lib/spellingvariant";
import { alleRijen } from "@/lib/allerijen";
import { formatAntwoord } from "@/lib/antwoordWeergave";
import { type VraagType } from "@/lib/vraagvorm";

/*
  "Nog te oefenen": alle vragen waarvan de laatste poging van dit kind fout
  was, over alle vakken heen. Sarah en Linda vroegen in de enquête van
  november 2026 om de fouten van hun kind te kunnen zien zonder elk hoofdstuk
  apart te openen. Wat het kind intussen wél juist had, valt er vanzelf af.
  Staat er een pincode op het account, dan gaat deze pagina pas open na die
  pincode (lib/ouderpin.ts).
*/

type Vraag = {
  id: string;
  volgnummer: number;
  type: VraagType;
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean | number[] | string[];
  uitleg: string | null;
  varianten?: unknown;
  hoofdstukken: {
    id: string;
    titel: string;
    volgnummer: number;
    vakken: { naam: string; slug: string } | null;
  } | null;
};

type VoortgangRij = {
  vraag_id: string;
  correct: boolean;
  gegeven_antwoord: number | string | boolean | number[] | null;
  beantwoord_op: string;
  variant?: number | null;
};

const PAKJE = 150;

export default async function NogTeOefenenPage({
  params,
}: {
  params: Promise<{ kindId: string }>;
}) {
  const session = await requireIngelogd();
  const { kindId } = await params;
  await vereisOuderPin(session.userId, `/account/kinderen/${kindId}/fouten`);
  const supabase = await createClient();

  const { data: kind } = await supabase
    .from("kinderen")
    .select("id, naam, profile_id")
    .eq("id", kindId)
    .single();
  if (
    !kind ||
    (kind.profile_id !== session.userId &&
      session.profile?.role !== "beheerder")
  )
    notFound();

  const voortgang = (await alleRijen((van, tot) =>
    supabase
      .from("voortgang")
      .select("*")
      .eq("kind_id", kindId)
      .order("beantwoord_op", { ascending: false })
      .order("id")
      .range(van, tot),
  )) as VoortgangRij[];

  // De laatste poging per vraag. Was die fout, dan staat de vraag hier.
  const laatste = new Map<string, VoortgangRij>();
  for (const rij of voortgang) {
    if (!laatste.has(rij.vraag_id)) laatste.set(rij.vraag_id, rij);
  }
  const foutIds = [...laatste.values()]
    .filter((r) => !r.correct)
    .map((r) => r.vraag_id);

  const vragen: Vraag[] = [];
  for (let i = 0; i < foutIds.length; i += PAKJE) {
    const { data } = await supabase
      .from("vragen")
      .select("*, hoofdstukken(id, titel, volgnummer, vakken(naam, slug))")
      .in("id", foutIds.slice(i, i + PAKJE));
    vragen.push(...((data ?? []) as Vraag[]));
  }

  // Per vak, en daarbinnen per hoofdstuk, in de volgorde van het vak.
  type Groep = {
    titel: string;
    volgnummer: number;
    vakNaam: string;
    vakSlug: string;
    vragen: Vraag[];
  };
  const groepen = new Map<string, Groep>();
  for (const v of vragen) {
    const h = v.hoofdstukken;
    if (!h || !h.vakken) continue;
    let g = groepen.get(h.id);
    if (!g) {
      g = {
        titel: h.titel,
        volgnummer: h.volgnummer,
        vakNaam: h.vakken.naam,
        vakSlug: h.vakken.slug,
        vragen: [],
      };
      groepen.set(h.id, g);
    }
    g.vragen.push(v);
  }
  const lijst = [...groepen.values()].sort(
    (a, b) =>
      a.vakNaam.localeCompare(b.vakNaam, "nl") || a.volgnummer - b.volgnummer,
  );
  for (const g of lijst) g.vragen.sort((a, b) => a.volgnummer - b.volgnummer);
  const totaal = lijst.reduce((s, g) => s + g.vragen.length, 0);

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-2xl flex-1 px-6 py-10">
        <Link
          href={`/account/kinderen/${kindId}`}
          className="text-sm text-ink-dim hover:text-ink"
        >
          &larr; Voortgang — {kind.naam}
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Nog te oefenen — {kind.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          {totaal === 0
            ? `Er staat niets open: elke vraag die ${kind.naam} maakte, was de laatste keer juist.`
            : `${totaal} ${totaal === 1 ? "vraag" : "vragen"} waarvan de laatste poging nog niet juist was. Wat ${kind.naam} intussen juist heeft, verdwijnt vanzelf uit deze lijst.`}
        </p>

        <div className="mt-6 space-y-8">
          {lijst.map((g) => (
            <section key={`${g.vakSlug}-${g.volgnummer}`}>
              <div className="flex flex-wrap items-baseline justify-between gap-2">
                <h2 className="font-display text-lg font-semibold text-forest-dark">
                  {g.vakNaam} — {g.titel}
                </h2>
                <Link
                  href={`/vakken/${g.vakSlug}/${g.volgnummer}`}
                  className="text-sm text-forest-dark hover:underline"
                >
                  Opnieuw oefenen &rarr;
                </Link>
              </div>
              <div className="mt-2 space-y-3">
                {g.vragen.map((rij) => {
                  const poging = laatste.get(rij.id);
                  const vraag = variantVoorBeurt(rij, rij.varianten, poging?.variant);
                  return (
                    <div
                      key={rij.id}
                      className="rounded-xl border border-border bg-surface p-5"
                    >
                      <VraagTekst tekst={vraag.vraag} />
                      <div className="mt-3 rounded-md bg-amber/10 px-3 py-2 text-sm text-ink">
                        Antwoord van {kind.naam}:{" "}
                        <strong>
                          <Formule
                            tekst={formatAntwoord(vraag, poging?.gegeven_antwoord ?? null)}
                          />
                        </strong>
                      </div>
                      <p className="mt-2 text-sm text-ink-dim">
                        Juiste antwoord:{" "}
                        <strong className="text-ink">
                          <Formule tekst={formatAntwoord(vraag, vraag.antwoord)} />
                        </strong>
                      </p>
                      {vraag.uitleg && (
                        <p className="mt-2 text-sm text-ink-dim">
                          <Formule tekst={vraag.uitleg} />
                        </p>
                      )}
                    </div>
                  );
                })}
              </div>
            </section>
          ))}
        </div>
      </main>
    </>
  );
}
