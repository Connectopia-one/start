"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakWebgeschikt } from "@/lib/beeldOmzetten";
import { maakFotoUploadUrl, registreerFoto } from "./actions";

/* Pauze tussen twee foto's, zodat de opslag niet overspoeld wordt. */
const PAUZE_MS = 600;
/* Hoe vaak één foto opnieuw geprobeerd wordt, bv. na "Too many requests". */
const POGINGEN = 4;

function wacht(ms: number) {
  return new Promise((r) => setTimeout(r, ms));
}

function isTeVeel(bericht: string) {
  const b = bericht.toLowerCase();
  return b.includes("too many") || b.includes("429") || b.includes("rate limit");
}

export function NieuweFotosForm({ klasjeId, slug }: { klasjeId: string; slug: string }) {
  const router = useRouter();
  const [status, setStatus] = useState<"idle" | "bezig" | "fout">("idle");
  const [voortgang, setVoortgang] = useState<string | null>(null);
  const [fout, setFout] = useState<string | null>(null);
  const [mislukt, setMislukt] = useState<{ naam: string; reden: string }[]>([]);
  const [gelukt, setGelukt] = useState<string | null>(null);

  /* Eén foto: omzetten, opladen en registreren, met nieuwe pogingen bij een fout. */
  async function laadEenFotoOp(
    supabase: ReturnType<typeof createClient>,
    origineel: File,
    bijschrift: string | null,
    label: string,
  ) {
    const bestand = await maakWebgeschikt(origineel);
    let laatsteFout = "Onbekende fout";

    for (let poging = 1; poging <= POGINGEN; poging++) {
      try {
        const link = await maakFotoUploadUrl(klasjeId, bestand.name);
        if (!link.gelukt) throw new Error(link.bericht);
        const { error } = await supabase.storage.from("fotos").uploadToSignedUrl(link.path, link.token, bestand);
        if (error) throw new Error(error.message);
        const uitkomst = await registreerFoto({ klasjeId, slug, bestandspad: link.path, bijschrift });
        if (!uitkomst.gelukt) throw new Error(uitkomst.bericht);
        return;
      } catch (err) {
        laatsteFout = err instanceof Error ? err.message : String(err);
        if (poging < POGINGEN) {
          const wachttijd = (isTeVeel(laatsteFout) ? 3000 : 1500) * poging;
          setVoortgang(`${label}: even wachten en opnieuw proberen (poging ${poging + 1} van ${POGINGEN})…`);
          await wacht(wachttijd);
        }
      }
    }
    throw new Error(isTeVeel(laatsteFout) ? "De opslag kreeg te veel verzoeken tegelijk (Too many requests)." : laatsteFout);
  }

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);
    setGelukt(null);
    setMislukt([]);

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
    const nietAangekomen: { naam: string; reden: string }[] = [];
    let aantalGelukt = 0;

    for (let i = 0; i < bestanden.length; i++) {
      const label = `Foto ${i + 1} van ${bestanden.length}`;
      setVoortgang(`Bezig met foto ${i + 1} van ${bestanden.length}…`);
      try {
        await laadEenFotoOp(supabase, bestanden[i], bijschrift, label);
        aantalGelukt++;
      } catch (err) {
        nietAangekomen.push({
          naam: bestanden[i].name,
          reden: err instanceof Error ? err.message : "Er ging iets mis.",
        });
      }
      if (i < bestanden.length - 1) await wacht(PAUZE_MS);
    }

    setVoortgang(null);
    setMislukt(nietAangekomen);
    if (nietAangekomen.length === 0) {
      form.reset();
      setStatus("idle");
      setGelukt(aantalGelukt === 1 ? "De foto staat online." : `Alle ${aantalGelukt} foto's staan online.`);
    } else {
      setStatus("fout");
      setGelukt(aantalGelukt > 0 ? `${aantalGelukt} van de ${bestanden.length} foto's staan online.` : null);
    }
    router.refresh();
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-4">
      {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
      {gelukt && <p className="rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{gelukt}</p>}
      {mislukt.length > 0 && (
        <div className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
          <p className="font-medium">
            {mislukt.length === 1 ? "Deze foto is niet aangekomen:" : `Deze ${mislukt.length} foto's zijn niet aangekomen:`}
          </p>
          <ul className="mt-1 list-disc space-y-0.5 pl-5">
            {mislukt.map((m, i) => (
              <li key={i}>
                {m.naam} <span className="text-ink-dim">({m.reden})</span>
              </li>
            ))}
          </ul>
          <p className="mt-1">Kies enkel deze foto&apos;s nog eens en klik opnieuw op Uploaden.</p>
        </div>
      )}
      {voortgang && (
        <p className="rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">{voortgang}</p>
      )}

      <div className="space-y-1.5">
        <label htmlFor="bestanden" className="text-sm font-medium text-ink">
          Foto&apos;s (je kan er meerdere tegelijk kiezen)
        </label>
        <input id="bestanden" name="bestanden" type="file" accept="image/*,.heic,.heif,.dng" multiple className="w-full text-sm" />
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
