"""Stellt interne Links, Canonicals, og:url und JSON-LD-URLs auf finale URLs um.

Nutzung: python seo/tools/rewrite-links.py [--dry]
Gibt Links aus, deren Ziel sich inhaltlich geändert hat (Ankertext prüfen).
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
import urlmap  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SKIP_DIRS = {"node_modules", ".git", ".vercel", "seo", "skills", "Datei Manager", "transfer", ".codex-remote-attachments", "api"}
HOST_RE = r"https?://(?:www\.)?powertech-performance\.com"

HREF_RE = re.compile(r'(href=")(' + HOST_RE + r')?(/[^"#?]*)?([?#][^"]*)?(")')
ABS_RE = re.compile(r'(' + HOST_RE + r')(/[^"\'\s<>#?\\]*)')


def html_files():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if f.endswith(".html") and not f.startswith("google"):
                yield os.path.join(dp, f)


def merged(old, new):
    norm = lambda p: p.rstrip("/") or "/"
    return norm(old) != norm(new)


def main(dry=False):
    changes = 0
    review = []
    for path in html_files():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        src = open(path, encoding="utf-8").read()

        def fix_href(m):
            pre, host, p, tail, post = m.groups()
            if p is None:
                return m.group(0)
            if p.startswith(("/images/", "/css/", "/js/", "/fonts/", "/api/")) or p in ("/sitemap.xml", "/robots.txt"):
                return m.group(0)
            new = urlmap.resolve(p)
            if merged(p, new):
                review.append((rel, p, new))
            return pre + (urlmap.HOST if host else "") + new + (tail or "") + post

        out = HREF_RE.sub(fix_href, src)

        def fix_abs(m):
            p = m.group(2)
            if p.startswith(("/images/", "/css/", "/js/", "/fonts/")) or p in ("/sitemap.xml", "/robots.txt"):
                return urlmap.HOST + p
            return urlmap.HOST + urlmap.resolve(p)

        out = ABS_RE.sub(fix_abs, out)
        if out != src:
            changes += 1
            if not dry:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(out)
    print(changes, "Dateien geändert")
    for rel, old, new in sorted(set(review)):
        print("ZIEL GEÄNDERT", rel, old, "->", new)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main("--dry" in sys.argv)
