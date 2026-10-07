import "server-only";
import createMollieClient from "@mollie/api-client";

export function mollieClient() {
  return createMollieClient({ apiKey: process.env.MOLLIE_API_KEY! });
}

/**
 * Begint de sleutel in Vercel met test_, dan staat Mollie in testmodus. Dan
 * kiest de bezoeker op het afrekenscherm zélf of de betaling "betaald", "open"
 * of "mislukt" is, beweegt er geen geld, en zou hij toch volledige toegang
 * krijgen. Daarom starten we geen betaling zolang die sleutel er staat, en
 * geeft de webhook geen toegang voor een betaling in testmodus.
 */
export function isTestSleutel() {
  return (process.env.MOLLIE_API_KEY || "").startsWith("test_");
}

// De prijs zelf staat in lib/prijs.ts, zodat hij op één plek aan te passen is.
