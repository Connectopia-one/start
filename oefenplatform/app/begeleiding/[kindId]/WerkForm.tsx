"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakWerkUploadUrl, registreerWerk } from "./actions";

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

export function WerkForm({ kindId }: { kindId: string }) {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  const vandaag = new Date().toISOString().slice(0, 10);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);
    const titel = String(data.get("titel") || "").trim();
    const omschrijving = String(data.get("omschrijving") || "").trim();
    const datum = String(data.get("datum") || "").trim();
    const bestand = data.get("bestand");

    try {
      if (!titel) throw new Error("Geef het werk een titel.");
      if (!(bestand instanceof File) || bestand.size === 0) {
        throw new Error("Kies een bestand om op te laden.");
      }

      const { path, token } = await maakWerkUploadUrl(kindId, bestand.name);
      const supabase = createClient();
      const { error } = await supabase.storage
        .from("kinddossier")
        .uploadToSignedUrl(path, token, bestand);
      if (error) throw new Error("Opladen mislukt: " + error.message);

      await registreerWerk({
        kindId,
        titel,
        bestandspad: path,
        omschrijving,
        datum,
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
    <form
      onSubmit={onSubmit}
      className="niet-afdrukken mt-4 space-y-3 rounded-lg border border-border bg-paper p-4"
    >
      {fout && (
        <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
          {fout}
        </p>
      )}

      <div className="flex flex-wrap gap-3">
        <div className="flex-1 space-y-1.5">
          <label htmlFor="werkTitel" className="text-sm font-medium text-ink">
            Wat is het?
          </label>
          <input
            id="werkTitel"
            name="titel"
            required
            placeholder="Bijvoorbeeld: oefeningen breuken, week 3"
            className={veld}
          />
        </div>
        <div className="space-y-1.5">
          <label htmlFor="werkDatum" className="text-sm font-medium text-ink">
            Datum
          </label>
          <input
            id="werkDatum"
            name="datum"
            type="date"
            defaultValue={vandaag}
            className={veld}
          />
        </div>
      </div>

      <div className="space-y-1.5">
        <label
          htmlFor="werkOmschrijving"
          className="text-sm font-medium text-ink"
        >
          Korte nota <span className="text-ink-dim">(mag leeg blijven)</span>
        </label>
        <input id="werkOmschrijving" name="omschrijving" className={veld} />
      </div>

      <div className="space-y-1.5">
        <label htmlFor="werkBestand" className="text-sm font-medium text-ink">
          Bestand
        </label>
        <input
          id="werkBestand"
          name="bestand"
          type="file"
          accept="application/pdf,image/*"
          required
          className="block w-full text-sm text-ink-dim file:mr-3 file:rounded-md file:border-0 file:bg-forest file:px-3 file:py-2 file:text-sm file:font-medium file:text-white hover:file:bg-forest-dark"
        />
      </div>

      <button
        type="submit"
        disabled={bezig}
        className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white transition hover:bg-forest-dark disabled:opacity-60"
      >
        {bezig ? "Bezig met opladen…" : "Werk opladen"}
      </button>
    </form>
  );
}
