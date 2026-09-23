"use client";

import { useRef, useState } from "react";
import { useRouter } from "next/navigation";
import { begeleidingTekst as t } from "@/inhoud/begeleiding";
import { voegNotitieToe } from "./actions";

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

export function NotitieForm({ kindId }: { kindId: string }) {
  const router = useRouter();
  const formRef = useRef<HTMLFormElement>(null);
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  const vandaag = new Date().toISOString().slice(0, 10);

  return (
    <form
      ref={formRef}
      action={async (data) => {
        setBezig(true);
        setFout(null);
        try {
          await voegNotitieToe(data);
          formRef.current?.reset();
          router.refresh();
        } catch (err) {
          setFout(err instanceof Error ? err.message : "Er ging iets mis.");
        } finally {
          setBezig(false);
        }
      }}
      className="niet-afdrukken mt-4 space-y-3 rounded-lg border border-border bg-paper p-4"
    >
      {fout && (
        <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
          {fout}
        </p>
      )}
      <input type="hidden" name="kindId" value={kindId} />

      <div className="flex flex-wrap gap-3">
        <div className="space-y-1.5">
          <label htmlFor="datum" className="text-sm font-medium text-ink">
            Datum
          </label>
          <input
            id="datum"
            name="datum"
            type="date"
            defaultValue={vandaag}
            className={veld}
          />
        </div>
        <div className="flex-1 space-y-1.5">
          <label htmlFor="soort" className="text-sm font-medium text-ink">
            Soort
          </label>
          <select
            id="soort"
            name="soort"
            className={veld}
            defaultValue="opmerking"
          >
            {t.soorten.map((s) => (
              <option key={s.waarde} value={s.waarde}>
                {s.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="tekst" className="text-sm font-medium text-ink">
          Wat wil je noteren?
        </label>
        <textarea id="tekst" name="tekst" rows={3} required className={veld} />
      </div>

      <button
        type="submit"
        disabled={bezig}
        className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white transition hover:bg-forest-dark disabled:opacity-60"
      >
        {bezig ? "Bezig…" : "Opmerking bewaren"}
      </button>
    </form>
  );
}
