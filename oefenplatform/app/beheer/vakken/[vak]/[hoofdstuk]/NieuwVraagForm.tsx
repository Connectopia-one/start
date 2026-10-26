"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakVraag, maakVraagAfbeeldingUploadUrl } from "./actions";
import { TypeOpties, VormHulp, ZonePrikker } from "./VormHulp";

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
  // Bij een klikvraag trek je het juiste vak op de prent zelf, dus moeten het
  // type, de gekozen prent en het antwoord hier bekend zijn.
  const [type, setType] = useState("meerkeuze");
  const [prent, setPrent] = useState<string | null>(null);
  const [antwoord, setAntwoord] = useState("");

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

      const uitkomst = await maakVraag(data);
      if (uitkomst?.fout) throw new Error(uitkomst.fout);
      form.reset();
      setType("meerkeuze");
      setAntwoord("");
      setPrent(null);
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
          value={type}
          onChange={(e) => setType(e.target.value)}
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        >
          <TypeOpties />
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
          Opties <span className="font-normal text-ink-dim">(bij meerkeuze de keuzes, bij een tabel de uitspraken, één per regel)</span>
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
          value={antwoord}
          onChange={(e) => setAntwoord(e.target.value)}
          placeholder='Meerkeuze: nummer (0, 1, 2...), of meerdere met een komma: 0,2 · Waar/niet: "waar" of "niet waar" · Invultekst: het juiste woord, of meerdere met een streep ertussen: planteneters | herbivoren'
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
      </div>

      {type === "hotspot" &&
        (prent ? (
          <ZonePrikker src={prent} waarde={antwoord} onWaarde={setAntwoord} />
        ) : (
          <p className="text-xs text-ink-dim">Kies hieronder eerst een afbeelding; daarna trek je er het juiste vak op.</p>
        ))}

      <VormHulp />

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Casus <span className="font-normal text-ink-dim">(optioneel: een situatie die boven de vraag staat)</span>
        </label>
        <textarea
          name="casus"
          rows={2}
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
        <input
          name="afbeelding"
          type="file"
          accept="image/*"
          onChange={(e) => {
            const f = e.target.files?.[0];
            setPrent(f ? URL.createObjectURL(f) : null);
          }}
          className="block w-full cursor-pointer text-sm text-ink-dim file:mr-3 file:cursor-pointer file:rounded-md file:border-0 file:bg-forest file:px-4 file:py-2 file:text-sm file:font-medium file:text-white hover:file:bg-forest-dark" />
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
