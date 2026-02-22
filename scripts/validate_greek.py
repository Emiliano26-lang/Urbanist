from fontTools.ttLib import TTFont
import sys

font = TTFont("fonts/Urbanist-Regular.ttf")
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
