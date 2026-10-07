// Browser fallback and the old favicon URL both use the approved portrait.
import { readFileSync, writeFileSync } from "node:fs";
import assets from "../src/brand-assets.json";

const png = readFileSync(`public${assets.icon32.src}`);
// ICO supports a PNG payload; preserve the approved pixels without conversion.
const directory = Buffer.alloc(22);
directory.writeUInt16LE(1, 2);
directory.writeUInt16LE(1, 4);
directory[6] = assets.icon32.width;
directory[7] = assets.icon32.height;
directory.writeUInt16LE(1, 10);
directory.writeUInt16LE(32, 12);
directory.writeUInt32LE(png.length, 14);
directory.writeUInt32LE(directory.length, 18);
writeFileSync("public/favicon.ico", Buffer.concat([directory, png]));

// Compatibility for older open pages pointing at /icon.svg. This embeds raster
// artwork in an SVG container; it is not a vector drawing of the character.
const portrait = readFileSync(`public${assets.icon192.src}`).toString("base64");
writeFileSync(
  "public/icon.svg",
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 192 192"><title>Kiyo · Sayo</title><image width="192" height="192" href="data:image/png;base64,${portrait}"/></svg>`,
);
console.log("Exported Sayo browser favicon and legacy-URL compatibility icon.");
