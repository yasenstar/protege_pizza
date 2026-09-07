import math
from PIL import Image, ImageDraw, ImageFont

def lighten_color(hex_color, factor=0.5):
    r = int(int(hex_color[1:3], 16) + (255 - int(hex_color[1:3], 16)) * factor)
    g = int(int(hex_color[3:5], 16) + (255 - int(hex_color[3:5], 16)) * factor)
    b = int(int(hex_color[5:7], 16) + (255 - int(hex_color[5:7], 16)) * factor)
    return (r, g, b)

def draw_pizza_slice(draw, cx, cy, size, slice_color, crust_color, bg_color_hex):
    bg_color = tuple(int(bg_color_hex[i:i+2], 16) for i in (1, 3, 5))

    angle_span = 120
    angle_start = -90 - angle_span // 2   # -150
    angle_end   = -90 + angle_span // 2   # -30

    # Slice body polygon
    arc_points = []
    r = size
    steps = 50
    for i in range(steps + 1):
        angle = math.radians(angle_start + (angle_end - angle_start) * i / steps)
        arc_points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    arc_points.append((cx, cy + size * 1.15))  # tip
    draw.polygon(arc_points, fill=slice_color)

    # Crust arc
    crust_r = size + 5
    crust_thickness = 20
    for i in range(steps + 1):
        angle = math.radians(angle_start + (angle_end - angle_start) * i / steps)
        x = cx + crust_r * math.cos(angle)
        y = cy + crust_r * math.sin(angle)
        draw.ellipse([x - crust_thickness//2, y - crust_thickness//2,
                      x + crust_thickness//2, y + crust_thickness//2], fill=crust_color)

    # Crust end bumps
    for angle_deg in [angle_start, angle_end]:
        angle = math.radians(angle_deg)
        x = cx + crust_r * math.cos(angle)
        y = cy + crust_r * math.sin(angle)
        bump_r = 14
        draw.ellipse([x - bump_r, y - bump_r, x + bump_r, y + bump_r], fill=crust_color)

    # Pepperoni (background-colored circles)
    pepperoni = [
        (cx - 5,  cy - 10, 24),   # top center
        (cx - 40, cy + 30, 20),   # left
        (cx + 35, cy + 25, 22),   # right
        (cx + 15, cy + 65, 18),   # lower right
        (cx - 25, cy + 70, 16),   # lower left (bitten)
    ]
    for i, (px, py, pr) in enumerate(pepperoni):
        if i == 4:  # bitten
            draw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=bg_color)
            bite_r = int(pr * 0.6)
            bite_x = px - int(pr * 0.35)
            bite_y = py + int(pr * 0.3)
            draw.ellipse([bite_x - bite_r, bite_y - bite_r,
                          bite_x + bite_r, bite_y + bite_r], fill=slice_color)
        else:
            draw.ellipse([px - pr, py - pr, px + pr, py + pr], fill=bg_color)

def create_single_cover(vol_num, bg_hex, accent_hex, accent_light_hex, subtitle_text):
    W, H = 1600, 2560
    bg_color = tuple(int(bg_hex[i:i+2], 16) for i in (1, 3, 5))
    accent_color = tuple(int(accent_hex[i:i+2], 16) for i in (1, 3, 5))
    accent_light = tuple(int(accent_light_hex[i:i+2], 16) for i in (1, 3, 5))
    
    img = Image.new("RGB", (W, H), bg_color)
    draw = ImageDraw.Draw(img)
    
    # 1. Frame border (50% opacity approximation by blending with bg)
    border_color = accent_color # simplified for solid draw or RGBA if needed
    draw.rectangle([45, 45, 1555, 2515], outline=border_color, width=2)
    
    # Fonts (Fallback to default or system TTF if available)
    try:
        font_eyebrow = ImageFont.truetype("DejaVuSans.ttf", 34)
        font_title = ImageFont.truetype("DejaVuSerif-Bold.ttf", 112)
        font_sub = ImageFont.truetype("DejaVuSans-Oblique.ttf", 54)
        font_vol = ImageFont.truetype("DejaVuSans-Bold.ttf", 74)
        font_body = ImageFont.truetype("DejaVuSans.ttf", 46)
        font_author = ImageFont.truetype("DejaVuSans-Bold.ttf", 50)
    except:
        font_eyebrow = font_title = font_sub = font_vol = font_body = font_author = ImageFont.load_default()

    # 2. Eyebrow text
    draw.text((W/2, 85), "From Semantic Foundations to", fill=accent_light, anchor="mt", font=font_eyebrow)
    draw.text((W/2, 129), "Executable Knowledge Architecture (EKA)", fill=accent_light, anchor="mt", font=font_eyebrow)
    
    # 3. Pizza Slice Logo
    crust_color = lighten_color(accent_hex, 0.5)
    draw_pizza_slice(draw, cx=800, cy=460, size=185, slice_color=accent_color, crust_color=crust_color, bg_color_hex=bg_hex)
    
    # 4. Main Title
    draw.text((W/2, 920), "Mastering Ontology", fill="#FFFFFF", anchor="mt", font=font_title)
    draw.text((W/2, 1040), "Engineering", fill="#FFFFFF", anchor="mt", font=font_title)
    
    # 5. Subtitle
    draw.text((W/2, 1180), "with Protégé and Pizza.owl", fill=accent_color, anchor="mt", font=font_sub)
    
    # 6. Horizontal Divider
    draw.line([(600, 1260), (1000, 1260)], fill=accent_color, width=3)
    
    # 7. Volume Label
    draw.text((W/2, 1320), f"VOLUME {vol_num}", fill=accent_color, anchor="mt", font=font_vol)
    
    # 9. Bottom Subtitle
    draw.text((W/2, 1750), subtitle_text[0], fill=accent_light, anchor="mt", font=font_body)
    draw.text((W/2, 1812), subtitle_text[1], fill=accent_light, anchor="mt", font=font_body)
    
    # 10. Author Name
    draw.text((W/2, 2340), "XIAOQI ZHAO", fill="#FFFFFF", anchor="mt", font=font_author)
    
    return img

def generate_table_promotion_banner():
    # Volume metadata based on prompt
    volumes_data = [
        (1, "#0B2E28", "#1D9E75", "#9FE1CB", ("Ontology Foundation", "in Protégé")),
        (2, "#0A2138", "#378ADD", "#B5D4F4", ("Object Properties &", "Relationships")),
        (3, "#211A3D", "#7F77DD", "#CECBF6", ("Semantic Requirements &", "EKA Governance")),
        (4, "#2D1F0B", "#E8913A", "#F5D0A0", ("SKDL — Semantic Knowledge", "Development Lifecycle")),
        (5, "#1E293B", "#38BDF8", "#BAE6FD", ("Data Properties, Custom UI,", "and Graph Ecosystems")),
        (6, "#18222A", "#64748B", "#CBD5E1", ("Advanced Reasoning, Constraints,", "and Interdisciplinary Depth")),
        (7, "#1C0A0A", "#E11D48", "#FDA4AF", ("EKA Practices & The SKDL", "Methodology Package")),
    ]
    
    covers = []
    for vol_num, bg, accent, accent_light, sub in volumes_data:
        covers.append(create_single_cover(vol_num, bg, accent, accent_light, sub))
        
    # Create a grand promotion banner where all 7 volumes are laid out on a virtual table
    # Banner dimensions: 7 books side-by-side with padding + wooden table background
    thumb_w, thumb_h = 320, 512  # Scaled down for banner view
    margin_x, margin_y = 60, 100
    spacing = 30
    
    banner_w = margin_x * 2 + 7 * thumb_w + 6 * spacing
    banner_h = thumb_h + margin_y * 2 + 150  # Extra space for title header
    
    # Table background (Deep rich wood / studio dark tabletop)
    banner_img = Image.new("RGB", (banner_w, banner_h), "#111827")
    draw_banner = ImageDraw.Draw(banner_img)
    
    # Add promotional title header
    try:
        font_header = ImageFont.truetype("DejaVuSans-Bold.ttf", 44)
        font_subhead = ImageFont.truetype("DejaVuSans.ttf", 26)
    except:
        font_header = font_subhead = ImageFont.load_default()
        
    draw_banner.text((banner_w / 2, 40), "MASTERING ONTOLOGY ENGINEERING WITH PROTÉGÉ AND PIZZA.OWL", fill="#FFFFFF", anchor="mt", font=font_header)
    draw_banner.text((banner_w / 2, 95), "The Complete 7-Volume Executable Knowledge Architecture (EKA) & SKDL Series", fill="#9CA3AF", anchor="mt", font=font_subhead)
    
    # Paste each volume cover onto the table
    start_y = margin_y + 60
    for i, cover in enumerate(covers):
        thumb = cover.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        pos_x = margin_x + i * (thumb_w + spacing)
        
        # Draw a soft drop shadow effect behind each book
        shadow_box = [pos_x - 6, start_y - 6, pos_x + thumb_w + 10, start_y + thumb_h + 10]
        draw_banner.rectangle(shadow_box, fill="#030712")
        
        banner_img.paste(thumb, (pos_x, start_y))
        
    # Save final promo picture
    banner_img.save("complete_7_volumes_promotion_banner.jpg", quality=95)
    print("Successfully generated 'complete_7_volumes_promotion_banner.jpg' showcasing all 7 volumes on the table!")

if __name__ == "__main__":
    generate_table_promotion_banner()