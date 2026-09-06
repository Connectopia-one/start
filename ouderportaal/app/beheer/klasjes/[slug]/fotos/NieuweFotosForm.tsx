"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakFotoUploadUrl, registreerFoto } from "./actions";

export function NieuweFotosForm({ klasjeId, slug }: { klasjeId: string; slug: string }) {
  const router = useRouter();
  const [status, setStatus] = useState<"idle" | "bezig" | "fout">("idle");
  const [voortgang, setVoortgang] = useState<string | null>(null);
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);
    const bijschrift = String(data.get("bijschrift") || "").trim() || null;
    const bestanden = (data.getAll("bestanden") as File[]).filter((f) => f instanceof File && f.size > 0);

    if (bestanden.length === 0) {
      setStatus("fout");
      setFout("Kies minstens één foto.");
      return;
    }

    const supabase = createClient();

    try {
      for (let i = 0; i < bestanden.length; i++) {
        const bestand = bestanden[i];
        setVoortgang(`Bezig met foto ${i + 1} van ${bestanden.length}…`);

        const { path, token } = await maakFotoUploadUrl(klasjeId, bestand.name);
        const { error: uploadError } = await supabase.storage.from("fotos").uploadToSignedUrl(path, token, bestand);
        if (uploadError) throw new Error(`Foto "${bestand.name}" uploaden mislukt: ${uploadError.message}`);

        await registreerFoto({ klasjeId, slug, bestandspad: path, bijschrift });
      }

      form.reset();
      setStatus("idle");
      setVoortgang(null);
      router.refresh();
    } catch (err) {
      setStatus("fout");
      setVoortgang(null);
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-4">
      {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
      {voortgang && (
        <p className="rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{voortgang}</p>
      )}

      <div className="space-y-1.5">
        <label htmlFor="bestanden" className="text-sm font-medium text-ink">
          Foto&apos;s (je kan er meerdere tegelijk kiezen)
        </label>
        <input id="bestanden" name="bestanden" type="file" accept="image/*" multiple className="w-full text-sm" />
      </div>
      <div className="space-y-1.5">
        <label htmlFor="bijschrift" className="text-sm font-medium text-ink">
          Bijschrift (optioneel, geldt voor alle gekozen foto&apos;s)
        </label>
        <input
          id="bijschrift"
          name="bijschrift"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>
      <button
        type="submit"
        disabled={status === "bezig"}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {status === "bezig" ? "Bezig met uploaden…" : "Uploaden"}
      </button>
    </form>
  );
}
