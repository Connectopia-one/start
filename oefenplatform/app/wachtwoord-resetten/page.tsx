"use client";

import { useEffect, useState, type FormEvent } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";

export default function WachtwoordResettenPage() {
  const router = useRouter();
  const [klaarOmTeControleren, setKlaarOmTeControleren] = useState(false);
  const [heeftSessie, setHeeftSessie] = useState(false);
  const [status, setStatus] = useState<"idle" | "bezig" | "gelukt" | "fout">("idle");
  const [fout, setFout] = useState<string | null>(null);

  useEffect(() => {
    const supabase = createClient();
    // De reset-link van Supabase zet de sessie automatisch via de URL — even
    // controleren of dat gelukt is vóór we het formulier tonen.
    supabase.auth.getSession().then(({ data }) => {
      setHeeftSessie(!!data.session);
      setKlaarOmTeControleren(true);
    });
  }, []);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setStatus("bezig");
    setFout(null);

    const data = new FormData(e.currentTarget);
    const wachtwoord = String(data.get("wachtwoord") || "");
    const bevestig = String(data.get("bevestig") || "");

    if (wachtwoord.length < 8) {
      setStatus("fout");
      setFout("Kies een wachtwoord van minstens 8 tekens.");
      return;
    }
    if (wachtwoord !== bevestig) {
      setStatus("fout");
      setFout("De wachtwoorden komen niet overeen.");
      return;
    }

    const supabase = createClient();
    const { error } = await supabase.auth.updateUser({ password: wachtwoord });
    if (error) {
      setStatus("fout");
      setFout(error.message);
      return;
    }

    setStatus("gelukt");
    setTimeout(() => router.push("/account"), 1500);
  }

  return (
    <main className="flex flex-1 items-center justify-center bg-paper px-6 py-16">
      <div className="w-full max-w-sm">
        <p className="mb-1 text-sm font-medium uppercase tracking-wide text-forest">
          Connectopia
        </p>
        <h1 className="font-display text-2xl font-semibold text-ink">Nieuw wachtwoord instellen</h1>

        {!klaarOmTeControleren ? (
          <p className="mt-8 text-sm text-ink-dim">Even controleren...</p>
        ) : !heeftSessie ? (
          <div className="mt-8 rounded-xl border border-border bg-surface p-6 text-sm text-ink">
            <p>Deze link is niet (meer) geldig of is verlopen.</p>
            <Link
              href="/wachtwoord-vergeten"
              className="mt-4 inline-block text-forest-dark underline-offset-2 hover:underline"
            >
              Nieuwe reset-link aanvragen
            </Link>
          </div>
        ) : status === "gelukt" ? (
          <p className="mt-8 rounded-xl border border-border bg-forest/10 p-6 text-sm text-forest-dark">
            Je wachtwoord is aangepast. Je wordt zo doorgestuurd...
          </p>
        ) : (
          <form onSubmit={onSubmit} className="mt-8 space-y-4 rounded-xl border border-border bg-surface p-6">
            {fout && <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">{fout}</p>}
            <div className="space-y-1.5">
              <label htmlFor="wachtwoord" className="text-sm font-medium text-ink">
                Nieuw wachtwoord
              </label>
              <input
                id="wachtwoord"
                name="wachtwoord"
                type="password"
                required
                minLength={8}
                autoComplete="new-password"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <div className="space-y-1.5">
              <label htmlFor="bevestig" className="text-sm font-medium text-ink">
                Bevestig wachtwoord
              </label>
              <input
                id="bevestig"
                name="bevestig"
                type="password"
                required
                minLength={8}
                autoComplete="new-password"
                className="w-full rounded-md border border-border bg-paper px-3 py-2 text-sm text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest"
              />
            </div>
            <button
              type="submit"
              disabled={status === "bezig"}
              className="w-full rounded-md bg-forest px-4 py-2 text-sm font-medium text-white transition hover:bg-forest-dark disabled:opacity-60"
            >
              {status === "bezig" ? "Bezig..." : "Wachtwoord instellen"}
            </button>
          </form>
        )}
      </div>
    </main>
  );
}
