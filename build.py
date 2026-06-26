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
from collections import Counter

stats = {
    "total": len(lines),
    "vless": 0,
    "vmess": 0,
    "trojan": 0,
    "shadowsocks": 0,
    "countries": {}
}

country_counter = Counter()

for config in lines:
    
    if config.startswith("vless://"):
        stats["vless"] += 1

    elif config.startswith("vmess://"):
        stats["vmess"] += 1

    elif config.startswith("trojan://"):
        stats["trojan"] += 1

    elif config.startswith("ss://"):
        stats["shadowsocks"] += 1

    # استخراج کشور از نام کانفیگ
    if "#" in config:
        name = config.split("#",1)[1]

        country_list = [
            "Germany",
            "France",
            "Singapore",
            "Turkey",
            "Netherlands",
            "Finland",
            "Japan",
            "United States",
            "Canada",
            "United Kingdom",
            "UAE"
        ]

        for country in country_list:
            if country.lower() in name.lower():
                country_counter[country] += 1
                break

stats["countries"] = dict(country_counter)

with open("stats.json","w",encoding="utf-8") as f:
    json.dump(stats,f,indent=4,ensure_ascii=False)

print("Stats generated.")

# ذخیره خروجی
Path("sub.txt").write_text("\n".join(lines), encoding="utf-8")

Path("sub_base64.txt").write_text(
    base64.b64encode("\n".join(lines).encode()).decode(),
    encoding="utf-8"
)

print("Done")
