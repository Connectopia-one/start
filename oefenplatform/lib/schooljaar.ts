/** Geeft het huidige schooljaar terug als "2026-2027". Schooljaar start in september. */
export function huidigSchooljaar(datum = new Date()): string {
  const jaar = datum.getFullYear();
  const maand = datum.getMonth() + 1; // 1-12
  return maand >= 8 ? `${jaar}-${jaar + 1}` : `${jaar - 1}-${jaar}`;
}
