/**
 * Welk kind op dit toestel aan het oefenen is.
 *
 * Eén ouder kan meerdere kinderen hebben, en die oefenen op dezelfde laptop
 * met dezelfde login. De keuze staat daarom in de browser zelf, niet in de
 * databank: ze hoort bij het toestel, niet bij het account. De Quiz gebruikt
 * ze om een antwoord bij het juiste kind op te slaan, en de hoofdstukken- en
 * vakkenlijsten om te tonen wat dát kind al gemaakt heeft.
 *
 * Privénavigatie of geblokkeerde opslag mag nooit iets breken, dus alles zit
 * in een try/catch en valt terug op het eerste kind.
 */

export const ACTIEF_KIND_KEY = "oefenplatform_actief_kind";

export function leesActiefKind(): string | null {
  try {
    return localStorage.getItem(ACTIEF_KIND_KEY);
  } catch {
    return null;
  }
}

export function bewaarActiefKind(id: string): void {
  try {
    localStorage.setItem(ACTIEF_KIND_KEY, id);
  } catch {
    // privénavigatie of geblokkeerde opslag: gewoon zonder onthouden verder
  }
}
