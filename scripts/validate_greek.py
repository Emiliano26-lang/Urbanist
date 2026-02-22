import os, sys
from fontTools.ttLib import TTFont

search_dirs = ["fonts/ttf", "fonts/otf", "fonts/variable"]
font_path = None

for d in search_dirs:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        if f.startswith("Urbanist") and f.endswith((".ttf", ".otf")):
            font_path = os.path.join(d, f)
            break
    if font_path:
        break

if not font_path:
    print("❌ No Urbanist font found in:", search_dirs)
    sys.exit(1)

print(f"✅ Found font at {font_path}")
font = TTFont(font_path)

greek_ranges = [(0x0370, 0x03FF), (0x1F00, 0x1FFF)]
missing = []
for start, end in greek_ranges:
    for code in range(start, end+1):
        if code not in font.getBestCmap():
            missing.append(hex(code))

if missing:
    print("❌ Missing Greek glyphs:", missing)
    sys.exit(1)
else:
    print("✅ All Greek glyphs present.")
