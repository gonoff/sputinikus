###############################################################################
# THE CHRONICLER'S DEVICE - MAIN SCRIPT
# Entry point for the visual novel
###############################################################################

# The game starts here
label start:

    # Initialize the game
    $ persistent.playthrough_count += 1

    # Title screen transition
    scene black with fade

    # Show game title
    show text "{size=+30}THE CHRONICLER'S DEVICE{/size}\n\n{size=+10}A Time Travel Visual Novel{/size}" with dissolve
    pause 3.0
    hide text with dissolve

    # Part 1 introduction
    show text "{size=+20}Part 1{/size}\n\nThe Accidental Time Traveler" with dissolve
    pause 2.0
    hide text with dissolve

    # Jump to chapter 1
    jump chapter_1


###############################################################################
# CHAPTER NAVIGATION
###############################################################################

# Part 1: The Accidental Time Traveler
label part_1:
    $ current_part = 1
    jump chapter_1

# Part 2: The Renaissance Genius
label part_2:
    $ current_part = 2

    scene black with fade
    show text "{size=+20}Part 2{/size}\n\nThe Renaissance Genius" with dissolve
    pause 2.0
    hide text with dissolve

    jump chapter_7

# Part 3: The Legend of Gary
label part_3:
    $ current_part = 3

    scene black with fade
    show text "{size=+20}Part 3{/size}\n\nThe Legend of Gary" with dissolve
    pause 2.0
    hide text with dissolve

    jump chapter_12


###############################################################################
# ENDING ROUTER
###############################################################################

label determine_ending:
    # Calculate which ending the player gets
    $ ending = calculate_ending()

    if ending == "legendary":
        jump ending_legendary
    elif ending == "fraud_exposed":
        jump ending_fraud_exposed
    elif ending == "inquisition":
        jump ending_inquisition
    elif ending == "limited_impact":
        jump ending_limited_impact
    elif ending == "corruption":
        jump ending_corruption
    elif ending == "paradox":
        jump ending_paradox
    elif ending == "early_return":
        jump ending_early_return
    else:
        # Fallback
        jump ending_limited_impact


###############################################################################
# GAME OVER / CREDITS
###############################################################################

label game_over:
    scene black with fade

    show text "{size=+20}THE END{/size}" with dissolve
    pause 2.0

    show text "{size=+20}THE END{/size}\n\n{size=+5}Thank you for playing\nThe Chronicler's Device{/size}" with dissolve
    pause 3.0

    # Return to main menu
    return


###############################################################################
# DEBUG / TESTING MENU
###############################################################################

label debug_menu:
    menu:
        "DEBUG: Jump to which chapter?"

        "Chapter 1 - Fish, Hole, Destiny":
            jump chapter_1
        "Chapter 7 - Great Deception":
            jump chapter_7
        "Chapter 12 - God of Innovation":
            jump chapter_12
        "Test Endings":
            jump debug_endings
        "Return to Start":
            jump start

label debug_endings:
    menu:
        "DEBUG: Test which ending?"

        "Legendary (Best)":
            $ innovation_score = 10
            $ influence_score = 10
            $ historical_changes = 5
            $ reputation = 90
            $ played_safe = False
            $ aria_discovered = False
            $ inquisition_caught = False
            jump ending_legendary

        "Fraud Exposed":
            $ aria_discovered = True
            $ escaped_discovery = False
            jump ending_fraud_exposed

        "Inquisition":
            $ inquisition_caught = True
            jump ending_inquisition

        "Limited Impact":
            $ played_safe = True
            jump ending_limited_impact

        "Corruption":
            $ corruption_score = 6
            jump ending_corruption

        "Paradox":
            $ timeline_corrupted = 4
            jump ending_paradox

        "Early Return":
            $ left_early = True
            jump ending_early_return

        "Back":
            jump debug_menu
