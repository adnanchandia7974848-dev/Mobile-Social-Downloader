import os
from PIL import Image, ImageDraw, ImageFont

icons_dir = os.path.join(os.path.dirname(__file__), "assets", "icons")
os.makedirs(icons_dir, exist_ok=True)

size = 512
img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Outer rounded rectangle with vibrant gradient (Dark Slate to Deep Indigo)
for y in range(size):
    r = int(15 + (30 - 15) * (y / size))
    g = int(23 + (41 - 23) * (y / size))
    b = int(42 + (70 - 42) * (y / size))
    draw.line([(0, y), (size, y)], fill=(r, g, b, 255))

mask = Image.new("L", (size, size), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rounded_rectangle([16, 16, 496, 496], radius=110, fill=255)

app_icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
app_icon.paste(img, (0, 0), mask=mask)
app_draw = ImageDraw.Draw(app_icon)

# Subtle glowing border
app_draw.rounded_rectangle([18, 18, 494, 494], radius=108, outline=(14, 165, 233, 200), width=6)

# Outer Media Ring (Cyan / Blue Gradient accent)
app_draw.ellipse([110, 110, 402, 402], outline=(14, 165, 233, 255), width=18)

# Download Arrow (White / Bright Gradient)
# Arrow Shaft
app_draw.rounded_rectangle([232, 160, 280, 310], radius=12, fill=(255, 255, 255, 255))
# Arrow Point
app_draw.polygon([(180, 290), (332, 290), (256, 370)], fill=(255, 255, 255, 255))

# 4 Accent Dots around the ring representing YouTube, Facebook, Instagram, Twitter
# Top-Left: Red (YouTube)
app_draw.ellipse([88, 88, 128, 128], fill=(239, 68, 68, 255))
# Top-Right: Blue (Facebook)
app_draw.ellipse([384, 88, 424, 128], fill=(59, 130, 246, 255))
# Bottom-Left: Pink (Instagram)
app_draw.ellipse([88, 384, 128, 424], fill=(236, 72, 153, 255))
# Bottom-Right: Cyan (Twitter/X)
app_draw.ellipse([384, 384, 424, 424], fill=(6, 182, 212, 255))

# Save high-res 512x512 app logo
app_icon_path = os.path.join(icons_dir, "app_icon.png")
app_icon.save(app_icon_path, "PNG")

# Also save 128x128 version
app_icon_128 = app_icon.resize((128, 128), Image.Resampling.LANCZOS)
app_icon_128.save(os.path.join(icons_dir, "app_icon_128.png"), "PNG")

print(f"App Main Logo created successfully at: {app_icon_path}")
