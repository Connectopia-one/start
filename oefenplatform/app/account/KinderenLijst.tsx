"use client";

import { useRef, useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { maakKind, verwijderKind } from "./kinderen/actions";

type Kind = { id: string; naam: string };

export function KinderenLijst({ kinderen }: { kinderen: Kind[] }) {
  const router = useRouter();
  const formRef = useRef<HTMLFormElement>(null);
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);
  const [zekerId, setZekerId] = useState<string | null>(null);

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
          const antwoord = await maakKind(data);
          if (antwoord.fout) setFout(antwoord.fout);
          else formRef.current?.reset();
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
