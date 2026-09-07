"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakLeerstofUploadUrl, registreerLeerstof } from "./actions";

export function NieuwLeerstofForm({
  hoofdstukId,
  vakSlug,
  volgnummer,
}: {
  hoofdstukId: string;
  vakSlug: string;
  volgnummer: string;
}) {
  const router = useRouter();
  const [status, setStatus] = useState<"idle" | "bezig" | "fout">("idle");
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);
    const titel = String(data.get("titel") || "").trim();
    const bestand = data.get("bestand");

    try {
      if (!titel) throw new Error("Vul een titel in.");
      if (!(bestand instanceof File) || bestand.size === 0) {
        throw new Error("Kies een bestand om te uploaden.");
      }

      const { path, token } = await maakLeerstofUploadUrl(hoofdstukId, bestand.name);
      const supabase = createClient();
      const { error: uploadError } = await supabase.storage.from("leerstof").uploadToSignedUrl(path, token, bestand);
      if (uploadError) throw new Error("Uploaden mislukt: " + uploadError.message);

      await registreerLeerstof({ hoofdstukId, vakSlug, volgnummer, titel, bestandspad: path });

      form.reset();
      setStatus("idle");
      router.refresh();
    } catch (err) {
      setStatus("fout");
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-3">
      {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

      <div className="space-y-1.5">
        <label htmlFor="titel" className="text-sm font-medium text-ink">
          Titel
        </label>
        <input
          id="titel"
          name="titel"
          required
          placeholder="bv. Leerbundel — Breuken"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label htmlFor="bestand" className="text-sm font-medium text-ink">
          Bestand (PDF)
        </label>
        <input id="bestand" name="bestand" type="file" accept="application/pdf" className="w-full text-sm" />
      </div>

      <button
        type="submit"
        disabled={status === "bezig"}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {status === "bezig" ? "Bezig met uploaden…" : "Toevoegen"}
      </button>
    </form>
  );
}
