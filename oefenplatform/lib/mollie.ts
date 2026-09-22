import "server-only";
import createMollieClient from "@mollie/api-client";

export function mollieClient() {
  return createMollieClient({ apiKey: process.env.MOLLIE_API_KEY! });
}

// De prijs zelf staat in lib/prijs.ts, zodat hij op één plek aan te passen is.
