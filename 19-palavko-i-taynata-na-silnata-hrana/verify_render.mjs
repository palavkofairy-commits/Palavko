import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";
import { resolve } from "node:path";

const require = createRequire(import.meta.url);
const { chromium } = require("C:/Users/evgen/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright");

const base = resolve("D:/codex/Палавко редакция/19-palavko-i-taynata-na-silnata-hrana");
const url = pathToFileURL(resolve(base, "index.html")).href;
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 });
await page.goto(url, { waitUntil: "networkidle" });

const result = await page.evaluate(() => {
  const imgs = [...document.images];
  const broken = imgs.filter((img) => !img.complete || img.naturalWidth === 0).map((img) => img.getAttribute("src"));
  const firstMainChildren = [...document.querySelector("main").children].slice(0, 4).map((node) => node.tagName.toLowerCase());
  return {
    title: document.title,
    imageCount: imgs.length,
    broken,
    figureCount: document.querySelectorAll("figure").length,
    firstMainChildren,
    bodyHeight: document.body.scrollHeight,
  };
});

await page.screenshot({ path: resolve(base, "screenshot-first-screen.png"), fullPage: false });
await browser.close();
console.log(JSON.stringify(result, null, 2));
