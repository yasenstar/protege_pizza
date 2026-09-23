"""
EKA Cover Generator v2.0

Executable Knowledge Architecture (EKA)
From Pizza.owl to Executable Intelligence

Features
--------
1. Amazon cover output
2. Leanpub cover output
3. 300 DPI print cover output
4. Website promotion banner
5. LinkedIn promotion image
6. Automatic font-size fitting
7. Automatic text wrapping
8. Optional 3D title and book shadows
9. Optional gradient backgrounds
10. Configurable output formats

Requirements
------------
pip install pillow

Usage
-----
python eka_cover_generator.py

The program displays an interactive menu at startup.
"""

from __future__ import annotations

import math
import os
import textwrap
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont


# ============================================================
# Feature switches
# ============================================================

USE_3D_SHADOW = True
USE_GRADIENT_BACKGROUND = True
USE_HD_PRINT_VERSION = True


# ============================================================
# Project configuration
# ============================================================

PROJECT_NAME = "EKA Cover Generator"
PROJECT_VERSION = "2.0"

SERIES_TITLE_LINE_1 = "EXECUTABLE KNOWLEDGE"
SERIES_TITLE_LINE_2 = "ARCHITECTURE (EKA)"

DISCIPLINE_TEXT = "Mastering Ontology Engineering"
HERITAGE_TEXT = "with Protégé and Pizza.owl"
JOURNEY_TEXT = "From Pizza.owl to Executable Intelligence"
AUTHOR_NAME = "XIAOQI ZHAO"

OUTPUT_DIRECTORY = Path("eka_generated_covers")

BORDER_MARGIN_RATIO = 0.028
BORDER_WIDTH_RATIO = 0.0015
LOGO_WIDTH_RATIO = 0.23

BACKGROUND_GRADIENT_STRENGTH = 0.18
TEXT_SHADOW_OPACITY = 125
TEXT_SHADOW_OFFSET_RATIO = 0.004

PRINT_DPI = 300
PRINT_WIDTH_INCHES = 6
PRINT_HEIGHT_INCHES = 9

WEBSITE_BANNER_WIDTH = 2800
WEBSITE_BANNER_HEIGHT = 1000

LINKEDIN_WIDTH = 1200
LINKEDIN_HEIGHT = 627


# ============================================================
# Output presets
# ============================================================

OUTPUT_PRESETS = {
    "amazon": {
        "label": "Amazon版本",
        "width": 1600,
        "height": 2560,
        "dpi": 72,
        "format": "PNG",
        "quality": 95,
        "suffix": "amazon",
    },
    "leanpub": {
        "label": "Leanpub版本",
        "width": 1600,
        "height": 2560,
        "dpi": 144,
        "format": "PNG",
        "quality": 95,
        "suffix": "leanpub",
    },
    "print": {
        "label": "高清印刷版（300 DPI）",
        "width": PRINT_WIDTH_INCHES * PRINT_DPI,
        "height": PRINT_HEIGHT_INCHES * PRINT_DPI,
        "dpi": PRINT_DPI,
        "format": "PNG",
        "quality": 100,
        "suffix": "print_300dpi",
    },
    "website": {
        "label": "网站宣传横幅版",
        "width": WEBSITE_BANNER_WIDTH,
        "height": WEBSITE_BANNER_HEIGHT,
        "dpi": 72,
        "format": "PNG",
        "quality": 95,
        "suffix": "website_banner",
    },
    "linkedin": {
        "label": "LinkedIn推广图版",
        "width": LINKEDIN_WIDTH,
        "height": LINKEDIN_HEIGHT,
        "dpi": 72,
        "format": "PNG",
        "quality": 95,
        "suffix": "linkedin",
    },
}


# ============================================================
# Volume metadata
# ============================================================

VOLUMES = [
    {
        "volume": 1,
        "chapters": "Chapters 00-08",
        "theme": "SEMANTIC FOUNDATIONS",
        "description": (
            "Learning Ontology Engineering "
            "through Protégé and Pizza.owl"
        ),
        "background": "#0B2E28",
        "accent": "#1D9E75",
        "light": "#9FE1CB",
    },
    {
        "volume": 2,
        "chapters": "Chapters 09-13",
        "theme": "SEMANTIC RELATIONSHIPS",
        "description": (
            "Mastering Object Properties "
            "and Ontology Structures"
        ),
        "background": "#0A2138",
        "accent": "#378ADD",
        "light": "#B5D4F4",
    },
    {
        "volume": 3,
        "chapters": "Chapters 14-16",
        "theme": "SEMANTIC LOGIC",
        "description": (
            "OWL Restrictions, Reasoning and Governance"
        ),
        "background": "#211A3D",
        "accent": "#7F77DD",
        "light": "#CECBF6",
    },
    {
        "volume": 4,
        "chapters": "Chapters 17-24",
        "theme": "SEMANTIC KNOWLEDGE ENGINEERING",
        "description": (
            "The Semantic Knowledge "
            "Development Lifecycle (SKDL)"
        ),
        "background": "#2D1F0B",
        "accent": "#E8913A",
        "light": "#F5D0A0",
    },
    {
        "volume": 5,
        "chapters": "Chapters 25-30",
        "theme": "KNOWLEDGE GRAPH ENGINEERING",
        "description": (
            "Transforming Ontologies "
            "into Connected Intelligence"
        ),
        "background": "#1E293B",
        "accent": "#38BDF8",
        "light": "#BAE6FD",
    },
    {
        "volume": 6,
        "chapters": "Chapters 31-36",
        "theme": "AI-READY SEMANTIC SYSTEMS",
        "description": (
            "Knowledge Graphs, Agents "
            "and Intelligent Retrieval"
        ),
        "background": "#18222A",
        "accent": "#64748B",
        "light": "#CBD5E1",
    },
    {
        "volume": 7,
        "chapters": "Chapters 37-42",
        "theme": "EXECUTABLE INTELLIGENCE",
        "description": (
            "Realizing the Vision of "
            "Executable Knowledge Architecture"
        ),
        "background": "#1C0A0A",
        "accent": "#E11D48",
        "light": "#FDA4AF",
    },
]


# ============================================================
# Font discovery
# ============================================================

FONT_CANDIDATES = {
    "serif_bold": [
        "DejaVuSerif-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "C:/Windows/Fonts/georgiab.ttf",
        "/Library/Fonts/Georgia Bold.ttf",
    ],
    "sans": [
        "DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "/Library/Fonts/Arial.ttf",
    ],
    "sans_bold": [
        "DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
        "/Library/Fonts/Arial Bold.ttf",
    ],
    "sans_italic": [
        "DejaVuSans-Oblique.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
        "C:/Windows/Fonts/ariali.ttf",
        "/Library/Fonts/Arial Italic.ttf",
    ],
}


def resolve_font(font_role: str) -> str:
    """Find the first usable font for the requested role."""

    for candidate in FONT_CANDIDATES[font_role]:
        try:
            ImageFont.truetype(candidate, 20)
            return candidate
        except OSError:
            continue

    raise FileNotFoundError(
        f"找不到可用字体：{font_role}。"
        "请安装 DejaVu Fonts，或更新 FONT_CANDIDATES。"
    )


FONT_SERIF_BOLD = resolve_font("serif_bold")
FONT_SANS = resolve_font("sans")
FONT_SANS_BOLD = resolve_font("sans_bold")
FONT_SANS_ITALIC = resolve_font("sans_italic")


# ============================================================
# Color utilities
# ============================================================

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hexadecimal color to RGB."""

    hex_color = hex_color.lstrip("#")

    return tuple(
        int(hex_color[index:index + 2], 16)
        for index in (0, 2, 4)
    )


def blend_colors(
    color_a: tuple[int, int, int],
    color_b: tuple[int, int, int],
    factor: float,
) -> tuple[int, int, int]:
    """Blend two RGB colors."""

    factor = max(0.0, min(1.0, factor))

    return tuple(
        round(a + (b - a) * factor)
        for a, b in zip(color_a, color_b)
    )


def lighten_color(
    hex_color: str,
    factor: float = 0.5,
) -> tuple[int, int, int]:
    """Lighten a hexadecimal color."""

    return blend_colors(
        hex_to_rgb(hex_color),
        (255, 255, 255),
        factor,
    )


def darken_color(
    hex_color: str,
    factor: float = 0.5,
) -> tuple[int, int, int]:
    """Darken a hexadecimal color."""

    return blend_colors(
        hex_to_rgb(hex_color),
        (0, 0, 0),
        factor,
    )


# ============================================================
# Background utilities
# ============================================================

def create_gradient_background(
    width: int,
    height: int,
    background_hex: str,
    accent_hex: str,
) -> Image.Image:
    """
    Create a subtle vertical and radial-style gradient.

    Pillow is used directly so no NumPy dependency is required.
    """

    base_color = hex_to_rgb(background_hex)
    top_color = blend_colors(
        base_color,
        hex_to_rgb(accent_hex),
        BACKGROUND_GRADIENT_STRENGTH,
    )
    bottom_color = blend_colors(
        base_color,
        (0, 0, 0),
        0.22,
    )

    image = Image.new("RGB", (width, height), base_color)
    pixels = image.load()

    for y in range(height):
        vertical_factor = y / max(1, height - 1)
        row_color = blend_colors(
            top_color,
            bottom_color,
            vertical_factor,
        )

        for x in range(width):
            center_distance = abs(x - width / 2) / (width / 2)
            edge_darkening = min(0.12, center_distance * 0.12)

            pixels[x, y] = blend_colors(
                row_color,
                (0, 0, 0),
                edge_darkening,
            )

    return image


def create_background(
    width: int,
    height: int,
    background_hex: str,
    accent_hex: str,
) -> Image.Image:
    """Create either a gradient or flat background."""

    if USE_GRADIENT_BACKGROUND:
        return create_gradient_background(
            width,
            height,
            background_hex,
            accent_hex,
        )

    return Image.new(
        "RGB",
        (width, height),
        hex_to_rgb(background_hex),
    )


# ============================================================
# Typography utilities
# ============================================================

def measure_multiline_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    spacing: int = 8,
) -> tuple[int, int]:
    """Measure multiline text accurately."""

    box = draw.multiline_textbbox(
        (0, 0),
        text,
        font=font,
        align="center",
        spacing=spacing,
    )

    return box[2] - box[0], box[3] - box[1]


def wrap_text_by_width(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    max_width: int,
    max_lines: int | None = None,
) -> str:
    """
    Wrap text according to actual rendered pixel width.

    Existing line breaks are respected.
    """

    paragraphs = text.splitlines() or [text]
    output_lines: list[str] = []

    for paragraph in paragraphs:
        words = paragraph.split()

        if not words:
            output_lines.append("")
            continue

        current_line = words[0]

        for word in words[1:]:
            candidate = f"{current_line} {word}"

            width = draw.textbbox(
                (0, 0),
                candidate,
                font=font,
            )[2]

            if width <= max_width:
                current_line = candidate
            else:
                output_lines.append(current_line)
                current_line = word

        output_lines.append(current_line)

    if max_lines and len(output_lines) > max_lines:
        return "\n".join(output_lines[:max_lines])

    return "\n".join(output_lines)


def fit_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font_path: str,
    max_width: int,
    max_height: int,
    maximum_size: int,
    minimum_size: int = 18,
    max_lines: int | None = None,
    spacing_ratio: float = 0.18,
) -> tuple[str, ImageFont.FreeTypeFont, int]:
    """
    Automatically select font size and wrapping.

    Returns:
        wrapped_text
        font
        line_spacing
    """

    for size in range(maximum_size, minimum_size - 1, -2):
        font = ImageFont.truetype(font_path, size)
        spacing = max(4, round(size * spacing_ratio))

        wrapped_text = wrap_text_by_width(
            draw,
            text,
            font,
            max_width,
            max_lines=max_lines,
        )

        width, height = measure_multiline_text(
            draw,
            wrapped_text,
            font,
            spacing,
        )

        line_count = wrapped_text.count("\n") + 1

        if (
            width <= max_width
            and height <= max_height
            and (max_lines is None or line_count <= max_lines)
        ):
            return wrapped_text, font, spacing

    fallback_font = ImageFont.truetype(
        font_path,
        minimum_size,
    )

    fallback_spacing = max(
        4,
        round(minimum_size * spacing_ratio),
    )

    fallback_text = wrap_text_by_width(
        draw,
        text,
        fallback_font,
        max_width,
        max_lines=max_lines,
    )

    return fallback_text, fallback_font, fallback_spacing


def draw_centered_text(
    image: Image.Image,
    draw: ImageDraw.ImageDraw,
    center_x: int,
    top_y: int,
    text: str,
    font: ImageFont.FreeTypeFont,
    fill,
    spacing: int = 8,
    use_shadow: bool = False,
    shadow_scale: float = 1.0,
) -> None:
    """Draw centered multiline text with optional shadow."""

    if use_shadow and USE_3D_SHADOW:
        shadow_layer = Image.new(
            "RGBA",
            image.size,
            (0, 0, 0, 0),
        )

        shadow_draw = ImageDraw.Draw(shadow_layer)

        offset = max(
            3,
            round(
                image.width
                * TEXT_SHADOW_OFFSET_RATIO
                * shadow_scale
            ),
        )

        shadow_draw.multiline_text(
            (center_x + offset, top_y + offset),
            text,
            font=font,
            fill=(0, 0, 0, TEXT_SHADOW_OPACITY),
            anchor="ma",
            align="center",
            spacing=spacing,
        )

        shadow_layer = shadow_layer.filter(
            ImageFilter.GaussianBlur(
                radius=max(2, offset // 2)
            )
        )

        image.paste(
            shadow_layer,
            (0, 0),
            shadow_layer,
        )

    draw.multiline_text(
        (center_x, top_y),
        text,
        font=font,
        fill=fill,
        anchor="ma",
        align="center",
        spacing=spacing,
    )


# ============================================================
# Pizza logo
# ============================================================

def draw_pizza_logo(
    draw: ImageDraw.ImageDraw,
    center_x: float,
    center_y: float,
    size: float,
    accent_hex: str,
    background_hex: str,
) -> None:
    """Draw the Pizza.owl lineage logo."""

    accent = hex_to_rgb(accent_hex)
    background = hex_to_rgb(background_hex)
    crust_color = lighten_color(accent_hex, 0.5)

    start_angle = -150
    end_angle = -30
    steps = 70

    body_points = []

    for index in range(steps + 1):
        angle = math.radians(
            start_angle
            + (end_angle - start_angle)
            * index / steps
        )

        body_points.append(
            (
                center_x + size * math.cos(angle),
                center_y + size * math.sin(angle),
            )
        )

    body_points.append(
        (
            center_x,
            center_y + size * 1.15,
        )
    )

    draw.polygon(
        body_points,
        fill=accent,
    )

    crust_radius = size + size * 0.027
    crust_thickness = max(10, round(size * 0.11))

    for index in range(steps + 1):
        angle = math.radians(
            start_angle
            + (end_angle - start_angle)
            * index / steps
        )

        x = center_x + crust_radius * math.cos(angle)
        y = center_y + crust_radius * math.sin(angle)

        draw.ellipse(
            (
                x - crust_thickness / 2,
                y - crust_thickness / 2,
                x + crust_thickness / 2,
                y + crust_thickness / 2,
            ),
            fill=crust_color,
        )

    hole_positions = [
        (-0.03, -0.05, 0.13),
        (-0.22, 0.16, 0.11),
        (0.19, 0.13, 0.12),
        (0.08, 0.36, 0.10),
        (-0.14, 0.38, 0.09),
    ]

    for dx, dy, radius_ratio in hole_positions:
        x = center_x + size * dx
        y = center_y + size * dy
        radius = size * radius_ratio

        draw.ellipse(
            (
                x - radius,
                y - radius,
                x + radius,
                y + radius,
            ),
            fill=background,
        )


# ============================================================
# Book shadow
# ============================================================

def add_book_shadow(
    canvas: Image.Image,
    cover: Image.Image,
    position: tuple[int, int],
    blur_radius: int,
    offset: tuple[int, int],
) -> None:
    """Paste a cover with a soft 3D shadow."""

    x, y = position

    if USE_3D_SHADOW:
        shadow = Image.new(
            "RGBA",
            canvas.size,
            (0, 0, 0, 0),
        )

        shadow_draw = ImageDraw.Draw(shadow)

        shadow_draw.rounded_rectangle(
            (
                x + offset[0],
                y + offset[1],
                x + cover.width + offset[0],
                y + cover.height + offset[1],
            ),
            radius=max(4, cover.width // 45),
            fill=(0, 0, 0, 180),
        )

        shadow = shadow.filter(
            ImageFilter.GaussianBlur(blur_radius)
        )

        canvas.paste(
            shadow,
            (0, 0),
            shadow,
        )

    canvas.paste(
        cover,
        (x, y),
    )


# ============================================================
# Single-volume cover generation
# ============================================================

def generate_single_cover(
    volume: dict,
    width: int,
    height: int,
    dpi: int,
    output_path: Path,
) -> Image.Image:
    """Generate one portrait cover."""

    scale = width / 1600

    background_hex = volume["background"]
    accent_hex = volume["accent"]
    light_hex = volume["light"]

    image = create_background(
        width,
        height,
        background_hex,
        accent_hex,
    )

    draw = ImageDraw.Draw(image)

    accent = hex_to_rgb(accent_hex)
    light = hex_to_rgb(light_hex)
    white = (255, 255, 255)

    border_margin = round(width * BORDER_MARGIN_RATIO)
    border_width = max(
        2,
        round(width * BORDER_WIDTH_RATIO),
    )

    draw.rectangle(
        (
            border_margin,
            border_margin,
            width - border_margin,
            height - border_margin,
        ),
        outline=accent,
        width=border_width,
    )

    content_width = round(width * 0.86)
    center_x = width // 2

    # Journey slogan
    journey_text, journey_font, journey_spacing = fit_text(
        draw,
        JOURNEY_TEXT,
        FONT_SANS,
        max_width=round(width * 0.78),
        max_height=round(height * 0.045),
        maximum_size=round(36 * scale),
        minimum_size=max(16, round(24 * scale)),
        max_lines=2,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.040),
        journey_text,
        journey_font,
        light,
        journey_spacing,
    )

    # Pizza logo
    logo_size = width * LOGO_WIDTH_RATIO / 2

    draw_pizza_logo(
        draw,
        center_x,
        height * 0.18,
        logo_size,
        accent_hex,
        background_hex,
    )

    # Main series title
    title_1, title_font_1, title_spacing_1 = fit_text(
        draw,
        SERIES_TITLE_LINE_1,
        FONT_SERIF_BOLD,
        max_width=content_width,
        max_height=round(height * 0.065),
        maximum_size=round(82 * scale),
        minimum_size=max(28, round(52 * scale)),
        max_lines=1,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.350),
        title_1,
        title_font_1,
        white,
        title_spacing_1,
        use_shadow=True,
    )

    title_2, title_font_2, title_spacing_2 = fit_text(
        draw,
        SERIES_TITLE_LINE_2,
        FONT_SERIF_BOLD,
        max_width=content_width,
        max_height=round(height * 0.065),
        maximum_size=round(82 * scale),
        minimum_size=max(28, round(52 * scale)),
        max_lines=1,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.395),
        title_2,
        title_font_2,
        white,
        title_spacing_2,
        use_shadow=True,
    )

    # Discipline positioning
    discipline_text, discipline_font, discipline_spacing = fit_text(
        draw,
        DISCIPLINE_TEXT,
        FONT_SANS,
        max_width=round(width * 0.72),
        max_height=round(height * 0.032),
        maximum_size=round(42 * scale),
        minimum_size=max(16, round(28 * scale)),
        max_lines=1,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.452),
        discipline_text,
        discipline_font,
        light,
        discipline_spacing,
    )

    # Heritage statement
    heritage_text, heritage_font, heritage_spacing = fit_text(
        draw,
        HERITAGE_TEXT,
        FONT_SANS_ITALIC,
        max_width=round(width * 0.72),
        max_height=round(height * 0.035),
        maximum_size=round(44 * scale),
        minimum_size=max(16, round(28 * scale)),
        max_lines=1,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.482),
        heritage_text,
        heritage_font,
        accent,
        heritage_spacing,
    )

    # Divider
    divider_y = round(height * 0.521)

    draw.line(
        (
            round(width * 0.375),
            divider_y,
            round(width * 0.625),
            divider_y,
        ),
        fill=accent,
        width=max(3, round(3 * scale)),
    )

    # Volume label
    volume_text = f"VOLUME {volume['volume']}"

    volume_label, volume_font, volume_spacing = fit_text(
        draw,
        volume_text,
        FONT_SANS_BOLD,
        max_width=round(width * 0.55),
        max_height=round(height * 0.055),
        maximum_size=round(74 * scale),
        minimum_size=max(28, round(48 * scale)),
        max_lines=1,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.540),
        volume_label,
        volume_font,
        accent,
        volume_spacing,
        use_shadow=True,
        shadow_scale=0.6,
    )

    # Chapter range
    chapter_text, chapter_font, chapter_spacing = fit_text(
        draw,
        volume["chapters"],
        FONT_SANS,
        max_width=round(width * 0.60),
        max_height=round(height * 0.040),
        maximum_size=round(44 * scale),
        minimum_size=max(18, round(30 * scale)),
        max_lines=1,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.585),
        chapter_text,
        chapter_font,
        white,
        chapter_spacing,
    )

    # Volume theme
    theme_text, theme_font, theme_spacing = fit_text(
        draw,
        volume["theme"],
        FONT_SANS_BOLD,
        max_width=round(width * 0.82),
        max_height=round(height * 0.080),
        maximum_size=round(48 * scale),
        minimum_size=max(18, round(30 * scale)),
        max_lines=2,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.675),
        theme_text,
        theme_font,
        light,
        theme_spacing,
    )

    # Volume description
    description_text, description_font, description_spacing = fit_text(
        draw,
        volume["description"],
        FONT_SANS,
        max_width=round(width * 0.78),
        max_height=round(height * 0.095),
        maximum_size=round(42 * scale),
        minimum_size=max(17, round(27 * scale)),
        max_lines=3,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.720),
        description_text,
        description_font,
        light,
        description_spacing,
    )

    # Author
    author_text, author_font, author_spacing = fit_text(
        draw,
        AUTHOR_NAME,
        FONT_SANS_BOLD,
        max_width=round(width * 0.55),
        max_height=round(height * 0.040),
        maximum_size=round(50 * scale),
        minimum_size=max(20, round(34 * scale)),
        max_lines=1,
    )

    draw_centered_text(
        image,
        draw,
        center_x,
        round(height * 0.920),
        author_text,
        author_font,
        white,
        author_spacing,
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    image.save(
        output_path,
        format="PNG",
        dpi=(dpi, dpi),
        optimize=True,
    )

    return image


# ============================================================
# Promotional banner generation
# ============================================================

def generate_promotion_banner(
    output_type: str,
    output_path: Path,
) -> Image.Image:
    """Generate website or LinkedIn promotion image."""

    preset = OUTPUT_PRESETS[output_type]

    width = preset["width"]
    height = preset["height"]
    dpi = preset["dpi"]

    background = Image.new(
        "RGB",
        (width, height),
        (17, 24, 39),
    )

    if USE_GRADIENT_BACKGROUND:
        background = create_gradient_background(
            width,
            height,
            "#111827",
            "#378ADD",
        )

    draw = ImageDraw.Draw(background)

    if output_type == "website":
        heading_max_size = 58
        subtitle_max_size = 32
        top_space = 175
        columns = 7
    else:
        heading_max_size = 38
        subtitle_max_size = 23
        top_space = 145
        columns = 4

    heading, heading_font, heading_spacing = fit_text(
        draw,
        "EXECUTABLE KNOWLEDGE ARCHITECTURE (EKA)",
        FONT_SANS_BOLD,
        max_width=round(width * 0.88),
        max_height=round(height * 0.10),
        maximum_size=heading_max_size,
        minimum_size=22,
        max_lines=2,
    )

    draw_centered_text(
        background,
        draw,
        width // 2,
        round(height * 0.045),
        heading,
        heading_font,
        (255, 255, 255),
        heading_spacing,
        use_shadow=True,
    )

    subtitle, subtitle_font, subtitle_spacing = fit_text(
        draw,
        JOURNEY_TEXT,
        FONT_SANS,
        max_width=round(width * 0.80),
        max_height=round(height * 0.06),
        maximum_size=subtitle_max_size,
        minimum_size=18,
        max_lines=2,
    )

    draw_centered_text(
        background,
        draw,
        width // 2,
        round(height * 0.115),
        subtitle,
        subtitle_font,
        (156, 163, 175),
        subtitle_spacing,
    )

    if output_type == "website":
        cover_width = round(width * 0.105)
        cover_height = round(cover_width * 1.6)
        horizontal_gap = round(width * 0.012)
        rows = 1
    else:
        cover_width = round(width * 0.145)
        cover_height = round(cover_width * 1.6)
        horizontal_gap = round(width * 0.022)
        rows = 2

    total_first_row = min(columns, len(VOLUMES))
    first_row_width = (
        total_first_row * cover_width
        + (total_first_row - 1) * horizontal_gap
    )

    start_x = (width - first_row_width) // 2
    start_y = top_space

    for index, volume in enumerate(VOLUMES):
        row = index // columns
        column = index % columns

        items_in_row = min(
            columns,
            len(VOLUMES) - row * columns,
        )

        row_width = (
            items_in_row * cover_width
            + (items_in_row - 1) * horizontal_gap
        )

        row_start_x = (width - row_width) // 2

        x = row_start_x + column * (
            cover_width + horizontal_gap
        )

        y = start_y + row * (
            cover_height + round(height * 0.06)
        )

        temporary_cover = generate_single_cover(
            volume,
            800,
            1280,
            72,
            OUTPUT_DIRECTORY
            / "_temporary"
            / f"volume_{volume['volume']}.png",
        )

        thumbnail = temporary_cover.resize(
            (cover_width, cover_height),
            Image.Resampling.LANCZOS,
        )

        add_book_shadow(
            background,
            thumbnail,
            (x, y),
            blur_radius=max(5, cover_width // 30),
            offset=(
                max(5, cover_width // 24),
                max(7, cover_width // 18),
            ),
        )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    background.save(
        output_path,
        format="PNG",
        dpi=(dpi, dpi),
        optimize=True,
    )

    return background


# ============================================================
# Selection and output logic
# ============================================================

def get_volume_by_number(volume_number: int) -> dict:
    """Return volume metadata by number."""

    for volume in VOLUMES:
        if volume["volume"] == volume_number:
            return volume

    raise ValueError(
        f"Volume {volume_number} 不存在。"
    )


def select_volumes_interactively() -> list[dict]:
    """Prompt thee volume or all volumes."""

    print()
    print("请选择需要生成的卷：")
    print("0. 生成全部 Volume 1-7")
    print("1-7. 只生成指定 Volume")
    print()

    selection = input(
        "请输入卷号 [默认 0]："
    ).strip()

    if not selection:
        selection = "0"

    if selection == "0":
        return VOLUMES

    try:
        volume_number = int(selection)
        return [get_volume_by_number(volume_number)]
    except (ValueError, TypeError):
        print("输入无效，自动生成全部 Volume 1-7。")
        return VOLUMES


def generate_cover_set(
    preset_name: str,
    selected_volumes: Iterable[dict],
) -> None:
    """Generate portrait covers for a selected output preset."""

    preset = OUTPUT_PRESETS[preset_name]

    output_folder = (
        OUTPUT_DIRECTORY / preset["suffix"]
    )

    print()
    print(f"正在生成：{preset['label']}")
    print(
        f"输出尺寸：{preset['width']} × "
        f"{preset['height']} px"
    )
    print(f"输出 DPI：{preset['dpi']}")
    print()

    for volume in selected_volumes:
        filename = (
            f"EKA_Volume_{volume['volume']}_"
            f"{preset['suffix']}.png"
        )

        output_path = output_folder / filename

        generate_single_cover(
            volume=volume,
            width=preset["width"],
            height=preset["height"],
            dpi=preset["dpi"],
            output_path=output_path,
        )

        print(f"已生成：{output_path}")

    print()
    print(f"{preset['label']}生成完成。")


# ============================================================
# Interactive menu
# ============================================================

def display_menu() -> None:
    """Display the generation menu."""

    print()
    print("=" * 64)
    print(f"{PROJECT_NAME} v{PROJECT_VERSION}")
    print("Executable Knowledge Architecture (EKA)")
    print("=" * 64)
    print()
    print("自动生成：")
    print("1. Amazon版本")
    print("2. Leanpub版本")
    print("3. 高清印刷版（300 DPI）")
    print("4. 网站宣传横幅版")
    print("5. LinkedIn推广图版")
    print("6. 一次生成全部版本")
    print("0. 退出")
    print()
    print("当前功能开关：")
    print(f"USE_3D_SHADOW = {USE_3D_SHADOW}")
    print(
        "USE_GRADIENT_BACKGROUND = "
        f"{USE_GRADIENT_BACKGROUND}"
    )
    print(
        "USE_HD_PRINT_VERSION = "
        f"{USE_HD_PRINT_VERSION}"
    )
    print()


def run_interactive() -> None:
    """Run the interactive generator."""

    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    while True:
        display_menu()

        choice = input(
            "请选择输出类型 [0-6]："
        ).strip()

        if choice == "0":
            print("程序已退出。")
            return

        if choice == "1":
            volumes = select_volumes_interactively()
            generate_cover_set("amazon", volumes)
            return

        if choice == "2":
            volumes = select_volumes_interactively()
            generate_cover_set("leanpub", volumes)
            return

        if choice == "3":
            if not USE_HD_PRINT_VERSION:
                print(
                    "高清印刷版已被关闭。"
                    "请将 USE_HD_PRINT_VERSION 设为 True。"
                )
                return

            volumes = select_volumes_interactively()
            generate_cover_set("print", volumes)
            return

        if choice == "4":
            output_path = (
                OUTPUT_DIRECTORY
                / "website"
                / "EKA_7_Volumes_Website_Banner.png"
            )

            print("正在生成网站宣传横幅版……")

            generate_promotion_banner(
                "website",
                output_path,
            )

            print(f"已生成：{output_path}")
            return

        if choice == "5":
            output_path = (
                OUTPUT_DIRECTORY
                / "linkedin"
                / "EKA_7_Volumes_LinkedIn.png"
            )

            print("正在生成 LinkedIn 推广图版……")

            generate_promotion_banner(
                "linkedin",
                output_path,
            )

            print(f"已生成：{output_path}")
            return

        if choice == "6":
            selected_volumes = VOLUMES

            generate_cover_set(
                "amazon",
                selected_volumes,
            )

            generate_cover_set(
                "leanpub",
                selected_volumes,
            )

            if USE_HD_PRINT_VERSION:
                generate_cover_set(
                    "print",
                    selected_volumes,
                )

            website_path = (
                OUTPUT_DIRECTORY
                / "website"
                / "EKA_7_Volumes_Website_Banner.png"
            )

            linkedin_path = (
                OUTPUT_DIRECTORY
                / "linkedin"
                / "EKA_7_Volumes_LinkedIn.png"
            )

            generate_promotion_banner(
                "website",
                website_path,
            )

            generate_promotion_banner(
                "linkedin",
                linkedin_path,
            )

            print()
            print("全部封面和推广图片已生成完成。")
            print(f"输出目录：{OUTPUT_DIRECTORY.resolve()}")
            return

        print()
        print("输入无效，请输入 0 到 6。")


# ============================================================
# Program entry point
# ============================================================

if __name__ == "__main__":
    run_interactive()