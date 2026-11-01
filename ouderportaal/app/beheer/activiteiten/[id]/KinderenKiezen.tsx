"use client";

import { useMemo, useState } from "react";
import { lijstZin } from "@/lib/kind";

/*
  Kinderen die al in het ouderportaal staan op deze lijst zetten.

  Kim op 1 november 2026: "kan ik als ik kinderen toevoeg aan een traject of
  kamp gewoon klikken op de gegevens om zo een kind te selecteren? van de
  kinderen die er al instaan? want de kinderen van de plusklas gaan ook komen
  naar kamp."

  Daarom geen keuzelijstje met één kind per keer, maar een lijst om aan te
  klikken: zoeken op naam of gezin, meerdere kinderen tegelijk, en in één klik
  alle kinderen van een andere lijst (de plusklas, een vorige kampdag)
  aanvinken. De fiche hoeft niet opnieuw ingevuld te worden: die hangt aan het
  kind, niet aan de activiteit.

  Een kind waarvan de fiche nog niet in orde is, kan gewoon gekozen worden; we
  zeggen er enkel bij wat er nog ontbreekt.
*/

export type KiesKind = {
  id: string;
  naam: string;
  leeftijd: number | null;
  gezin: string | null;
  ontbreekt: string[];
};

export type AndereLijst = {
  id: string;
  naam: string;
  kinderen: string[];
};

export function KinderenKiezen({
  activiteitId,
  kinderen,
  andereLijsten,
  actie,
}: {
  activiteitId: string;
  kinderen: KiesKind[];
  andereLijsten: AndereLijst[];
  actie: (formData: FormData) => void | Promise<void>;
}) {
  const [zoek, setZoek] = useState("");
  const [gekozen, setGekozen] = useState<Set<string>>(new Set());

  const kanKiezen = useMemo(
    () => new Set(kinderen.map((k) => k.id)),
    [kinderen],
  );

  const zichtbaar = useMemo(() => {
    const woord = zoek.trim().toLowerCase();
    if (!woord) return kinderen;
    return kinderen.filter(
      (k) =>
        k.naam.toLowerCase().includes(woord) ||
        (k.gezin ?? "").toLowerCase().includes(woord),
    );
  }, [kinderen, zoek]);

  /* Enkel lijsten waar nog iemand op staat die hier nog niet staat. */
  const lijsten = andereLijsten
    .map((l) => ({ ...l, nieuw: l.kinderen.filter((id) => kanKiezen.has(id)) }))
    .filter((l) => l.nieuw.length > 0);

  function wissel(id: string) {
    setGekozen((oud) => {
      const nieuw = new Set(oud);
      if (nieuw.has(id)) nieuw.delete(id);
      else nieuw.add(id);
      return nieuw;
    });
  }

  function vinkLijstAan(id: string) {
    const lijst = lijsten.find((l) => l.id === id);
    if (!lijst) return;
    setGekozen((oud) => new Set([...oud, ...lijst.nieuw]));
  }

  return (
    <form
      action={actie}
      className="mt-2"
    >
      <input type="hidden" name="activiteit_id" value={activiteitId} />
      {[...gekozen].map((id) => (
        <input key={id} type="hidden" name="kind_id" value={id} />
      ))}

      <p className="text-xs text-ink-dim">
        Klik de kinderen aan die al in het ouderportaal staan. Hun fiche komt
        vanzelf mee; die moet niet opnieuw ingevuld worden.
      </p>

      <div className="mt-3 flex flex-wrap items-end gap-2">
        <label className="min-w-[12rem] flex-1">
          <span className="text-xs text-ink-dim">Zoek op naam of gezin</span>
          <input
            type="search"
            value={zoek}
            onChange={(e) => setZoek(e.target.value)}
            placeholder="bijvoorbeeld: Elena"
            className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-1.5 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
          />
        </label>
        {lijsten.length > 0 && (
          <label className="min-w-[12rem] flex-1">
            <span className="text-xs text-ink-dim">
              Of vink in één keer alle kinderen aan van
            </span>
            <select
              value=""
              onChange={(e) => vinkLijstAan(e.target.value)}
              className="mt-1 w-full rounded-md border border-border bg-paper px-3 py-1.5 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
            >
              <option value="">Kies een andere lijst</option>
              {lijsten.map((l) => (
                <option key={l.id} value={l.id}>
                  {l.naam} ({l.nieuw.length}{" "}
                  {l.nieuw.length === 1 ? "kind" : "kinderen"})
                </option>
              ))}
            </select>
          </label>
        )}
      </div>

      <ul className="mt-3 max-h-80 divide-y divide-border/60 overflow-y-auto rounded-md border border-border bg-paper">
        {zichtbaar.map((kind) => {
          const aan = gekozen.has(kind.id);
          return (
            <li key={kind.id}>
              <label
                className={`flex cursor-pointer items-start gap-3 px-3 py-2 text-sm transition ${
                  aan ? "bg-forest/10" : "hover:bg-forest/5"
                }`}
              >
                <input
                  type="checkbox"
                  checked={aan}
                  onChange={() => wissel(kind.id)}
                  className="mt-0.5 h-4 w-4 accent-forest"
                />
                <span className="flex-1">
                  <span className="font-medium text-ink">{kind.naam}</span>
                  {kind.leeftijd !== null && (
                    <span className="ml-1.5 text-xs text-ink-dim">
                      {kind.leeftijd} jaar
                    </span>
                  )}
                  {kind.gezin && (
                    <span className="block text-xs text-ink-dim">
                      gezin {kind.gezin}
                    </span>
                  )}
                </span>
                {kind.ontbreekt.length === 0 ? (
                  <span className="shrink-0 rounded-full bg-forest/10 px-2 py-0.5 text-xs font-medium text-forest-dark">
                    Fiche in orde
                  </span>
                ) : (
                  <span className="max-w-[45%] shrink-0 rounded-md bg-amber/15 px-2 py-0.5 text-right text-xs font-medium text-ink">
                    Fiche nog niet in orde: {lijstZin(kind.ontbreekt)}
                  </span>
                )}
              </label>
            </li>
          );
        })}
        {zichtbaar.length === 0 && (
          <li className="px-3 py-3 text-sm text-ink-dim">
            Geen kind gevonden met &ldquo;{zoek}&rdquo;. Staat het nog niet in
            het ouderportaal, voeg het dan eerst toe bij Gezinnen.
          </li>
        )}
      </ul>

      <div className="mt-3 flex flex-wrap items-center gap-3">
        <button
          type="submit"
          disabled={gekozen.size === 0}
          className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:cursor-not-allowed disabled:opacity-50"
        >
          {gekozen.size === 0
            ? "Toevoegen"
            : `${gekozen.size} ${gekozen.size === 1 ? "kind" : "kinderen"} toevoegen`}
        </button>
        {gekozen.size > 0 && (
          <button
            type="button"
            onClick={() => setGekozen(new Set())}
            className="text-sm text-ink-dim underline underline-offset-2"
          >
            niets aanvinken
          </button>
        )}
      </div>
    </form>
  );
}
