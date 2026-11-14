import { getSessionProfile } from "@/lib/auth";
import { QUIZ_HTML } from "@/lib/quiz/pagina";

/* De quiz zelf, enkel voor wie als beheerder is ingelogd. Zie lib/quiz/pagina.ts. */
export async function GET(request: Request) {
  const session = await getSessionProfile();
  if (!session) return Response.redirect(new URL("/login", request.url));
  if (session.profile?.role !== "beheerder") {
    return Response.redirect(new URL("/portaal", request.url));
  }
  return new Response(QUIZ_HTML, {
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
      "X-Robots-Tag": "noindex, nofollow",
    },
  });
}
