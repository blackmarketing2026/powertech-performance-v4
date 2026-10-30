"""Erzeugt sitemap.xml aus den indexierbaren HTML-Seiten.

Nur finale URLs (Canonical der Seite), keine noindex-Seiten. <lastmod> ist das
Datum des letzten Commits der Datei bzw. heute bei lokalen Änderungen.
"""
import datetime
import os
import re
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SKIP_DIRS = {"node_modules", ".git", ".vercel", "seo", "skills", "Datei Manager", "transfer", ".codex-remote-attachments", "api"}


def lastmod(rel):
    dirty = subprocess.run(["git", "status", "--porcelain", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    if dirty:
        return datetime.date.today().isoformat()
    out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    return out or datetime.date.today().isoformat()


def main():
    entries = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not f.endswith(".html") or f.startswith("google"):
                continue
            path = os.path.join(dp, f)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            src = open(path, encoding="utf-8").read()
            if re.search(r'<meta name="robots" content="[^"]*noindex', src):
                continue
            m = re.search(r'<link rel="canonical" href="([^"]+)">', src)
            if not m:
                raise SystemExit("Canonical fehlt: " + rel)
            entries.append((m.group(1), lastmod(rel)))
    order = lambda e: (e[0].count("/blog/") + e[0].count("/ratgeber/"), e[0] != "https://www.powertech-performance.com/", e[0])
    entries.sort(key=order)
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, mod in entries:
        lines.append("  <url><loc>%s</loc><lastmod>%s</lastmod></url>" % (loc, mod))
    lines.append("</urlset>")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    print(len(entries), "URLs in sitemap.xml")


if __name__ == "__main__":
    main()
