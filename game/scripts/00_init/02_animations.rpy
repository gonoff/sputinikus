###############################################################################
# THE CHRONICLER'S DEVICE - ANIMATIONS & TRANSFORMS
# Dynamic visual effects to make the game feel alive
###############################################################################

###############################################################################
# CHARACTER IDLE ANIMATIONS - Subtle breathing/movement
###############################################################################

# Gentle breathing animation for characters
transform breathing:
    ease 3.0 zoom 1.02
    ease 3.0 zoom 1.0
    repeat

# Subtle floating for ARIA device
transform aria_float:
    xalign 0.9
    yalign 0.3
    zoom 0.5
    ease 2.0 yoffset -10
    ease 2.0 yoffset 0
    repeat

# Nervous fidgeting
transform nervous:
    ease 0.3 xoffset 3
    ease 0.3 xoffset -3
    ease 0.3 xoffset 2
    ease 0.3 xoffset 0
    repeat

# Confident stance with subtle sway
transform confident_sway:
    ease 4.0 rotate 1
    ease 4.0 rotate -1
    repeat

###############################################################################
# CHARACTER ENTRANCE ANIMATIONS
###############################################################################

# Slide in from left
transform slide_in_left:
    xalign -0.5
    alpha 0.0
    ease 0.5 xalign 0.2 alpha 1.0

# Slide in from right
transform slide_in_right:
    xalign 1.5
    alpha 0.0
    ease 0.5 xalign 0.8 alpha 1.0

# Slide in from center (dramatic entrance)
transform dramatic_entrance:
    xalign 0.5
    yalign 1.2
    alpha 0.0
    zoom 0.8
    ease 0.7 yalign 1.0 alpha 1.0 zoom 1.0

# Fade in with slight rise
transform fade_rise:
    alpha 0.0
    yoffset 30
    ease 0.6 alpha 1.0 yoffset 0

# Quick pop in
transform pop_in:
    alpha 0.0
    zoom 0.5
    ease 0.3 alpha 1.0 zoom 1.05
    ease 0.1 zoom 1.0

###############################################################################
# CHARACTER EXIT ANIMATIONS
###############################################################################

# Slide out left
transform slide_out_left:
    ease 0.4 xalign -0.5 alpha 0.0

# Slide out right
transform slide_out_right:
    ease 0.4 xalign 1.5 alpha 0.0

# Fade down and out
transform fade_down:
    ease 0.5 alpha 0.0 yoffset 30

###############################################################################
# SCREEN POSITION TRANSFORMS (Enhanced with breathing)
###############################################################################

# Left position with breathing
transform left_pos_animated:
    xalign 0.2
    yalign 1.0
    parallel:
        ease 3.0 zoom 1.015
        ease 3.0 zoom 1.0
        repeat

# Center position with breathing
transform center_pos_animated:
    xalign 0.5
    yalign 1.0
    parallel:
        ease 3.5 zoom 1.015
        ease 3.5 zoom 1.0
        repeat

# Right position with breathing
transform right_pos_animated:
    xalign 0.8
    yalign 1.0
    parallel:
        ease 3.2 zoom 1.015
        ease 3.2 zoom 1.0
        repeat

###############################################################################
# DRAMATIC SCREEN EFFECTS
###############################################################################

# Screen shake - light
transform shake_light:
    ease 0.05 xoffset 5
    ease 0.05 xoffset -5
    ease 0.05 xoffset 4
    ease 0.05 xoffset -4
    ease 0.05 xoffset 2
    ease 0.05 xoffset 0

# Screen shake - heavy (for dramatic moments)
transform shake_heavy:
    ease 0.04 xoffset 15 yoffset 10
    ease 0.04 xoffset -15 yoffset -8
    ease 0.04 xoffset 12 yoffset 6
    ease 0.04 xoffset -10 yoffset -5
    ease 0.04 xoffset 8 yoffset 4
    ease 0.04 xoffset -5 yoffset -2
    ease 0.04 xoffset 3 yoffset 1
    ease 0.04 xoffset 0 yoffset 0

# Pulse effect (for revelations)
transform pulse:
    ease 0.15 zoom 1.05
    ease 0.15 zoom 1.0
    ease 0.1 zoom 1.03
    ease 0.1 zoom 1.0

# Dramatic zoom in
transform zoom_dramatic:
    ease 1.5 zoom 1.15 xalign 0.5 yalign 0.4

# Time distortion effect
transform time_warp:
    parallel:
        ease 0.5 zoom 1.3
        ease 0.3 zoom 0.8
        ease 0.2 zoom 1.0
    parallel:
        ease 0.3 rotate 5
        ease 0.4 rotate -5
        ease 0.3 rotate 0

###############################################################################
# BACKGROUND ANIMATIONS
###############################################################################

# Subtle background pan (creates depth)
transform bg_slow_pan:
    xalign 0.5
    ease 30.0 xalign 0.52
    ease 30.0 xalign 0.48
    ease 30.0 xalign 0.5
    repeat

# Background breathing (very subtle zoom)
transform bg_breathe:
    ease 8.0 zoom 1.02
    ease 8.0 zoom 1.0
    repeat

# Ominous slow zoom
transform ominous_zoom:
    zoom 1.0
    linear 60.0 zoom 1.1

###############################################################################
# CUSTOM TRANSITIONS
###############################################################################

# Time travel transition - flash sequence
define time_travel_transition = MultipleTransition([
    False, Dissolve(0.2),
    Solid("#00ffff"), Dissolve(0.1),
    Solid("#ffffff"), Dissolve(0.1),
    Solid("#000000"), Dissolve(0.3),
    True
])

# Revelation flash - golden
define revelation = MultipleTransition([
    False, Dissolve(0.1),
    Solid("#ffd700"), Dissolve(0.2),
    True
])

# Danger flash (red)
define danger_flash = MultipleTransition([
    False, Dissolve(0.05),
    Solid("#8b0000"), Dissolve(0.15),
    True
])

# Dream/memory fade
define dream_fade = Dissolve(1.5)

###############################################################################
# TEXT EFFECTS
###############################################################################

# Slow text reveal for dramatic moments
define slow_text = Character(None, what_slow_cps=20)

# Very slow for suspense
define suspense_text = Character(None, what_slow_cps=10)

###############################################################################
# CG PRESENTATION TRANSFORMS
###############################################################################

# CG reveal with dramatic zoom
transform cg_reveal:
    zoom 1.1
    alpha 0.0
    ease 1.0 zoom 1.0 alpha 1.0

# CG exit
transform cg_exit:
    ease 0.8 zoom 1.1 alpha 0.0

# Ken Burns effect for CGs (slow pan/zoom)
transform ken_burns:
    zoom 1.0 xalign 0.5 yalign 0.5
    linear 10.0 zoom 1.1 xalign 0.55 yalign 0.45

###############################################################################
# ARIA-SPECIFIC EFFECTS
###############################################################################

# ARIA glitch effect (when malfunctioning/stressed)
transform aria_glitch:
    ease 0.05 xoffset 3 alpha 0.7
    ease 0.05 xoffset -2 alpha 1.0
    ease 0.05 xoffset 1 alpha 0.8
    ease 0.05 xoffset 0 alpha 1.0

# ARIA processing animation
transform aria_processing:
    ease 0.3 zoom 1.1
    ease 0.3 zoom 0.95
    ease 0.2 zoom 1.0
    repeat

# ARIA warning pulse
transform aria_warning:
    ease 0.5 matrixcolor TintMatrix("#ff6666")
    ease 0.5 matrixcolor TintMatrix("#ffffff")
    repeat

###############################################################################
# ECLIPSE EFFECT
###############################################################################

# Darkening for eclipse scene
transform eclipse_darken:
    matrixcolor BrightnessMatrix(0.0)
    linear 5.0 matrixcolor BrightnessMatrix(-0.4)

# Return to normal brightness
transform eclipse_brighten:
    linear 3.0 matrixcolor BrightnessMatrix(0.0)

###############################################################################
# EMOTION EMPHASIS
###############################################################################

# Surprised jump
transform surprised_jump:
    ease 0.1 yoffset -20
    ease 0.15 yoffset 0

# Angry shake
transform angry_shake:
    ease 0.08 xoffset 4 rotate 2
    ease 0.08 xoffset -4 rotate -2
    ease 0.08 xoffset 3 rotate 1
    ease 0.08 xoffset -2 rotate -1
    ease 0.08 xoffset 0 rotate 0

# Sad droop
transform sad_droop:
    ease 0.5 yoffset 10 zoom 0.98

# Thinking pose (slight tilt)
transform thinking:
    ease 0.3 rotate 3
    pause 2.0
    ease 0.3 rotate 0
