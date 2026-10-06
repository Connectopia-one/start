"use client";

import { useState, type FormEvent } from "react";
import { briefjeOphangen } from "@/app/prikbord/acties";
import { verzenden } from "@/content/formulier";
import { prikbord } from "@/content/prikbord";
import { mailtoUitFormulier } from "@/lib/mailversturen";

/*
  Het formulier waarmee iemand een briefje op het prikbord hangt.

  Staat de databank klaar, dan hangt het briefje er meteen. Staat ze nog
  niet klaar (de sleutels ontbreken), dan valt het formulier terug op een
  mail naar ons, zodat de pagina nooit stuk is.

  De teksten staan in content/prikbord.ts bij "formulier".
*/

const veld =
  "mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[16px] text-ink outline-none focus:border-green";

export function Briefjeformulier({
  bord,
  bordNaam,
  metWanneer = false,
  viaDatabank,
  keuze,
  terug,
}: {
  /* De slug van het bord, bv. "zoekertjes". Bij een keuzelijst het eerste. */
  bord: string;
  /* De naam zoals ze op het scherm staat, bv. "Zoekertjes". */
  bordNaam: string;
  /* Op het bord Samenkomen vragen we er ook naar wanneer iets doorgaat. */
  metWanneer?: boolean;
  /* Staat de databank klaar? Zo niet, dan gaat het briefje per mail. */
  viaDatabank: boolean;
  /*
    Op het overzicht kies je het bord in het formulier zelf, zodat je er
    niet eerst naartoe moet klikken. Op een bord zelf laat je dit weg.
  */
  keuze?: { slug: string; naam: string; ondertitel: string }[];
  /* Waar je na het ophangen weer terechtkomt. */
  terug?: string;
}) {
  const [gekozen, setGekozen] = useState(bord);
  const huidig = keuze?.find((b) => b.slug === gekozen);
  const naarNaam = keuze ? (huidig?.naam ?? bordNaam) : bordNaam;
  const toonWanneer = keuze ? gekozen === "samenkomen" : metWanneer;
  const perMail = !verzenden.webadres;
  /* Gaat het briefje niet naar de databank maar per mail, dan bouwen we die
     mail zelf op; zie lib/mailversturen.ts voor waarom. */
  const zelfMailen = !viaDatabank && perMail;

  function openMailprogramma(gebeurtenis: FormEvent<HTMLFormElement>) {
    gebeurtenis.preventDefault();
    window.location.href = mailtoUitFormulier(
      gebeurtenis.currentTarget,
      verzenden.mailnaar,
      `Prikbord: ${naarNaam}`
    );
  }

  return (
    <form
      action={
        viaDatabank ? briefjeOphangen : zelfMailen ? undefined : verzenden.webadres!
      }
      method={viaDatabank || zelfMailen ? undefined : "post"}
      onSubmit={zelfMailen ? openMailprogramma : undefined}
      className="grid gap-4"
    >
      {keuze ? null : (
        <input
          type="hidden"
          name="bord"
          value={viaDatabank ? bord : bordNaam}
        />
      )}
      {terug ? <input type="hidden" name="terug" value={terug} /> : null}

      {keuze ? (
        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {prikbord.formulier.bordLabel}
            <span className="text-orange" aria-hidden>
              {" "}
              *
            </span>
          </span>
          <select
            name={viaDatabank ? "bord" : "Bord"}
            value={viaDatabank ? gekozen : naarNaam}
            onChange={(e) =>
              setGekozen(
                viaDatabank
                  ? e.target.value
                  : (keuze.find((b) => b.naam === e.target.value)?.slug ?? bord)
              )
            }
            required
            className={veld}
          >
            {keuze.map((b) => (
              <option key={b.slug} value={viaDatabank ? b.slug : b.naam}>
                {b.naam}
              </option>
            ))}
          </select>
          {huidig ? (
            <span className="mt-1 block text-[14px] text-ink-dim">
              {huidig.ondertitel}
            </span>
          ) : null}
        </label>
      ) : null}

      {/* Een vakje dat alleen een robot invult. Blijft onzichtbaar. */}
      {viaDatabank ? (
        <div className="hidden" aria-hidden>
          <label>
            Laat dit veld leeg
            <input type="text" name="adres" tabIndex={-1} autoComplete="off" />
          </label>
        </div>
      ) : null}

      <label className="block">
        <span className="text-[15px] font-bold text-ink">
          {prikbord.formulier.briefjeLabel}
          <span className="text-orange" aria-hidden>
            {" "}
            *
          </span>
        </span>
        <textarea
          name={viaDatabank ? "tekst" : "Briefje"}
          rows={4}
          maxLength={600}
          required
          className={veld}
        />
      </label>

      {toonWanneer ? (
        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {prikbord.formulier.wanneerLabel}
          </span>
          <input
            type="text"
            name={viaDatabank ? "wanneer" : "Wanneer"}
            maxLength={120}
            placeholder="Woensdag 8 oktober, 20u, online"
            className={veld}
          />
        </label>
      ) : null}

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {prikbord.formulier.voornaamLabel}
            <span className="text-orange" aria-hidden>
              {" "}
              *
            </span>
          </span>
          <input
            type="text"
            name={viaDatabank ? "naam" : "Voornaam op het briefje"}
            maxLength={60}
            required
            className={veld}
          />
          <span className="mt-1 block text-[14px] text-ink-dim">
            {prikbord.formulier.voornaamUitleg}
          </span>
        </label>

        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {prikbord.formulier.volledigeNaamLabel}
            <span className="text-orange" aria-hidden>
              {" "}
              *
            </span>
          </span>
          <input
            type="text"
            name={viaDatabank ? "volledigeNaam" : "Volledige naam (voor ons)"}
            maxLength={120}
            required
            className={veld}
          />
          <span className="mt-1 block text-[14px] text-ink-dim">
            {prikbord.formulier.volledigeNaamUitleg}
          </span>
        </label>
      </div>

      <label className="block">
        <span className="text-[15px] font-bold text-ink">
          {prikbord.formulier.mailLabel}
          <span className="text-orange" aria-hidden>
            {" "}
            *
          </span>
        </span>
        <input
          type="email"
          name={viaDatabank ? "contact" : "E-mailadres (voor ons)"}
          maxLength={120}
          required
          className={`${veld} sm:max-w-sm`}
        />
      </label>

      <p className="text-[14.5px] text-ink-dim">{prikbord.formulier.privacy}</p>

      <div>
        <button
          type="submit"
          className="rounded-full bg-green px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
        >
          {prikbord.formulier.knopTekst} →
        </button>
      </div>
    </form>
  );
}
