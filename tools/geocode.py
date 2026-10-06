import json, time, urllib.parse, urllib.request, sys
sys.path.insert(0, __file__.rsplit("tools",1)[0] + "tools")
from institutions import I
out = []
for cat, name, traeger, adr, tel, mail, web in I:
    q = urllib.parse.urlencode({"q": adr, "format": "json", "limit": 1, "countrycodes": "de"})
    req = urllib.request.Request("https://nominatim.openstreetmap.org/search?" + q, headers={"User-Agent": "kiezkarte-hellersdorf/1.0 (illingjohann@gmail.com)"})
    r = json.load(urllib.request.urlopen(req))
    if not r:
        # Fallback: ohne PLZ
        q = urllib.parse.urlencode({"q": adr.split(",")[0] + ", Berlin Hellersdorf", "format": "json", "limit": 1})
        req = urllib.request.Request("https://nominatim.openstreetmap.org/search?" + q, headers={"User-Agent": "kiezkarte-hellersdorf/1.0"})
        r = json.load(urllib.request.urlopen(req))
    lat, lng = (float(r[0]["lat"]), float(r[0]["lon"])) if r else (None, None)
    print("OK " if r else "MISS", name, lat, lng)
    out.append(dict(id=len(out)+1, kategorie=cat, name=name, traeger=traeger, adresse=adr, telefon=tel, email=mail, web=web, lat=lat, lng=lng))
    time.sleep(1.2)
json.dump(out, open("data/einrichtungen.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
