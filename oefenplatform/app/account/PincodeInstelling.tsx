import { vergrendelNu, zetPin, zetPinUit } from "./pincode/actions";

/*
  In Mijn account: een pincode voor de ouder, voor wie een kind heeft dat
  zelfstandig oefent op het account van de ouder. Staat standaard uit.
*/
export function PincodeInstelling({ aan }: { aan: boolean }) {
  const veld =
    "w-28 rounded-md border border-border bg-paper px-3 py-2 text-sm tracking-widest text-ink outline-none focus:border-forest focus:ring-1 focus:ring-forest";
  const pinVeld = (naam: string, label: string) => (
    <input
      name={naam}
      type="password"
      inputMode="numeric"
      pattern="\d{4}"
      maxLength={4}
      required
      autoComplete="off"
      placeholder="4 cijfers"
      aria-label={label}
      className={veld}
    />
  );

  return (
    <div id="pincode" className="mt-8 rounded-xl border border-border bg-surface p-6">
      <h2 className="font-display text-lg font-semibold text-ink">
        <span aria-hidden>🔒</span> Pincode voor ouders
      </h2>
      {aan ? (
        <>
          <p className="mt-1 text-sm text-ink-dim">
            De pincode staat aan. Mijn account, de voortgang en de lijst met
            foute vragen gaan pas open na de pincode. Na een halfuur gaan ze
            vanzelf weer op slot.
          </p>
          <div className="mt-4 flex flex-wrap gap-3">
            <form action={vergrendelNu}>
              <button
                type="submit"
                className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
              >
                Nu op slot doen
              </button>
            </form>
            <form action={zetPinUit}>
              <button
                type="submit"
                className="rounded-md border border-border px-3 py-2 text-sm text-ink-dim hover:border-danger hover:text-danger"
              >
                Pincode uitzetten
              </button>
            </form>
          </div>
          <details className="mt-4 text-sm">
            <summary className="cursor-pointer text-ink-dim hover:text-ink">
              Pincode wijzigen
            </summary>
            <form action={zetPin} className="mt-3 flex flex-wrap items-center gap-2">
              {pinVeld("pin", "Nieuwe pincode")}
              {pinVeld("pin2", "Nieuwe pincode nog eens")}
              <button
                type="submit"
                className="rounded-md border border-border px-3 py-2 text-sm text-ink hover:border-forest"
              >
                Bewaren
              </button>
            </form>
          </details>
        </>
      ) : (
        <details className="mt-1 text-sm">
          <summary className="cursor-pointer text-ink-dim hover:text-ink">
            Mijn kind oefent zelfstandig: scherm de voortgang af met een pincode
          </summary>
          <p className="mt-2 text-ink-dim">
            Dan gaan Mijn account, de voortgang en de lijst met foute vragen
            pas open na een pincode van 4 cijfers die enkel jij kent. Het
            oefenen zelf blijft gewoon open. Vergeet je de pincode, dan zet je
            ze opnieuw met het wachtwoord van je account.
          </p>
          <form action={zetPin} className="mt-3 flex flex-wrap items-center gap-2">
            {pinVeld("pin", "Pincode")}
            {pinVeld("pin2", "Pincode nog eens")}
            <button
              type="submit"
              className="rounded-md bg-forest px-3 py-2 text-sm font-medium text-white hover:bg-forest-dark"
            >
              Pincode aanzetten
            </button>
          </form>
        </details>
      )}
    </div>
  );
}
