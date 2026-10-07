import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { VitePWA } from "vite-plugin-pwa";
import audioAssets from "./src/audio-assets.json";
import brandAssets from "./src/brand-assets.json";
// An explicit offline download must fit the installed catalog, including future levels.
const audioCacheCapacity = Math.max(
  6000,
  new Set(Object.values(audioAssets).flatMap((voices) => Object.values(voices)))
    .size,
);
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: "prompt",
      includeAssets: [brandAssets.icon32.src.slice(1), "favicon.ico", "icon.svg"],
      manifest: {
        name: "Kiyo 清 · Mandarin, crystal clear",
        short_name: "Kiyo",
        description: "Listen. Understand. Join the conversation.",
        theme_color: "#101b2b",
        background_color: "#101b2b",
        display: "standalone",
        icons: [
          {
            src: brandAssets.icon192.src,
            sizes: "192x192",
            type: "image/png",
            purpose: "any",
          },
          {
            src: brandAssets.icon512.src,
            sizes: "512x512",
            type: "image/png",
            purpose: "any",
          },
        ],
      },
      workbox: {
        // Activate the cache update even for older installs without an update UI.
        // UpdateNotice leaves the running React session intact until Refresh.
        skipWaiting: true,
        clientsClaim: true,
        // Access must finish its server-side callback before the offline shell
        // handles app navigation; otherwise an expired login cannot recover.
        navigateFallbackDenylist: [/^\/cdn-cgi\//],
        globPatterns: ["**/*.{js,css,html,svg,woff2,mp3,json,png,webp}"],
        // CJK fonts ship as ~100 unicode-range slices per weight; cache the
        // slices a learner actually uses instead of precaching all of them.
        // Full-size mascot PNGs are only for the gallery download; the app uses WebP.
        // Sayo's clips are cached the first time each one plays (and all at once from
        // Settings → "Save audio for offline"), so the install stays small as the course grows.
        globIgnores: [
          "**/noto-serif-sc-*.woff2",
          "**/mascot/quiet/*.png",
          "audio/**",
          "audio-reactions/**",
          "audio-v2/**",
          // The dictionary (~17 MB in 256 shards) loads per lookup; see src/dictionary.ts.
          "dict/**",
        ],
        runtimeCaching: [
          {
            urlPattern: /\/dict\/[^/]+\.json$/,
            handler: "StaleWhileRevalidate",
            options: {
              cacheName: "kiyo-dict",
              expiration: { maxEntries: 300 },
              cacheableResponse: { statuses: [200] },
              plugins: [
                {
                  // Never store an HTML fallback page as a dictionary shard.
                  cacheWillUpdate: async ({ response }) =>
                    response.status === 200 &&
                    /json/i.test(response.headers.get("content-type") ?? "")
                      ? response
                      : null,
                },
              ],
            },
          },
          {
            urlPattern: /\/audio-v2\/.+\.(mp3|wav)$/,
            handler: "CacheFirst",
            options: {
              cacheName: "sayo-audio",
              // Clip files are content-hashed, so a cached clip never goes stale.
              expiration: { maxEntries: audioCacheCapacity },
              cacheableResponse: { statuses: [200] },
              rangeRequests: true,
              plugins: [
                {
                  // <audio> asks for byte ranges; fetch the whole clip so it can be cached,
                  // then later ranges are served from the cached copy.
                  requestWillFetch: async ({ request }) =>
                    new Request(request.url, { credentials: "same-origin" }),
                  cacheWillUpdate: async ({ response }) =>
                    response.status === 200 &&
                    /^audio\//i.test(response.headers.get("content-type") ?? "")
                      ? response
                      : null,
                },
              ],
            },
          },
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
    watch: {
      ignored: [
        "**/.voice-design-env/**",
        "**/.tts-env/**",
        "**/.audio-env/**",
        "**/.models/**",
        "**/.tts/**",
        "**/.cache/**",
        "**/.dict-cache/**",
        "**/output/**",
      ],
    },
  },
  build: {
    chunkSizeWarningLimit: 700,
    // Keep each data bundle below the existing offline precache file limit.
    // All are still cached; this separates data from frequently changing UI code.
    rolldownOptions: {
      output: {
        codeSplitting: {
          groups: [
            { name: "course-data", test: /generated[\\/]packs\.json$/ },
            { name: "audio-catalog", test: /src[\\/]audio-assets\.json$/ },
          ],
        },
      },
    },
  },
});
