"use client";

import { useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import { maakWebgeschikt } from "@/lib/beeldOmzetten";
import { maakLogoUploadUrl, zetLogo } from "./actions";

/*
  Een logo opladen bij een organisatie in de gids, of het vervangen of
  weghalen. Het bestand gaat rechtstreeks naar Supabase Storage, niet langs
  de server, net als bij In de kijker. Zie maakLogoUploadUrl in actions.ts.
*/
export function LogoForm({
  id,
  logoAdres,
}: {
  id: string;
  /* Het volledige webadres van het huidige logo, of null. */
  logoAdres: string | null;
}) {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);

    const form = e.currentTarget;
    const gekozen = new FormData(form).get("logo");
    if (!(gekozen instanceof File) || gekozen.size === 0) {
      setBezig(false);
      setFout("Kies eerst een logo.");
      return;
    }

    try {
      const bestand = await maakWebgeschikt(gekozen);
      const plek = await maakLogoUploadUrl(bestand.name);
      if (!plek.gelukt) throw new Error(plek.bericht);

      const { error } = await createClient()
        .storage.from("social")
        .uploadToSignedUrl(plek.pad, plek.token, bestand);
      if (error) throw new Error(`Het logo opladen mislukte: ${error.message}`);

      const antwoord = await zetLogo({ id, logo: plek.pad });
      if (!antwoord.gelukt) throw new Error(antwoord.bericht);

      form.reset();
      router.refresh();
    } catch (err) {
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    } finally {
      setBezig(false);
    }
  }

  async function haalWeg() {
    setBezig(true);
    setFout(null);
    const antwoord = await zetLogo({ id, logo: null });
    if (!antwoord.gelukt) setFout(antwoord.bericht);
    setBezig(false);
    router.refresh();
  }

  return (
    <form onSubmit={onSubmit} className="mt-3 space-y-2">
      <p className="text-sm font-medium text-ink">Logo</p>
      {logoAdres ? (
        // eslint-disable-next-line @next/next/no-img-element
        <img
          src={logoAdres}
          alt="Het logo dat nu in de gids staat"
          className="max-h-14 w-auto max-w-[60%] object-contain"
        />
      ) : (
        <p className="text-sm text-ink-dim">
          Nog geen logo. Dan staat hun naam in het vakje, in het
          handschriftlettertype.
        </p>
      )}
      {fout && <p className="text-sm text-danger">{fout}</p>}
      <div className="flex flex-wrap items-center gap-2">
        <input
          name="logo"
          type="file"
          accept="image/*,.heic,.heif"
          aria-label={logoAdres ? "Ander logo kiezen" : "Een logo kiezen"}
          className="text-sm"
        />
        <button
          type="submit"
          disabled={bezig}
          className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark disabled:opacity-60"
        >
          {bezig ? "Bezig…" : logoAdres ? "Logo vervangen" : "Logo toevoegen"}
        </button>
        {logoAdres && (
          <button
            type="button"
            onClick={haalWeg}
            disabled={bezig}
            className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-danger hover:text-danger disabled:opacity-60"
          >
            Logo weghalen
          </button>
        )}
      </div>
    </form>
  );
}
