"use client";

import { useState, type FormEvent } from "react";
import { meldIets } from "@/app/vakken/[vak]/[hoofdstuk]/actions";

type VraagKeuze = { id: string; volgnummer: number; vraag: string };

const SOORTEN = [
  { waarde: "fout", label: "Er staat een fout in" },
  { waarde: "onduidelijk", label: "De vraag is onduidelijk" },
  { waarde: "te-moeilijk", label: "Te moeilijk" },
  { waarde: "te-makkelijk", label: "Te makkelijk" },
  { waarde: "andere", label: "Iets anders" },
];

/** Kort genoeg om in een keuzelijst te passen, lang genoeg om ze te herkennen. */
function kort(tekst: string) {
  const schoon = tekst.replace(/\s+/g, " ").trim();
  return schoon.length > 70 ? schoon.slice(0, 69) + "…" : schoon;
}

export function MeldingKnop({
  hoofdstukId,
  vragen,
}: {
  hoofdstukId: string;
  vragen: VraagKeuze[];
}) {
  const [open, setOpen] = useState(false);
  const [status, setStatus] = useState<"idle" | "bezig" | "klaar">("idle");
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);
    try {
      await meldIets(new FormData(e.currentTarget));
      setStatus("klaar");
    } catch (err) {
      setFout(err instanceof Error ? err.message : "Versturen lukte niet.");
      setStatus("idle");
    }
  }

  if (status === "klaar") {
    return (
      <div className="mt-10 rounded-xl border border-forest/30 bg-forest/5 px-5 py-4 text-sm text-ink">
        <p className="font-medium">Bedankt, je melding is doorgestuurd.</p>
        <p className="mt-1 text-ink-dim">
          We kijken ze na en passen het hoofdstuk aan als het nodig is.
        </p>
      </div>
    );
  }

  if (!open) {
    return (
      <button
        type="button"
        onClick={() => setOpen(true)}
        className="mt-10 w-full rounded-xl border border-border bg-surface px-5 py-3 text-sm text-ink-dim transition hover:border-forest hover:text-ink"
      >
        Iets gezien dat niet klopt in dit hoofdstuk? Laat het ons hier weten.
      </button>
    );
  }

  return (
    <form
      onSubmit={onSubmit}
      className="mt-10 rounded-xl border border-border bg-surface px-5 py-5 text-sm"
    >
      <input type="hidden" name="hoofdstuk_id" value={hoofdstukId} />
      <p className="font-medium text-ink">Wat is er met dit hoofdstuk?</p>

      <label className="mt-4 block text-ink-dim" htmlFor="melding-soort">
        Waarover gaat het?
      </label>
      <select
        id="melding-soort"
        name="soort"
        defaultValue="fout"
        className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-ink"
      >
        {SOORTEN.map((s) => (
          <option key={s.waarde} value={s.waarde}>
            {s.label}
          </option>
        ))}
      </select>

      {vragen.length > 0 && (
        <>
          <label className="mt-4 block text-ink-dim" htmlFor="melding-vraag">
            Over welke vraag? (mag je leeg laten)
          </label>
          <select
            id="melding-vraag"
            name="vraag_id"
            defaultValue=""
            className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-ink"
          >
            <option value="">Over het hoofdstuk in het algemeen</option>
            {vragen.map((v) => (
              <option key={v.id} value={v.id}>
                {v.volgnummer}. {kort(v.vraag)}
              </option>
            ))}
          </select>
        </>
      )}

      <label className="mt-4 block text-ink-dim" htmlFor="melding-bericht">
        Wat klopt er niet?
      </label>
      <textarea
        id="melding-bericht"
        name="bericht"
        required
        rows={4}
        maxLength={2000}
        placeholder="Bijvoorbeeld: het juiste antwoord bij vraag 7 lijkt me niet te kloppen."
        className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-2 text-ink"
      />

      {fout && <p className="mt-3 text-danger">{fout}</p>}

      <div className="mt-4 flex items-center gap-3">
        <button
          type="submit"
          disabled={status === "bezig"}
          className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark disabled:opacity-60"
        >
          {status === "bezig" ? "Bezig…" : "Versturen"}
        </button>
        <button
          type="button"
          onClick={() => setOpen(false)}
          className="text-ink-dim hover:text-ink"
        >
          Annuleren
        </button>
      </div>
    </form>
  );
}
