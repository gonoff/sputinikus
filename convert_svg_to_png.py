#!/usr/bin/env python3
"""
Convert all SVG files to PNG for Ren'Py compatibility
"""

import os
import cairosvg
from pathlib import Path

BASE_PATH = Path(__file__).parent / "game" / "images"

# Output dimensions by type
DIMENSIONS = {
    "backgrounds": (1920, 1080),
    "characters/aria": (200, 300),
    "characters": (400, 800),  # Default for other characters
    "cg": (1920, 1080),
}

def get_dimensions(svg_path):
    """Determine output dimensions based on file path"""
    path_str = str(svg_path)
    if "backgrounds" in path_str:
        return DIMENSIONS["backgrounds"]
    elif "characters/aria" in path_str:
        return DIMENSIONS["characters/aria"]
    elif "characters" in path_str:
        return DIMENSIONS["characters"]
    elif "cg" in path_str:
        return DIMENSIONS["cg"]
    return (400, 800)  # Default

def convert_svg_to_png(svg_path):
    """Convert a single SVG file to PNG"""
    png_path = svg_path.with_suffix('.png')
    width, height = get_dimensions(svg_path)

    try:
        cairosvg.svg2png(
            url=str(svg_path),
            write_to=str(png_path),
            output_width=width,
            output_height=height
        )
        print(f"✓ Converted: {svg_path.name} -> {png_path.name}")
        return True
    except Exception as e:
        print(f"✗ Error converting {svg_path.name}: {e}")
        return False

def main():
    print("Converting SVG files to PNG...")
    print("=" * 60)

    # Find all SVG files
    svg_files = list(BASE_PATH.rglob("*.svg"))

    if not svg_files:
        print("No SVG files found.")
        return

    print(f"Found {len(svg_files)} SVG files\n")

    success_count = 0
    for svg_path in sorted(svg_files):
        if convert_svg_to_png(svg_path):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"Converted {success_count}/{len(svg_files)} files successfully")

if __name__ == "__main__":
    main()
