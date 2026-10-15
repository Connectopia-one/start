"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { heicNaarJpeg } from "@/lib/beeldOmzetten";
import { maakFotoUploadUrl, vervangFotoBestand } from "./actions";

type HeicFoto = { id: string; bestandspad: string; url: string };

/*
  Foto's die vroeger als HEIC opgeladen werden, tonen niet in Chrome of Edge.
  Deze knop haalt ze één voor één op, zet ze in de browser om naar JPEG en
  vervangt het bestand. Bijschrift en datum blijven.
*/
export function HeicOmzetten({ fotos, slug }: { fotos: HeicFoto[]; slug: string }) {
  const router = useRouter();
  const [bezig, setBezig] = useState<string | null>(null);
  const [fout, setFout] = useState<string | null>(null);

  async function zetOm() {
    setFout(null);
    const supabase = createClient();
    try {
      for (let i = 0; i < fotos.length; i++) {
        const f = fotos[i];
        setBezig(`Bezig met foto ${i + 1} van ${fotos.length}…`);

        const antwoord = await fetch(f.url);
        if (!antwoord.ok) throw new Error("Een foto kon niet opgehaald worden. Laad de pagina opnieuw.");
        const naam = f.bestandspad.split("/").pop() ?? "foto.heic";
        const jpeg = await heicNaarJpeg(await antwoord.blob(), naam);

        const klasjeId = f.bestandspad.split("/")[0];
        const { path, token } = await maakFotoUploadUrl(klasjeId, jpeg.name);
        const { error } = await supabase.storage.from("fotos").uploadToSignedUrl(path, token, jpeg);
        if (error) throw new Error(`Opladen mislukt: ${error.message}`);

        const uitkomst = await vervangFotoBestand({ id: f.id, slug, oudPad: f.bestandspad, nieuwPad: path });
        if (!uitkomst.gelukt) throw new Error(uitkomst.bericht);
      }
      setBezig(null);
      router.refresh();
    } catch (err) {
      setBezig(null);
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <div className="mt-4 rounded-md border border-border bg-surface px-4 py-3 text-sm text-ink">
      <p>
        {fotos.length === 1 ? "Eén foto staat" : `${fotos.length} foto's staan`} hier als HEIC, het
        formaat van een iPhone. Ouders met Chrome of Edge zien die als gebroken afbeelding.
      </p>
      {fout && <p className="mt-2 text-danger">{fout}</p>}
      <button
        type="button"
        onClick={zetOm}
        disabled={bezig !== null}
        className="mt-2 rounded-md bg-forest px-3 py-1.5 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {bezig ?? "Omzetten naar JPEG"}
      </button>
    </div>
  );
}
