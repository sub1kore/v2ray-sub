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

# ذخیره خروجی
Path("sub.txt").write_text("\n".join(lines), encoding="utf-8")

Path("sub_base64.txt").write_text(
    base64.b64encode("\n".join(lines).encode()).decode(),
    encoding="utf-8"
)

print("Done")
