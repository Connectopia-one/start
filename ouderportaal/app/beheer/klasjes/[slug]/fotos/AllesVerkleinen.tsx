"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { moetKleiner, verklein } from "@/lib/beeldOmzetten";
import { maakFotoUploadUrl, vervangFotoBestand } from "./actions";

type Foto = { id: string; url: string; bestandspad: string };

/*
  Eén knop die de foto's van dit klasje die er al staan kleiner maakt.

  Nieuwe foto's worden bij het opladen al verkleind (zie lib/beeldOmzetten.ts),
  maar wat er vóór 26 oktober 2026 opgeladen werd, staat er nog in volle
  grootte. Elke ouder die de fotopagina opent, haalt die binnen, en dat
  verkeer deed Supabase over zijn gratis grens gaan.

  Het verkleinen gebeurt hier in de browser, één foto na de andere. Een foto
  die al klein genoeg is, blijft staan zoals hij is, dus nog eens klikken
  kan geen kwaad.
*/
export function AllesVerkleinen({ fotos, slug }: { fotos: Foto[]; slug: string }) {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);
  const [stand, setStand] = useState<string | null>(null);
  const [fouten, setFouten] = useState<string[]>([]);

  async function start() {
    setBezig(true);
    setFouten([]);
    const supabase = createClient();
    let kleiner = 0;
    let bespaard = 0;
    const mis: string[] = [];
    for (let i = 0; i < fotos.length; i++) {
      const f = fotos[i];
      const naam = f.bestandspad.split("/").pop() ?? "foto";
      setStand(`Foto ${i + 1} van ${fotos.length} nakijken…`);
      try {
        const antwoord = await fetch(f.url);
        if (!antwoord.ok) throw new Error(`de opslag gaf fout ${antwoord.status}`);
        const blob = await antwoord.blob();
        if (!(await moetKleiner(blob))) continue;
        const klein = await verklein(new File([blob], naam, { type: blob.type }));
        if (klein.size >= blob.size) continue;

        const klasjeId = f.bestandspad.split("/")[0];
        const { path, token } = await maakFotoUploadUrl(klasjeId, klein.name);
        const { error } = await supabase.storage.from("fotos").uploadToSignedUrl(path, token, klein);
        if (error) throw new Error(`opladen mislukt: ${error.message}`);
        const uitkomst = await vervangFotoBestand({ id: f.id, slug, oudPad: f.bestandspad, nieuwPad: path });
        if (!uitkomst.gelukt) throw new Error(uitkomst.bericht);
        kleiner++;
        bespaard += blob.size - klein.size;
      } catch (err) {
        mis.push(`${naam}: ${err instanceof Error ? err.message : "er ging iets mis"}`);
      }
    }
    const mb = (bespaard / 1024 / 1024).toFixed(1).replace(".", ",");
    setStand(
      kleiner === 0
        ? "Alle foto's waren al klein genoeg."
        : `${kleiner} ${kleiner === 1 ? "foto" : "foto's"} verkleind, samen ${mb} MB lichter.`,
    );
    setFouten(mis);
    setBezig(false);
    router.refresh();
  }

  if (!fotos.length) return null;

  return (
    <div className="mt-6 rounded-lg border border-border bg-surface px-4 py-3 text-sm">
      <p className="text-ink">
        Foto&apos;s die vroeger opgeladen werden, staan er nog in volle grootte. Verkleinen maakt de fotopagina voor
        de ouders sneller en spaart verkeer bij Supabase. Op een scherm zie je geen verschil.
      </p>
      <button
        type="button"
        onClick={start}
        disabled={bezig}
        className="mt-2 rounded-md bg-forest px-3 py-1.5 font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {bezig ? "Bezig…" : "Alle foto's van dit klasje verkleinen"}
      </button>
      {stand && <p className="mt-2 text-ink-dim">{stand}</p>}
      {fouten.length > 0 && (
        <ul className="mt-2 list-disc pl-5 text-danger">
          {fouten.map((f) => (
            <li key={f}>{f}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
