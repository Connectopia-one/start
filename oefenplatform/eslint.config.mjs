import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // inhoud/leerbundels/bron is gereedschap dat los van de site draait (Node en
  // Python, om de pdf-leerbundels te maken), geen code van de website zelf.
  globalIgnores([
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
    "inhoud/leerbundels/bron/**",
  ]),
]);

export default eslintConfig;
