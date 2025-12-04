# The Chronicler's Device

A time-travel visual novel where you play as Gary Sputnik, a software developer who discovers a mysterious device and travels to Renaissance Florence with an AI companion.

## Story

Gary Sputnik stumbles upon a time travel device while burying his goldfish. Armed with ARIA, an advanced AI, he travels to 1505 Florence seeking fame. Using ARIA's knowledge secretly, Gary poses as a genius mathematician and advisor, working with Leonardo da Vinci, the Medici family, and Pope Julius II.

**Your choices determine whether Gary becomes a legend... or meets a darker fate.**

## Features

- 16 chapters across 3 parts
- 7 distinct endings
- Full branching narrative with compounding choices
- Meet historical Renaissance figures
- Custom Renaissance-themed GUI with gold accents
- Visual novel style with backgrounds and character sprites

## Endings

| Ending | Description |
|--------|-------------|
| Legendary | Return as a historical legend |
| Fraud Exposed | ARIA discovered, executed |
| Inquisition | Caught by the Church |
| Limited Impact | Played it safe |
| Corruption | Used power selfishly |
| Paradox | Timeline fractures |
| Early Return | Fled before making impact |

## Running the Game

### Requirements

- [Ren'Py SDK](https://www.renpy.org/latest.html) (version 8.x recommended)

### Quick Start

1. **Download Ren'Py SDK** from https://www.renpy.org/latest.html
2. **Clone this repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/sputinikus.git
   ```
3. **Open Ren'Py Launcher**
4. **Add project directory:**
   - Click "preferences" in the launcher
   - Add the path to your cloned `sputinikus` folder
5. **Launch the game:**
   - Select "The Chronicler's Device" from the projects list
   - Click "Launch Project"

### Alternative: Command Line

If you have Ren'Py installed and in your PATH:

```bash
# Linux/Mac
renpy.sh /path/to/sputinikus

# Windows
renpy.exe C:\path\to\sputinikus
```

### Building Distributions

**Desktop (Windows/Mac/Linux):**
```
Ren'Py Launcher → Build Distributions → Select platforms → Build
```

**Android APK:**
```
Ren'Py Launcher → Android → Build Package
```

## Project Structure

```
game/                    # Ren'Py game files
├── gui.rpy              # GUI configuration
├── screens.rpy          # Custom screen definitions
├── options.rpy          # Game options
├── script.rpy           # Main entry point
├── gui/                 # GUI assets (PNG)
│   ├── main_menu_bg.png # Renaissance night sky background
│   ├── logo.png         # Gold game title
│   ├── textbox.png      # Dialog box
│   ├── namebox.png      # Character name box
│   ├── button_*.png     # Menu buttons
│   ├── choice_*.png     # Choice buttons
│   ├── frame.png        # Menu frame
│   ├── bar/             # Slider assets
│   └── scrollbar/       # Scrollbar assets
├── scripts/             # Story scripts (.rpy)
│   ├── 00_init/         # Variables, characters
│   ├── 01_part1/        # Chapters 1-6
│   ├── 02_part2/        # Chapters 7-11
│   ├── 03_part3/        # Chapters 12-16
│   └── 04_endings/      # 7 ending scripts
├── images/              # Backgrounds, sprites, CGs
│   ├── backgrounds/     # 23 scene backgrounds
│   ├── characters/      # Character sprites
│   └── cg/              # 12 CG event images
└── audio/               # Music and sound effects
    └── AUDIO_MANIFEST.md # Audio requirements

docs/                    # Documentation
└── DESIGN_DOCUMENT.md   # Full game design doc

gary_renaissance_*.md    # Source story (3 parts)
convert_svg_to_png.py    # Asset conversion script
convert_gui_svg.py       # GUI asset conversion
```

## Visual Style

The game features a custom Renaissance-themed GUI:

- **Color Palette:** Deep purples, golds, and bronze
- **Main Menu:** Florence skyline at night with time vortex effect
- **Dialog Box:** Parchment-style with ornate gold corners
- **Buttons:** Gold glow on hover
- **Typography:** Clean sans-serif with gold accents for names

## Development

### Asset Pipeline

All artwork is created as SVG and converted to PNG:

```bash
# Convert character/background SVGs
python convert_svg_to_png.py

# Convert GUI SVGs
python convert_gui_svg.py
```

### Current Status

- [x] Project structure
- [x] Variable system
- [x] Character definitions (24 characters)
- [x] All backgrounds (23 scenes)
- [x] All character sprites (18 sprites)
- [x] All CG images (12 event illustrations)
- [x] Custom GUI (Renaissance theme)
- [x] Part 1 scripts (Chapters 1-6)
- [x] Part 2 scripts (Chapters 7-11)
- [x] Part 3 scripts (Chapters 12-16)
- [x] All 7 endings
- [ ] Audio (music and sound effects)
- [ ] Additional character expressions

## License

Story and game content: All rights reserved

## Credits

- Story: Original content
- Engine: [Ren'Py](https://www.renpy.org/)
