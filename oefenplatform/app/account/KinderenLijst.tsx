"use client";

import { useRef, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { maakKind, verwijderKind, zetVoortgangsbalk } from "./kinderen/actions";

type Kind = { id: string; naam: string; toonVoortgang: boolean };

export function KinderenLijst({ kinderen }: { kinderen: Kind[] }) {
  const router = useRouter();
  const formRef = useRef<HTMLFormElement>(null);
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);
  // Geen fout maar een goed bericht: bijvoorbeeld wanneer iemand zijn
  // toegangscode in het naamveld tikte en we ze meteen gebruikt hebben.
  const [melding, setMelding] = useState<string | null>(null);
  const [zekerId, setZekerId] = useState<string | null>(null);

  /*
    De voortgangsbalk bij de oefeningen staat per kind. Gemeld door een ouder
    op 29 september 2026: haar ene kind was blij dat er geen balk staat en
    blokkeerde zodra het zag hoeveel vragen er waren, haar andere kind was net
    gefrustreerd omdat het graag weet hoe ver het al is.

    Het vinkje slaat meteen op. Wat je aanklikt blijft intussen staan, ook
    voor de server antwoordt; anders springt het vinkje terug en lijkt het
    alsof er niets gebeurd is.
  */
  const [balken, setBalken] = useState<Record<string, boolean>>({});
  const balkAan = (k: Kind) => balken[k.id] ?? k.toonVoortgang;

  async function zetBalk(kind: Kind, aan: boolean) {
    setBalken((b) => ({ ...b, [kind.id]: aan }));
    setFout(null);
    const data = new FormData();
    data.set("kind_id", kind.id);
    data.set("aan", aan ? "ja" : "nee");
    const antwoord = await zetVoortgangsbalk(data);
    if (antwoord.fout) {
      setFout(antwoord.fout);
      setBalken((b) => ({ ...b, [kind.id]: !aan }));
      return;
    }
    router.refresh();
  }

  async function wis(kindId: string) {
    setBezig(true);
    setFout(null);
    const data = new FormData();
    data.set("kind_id", kindId);
    const antwoord = await verwijderKind(data);
    if (antwoord.fout) setFout(antwoord.fout);
    setZekerId(null);
    setBezig(false);
    router.refresh();
  }

  return (
    <>
      {fout && (
        <p className="mt-4 rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
          {fout}
        </p>
      )}
      {melding && (
        <p className="mt-4 rounded-md bg-forest/10 px-3 py-2 text-sm text-forest-dark">
          {melding}
        </p>
      )}

      <ul className="mt-4 space-y-2">
        {kinderen.map((k) => (
          <li
            key={k.id}
            className="rounded-lg border border-border px-3 py-2 text-sm"
          >
            <div className="flex flex-wrap items-center justify-between gap-2">
              <span className="text-ink">{k.naam}</span>
              <div className="flex items-center gap-3">
                <Link
                  href={`/account/kinderen/${k.id}`}
                  className="text-forest-dark hover:underline"
                >
                  Voortgang bekijken &rarr;
                </Link>
                <button
                  type="button"
                  onClick={() => setZekerId(zekerId === k.id ? null : k.id)}
                  className="text-ink-dim hover:text-danger"
                >
                  Verwijderen
                </button>
              </div>
            </div>

            <label className="mt-2 flex items-start gap-2 text-sm text-ink-dim">
              <input
                type="checkbox"
                checked={balkAan(k)}
                onChange={(e) => zetBalk(k, e.target.checked)}
                className="mt-0.5 h-4 w-4 shrink-0 rounded border-border text-forest focus:ring-forest"
              />
              <span>
                Toon een voortgangsbalk bij de oefeningen
                <span className="block text-xs">
                  Dan ziet {k.naam} hoeveel vragen er zijn en hoeveel er al
                  nagekeken zijn. Sommige kinderen hebben daar rust bij, andere
                  net niet.
                </span>
              </span>
            </label>

            {zekerId === k.id && (
              <div className="mt-2 rounded-md bg-danger/10 px-3 py-2 text-sm">
                <p className="text-ink">
                  {k.naam} verwijderen? Ook de opgeloste vragen, de sterren en
                  de badges van {k.naam} gaan dan weg. Dat kan niet meer
                  teruggedraaid worden.
                </p>
                <div className="mt-2 flex gap-3">
                  <button
                    type="button"
                    disabled={bezig}
                    onClick={() => wis(k.id)}
                    className="rounded-md bg-danger px-3 py-1.5 text-sm font-medium text-white disabled:opacity-60"
                  >
                    {bezig ? "Bezig…" : "Ja, verwijderen"}
                  </button>
                  <button
                    type="button"
                    onClick={() => setZekerId(null)}
                    className="text-sm text-ink-dim hover:text-ink"
                  >
                    Nee, toch niet
                  </button>
                </div>
              </div>
            )}
          </li>
        ))}
        {!kinderen.length && (
          <li className="text-sm text-ink-dim">
            Nog geen kinderen toegevoegd.
          </li>
        )}
      </ul>

      <form
        ref={formRef}
        action={async (data) => {
          if (bezig) return;
          setBezig(true);
          setFout(null);
          setMelding(null);
          const antwoord = await maakKind(data);
          if (antwoord.fout) setFout(antwoord.fout);
          else formRef.current?.reset();
          if (antwoord.melding) setMelding(antwoord.melding);
          setBezig(false);
          router.refresh();
        }}
        className="mt-4 flex gap-2"
      >
        <input
          name="naam"
          required
          placeholder="Naam van je kind"
          className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest"
        />
        <button
          type="submit"
          disabled={bezig}
          className="shrink-0 rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:cursor-not-allowed disabled:opacity-60"
        >
          {bezig ? "Bezig…" : "Toevoegen"}
        </button>
      </form>
    </>
  );
}
