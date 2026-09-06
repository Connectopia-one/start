"use client";

import { useState } from "react";

type Vraag = {
  id: string;
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean;
  uitleg: string | null;
  volgnummer: number;
};

type Status = { gecontroleerd: boolean; correct: boolean; gegevenAntwoord: string | number | boolean | null };

function isCorrect(vraag: Vraag, gegeven: string | number | boolean | null): boolean {
  if (gegeven === null) return false;
  if (vraag.type === "invultekst") {
    return String(gegeven).trim().toLowerCase() === String(vraag.antwoord).trim().toLowerCase();
  }
  return gegeven === vraag.antwoord;
}

function VraagKaart({
  vraag,
  status,
  onAntwoord,
  onControleer,
}: {
  vraag: Vraag;
  status: Status;
  onAntwoord: (v: string | number | boolean) => void;
  onControleer: () => void;
}) {
  const gegeven = status.gegevenAntwoord;

  return (
    <div className="rounded-xl border border-border bg-surface p-5">
      <p className="font-medium text-ink">{vraag.vraag}</p>

      {vraag.type === "meerkeuze" && (
        <div className="mt-3 space-y-2">
          {vraag.opties?.map((optie, i) => (
            <label
              key={i}
              className={`flex cursor-pointer items-center gap-2 rounded-md border px-3 py-2 text-sm ${
                gegeven === i ? "border-forest bg-forest/5" : "border-border"
              }`}
            >
              <input
                type="radio"
                name={vraag.id}
                checked={gegeven === i}
                disabled={status.gecontroleerd}
                onChange={() => onAntwoord(i)}
                className="accent-forest"
              />
              {optie}
            </label>
          ))}
        </div>
      )}

      {vraag.type === "waarofniet" && (
        <div className="mt-3 flex gap-2">
          {[true, false].map((optie) => (
            <button
              key={String(optie)}
              type="button"
              disabled={status.gecontroleerd}
              onClick={() => onAntwoord(optie)}
              className={`rounded-md border px-4 py-2 text-sm ${
                gegeven === optie ? "border-forest bg-forest/5 text-forest-dark" : "border-border text-ink"
              }`}
            >
              {optie ? "Waar" : "Niet waar"}
            </button>
          ))}
        </div>
      )}

      {vraag.type === "invultekst" && (
        <input
          type="text"
          disabled={status.gecontroleerd}
          value={typeof gegeven === "string" ? gegeven : ""}
          onChange={(e) => onAntwoord(e.target.value)}
          className="mt-3 w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          placeholder="Typ je antwoord..."
        />
      )}

      {!status.gecontroleerd ? (
        <button
          type="button"
          onClick={onControleer}
          disabled={gegeven === null || gegeven === ""}
          className="mt-4 rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark disabled:cursor-not-allowed disabled:opacity-40"
        >
          Controleer
        </button>
      ) : (
        <div
          className={`mt-4 rounded-md px-3 py-2 text-sm ${
            status.correct ? "bg-forest/10 text-forest-dark" : "bg-danger/10 text-danger"
          }`}
        >
          <p className="font-medium">{status.correct ? "Juist!" : "Niet helemaal juist."}</p>
          {vraag.uitleg && <p className="mt-1 text-ink">{vraag.uitleg}</p>}
        </div>
      )}
    </div>
  );
}

export function Quiz({ vragen }: { vragen: Vraag[] }) {
  const [statussen, setStatussen] = useState<Record<string, Status>>(() =>
    Object.fromEntries(vragen.map((v) => [v.id, { gecontroleerd: false, correct: false, gegevenAntwoord: null }]))
  );

  const aantalGecontroleerd = Object.values(statussen).filter((s) => s.gecontroleerd).length;
  const aantalCorrect = Object.values(statussen).filter((s) => s.correct).length;
  const klaar = vragen.length > 0 && aantalGecontroleerd === vragen.length;

  const opnieuw = () =>
    setStatussen(
      Object.fromEntries(vragen.map((v) => [v.id, { gecontroleerd: false, correct: false, gegevenAntwoord: null }]))
    );

  if (!vragen.length) {
    return <p className="mt-8 text-sm text-ink-dim">Er zijn nog geen vragen in dit hoofdstuk.</p>;
  }

  return (
    <div className="mt-8 space-y-4">
      {vragen.map((vraag) => (
        <VraagKaart
          key={vraag.id}
          vraag={vraag}
          status={statussen[vraag.id]}
          onAntwoord={(v) =>
            setStatussen((s) => ({ ...s, [vraag.id]: { ...s[vraag.id], gegevenAntwoord: v } }))
          }
          onControleer={() =>
            setStatussen((s) => ({
              ...s,
              [vraag.id]: { ...s[vraag.id], gecontroleerd: true, correct: isCorrect(vraag, s[vraag.id].gegevenAntwoord) },
            }))
          }
        />
      ))}

      {klaar && (
        <div className="rounded-xl border border-forest/30 bg-forest/10 px-5 py-4 text-center">
          <p className="font-display text-lg font-semibold text-forest-dark">
            Je scoorde {aantalCorrect} / {vragen.length}
          </p>
          <button
            type="button"
            onClick={opnieuw}
            className="mt-3 rounded-md border border-forest px-4 py-2 text-sm font-medium text-forest-dark transition hover:bg-forest/10"
          >
            Opnieuw proberen
          </button>
        </div>
      )}
    </div>
  );
}
