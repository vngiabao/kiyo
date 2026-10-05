import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { VitePWA } from "vite-plugin-pwa";
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: "prompt",
      includeAssets: ["icon.svg"],
      manifest: {
        name: "Kiyo 清 · Mandarin, crystal clear",
        short_name: "Kiyo",
        description: "Listen. Understand. Join the conversation.",
        theme_color: "#101b2b",
        background_color: "#101b2b",
        display: "standalone",
        icons: [
          {
            src: "/icon.svg",
            sizes: "any",
            type: "image/svg+xml",
            purpose: "any",
          },
        ],
      },
      workbox: {
        globPatterns: ["**/*.{js,css,html,svg,woff2,mp3,json,png,webp}"],
        // CJK fonts ship as ~100 unicode-range slices per weight; cache the
        // slices a learner actually uses instead of precaching all of them.
        // Full-size mascot PNGs are only for the gallery download; the app uses WebP.
        globIgnores: ["**/noto-serif-sc-*.woff2", "**/mascot/quiet/*.png", "audio/**", "audio-reactions/**"],
        runtimeCaching: [
          {
            urlPattern: /noto-serif-sc-.*\.woff2$/,
            handler: "CacheFirst",
            options: {
              cacheName: "cjk-fonts",
              expiration: { maxEntries: 400 },
            },
          },
        ],
        maximumFileSizeToCacheInBytes: 4000000,
      },
    }),
  ],
  server: {
    port: 5173,
    // Local speech runtimes contain thousands of files unrelated to the app.
    watch: { ignored: ["**/.voice-design-env/**", "**/.tts-env/**", "**/.audio-env/**", "**/.models/**", "**/.tts/**"] },
  },
  build: { chunkSizeWarningLimit: 700 },
});
