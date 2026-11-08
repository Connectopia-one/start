/**
 * De hoofdstukken die enkel voor de richting welzijnswetenschappen tellen.
 *
 * Kim op 8 november 2026: zet ze in het gewone vak natuurwetenschappen 🌍
 * Beyond, met een eigen kleur en de vermelding dat ze enkel voor
 * welzijnswetenschappen tellen, en laat ze niet zomaar in het examen van het
 * vak opduiken. De vakfiche "natuurwetenschappen welzijnswetenschappen" bevat
 * alles van de gewone fiche 3DO plus een blok over het menselijk lichaam
 * (nagekeken lijn per lijn op Kims usb-stick). Eén examen, dus één vak.
 *
 * Herkend aan de titel, net als "— pittig": "Welzijnswetenschappen: Het bloed
 * — deel 1". Geen kolom in de databank. Hoe ze verhuisd zijn: zie
 * supabase/welzijn-in-natuurwetenschappen.sql.
 */
export const WELZIJN_VOORVOEGSEL = "Welzijnswetenschappen:";

export function isWelzijn(titel: string) {
  return titel.trim().toLowerCase().startsWith(WELZIJN_VOORVOEGSEL.toLowerCase());
}
