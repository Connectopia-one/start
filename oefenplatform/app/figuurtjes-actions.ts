"use server";

import type { SupabaseClient } from "@supabase/supabase-js";
import { createClient } from "@/lib/supabase/server";
import { createAdminClient } from "@/lib/supabase/admin";
import { alleRijen } from "@/lib/allerijen";
import { figuurtjeVan, uitgegeven } from "@/lib/figuurtjes";

/*
  Figuurtjes kiezen met sterretjes (supabase/figuurtjes.sql, lib/figuurtjes.ts).

  Een sterretje = een hoofdstuk dat het kind helemaal afwerkte: elke vraag die
  er nu in staat, minstens één keer beantwoord, juist of fout. Een hoofdstuk
  met een sticker (alles juist) telt ook. De sterretjes worden nergens
  bewaard, ze volgen altijd uit de voortgang, net als de badges.
*/

type Kind = {
  id: string;
  profile_id: string;
  toon_figuurtjes: boolean | null;
  figuurtjes: string[] | null;
  figuurtje: string | null;
};

async function eigenKind(
  kindId: string,
): Promise<{ admin: SupabaseClient; kind: Kind } | null> {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();
  if (!user) return null;
  const admin = createAdminClient();
  const { data: kind } = await admin
    .from("kinderen")
    .select("id, profile_id, toon_figuurtjes, figuurtjes, figuurtje")
    .eq("id", kindId)
    .maybeSingle();
  if (!kind || kind.profile_id !== user.id) return null;
  return { admin, kind: kind as Kind };
}

async function telSterretjes(admin: SupabaseClient, kindId: string): Promise<number> {
  const rijen = await alleRijen<{ hoofdstuk_id: string | null; vraag_id: string | null }>(
    (van, tot) =>
      admin
        .from("voortgang")
        .select("hoofdstuk_id, vraag_id")
        .eq("kind_id", kindId)
        .order("id")
        .range(van, tot),
  );
  const beantwoord = new Map<string, Set<string>>();
  for (const r of rijen) {
    if (!r.hoofdstuk_id || !r.vraag_id) continue;
    let set = beantwoord.get(r.hoofdstuk_id);
    if (!set) beantwoord.set(r.hoofdstuk_id, (set = new Set()));
    set.add(r.vraag_id);
  }

  // Hoeveel vragen staan er nu in de hoofdstukken waar het kind aan werkte?
  const ids = [...beantwoord.keys()];
  const totaal = new Map<string, number>();
  for (let i = 0; i < ids.length; i += 150) {
    const blok = ids.slice(i, i + 150);
    const vragen = await alleRijen<{ id: string; hoofdstuk_id: string }>((van, tot) =>
      admin
        .from("vragen")
        .select("id, hoofdstuk_id")
        .in("hoofdstuk_id", blok)
        .order("id")
        .range(van, tot),
    );
    for (const v of vragen) totaal.set(v.hoofdstuk_id, (totaal.get(v.hoofdstuk_id) ?? 0) + 1);
  }

  const afgewerkt = new Set<string>();
  for (const [id, set] of beantwoord) {
    const n = totaal.get(id) ?? 0;
    if (n > 0 && set.size >= n) afgewerkt.add(id);
  }
  const { data: stickers } = await admin
    .from("stickers")
    .select("hoofdstuk_id")
    .eq("kind_id", kindId);
  for (const s of stickers ?? []) afgewerkt.add(s.hoofdstuk_id as string);
  return afgewerkt.size;
}

export type FiguurtjesStand = {
  aan: boolean;
  verdiend: number;
  over: number;
  eigen: string[];
  gekozen: string | null;
};

export async function haalFiguurtjes(kindId: string): Promise<FiguurtjesStand | null> {
  const r = await eigenKind(kindId);
  if (!r) return null;
  const eigen = r.kind.figuurtjes ?? [];
  if (!r.kind.toon_figuurtjes)
    return { aan: false, verdiend: 0, over: 0, eigen, gekozen: r.kind.figuurtje };
  const verdiend = await telSterretjes(r.admin, kindId);
  return {
    aan: true,
    verdiend,
    over: Math.max(0, verdiend - uitgegeven(eigen)),
    eigen,
    gekozen: r.kind.figuurtje,
  };
}

/** Een nieuw figuurtje nemen met sterretjes. Het wordt meteen ook het gekozen figuurtje. */
export async function neemFiguurtje(
  kindId: string,
  sleutel: string,
): Promise<{ fout?: string }> {
  const r = await eigenKind(kindId);
  const f = figuurtjeVan(sleutel);
  if (!r || !f || !r.kind.toon_figuurtjes) return { fout: "Dat lukte niet." };
  const eigen = r.kind.figuurtjes ?? [];
  if (eigen.includes(f.sleutel)) return {};
  const verdiend = await telSterretjes(r.admin, kindId);
  if (verdiend - uitgegeven(eigen) < f.prijs)
    return { fout: "Daarvoor heb je nog niet genoeg sterretjes." };
  const { error } = await r.admin
    .from("kinderen")
    .update({ figuurtjes: [...eigen, f.sleutel], figuurtje: f.sleutel })
    .eq("id", kindId);
  return error ? { fout: "Kon dit niet bewaren, probeer opnieuw." } : {};
}

/** Een figuurtje dat het kind al heeft, opnieuw kiezen als zijn figuurtje. */
export async function kiesFiguurtje(
  kindId: string,
  sleutel: string,
): Promise<{ fout?: string }> {
  const r = await eigenKind(kindId);
  if (!r || !(r.kind.figuurtjes ?? []).includes(sleutel)) return { fout: "Dat lukte niet." };
  const { error } = await r.admin.from("kinderen").update({ figuurtje: sleutel }).eq("id", kindId);
  return error ? { fout: "Kon dit niet bewaren, probeer opnieuw." } : {};
}
