"use client";

import { useRef, useState, type FormEvent } from "react";
import { useRouter } from "next/navigation";
import { createClient } from "@/lib/supabase/client";
import {
  bewaarNieuwePost,
  haalLinkGegevens,
  maakBeeldUploadUrl,
  zetBeeld,
} from "./actions";

/*
  De twee formulieren van "In de kijker".

  Bij een nieuw bericht plak je alleen de link. Wij proberen dan zelf het
  kanaal, wie het postte, de titel, een stukje tekst en het beeld op te halen,
  zodat jij enkel nog nakijkt. Lukt dat niet, dan vul je het zelf aan; dat is
  geen fout, want Facebook en Instagram geven dit niet vrij.

  Wat jij zelf in een veld typt, overschrijven we nooit.

  Het beeld dat je zelf oplaadt gaat rechtstreeks naar Supabase Storage, niet
  door een server action heen: zo blijft het buiten de limiet van ongeveer
  4,5MB die Vercel op een gewoon verzoek zet. Dezelfde aanpak als bij de
  foto's van een klasje.
*/

const BAK = "social";

const KANALEN = [
  ["facebook", "Facebook"],
  ["instagram", "Instagram"],
  ["linkedin", "LinkedIn"],
  ["tiktok", "TikTok"],
  ["youtube", "YouTube"],
  ["anders", "Elders online"],
] as const;

const veld =
  "w-full rounded-md border border-border bg-paper px-3 py-2 text-sm outline-none focus:border-forest focus:ring-1 focus:ring-forest";

async function laadBeeldOp(bestand: File) {
  const { pad, token } = await maakBeeldUploadUrl(bestand.name);
  const supabase = createClient();
  const { error } = await supabase.storage
    .from(BAK)
    .uploadToSignedUrl(pad, token, bestand);
  if (error) throw new Error(`Het beeld opladen mislukte: ${error.message}`);
  return pad;
}

function eersteBestand(data: FormData, naam: string): File | null {
  const bestand = data.get(naam);
  return bestand instanceof File && bestand.size > 0 ? bestand : null;
}

export function NieuwePostForm() {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  /* De velden houden we zelf bij, zodat het ophalen ze kan invullen. */
  const [link, setLink] = useState("");
  const [tekst, setTekst] = useState("");
  const [van, setVan] = useState("Connectopia");
  const [kanaal, setKanaal] = useState("facebook");
  const [titel, setTitel] = useState("");

  /* Wat Kim met de hand aanpaste, laten we staan. */
  const metDeHand = useRef<Set<string>>(new Set());

  const [ophalen, setOphalen] = useState(false);
  const [gelezen, setGelezen] = useState<string | null>(null);
  /* Het beeld dat we bij de link vonden. Pas bij bewaren halen we het binnen. */
  const [beeldVanLink, setBeeldVanLink] = useState<string | null>(null);
  const [laatstGelezen, setLaatstGelezen] = useState("");

  function zetVeld(
    naam: string,
    waarde: string | null,
    huidig: string,
    zet: (w: string) => void,
  ) {
    if (!waarde) return;
    if (metDeHand.current.has(naam) && huidig.trim()) return;
    zet(waarde);
  }

  async function leesDeLink(adres: string) {
    const schoon = adres.trim();
    if (!schoon || schoon === laatstGelezen) return;

    setOphalen(true);
    setGelezen(null);
    setLaatstGelezen(schoon);
    try {
      const gevonden = await haalLinkGegevens(schoon);
      setKanaal(gevonden.kanaal);
      zetVeld("van", gevonden.van, van, setVan);
      zetVeld("titel", gevonden.titel, titel, setTitel);
      zetVeld("tekst", gevonden.tekst, tekst, setTekst);
      setBeeldVanLink(gevonden.beeldUrl);
      setGelezen(gevonden.bericht);
    } catch {
      setGelezen("Het ophalen lukte niet. Vul het zelf even aan.");
    } finally {
      setOphalen(false);
    }
  }

  function leeg() {
    setLink("");
    setTekst("");
    setVan("Connectopia");
    setKanaal("facebook");
    setTitel("");
    setBeeldVanLink(null);
    setGelezen(null);
    setLaatstGelezen("");
    metDeHand.current = new Set();
  }

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);

    const form = e.currentTarget;
    const data = new FormData(form);

    try {
      const bestand = eersteBestand(data, "beeld");
      const beeld = bestand ? await laadBeeldOp(bestand) : null;

      const antwoord = await bewaarNieuwePost({
        titel: titel || null,
        tekst,
        van,
        kanaal,
        link,
        eigen: data.get("eigen") === "ja",
        beeld,
        /* Zelf opgeladen gaat voor; anders nemen we het beeld van de link. */
        beeldVanLink: beeld ? null : beeldVanLink,
      });

      if (!antwoord.gelukt) {
        setBezig(false);
        setFout(antwoord.bericht);
        return;
      }

      form.reset();
      leeg();
      setBezig(false);
      router.refresh();
    } catch (err) {
      setBezig(false);
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-4 space-y-4">
      {fout && (
        <p className="rounded-md bg-danger/10 px-3 py-2 text-sm text-danger">
          {fout}
        </p>
      )}

      {/* De link staat apart in een kader: het is het enige dat echt moet. */}
      <div className="space-y-2 rounded-lg border-2 border-forest bg-forest/5 p-4">
        <label htmlFor="link" className="block text-sm font-medium text-ink">
          Plak hier de link van het bericht
        </label>
        <div className="flex flex-wrap items-center gap-2">
          <input
            id="link"
            name="link"
            type="url"
            required
            value={link}
            onChange={(e) => setLink(e.target.value)}
            onBlur={(e) => void leesDeLink(e.target.value)}
            placeholder="https://www.facebook.com/..."
            spellCheck={false}
            autoCorrect="off"
            autoCapitalize="off"
            autoComplete="off"
            className={`${veld} min-w-0 flex-1`}
          />
          <button
            type="button"
            onClick={() => {
              setLaatstGelezen("");
              void leesDeLink(link);
            }}
            disabled={ophalen || !link.trim()}
            className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
          >
            {ophalen ? "Bezig…" : "Ophalen"}
          </button>
        </div>
        <p className="text-xs text-ink-dim">
          Van Facebook, Instagram, TikTok, YouTube, LinkedIn of een gewone
          website. Het volledige adres, dus beginnend met https://
        </p>
        {gelezen && <p className="text-sm font-medium text-forest">{gelezen}</p>}
      </div>

      <div className="space-y-1.5">
        <label htmlFor="tekst" className="text-sm font-medium text-ink">
          Wat er op het kaartje komt
        </label>
        <textarea
          id="tekst"
          name="tekst"
          rows={3}
          required
          value={tekst}
          onChange={(e) => {
            metDeHand.current.add("tekst");
            setTekst(e.target.value);
          }}
          className={veld}
        />
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="space-y-1.5">
          <label htmlFor="van" className="text-sm font-medium text-ink">
            Van wie is het bericht?
          </label>
          <input
            id="van"
            name="van"
            required
            value={van}
            onChange={(e) => {
              metDeHand.current.add("van");
              setVan(e.target.value);
            }}
            className={veld}
          />
        </div>
        <div className="space-y-1.5">
          <label htmlFor="kanaal" className="text-sm font-medium text-ink">
            Waar staat het?
          </label>
          <select
            id="kanaal"
            name="kanaal"
            value={kanaal}
            onChange={(e) => setKanaal(e.target.value)}
            className={veld}
          >
            {KANALEN.map(([sleutel, naam]) => (
              <option key={sleutel} value={sleutel}>
                {naam}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="space-y-1.5">
        <label htmlFor="titel" className="text-sm font-medium text-ink">
          Kop boven het kaartje (mag leeg blijven)
        </label>
        <input
          id="titel"
          name="titel"
          value={titel}
          onChange={(e) => {
            metDeHand.current.add("titel");
            setTitel(e.target.value);
          }}
          className={veld}
        />
      </div>

      {beeldVanLink && (
        <div className="flex flex-wrap items-center gap-3 rounded-lg border border-border bg-paper p-3">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img
            src={beeldVanLink}
            alt="Het beeld dat bij deze link hoort"
            className="h-16 w-24 rounded-md object-cover"
          />
          <div className="min-w-0 flex-1 space-y-1">
            <p className="text-sm font-medium text-ink">
              Dit beeld vonden we bij de link.
            </p>
            <p className="text-xs text-ink-dim">
              Bij bewaren komt het op onze eigen server te staan, niet bij het
              kanaal zelf.
            </p>
          </div>
          <button
            type="button"
            onClick={() => setBeeldVanLink(null)}
            className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark"
          >
            Niet gebruiken
          </button>
        </div>
      )}

      <div className="space-y-1.5">
        <label htmlFor="beeld" className="text-sm font-medium text-ink">
          {beeldVanLink
            ? "Of laad zelf een ander beeld op"
            : "Een beeld erbij (mag leeg blijven)"}
        </label>
        <input
          id="beeld"
          name="beeld"
          type="file"
          accept="image/*"
          className="w-full text-sm"
        />
        <p className="text-xs text-ink-dim">
          Wat jij hier kiest, gaat voor op het beeld van de link. Zonder beeld
          is het kaartje gewoon tekst, met het teken van het kanaal erop.
        </p>
      </div>

      <label className="flex items-center gap-2 text-sm text-ink">
        <input
          type="checkbox"
          name="eigen"
          value="ja"
          defaultChecked
          className="h-4 w-4 rounded border-border"
        />
        Dit is een bericht van onszelf
      </label>

      <button
        type="submit"
        disabled={bezig}
        className="rounded-md bg-forest px-4 py-2 text-sm font-medium text-white hover:bg-forest-dark disabled:opacity-60"
      >
        {bezig ? "Bezig…" : "Op de website zetten"}
      </button>
    </form>
  );
}

/* Een beeld bij een bericht dat er al staat, of een beeld vervangen. */
export function BeeldForm({
  id,
  heeftBeeld,
}: {
  id: string;
  heeftBeeld: boolean;
}) {
  const router = useRouter();
  const [bezig, setBezig] = useState(false);
  const [fout, setFout] = useState<string | null>(null);

  async function onSubmit(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBezig(true);
    setFout(null);

    const form = e.currentTarget;
    const bestand = eersteBestand(new FormData(form), "beeld");
    if (!bestand) {
      setBezig(false);
      setFout("Kies eerst een beeld.");
      return;
    }

    try {
      const beeld = await laadBeeldOp(bestand);
      await zetBeeld({ id, beeld });
      form.reset();
      setBezig(false);
      router.refresh();
    } catch (err) {
      setBezig(false);
      setFout(err instanceof Error ? err.message : "Er ging iets mis.");
    }
  }

  return (
    <form onSubmit={onSubmit} className="mt-3 space-y-2">
      {fout && <p className="text-sm text-danger">{fout}</p>}
      <div className="flex flex-wrap items-center gap-2">
        <input
          name="beeld"
          type="file"
          accept="image/*"
          aria-label={heeftBeeld ? "Ander beeld kiezen" : "Een beeld kiezen"}
          className="text-sm"
        />
        <button
          type="submit"
          disabled={bezig}
          className="rounded-md border border-border px-3 py-1.5 text-sm text-ink-dim hover:border-forest hover:text-forest-dark disabled:opacity-60"
        >
          {bezig
            ? "Bezig…"
            : heeftBeeld
              ? "Beeld vervangen"
              : "Beeld toevoegen"}
        </button>
      </div>
    </form>
  );
}
