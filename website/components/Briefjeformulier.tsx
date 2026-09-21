import { verzenden } from "@/content/formulier";
import { prikbord } from "@/content/prikbord";

/*
  Het formulier waarmee een ouder een briefje instuurt voor het prikbord.
  Het werkt net als het aanvraagformulier: zolang er geen formulierdienst
  is ingesteld, opent het het mailprogramma met alles al ingevuld.

  De teksten staan in content/prikbord.ts bij "formulier".
*/
export function Briefjeformulier({ bord }: { bord: string }) {
  const perMail = !verzenden.webadres;
  const actie = perMail
    ? `mailto:${verzenden.mailnaar}?subject=${encodeURIComponent(`Prikbord: ${bord}`)}`
    : verzenden.webadres!;

  const veld =
    "mt-1.5 block w-full rounded-[14px] border border-border bg-cream px-4 py-3 text-[15px] text-ink outline-none focus:border-green";

  return (
    <form
      action={actie}
      method="post"
      encType={perMail ? "text/plain" : undefined}
      className="grid gap-4"
    >
      <input type="hidden" name="Bord" value={bord} />

      <label className="block">
        <span className="text-[14px] font-bold text-ink">
          {prikbord.formulier.briefjeLabel}
          <span className="text-orange" aria-hidden>
            {" "}
            *
          </span>
        </span>
        <textarea name="Briefje" rows={4} required className={veld} />
      </label>

      <div className="grid gap-4 sm:grid-cols-2">
        <label className="block">
          <span className="text-[14px] font-bold text-ink">
            {prikbord.formulier.naamLabel}
          </span>
          <input type="text" name="Naam" className={veld} />
        </label>
        <label className="block">
          <span className="text-[14px] font-bold text-ink">
            {prikbord.formulier.mailLabel}
            <span className="text-orange" aria-hidden>
              {" "}
              *
            </span>
          </span>
          <input type="email" name="E-mailadres" required className={veld} />
        </label>
      </div>

      <p className="text-[13.5px] text-ink-dim">{prikbord.formulier.privacy}</p>

      <div>
        <button
          type="submit"
          className="rounded-full bg-green px-6 py-3 text-[15px] font-extrabold text-cream transition hover:-translate-y-0.5"
        >
          {prikbord.formulier.knopTekst} →
        </button>
      </div>
    </form>
  );
}
