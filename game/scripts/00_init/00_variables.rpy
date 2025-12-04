###############################################################################
# THE CHRONICLER'S DEVICE - GAME STATE VARIABLES
# All variables that track player choices and game state
###############################################################################

init -5 python:
    import random

    ###########################################################################
    # VOICE BLIP SYSTEM - Animal Crossing style gibberish speech
    ###########################################################################

    # Map character names to their voice blip files
    VOICE_BLIPS = {
        "Gary": "audio/voice/voice_gary.ogg",
        "ARIA": "audio/voice/voice_aria.ogg",
        "Leonardo da Vinci": "audio/voice/voice_leonardo.ogg",
        "Lorenzo de' Medici": "audio/voice/voice_lorenzo.ogg",
        "Pope Julius II": "audio/voice/voice_pope.ogg",
        # Use shared voices for characters without specific blips
        "Benedetto": "audio/voice/voice_gary.ogg",
        "Pietro": "audio/voice/voice_gary.ogg",
        "Lorenzo Capponi": "audio/voice/voice_lorenzo.ogg",
        "Francesco Guicciardini": "audio/voice/voice_savonarola.ogg",
        "Giuliano de' Medici": "audio/voice/voice_lorenzo.ogg",
        "Michelangelo": "audio/voice/voice_leonardo.ogg",
        "Maestro Sangallo": "audio/voice/voice_leonardo.ogg",
        "Machiavelli": "audio/voice/voice_savonarola.ogg",
        "Cardinal della Rovere": "audio/voice/voice_pope.ogg",
        "Bramante": "audio/voice/voice_leonardo.ogg",
        "Franco": "audio/voice/voice_gary.ogg",
        "Maestro Roberto": "audio/voice/voice_leonardo.ogg",
        "Francesco Soderini": "audio/voice/voice_lorenzo.ogg",
        "Inquisitor": "audio/voice/voice_savonarola.ogg",
        "???": "audio/voice/voice_gary.ogg",
    }

    # Current speaking character for blip system
    current_speaker = None

    def voice_blip_callback(event, interact=True, **kwargs):
        """
        Character callback that plays looping voice blips while text displays.
        Uses cb_data to identify which character is speaking.
        """
        global current_speaker
        if event == "begin":
            # cb_data="X" becomes just "data" in kwargs (cb_ prefix is stripped by Ren'Py)
            who = kwargs.get("data", None)
            if who and who in VOICE_BLIPS:
                current_speaker = who
                # Play looping blip sound while character speaks
                renpy.music.play(VOICE_BLIPS[who], channel="voice_blip", loop=True, fadein=0.0)
        elif event == "slow_done":
            # Stop when text animation finishes, not when player clicks
            current_speaker = None
            renpy.music.stop(channel="voice_blip", fadeout=0.1)

    def calculate_ending():
        """Determines which ending the player gets based on accumulated choices."""

        # Check for immediate bad endings first
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

        # Calculate impact score
        impact = innovation_score + influence_score + historical_changes

        if impact >= 15 and reputation >= 80 and not played_safe:
            return "legendary"
        else:
            return "limited_impact"

###############################################################################
# CORE STORY FLAGS - Major branching decisions
###############################################################################

# Deception Strategy (Branching Point 1)
default deception_strategy = "none"      # "hide_aria", "reveal_aria", "partial_reveal"
default aria_hidden = True               # Is ARIA kept secret from everyone?
default trusted_with_aria = []           # List of characters who know about ARIA

# Intelligence Recruitment (Branching Point 2)
default accepted_intelligence = False    # Did Gary accept Guicciardini's offer?
default intelligence_missions = 0        # How many missions completed
default spy_reputation = 0               # Standing with intelligence services

# Leonardo Collaboration (Branching Point 3)
default leonardo_collaboration = "none"  # "all", "some", "withheld", "deceived"
default leonardo_innovations = []        # List of innovations shared

# Vatican Project (Branching Point 4)
default accepted_vatican = False         # Agreed to work for Pope?
default vatican_contributions = []       # What was contributed
default papal_favor = 0                  # Standing with Church

# Inquisition Response (Branching Point 5)
default inquisition_response = "none"    # "flee", "face", "hide"
default inquisition_caught = False       # Were they caught?
default escaped_discovery = False        # Did they successfully evade?

# Return Timing (Branching Point 6)
default return_timing = "none"           # "early", "planned", "forced", "never"
default left_early = False               # Left before making impact?
default months_in_past = 0               # Time spent in Renaissance

###############################################################################
# RELATIONSHIP SCORES - Character affinity tracking (0-100)
###############################################################################

# Core relationships
default benedetto_trust = 50
default guicciardini_trust = 50
default lorenzo_medici_trust = 50
default leonardo_trust = 50
default michelangelo_trust = 50
default pope_trust = 50

# Minor relationships
default pietro_friendship = 50
default capponi_respect = 50
default cardinal_rovere_opinion = 50

###############################################################################
# REPUTATION & IMPACT SCORES
###############################################################################

# Reputation metrics
default reputation = 0                   # Overall fame (0-100)
default scholar_reputation = 0           # Known as intellectual
default engineer_reputation = 0          # Known for technical work
default advisor_reputation = 0           # Known for counsel

# Impact on history
default innovation_score = 0             # Technical innovations introduced
default influence_score = 0              # Political/social influence
default historical_changes = 0           # Major historical alterations
default timeline_corrupted = 0           # Paradox risk counter

# Moral alignment
default corruption_score = 0             # Using power selfishly
default played_safe = False              # Avoided risks entirely

###############################################################################
# ARIA STATUS TRACKING
###############################################################################

default aria_discovered = False          # Has anyone discovered ARIA's true nature?
default aria_battery = 100               # Battery percentage
default aria_trust = 50                  # ARIA's trust in Gary's judgment
default aria_warnings_ignored = 0        # How many warnings dismissed

###############################################################################
# CHAPTER COMPLETION FLAGS
###############################################################################

default chapters_completed = []          # List of completed chapter numbers
default current_part = 1                 # Which part (1, 2, or 3)
default current_chapter = 1              # Current chapter number

###############################################################################
# PERSISTENT DATA - Saved across playthroughs
###############################################################################

default persistent.endings_unlocked = set()  # Which endings have been seen
default persistent.cg_unlocked = set()       # Which CGs have been viewed
default persistent.playthrough_count = 0     # Number of complete playthroughs
default persistent.best_ending_seen = False  # Has player seen legendary ending

###############################################################################
# SCENE VARIATION FLAGS - Minor choice tracking
###############################################################################

# Part 1 choices
default mr_bubbles_buried = False        # Did Gary finish burying the fish?
default first_impression = "confused"    # First impression in Florence
default benedetto_deal = 40              # Deal percentage negotiated
default chapter_1_complete = False       # Completed chapter 1?
default aria_revealed = "basic"          # How much revealed to Benedetto: "basic", "astronomy"

# Part 2 choices
default dinner_performance = "moderate"  # "failed", "moderate", "impressive", "legendary"
default revealed_eclipse = False         # Predicted the eclipse publicly?

# Part 3 choices
default st_peters_design = "standard"    # "standard", "ambitious", "revolutionary"
default final_collaborations = []        # Which artists worked with

###############################################################################
# HELPER VARIABLES
###############################################################################

default player_name = "Gary"             # In case we want customization later
default current_location = "modern"      # Track where we are for backgrounds
