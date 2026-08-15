
from PIL import Image, ImageDraw, ImageFont
import os
import math

def generate_cover_correct(bg_color, pizza_color, crust_color, accent_color, subtitle_color, 
                           middle_color, volume_num, chapters, middle_text_lines, 
                           top_text_line1, top_text_line2, filename):
    width, height = 1200, 1800
    white = (255, 255, 255)
    
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    try:
        font_top = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 80)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf", 42)
        font_volume = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
        font_chapters = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 34)
        font_middle = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 38)
        font_author = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 44)
    except:
        font_top = font_title = font_subtitle = font_volume = font_chapters = font_middle = font_author = ImageFont.load_default()
    
    # Top text
    bbox = draw.textbbox((0, 0), top_text_line1, font=font_top)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) // 2, 75), top_text_line1, fill=(210, 195, 175), font=font_top)
    
    bbox = draw.textbbox((0, 0), top_text_line2, font=font_top)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) // 2, 105), top_text_line2, fill=(210, 195, 175), font=font_top)
    
    # === PIZZA SLICE (Sector: arc on top, point at bottom) ===
    cx, cy = width // 2, 720  # center (vertex/point) of sector
    r_pizza = 320
    r_crust = 345
    start_angle = 225
    end_angle = 315
    cap_radius = 16
    
    # 1. Crust: outer sector
    draw.pieslice(
        [cx - r_crust, cy - r_crust, cx + r_crust, cy + r_crust],
        start=start_angle, end=end_angle, fill=crust_color
    )
    
    # 2. Pizza body: inner sector
    draw.pieslice(
        [cx - r_pizza, cy - r_pizza, cx + r_pizza, cy + r_pizza],
        start=start_angle, end=end_angle, fill=pizza_color
    )
    
    # 3. End caps (rounded corners on crust endpoints)
    for angle in [start_angle, end_angle]:
        rad = math.radians(angle)
        cap_x = cx + r_crust * math.cos(rad)
        cap_y = cy + r_crust * math.sin(rad)
        draw.ellipse(
            [cap_x - cap_radius, cap_y - cap_radius,
             cap_x + cap_radius, cap_y + cap_radius],
            fill=crust_color
        )
    
    # 4. Pepperoni (small dark circles on pizza body)
    # Positioned within the sector area
    pepperoni = [
        (cx - 70, cy - 160, 30),
        (cx + 60, cy - 140, 28),
        (cx - 10, cy - 220, 32),
        (cx + 80, cy - 200, 26),
        (cx - 90, cy - 100, 24),
    ]
    for px, py, pr in pepperoni:
        draw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=bg_color)
    
    # Title
    y_title = 820
    for line in ["Mastering Ontology", "Engineering"]:
        bbox = draw.textbbox((0, 0), line, font=font_title)
        text_w = bbox[2] - bbox[0]
        draw.text(((width - text_w) // 2, y_title), line, fill=white, font=font_title)
        y_title += 100
    
    # Subtitle
    subtitle = "with Protégé and Pizza.owl"
    bbox = draw.textbbox((0, 0), subtitle, font=font_subtitle)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) // 2, 1030), subtitle, fill=subtitle_color, font=font_subtitle)
    
    # Line
    draw.line([(width//2 - 160, 1110), (width//2 + 160, 1110)], fill=accent_color, width=3)
    
    # Volume
    volume_text = f"VOLUME {volume_num}"
    bbox = draw.textbbox((0, 0), volume_text, font=font_volume)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) // 2, 1160), volume_text, fill=accent_color, font=font_volume)
    
    # Chapters
    bbox = draw.textbbox((0, 0), chapters, font=font_chapters)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) // 2, 1240), chapters, fill=white, font=font_chapters)
    
    # Middle text
    y_mid = 1420
    for line in middle_text_lines:
        bbox = draw.textbbox((0, 0), line, font=font_middle)
        text_w = bbox[2] - bbox[0]
        draw.text(((width - text_w) // 2, y_mid), line, fill=middle_color, font=font_middle)
        y_mid += 55
    
    # Author
    author_text = "XIAOQI ZHAO"
    bbox = draw.textbbox((0, 0), author_text, font=font_author)
    text_w = bbox[2] - bbox[0]
    draw.text(((width - text_w) // 2, 1620), author_text, fill=white, font=font_author)
    
    # Border frame
    frame_color = tuple(min(255, c + 30) for c in bg_color)
    draw.rectangle([35, 35, width-35, height-35], outline=frame_color, width=2)
    
    png_path = f"/mnt/agents/output/{filename}.png"
    pdf_path = f"/mnt/agents/output/{filename}.pdf"
    img.save(png_path, "PNG")
    img.save(pdf_path, "PDF", resolution=300.0)
    print(f"Saved: {png_path} ({os.path.getsize(png_path)} bytes)")
    print(f"Saved: {pdf_path} ({os.path.getsize(pdf_path)} bytes)")
    return img

# Volume 1 - Green scheme
v1 = generate_cover_correct(
    bg_color=(18, 45, 38),
    pizza_color=(46, 139, 87),
    crust_color=(200, 230, 210),
    accent_color=(46, 139, 87),
    subtitle_color=(144, 238, 144),
    middle_color=(160, 190, 175),
    volume_num="1",
    chapters="Chapters 00-08",
    middle_text_lines=["Ontology Foundations in", "Protégé"],
    top_text_line1="From Semantic Foundations to",
    top_text_line2="Executable Knowledge Architecture (EKA)",
    filename="cover_volume1"
)

# Volume 2 - Blue scheme
v2 = generate_cover_correct(
    bg_color=(26, 39, 68),
    pizza_color=(74, 144, 217),
    crust_color=(200, 220, 240),
    accent_color=(74, 144, 217),
    subtitle_color=(150, 200, 240),
    middle_color=(170, 190, 210),
    volume_num="2",
    chapters="Chapters 09-13",
    middle_text_lines=["Object Properties &", "Relationships"],
    top_text_line1="From Semantic Foundations to",
    top_text_line2="Executable Knowledge Architecture (EKA)",
    filename="cover_volume2"
)

# Volume 3 - Purple scheme
v3 = generate_cover_correct(
    bg_color=(45, 31, 74),
    pizza_color=(139, 127, 217),
    crust_color=(210, 200, 230),
    accent_color=(139, 127, 217),
    subtitle_color=(180, 170, 220),
    middle_color=(190, 180, 210),
    volume_num="3",
    chapters="Chapters 14-16",
    middle_text_lines=["Semantic Requirements & EKA", "Governance"],
    top_text_line1="From Semantic Foundations to",
    top_text_line2="Executable Knowledge Architecture (EKA)",
    filename="cover_volume3"
)

# Volume 4 - Brown/Orange scheme
v4 = generate_cover_correct(
    bg_color=(61, 43, 31),
    pizza_color=(230, 150, 80),
    crust_color=(220, 190, 150),
    accent_color=(230, 150, 80),
    subtitle_color=(220, 180, 140),
    middle_color=(200, 175, 145),
    volume_num="4",
    chapters="Chapters 17-24",
    middle_text_lines=["SKDL — Semantic Knowledge", "Development Lifecycle"],
    top_text_line1="From Semantic Foundations to",
    top_text_line2="Executable Knowledge Architecture (EKA)",
    filename="cover_volume4"
)

print("\nAll 4 covers regenerated with correct sector pizza!")
