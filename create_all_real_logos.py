import os
from PIL import Image, ImageDraw

icons_dir = os.path.join(os.path.dirname(__file__), "assets", "icons")
os.makedirs(icons_dir, exist_ok=True)

size = 256

# 1. Official YouTube Logo
yt_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
yt_draw = ImageDraw.Draw(yt_img)
# Red rounded rectangle (#FF0000)
yt_draw.rounded_rectangle([16, 48, 240, 208], radius=44, fill=(255, 0, 0, 255))
# White play triangle
yt_draw.polygon([(104, 96), (104, 160), (168, 128)], fill=(255, 255, 255, 255))
yt_img.resize((128, 128), Image.Resampling.LANCZOS).save(os.path.join(icons_dir, "youtube.png"))

# 2. Official Facebook Logo
fb_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
fb_draw = ImageDraw.Draw(fb_img)
fb_blue = (24, 119, 242, 255)
fb_draw.ellipse([8, 8, 248, 248], fill=fb_blue)
# White 'f'
fb_draw.rectangle([138, 98, 170, 248], fill=(255, 255, 255))
fb_draw.rectangle([105, 120, 195, 146], fill=(255, 255, 255))
fb_draw.arc([102, 40, 170, 120], start=270, end=360, fill=(255, 255, 255), width=32)
fb_img.resize((128, 128), Image.Resampling.LANCZOS).save(os.path.join(icons_dir, "facebook.png"))

# 3. Official Instagram Logo (Gradient + White Camera)
ig_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
ig_draw = ImageDraw.Draw(ig_img)
# Instagram Gradient background
for y in range(size):
    r = int(131 + (225 - 131) * (y / size))
    g = int(58 + (48 - 58) * (y / size))
    b = int(180 + (108 - 180) * (y / size))
    ig_draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

# Mask with rounded rect
mask = Image.new("L", (size, size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rounded_rectangle([12, 12, 244, 244], radius=56, fill=255)

ig_final = Image.new("RGBA", (size, size), (0, 0, 0, 0))
ig_final.paste(ig_img, (0, 0), mask=mask)
ig_draw_final = ImageDraw.Draw(ig_final)
# Camera box
ig_draw_final.rounded_rectangle([52, 52, 204, 204], radius=42, outline=(255, 255, 255), width=16)
# Lens
ig_draw_final.ellipse([92, 92, 164, 164], outline=(255, 255, 255), width=14)
# Flash
ig_draw_final.ellipse([168, 76, 184, 92], fill=(255, 255, 255))
ig_final.resize((128, 128), Image.Resampling.LANCZOS).save(os.path.join(icons_dir, "instagram.png"))

# 4. Official Twitter / X Logo
x_img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
x_draw = ImageDraw.Draw(x_img)
x_draw.ellipse([8, 8, 248, 248], fill=(15, 20, 25, 255))
x_draw.line([(68, 68), (188, 188)], fill=(255, 255, 255), width=24)
x_draw.line([(188, 68), (68, 188)], fill=(255, 255, 255), width=24)
x_img.resize((128, 128), Image.Resampling.LANCZOS).save(os.path.join(icons_dir, "twitter.png"))

print("All 4 official platform PNG logos generated successfully!")
