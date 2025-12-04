###############################################################################
# THE CHRONICLER'S DEVICE - PART 2 CONTINUATION
# Chapters 9, 10, 11: Intelligence Recruitment
###############################################################################

label chapter_9:

    if not accepted_intelligence:
        # Skip intelligence recruitment if declined
        jump chapter_9_alt

    scene black with fade

    narrator "The carriage that arrives the next morning isn't the kind of vehicle that suggests friendly conversation."

    narrator "It's black, unmarked, and driven by a man whose expression suggests he learned customer service from gargoyles."

    scene bg florence_market_day with fade

    play music "audio/music/mysterious.ogg" fadein 2.0

    show gary renaissance neutral at center_pos
    show aria neutral at aria_pos

    with dissolve

    narrator "The windows are covered with thick curtains, preventing Gary from seeing where they're going."

    gary "This is either really good or really bad."

    aria "Gary, based on my analysis of last night's conversation..."

    aria "I believe you may have attracted the attention of Renaissance Italy's intelligence services."

    gary "We have intelligence services?"

    aria "Every major power in this period employs networks of spies, informants, and analysts."

    aria "Francesco Guicciardini is one of the most sophisticated political minds of his era."

    gary "What does he want with me?"

    aria "Probably to determine whether you're a valuable asset, a dangerous threat, or both."

    scene bg capponi_study with fade

    narrator "After twenty minutes, Gary is escorted through corridors that smell like old stone and important decisions."

    narrator "He's led into a circular chamber with a domed ceiling decorated with allegorical frescoes."

    narrator "Justice, Wisdom, and other concepts stare down at him."

    show guicciardini neutral at center_pos with dissolve

    guicciardini "Master Gary. Thank you for accepting my invitation."

    show gary renaissance neutral at right_pos with dissolve

    gary "Thank you for extending it."

    narrator "They both know it hadn't really been an invitation."

    guicciardini "I trust you slept well after our stimulating dinner conversation?"

    gary "Very well, thank you."

    guicciardini "Excellent. Clear thinking is essential for what we need to discuss."

    narrator "Guicciardini opens a leather portfolio filled with notes, diagrams, and Gary's name written in various scripts."

    guicciardini "I've spent the morning reviewing your remarkable demonstrations."

    guicciardini "Your engineering solutions were innovative and practical."

    guicciardini "Your political predictions were... intriguingly specific."

    guicciardini "Your mathematical methods appear to be centuries ahead of current practice."

    gary "You're very kind."

    guicciardini "I'm not being kind, Master Gary. I'm being accurate."

    guicciardini "Which brings us to an interesting question:"

    guicciardini "How does a traveling scholar from Germania possess knowledge that surpasses the finest minds in Italy?"

    gary "I've been blessed with exceptional teachers and access to... rare texts."

    guicciardini "What kind of rare texts?"

    gary "Ancient manuscripts. Greek works that survived the fall of Constantinople."

    gary "Mathematical treatises that most scholars haven't seen."

    narrator "It's a reasonable explanation—Constantinople's fall scattered Byzantine scholars across Europe."

    guicciardini "And these exceptional teachers developed these advanced techniques themselves?"

    gary "Knowledge builds upon knowledge. Sometimes a single insight can illuminate decades of understanding."

    guicciardini "Indeed. And you're willing to share this illumination with appropriate patrons?"

    gary "I serve those who appreciate learning and can put knowledge to good use."

    guicciardini "Excellent answer."

    narrator "Guicciardini closes the portfolio."

    guicciardini "Master Gary, I'm going to be direct with you."

    guicciardini "Florence faces challenges that require innovative solutions."

    guicciardini "Political challenges. Military challenges. Economic challenges."

    guicciardini "Men with your apparent abilities could be... invaluable in addressing these issues."

    gary "What kind of challenges?"

    guicciardini "The kind that determine whether Florence remains independent and prosperous..."

    guicciardini "...or becomes a footnote in someone else's history."

    narrator "Guicciardini walks to a large map showing Italy divided into dozens of territories."

    guicciardini "Italy is changing, Master Gary. Foreign armies cross our borders at will."

    guicciardini "The French control Milan. The Spanish threaten Naples."

    guicciardini "The Pope makes alliances with whoever offers the most gold this week."

    guicciardini "In such times, superior information and analysis can mean the difference between survival and conquest."

    gary "And you think I can provide superior analysis?"

    guicciardini "I think you demonstrated capabilities last night that could revolutionize strategic planning."

    narrator "Guicciardini pulls out another document covered with official seals."

    guicciardini "I'm prepared to offer you a position as consultant to the Florentine intelligence services."

    guicciardini "You would analyze political and military situations, predict economic trends..."

    guicciardini "...solve technical problems that support our strategic objectives."

    gary "What would that involve exactly?"

    guicciardini "Meetings with officials who need your expertise. Travel to locations where your skills prove useful."

    guicciardini "Occasional... special projects that require discretionary handling."

    # CHOICE: Negotiate terms
    menu:
        "How does Gary negotiate?"

        "Ask about compensation":
            $ spy_reputation += 5

            gary "What kind of compensation are we discussing?"

            guicciardini "The kind that makes men wealthy and respected."

            guicciardini "Formal patronage, private residence, access to the finest libraries and workshops."

            guicciardini "Introduction to scholars, artists, and political leaders throughout Italy."

            guicciardini "And of course... protection from those who might question your unconventional methods."

            gary "What kind of protection?"

            guicciardini "The kind that ensures your talents can be exercised without interference from less... enlightened authorities."

        "Ask about consequences of declining":
            $ spy_reputation -= 5

            gary "What happens if I decline this generous offer?"

            guicciardini "Why would you decline?"

            guicciardini "You're a scholar seeking patronage in a city famous for supporting exceptional minds."

            guicciardini "We're offering you everything you could possibly want."

            narrator "His smile doesn't change, but something in his eyes does."

        "Accept immediately":
            $ spy_reputation += 10
            $ guicciardini_trust += 10

            gary "I'm honored by your confidence in me. I accept."

            guicciardini "A decisive man. I appreciate that."

    narrator "Gary realizes Guicciardini is offering a deal:"

    narrator "Work for Florentine intelligence, and they'll protect him from uncomfortable questions."

    gary "I accept."

    guicciardini "Wonderful."

    narrator "Guicciardini presents documents written in Latin, covered with official seals."

    guicciardini "Just standard language. Confidentiality agreements, loyalty oaths, compensation details."

    narrator "Gary signs where indicated, trying to look like he understands what he's agreeing to."

    guicciardini "Welcome to the service of Florence, Master Gary."

    guicciardini "I believe this arrangement will prove beneficial for everyone involved."

    jump chapter_10

###############################################################################
# CHAPTER 9 ALTERNATE - If declined intelligence offer
###############################################################################

label chapter_9_alt:

    scene bg benedetto_shop with fade

    show gary renaissance neutral at center_pos
    show benedetto neutral at left_pos
    show aria neutral at aria_pos

    with dissolve

    narrator "Gary spends the next few days trying to avoid Guicciardini's attention."

    narrator "He focuses on smaller projects, building his reputation more carefully."

    benedetto "You made a mistake refusing Guicciardini's offer."

    gary "I don't want to be a spy, Benedetto. I just want to be a scholar."

    benedetto "In Florence, being a scholar means being useful to powerful men."

    benedetto "And powerful men don't like being refused."

    aria "He's right, Gary. Guicciardini will be watching you more closely now."

    aria "Every success you have will make him more curious about your methods."

    narrator "Despite his caution, Gary continues to solve problems and build his reputation."

    narrator "Word spreads about the German genius who can solve impossible challenges."

    narrator "And eventually, an opportunity arises that even careful Gary cannot refuse..."

    $ intelligence_missions = 0

    jump chapter_10

###############################################################################
# CHAPTER 10 - Meeting Leonardo
###############################################################################

label chapter_10:

    scene bg leonardo_workshop with dream_fade

    play music "audio/music/wonder.ogg" fadein 2.0

    narrator "A month has passed. Gary's reputation has grown beyond anything he'd imagined."

    narrator "He's solved engineering problems, predicted market trends, advised on construction projects."

    narrator "And now he stands before a door that represents everything he'd dreamed about when he first pressed that red button."

    # Gary enters with anticipation
    show gary renaissance neutral at center_pos:
        fade_rise
    with dissolve

    thoughts "Leonardo da Vinci's workshop. THE Leonardo da Vinci."

    # Background slowly zooms as wonder builds
    show layer master at bg_breathe

    narrator "The door opens to reveal a space that looks like a museum exhibit come to life."

    narrator "Drawings cover every surface. Models hang from the ceiling. Half-finished inventions crowd every corner."

    narrator "And in the center of it all stands a man with long gray hair and intense, curious eyes."

    # Leonardo's dramatic entrance
    show leonardo neutral at left_pos:
        dramatic_entrance
    with dissolve

    leonardo "So. You are the German who claims to understand mathematics better than our Italian scholars."

    gary "I don't claim to understand it better. Just... differently."

    leonardo "Differently."

    narrator "Leonardo walks in a slow circle around Gary, examining him like a specimen."

    leonardo "Lorenzo Capponi tells me you solved his warehouse problem in minutes."

    leonardo "Guicciardini says you predicted political outcomes with remarkable precision."

    leonardo "Sangallo believes your structural analysis techniques are centuries ahead of current practice."

    narrator "Leonardo stops directly in front of Gary."

    leonardo "Either you are the greatest genius since the ancient Greeks..."

    leonardo "...or you are hiding something."

    narrator "Gary feels his heart stop. Leonardo's eyes seem to pierce right through his carefully constructed persona."

    # CHOICE: How to handle Leonardo
    menu:
        "How does Gary respond to Leonardo?"

        "Maintain the deception":
            $ leonardo_collaboration = "withheld"
            $ leonardo_trust -= 10

            gary "I've simply been fortunate to study with exceptional teachers."

            leonardo "The same answer you've given everyone else."

            leonardo "I had hoped for something more... illuminating from a fellow seeker of truth."

            narrator "Leonardo's disappointment is palpable."

        "Partially reveal ARIA":
            $ leonardo_collaboration = "some"
            $ leonardo_trust += 20
            $ trusted_with_aria.append("leonardo")

            gary "Maestro Leonardo... may I show you something?"

            narrator "Gary slowly retrieves ARIA from his satchel."

            gary "I have a device. A calculating tool unlike anything this world has seen."

            gary "It can perform mathematical operations, analyze structures, predict outcomes..."

            leonardo "Show me."

            narrator "Gary demonstrates some of ARIA's capabilities—careful to present it as a mechanical tool, not artificial intelligence."

            leonardo "Extraordinary. The craftsmanship... the precision..."

            leonardo "This is not from Germania. This is not from anywhere in our world."

            gary "You're right. And I need you to keep this secret."

            leonardo "A secret shared between those who seek knowledge above all else. I accept these terms."

        "Tell the full truth":
            $ leonardo_collaboration = "all"
            $ leonardo_trust += 30
            $ trusted_with_aria.append("leonardo")
            $ aria_hidden = False

            gary "Maestro Leonardo, what I'm about to tell you must never leave this room."

            leonardo "I have kept many secrets. One more will not burden me."

            gary "I am not from Germania. I am from... the future. Over 500 years in the future."

            narrator "Leonardo is silent for a long moment."

            leonardo "That would explain much. The knowledge you possess, the techniques you demonstrate..."

            leonardo "They are not ahead of our time. They ARE from another time."

            gary "You believe me?"

            leonardo "I believe in evidence. And the evidence suggests your explanation is more plausible than any alternative."

            leonardo "Show me everything."

    narrator "What follows is either a cautious exchange of ideas or the beginning of history's most unlikely collaboration."

    if leonardo_collaboration == "all":
        # Dramatic CG reveal with Ken Burns
        show cg leonardo_collab at cg_reveal
        pause 0.3
        show cg leonardo_collab at ken_burns

        narrator "Gary and Leonardo spend hours together, exploring the possibilities."

        narrator "Leonardo's questions are brilliant, probing, endlessly curious."

        narrator "And with ARIA's help, Gary can actually answer most of them."

        leonardo "The mathematics of flight... I've worked on this for years..."

        gary "Your designs are sound, Maestro. With a few modifications..."

        narrator "Together, they begin to create things that neither could accomplish alone."

        $ innovation_score += 5
        $ historical_changes += 2

        # Triumphant flash as collaboration succeeds
        with revelation
        hide cg at cg_exit

    elif leonardo_collaboration == "some":
        narrator "Leonardo examines ARIA with the intense focus of a master craftsman."

        leonardo "I have many questions. But I understand the need for discretion."

        leonardo "Perhaps we can collaborate... carefully. Share knowledge that benefits us both."

        gary "I would be honored, Maestro."

        $ innovation_score += 3

    else:
        narrator "Leonardo steps back, his expression unreadable."

        leonardo "Very well. Keep your secrets."

        leonardo "But know this—I will discover the truth eventually."

        leonardo "I always do."

    scene black with fade

    $ months_in_past = 3

    jump chapter_11

###############################################################################
# CHAPTER 11 - The Eclipse
###############################################################################

label chapter_11:

    scene bg florence_market_day with fade

    play music "audio/music/anticipation.ogg" fadein 2.0

    narrator "September 27th arrives—the day Gary predicted the solar eclipse."

    narrator "Word has spread throughout Florence. Crowds gather in the piazzas, looking up at the sky."

    show gary renaissance neutral at center_pos with dissolve

    narrator "Gary stands in the Piazza della Signoria, surrounded by some of the most powerful people in Florence."

    show capponi neutral at left_pos
    show guicciardini neutral at right_pos

    with dissolve

    capponi "Are you certain about this, Master Gary?"

    gary "The mathematics are precise. The eclipse will begin at approximately two hours past noon."

    guicciardini "And if you're wrong?"

    narrator "Gary doesn't answer. If he's wrong, his reputation—and possibly his life—is over."

    narrator "The sun climbs toward its apex. Gary checks his mental clock against ARIA's calculations."

    narrator "Two hours past noon approaches."

    narrator "Then the sky begins to darken."

    # Eclipse effect - dramatic darkening
    show layer master at eclipse_darken

    play sound "audio/sfx/crowd_gasping.ogg"

    # CG with dramatic reveal
    show cg first_success at cg_reveal

    narrator "The moon slides across the face of the sun, exactly as Gary predicted."

    # Screen shake from crowd reaction
    show layer master at shake_light

    narrator "The crowd erupts in a mixture of awe and fear."

    narrator "Some people fall to their knees. Others point at Gary in amazement."

    unknown "He predicted it! The German predicted it!"

    unknown "It's a miracle!"

    unknown "Or witchcraft..."

    # Return to normal brightness
    show layer master at eclipse_brighten

    hide cg at cg_exit

    capponi "Extraordinary. Absolutely extraordinary."

    guicciardini "Your reputation is now beyond question, Master Gary."

    guicciardini "Which means you've become extremely valuable... and extremely dangerous."

    narrator "Gary feels the weight of what he's accomplished settle on his shoulders."

    narrator "He's no longer just an impressive scholar. He's a man who can predict the movements of the heavens."

    narrator "In Renaissance Italy, that kind of power attracts attention from everyone."

    narrator "Including people Gary hasn't even met yet."

    $ revealed_eclipse = True
    $ reputation += 30
    $ innovation_score += 2

    scene black with fade

    show text "{size=+20}END OF PART 2{/size}\n\n{size=+10}Gary has established himself as one of the most remarkable minds in Florence.\n\nBut his greatest challenges—and greatest opportunities—lie ahead.\n\nIn Part 3, Gary will face the Vatican, the Medici, and the question of whether he can change history without destroying it...{/size}" with dissolve

    pause 4.0

    hide text with dissolve

    $ current_part = 2

    jump part_3
