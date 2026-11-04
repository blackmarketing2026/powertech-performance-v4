# Neue Seiten zur Fahrzeugaufbereitung – 04.11.2026

Ausgangsbasis ist der Search-Console-Webexport vom 03.08. bis 02.11.2026 (siehe `data-analysis.md`). „verkaufsaufbereitung“ hatte zwei Impressionen und keinen Klick; dies belegt weder das regionale Suchvolumen noch eine konkrete Seite als Ursache. Für Tierhaare, Gerüche und Firmenfahrzeuge sind die Zielbegriffe redaktionelle Hypothesen. Bestehende Autoaufbereitungs-, Innenreinigungs- und Leasingseiten sowie die bestehende Kosten- und Leasingberatung wurden berücksichtigt. Keine Aussage über Ranking-Kannibalisierung ohne Query-URL-Zeitreihen.

| Priorität | Neue URL und Suchintention | Abgrenzung und Fragen |
|---|---|---|
| P1 | `/blog/autoaufbereitung-vor-verkauf-erfurt/`: Auto vor Verkauf aufbereiten lassen | Der Verkaufsanlass ergänzt `/autoaufbereitung/` und die bestehende Leasingseite. H1: Autoaufbereitung vor dem Verkauf in Erfurt. H2: geeignete Arbeiten, Grenzen, Nutzen, Kosten und Anfrage. |
| P1 | `/blog/tierhaare-auto-entfernen-erfurt/`: Entfernung von Tierhaaren | Vertieft eine konkrete Innenraumfrage; `/innenraumreinigung-erfurt/` bleibt die allgemeine Leistungsseite. H2: betroffene Bereiche, Reinigung, Aufwand, Rückgabe. |
| P1 | `/blog/geruch-im-auto-innenraumreinigung-erfurt/`: Umgang mit Gerüchen | Vertieft Ursachen und mögliche Reinigung; keine pauschale Erfolgsgarantie. H2: Ursachen, Behandlung, Grenzen, Anfrage. |
| P2 | `/blog/firmenfahrzeuge-autoaufbereitung-erfurt/`: gewerbliche Anfrage für ein oder mehrere Fahrzeuge | Eigener Anwendungsfall mit individueller Abstimmung, ohne erfundene Verträge oder Sonderkonditionen. Nutzer bestätigte am 04.11.2026 Anfrage per Formular, Telefon oder WhatsApp und persönliches Gespräch mit Benjamin. H2: Arbeiten, Anlässe, Anfrage, Kontakt. |

Primäre Belege für Umfang und Grenzen sind die bestehenden Leistungsseiten `autoaufbereitung.html`, `innenraumreinigung-erfurt.html`, `lackaufbereitung-erfurt.html` und `leasingrueckgabe-aufbereitung-erfurt.html` sowie die Nutzerangabe zu Firmenfahrzeugen. Keine zusätzlichen Preise, Projekte oder Ergebnisgarantien erfunden.

Interne Links: Ratgeberübersicht `/blog/` auf alle vier neuen Artikel; `/autoaufbereitung/` mit den Ankern „Autoaufbereitung vor dem Verkauf“ und „Firmenfahrzeuge und Fuhrparks“ auf die entsprechenden Artikel; `/innenraumreinigung-erfurt/` mit „Tierhaare im Auto entfernen lassen“ und „Gerüche im Auto behandeln“ auf die anderen Artikel. Artikel verlinken kontextbezogen zu den vorhandenen Leistungs- und Kontaktseiten. Die Sitemap wird mit `python seo/tools/build-sitemap.py` erzeugt; die Blogpfade besitzen jeweils eine physische `index.html` und benötigen kein neues Rewrite.

Ein Vorher-nachher-Projekt ist noch nicht erstellt: Laut Nutzer liegen derzeit keine entsprechenden Fotos und Falldaten vor. Die historischen CSV-Maps sind nicht auf den Stand dieser Ergänzung regeneriert; diese Datei dokumentiert die neuen Zuordnungen. Nach Veröffentlichung Indexierung und organische Entwicklung prüfen; aktuelle Daten belegen noch keine Wirkung.
