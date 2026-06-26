import base64
from pathlib import Path

BRAND = "⚡ Sub1Kore VPN"

cfg = Path("configs.txt")
lines = []
seen = set()

if cfg.exists():
    for l in cfg.read_text(encoding="utf-8").splitlines():
        l = l.strip()
        if not l or l in seen:
            continue

        seen.add(l)

        # اضافه کردن نام برند
        if "#" in l:
            link, name = l.rsplit("#", 1)

            if not name.startswith(BRAND):
                l = f"{link}#{BRAND} | {name}"

        lines.append(l)

import json
from datetime import datetime
from collections import Counter

protocols = Counter()
countries = Counter()

for config in configs:
    # پروتکل
    if "://" in config:
        protocol = config.split("://")[0].lower()
        protocols[protocol] += 1

    # کشور (از نام کانفیگ)
    if "#" in config:
        name = config.split("#", 1)[1]

        country_list = [
            "Germany",
            "France",
            "Netherlands",
            "Singapore",
            "Turkey",
            "Japan",
            "United States",
            "United Kingdom",
            "Finland",
            "Canada"
        ]

        for country in country_list:
            if country.lower() in name.lower():
                countries[country] += 1

stats = {
    "brand": "Sub1Kore VPN",
    "updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
    "total_configs": len(configs),
    "protocols": dict(protocols),
    "countries": dict(countries)
}

with open("stats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=4, ensure_ascii=False)

print("stats.json created")

# ذخیره خروجی
Path("sub.txt").write_text("\n".join(lines), encoding="utf-8")

Path("sub_base64.txt").write_text(
    base64.b64encode("\n".join(lines).encode()).decode(),
    encoding="utf-8"
)

print("Done")
