/* Schrijft "2026-09-04" als "4 september 2026". */
export function datumInWoorden(datum: string) {
  return new Date(`${datum}T12:00:00`).toLocaleDateString("nl-BE", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}
