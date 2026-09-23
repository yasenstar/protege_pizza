"""
EKA Cover Generator v1.0

Executable Knowledge Architecture (EKA)
From Pizza.owl to Executable Intelligence

Author:
Xiaoqi Zhao

Generate:
    cover_volume1.png
    cover_volume2.png
    ...
    cover_volume7.png

Output:
    1600 × 2560 PNG
"""

import math
from PIL import Image, ImageDraw, ImageFont


# ============================================================
# Global Configuration
# ============================================================

CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 2560

TITLE_TEXT = "EXECUTABLE KNOWLEDGE\nARCHITECTURE (EKA)"

DISCIPLINE_TEXT = "Mastering Ontology Engineering"

HERITAGE_TEXT = "with Protégé and Pizza.owl"

JOURNEY_TEXT = "From Pizza.owl to Executable Intelligence"

AUTHOR_NAME = "XIAOQI ZHAO"

BORDER_MARGIN = 45
BORDER_WIDTH = 2

LOGO_SIZE = 185


# ============================================================
# Fonts
# ============================================================

FONT_SERIF_BOLD = "DejaVuSerif-Bold.ttf"

FONT_SANS = "DejaVuSans.ttf"
FONT_SANS_BOLD = "DejaVuSans-Bold.ttf"
FONT_SANS_ITALIC = "DejaVuSans-Oblique.ttf"


# ============================================================
# Volume Definitions
# ============================================================

volumes_data = [

    {
        "volume": 1,
        "chapters": "Chapters 00-08",
        "theme": "SEMANTIC FOUNDATIONS",
        "description":
            "Learning Ontology Engineering\n"
            "through Protégé and Pizza.owl",

        "bg": "#0B2E28",
        "accent": "#1D9E75",
        "light": "#9FE1CB"
    },

    {
        "volume": 2,
        "chapters": "Chapters 09-13",
        "theme": "SEMANTIC RELATIONSHIPS",
        "description":
            "Mastering Object Properties\n"
            "and Ontology Structures",

        "bg": "#0A2138",
        "accent": "#378ADD",
        "light": "#B5D4F4"
    },

    {
        "volume": 3,
        "chapters": "Chapters 14-16",
        "theme": "SEMANTIC LOGIC",
        "description":
            "OWL Restrictions,\n"
            "Reasoning and Governance",

        "bg": "#211A3D",
        "accent": "#7F77DD",
        "light": "#CECBF6"
    },

    {
        "volume": 4,
        "chapters": "Chapters 17-24",
        "theme": "SEMANTIC KNOWLEDGE ENGINEERING",
        "description":
            "The Semantic Knowledge\n"
            "Development Lifecycle (SKDL)",

        "bg": "#2D1F0B",
        "accent": "#E8913A",
        "light": "#F5D0A0"
    },

    {
        "volume": 5,
        "chapters": "Chapters 25-30",
        "theme": "KNOWLEDGE GRAPH ENGINEERING",
        "description":
            "Transforming Ontologies\n"
            "into Connected Intelligence",

        "bg": "#1E293B",
        "accent": "#38BDF8",
        "light": "#BAE6FD"
    },

    {
        "volume": 6,
        "chapters": "Chapters 31-36",
        "theme": "AI-READY SEMANTIC SYSTEMS",
        "description":
            "Knowledge Graphs, Agents\n"
            "and Intelligent Retrieval",

        "bg": "#18222A",
        "accent": "#64748B",
        "light": "#CBD5E1"
    },

    {
        "volume": 7,
        "chapters": "Chapters 37-42",
        "theme": "EXECUTABLE INTELLIGENCE",
        "description":
            "Realizing the Vision of\n"
            "Executable Knowledge Architecture",

        "bg": "#1C0A0A",
        "accent": "#E11D48",
        "light": "#FDA4AF"
    }
]


# ============================================================
# Utility Functions
# ============================================================

def hex_to_rgb(hex_color):
    return tuple(
        int(hex_color[i:i + 2], 16)
        for i in (1, 3, 5)
    )


def lighten_color(hex_color, factor=0.5):

    r, g, b = hex_to_rgb(hex_color)

    r = round(r + (255 - r) * factor)
    g = round(g + (255 - g) * factor)
    b = round(b + (255 - b) * factor)

    return (r, g, b)


# ============================================================
# Pizza Logo
# ============================================================

def draw_pizza_logo(draw, cx, cy, size, accent_hex, bg_hex):

    accent = hex_to_rgb(accent_hex)
    bg = hex_to_rgb(bg_hex)

    angle_start = -150
    angle_end = -30

    points = []

    for i in range(50):

        angle = math.radians(
            angle_start
            + (angle_end - angle_start) * i / 49
        )

        points.append(
            (
                cx + size * math.cos(angle),
                cy + size * math.sin(angle)
            )
        )

    points.append((cx, cy + size * 1.15))

    draw.polygon(points, fill=accent)

    crust_color = lighten_color(accent_hex)

    r = size + 5

    for i in range(50):

        angle = math.radians(
            angle_start
            + (angle_end - angle_start) * i / 49
        )

        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)

        draw.ellipse(
            [x - 10, y - 10, x + 10, y + 10],
            fill=crust_color
        )

    pepperoni = [

        (-5, -10, 24),
        (-40, 30, 20),
        (35, 25, 22),
        (15, 65, 18),
        (-25, 70, 16)
    ]

    for dx, dy, rr in pepperoni:

        px = cx + dx
        py = cy + dy

        draw.ellipse(
            [px - rr, py - rr, px + rr, py + rr],
            fill=bg
        )


# ============================================================
# Generate Single Cover
# ============================================================

def generate_cover(volume_info):

    bg = volume_info["bg"]
    accent = volume_info["accent"]
    light = volume_info["light"]

    img = Image.new(
        "RGB",
        (CANVAS_WIDTH, CANVAS_HEIGHT),
        hex_to_rgb(bg)
    )

    draw = ImageDraw.Draw(img)

    # --------------------------------------------------------
    # Border
    # --------------------------------------------------------

    draw.rectangle(

        [
            BORDER_MARGIN,
            BORDER_MARGIN,
            CANVAS_WIDTH - BORDER_MARGIN,
            CANVAS_HEIGHT - BORDER_MARGIN
        ],

        outline=hex_to_rgb(accent),
        width=BORDER_WIDTH
    )

    # --------------------------------------------------------
    # Fonts
    # --------------------------------------------------------

    font_top = ImageFont.truetype(FONT_SANS, 34)

    font_title = ImageFont.truetype(FONT_SERIF_BOLD, 82)

    font_disc = ImageFont.truetype(FONT_SANS, 42)

    font_heritage = ImageFont.truetype(FONT_SANS_ITALIC, 44)

    font_volume = ImageFont.truetype(FONT_SANS_BOLD, 74)

    font_chapters = ImageFont.truetype(FONT_SANS, 44)

    font_theme = ImageFont.truetype(FONT_SANS_BOLD, 44)

    font_desc = ImageFont.truetype(FONT_SANS, 42)

    font_author = ImageFont.truetype(FONT_SANS_BOLD, 50)

    # --------------------------------------------------------
    # Journey
    # --------------------------------------------------------

    draw.text(
        (CANVAS_WIDTH / 2, 100),
        JOURNEY_TEXT,
        fill=hex_to_rgb(light),
        anchor="mt",
        font=font_top
    )

    # --------------------------------------------------------
    # Logo
    # --------------------------------------------------------

    draw_pizza_logo(
        draw,
        800,
        460,
        LOGO_SIZE,
        accent,
        bg
    )

    # --------------------------------------------------------
    # Main Brand
    # --------------------------------------------------------

    draw.multiline_text(
        (CANVAS_WIDTH / 2, 900),
        TITLE_TEXT,
        anchor="mt",
        align="center",
        fill="white",
        font=font_title
    )

    # --------------------------------------------------------
    # Discipline
    # --------------------------------------------------------

    draw.text(
        (CANVAS_WIDTH / 2, 1145),
        DISCIPLINE_TEXT,
        anchor="mt",
        fill=hex_to_rgb(light),
        font=font_disc
    )

    # --------------------------------------------------------
    # Heritage
    # --------------------------------------------------------

    draw.text(
        (CANVAS_WIDTH / 2, 1210),
        HERITAGE_TEXT,
        anchor="mt",
        fill=hex_to_rgb(accent),
        font=font_heritage
    )

    draw.line(
        [(600, 1290), (1000, 1290)],
        fill=hex_to_rgb(accent),
        width=3
    )

    # --------------------------------------------------------
    # Volume
    # --------------------------------------------------------

    draw.text(
        (CANVAS_WIDTH / 2, 1340),
        f"VOLUME {volume_info['volume']}",
        anchor="mt",
        fill=hex_to_rgb(accent),
        font=font_volume
    )

    draw.text(
        (CANVAS_WIDTH / 2, 1440),
        volume_info["chapters"],
        anchor="mt",
        fill="white",
        font=font_chapters
    )

    # --------------------------------------------------------
    # Theme
    # --------------------------------------------------------

    draw.text(
        (CANVAS_WIDTH / 2, 1710),
        volume_info["theme"],
        anchor="mt",
        fill=hex_to_rgb(light),
        font=font_theme
    )

    draw.multiline_text(
        (CANVAS_WIDTH / 2, 1780),
        volume_info["description"],
        anchor="mt",
        align="center",
        fill=hex_to_rgb(light),
        font=font_desc
    )

    # --------------------------------------------------------
    # Author
    # --------------------------------------------------------

    draw.text(
        (CANVAS_WIDTH / 2, 2335),
        AUTHOR_NAME,
        anchor="mt",
        fill="white",
        font=font_author
    )

    filename = f"cover_volume{volume_info['volume']}.png"

    img.save(filename)

    print(f"Generated {filename}")


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":

    for volume in volumes_data:
        generate_cover(volume)

    print("All EKA covers generated successfully.")