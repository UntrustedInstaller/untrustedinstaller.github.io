#!/usr/bin/env python3
"""Generate the SYSTEM_PORTAL 88x31 badge GIFs and the favicon.

Outputs to img/ (badges) and favicon.ico.
All images are small palette GIFs/ICOs so they load fine on IE 5.5.
Run: python3 make-badges.py
"""

from PIL import Image, ImageDraw, ImageFont

FONT_B = "/usr/share/fonts/liberation/LiberationSans-Bold.ttf"
FONT_M = "/usr/share/fonts/liberation/LiberationMono-Bold.ttf"

W, H = 88, 31


def new_canvas():
    img = Image.new("P", (W, H))
    pal = []
    # fixed palette: append colours as needed
    img.info["transparency"] = None
    return img


def save(img, name):
    img = img.convert("RGB").quantize(colors=16, method=Image.MEDIANCUT)
    img.save(name, optimize=True)


def badge_center(lines, font_path, fg, bg, border):
    """Solid background badge with centred multi-line text."""
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline=border, width=2)
    f = ImageFont.truetype(font_path, 13)
    sizes = [d.textbbox((0, 0), t, font=f) for t in lines]
    widths = [b[2] - b[0] for b in sizes]
    heights = [b[3] - b[1] for b in sizes]
    total_h = sum(heights) + 2 * (len(lines) - 1)
    y = (H - total_h) / 2
    for t, (bb, w, h) in zip(lines, zip(sizes, widths, heights)):
        x = (W - w) / 2
        d.text((x - bb[0], y - bb[1]), t, font=f, fill=fg)
        y += h + 2
    return img


def badge_html401():
    """Classic look: dark blue banner, gold text border."""
    img = Image.new("RGB", (W, H), "#000033")
    d = ImageDraw.Draw(img)
    # gold frame with dark inset line
    d.rectangle([0, 0, W - 1, H - 1], outline="#cc9900")
    d.rectangle([2, 2, W - 3, H - 3], outline="#006666")
    f = ImageFont.truetype(FONT_B, 13)
    t1, t2 = "HTML", "4.01"
    b1 = d.textbbox((0, 0), "HTML", font=f)
    b2 = d.textbbox((0, 0), "4.01", font=f)
    w1, h1 = b1[2] - b1[0], b1[3] - b1[1]
    w2, h2 = b2[2] - b2[0], b2[3] - b2[1]
    y = 4
    d.text(((W - w1) / 2 - b1[0], y - b1[1]), t1, font=f, fill="#ffffff")
    y += h1 + 1
    d.text(((W - w2) / 2 - b2[0], y - b2[1]), t2, font=f, fill="#ffcc00")
    return img


def badge_800x600():
    """White/blue classic 'Best viewed at 800x600'."""
    img = Image.new("RGB", (W, H), "#ffffff")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline="#000066", width=2)
    f = ImageFont.truetype(FONT_B, 11)
    t1, t2 = "BEST VIEWED", "800 x 600"
    b1 = d.textbbox((0, 0), t1, font=f)
    b2 = d.textbbox((0, 0), t2, font=f)
    y = 5
    d.text(((W - (b1[2] - b1[0])) / 2 - b1[0], y - b1[1]), t1, font=f, fill="#000066")
    y += (b1[3] - b1[1]) + 2
    d.text(((W - (b2[2] - b2[0])) / 2 - b2[0], y - b2[1]), t2, font=f, fill="#cc0000")
    return img


def badge_nojs():
    """Black terminal-style 'NO JAVASCRIPT'."""
    img = Image.new("RGB", (W, H), "#000000")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W - 1, H - 1], outline="#00ff00")
    f = ImageFont.truetype(FONT_M, 11)
    t1, t2 = "NO", "JAVASCRIPT"
    b1 = d.textbbox((0, 0), t1, font=f)
    b2 = d.textbbox((0, 0), t2, font=f)
    y = 6
    d.text(((W - (b1[2] - b1[0])) / 2 - b1[0], y - b1[1]), t1, font=f, fill="#ffffff")
    y += (b1[3] - b1[1]) + 2
    d.text(((W - (b2[2] - b2[0])) / 2 - b2[0], y - b2[1]), t2, font=f, fill="#00ff00")
    return img


def make_favicon():
    """16x16 favicon: navy square, teal 'S'."""
    img = Image.new("RGB", (16, 16), "#000033")
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 15, 15], outline="#66cccc")
    f = ImageFont.truetype(FONT_M, 12)
    b = d.textbbox((0, 0), "S", font=f)
    w, h = b[2] - b[0], b[3] - b[1]
    d.text(((16 - w) / 2 - b[0], (16 - h) / 2 - b[1]), "S", font=f, fill="#00cccc")
    # upscale for a crisp 32px variant
    big = img.resize((32, 32), Image.NEAREST)
    big.save("favicon.ico", sizes=[(16, 16), (32, 32)])
    img.save("favicon-16.png")
    big.save("favicon-32.png")
    return img


if __name__ == "__main__":
    import os
    os.makedirs("img", exist_ok=True)
    save(badge_html401(), "img/badge-html401.gif")
    save(badge_800x600(), "img/badge-800x600.gif")
    save(badge_nojs(), "img/badge-nojs.gif")
    make_favicon()
    print("done: img/badge-*.gif, favicon.ico")