import { NextResponse } from "next/server";
import type { EmailOtpType } from "@supabase/supabase-js";
import { createClient } from "@/lib/supabase/server";

/**
 * Waar de bevestigingslink uit de registratiemail op uitkomt.
 *
 * Supabase stuurt die link in twee mogelijke vormen, afhankelijk van de
 * instellingen van het project:
 *   - ?code=...                       (de nieuwe manier, PKCE)
 *   - ?token_hash=...&type=signup     (de klassieke manier)
 * Allebei worden ze hier afgehandeld, zodat het niet uitmaakt hoe het project
 * staat ingesteld.
 *
 * Vóór deze route bestond er helemaal geen landingsplaats: de link viel terug
 * op de "Site URL" van Supabase, en dat is gewoon de startpagina. Die pagina
 * wordt op de server gemaakt en doet niets met de sleutel die in het adres
 * meekomt, dus een ouder klikte op de link, kwam op een gewone pagina uit en
 * was nog altijd niet ingelogd. Dat voelt als "registreren lukt niet".
 */
export async function GET(request: Request) {
  const url = new URL(request.url);
  const code = url.searchParams.get("code");
  const tokenHash = url.searchParams.get("token_hash");
  const type = url.searchParams.get("type") as EmailOtpType | null;

  const supabase = await createClient();
  let fout: string | null = null;

  if (code) {
    const { error } = await supabase.auth.exchangeCodeForSession(code);
    fout = error?.message ?? null;
  } else if (tokenHash && type) {
    const { error } = await supabase.auth.verifyOtp({ token_hash: tokenHash, type });
    fout = error?.message ?? null;
  } else {
    fout = "Deze link is niet volledig. Vraag een nieuwe bevestigingsmail aan.";
  }

  if (fout) {
    console.error("bevestigingslink mislukt:", fout);
    return NextResponse.redirect(
      new URL(
        `/login?fout=${encodeURIComponent(
          "Deze bevestigingslink werkt niet meer. Hij is misschien al gebruikt of te oud. Log gewoon in met je e-mailadres en wachtwoord, of vraag een nieuw wachtwoord aan."
        )}`,
        url
      )
    );
  }

  return NextResponse.redirect(new URL("/account", url));
}
