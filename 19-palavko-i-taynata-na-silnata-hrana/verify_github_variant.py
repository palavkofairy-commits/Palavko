import re
from pathlib import Path


BASE = Path(__file__).resolve().parent
html = (BASE / "index.html").read_text(encoding="utf-8")
images = re.findall(r'<img src="([^"]+)"', html)
missing = [src for src in images if not (BASE / src).exists()]

print(f"images={len(images)}")
print(f"figures={html.count('<figure')}")
print(f"missing={missing}")
print(f"has_moral={'ПОУКА' in html}")
print(f"starts_with_image={'scene-01-breakfast-chocolate.png' in html[:2000]}")
