import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { requireBegeleider } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { begeleidingTekst as t } from "@/inhoud/begeleiding";
import { NotitieForm } from "./NotitieForm";
import { WerkForm } from "./WerkForm";
import { verwijderNotitie, verwijderWerk } from "./actions";

type VoortgangRij = {
  correct: boolean;
  beantwoord_op: string;
  vragen: {
    hoofdstukken: {
      id: string;
      titel: string;
      vakken: { id: string; naam: string };
    };
  };
};
type StickerRij = {
  id: string;
  verdiend_op: string;
  hoofdstukken: { titel: string; vakken: { naam: string } };
};
type Notitie = {
  id: string;
  datum: string;
  soort: string;
  tekst: string;
  auteur_naam: string | null;
};
type Document = {
  id: string;
  datum: string;
  titel: string;
  omschrijving: string | null;
  bestandspad: string;
  auteur_naam: string | null;
};

type HoofdstukStat = {
  titel: string;
  aantal: number;
  correct: number;
  laatst: string;
};
type VakStat = { naam: string; hoofdstukken: Map<string, HoofdstukStat> };

function datum(waarde: string) {
  return new Date(waarde).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

export default async function FichePage({
  params,
}: {
  params: Promise<{ kindId: string }>;
}) {
  const session = await requireBegeleider();
  const { kindId } = await params;
  const supabase = await createClient();

  const { data: kind } = await supabase
    .from("kinderen")
    .select("id, naam, created_at, profiles(full_name, is_plusklas)")
    .eq("id", kindId)
    .single();

  const gezin = (
    kind as { profiles?: { full_name: string; is_plusklas: boolean } } | null
  )?.profiles;
  /* Enkel plusklaskinderen hebben een fiche — ook voor jou als beheerder. */
  if (!kind || !gezin?.is_plusklas) notFound();

  const [
    { data: rijen },
    { data: stickers },
    { data: notities },
    { data: documenten },
  ] = await Promise.all([
    supabase
      .from("voortgang")
      .select(
        "correct, beantwoord_op, vragen(hoofdstukken(id, titel, vakken(id, naam)))",
      )
      .eq("kind_id", kindId)
      .order("beantwoord_op", { ascending: false }),
    supabase
      .from("stickers")
      .select("id, verdiend_op, hoofdstukken(titel, vakken(naam))")
      .eq("kind_id", kindId)
      .order("verdiend_op", { ascending: false }),
    supabase
      .from("kind_notities")
      .select("id, datum, soort, tekst, auteur_naam")
      .eq("kind_id", kindId)
      .order("datum", { ascending: false })
      .order("created_at", { ascending: false }),
    supabase
      .from("kind_documenten")
      .select("id, datum, titel, omschrijving, bestandspad, auteur_naam")
      .eq("kind_id", kindId)
      .order("datum", { ascending: false }),
  ]);

  /* Voortgang samenvatten per vak en per hoofdstuk. */
  const vakken = new Map<string, VakStat>();
  let totaal = 0;
  let juist = 0;
  for (const rij of (rijen ?? []) as unknown as VoortgangRij[]) {
    const hoofdstuk = rij.vragen?.hoofdstukken;
    const vak = hoofdstuk?.vakken;
    if (!hoofdstuk || !vak) continue;
    totaal += 1;
    if (rij.correct) juist += 1;
    if (!vakken.has(vak.id))
      vakken.set(vak.id, { naam: vak.naam, hoofdstukken: new Map() });
    const v = vakken.get(vak.id)!;
    if (!v.hoofdstukken.has(hoofdstuk.id)) {
      v.hoofdstukken.set(hoofdstuk.id, {
        titel: hoofdstuk.titel,
        aantal: 0,
        correct: 0,
        laatst: rij.beantwoord_op,
      });
    }
    const h = v.hoofdstukken.get(hoofdstuk.id)!;
    h.aantal += 1;
    if (rij.correct) h.correct += 1;
    if (rij.beantwoord_op > h.laatst) h.laatst = rij.beantwoord_op;
  }

  /*
    De opslagmap staat niet op publiek, want er zit werk van kinderen in.
    Daarom maken we per document een link die een uur geldig blijft.
  */
  const paden = ((documenten ?? []) as Document[]).map((d) => d.bestandspad);
  const { data: links } = paden.length
    ? await supabase.storage.from("kinddossier").createSignedUrls(paden, 3600)
    : { data: null };
  const linkPerPad = new Map(
    (links ?? []).map((l) => [l.path ?? "", l.signedUrl]),
  );

  const soortLabel = new Map(
    t.soorten.map((s) => [s.waarde as string, s.label]),
  );

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link
          href="/begeleiding"
          className="niet-afdrukken text-sm text-ink-dim hover:text-ink"
        >
          &larr; {t.titel}
        </Link>

        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          {kind.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Gezin {gezin.full_name} &middot; op het platform sinds{" "}
          {datum(kind.created_at)}
        </p>

        {/* Voortgang */}
        <section className="mt-8">
          <h2 className="font-display text-lg font-semibold text-ink">
            {t.fiche.voortgangKop}
          </h2>
          {totaal === 0 ? (
            <p className="mt-2 text-sm text-ink-dim">{t.fiche.voortgangLeeg}</p>
          ) : (
            <>
              <p className="mt-1 text-sm text-ink-dim">
                {totaal} {totaal === 1 ? "vraag" : "vragen"} beantwoord, waarvan{" "}
                {juist} juist ({Math.round((juist / totaal) * 100)}%).
              </p>
              <div className="mt-3 space-y-5">
                {[...vakken.entries()].map(([vakId, vak]) => (
                  <div key={vakId}>
                    <h3 className="font-display text-base font-semibold text-forest-dark">
                      {vak.naam}
                    </h3>
                    <div className="mt-2 overflow-hidden rounded-lg border border-border">
                      <table className="w-full text-sm">
                        <thead className="bg-paper text-left text-xs text-ink-dim">
                          <tr>
                            <th className="px-3 py-2">Hoofdstuk</th>
                            <th className="px-3 py-2">Score</th>
                            <th className="px-3 py-2">Laatst geoefend</th>
                          </tr>
                        </thead>
                        <tbody>
                          {[...vak.hoofdstukken.entries()].map(([id, h]) => (
                            <tr key={id} className="border-t border-border">
                              <td className="px-3 py-2 text-ink">{h.titel}</td>
                              <td className="px-3 py-2 text-ink">
                                {h.correct}/{h.aantal} (
                                {Math.round((h.correct / h.aantal) * 100)}%)
                              </td>
                              <td className="px-3 py-2 text-ink-dim">
                                {datum(h.laatst)}
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </div>
                ))}
              </div>
            </>
          )}
        </section>

        {/* Stickers */}
        {!!stickers?.length && (
          <section className="mt-8">
            <h2 className="font-display text-lg font-semibold text-ink">
              {t.fiche.stickersKop} ({stickers.length})
            </h2>
            <div className="mt-2 flex flex-wrap gap-2">
              {((stickers ?? []) as unknown as StickerRij[]).map((s) => (
                <span
                  key={s.id}
                  className="flex items-center gap-1.5 rounded-full border border-amber/40 bg-amber/10 px-3 py-1.5 text-xs font-medium text-amber"
                >
                  🌟 {s.hoofdstukken.vakken.naam} — {s.hoofdstukken.titel}
                </span>
              ))}
            </div>
          </section>
        )}

        {/* Opmerkingen */}
        <section className="mt-10">
          <h2 className="font-display text-lg font-semibold text-ink">
            {t.fiche.notitiesKop}
          </h2>
          <p className="mt-1 text-sm text-ink-dim">{t.fiche.notitiesUitleg}</p>

          <NotitieForm kindId={kindId} />

          {!notities?.length ? (
            <p className="mt-4 text-sm text-ink-dim">{t.fiche.notitiesLeeg}</p>
          ) : (
            <ul className="mt-4 space-y-3">
              {(notities as Notitie[]).map((n) => (
                <li
                  key={n.id}
                  className="rounded-lg border border-border bg-surface p-4"
                >
                  <div className="flex flex-wrap items-baseline justify-between gap-2">
                    <span className="text-xs font-medium uppercase tracking-wide text-forest">
                      {soortLabel.get(n.soort) ?? n.soort}
                    </span>
                    <span className="text-xs text-ink-dim">
                      {datum(n.datum)}
                      {n.auteur_naam ? ` · ${n.auteur_naam}` : ""}
                    </span>
                  </div>
                  <p className="mt-2 whitespace-pre-wrap text-sm text-ink">
                    {n.tekst}
                  </p>
                  <form
                    action={verwijderNotitie}
                    className="niet-afdrukken mt-2"
                  >
                    <input type="hidden" name="kindId" value={kindId} />
                    <input type="hidden" name="id" value={n.id} />
                    <button
                      type="submit"
                      className="text-xs text-ink-dim underline-offset-2 hover:text-danger hover:underline"
                    >
                      Verwijderen
                    </button>
                  </form>
                </li>
              ))}
            </ul>
          )}
        </section>

        {/* Werk van thuis */}
        <section className="mt-10">
          <h2 className="font-display text-lg font-semibold text-ink">
            {t.fiche.documentenKop}
          </h2>
          <p className="mt-1 text-sm text-ink-dim">
            {t.fiche.documentenUitleg}
          </p>

          <WerkForm kindId={kindId} />

          {!documenten?.length ? (
            <p className="mt-4 text-sm text-ink-dim">
              {t.fiche.documentenLeeg}
            </p>
          ) : (
            <ul className="mt-4 space-y-2">
              {(documenten as Document[]).map((d) => {
                const href = linkPerPad.get(d.bestandspad);
                return (
                  <li
                    key={d.id}
                    className="flex flex-wrap items-baseline justify-between gap-2 rounded-lg border border-border bg-surface p-4"
                  >
                    <div>
                      {href ? (
                        <a
                          href={href}
                          target="_blank"
                          rel="noopener noreferrer"
                          className="font-medium text-forest-dark hover:underline"
                        >
                          {d.titel} ↗
                        </a>
                      ) : (
                        <span className="font-medium text-ink">{d.titel}</span>
                      )}
                      {d.omschrijving && (
                        <span className="mt-1 block text-sm text-ink-dim">
                          {d.omschrijving}
                        </span>
                      )}
                      <span className="mt-1 block text-xs text-ink-dim">
                        {datum(d.datum)}
                        {d.auteur_naam ? ` · ${d.auteur_naam}` : ""}
                      </span>
                    </div>
                    <form action={verwijderWerk} className="niet-afdrukken">
                      <input type="hidden" name="kindId" value={kindId} />
                      <input type="hidden" name="id" value={d.id} />
                      <input
                        type="hidden"
                        name="bestandspad"
                        value={d.bestandspad}
                      />
                      <button
                        type="submit"
                        className="text-xs text-ink-dim underline-offset-2 hover:text-danger hover:underline"
                      >
                        Verwijderen
                      </button>
                    </form>
                  </li>
                );
              })}
            </ul>
          )}
        </section>
      </main>
    </>
  );
}
