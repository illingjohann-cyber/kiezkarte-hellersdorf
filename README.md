# Kiezkarte Alte Hellersdorfer Straße

Interaktive Karte der Einrichtungen im Kiez (Quartiersmanagement Alte Hellersdorfer Straße):
**Freizeit & Kultur**, **Schulen** und **Kitas** – mit Filter-Buttons, Suche, Einrichtungsliste und Detail-Popups.

Technik: HTML, Tailwind CSS (CDN), JavaScript, Leaflet + OpenStreetMap (kein API-Key nötig).

## Starten
`index.html` im Browser öffnen oder lokal servieren: `python -m http.server`

## Daten
- `data/einrichtungen.json` / `data/einrichtungen.js` – Einrichtungen inkl. Koordinaten
- `tools/institutions.py` – Quelldaten aus der Excel-Liste (Stand 06.10.2026)
- `tools/geocode.py` – Adressen via Nominatim geocodieren

Änderungen: `institutions.py` anpassen, `python tools/geocode.py` ausführen, danach `einrichtungen.js` aus der JSON neu erzeugen.
