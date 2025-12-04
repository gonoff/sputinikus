#!/usr/bin/env python3
"""
Convert GUI SVG files to PNG for Ren'Py
"""

import os
import cairosvg

# GUI asset dimensions
GUI_DIMENSIONS = {
    "main_menu_bg.svg": (1920, 1080),
    "textbox.svg": (1920, 350),
    "namebox.svg": (400, 70),
    "button_idle.svg": (480, 80),
    "button_hover.svg": (480, 80),
    "choice_button_idle.svg": (1000, 90),
    "choice_button_hover.svg": (1000, 90),
    "frame.svg": (600, 500),
    "logo.svg": (1200, 400),
}

# Bar assets (for sliders in preferences)
BAR_DIMENSIONS = {
    "bar/left.svg": (500, 18),
    "bar/bottom.svg": (500, 18),
    "bar/thumb.svg": (22, 22),
}

# Scrollbar assets
SCROLLBAR_DIMENSIONS = {
    "scrollbar/vertical_idle_bar.svg": (18, 200),
    "scrollbar/vertical_idle_thumb.svg": (18, 60),
    "scrollbar/horizontal_idle_bar.svg": (200, 18),
    "scrollbar/horizontal_idle_thumb.svg": (60, 18),
}

def convert_svgs(dimensions_dict, gui_dir):
    """Convert a dictionary of SVG files to PNG."""
    converted = 0

    for svg_file, (width, height) in dimensions_dict.items():
        svg_path = os.path.join(gui_dir, svg_file)
        png_path = svg_path.replace('.svg', '.png')

        if os.path.exists(svg_path):
            try:
                cairosvg.svg2png(
                    url=svg_path,
                    write_to=png_path,
                    output_width=width,
                    output_height=height
                )
                print(f"Converted: {svg_file} -> {png_path.split('/')[-1]} ({width}x{height})")
                converted += 1
            except Exception as e:
                print(f"Error converting {svg_file}: {e}")
        else:
            print(f"Not found: {svg_path}")

    return converted


def convert_gui_svgs():
    gui_dir = "game/gui"

    if not os.path.exists(gui_dir):
        print(f"GUI directory not found: {gui_dir}")
        return

    total = 0

    print("Converting main GUI assets...")
    total += convert_svgs(GUI_DIMENSIONS, gui_dir)

    print("\nConverting bar assets...")
    total += convert_svgs(BAR_DIMENSIONS, gui_dir)

    print("\nConverting scrollbar assets...")
    total += convert_svgs(SCROLLBAR_DIMENSIONS, gui_dir)

    print(f"\nTotal converted: {total} GUI assets")

if __name__ == "__main__":
    convert_gui_svgs()
