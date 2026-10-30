"""Zentrale URL-Zuordnung (Stand 12.10.2026, freigegeben im SEO-Audit seo-audit.md).

Einheitliches Schema: https://www.powertech-performance.com/pfad/ (mit Slash).
Wird von build-routing.py (vercel.json) und rewrite-links.py (Links, Canonicals,
Sitemap) gelesen. Nicht von Hand in vercel.json ändern, sondern hier.
"""

HOST = "https://www.powertech-performance.com"

# Root-Seiten als Datei <slug>.html, ausgeliefert unter /<slug>/ (Rewrite).
ROOT_PAGES = [
    "autoaufbereitung",
    "keramikversiegelung-erfurt",
    "lackaufbereitung-erfurt",
    "innenraumreinigung-erfurt",
    "cabrioverdeck-reinigung-erfurt",
    "oldtimer-aufbereitung-erfurt",
    "leasingrueckgabe-aufbereitung-erfurt",
    "leasingrueckgabe-termin",
    "trockeneisreinigung",
    "motorwaesche-trockeneis",
    "auto-handwaesche-erfurt",
    "graffiti-entfernung-trockeneis",
    "adblue-diagnose-erfurt",
    "einzugsgebiet",
    "online-termin-buchen",
    "glosar",
]

# Ads-Landingpage und Danke-Seite (Conversion) behalten ihre bisherige URL ohne
# Slash, damit Google-Ads-Ziel-URLs und GTM-Trigger unverändert gelten.
LEGACY_NOSLASH = ["ads", "anfrage-danke"]

# Weitere Rewrites: öffentliche URL -> Datei
EXTRA_REWRITES = {
    "/kontakt/": "/pages/kontakt.html",
}

# Ehemalige Root-Seiten (Datei, Landingpage-Pfad, Slash-Varianten) -> Endziel
OLD_ROOT_PAGES = {
    "gotha": "/einzugsgebiet/",
    "jena": "/einzugsgebiet/",
    "suhl": "/einzugsgebiet/",
    "gera": "/einzugsgebiet/",
    "nordhausen": "/einzugsgebiet/",
    "eisenach": "/einzugsgebiet/",
    "fahrzeugaufbereitung-aus-erfurt": "/autoaufbereitung/",
    "luxus-aufbereitung": "/keramikversiegelung-erfurt/",
    "adblue-service": "/adblue-diagnose-erfurt/",
    "adblue-deaktivieren": "/blog/adblue-deaktivieren-vor-nachteile-wahrheit/",
    "fahrzeugaufbereitung-erfurt": "/autoaufbereitung/",
}

# Zusammengeführte oder umbenannte Blogartikel: Slug -> Endziel
BLOG_MERGED = {
    "fahrzeugaufbereitung-erfurt": "/autoaufbereitung/",
    "professionelle-keramikversiegelung-erfurt": "/keramikversiegelung-erfurt/",
    "profi-keramikversiegelung": "/keramikversiegelung-erfurt/",
    "keramikversiegelung-erfurt-high-end-lackschutz-powertech-performance": "/keramikversiegelung-erfurt/",
    "haltbarkeit-keramikversiegelung-lackschutz": "/blog/keramikversiegelung-haltbarkeit/",
    "blog-keramikversiegelung": "/blog/keramikversiegelung-haltbarkeit/",
    "keramik-fuer-auto-erfurt-vorteile-haltbarkeit": "/blog/keramikversiegelung-haltbarkeit/",
    "keramikversiegelung-profi-lackschutz": "/blog/keramikversiegelung-haltbarkeit/",
    "harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung": "/blog/harte-weiche-autolacke-lackaufbereitung/",
    "harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung-2": "/blog/harte-weiche-autolacke-lackaufbereitung/",
    "1-step-politur-erklaert": "/blog/1-step-2-step-oder-lackkorrektur-lackaufbereitung-im-vergleich/",
    "wie-lange-dauert-adblue-off": "/blog/adblue-deaktivieren-vor-nachteile-wahrheit/",
    "innenreinigung-auto-in-der-naehe": "/innenraumreinigung-erfurt/",
    "professionelle-cabrioverdeck-impraegnierung-und-reinigung": "/cabrioverdeck-reinigung-erfurt/",
    "oldtimer-aufbereitung-erfurt-wertschonende-pflege": "/oldtimer-aufbereitung-erfurt/",
    "leasing-rueckgabe-aufbereitung-erfurt": "/leasingrueckgabe-aufbereitung-erfurt/",
}

# Historische Root-Varianten von Blog-Slugs (aus GSC bzw. bisherigen Redirects)
BLOG_ROOT_ALIASES = [
    "adblue-deaktivieren-vor-nachteile-wahrheit",
    "auto-selber-waschen-erfurt",
    "adblue-deaktivierung",
    "lackierung-oldtimer-erfurt-lackaufbereitung-keramik",
    "leasing-rueckgabe-aufbereitung-erfurt",
    "oldtimer-aufbereitung-erfurt-wertschonende-pflege",
    "professionelle-keramikversiegelung-erfurt",
    "audi-r8-aufbereitung-erfurt-keramikversiegelung",
    "boot-aufbereitung-keramikversiegelung-marine",
    "harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung",
    "harte-und-weiche-autolacke-der-geheime-schlssel-zur-perfekten-lackaufbereitung-2",
    "keramik-fuer-auto-erfurt-vorteile-haltbarkeit",
    "professionelle-cabrioverdeck-impraegnierung-und-reinigung",
    "profi-keramikversiegelung",
    "motorwaesche-erfurt-vorteile-kosten",
]

# Einzelne Pfade
EXACT = {
    "/glanz-erfurt": "/keramikversiegelung/",
    "/glanz-erfurt/": "/keramikversiegelung/",
    "/glanz-erfurt/index.html": "/keramikversiegelung/",
    "/ads2": "/ads",
    "/ads2/": "/ads",
    "/ads2.html": "/ads",
    "/index.html": "/",
    "/blog/index.html": "/blog/",
    "/pages/kontakt.html": "/kontakt/",
    "/blog/wie-oft-auto-aufbereiten-lassen.html": "/blog/wie-oft-auto-aufbereiten-lassen/",
}


def blog_final(slug):
    return BLOG_MERGED.get(slug, "/blog/%s/" % slug)


def redirects():
    """Liste (source, destination) in Prioritätsreihenfolge, ohne Ketten."""
    out = []
    for src, dst in EXACT.items():
        out.append((src, dst))
    for slug in ROOT_PAGES:
        out.append(("/%s.html" % slug, "/%s/" % slug))
        out.append(("/landingpage/%s" % slug, "/%s/" % slug))
        out.append(("/landingpage/%s/(.*)" % slug, "/%s/" % slug))
    for slug in LEGACY_NOSLASH:
        for src in ("/%s/" % slug, "/%s.html" % slug, "/landingpage/%s" % slug, "/landingpage/%s/(.*)" % slug):
            out.append((src, "/%s" % slug))
    for slug, dst in OLD_ROOT_PAGES.items():
        for src in ("/%s" % slug, "/%s/" % slug, "/%s.html" % slug,
                    "/landingpage/%s" % slug, "/landingpage/%s/(.*)" % slug):
            out.append((src, dst))
    for slug, dst in BLOG_MERGED.items():
        out.append(("/blog/%s/" % slug, dst))
        out.append(("/blog/%s" % slug, dst))
    for slug in BLOG_ROOT_ALIASES:
        dst = blog_final(slug)
        out.append(("/%s/" % slug, dst))
        out.append(("/%s" % slug, dst))
    seen, uniq = set(), []
    for src, dst in out:
        if src in seen:
            continue
        seen.add(src)
        uniq.append((src, dst))
    return uniq


def resolve(path):
    """Interner Pfad -> finale URL (ohne Host). Unbekannte Pfade bleiben."""
    table = {s: d for s, d in redirects() if "(" not in s}
    if path in table:
        return table[path]
    bare = path.rstrip("/")
    if bare.lstrip("/") in LEGACY_NOSLASH:
        return bare
    if bare.lstrip("/") in ROOT_PAGES:
        return bare + "/"
    if path.startswith("/blog/") and not path.endswith("/") and "." not in path.rsplit("/", 1)[-1]:
        return path + "/"
    if path.startswith("/ratgeber/") and not path.endswith("/"):
        return path + "/"
    if path == "/blog":
        return "/blog/"
    return path
