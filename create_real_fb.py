import os
from PIL import Image, ImageDraw, ImageFont

icons_dir = os.path.join(os.path.dirname(__file__), "assets", "icons")
os.makedirs(icons_dir, exist_ok=True)

# High-res 256x256 image for anti-aliasing
size = 256
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Official Facebook Blue Circle (#1877F2)
fb_blue = (24, 119, 242, 255)
draw.ellipse([8, 8, 248, 248], fill=fb_blue)

# Official White 'f'
# Right leg of f from x=136 to 172, from y=90 to 248
draw.rectangle([138, 98, 170, 248], fill=(255, 255, 255))

# Crossbar of f at y=120 to 146, x=105 to 195
draw.rectangle([105, 120, 195, 146], fill=(255, 255, 255))

# Top arch of f
draw.arc([102, 40, 170, 120], start=270, end=360, fill=(255, 255, 255), width=32)

# Smooth downscaling to 128x128 with Lanczos
img_resized = img.resize((128, 128), Image.Resampling.LANCZOS)
fb_path = os.path.join(icons_dir, "facebook.png")
img_resized.save(fb_path, "PNG")
print(f"Saved authentic Facebook logo to {fb_path}")
