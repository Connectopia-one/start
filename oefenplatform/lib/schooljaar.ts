/** Geeft het huidige schooljaar terug als "2026-2027". Schooljaar loopt van september t.e.m. augustus. */
export function huidigSchooljaar(datum = new Date()): string {
  const jaar = datum.getFullYear();
  const maand = datum.getMonth() + 1; // 1-12
  return maand >= 8 ? `${jaar}-${jaar + 1}` : `${jaar - 1}-${jaar}`;
}

/** Voor weergave: "31 augustus 2027" — het einde van het gegeven (of huidige) schooljaar. */
export function schooljaarEindeLabel(schooljaar = huidigSchooljaar()): string {
  const eindJaar = schooljaar.split("-")[1];
  return `31 augustus ${eindJaar}`;
}
