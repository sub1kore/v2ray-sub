import base64
from pathlib import Path
cfg=Path("configs.txt")
lines=[]
seen=set()
if cfg.exists():
    for l in cfg.read_text(encoding="utf-8").splitlines():
        l=l.strip()
        if l and l not in seen:
            seen.add(l); lines.append(l)
Path("sub.txt").write_text("\n".join(lines),encoding="utf-8")
Path("sub_base64.txt").write_text(base64.b64encode("\n".join(lines).encode()).decode(),encoding="utf-8")
print("Done")
