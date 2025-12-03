#!/usr/bin/env python3
"""
Generate placeholder images for The Chronicler's Device
Run this script to create colored rectangles with labels for all game assets
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Base path for images
BASE_PATH = "/workspaces/sputinikus/game/images"

# Dimensions
BG_WIDTH, BG_HEIGHT = 1920, 1080
SPRITE_WIDTH, SPRITE_HEIGHT = 400, 800
ARIA_WIDTH, ARIA_HEIGHT = 200, 300
CG_WIDTH, CG_HEIGHT = 1920, 1080

# Color schemes for different categories
COLORS = {
    # Backgrounds
    "modern": "#3a5a8c",       # Blue-gray for modern scenes
    "florence": "#8b6914",     # Golden-brown for Florence
    "rome": "#6b2d2d",         # Deep red for Rome

    # Characters
    "gary": "#4a90d9",         # Blue for Gary
    "aria": "#00ffff",         # Cyan for ARIA
    "benedetto": "#8b4513",    # Brown for Benedetto
    "pietro": "#654321",       # Dark brown
    "leonardo": "#2e8b57",     # Green for Leonardo
    "michelangelo": "#483d8b", # Purple
    "lorenzo_medici": "#4b0082",  # Indigo
    "guicciardini": "#800000", # Dark red
    "pope_julius": "#ffd700",  # Gold for Pope
    "cardinal": "#8b0000",     # Cardinal red

    # CG events
    "cg": "#2f4f4f",           # Dark slate
}


def create_placeholder(width, height, color, text, filepath):
    """Create a simple placeholder image with text label"""
    # Create image
    img = Image.new('RGB', (width, height), color)
    draw = ImageDraw.Draw(img)

    # Add border
    border_color = "#ffffff"
    border_width = 4
    draw.rectangle(
        [(border_width, border_width), (width - border_width, height - border_width)],
        outline=border_color,
        width=border_width
    )

    # Add text - use default font (no external font needed)
    try:
        # Try to use a larger built-in font
        font = ImageFont.load_default()
    except:
        font = None

    # Calculate text position (center)
    # Split long text into multiple lines
    lines = text.split('\n')
    if len(lines) == 1 and len(text) > 30:
        # Auto-wrap long single lines
        words = text.split('_')
        mid = len(words) // 2
        lines = ['_'.join(words[:mid]), '_'.join(words[mid:])]

    line_height = 20
    total_height = len(lines) * line_height
    y_start = (height - total_height) // 2

    for i, line in enumerate(lines):
        # Estimate text width (rough approximation)
        text_width = len(line) * 8
        x = (width - text_width) // 2
        y = y_start + i * line_height

        # Draw text with outline for visibility
        outline_color = "#000000"
        for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            draw.text((x+dx, y+dy), line, font=font, fill=outline_color)
        draw.text((x, y), line, font=font, fill="#ffffff")

    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    # Save image
    img.save(filepath)
    print(f"Created: {filepath}")


def generate_backgrounds():
    """Generate all background placeholders"""
    backgrounds = {
        "modern": [
            "gary_house_interior",
            "gary_backyard_day",
            "gary_backyard_rain",
            "transformed_2025_street",
            "transformed_2025_home",
        ],
        "florence": [
            "alley_arrival",
            "street_market_day",
            "street_market_night",
            "benedetto_shop_exterior",
            "benedetto_shop_interior",
            "capponi_palazzo_exterior",
            "capponi_palazzo_dining",
            "capponi_palazzo_study",
            "medici_palazzo_interior",
            "leonardo_workshop",
            "gary_workshop_palazzo",
            "countryside_departure",
        ],
        "rome": [
            "rome_cityscape",
            "vatican_exterior",
            "vatican_corridor",
            "pope_chambers",
            "st_peters_construction",
            "inquisition_chamber",
        ],
    }

    for category, bg_list in backgrounds.items():
        color = COLORS[category]
        for bg_name in bg_list:
            filepath = f"{BASE_PATH}/backgrounds/{category}/{bg_name}.png"
            label = f"BG: {bg_name.replace('_', ' ').title()}"
            create_placeholder(BG_WIDTH, BG_HEIGHT, color, label, filepath)


def generate_character_sprites():
    """Generate all character sprite placeholders"""
    characters = {
        "gary": [
            "gary_modern_neutral",
            "gary_modern_excited",
            "gary_modern_worried",
            "gary_renaissance_neutral",
            "gary_renaissance_confident",
            "gary_renaissance_nervous",
            "gary_renaissance_panicked",
            "gary_renaissance_triumphant",
        ],
        "aria": [
            "aria_neutral",
            "aria_warning",
            "aria_processing",
            "aria_happy",
            "aria_concerned",
        ],
        "benedetto": [
            "benedetto_neutral",
            "benedetto_interested",
            "benedetto_scheming",
            "benedetto_worried",
        ],
        "pietro": [
            "pietro_neutral",
            "pietro_friendly",
            "pietro_surprised",
        ],
        "leonardo": [
            "leonardo_neutral",
            "leonardo_intense",
            "leonardo_excited",
            "leonardo_skeptical",
        ],
        "michelangelo": [
            "michelangelo_neutral",
            "michelangelo_impressed",
            "michelangelo_offended",
        ],
        "lorenzo_medici": [
            "lorenzo_medici_neutral",
            "lorenzo_medici_pleased",
            "lorenzo_medici_calculating",
            "lorenzo_medici_suspicious",
        ],
        "guicciardini": [
            "guicciardini_neutral",
            "guicciardini_interested",
            "guicciardini_dangerous",
        ],
        "pope_julius": [
            "pope_julius_neutral",
            "pope_julius_impressed",
            "pope_julius_suspicious",
            "pope_julius_angry",
        ],
        "cardinal": [
            "cardinal_neutral",
            "cardinal_warning",
        ],
    }

    for char_name, sprite_list in characters.items():
        color = COLORS.get(char_name, "#666666")

        # ARIA gets smaller dimensions
        if char_name == "aria":
            width, height = ARIA_WIDTH, ARIA_HEIGHT
        else:
            width, height = SPRITE_WIDTH, SPRITE_HEIGHT

        for sprite_name in sprite_list:
            filepath = f"{BASE_PATH}/characters/{char_name}/{sprite_name}.png"
            # Extract expression from sprite name
            expression = sprite_name.split('_')[-1]
            label = f"{char_name.upper()}\n{expression}"
            create_placeholder(width, height, color, label, filepath)


def generate_cg_images():
    """Generate all CG (event illustration) placeholders"""
    cg_images = [
        "cg_time_travel",
        "cg_first_success",
        "cg_leonardo_collaboration",
        "cg_medici_meeting",
        "cg_papal_audience",
        "cg_ending_legendary",
        "cg_ending_fraud",
        "cg_ending_inquisition",
        "cg_ending_limited",
        "cg_ending_corruption",
        "cg_ending_paradox",
        "cg_ending_early",
    ]

    color = COLORS["cg"]
    for cg_name in cg_images:
        filepath = f"{BASE_PATH}/cg/{cg_name}.png"
        label = f"CG: {cg_name.replace('cg_', '').replace('_', ' ').title()}"
        create_placeholder(CG_WIDTH, CG_HEIGHT, color, label, filepath)


def main():
    print("Generating placeholder images for The Chronicler's Device...")
    print("=" * 60)

    print("\n--- Backgrounds ---")
    generate_backgrounds()

    print("\n--- Character Sprites ---")
    generate_character_sprites()

    print("\n--- CG Images ---")
    generate_cg_images()

    print("\n" + "=" * 60)
    print("Done! All placeholder images generated.")
    print(f"Images saved to: {BASE_PATH}")


if __name__ == "__main__":
    main()
