# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is "The Chronicler's Device," a Ren'Py visual novel about time travel to Renaissance Florence. The game features 16 chapters across 3 parts with 7 distinct endings based on player choices.

## Running and Building

**Requirements:** Ren'Py SDK 8.x (download from https://www.renpy.org/latest.html)

```bash
# Run via Ren'Py launcher - add project directory to launcher preferences
# Or via command line:
renpy.sh /path/to/sputinikus

# Convert SVG assets to PNG (requires cairosvg):
python convert_svg_to_png.py    # Characters, backgrounds, CGs
python convert_gui_svg.py       # GUI elements
```

## Architecture

### Asset Pipeline
All artwork is SVG files converted to PNG for Ren'Py. SVGs are version-controlled and edited as text.
- `convert_svg_to_png.py` - Converts `game/images/` SVGs (backgrounds: 1920x1080, characters: 400x800, ARIA: 200x300, CGs: 1920x1080)
- `convert_gui_svg.py` - Converts `game/gui/` SVGs with specific dimensions per asset type

### Script Structure
```
game/
├── script.rpy              # Entry point, chapter navigation, ending router
├── scripts/
│   ├── 00_init/
│   │   ├── 00_variables.rpy  # Game state, branching flags, relationship scores
│   │   └── 01_characters.rpy # Character definitions with colors and images
│   ├── 01_part1/           # Chapters 1-6
│   ├── 02_part2/           # Chapters 7-11
│   ├── 03_part3/           # Chapters 12-16
│   └── 04_endings/         # All 7 ending scripts
```

### Key Variable Systems

**Branching Flags** (in `00_variables.rpy`):
- `deception_strategy` - How Gary hides ARIA
- `accepted_intelligence` - Spy network involvement
- `leonardo_collaboration` - Knowledge sharing level
- `accepted_vatican` - Papal project acceptance
- `inquisition_response` - How to handle Church threat
- `return_timing` - When to return to 2025

**Score Tracking**:
- `reputation` (0-100) - Fame level
- `innovation_score`, `influence_score`, `corruption_score` - Determine endings
- Relationship scores per character (0-100)

**Ending Calculation**: The `calculate_ending()` function in `00_variables.rpy` checks flags in priority order (bad endings first, then score-based endings).

### Testing
Use `label debug_menu` (in `script.rpy`) to jump to specific chapters or test endings directly.
