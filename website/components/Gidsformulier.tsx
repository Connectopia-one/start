import { organisatieAanbrengen } from "@/app/waar-kan-je-terecht/acties";
import { gidsTekst } from "@/content/gids";

/*
  Het formulier onderaan de gids, waarmee iemand een organisatie of zichzelf
  aanbrengt.

  Er zit geen javascript aan vast: het is een gewoon formulier dat naar de
  server gaat. De organisatie staat nog niet in de gids; dat gebeurt pas als
  ze in het ouderportaal goedgekeurd wordt.

  De teksten staan in content/gids.ts bij "formulier".
*/

const veld =
  "mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[16px] text-ink outline-none focus:border-purple";

function Sterretje() {
  return (
    <span className="text-orange" aria-hidden>
      {" "}
      *
    </span>
  );
}

export function Gidsformulier() {
  const t = gidsTekst.formulier;

  return (
    <form action={organisatieAanbrengen} className="grid gap-4">
      {/* Een vakje dat alleen een robot invult. Blijft onzichtbaar. */}
      <div className="hidden" aria-hidden>
        <label>
          Laat dit veld leeg
          <input type="text" name="adres" tabIndex={-1} autoComplete="off" />
        </label>
      </div>

      <fieldset>
        <legend className="text-[15px] font-bold text-ink">{t.wieLabel}</legend>
        <div className="mt-2 flex flex-wrap gap-x-6 gap-y-2">
          <label className="flex items-center gap-2 text-[16px] text-ink">
            <input type="radio" name="wie" value="zelf" defaultChecked />
            {t.wieZelf}
          </label>
          <label className="flex items-center gap-2 text-[16px] text-ink">
            <input type="radio" name="wie" value="iemand" />
            {t.wieIemand}
          </label>
        </div>
      </fieldset>

      <label className="block">
        <span className="text-[15px] font-bold text-ink">
          {t.naamLabel}
          <Sterretje />
        </span>
        <input
          type="text"
          name="naam"
          maxLength={120}
          required
          className={veld}
        />
      </label>

      <label className="block">
        <span className="text-[15px] font-bold text-ink">
          {t.omschrijvingLabel}
          <Sterretje />
        </span>
        <textarea
          name="omschrijving"
          rows={3}
          minLength={10}
          maxLength={400}
          required
          className={veld}
        />
        <span className="mt-1 block text-[14px] text-ink-dim">
          {t.omschrijvingUitleg}
        </span>
      </label>

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-[15px] font-bold text-ink">{t.regioLabel}</span>
          <input type="text" name="regio" maxLength={80} className={veld} />
          <span className="mt-1 block text-[14px] text-ink-dim">
            {t.regioUitleg}
          </span>
        </label>

        <label className="block">
          <span className="text-[15px] font-bold text-ink">{t.linkLabel}</span>
          <input
            type="text"
            name="link"
            maxLength={400}
            inputMode="url"
            placeholder="https://"
            className={veld}
          />
          <span className="mt-1 block text-[14px] text-ink-dim">
            {t.linkUitleg}
          </span>
        </label>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {t.jouwNaamLabel}
            <Sterretje />
          </span>
          <input
            type="text"
            name="volledigeNaam"
            maxLength={120}
            required
            autoComplete="name"
            className={veld}
          />
        </label>

        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {t.mailLabel}
            <Sterretje />
          </span>
          <input
            type="email"
            name="contact"
            maxLength={120}
            required
            autoComplete="email"
            className={veld}
          />
        </label>
      </div>

      <p className="text-[14.5px] text-ink-dim">{t.privacy}</p>

      <div>
        <button
          type="submit"
          className="rounded-full bg-purple px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
        >
          {t.knopTekst} →
        </button>
      </div>
    </form>
  );
}
