import "server-only";
import createMollieClient from "@mollie/api-client";

export function mollieClient() {
  return createMollieClient({ apiKey: process.env.MOLLIE_API_KEY! });
}

/** Prijs voor een volledig schooljaar toegang, in euro. Pas hier aan als de prijs wijzigt. */
export const PRIJS_SCHOOLJAAR_EUR = 50;
