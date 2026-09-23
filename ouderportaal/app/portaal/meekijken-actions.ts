"use server";

import { redirect } from "next/navigation";
import { revalidatePath } from "next/cache";
import { zetMeekijken, wisMeekijken } from "@/lib/meekijken";

/** Start het meekijken met een gezin en ga meteen naar het portaaloverzicht. */
export async function startMeekijken(formData: FormData) {
  const id = String(formData.get("gezinId") || "");
  if (!id) return;
  const gelukt = await zetMeekijken(id);
  if (!gelukt) return;
  revalidatePath("/", "layout");
  redirect("/portaal");
}

/** Stop het meekijken. Je bent daarna gewoon weer jezelf. */
export async function stopMeekijken(formData: FormData) {
  await wisMeekijken();
  revalidatePath("/", "layout");
  const terug = String(formData.get("terug") || "/beheer/gezinnen");
  redirect(terug);
}
