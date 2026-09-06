import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    serverActions: {
      // Standaard is dit 1MB — te weinig voor foto's en pdf's.
      bodySizeLimit: "25mb",
    },
  },
};

export default nextConfig;
