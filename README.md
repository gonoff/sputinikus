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

## Project Structure

```
game/                    # Ren'Py game files
├── scripts/             # Story scripts (.rpy)
│   ├── 00_init/         # Variables, characters
│   ├── part1-3/         # Chapter scripts
│   ├── endings/         # 7 ending scripts
│   └── branches/        # Branch variations
├── images/              # Backgrounds, sprites, CGs
└── audio/               # Music and sound effects

docs/                    # Documentation
├── DESIGN_DOCUMENT.md   # Full game design doc

gary_renaissance_*.md    # Source story (3 parts)
```

## Development

### Engine
- **Ren'Py** (Python-based visual novel engine)

### Current Status
- [x] Project structure
- [x] Variable system
- [x] Character definitions
- [x] Placeholder images
- [ ] Chapter scripts (in progress)
- [ ] Real artwork
- [ ] Audio

### Testing

This project is developed in GitHub Codespaces. Since Ren'Py requires a GUI:

1. Clone locally
2. Download [Ren'Py SDK](https://www.renpy.org/latest.html)
3. Open project in Ren'Py launcher
4. Click "Launch Project"

### Building

**Desktop:**
```
Ren'Py Launcher → Build Distributions
```

**Android APK:**
```
Ren'Py Launcher → Android → Build Package
```

## License

Story and game content: All rights reserved

## Credits

- Story: Original content
- Engine: [Ren'Py](https://www.renpy.org/)
