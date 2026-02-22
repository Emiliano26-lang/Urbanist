import os, sys
from fontTools.ttLib import TTFont

possible_paths = [
    "fonts/ttf/Urbanist-Regular.ttf",
    "fonts/otf/Urbanist-Black.otf",
    "fonts/variable/Urbanist[wght].ttf"
]

font_path = None
for path in possible_paths:
    if os.path.exists(path):
        font_path = path
        break

if not font_path:
    print("❌ No built font found in expected paths:", possible_paths)
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
