"use client";

import { useFormStatus } from "react-dom";

/**
 * Een verzendknop die zichzelf op slot zet zolang het formulier onderweg is.
 *
 * Zonder dit kan iemand twee keer klikken, en dan vertrekken er twee
 * aanvragen. Bij registreren maakte de eerste het account aan en zei de
 * tweede "dit adres bestaat al" — terwijl alles gelukt was. Een knop op slot
 * is daar nooit de hele oplossing voor: er hoort altijd ook een controle op
 * de server naast. Zie app/registreren/actions.ts.
 */
export function Verzendknop({
  label,
  bezigLabel,
  className,
}: {
  label: string;
  bezigLabel: string;
  className?: string;
}) {
  const { pending } = useFormStatus();
  return (
    <button
      type="submit"
      disabled={pending}
      aria-busy={pending}
      className={`${className ?? ""} disabled:cursor-not-allowed disabled:opacity-60`}
    >
      {pending ? bezigLabel : label}
    </button>
  );
}
