"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakVraag, maakVraagAfbeeldingUploadUrl } from "./actions";

export function NieuwVraagForm({
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
    const afbeelding = data.get("afbeelding");

    try {
      if (afbeelding instanceof File && afbeelding.size > 0) {
        const { path, token } = await maakVraagAfbeeldingUploadUrl(hoofdstukId, afbeelding.name);
        const supabase = createClient();
        const { error: uploadError } = await supabase.storage
          .from("vraagafbeeldingen")
          .uploadToSignedUrl(path, token, afbeelding);
        if (uploadError) throw new Error("Uploaden van afbeelding mislukt: " + uploadError.message);
        data.set("afbeelding_pad", path);
      }
      data.delete("afbeelding");

      await maakVraag(data);
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
      <input type="hidden" name="hoofdstuk_id" value={hoofdstukId} />
      <input type="hidden" name="vak_slug" value={vakSlug} />
      <input type="hidden" name="volgnummer" value={volgnummer} />

      {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Type</label>
        <select
          name="type"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        >
          <option value="meerkeuze">Meerkeuze</option>
          <option value="waarofniet">Waar of niet waar</option>
          <option value="invultekst">Invultekst</option>
        </select>
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Vraag</label>
        <textarea
          name="vraag"
          required
          rows={2}
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Opties <span className="font-normal text-ink-dim">(enkel bij meerkeuze, één per regel)</span>
        </label>
        <textarea
          name="opties"
          rows={3}
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Antwoord</label>
        <input
          name="antwoord"
          required
          placeholder='Meerkeuze: nummer (0, 1, 2...), of meerdere met een komma: 0,2 · Waar/niet: "waar" of "niet waar" · Invultekst: het juiste woord'
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Uitleg <span className="font-normal text-ink-dim">(optioneel)</span>
        </label>
        <textarea
          name="uitleg"
          rows={2}
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Afbeelding <span className="font-normal text-ink-dim">(optioneel — bv. een figuur bij meetkunde)</span>
        </label>
        <input name="afbeelding" type="file" accept="image/*" className="block w-full cursor-pointer text-sm text-ink-dim file:mr-3 file:cursor-pointer file:rounded-md file:border-0 file:bg-forest file:px-4 file:py-2 file:text-sm file:font-medium file:text-white hover:file:bg-forest-dark" />
      </div>

      <button
        type="submit"
        disabled={status === "bezig"}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {status === "bezig" ? "Bezig..." : "Vraag toevoegen"}
      </button>
    </form>
  );
}
