"""Erzeugt vercel.json aus seo/tools/urlmap.py.

Reihenfolge: spezifische Redirects zuerst (ein Sprung zum Endziel), danach die
allgemeine Slash-Regel. Ausgenommen sind /api (Formularversand), /_vercel,
/.well-known, /ads und /anfrage-danke (Ads/Conversion) und Pfade mit Dateiendung.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import urlmap  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

SLASH_RULE = {
    "source": "/:path((?!api/|api$|_vercel|\\.well-known|ads$|anfrage-danke$)(?:[^/]+/)*[^/.]+)",
    "destination": "/:path/",
    "permanent": True,
}


def main():
    redirects = [{"source": s, "destination": d, "permanent": True} for s, d in urlmap.redirects()]
    redirects.append(SLASH_RULE)
    rewrites = [{"source": "/%s/" % slug, "destination": "/%s.html" % slug} for slug in urlmap.ROOT_PAGES]
    rewrites += [{"source": "/%s" % slug, "destination": "/%s.html" % slug} for slug in urlmap.LEGACY_NOSLASH]
    rewrites += [{"source": s, "destination": d} for s, d in urlmap.EXTRA_REWRITES.items()]
    for r in rewrites:
        if not os.path.isfile(os.path.join(ROOT, r["destination"].lstrip("/"))):
            raise SystemExit("Rewrite-Ziel fehlt: " + r["destination"])
    lines = ["{", '  "redirects": [']
    lines.append(",\n".join("    " + json.dumps(r, ensure_ascii=False) for r in redirects))
    lines += ["  ],", '  "rewrites": [']
    lines.append(",\n".join("    " + json.dumps(r, ensure_ascii=False) for r in rewrites))
    lines += ["  ]", "}", ""]
    with open(os.path.join(ROOT, "vercel.json"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))
    print(len(redirects), "Redirects,", len(rewrites), "Rewrites")


if __name__ == "__main__":
    main()
