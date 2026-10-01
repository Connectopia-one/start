import { postInsturen } from "@/app/in-de-kijker/acties";
import { inkijker, kanalen } from "@/content/inkijker";

/*
  Het formulier waarmee iemand van buiten zijn bericht instuurt.

  Er zit geen javascript aan vast: het is een gewoon formulier dat naar de
  server gaat. Het ingestuurde bericht staat nog niet op de site; dat
  gebeurt pas als het in het ouderportaal goedgekeurd wordt.

  De teksten staan in content/inkijker.ts bij "formulier".
*/

const veld =
  "mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[16px] text-ink outline-none focus:border-green";

function Sterretje() {
  return (
    <span className="text-orange" aria-hidden>
      {" "}
      *
    </span>
  );
}

export function Postformulier() {
  const t = inkijker.formulier;

  return (
    <form action={postInsturen} className="grid gap-4">
      {/* Een vakje dat alleen een robot invult. Blijft onzichtbaar. */}
      <div className="hidden" aria-hidden>
        <label>
          Laat dit veld leeg
          <input type="text" name="adres" tabIndex={-1} autoComplete="off" />
        </label>
      </div>

      <label className="block">
        <span className="text-[15px] font-bold text-ink">
          {t.linkLabel}
          <Sterretje />
        </span>
        <input
          type="url"
          name="link"
          maxLength={400}
          required
          placeholder="https://"
          className={veld}
        />
        <span className="mt-1 block text-[14px] text-ink-dim">
          {t.linkUitleg}
        </span>
      </label>

      <label className="block">
        <span className="text-[15px] font-bold text-ink">
          {t.tekstLabel}
          <Sterretje />
        </span>
        <textarea
          name="tekst"
          rows={4}
          maxLength={600}
          required
          className={veld}
        />
        <span className="mt-1 block text-[14px] text-ink-dim">
          {t.tekstUitleg}
        </span>
      </label>

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {t.vanLabel}
            <Sterretje />
          </span>
          <input
            type="text"
            name="van"
            maxLength={80}
            required
            className={veld}
          />
          <span className="mt-1 block text-[14px] text-ink-dim">
            {t.vanUitleg}
          </span>
        </label>

        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {t.kanaalLabel}
          </span>
          <select name="kanaal" defaultValue="facebook" className={veld}>
            {Object.entries(kanalen).map(([sleutel, naam]) => (
              <option key={sleutel} value={sleutel}>
                {naam}
              </option>
            ))}
          </select>
        </label>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-[15px] font-bold text-ink">
            {t.naamLabel}
            <Sterretje />
          </span>
          <input
            type="text"
            name="volledigeNaam"
            maxLength={120}
            required
            className={veld}
          />
          <span className="mt-1 block text-[14px] text-ink-dim">
            {t.naamUitleg}
          </span>
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
            className={veld}
          />
          <span className="mt-1 block text-[14px] text-ink-dim">
            {t.mailUitleg}
          </span>
        </label>
      </div>

      <p className="text-[14.5px] text-ink-dim">{t.privacy}</p>

      <div>
        <button
          type="submit"
          className="rounded-full bg-green px-6 py-3 text-[16px] font-extrabold text-cream transition hover:-translate-y-0.5"
        >
          {t.knopTekst} →
        </button>
      </div>
    </form>
  );
}
