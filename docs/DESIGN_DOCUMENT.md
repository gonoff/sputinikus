# The Chronicler's Device - Game Design Document

## Project Overview

| Field | Value |
|-------|-------|
| **Title** | The Chronicler's Device |
| **Genre** | Visual Novel / Historical Fiction |
| **Engine** | Ren'Py 8.x |
| **Platforms** | Windows, Mac, Linux, Android (APK) |
| **Playtime** | 4-6 hours per playthrough |
| **Content** | 16 chapters, 3 parts, 7 endings |

---

## Story Summary

Gary Sputnik, a 25-year-old software developer from 2025, discovers a mysterious time travel device while burying his goldfish. Armed with ARIA, an advanced AI assistant hidden in a portable device, he travels to Renaissance Florence (1505) seeking fame and fortune.

Through mathematical "predictions" and engineering "innovations" (secretly powered by ARIA), Gary rises from a confused foreigner to the most influential advisor in Italy, working with Leonardo da Vinci, the Medici family, and eventually Pope Julius II.

**The player's choices determine Gary's fate:**
- Become a legendary historical figure
- Be exposed as a fraud
- Face the Inquisition
- Or find other endings based on their decisions

---

## Technical Decisions

### Why Ren'Py?

| Consideration | Ren'Py Advantage |
|--------------|------------------|
| Python-based | Familiar syntax, easy to extend |
| Built-in features | Save/load, rollback, settings menu |
| Multi-platform | Easy export to Windows/Mac/Linux/Android |
| VN-focused | Perfect for dialog-heavy games |
| Community | Large community, many tutorials |

### Hosting Strategy

- **Primary:** Downloadable builds (itch.io, direct download)
- **Android:** APK export for mobile
- **Testing:** Local Ren'Py launcher (Codespaces can't run GUI)

---

## Visual Style

### Full VN Style
- **Backgrounds:** Scene images for all locations
- **Character Sprites:** Multiple expressions per character
- **CG Events:** Special illustrations for key moments

### Art Pipeline Decision: SVG → PNG

**Decision:** All artwork is created as **SVG (Scalable Vector Graphics)** and converted to PNG for Ren'Py.

**Why SVG?**
| Benefit | Description |
|---------|-------------|
| Vector-based | Infinitely scalable, no pixelation |
| Code-friendly | Can be edited as text, version controlled |
| Expression reuse | Copy base sprite, modify only face elements for new expressions |
| Small file size | SVG sources are tiny compared to raster art files |
| Easy iteration | Quick tweaks without redrawing entire assets |

**Conversion Pipeline:**
```
SVG artwork → cairosvg library → PNG (Ren'Py compatible)
```

**Scripts:**
- `generate_placeholders.py` - Creates basic colored rectangle placeholders
- `convert_svg_to_png.py` - Batch converts all SVGs to PNGs

### Current Asset Status

| Asset Type | Total Needed | SVG Created | PNG Ready | Status |
|------------|--------------|-------------|-----------|--------|
| Backgrounds | 23 | 23 | 23 | **ALL COMPLETE** |
| Character Sprites | 18 | 18 | 18 | **ALL COMPLETE** (neutral expressions) |
| CG Images | 12 | 12 | 12 | **ALL COMPLETE** |

### Script Status

| Part | Chapters | Status |
|------|----------|--------|
| Part 1 | 1-6 | **COMPLETE** - The Accidental Time Traveler |
| Part 2 | 7-11 | **COMPLETE** - The Renaissance Genius |
| Part 3 | 12-16 | **COMPLETE** - The Legend of Gary |
| Endings | 7 endings | **COMPLETE** - All 7 endings written |

### GUI Status

| Asset | File | Status |
|-------|------|--------|
| Main Menu Background | `gui/main_menu_bg.png` | **COMPLETE** - Florence skyline with time vortex |
| Game Logo | `gui/logo.png` | **COMPLETE** - Gold title with cyan accents |
| Dialog Textbox | `gui/textbox.png` | **COMPLETE** - Parchment style with gold corners |
| Name Box | `gui/namebox.png` | **COMPLETE** - Gold-bordered tab |
| Menu Buttons | `gui/button_*.png` | **COMPLETE** - Idle and hover states |
| Choice Buttons | `gui/choice_button_*.png` | **COMPLETE** - Wide buttons with arrows |
| Menu Frame | `gui/frame.png` | **COMPLETE** - Dark frame with gold border |
| Slider Bars | `gui/bar/*.png` | **COMPLETE** - Gold thumb, dark track |
| Scrollbars | `gui/scrollbar/*.png` | **COMPLETE** - Vertical and horizontal |
| screens.rpy | `game/screens.rpy` | **COMPLETE** - Full custom screen system |
| gui.rpy | `game/gui.rpy` | **COMPLETE** - GUI configuration |

### Hand-Drawn SVG Assets (Completed)

**Characters:**
| Character | File | Description |
|-----------|------|-------------|
| Gary (Modern) | `gary_modern_neutral.svg` | Hoodie, jeans, glasses, messy hair |
| Gary (Modern) | `gary_modern_excited.svg` | Raised brows, big smile, sparkly eyes |
| Gary (Modern) | `gary_modern_worried.svg` | Frown, sweat drop, worried brows |
| Gary (Renaissance) | `gary_renaissance_neutral.svg` | Scholar's cap, doublet, silver trim |
| ARIA | `aria_neutral.svg` | Sleek device, cyan glowing screen, face UI |
| Leonardo | `leonardo_neutral.svg` | Long gray hair/beard, red robe, intense eyes |
| Benedetto | `benedetto_neutral.svg` | Rotund merchant, brown vest, balding |

**Backgrounds:**
| Location | File | Description |
|----------|------|-------------|
| Florence Market | `street_market_day.svg` | Buildings, stalls, laundry lines, cobblestones |
| Gary's Backyard | `gary_backyard_rain.svg` | Rainy, shed, fence, THE GLOWING HOLE with shovel |

### Expression Modification Workflow

To create new expressions from existing SVG:
1. Copy base SVG file
2. Modify only these elements:
   - **Eyebrows:** Angle and position (worried = inner up, angry = inner down)
   - **Eyes:** Size, pupil position, add sparkles/tears
   - **Mouth:** Curve direction (smile up, frown down), open/closed
   - **Optional:** Add blush, sweat drops, tears, veins
3. Save as new expression name
4. Run `python convert_svg_to_png.py`

### Art Style Guide

**Characters:**
- Semi-realistic anime-inspired style
- Soft gradients for shading
- Clear silhouettes
- Expressive faces with distinct features
- Drop shadows for depth

**Backgrounds:**
- Painterly style with gradient fills
- Atmospheric perspective (distant = faded)
- Period-appropriate architecture
- Mood lighting (warm Florence, dramatic Vatican)

**Color Palettes:**
| Setting | Primary Colors |
|---------|---------------|
| Modern 2025 | Blues, grays, whites |
| Florence | Warm golds, browns, terracotta |
| Rome/Vatican | Deep reds, golds, marble whites |
| ARIA UI | Cyan (#00FFFF), dark backgrounds |

---

## Narrative Structure

### Three-Part Structure

**Part 1: The Accidental Time Traveler (Chapters 1-6)**
- Discovery of the device
- Decision to travel
- Arrival in Florence
- Meeting Benedetto, establishing cover

**Part 2: The Renaissance Genius (Chapters 7-11)**
- Building reputation
- The dinner party test
- Intelligence recruitment
- Rise to prominence

**Part 3: The Legend of Gary (Chapters 12-16)**
- Collaborations with Leonardo, Michelangelo
- Vatican project
- Inquisition threat
- Return to 2025

---

## Branching System

### Six Major Branch Points

| # | Branch | Chapter | Choices | Impact |
|---|--------|---------|---------|--------|
| 1 | Deception Strategy | 4-5 | Hide ARIA / Partial / Full reveal | Discovery risk |
| 2 | Intelligence Work | 11 | Accept / Refuse Guicciardini | Access vs freedom |
| 3 | Leonardo Collaboration | 13 | Share all / Some / Withhold | Innovation score |
| 4 | Vatican Project | 14-15 | Accept / Refuse / Limit | Influence vs danger |
| 5 | Inquisition Response | 15-16 | Flee / Face / Hide | Survival |
| 6 | Return Timing | 16 | Early / Planned / Delayed | Historical impact |

### Variable System

```python
# Core flags (track major decisions)
deception_strategy = "none"      # How Gary hides ARIA
accepted_intelligence = False    # Joined spy network?
leonardo_collaboration = "none"  # Knowledge sharing level
accepted_vatican = False         # Papal project?
inquisition_response = "none"    # How to handle threat
return_timing = "none"           # When to go home

# Scores (determine endings)
reputation = 0                   # 0-100 fame level
innovation_score = 0             # Technical changes made
influence_score = 0              # Political power gained
corruption_score = 0             # Selfish use of power
timeline_corrupted = 0           # Paradox risk
```

---

## Seven Endings

| # | Ending | Requirements | Description |
|---|--------|-------------|-------------|
| 1 | **Legendary** | High scores, not caught | Returns to transformed world as legend |
| 2 | **Fraud Exposed** | ARIA discovered | Executed as charlatan |
| 3 | **Inquisition** | Caught by Church | Heresy trial |
| 4 | **Limited Impact** | Played safe | Returns unchanged |
| 5 | **Corruption** | corruption >= 5 | Used power selfishly |
| 6 | **Paradox** | timeline_corrupted >= 3 | Timeline fractures |
| 7 | **Early Return** | left_early = True | Fled before impact |

### Ending Calculation

```python
def calculate_ending():
    # Bad endings checked first
    if aria_discovered and not escaped_discovery:
        return "fraud_exposed"
    if inquisition_caught:
        return "inquisition"
    if timeline_corrupted >= 3:
        return "paradox"
    if left_early:
        return "early_return"
    if corruption_score >= 5:
        return "corruption"

    # Good endings based on scores
    impact = innovation_score + influence_score + historical_changes
    if impact >= 15 and reputation >= 80:
        return "legendary"
    else:
        return "limited_impact"
```

---

## Characters

### Main Characters

| Character | Role | Sprite Expressions |
|-----------|------|-------------------|
| **Gary Sputnik** | Protagonist, time traveler | neutral, excited, worried (modern); neutral, confident, nervous, panicked, triumphant (renaissance) |
| **ARIA** | AI device, secret helper | neutral, warning, processing, happy, concerned |

### Florence Characters

| Character | Role | Sprite Expressions |
|-----------|------|-------------------|
| **Benedetto** | Merchant, first ally | neutral, interested, scheming, worried |
| **Pietro** | Cart driver | neutral, friendly, surprised |
| **Lorenzo Capponi** | First major patron | (using Medici sprites) |
| **Guicciardini** | Intelligence official | neutral, interested, dangerous |
| **Lorenzo de' Medici** | Ruler of Florence | neutral, pleased, calculating, suspicious |

### Artists & Intellectuals

| Character | Role | Sprite Expressions |
|-----------|------|-------------------|
| **Leonardo da Vinci** | Master artist/inventor | neutral, intense, excited, skeptical |
| **Michelangelo** | Sculptor | neutral, impressed, offended |

### Vatican Characters

| Character | Role | Sprite Expressions |
|-----------|------|-------------------|
| **Pope Julius II** | The Pope | neutral, impressed, suspicious, angry |
| **Cardinal della Rovere** | Pope's nephew | neutral, warning |

---

## Locations

### Modern (2025)
- Gary's house interior
- Gary's backyard (day/rain variants)
- Transformed 2025 (ending scenes)

### Florence
- Arrival alley
- Street market (day/night)
- Benedetto's shop
- Capponi palazzo (dining, study)
- Medici palazzo
- Leonardo's workshop
- Gary's workshop palazzo
- Countryside (departure)

### Rome
- Rome cityscape
- Vatican exterior
- Vatican corridor
- Pope's chambers
- St. Peter's construction site
- Inquisition chamber (bad ending)

---

## File Structure

```
game/
├── audio/
│   ├── music/          # Background music
│   └── sfx/            # Sound effects
├── images/
│   ├── backgrounds/
│   │   ├── modern/     # 5 backgrounds
│   │   ├── florence/   # 12 backgrounds
│   │   └── rome/       # 6 backgrounds
│   ├── characters/     # 10 character folders, ~40 sprites total
│   └── cg/             # 12 event illustrations
├── scripts/
│   ├── 00_init/        # Variables, characters, config
│   ├── part1/          # Chapters 1-6
│   ├── part2/          # Chapters 7-11
│   ├── part3/          # Chapters 12-16
│   ├── endings/        # 7 ending scripts
│   └── branches/       # Branch variation content
├── script.rpy          # Main entry point
└── options.rpy         # Game configuration
```

---

## Implementation Status

### Phase 1: Infrastructure (COMPLETE)
- [x] Folder structure
- [x] Variable definitions (`00_variables.rpy`)
- [x] Character definitions (`01_characters.rpy`)
- [x] Main script (`script.rpy`)
- [x] Options (`options.rpy`)
- [x] Placeholder images (all generated)
- [x] Design document

### Phase 2: Part 1 Scripts (COMPLETE)
- [x] Chapter 1: A Fish, A Hole, and Destiny
- [x] Chapter 2: Making of a Plan
- [x] Chapter 3: Arrival and Regrets
- [x] Chapter 4: The Art of Survival
- [x] Chapter 5: First Patron
- [x] Chapter 6: Establishing

### Phase 3: Part 2 Scripts (COMPLETE)
- [x] Chapter 7: The Great Deception
- [x] Chapter 8: The Miracle Worker
- [x] Chapter 9: The Dinner Party
- [x] Chapter 10: The Performance
- [x] Chapter 11: The Job Interview

### Phase 4: Part 3 Scripts (COMPLETE)
- [x] Chapter 12: The God of Innovation
- [x] Chapter 13: Renaissance Startup
- [x] Chapter 14: The Tipping Point
- [x] Chapter 15: Divine Architecture
- [x] Chapter 16: The Return

### Phase 5: Endings (COMPLETE)
- [x] Legendary ending
- [x] Fraud Exposed ending
- [x] Inquisition ending
- [x] Limited Impact ending
- [x] Corruption ending
- [x] Paradox ending
- [x] Early Return ending

### Phase 6: Custom GUI (COMPLETE)
- [x] Main menu background (Florence skyline with time vortex)
- [x] Game logo (gold gradient with cyan accents)
- [x] Dialog textbox (parchment style with gold corners)
- [x] Name box (gold-bordered tab)
- [x] Menu buttons (idle/hover states)
- [x] Choice buttons (wide with arrow accents)
- [x] Menu frame (dark with gold border)
- [x] Slider bars (preferences screen)
- [x] Scrollbars (vertical/horizontal)
- [x] screens.rpy (complete custom screen system)
- [x] gui.rpy (GUI configuration variables)

### Phase 7: Polish (IN PROGRESS)
- [x] SVG artwork for all assets
- [ ] Music and sound effects (documented in AUDIO_MANIFEST.md)
- [ ] Additional character expressions
- [ ] Testing all paths
- [ ] Bug fixes

---

## Testing Workflow

Since Codespaces doesn't have GUI support:

1. **Write scripts** in Codespaces
2. **Push to GitHub**
3. **Pull locally** to machine with Ren'Py SDK
4. **Test** using Ren'Py launcher
5. **Build APK** for Android testing

Alternative: Build web export and host on VPS for browser testing.

---

## Source Material

The story is adapted from three markdown files in this repository:
- `gary_renaissance_part1.md` - Chapters 1-4
- `gary_renaissance_part2.md` - Chapters 7-11
- `gary_renaissance_part3.md` - Chapters 12-16

These contain the "correct" path (Legendary ending). Alternative paths and endings need to be written as part of the game development.
