import { chromium } from '@playwright/test';
import { fileURLToPath, pathToFileURL } from 'node:url';
import path from 'node:path';

const root = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ channel: 'chrome', headless: true });
try {
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(path.join(root, 'review.html')).href);
  await page.locator('img').evaluateAll(images => Promise.all(images.map(image => image.decode())));
  for (const name of ['peek', 'stamp', 'watch']) {
    await page.goto(pathToFileURL(path.join(root, `${name}.svg`)).href);
    await page.setViewportSize({ width: 1254, height: 1254 });
    await page.screenshot({ path: path.join(root, `${name}-vector-preview.png`), omitBackground: true });
  }
  await page.setViewportSize({ width: 1400, height: 900 });
  await page.goto(pathToFileURL(path.join(root, 'review.html')).href);
  await page.locator('img').evaluateAll(images => Promise.all(images.map(image => image.decode())));
  await page.screenshot({ path: path.join(root, 'review.png'), fullPage: true });
  console.log('Rendered all three SVGs and the full-size/96px review sheet.');
} finally {
  await browser.close();
}
