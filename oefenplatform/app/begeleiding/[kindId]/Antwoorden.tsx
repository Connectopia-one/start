import { schrijfKeuzes } from "@/lib/antwoord";
import { VraagTekst } from "@/components/Figuren";

/*
  De vragen van één hoofdstuk met het antwoord dat het kind gaf. Bij een fout
  antwoord staat het juiste antwoord er meteen onder, want dat is net wat je
  op een oudercontact wil kunnen tonen.

  Let op bij het lezen van de code: de keuzes worden bij het OEFENEN door
  elkaar gehusseld (lib/optievolgorde.ts), maar in de databank staat het
  nummer van de oorspronkelijke volgorde. Daarom mag je hier gewoon
  vraag.opties[nummer] nemen.
*/

export type Vraag = {
  id: string;
  volgnummer: number;
  type: "meerkeuze" | "invultekst" | "waarofniet";
  vraag: string;
  opties: string[] | null;
  antwoord: number | string | boolean;
  uitleg: string | null;
};

export type Poging = {
  vraag_id: string;
  correct: boolean;
  gegeven_antwoord: number | string | boolean | number[] | null;
  beantwoord_op: string;
};

export function schrijfAntwoord(
  vraag: Vraag,
  waarde: number | string | boolean | number[] | null,
): string {
  if (waarde === null || waarde === undefined || waarde === "") return "—";
  if (vraag.type === "meerkeuze") return schrijfKeuzes(vraag.opties, waarde);
  if (vraag.type === "waarofniet")
    return waarde === true ? "Waar" : "Niet waar";
  return String(waarde);
}

export function Antwoorden({
  vragen,
  pogingen,
  kindNaam,
}: {
  vragen: Vraag[];
  /* Alle pogingen van dit kind, nieuwste eerst. */
  pogingen: Poging[];
  kindNaam: string;
}) {
  const laatste = new Map<string, Poging>();
  const aantalPogingen = new Map<string, number>();
  for (const p of pogingen) {
    if (!laatste.has(p.vraag_id)) laatste.set(p.vraag_id, p);
    aantalPogingen.set(p.vraag_id, (aantalPogingen.get(p.vraag_id) ?? 0) + 1);
  }

  if (vragen.length === 0) {
    return (
      <p className="text-sm text-ink-dim">
        Dit hoofdstuk heeft nog geen vragen.
      </p>
    );
  }

  return (
    <ol className="space-y-3">
      {vragen.map((vraag, i) => {
        const poging = laatste.get(vraag.id);
        const keer = aantalPogingen.get(vraag.id) ?? 0;
        return (
          <li
            key={vraag.id}
            className="break-inside-avoid rounded-xl border border-border bg-surface p-5"
          >
            <p className="text-xs font-medium text-ink-dim">Vraag {i + 1}</p>
            <div className="mt-1">
              <VraagTekst tekst={vraag.vraag} />
            </div>

            {!poging ? (
              <p className="mt-3 text-sm text-ink-dim">Nog niet geprobeerd.</p>
            ) : (
              <>
                <div
                  className={`mt-3 rounded-md px-3 py-2 text-sm ${
                    poging.correct
                      ? "bg-forest/10 text-forest-dark"
                      : "bg-danger/10 text-danger"
                  }`}
                >
                  {poging.correct ? "Juist" : "Fout"} — {kindNaam} antwoordde:{" "}
                  <strong>
                    {schrijfAntwoord(vraag, poging.gegeven_antwoord)}
                  </strong>
                </div>

                {!poging.correct && (
                  <p className="mt-2 text-sm text-ink-dim">
                    Het juiste antwoord was:{" "}
                    <strong className="text-ink">
                      {schrijfAntwoord(vraag, vraag.antwoord)}
                    </strong>
                  </p>
                )}

                {vraag.uitleg && (
                  <p className="mt-2 text-sm text-ink-dim">{vraag.uitleg}</p>
                )}

                <p className="mt-2 text-xs text-ink-dim">
                  {new Date(poging.beantwoord_op).toLocaleDateString("nl-BE", {
                    day: "numeric",
                    month: "long",
                    year: "numeric",
                  })}
                  {keer > 1
                    ? ` · ${keer} keer geprobeerd, dit was de laatste`
                    : ""}
                </p>
              </>
            )}
          </li>
        );
      })}
    </ol>
  );
}
