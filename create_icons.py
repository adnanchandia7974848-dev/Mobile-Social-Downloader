import os
from PIL import Image, ImageDraw, ImageFont

icons_dir = os.path.join(os.path.dirname(__file__), "assets", "icons")
os.makedirs(icons_dir, exist_ok=True)

def create_circle_icon(bg_color, draw_func, filename):
    size = (128, 128)
    img = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Outer circle background
    draw.ellipse([4, 4, 124, 124], fill=bg_color)
    
    draw_func(draw)
    
    filepath = os.path.join(icons_dir, filename)
    img.save(filepath, "PNG")
    print(f"Saved {filepath}")

# 1. YouTube Icon (Red circle with white play triangle)
def draw_yt(draw):
    # Rounded rect background or play symbol
    draw.rounded_rectangle([32, 40, 96, 88], radius=14, fill=(255, 255, 255))
    draw.polygon([(52, 48), (52, 80), (80, 64)], fill=(230, 33, 23))

create_circle_icon((230, 33, 23, 255), draw_yt, "youtube.png")

# 2. Facebook Icon (Blue circle with white 'f')
def draw_fb(draw):
    # White 'f' shape
    draw.rectangle([68, 30, 84, 105], fill=(255, 255, 255))
    draw.rectangle([50, 48, 84, 64], fill=(255, 255, 255))
    draw.arc([52, 30, 84, 62], start=180, end=270, fill=(255, 255, 255), width=16)

create_circle_icon((24, 119, 242, 255), draw_fb, "facebook.png")

# 3. Instagram Icon (Gradient/Purple circle with camera outline)
def draw_ig(draw):
    # Camera box outline
    draw.rounded_rectangle([34, 34, 94, 94], radius=16, outline=(255, 255, 255), width=8)
    # Lens circle
    draw.ellipse([50, 50, 78, 78], outline=(255, 255, 255), width=7)
    # Flash dot
    draw.ellipse([76, 42, 84, 50], fill=(255, 255, 255))

create_circle_icon((225, 48, 108, 255), draw_ig, "instagram.png")

# 4. Twitter / X Icon (Dark cyan circle with 'X')
def draw_x(draw):
    draw.line([(38, 38), (90, 90)], fill=(255, 255, 255), width=12)
    draw.line([(90, 38), (38, 90)], fill=(255, 255, 255), width=12)

create_circle_icon((18, 165, 214, 255), draw_x, "twitter.png")

print("All platform logo PNG icons generated successfully!")
