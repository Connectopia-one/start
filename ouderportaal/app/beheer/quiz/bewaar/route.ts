import { getSessionProfile } from "@/lib/auth";
import { createAdminClient } from "@/lib/supabase/admin";

/*
  Bewaart één deelname aan de wedstrijdquiz bij de aanvragen (soort
  "wedstrijd"), zodat ze in het beheer naast de gewone aanvragen staan.
  De quiz draait op Kims iPad, ingelogd als beheerder; enkel dan mag dit.
*/

const ONDERWERP = "Wedstrijd Dag van de Wetenschap 2026";
const SOORT = "wedstrijd";

function tekst(waarde: unknown, max = 300): string {
  return String(waarde ?? "").trim().slice(0, max);
}

export async function POST(request: Request) {
  const session = await getSessionProfile();
  if (session?.profile?.role !== "beheerder") {
    return Response.json({ ok: false, fout: "niet-ingelogd" }, { status: 401 });
  }

  let invoer: Record<string, unknown>;
  try {
    invoer = await request.json();
  } catch {
    return Response.json({ ok: false, fout: "ongeldig" }, { status: 400 });
  }

  const id = tekst(invoer.id, 40);
  const naam = tekst(invoer.naam, 200);
  const email = tekst(invoer.email, 200);
  if (!id || !naam || !email) {
    return Response.json({ ok: false, fout: "onvolledig" }, { status: 400 });
  }

  const gegevens: Record<string, string> = {
    "Naam ouder": naam,
    "E-mail": email,
    Telefoon: tekst(invoer.telefoon, 50),
    Gemeente: tekst(invoer.gemeente, 100),
    "Aantal kinderen": tekst(invoer.aantalKinderen, 5),
    "Leeftijden kinderen": tekst(invoer.leeftijden),
    "Quizscore": tekst(invoer.score, 10),
    "Schiftingsvraag (aantal deelnemers)": tekst(invoer.schifting, 10),
    "Antwoorden quiz": tekst(invoer.antwoorden, 1000),
    "Kamp en hobby: soort": tekst(invoer.kampSoort, 500),
    "Kamp en hobby: vakantie": tekst(invoer.kampVakantie, 500),
    "Kamp en hobby: vorm": tekst(invoer.kampVorm, 500),
    "Kamp en hobby: belangrijk": tekst(invoer.kampBelangrijk, 500),
    "Ingevuld op": tekst(invoer.datum, 40),
    "Akkoord wedstrijd en contact over Connectopia": "ja",
    "Quiz-id": id,
  };
  /* Elke interesse als eigen vakje met "ja": zo verschijnt ze ook vanzelf
     als lijst onder Aanvragen > Lijsten. */
  for (const interesse of tekst(invoer.interesses, 300).split(",")) {
    const schoon = interesse.trim();
    if (schoon) gegevens[`Interesse ${schoon}`.slice(0, 200)] = "ja";
  }
  for (const sleutel of Object.keys(gegevens)) {
    if (!gegevens[sleutel]) delete gegevens[sleutel];
  }

  const db = createAdminClient();

  /* Viel de wifi weg net na het bewaren, dan stuurt de iPad dezelfde
     deelname nog eens. Die zetten we er geen tweede keer bij. */
  const { data: bestaand } = await db
    .from("aanvragen")
    .select("id")
    .eq("soort", SOORT)
    .contains("gegevens", { "Quiz-id": id })
    .limit(1);
  if (bestaand && bestaand.length) return Response.json({ ok: true });

  const { error } = await db
    .from("aanvragen")
    .insert({ onderwerp: ONDERWERP, soort: SOORT, gegevens });
  if (error) {
    console.error("Quizdeelname bewaren mislukt:", error.message);
    return Response.json({ ok: false, fout: "mislukt" }, { status: 500 });
  }
  return Response.json({ ok: true });
}
