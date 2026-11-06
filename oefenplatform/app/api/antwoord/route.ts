import { registreerAntwoord } from "@/app/voortgang-actions";

/*
  Eén beantwoorde vraag bewaren, als gewoon verzoek in plaats van als server
  action.

  Testouders (Lotte, Marjolein, enquête november 2026) meldden dat het scherm
  soms bleef hangen als hun kind snel doorklikte. Server actions gaan in Next
  één voor één, in dezelfde wachtrij als het wisselen van pagina. Bij elke
  nagekeken vraag kwam er zo eentje bij, en elk ervan wacht op Supabase. Klikte
  een kind snel door en daarna op "terug" of een ander hoofdstuk, dan stond dat
  achteraan in de rij en leek alles vast te zitten. Een gewoon verzoek loopt
  daarnaast, zonder iets op te houden.
*/
export async function POST(request: Request) {
  try {
    const b = await request.json();
    if (typeof b?.kindId !== "string" || typeof b?.vraagId !== "string")
      return new Response(null, { status: 400 });
    await registreerAntwoord(
      b.kindId,
      b.vraagId,
      typeof b.hoofdstukId === "string" ? b.hoofdstukId : null,
      Boolean(b.correct),
      b.gegevenAntwoord ?? null,
      Number.isInteger(b.variant) ? b.variant : 0,
    );
    return new Response(null, { status: 204 });
  } catch {
    return new Response(null, { status: 500 });
  }
}
