import Link from "next/link";
import { requireBeheerder } from "@/lib/auth";
import { createClient } from "@/lib/supabase/server";
import { Header } from "@/components/Header";
import { BulkLeerstofForm, type Bundel, type Vak } from "./BulkLeerstofForm";

export default async function BeheerLeerstofPage() {
  const session = await requireBeheerder();
  const supabase = await createClient();

  const { data: vakken } = await supabase
    .from("vakken")
    .select("id, naam, hoofdstukken(id, titel, niveau, volgnummer)")
    .order("volgorde", { ascending: true });

  const lijst = (vakken as Vak[] | null)?.filter((v) => v.hoofdstukken.length > 0) ?? [];

  // Welke bundels staan er al? Daarmee kan het formulier waarschuwen dat een
  // hoofdstuk er al een heeft, en aanbieden om die te vervangen.
  const { data: bundels } = await supabase
    .from("leerstof")
    .select("id, hoofdstuk_id, titel, created_at")
    .order("created_at", { ascending: true });

  return (
    <>
      <Header naam={session.profile?.full_name} rol="beheerder" />
      <main className="mx-auto w-full max-w-3xl flex-1 px-6 py-10">
        <Link href="/beheer" className="text-sm text-ink-dim hover:text-ink">
          &larr; Beheer
        </Link>
        <h1 className="mt-2 font-display text-2xl font-semibold text-ink">
          Leerbundels in één keer uploaden
        </h1>
        <p className="mt-2 text-sm text-ink-dim">
          Kies een vak, selecteer alle pdf&apos;s tegelijk en upload ze in één beweging. Het
          platform zoekt zelf het juiste hoofdstuk bij elke bestandsnaam; je kan dat hieronder nog
          aanpassen voor je op uploaden klikt. Heeft een hoofdstuk al een bundel, dan wordt de
          oude vervangen door de nieuwe — tenzij je dat bij dat bestand uitvinkt.
        </p>

        {lijst.length === 0 ? (
          <p className="mt-8 rounded-xl border border-amber/40 bg-amber/10 px-5 py-4 text-sm text-ink">
            Er zijn nog geen hoofdstukken om leerstof bij te zetten. Maak eerst een vak met
            hoofdstukken aan bij{" "}
            <Link href="/beheer/vakken" className="font-medium text-forest-dark underline-offset-2 hover:underline">
              Vakken &amp; hoofdstukken
            </Link>
            .
          </p>
        ) : (
          <BulkLeerstofForm vakken={lijst} bundels={(bundels as Bundel[] | null) ?? []} />
        )}
      </main>
    </>
  );
}
