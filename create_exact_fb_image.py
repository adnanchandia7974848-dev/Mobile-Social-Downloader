import os
from PIL import Image, ImageDraw

icons_dir = os.path.join(os.path.dirname(__file__), "assets", "icons")
os.makedirs(icons_dir, exist_ok=True)

size = 256
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Official Facebook Blue Circle
fb_blue = (24, 119, 242, 255)
draw.ellipse([6, 6, 250, 250], fill=fb_blue)

# White 'f' exact alignment matching user image:
# 1. Vertical main stem (down to bottom edge)
draw.rectangle([112, 94, 146, 250], fill=(255, 255, 255, 255))

# 2. Horizontal crossbar
draw.rectangle([88, 124, 160, 152], fill=(255, 255, 255, 255))

# 3. Top curved arch
draw.arc([112, 54, 160, 124], start=270, end=360, fill=(255, 255, 255, 255), width=34)

# Smooth resize to 128x128
img_resized = img.resize((128, 128), Image.Resampling.LANCZOS)
fb_path = os.path.join(icons_dir, "facebook.png")
img_resized.save(fb_path, "PNG")
print(f"Saved exact Facebook logo image to {fb_path}")
