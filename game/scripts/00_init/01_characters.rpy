###############################################################################
# THE CHRONICLER'S DEVICE - CHARACTER DEFINITIONS
###############################################################################

###############################################################################
# MAIN CHARACTERS
###############################################################################

# Gary Sputnik - Protagonist
# 25-year-old software developer, time traveler
define gary = Character(
    "Gary",
    who_color="#4A90D9",
    who_bold=True,
    image="gary"
)

# ARIA - AI Device
# Helpful but increasingly concerned AI companion
define aria = Character(
    "ARIA",
    who_color="#00FFFF",
    who_italic=True,
    what_prefix="[",
    what_suffix="]",
    image="aria"
)

###############################################################################
# FLORENCE CHARACTERS
###############################################################################

# Benedetto - Merchant dealing in "interesting things"
define benedetto = Character(
    "Benedetto",
    who_color="#8B4513",
    image="benedetto"
)

# Pietro - Cart driver who first helps Gary
define pietro = Character(
    "Pietro",
    who_color="#654321",
    image="pietro"
)

# Lorenzo Capponi - Wealthy Florentine banker
define capponi = Character(
    "Lorenzo Capponi",
    who_color="#FFD700",
    image="capponi"
)

# Francesco Guicciardini - Intelligence official
define guicciardini = Character(
    "Francesco Guicciardini",
    who_color="#800000",
    image="guicciardini"
)

# Lorenzo de' Medici - Unofficial ruler of Florence
define lorenzo = Character(
    "Lorenzo de' Medici",
    who_color="#4B0082",
    who_bold=True,
    image="lorenzo_medici"
)

# Giuliano de' Medici - Lorenzo's brother
define giuliano_medici = Character(
    "Giuliano de' Medici",
    who_color="#6B238E",
    image="giuliano_medici"
)

###############################################################################
# ARTISTS & INTELLECTUALS
###############################################################################

# Leonardo da Vinci - The master
define leonardo = Character(
    "Leonardo da Vinci",
    who_color="#2E8B57",
    who_bold=True,
    image="leonardo"
)

# Michelangelo - Sculptor
define michelangelo = Character(
    "Michelangelo",
    who_color="#483D8B",
    image="michelangelo"
)

# Giuliano da Sangallo - Chief architect
define sangallo = Character(
    "Maestro Sangallo",
    who_color="#696969",
    image="sangallo"
)

# Niccolò Machiavelli - Political thinker
define machiavelli = Character(
    "Machiavelli",
    who_color="#2F4F4F",
    image="machiavelli"
)

###############################################################################
# ROME / VATICAN CHARACTERS
###############################################################################

# Pope Julius II
define pope = Character(
    "Pope Julius II",
    who_color="#FFFFFF",
    who_bold=True,
    what_color="#F5F5DC",
    image="pope_julius"
)

# Cardinal Giuliano della Rovere
define cardinal = Character(
    "Cardinal della Rovere",
    who_color="#8B0000",
    image="cardinal"
)

# Donato Bramante - Chief architect of St. Peter's
define bramante = Character(
    "Bramante",
    who_color="#A0522D",
    image="bramante"
)

###############################################################################
# MINOR / SUPPORTING CHARACTERS
###############################################################################

# Franco - Carpenter neighbor
define franco = Character(
    "Franco",
    who_color="#8B7355"
)

# Roberto - Engineer
define roberto = Character(
    "Maestro Roberto",
    who_color="#5F5F5F"
)

# Francesco Soderini - Banker
define soderini = Character(
    "Francesco Soderini",
    who_color="#B8860B"
)

# Inquisitor - unnamed threat
define inquisitor = Character(
    "Inquisitor",
    who_color="#2F2F2F",
    what_italic=True
)

###############################################################################
# SPECIAL SPEAKERS
###############################################################################

# Narration - No speaker
define narrator = Character(
    None,
    what_italic=True
)

# Historical documents / letters
define document = Character(
    None,
    what_color="#3C2415"
)

# ARIA's screen display (different from speech)
define aria_display = Character(
    None,
    what_color="#00FFFF",
    what_prefix=">>> ",
    what_suffix=" <<<"
)

# Internal monologue / thoughts
define thoughts = Character(
    None,
    what_italic=True,
    what_color="#AAAAAA"
)

# Unknown speaker
define unknown = Character(
    "???",
    who_color="#666666"
)

###############################################################################
# CHARACTER SPRITE DEFINITIONS - Gary
###############################################################################

# Gary sprites - Modern attire
image gary modern neutral = "images/characters/gary/gary_modern_neutral.png"
image gary modern excited = "images/characters/gary/gary_modern_excited.png"
image gary modern worried = "images/characters/gary/gary_modern_worried.png"

# Gary sprites - Renaissance attire
image gary renaissance neutral = "images/characters/gary/gary_renaissance_neutral.png"
image gary renaissance confident = "images/characters/gary/gary_renaissance_confident.png"
image gary renaissance nervous = "images/characters/gary/gary_renaissance_nervous.png"
image gary renaissance panicked = "images/characters/gary/gary_renaissance_panicked.png"
image gary renaissance triumphant = "images/characters/gary/gary_renaissance_triumphant.png"

###############################################################################
# CHARACTER SPRITE DEFINITIONS - ARIA
###############################################################################

image aria neutral = "images/characters/aria/aria_neutral.png"
image aria warning = "images/characters/aria/aria_warning.png"
image aria processing = "images/characters/aria/aria_processing.png"
image aria happy = "images/characters/aria/aria_happy.png"
image aria concerned = "images/characters/aria/aria_concerned.png"

###############################################################################
# CHARACTER SPRITE DEFINITIONS - Supporting Cast
###############################################################################

# Benedetto
image benedetto neutral = "images/characters/benedetto/benedetto_neutral.png"
image benedetto interested = "images/characters/benedetto/benedetto_interested.png"
image benedetto scheming = "images/characters/benedetto/benedetto_scheming.png"
image benedetto worried = "images/characters/benedetto/benedetto_worried.png"

# Pietro
image pietro neutral = "images/characters/pietro/pietro_neutral.png"
image pietro friendly = "images/characters/pietro/pietro_friendly.png"
image pietro surprised = "images/characters/pietro/pietro_surprised.png"

# Leonardo da Vinci
image leonardo neutral = "images/characters/leonardo/leonardo_neutral.png"
image leonardo intense = "images/characters/leonardo/leonardo_intense.png"
image leonardo excited = "images/characters/leonardo/leonardo_excited.png"
image leonardo skeptical = "images/characters/leonardo/leonardo_skeptical.png"

# Michelangelo
image michelangelo neutral = "images/characters/michelangelo/michelangelo_neutral.png"
image michelangelo impressed = "images/characters/michelangelo/michelangelo_impressed.png"
image michelangelo offended = "images/characters/michelangelo/michelangelo_offended.png"

# Lorenzo de' Medici
image lorenzo_medici neutral = "images/characters/lorenzo_medici/lorenzo_medici_neutral.png"
image lorenzo_medici pleased = "images/characters/lorenzo_medici/lorenzo_medici_pleased.png"
image lorenzo_medici calculating = "images/characters/lorenzo_medici/lorenzo_medici_calculating.png"
image lorenzo_medici suspicious = "images/characters/lorenzo_medici/lorenzo_medici_suspicious.png"

# Guicciardini
image guicciardini neutral = "images/characters/guicciardini/guicciardini_neutral.png"
image guicciardini interested = "images/characters/guicciardini/guicciardini_interested.png"
image guicciardini dangerous = "images/characters/guicciardini/guicciardini_dangerous.png"

# Pope Julius II
image pope_julius neutral = "images/characters/pope_julius/pope_julius_neutral.png"
image pope_julius impressed = "images/characters/pope_julius/pope_julius_impressed.png"
image pope_julius suspicious = "images/characters/pope_julius/pope_julius_suspicious.png"
image pope_julius angry = "images/characters/pope_julius/pope_julius_angry.png"

# Cardinal della Rovere
image cardinal neutral = "images/characters/cardinal/cardinal_neutral.png"
image cardinal warning = "images/characters/cardinal/cardinal_warning.png"

###############################################################################
# BACKGROUND IMAGE DEFINITIONS - Modern
###############################################################################

image bg gary_house = "images/backgrounds/modern/gary_house_interior.png"
image bg gary_backyard_day = "images/backgrounds/modern/gary_backyard_day.png"
image bg gary_backyard_rain = "images/backgrounds/modern/gary_backyard_rain.png"
image bg transformed_street = "images/backgrounds/modern/transformed_2025_street.png"
image bg transformed_home = "images/backgrounds/modern/transformed_2025_home.png"

###############################################################################
# BACKGROUND IMAGE DEFINITIONS - Florence
###############################################################################

image bg florence_alley = "images/backgrounds/florence/alley_arrival.png"
image bg florence_market_day = "images/backgrounds/florence/street_market_day.png"
image bg florence_market_night = "images/backgrounds/florence/street_market_night.png"
image bg benedetto_shop_ext = "images/backgrounds/florence/benedetto_shop_exterior.png"
image bg benedetto_shop = "images/backgrounds/florence/benedetto_shop_interior.png"
image bg capponi_palazzo = "images/backgrounds/florence/capponi_palazzo_exterior.png"
image bg capponi_dining = "images/backgrounds/florence/capponi_palazzo_dining.png"
image bg capponi_study = "images/backgrounds/florence/capponi_palazzo_study.png"
image bg medici_palazzo = "images/backgrounds/florence/medici_palazzo_interior.png"
image bg leonardo_workshop = "images/backgrounds/florence/leonardo_workshop.png"
image bg gary_workshop = "images/backgrounds/florence/gary_workshop_palazzo.png"
image bg countryside = "images/backgrounds/florence/countryside_departure.png"

###############################################################################
# BACKGROUND IMAGE DEFINITIONS - Rome
###############################################################################

image bg rome_city = "images/backgrounds/rome/rome_cityscape.png"
image bg vatican_exterior = "images/backgrounds/rome/vatican_exterior.png"
image bg vatican_corridor = "images/backgrounds/rome/vatican_corridor.png"
image bg pope_chambers = "images/backgrounds/rome/pope_chambers.png"
image bg st_peters = "images/backgrounds/rome/st_peters_construction.png"
image bg inquisition_chamber = "images/backgrounds/rome/inquisition_chamber.png"

###############################################################################
# CG (Event Illustration) DEFINITIONS
###############################################################################

image cg time_travel = "images/cg/cg_time_travel.png"
image cg first_success = "images/cg/cg_first_success.png"
image cg leonardo_collab = "images/cg/cg_leonardo_collaboration.png"
image cg medici_meeting = "images/cg/cg_medici_meeting.png"
image cg papal_audience = "images/cg/cg_papal_audience.png"
image cg ending_legendary = "images/cg/cg_ending_legendary.png"
image cg ending_fraud = "images/cg/cg_ending_fraud.png"
image cg ending_inquisition = "images/cg/cg_ending_inquisition.png"
image cg ending_limited = "images/cg/cg_ending_limited.png"
image cg ending_corruption = "images/cg/cg_ending_corruption.png"
image cg ending_paradox = "images/cg/cg_ending_paradox.png"
image cg ending_early = "images/cg/cg_ending_early.png"

###############################################################################
# SCREEN POSITIONS
###############################################################################

transform left_pos:
    xalign 0.2
    yalign 1.0

transform center_pos:
    xalign 0.5
    yalign 1.0

transform right_pos:
    xalign 0.8
    yalign 1.0

transform aria_pos:
    xalign 0.9
    yalign 0.3
    zoom 0.5
