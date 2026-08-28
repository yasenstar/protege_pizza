# About Cover Images

## 2026-08-08

Book title: Mastering Ontology Engineering with Protégé and Pizza.owl

Resolution: 1600 x 2560 px, which aims to fit in KDP requirement
Format: PNG (source), JPG (final KDP export)

Design approach: consolidate template and only change theme color and content text

| Volume 卷 | Theme Color | Logo Color | Sub Title |
| --- | --- | --- | --- |
| Volume 1 | 深青绿 | 青绿披萨 | Ontology Foundation in Protégé |
| Volume 2 | 深蓝 | 蓝色披萨 | Object Properties & Relationships |
| Volume 3 | 深紫 | 紫色披萨 | Semantic Requirements & EKA Governance |
| Volume 4 | 橙/琥珀 | 橙色披萨 | SKDL — Semantic Knowledge Development Lifecycle |
| Volume 5 | 钢蓝/石板灰 | 钢蓝色披萨 | Data Properties, Custom UI, and Graph Ecosystems |
| Volume 6 | 碳灰/深青灰 | 青灰色披萨 | Advanced Reasoning, Constraints, and Interdisciplinary Depth |
| Volume 7 | 深红/绯红 | 绯红色披萨 | EKA Practices & The SKDL Methodology Package |

### Cover Color Palette

| Volume | Background | Accent | Accent Light |
| --- | --- | --- | --- |
| Volume 1 (Teal) | #0B2E28 | #1D9E75 | #9FE1CB |
| Volume 2 (Blue) | #0A2138 | #378ADD | #B5D4F4 |
| Volume 3 (Purple) | #211A3D | #7F77DD | #CECBF6 |
| Volume 4 (Orange/Amber) | #2D1F0B | #E8913A | #F5D0A0 |
| Volume 5 (Steel Blue) | #1E293B | #38BDF8 | #BAE6FD |
| Volume 6 (Slate Gray) | #18222A | #64748B | #CBD5E1 |
| Volume 7 (Crimson/Red) | #1C0A0A | #E11D48 | #FDA4AF |

- Title text: #FFFFFF
- Frame border: volume's own Accent color at 50% opacity
- Border/pizza-slice icon: Accent
- Subtitle/eyebrow text: Accent Light

## 2026-08-11

Added Volume 4 cover for SKDL chapters.

- File: `cover-volume4-20260811.jpg`
- Chapters: 17-24 (SKDL Stage 2 through Stage 7, in progress)

## 2026-08-26

Added Volume 5, Volume 6, and Volume 7 cover color palettes and tracking details.

Volume 7 color updated on 2026-08-28 from Bronze/Gold (#2C1E12 / #D97706 / #FDE68A) to Crimson/Red (#1C0A0A / #E11D48 / #FDA4AF) to ensure clear visual distinction from Volume 4 (Orange/Amber).

---

## Cover Design Specification

### Canvas
- **Resolution:** 1600 x 2560 px (portrait, KDP-compliant)
- **Background:** Volume-specific Background color (solid fill)

---

### 1. Frame Border

| Property | Value |
|----------|-------|
| Shape | Rectangle |
| Margin from edge | 45 px |
| Stroke width | 2 px |
| Color | Volume Accent at 50% opacity (RGBA: R,G,B,128) |
| Position | `x1=45, y1=45, x2=1555, y2=2515` |

---

### 2. Eyebrow Text (Top)

| Property | Value |
|----------|-------|
| Content | Line 1: `From Semantic Foundations to`  <br>Line 2: `Executable Knowledge Architecture (EKA)` |
| Font family | Sans-serif (DejaVu Sans or Liberation Sans) |
| Font size | 34 px |
| Font style | Regular |
| Color | Accent Light |
| Line 1 position | Centered, Y = 85 px |
| Line 2 position | Centered, Y = 129 px (line height ≈ 44 px) |
| Alignment | Center (horizontal) |

---

### 3. Pizza Slice Logo

#### 3.1 Geometry

| Property | Value |
|----------|-------|
| Center X | 800 px (canvas center) |
| Center Y | 460 px |
| Sector radius | 185 px |
| Sector angle span | 120° |
| Angle start | −150° |
| Angle end | −30° |
| Tip Y offset | +1.15 × radius (≈ 213 px below center) |

#### 3.2 Slice Body
- Fill: Volume **Accent** color
- Shape: Polygon built from arc points + bottom tip
- Arc resolution: 50 steps

#### 3.3 Crust
- Position: Slightly outside the slice arc (radius + 5 px)
- Thickness: 20 px (drawn as overlapping circles)
- Color: Lightened Accent (mix with white at 50% factor)
- End bumps: 14 px radius circles at both arc endpoints

#### 3.4 Pepperoni (5 circles, background-colored)

| # | Center X | Center Y | Radius | Note |
|---|----------|----------|--------|------|
| 1 | cx − 5 | cy − 10 | 24 px | Top center |
| 2 | cx − 40 | cy + 30 | 20 px | Left |
| 3 | cx + 35 | cy + 25 | 22 px | Right |
| 4 | cx + 15 | cy + 65 | 18 px | Lower right |
| 5 | cx − 25 | cy + 70 | 16 px | Lower left — **bitten** |

**Bite mark on #5:** A smaller circle (60% radius) overlapping from bottom-left, filled with slice color to simulate a bite.

---

### 4. Main Title

| Property | Value |
|----------|-------|
| Content | Line 1: `Mastering Ontology`  <br>Line 2: `Engineering` |
| Font family | Serif bold (DejaVu Serif Bold or Liberation Serif Bold) |
| Font size | 112 px |
| Font style | Bold |
| Color | #FFFFFF |
| Line 1 position | Centered, Y = 920 px |
| Line 2 position | Centered, Y = 1040 px (line height ≈ 120 px) |
| Alignment | Center (horizontal) |

---

### 5. Subtitle (Italic)

| Property | Value |
|----------|-------|
| Content | `with Protégé and Pizza.owl` |
| Font family | Sans-serif oblique/italic |
| Font size | 54 px |
| Font style | Oblique / Italic |
| Color | Volume Accent |
| Position | Centered, Y = 1180 px |
| Alignment | Center (horizontal) |

---

### 6. Horizontal Divider Line

| Property | Value |
|----------|-------|
| Y position | 1260 px |
| X start | 600 px |
| X end | 1000 px (length = 800 px) |
| Stroke width | 3 px |
| Color | Volume Accent |

---

### 7. Volume Label

| Property | Value |
|----------|-------|
| Content | `VOLUME {N}` (e.g., `VOLUME 5`) |
| Font family | Sans-serif bold |
| Font size | 74 px |
| Font style | Bold |
| Color | Volume Accent |
| Position | Centered, Y = 1320 px |
| Alignment | Center (horizontal) |

---

### 8. Chapter Range

| Property | Value |
|----------|-------|
| Content | `Chapters XX-YY` |
| Font family | Sans-serif regular |
| Font size | 44 px |
| Font style | Regular |
| Color | #FFFFFF |
| Position | Centered, Y = 1420 px |
| Alignment | Center (horizontal) |

---

### 9. Bottom Subtitle (Volume Theme Description)

| Property | Value |
|----------|-------|
| Content | Volume-specific subtitle (2 lines, split at `—` or natural break) |
| Font family | Sans-serif regular |
| Font size | 46 px |
| Font style | Regular |
| Color | Accent Light |
| Line 1 position | Centered, Y = 1750 px |
| Line 2 position | Centered, Y = 1812 px (line height ≈ 62 px) |
| Alignment | Center (horizontal) |

---

### 10. Author Name

| Property | Value |
|----------|-------|
| Content | `XIAOQI ZHAO` |
| Font family | Sans-serif bold |
| Font size | 50 px |
| Font style | Bold |
| Color | #FFFFFF |
| Position | Centered, Y = 2340 px |
| Alignment | Center (horizontal) |

---

### 11. Pizza Slice Design Code (Python / Pillow)

```python
import math

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
```

---

### 12. Complete Cover Generation Parameters

```python
CANVAS_W, CANVAS_H = 1600, 2560
BORDER_MARGIN = 45
BORDER_WIDTH = 2
BORDER_OPACITY = 128  # 50% of 255

# Font stack (fallback order)
SERIF_BOLD = ["DejaVuSerif-Bold.ttf", "LiberationSerif-Bold.ttf"]
SANS_BOLD  = ["DejaVuSans-Bold.ttf",  "LiberationSans-Bold.ttf"]
SANS       = ["DejaVuSans.ttf",       "LiberationSans-Regular.ttf"]
SANS_OBL   = ["DejaVuSans-Oblique.ttf","LiberationSans-Italic.ttf"]

# Component map
components = {
    "eyebrow":      {"font": SANS,       "size": 34,  "style": "Regular",  "color": "accent_light", "y": [85, 129]},
    "title":        {"font": SERIF_BOLD,  "size": 112, "style": "Bold",     "color": "#FFFFFF",      "y": [920, 1040]},
    "subtitle":     {"font": SANS_OBL,    "size": 54,  "style": "Oblique",  "color": "accent",       "y": [1180]},
    "volume":       {"font": SANS_BOLD,   "size": 74,  "style": "Bold",     "color": "accent",       "y": [1320]},
    "chapters":     {"font": SANS,        "size": 44,  "style": "Regular",  "color": "#FFFFFF",      "y": [1420]},
    "bottom_sub":   {"font": SANS,        "size": 46,  "style": "Regular",  "color": "accent_light", "y": [1750, 1812]},
    "author":       {"font": SANS_BOLD,   "size": 50,  "style": "Bold",     "color": "#FFFFFF",      "y": [2340]},
}

# Pizza logo
PIZZA_CX = 800
PIZZA_CY = 460
PIZZA_RADIUS = 185
PIZZA_ANGLE_SPAN = 120
PIZZA_TIP_RATIO = 1.15
CRUST_OFFSET = 5
CRUST_THICKNESS = 20
BUMP_RADIUS = 14
```

---

## File Naming Convention

```
cover_volume{N}.png
```

Examples:
- `cover_volume1.png`
- `cover_volume5.png`
- `cover_volume7.png`
