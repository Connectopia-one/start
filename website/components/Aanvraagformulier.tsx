import type { ReactNode } from "react";
import type { Veld } from "@/content/formulier";
import { formulierTekst, velden } from "@/content/formulier";
import { aanvraagVersturen } from "@/app/acties";
import { Verstuurknop } from "@/components/Verstuurknop";

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
  vragen = velden,
  privacy = formulierTekst.privacy,
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
  /*
    Andere vragen dan de gewone, voor een formulier dat iets anders vraagt,
    zoals de inschrijving voor de winactie (content/winactie.ts).
  */
  vragen?: Veld[];
  /*
    Een eigen zin over wat er met de gegevens gebeurt. De standaardzin uit
    content/formulier.ts gaat over de deelname van een kind, en die klopt
    niet op elke pagina.
  */
  privacy?: string;
}) {
  /*
    Een ingevuld formulier gaat rechtstreeks naar de server en belandt in de
    databank van Connectopia; daarna komt de bezoeker op /bedankt. Er komt
    geen mailprogramma en geen andere firma aan te pas.

    Dit is met opzet een gewoon formulier zonder javascript eromheen: zo
    werkt het op elke telefoon, ook bij wie zijn mail in de browser leest.
    Zet hier dus nooit een mailto-actie terug.
  */
  return (
    <form action={aanvraagVersturen} className="grid gap-5">
      {kop}

      <input type="hidden" name="onderwerp" value={onderwerp} />
      {/* Een vakje dat alleen een robot invult. Blijft onzichtbaar. */}
      <div className="hidden" aria-hidden>
        <label>
          Laat dit veld leeg
          <input type="text" name="adres" tabIndex={-1} autoComplete="off" />
        </label>
      </div>
      {verborgen.map((veld) => (
        <input
          key={veld.naam}
          type="hidden"
          name={veld.naam}
          value={veld.waarde}
        />
      ))}

      <div className="grid gap-5 sm:grid-cols-2">
        {vragen.map((veld) => {
          /*
            Een groep aankruisvakjes neemt de volle breedte. Elk vakje
            stuurt zijn eigen naam mee, dus in de mail staat alleen wat
            werkelijk aangevinkt is.
          */
          if (veld.soort === "keuzes") {
            return (
              <fieldset key={veld.naam} className="sm:col-span-2">
                <legend className="text-[15px] font-bold text-ink">
                  {veld.label}
                </legend>
                {veld.hulp ? (
                  <p className="mt-1 text-[14px] text-ink-dim">{veld.hulp}</p>
                ) : null}
                <div className="mt-2 grid gap-2.5">
                  {(veld.keuzes ?? []).map((keuze) => (
                    <div
                      key={keuze.naam}
                      className="flex flex-wrap items-center gap-x-3 gap-y-2"
                    >
                      <label className="flex items-start gap-2.5 text-[16px] text-ink">
                        <input
                          type="checkbox"
                          name={keuze.naam}
                          value="ja"
                          className="mt-1 h-[18px] w-[18px] shrink-0 accent-green"
                        />
                        {keuze.label}
                      </label>
                      {keuze.aantal ? (
                        <label className="flex items-center gap-2 text-[14px] text-ink-dim">
                          {keuze.aantal.label}
                          <input
                            type="number"
                            name={keuze.aantal.naam}
                            min={1}
                            className="h-10 w-24 rounded-full border border-border bg-cream px-4 text-[16px] text-ink outline-none focus:border-green"
                          />
                        </label>
                      ) : null}
                    </div>
                  ))}
                </div>
              </fieldset>
            );
          }

          const lang = veld.soort === "lang";
          const verplicht = veld.verplicht && !optioneel.includes(veld.naam);
          const type =
            veld.soort === "email"
              ? "email"
              : veld.soort === "telefoon"
                ? "tel"
                : "text";
          return (
            <div key={veld.naam} className={lang ? "sm:col-span-2" : undefined}>
              <label className="block">
                <span className="text-[15px] font-bold text-ink">
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
                    className="mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[16px] text-ink outline-none focus:border-green"
                  />
                ) : (
                  <input
                    type={type}
                    name={veld.naam}
                    required={verplicht}
                    autoComplete={
                      veld.soort === "email"
                        ? "email"
                        : veld.soort === "telefoon"
                          ? "tel"
                          : undefined
                    }
                    className="mt-1.5 block h-11 w-full rounded-full border border-border bg-cream px-4 text-[16px] text-ink outline-none focus:border-green"
                  />
                )}
              </label>
              {veld.hulp ? (
                <p className="mt-1 text-[14px] text-ink-dim">{veld.hulp}</p>
              ) : null}
            </div>
          );
        })}
      </div>

      {/* Wat er met de gegevens gebeurt. */}
      <div className="rounded-[16px] bg-purple-soft px-5 py-4">
        <p className="text-[15px] text-ink">{privacy}</p>
        <label className="mt-3 flex items-start gap-2.5 text-[15px] font-bold text-ink">
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
        <Verstuurknop />
      </div>
    </form>
  );
}
