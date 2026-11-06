/*
  Stuurt een beantwoorde vraag naar app/api/antwoord. Wacht nergens op en
  faalt stil: een opslagprobleem mag de oefening nooit onderbreken. keepalive
  zorgt dat het antwoord ook aankomt als het kind meteen de pagina verlaat.
*/
export function bewaarAntwoord(
  kindId: string,
  vraagId: string,
  hoofdstukId: string | null,
  correct: boolean,
  gegevenAntwoord: string | number | boolean | number[] | null,
  variant = 0,
) {
  fetch("/api/antwoord", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ kindId, vraagId, hoofdstukId, correct, gegevenAntwoord, variant }),
    keepalive: true,
  }).catch(() => {});
}
