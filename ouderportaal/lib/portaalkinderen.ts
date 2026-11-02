import "server-only";
import { createAdminClient } from "@/lib/supabase/admin";
import { alleMailadressen } from "@/lib/mailadressen";
import type { PortaalKind } from "@/lib/kindzoeken";

/* Alle kinderen van het ouderportaal, met het gsm-nummer en het mailadres
   van hun gezin, om een naam van een inschrijving aan te koppelen. */
export async function portaalKinderen(): Promise<PortaalKind[]> {
  const db = createAdminClient();
  const [{ data: kinderen }, { data: gezinnen }, mails] = await Promise.all([
    db.from("kinderen").select("id, naam, profile_id"),
    db.from("profiles").select("id, telefoon"),
    alleMailadressen(),
  ]);
  const telefoon = new Map(
    ((gezinnen ?? []) as { id: string; telefoon: string | null }[]).map((g) => [
      g.id,
      g.telefoon,
    ]),
  );
  return ((kinderen ?? []) as { id: string; naam: string; profile_id: string }[]).map(
    (k) => ({
      id: k.id,
      naam: k.naam,
      telefoon: telefoon.get(k.profile_id) ?? null,
      mail: mails.get(k.profile_id) ?? null,
    }),
  );
}
