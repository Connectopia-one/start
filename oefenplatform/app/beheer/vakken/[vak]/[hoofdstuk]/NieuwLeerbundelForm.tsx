"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakLeerbundelUploadUrl, voegLeerbundelBlokToe, type LeerbundelSoort } from "./actions";

const SOORTEN: { waarde: LeerbundelSoort; naam: string; uitleg: string }[] = [
  { waarde: "titel", naam: "Tussentitel", uitleg: "Een kopje dat een nieuw stuk aankondigt." },
  { waarde: "tekst", naam: "Tekst", uitleg: "Een stuk uitleg. Een lege regel begint een nieuwe alinea." },
  { waarde: "weetje", naam: "Weetje", uitleg: "Een tip of ezelsbruggetje, in een gekleurd kadertje." },
  { waarde: "afbeelding", naam: "Afbeelding", uitleg: "Een tekening, schema of foto, met een onderschrift eronder." },
];

export function NieuwLeerbundelForm({
  hoofdstukId,
  vakSlug,
  volgnummer,
}: {
  hoofdstukId: string;
  vakSlug: string;
  volgnummer: string;
}) {
  const router = useRouter();
  const [soort, setSoort] = useState<LeerbundelSoort>("tekst");
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  const gekozen = SOORTEN.find((s) => s.waarde === soort)!;

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);
    const tekst = String(data.get("tekst") || "");
    const bestand = data.get("bestand");

    try {
      let afbeeldingPad: string | null = null;

      if (soort === "afbeelding") {
        if (!(bestand instanceof File) || bestand.size === 0) {
          throw new Error("Kies een afbeelding om te uploaden.");
        }
        const { path, token } = await maakLeerbundelUploadUrl(hoofdstukId, bestand.name);
        const supabase = createClient();
        const { error } = await supabase.storage.from("leerbundel").uploadToSignedUrl(path, token, bestand);
        if (error) throw new Error("Uploaden mislukt: " + error.message);
        afbeeldingPad = path;
      }

      await voegLeerbundelBlokToe({
        hoofdstukId,
        vakSlug,
        volgnummer,
        soort,
        tekst: tekst || null,
        afbeeldingPad,
      });

      form.reset();
      router.refresh();
    } catch (err) {
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    } finally {
      setBezig(false);
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-3">
      {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

      <div className="flex flex-wrap gap-2">
        {SOORTEN.map((s) => (
          <button
            key={s.waarde}
            type="button"
            onClick={() => setSoort(s.waarde)}
            className={`rounded-full border px-3 py-1.5 text-sm ${
              soort === s.waarde
                ? "border-forest bg-forest text-white"
                : "border-border text-ink-dim hover:border-forest hover:text-ink"
            }`}
          >
            {s.naam}
          </button>
        ))}
      </div>
      <p className="text-xs text-ink-dim">{gekozen.uitleg}</p>

      {soort === "afbeelding" ? (
        <>
          <div className="space-y-1.5">
            <label htmlFor="bestand" className="text-sm font-medium text-ink">
              Afbeelding
            </label>
            <input id="bestand" name="bestand" type="file" accept="image/*" className="w-full text-sm" />
          </div>
          <div className="space-y-1.5">
            <label htmlFor="tekst" className="text-sm font-medium text-ink">
              Onderschrift (mag leeg blijven)
            </label>
            <input
              id="tekst"
              name="tekst"
              placeholder="bv. De drie soorten hoeken naast elkaar"
              className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            />
          </div>
        </>
      ) : (
        <div className="space-y-1.5">
          <label htmlFor="tekst" className="text-sm font-medium text-ink">
            {soort === "titel" ? "Tussentitel" : soort === "weetje" ? "Weetje" : "Tekst"}
          </label>
          <textarea
            id="tekst"
            name="tekst"
            rows={soort === "titel" ? 1 : 5}
            className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </div>
      )}

      <button
        type="submit"
        disabled={bezig}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {bezig ? "Bezig…" : "Toevoegen aan de bundel"}
      </button>
    </form>
  );
}
