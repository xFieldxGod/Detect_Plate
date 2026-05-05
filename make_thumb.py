# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 498, 176
img = Image.new("RGB", (W, H), (15, 20, 30))
draw = ImageDraw.Draw(img)

# Dark gradient background
for y in range(H):
    t = y / H
    draw.line([(0, y), (W, y)], fill=(int(15+t*8), int(20+t*15), int(30+t*25)))

# --- Camera panel (left) ---
cam_x, cam_y, cam_w, cam_h = 10, 10, 295, 156
draw.rectangle([cam_x, cam_y, cam_x+cam_w, cam_y+cam_h],
               fill=(20, 25, 40), outline=(50, 65, 85), width=1)

# Paste real plate image
import glob as _glob
_plates = _glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                  "saved_plates", "*.jpg"))
plate_path = _plates[0] if _plates else ""
if os.path.exists(plate_path):
    plate = Image.open(plate_path).convert("RGB")
    pw, ph = 220, 80
    plate = plate.resize((pw, ph), Image.LANCZOS)
    px, py = cam_x + (cam_w - pw) // 2, cam_y + (cam_h - ph) // 2 - 10
    img.paste(plate, (px, py))
    # Detection box (blue-orange)
    draw.rectangle([px-3, py-3, px+pw+3, py+ph+3], outline=(0, 165, 255), width=3)
    # Corner brackets
    for cx, cy in [(px-3, py-3), (px+pw+3, py-3),
                   (px-3, py+ph+3), (px+pw+3, py+ph+3)]:
        sx = -1 if cx < px else 1
        sy = -1 if cy < py else 1
        draw.line([(cx, cy), (cx+sx*14, cy)], fill=(0, 220, 255), width=2)
        draw.line([(cx, cy), (cx, cy+sy*14)], fill=(0, 220, 255), width=2)

# Status bar
draw.rectangle([cam_x, cam_y+cam_h-24, cam_x+cam_w, cam_y+cam_h],
               fill=(0, 110, 190))

try:
    font_sm = ImageFont.truetype("C:/Windows/Fonts/Calibri.ttf", 14)
    font_md = ImageFont.truetype("C:/Windows/Fonts/Calibrib.ttf", 16)
    font_lg = ImageFont.truetype("C:/Windows/Fonts/Calibrib.ttf", 22)
    font_thai = ImageFont.truetype("C:/Windows/Fonts/LEELAWAD.TTF", 14)
except Exception:
    font_sm = font_md = font_lg = font_thai = ImageFont.load_default()

draw.text((cam_x+8, cam_y+cam_h-20), "Confirmed: กจ 3046", font=font_thai, fill=(255, 255, 255))

# --- Right info panel ---
rx = cam_x + cam_w + 16
draw.text((rx, 12), "License Plate", font=font_sm, fill=(0, 180, 255))
draw.text((rx, 28), "Recognition", font=font_lg, fill=(255, 255, 255))

# Tags
tags = ["YOLOv8", "EasyOCR", "Python", "OpenCV"]
tx, ty = rx, 68
for tag in tags:
    bb = draw.textbbox((0, 0), tag, font=font_sm)
    tw = bb[2] - bb[0] + 10
    if tx + tw > W - 5:
        tx = rx
        ty += 22
    draw.rounded_rectangle([tx, ty, tx+tw, ty+18], radius=3,
                            fill=(25, 45, 75), outline=(50, 100, 150))
    draw.text((tx+5, ty+2), tag, font=font_sm, fill=(140, 195, 255))
    tx += tw + 5

# Confidence bar
bx, by = rx, 110
draw.text((bx, by), "Confidence", font=font_sm, fill=(100, 120, 150))
draw.rectangle([bx, by+17, bx+148, by+27], fill=(35, 45, 65))
draw.rounded_rectangle([bx, by+17, bx+133, by+27], radius=3, fill=(0, 155, 230))
draw.text((bx+152, by+14), "90%", font=font_sm, fill=(0, 200, 255))

# Scan line animation effect
for i in range(3):
    y_line = cam_y + 30 + i * 45
    for x in range(cam_x+5, cam_x+cam_w-5):
        alpha = max(0, 40 - abs(x - (cam_x + cam_w//2)) // 3)
        # skip for simplicity, just draw subtle line
    draw.line([(cam_x+5, y_line), (cam_x+cam_w-5, y_line)],
              fill=(0, 180, 255, 30), width=1)

img.save("thumbnail.png")
