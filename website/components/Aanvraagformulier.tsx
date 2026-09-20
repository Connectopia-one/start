import type { ReactNode } from "react";
import { formulierTekst, velden, verzenden } from "@/content/formulier";

/*
  Het formulier dat op twee plaatsen gebruikt wordt: bij het aanbod
  (info vragen, inschrijven, proefles) en op de contactpagina om
  teruggebeld te worden.

  De vragen staan in content/formulier.ts, net als de plek waar een
  ingevuld formulier naartoe gaat. Hier staat alleen hoe het eruitziet.
*/
export function Aanvraagformulier({
  onderwerp,
  kop,
  verborgen = [],
  optioneel = [],
}: {
  /* Wat er in de onderwerpregel van de mail komt te staan. */
  onderwerp: string;
  /* Het gekleurde blok bovenaan, dat zegt waar de aanvraag over gaat. */
  kop?: ReactNode;
  /* Extra gegevens die meegestuurd worden zonder dat de ouder ze ziet. */
  verborgen?: { naam: string; waarde: string }[];
  /*
    Vragen die op deze plek niet verplicht zijn. Zet hier de "naam" van een
    vraag uit content/formulier.ts in. Op de contactpagina hoeft een ouder
    bijvoorbeeld de naam van het kind niet in te vullen.
  */
  optioneel?: string[];
}) {
  /*
    Zolang er geen formulierdienst is ingesteld, opent het formulier het
    mailprogramma van de ouder met alle antwoorden er al in.
  */
  const perMail = !verzenden.webadres;
  const actie = perMail
    ? `mailto:${verzenden.mailnaar}?subject=${encodeURIComponent(onderwerp)}`
    : verzenden.webadres!;

  return (
    <form
      action={actie}
      method="post"
      encType={perMail ? "text/plain" : undefined}
      className="grid gap-5"
    >
      {kop}
      {verborgen.map((veld) => (
        <input key={veld.naam} type="hidden" name={veld.naam} value={veld.waarde} />
      ))}

      <div className="grid gap-5 sm:grid-cols-2">
        {velden.map((veld) => {
          const lang = veld.soort === "lang";
          const verplicht = veld.verplicht && !optioneel.includes(veld.naam);
          const type =
            veld.soort === "email" ? "email" : veld.soort === "telefoon" ? "tel" : "text";
          return (
            <div key={veld.naam} className={lang ? "sm:col-span-2" : undefined}>
              <label className="block">
                <span className="text-[14px] font-bold text-ink">
                  {veld.label}
                  {verplicht ? (
                    <span className="text-orange" aria-hidden>
                      {" "}
                      *
                    </span>
                  ) : null}
                </span>
                {lang ? (
                  <textarea
                    name={veld.naam}
                    rows={4}
                    required={verplicht}
                    className="mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[15px] text-ink outline-none focus:border-green"
                  />
                ) : (
                  <input
                    type={type}
                    name={veld.naam}
                    required={verplicht}
                    autoComplete={
                      veld.soort === "email" ? "email" : veld.soort === "telefoon" ? "tel" : undefined
                    }
                    className="mt-1.5 block h-11 w-full rounded-full border border-border bg-cream px-4 text-[15px] text-ink outline-none focus:border-green"
                  />
                )}
              </label>
              {veld.hulp ? <p className="mt-1 text-[13px] text-ink-dim">{veld.hulp}</p> : null}
            </div>
          );
        })}
      </div>

      {/* Wat er met de gegevens gebeurt. */}
      <div className="rounded-[16px] bg-purple-soft px-5 py-4">
        <p className="text-[14px] text-ink">{formulierTekst.privacy}</p>
        <label className="mt-3 flex items-start gap-2.5 text-[14px] font-bold text-ink">
          <input
            type="checkbox"
            name="Akkoord met het gebruik van de gegevens"
            value="ja"
            required
            className="mt-0.5 h-[18px] w-[18px] shrink-0 accent-green"
          />
          {formulierTekst.akkoordTekst}
          <span className="text-orange" aria-hidden>
            *
          </span>
        </label>
      </div>

      <div>
        <button
          type="submit"
          className="rounded-full bg-green px-7 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5 hover:bg-green-mid"
        >
          {formulierTekst.verstuurKnop} →
        </button>
      </div>

      {perMail ? <p className="text-[13px] text-ink-dim">{formulierTekst.naVersturen}</p> : null}
    </form>
  );
}
