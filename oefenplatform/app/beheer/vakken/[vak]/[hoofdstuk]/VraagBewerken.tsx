"use client";

import { useState, type FormEvent, type ReactNode } from "react";
import { useRouter } from "next/navigation";
import { bewerkVraag } from "./actions";

type Antwoord = number | string | boolean | number[] | string[];

const VELD =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

/**
 * Zet het antwoord zoals het in de databank staat terug om naar wat je in het
 * veld intikt, zodat het formulier begint met wat er nu écht staat. De weg
 * terug staat in actions.ts (leesAntwoord); die twee horen bij elkaar.
 */
function antwoordAlsTekst(type: string, antwoord: Antwoord): string {
  if (type === "waarofniet") return antwoord === true || antwoord === "waar" ? "waar" : "niet waar";
  if (Array.isArray(antwoord)) return antwoord.join(type === "meerkeuze" ? ", " : " | ");
  return String(antwoord);
}

/**
 * De knop "Aanpassen" bij een vraag, en het formulier dat eronder openklapt.
 *
 * Zolang je niets aanpast, zie je gewoon de vraag zoals ze was: die staat als
 * `children` in dit component, door de pagina zelf gemaakt. Pas als je op
 * Aanpassen klikt, komt het formulier in de plaats. Zo blijft de lijst rustig
 * ook als er veertig vragen onder elkaar staan.
 */
export function VraagBewerken({
  vraag,
  vakSlug,
  volgnummer,
  verwijderen,
  children,
}: {
  vraag: { id: string; type: string; vraag: string; opties: string[] | null; antwoord: Antwoord; uitleg: string | null };
  vakSlug: string;
  volgnummer: string;
  verwijderen: ReactNode;
  children: ReactNode;
}) {
  const router = useRouter();
  const [open, setOpen] = useState(false);
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);
    try {
      await bewerkVraag(new FormData(e.currentTarget));
      setOpen(false);
      router.refresh();
    } catch (err) {
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    } finally {
      setBezig(false);
    }
  }

  if (!open) {
    return (
      <div className="flex items-start justify-between gap-3">
        {children}
        <div className="flex shrink-0 flex-col items-end gap-1">
          <button type="button" onClick={() => setOpen(true)} className="text-xs text-forest hover:underline">
            Aanpassen
          </button>
          {verwijderen}
        </div>
      </div>
    );
  }

  return (
    <form onSubmit={onSubmit} className="space-y-3">
      <input type="hidden" name="id" value={vraag.id} />
      <input type="hidden" name="vak_slug" value={vakSlug} />
      <input type="hidden" name="volgnummer" value={volgnummer} />

      {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Type</label>
        <select name="type" defaultValue={vraag.type} className={VELD}>
          <option value="meerkeuze">Meerkeuze</option>
          <option value="waarofniet">Waar of niet waar</option>
          <option value="invultekst">Invultekst</option>
        </select>
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">Vraag</label>
        <textarea name="vraag" required rows={2} defaultValue={vraag.vraag} className={VELD} />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Opties <span className="font-normal text-ink-dim">(enkel bij meerkeuze, één per regel)</span>
        </label>
        <textarea name="opties" rows={3} defaultValue={(vraag.opties ?? []).join("\n")} className={VELD} />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Antwoord{" "}
          <span className="font-normal text-ink-dim">
            (verschuift een optie van plaats, pas dan ook het nummer hier aan)
          </span>
        </label>
        <input
          name="antwoord"
          required
          defaultValue={antwoordAlsTekst(vraag.type, vraag.antwoord)}
          className={VELD}
        />
      </div>

      <div className="space-y-1.5">
        <label className="text-sm font-medium text-ink">
          Uitleg <span className="font-normal text-ink-dim">(optioneel)</span>
        </label>
        <textarea name="uitleg" rows={2} defaultValue={vraag.uitleg ?? ""} className={VELD} />
      </div>

      <div className="flex items-center gap-3">
        <button
          type="submit"
          disabled={bezig}
          className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
        >
          {bezig ? "Bezig..." : "Bewaren"}
        </button>
        <button type="button" onClick={() => setOpen(false)} className="text-sm text-ink-dim hover:text-ink">
          Laat maar
        </button>
      </div>
      <p className="text-xs text-ink-dim">
        De afbeelding bij deze vraag blijft staan zoals ze is. Wat de kinderen al gemaakt hebben, blijft ook
        meetellen.
      </p>
    </form>
  );
}
