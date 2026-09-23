import Link from "next/link";
import { notFound } from "next/navigation";
import { Header } from "@/components/Header";
import { requireBegeleider } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Antwoorden, type Poging, type Vraag } from "../Antwoorden";

/*
  Alle opgeloste testen van één kind, achter elkaar in één document. Bedoeld om
  af te drukken of als pdf te bewaren voor een oudercontact: elke vraag met het
  antwoord dat het kind gaf, en bij een fout antwoord ook het juiste.
*/

type VoortgangRij = Poging & {
  vragen: {
    hoofdstukken: { id: string; titel: string; vakken: { naam: string } };
  };
};

export default async function TestenPage({
  params,
  searchParams,
}: {
  params: Promise<{ kindId: string }>;
  searchParams: Promise<{ hoofdstuk?: string }>;
}) {
  const session = await requireBegeleider();
  const { kindId } = await params;
  const { hoofdstuk: enkelHoofdstuk } = await searchParams;
  const supabase = await createClient();

  const { data: kind } = await supabase
    .from("kinderen")
    .select("id, naam, profiles(full_name, is_plusklas)")
    .eq("id", kindId)
    .single();

  const gezin = (
    kind as { profiles?: { full_name: string; is_plusklas: boolean } } | null
  )?.profiles;
  if (!kind || !gezin?.is_plusklas) notFound();

  const { data: voortgang } = await supabase
    .from("voortgang")
    .select(
      "vraag_id, correct, gegeven_antwoord, beantwoord_op, vragen(hoofdstukken(id, titel, vakken(naam)))",
    )
    .eq("kind_id", kindId)
    .order("beantwoord_op", { ascending: false });

  /* Welke hoofdstukken heeft dit kind aangeraakt, en in welke volgorde tonen we ze? */
  const hoofdstukken = new Map<
    string,
    { titel: string; vak: string; pogingen: Poging[] }
  >();
  for (const rij of (voortgang ?? []) as unknown as VoortgangRij[]) {
    const h = rij.vragen?.hoofdstukken;
    if (!h) continue;
    if (enkelHoofdstuk && h.id !== enkelHoofdstuk) continue;
    if (!hoofdstukken.has(h.id)) {
      hoofdstukken.set(h.id, {
        titel: h.titel,
        vak: h.vakken.naam,
        pogingen: [],
      });
    }
    hoofdstukken.get(h.id)!.pogingen.push({
      vraag_id: rij.vraag_id,
      correct: rij.correct,
      gegeven_antwoord: rij.gegeven_antwoord,
      beantwoord_op: rij.beantwoord_op,
    });
  }

  const ids = [...hoofdstukken.keys()];
  const { data: alleVragen } = ids.length
    ? await supabase
        .from("vragen")
        .select(
          "id, hoofdstuk_id, volgnummer, type, vraag, opties, antwoord, uitleg",
        )
        .in("hoofdstuk_id", ids)
        .order("volgnummer", { ascending: true })
    : { data: [] };

  const vragenPerHoofdstuk = new Map<string, Vraag[]>();
  for (const v of (alleVragen ?? []) as unknown as (Vraag & {
    hoofdstuk_id: string;
  })[]) {
    if (!vragenPerHoofdstuk.has(v.hoofdstuk_id))
      vragenPerHoofdstuk.set(v.hoofdstuk_id, []);
    vragenPerHoofdstuk.get(v.hoofdstuk_id)!.push(v);
  }

  const vandaag = new Date().toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });

  return (
    <>
      <Header naam={session.profile?.full_name} rol={session.profile?.role} />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link
          href={`/begeleiding/${kindId}`}
          className="niet-afdrukken text-sm text-ink-dim hover:text-ink"
        >
          &larr; Fiche van {kind.naam}
        </Link>

        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Opgeloste testen — {kind.naam}
        </h1>
        <p className="mt-1 text-sm text-ink-dim">
          Gezin {gezin.full_name} &middot; afgedrukt op {vandaag}
        </p>
        <p className="mt-3 text-sm text-ink-dim">
          Per vraag staat het antwoord van de laatste poging. Ging het fout, dan
          staat het juiste antwoord eronder.
        </p>

        <p className="niet-afdrukken mt-4 rounded-lg border border-border bg-paper px-4 py-3 text-sm text-ink-dim">
          Wil je dit bewaren als pdf? Kies Afdrukken in je browser en dan
          &ldquo;Opslaan als pdf&rdquo;. De menubalk en de knoppen vallen dan
          weg. Wil je die pdf ook op de fiche houden, laad hem dan op bij{" "}
          <strong className="text-ink">Werk van thuis</strong>.
        </p>

        {ids.length === 0 ? (
          <p className="mt-8 text-sm text-ink-dim">
            Dit kind heeft nog geen vragen beantwoord op het platform.
          </p>
        ) : (
          <div className="mt-8 space-y-10">
            {[...hoofdstukken.entries()].map(([id, h]) => {
              const vragen = vragenPerHoofdstuk.get(id) ?? [];
              const juist = h.pogingen.filter((p) => p.correct).length;
              const beantwoord = new Set(h.pogingen.map((p) => p.vraag_id))
                .size;
              return (
                <section key={id}>
                  <h2 className="font-display text-lg font-semibold text-forest-dark">
                    {h.vak} — {h.titel}
                  </h2>
                  <p className="mt-1 mb-3 text-sm text-ink-dim">
                    {beantwoord} van de {vragen.length}{" "}
                    {vragen.length === 1 ? "vraag" : "vragen"} beantwoord
                    {h.pogingen.length > 0
                      ? `, ${juist} van de ${h.pogingen.length} pogingen juist`
                      : ""}
                    .
                  </p>
                  <Antwoorden
                    vragen={vragen}
                    pogingen={h.pogingen}
                    kindNaam={kind.naam}
                  />
                </section>
              );
            })}
          </div>
        )}
      </main>
    </>
  );
}
