################################################################################
# THE CHRONICLER'S DEVICE - GUI Configuration
################################################################################

init python:
    gui.init(1920, 1080)

################################################################################
## GUI Configuration Variables
################################################################################

# Game name and version
define config.name = _("The Chronicler's Device")
define config.version = "1.0"
define gui.about = _("A time-travel visual novel set in Renaissance Florence.\n\nCreated by the Sputinikus Team")

# Show the name and version on the main menu
define gui.show_name = True

################################################################################
## Colors
################################################################################

define gui.accent_color = "#ffd700"
define gui.idle_color = "#8b7355"
define gui.idle_small_color = "#6b5344"
define gui.hover_color = "#ffd700"
define gui.selected_color = "#c9a227"
define gui.insensitive_color = "#4a4a4a"
define gui.muted_color = "#6b5344"
define gui.hover_muted_color = "#8b7355"
define gui.text_color = "#f5f0e0"
define gui.interface_text_color = "#f5f0e0"

################################################################################
## Fonts and Font Sizes
################################################################################

define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "DejaVuSans.ttf"
define gui.interface_text_font = "DejaVuSans.ttf"

define gui.text_size = 28
define gui.name_text_size = 32
define gui.interface_text_size = 24
define gui.label_text_size = 32
define gui.notify_text_size = 22
define gui.title_text_size = 48

################################################################################
## Main and Game Menus
################################################################################

define gui.main_menu_background = "gui/main_menu_bg.png"
define gui.game_menu_background = "gui/main_menu_bg.png"

################################################################################
## Dialogue
################################################################################

define gui.textbox_height = 350
define gui.textbox_yalign = 1.0

define gui.name_xpos = 100
define gui.name_ypos = -10
define gui.name_xalign = 0.0

define gui.dialogue_xpos = 100
define gui.dialogue_ypos = 60
define gui.dialogue_width = 1720
define gui.dialogue_text_xalign = 0.0

################################################################################
## Buttons
################################################################################

define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(20, 20, 20, 20)
define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.5

################################################################################
## Choice Buttons
################################################################################

define gui.choice_button_width = 1000
define gui.choice_button_height = 90
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(80, 20, 80, 20)

define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#a6896a"
define gui.choice_button_text_hover_color = gui.accent_color

################################################################################
## File Slot Buttons
################################################################################

define gui.slot_button_width = 300
define gui.slot_button_height = 260
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 18
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

define config.thumbnail_width = 270
define config.thumbnail_height = 152

################################################################################
## Quick Menu
################################################################################

define gui.quick_button_text_size = 18
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_hover_color = gui.hover_color
define gui.quick_button_text_selected_color = gui.selected_color

################################################################################
## Navigation
################################################################################

define gui.navigation_xpos = 60
define gui.navigation_ypos = 0.5
define gui.navigation_spacing = 8

################################################################################
## History
################################################################################

define gui.history_height = 210
define gui.history_name_xpos = 0.5
define gui.history_name_ypos = 0
define gui.history_name_width = None
define gui.history_name_xalign = 0.5
define gui.history_text_xpos = 0
define gui.history_text_ypos = 50
define gui.history_text_width = 800
define gui.history_text_xalign = 0.0

define gui.history_allow_tags = { "alt", "b", "i", "u", "s", "color", "size" }

################################################################################
## NVL-Mode
################################################################################

define gui.nvl_name_xpos = 0.5
define gui.nvl_name_xalign = 0.5
define gui.nvl_name_ypos = 0
define gui.nvl_text_xpos = 0.5
define gui.nvl_text_yalign = 0.5
define gui.nvl_thought_xpos = 0.5
define gui.nvl_thought_yalign = 0.5
define gui.nvl_text_width = 1200
define gui.nvl_height = 170
define gui.nvl_spacing = 15
define gui.nvl_borders = Borders(0, 15, 0, 30)

################################################################################
## Scrollbars
################################################################################

define gui.scrollbar_size = 18
define gui.scrollbar_tile = False
define gui.scrollbar_borders = Borders(6, 6, 6, 6)

define gui.vscrollbar_borders = Borders(6, 6, 6, 6)

################################################################################
## Bars
################################################################################

define gui.bar_size = 18
define gui.bar_tile = False
define gui.bar_borders = Borders(6, 6, 6, 6)

define gui.vbar_borders = Borders(6, 6, 6, 6)

################################################################################
## Frames
################################################################################

define gui.frame_borders = Borders(50, 50, 50, 50)
define gui.frame_tile = False

define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

define gui.skip_frame_borders = Borders(24, 12, 50, 12)

define gui.notify_frame_borders = Borders(24, 12, 60, 12)

################################################################################
## Text-to-Speech
################################################################################

define config.has_voice = False
