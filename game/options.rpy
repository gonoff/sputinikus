###############################################################################
# THE CHRONICLER'S DEVICE - GAME OPTIONS
###############################################################################

## Basic game configuration

# Game title shown in the window title bar
define config.name = _("The Chronicler's Device")

# Version number
define config.version = "0.1.0"

# Save directory name
define config.save_directory = "TheChroniclerDevice-1234567890"

# GUI accent colors (Renaissance-inspired gold/brown theme)
define gui.accent_color = '#C9A227'          # Gold
define gui.idle_color = '#8B7355'            # Brown
define gui.idle_small_color = '#a6a6a6'
define gui.hover_color = '#FFD700'           # Bright gold on hover
define gui.selected_color = '#C9A227'
define gui.insensitive_color = '#5a5a5a'
define gui.muted_color = '#6b5344'
define gui.hover_muted_color = '#8b7355'
define gui.text_color = '#F5F5DC'            # Beige text
define gui.interface_text_color = '#F5F5DC'

## Screen dimensions
define config.screen_width = 1920
define config.screen_height = 1080

## Window settings
define config.window_icon = None

## Transitions
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = fade

## Sound settings
define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.main_menu_music = None  # Add later: "audio/music/main_theme.ogg"

## Text display
define config.default_text_cps = 30  # Characters per second
define gui.text_size = 28
define gui.name_text_size = 32

## Rollback (ability to go back in text)
define config.rollback_enabled = True

## Developer mode for debugging (disable in release)
define config.developer = True

## Console access (for debugging)
define config.console = True

## Auto-forward time
define config.default_afm_time = 15

## Skip settings
define config.allow_skipping = True
define config.fast_skipping = True

###############################################################################
# ABOUT TEXT
###############################################################################

define gui.about = _p("""
{b}The Chronicler's Device{/b}

A time travel visual novel about Gary Sputnik, a software developer who
discovers a mysterious device and travels to Renaissance Florence.

Armed with ARIA, an advanced AI assistant, Gary must navigate the dangerous
world of 15th-century Italy, working with historical figures like Leonardo
da Vinci, the Medici family, and even Pope Julius II.

Your choices determine whether Gary becomes a legendary figure remembered
through history... or meets a darker fate.

{b}Features:{/b}
- 16 chapters across 3 parts
- 7 distinct endings
- Full branching narrative
- Meet historical Renaissance figures

{b}Credits:{/b}
Story: [Your Name]
Engine: Ren'Py
""")

###############################################################################
# BUILD CONFIGURATION
###############################################################################

init python:

    # Packages to build
    build.package(build.directory_name + "-all", "zip", "windows linux mac renpy all")
    build.package(build.directory_name + "-win", "zip", "windows")
    build.package(build.directory_name + "-mac", "app-zip", "mac")
    build.package(build.directory_name + "-linux", "tar.bz2", "linux")

    # Files to exclude from distribution
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)  # Don't include script source
    build.classify('**.rpyc', 'all')  # Only compiled scripts

    # Documentation
    build.documentation('*.html')
    build.documentation('*.txt')
