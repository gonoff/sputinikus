###############################################################################
# THE CHRONICLER'S DEVICE - CUSTOM GUI SCREENS
# Renaissance-inspired visual design
###############################################################################

init offset = -1

################################################################################
## Styles
################################################################################

style default:
    font "DejaVuSans.ttf"
    size 28
    color "#f5f0e0"

style input:
    color "#ffd700"

style hyperlink_text:
    color "#c9a227"
    hover_color "#ffd700"
    hover_underline True

style gui_text:
    color "#f5f0e0"
    size 24

style button:
    xpadding 20
    ypadding 10

style button_text is gui_text:
    idle_color "#8b7355"
    hover_color "#ffd700"
    selected_color "#c9a227"
    insensitive_color "#4a4a4a"

style label_text is gui_text:
    color "#ffd700"
    size 32

style prompt_text is gui_text:
    color "#c9a227"
    size 26

style vbar:
    xsize 8
    base_bar Frame("gui/bar/left.png", 6, 6, 6, 6)
    thumb "gui/bar/thumb.png"

style hbar:
    ysize 8
    base_bar Frame("gui/bar/bottom.png", 6, 6, 6, 6)
    thumb "gui/bar/thumb.png"

style scrollbar:
    ysize 18
    base_bar "gui/scrollbar/horizontal_idle_bar.png"
    thumb "gui/scrollbar/horizontal_idle_thumb.png"

style vscrollbar:
    xsize 18
    base_bar "gui/scrollbar/vertical_idle_bar.png"
    thumb "gui/scrollbar/vertical_idle_thumb.png"

################################################################################
## Say Screen - Dialog Display
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        style "say_window"

        if who is not None:
            window:
                id "namebox"
                style "say_namebox"
                text who id "who" style "say_label"

        text what id "what" style "say_dialogue"

    # Quick menu at bottom
    if not renpy.variant("small"):
        use quick_menu

style say_window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 350
    background Frame("gui/textbox.png", 50, 50, 50, 50)
    padding (100, 60, 100, 40)

style say_namebox:
    xpos 100
    xanchor 0
    ypos -10
    ysize 70
    xsize 400
    background Frame("gui/namebox.png", 20, 20, 20, 20)
    padding (30, 10, 30, 10)

style say_label:
    color "#ffd700"
    size 32
    bold True
    xalign 0.5
    yalign 0.5
    text_align 0.5

style say_dialogue:
    xpos 0
    xsize 1720
    ypos 30
    color "#f5f0e0"
    size 28
    line_spacing 8

style say_thought:
    color "#aaaaaa"
    italic True

################################################################################
## Input Screen
################################################################################

screen input(prompt):
    style_prefix "input"

    window:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input:
    color "#ffd700"
    size 32

################################################################################
## Choice Screen - Player Choices
################################################################################

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        for i in items:
            textbutton i.caption action i.action

style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 20

style choice_button:
    xsize 1000
    ysize 90
    idle_background Frame("gui/choice_button_idle.png", 20, 20, 20, 20)
    hover_background Frame("gui/choice_button_hover.png", 20, 20, 20, 20)
    padding (80, 20, 80, 20)

style choice_button_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    idle_color "#a6896a"
    hover_color "#ffd700"
    size 28

################################################################################
## Quick Menu
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.98

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    padding (15, 6, 15, 6)

style quick_button_text:
    size 18
    idle_color "#8b7355"
    hover_color "#ffd700"
    selected_color "#c9a227"
    insensitive_color "#4a4a4a"

################################################################################
## Main Menu
################################################################################

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add "gui/main_menu_bg.png"

    # Game logo
    add "gui/logo.png":
        xalign 0.5
        ypos 80

    # Menu buttons
    vbox:
        xalign 0.5
        yalign 0.75
        spacing 20

        textbutton _("Start") action Start()
        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Quit") action Quit(confirm=not main_menu)

style main_menu_vbox is vbox
style main_menu_button is button
style main_menu_button_text is button_text

style main_menu_vbox:
    spacing 20

style main_menu_button:
    xsize 480
    ysize 80
    idle_background Frame("gui/button_idle.png", 20, 20, 20, 20)
    hover_background Frame("gui/button_hover.png", 20, 20, 20, 20)
    padding (40, 15, 40, 15)

style main_menu_button_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    idle_color "#a6896a"
    hover_color "#ffd700"
    size 32
    font "DejaVuSans.ttf"

################################################################################
## Game Menu Base
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add "gui/main_menu_bg.png"
    else:
        add "gui/main_menu_bg.png"

    frame:
        style "game_menu_outer_frame"

        hbox:
            # Navigation column
            frame:
                style "game_menu_navigation_frame"

            # Content column
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        transclude

                else:
                    transclude

    # Title
    label title:
        xpos 75
        ypos 55
        style "game_menu_title"

    # Return button
    textbutton _("Return"):
        style "return_button"
        action Return()

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar
style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background Frame("gui/frame.png", 50, 50, 50, 50)

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_title:
    color "#ffd700"
    size 48

style return_button:
    xpos 75
    yalign 1.0
    yoffset -45

style return_button_text:
    color "#8b7355"
    hover_color "#ffd700"
    size 28

################################################################################
## Navigation
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos 60
        yalign 0.5
        spacing 8

        if main_menu:
            textbutton _("Start") action Start()

        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"

style navigation_button_text:
    color "#8b7355"
    hover_color "#ffd700"
    selected_color "#c9a227"
    size 28

################################################################################
## About Screen
################################################################################

screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"

        vbox:
            spacing 20

            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            text "[gui.about!t]"

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    color "#ffd700"
    size 36

################################################################################
## Load and Save Screens
################################################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        fixed:
            order_reverse True

            # File slot grid
            grid 3 3:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing 15

                for i in range(9):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)

            # Page buttons
            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                spacing 25

                textbutton _("<") action FilePagePrevious()
                text "[page_name_value!t]"
                textbutton _(">") action FilePageNext()

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button:
    xsize 300
    ysize 260
    background "#1a1525"
    hover_background "#2a2035"
    padding (15, 15, 15, 15)

style slot_time_text:
    size 18
    color "#8b7355"

style slot_name_text:
    size 18
    color "#c9a227"

style page_button_text:
    color "#8b7355"
    hover_color "#ffd700"
    size 24

################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            xfill True
            spacing 30

            hbox:
                box_wrap True
                spacing 40

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Language")
                    textbutton "English" action Language(None)
                    textbutton "Português" action Language("portuguese")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height 20

            hbox:
                spacing 40

                vbox:
                    style_prefix "slider"
                    label _("Text Speed")
                    bar value Preference("text speed")

                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

            null height 20

            hbox:
                spacing 40

                vbox:
                    style_prefix "slider"
                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                        if config.sample_sound:
                            textbutton _("Test") action Play("sound", config.sample_sound)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text

style pref_label_text:
    color "#ffd700"
    size 28

style radio_button_text:
    color "#8b7355"
    hover_color "#ffd700"
    selected_color "#c9a227"
    size 24

style check_button_text:
    color "#8b7355"
    hover_color "#ffd700"
    selected_color "#c9a227"
    size 24

style slider_slider:
    xsize 500
    base_bar Frame("gui/bar/left.png", 6, 6, 6, 6)
    thumb "gui/bar/thumb.png"

################################################################################
## History Screen
################################################################################

screen history():
    tag menu

    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"

        for h in _history_list:
            window:
                has fixed:
                    yfit True

                if h.who:
                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_height = 210
define gui.history_name_xpos = 0.5
define gui.history_name_ypos = 0
define gui.history_name_width = None
define gui.history_name_xalign = 0.5
define gui.history_text_xpos = 0
define gui.history_text_ypos = 50
define gui.history_text_width = 800
define gui.history_text_xalign = 0.0

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name_text:
    color "#ffd700"
    size 26

style history_text:
    color "#d0d0d0"
    size 24

################################################################################
## Confirm Screen
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/main_menu_bg.png"

    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_button
style confirm_button_text is gui_button_text

style confirm_frame:
    background Frame("gui/frame.png", 50, 50, 50, 50)
    padding (60, 60, 60, 60)
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    color "#f5f0e0"
    size 32
    text_align 0.5
    layout "subtitle"

style confirm_button:
    xsize 200
    ysize 60
    idle_background Frame("gui/button_idle.png", 20, 20, 20, 20)
    hover_background Frame("gui/button_hover.png", 20, 20, 20, 20)

style confirm_button_text:
    xalign 0.5
    yalign 0.5
    color "#8b7355"
    hover_color "#ffd700"
    size 28

################################################################################
## Skip Indicator
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9

            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha 0.5
    pause delay
    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.6)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos 15
    background Frame("gui/namebox.png", 20, 20, 20, 20)
    padding (24, 12, 50, 12)

style skip_text:
    color "#ffd700"
    size 24

style skip_triangle:
    font "DejaVuSans.ttf"

################################################################################
## Notify Screen
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos 68
    background Frame("gui/namebox.png", 20, 20, 20, 20)
    padding (24, 12, 60, 12)

style notify_text:
    color "#ffd700"
    size 22

################################################################################
## NVL Screen (for NVL-mode dialogue)
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"

        has vbox:
            spacing 15

        use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background "gui/main_menu_bg.png"
    padding (30, 30, 30, 30)

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

################################################################################
## Character Position Transforms (for our sprites)
################################################################################

transform center_pos:
    xalign 0.5
    yalign 1.0

transform left_pos:
    xalign 0.2
    yalign 1.0

transform right_pos:
    xalign 0.8
    yalign 1.0

transform aria_pos:
    xalign 0.95
    yalign 0.95
    zoom 0.5
