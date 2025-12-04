###############################################################################
# THE CHRONICLER'S DEVICE - CHAPTERS 5 & 6
# Building Reputation in Florence
###############################################################################

label chapter_5:

    # Franco's carpentry problem - the first big test
    scene bg benedetto_shop with fade

    play music "audio/music/florence_day.ogg" fadein 2.0

    narrator "Three days into his new life as a Renaissance entrepreneur, Gary makes a discovery that will change everything."

    narrator "Renaissance people are really, really easy to impress."

    show gary renaissance neutral at right_pos
    show benedetto neutral at left_pos
    show aria neutral at aria_pos

    with dissolve

    benedetto "Gary! My neighbor Franco needs help. A carpentry problem he cannot solve."

    narrator "Franco the carpenter appears—a man with hands permanently stained with wood polish."

    show benedetto neutral at left_pos

    franco "It's driving me mad! I'm building a church pulpit with an octagonal base."

    franco "I've tried everything, measured a dozen times, but the pieces never fit right."

    narrator "Gary looks at Franco's rough sketches. It's a simple geometry problem that ARIA could solve in seconds."

    narrator "But this time, instead of obviously consulting his device, Gary has a better idea."

    # CHOICE: How to handle the first public problem
    menu:
        "How does Gary solve Franco's problem?"

        "Pretend to calculate it mentally":
            $ deception_strategy = "hide_aria"
            $ aria_hidden = True

            gary "May I?"

            narrator "Gary takes Franco's charcoal and studies the drawings with deep concentration."

            narrator "While pretending to think, he subtly activates ARIA in his pocket, reading the answer on the small screen."

            thoughts "135 degrees at each joint, not 130. Account for wood thickness..."

            gary "Ah. The issue is your corner angles. You need 135 degrees at each joint, not 130."

            gary "And your base measurements need to account for the wood thickness..."

            narrator "He writes out the solution, making it look like he's working through complex calculations in his head."

        "Credit the 'calculation device'":
            $ deception_strategy = "partial_reveal"
            $ aria_hidden = False

            gary "Let me consult my calculation device. It can solve geometry problems instantly."

            narrator "Gary openly uses ARIA, though he's careful not to reveal its true nature."

            aria "135 degrees at each joint. Adjust base measurements for wood thickness."

            gary "My device says 135 degrees at each joint, and you need to account for the wood thickness."

    narrator "Franco stares at Gary like he's just performed actual magic."

    franco "How did you... I've been working on this for weeks!"

    gary "It's just mathematics. Once you understand the underlying principles, these problems become quite straightforward."

    hide franco with dissolve

    narrator "Franco leaves shaking his head in amazement."

    narrator "Within hours, word spreads through the neighborhood that the strange northern scholar can solve impossible problems."

    if deception_strategy == "hide_aria":
        narrator "And best of all—everyone thinks the brilliance is coming from Gary himself."

        show aria neutral at aria_pos

        aria "Gary, I'm not sure this deception is wise. If people discover—"

        gary "They won't discover anything. As long as I'm careful, everyone will just think I'm the smartest person they've ever met."

        aria "And you're comfortable taking credit for knowledge you don't actually possess?"

        gary "Absolutely. Besides, I'm the one taking all the risks here."

        narrator "ARIA's screen flickers with digital frustration, but the AI doesn't argue further."

    scene black with fade
    pause 0.5

    narrator "Over the next week, Gary perfects his technique."

    narrator "He learns to activate ARIA without looking, to read responses while appearing deep in thought."

    narrator "The key is timing—pause just long enough to seem like he's working through complex calculations."

    narrator "The results are spectacular."

    jump chapter_6

###############################################################################
# CHAPTER 6 - The Rising Star
###############################################################################

label chapter_6:

    scene bg florence_market_day with fade

    show gary renaissance neutral at center_pos
    show benedetto neutral at left_pos
    show aria neutral at aria_pos

    with dissolve

    narrator "Two weeks have passed. Gary has solved increasingly complex problems for increasingly important people."

    narrator "What started with Franco's carpentry issue has escalated dramatically."

    benedetto "You have to see this. Word about your abilities has reached very interesting ears."

    gary "Whose ears specifically?"

    benedetto "Lorenzo Capponi. One of the wealthiest men in Florence."

    benedetto "He's heard about your eclipse prediction and wants to test your abilities personally."

    narrator "Gary feels a familiar thrill of excitement mixed with terror."

    thoughts "Lorenzo Capponi is exactly the kind of patron I've been hoping for..."

    thoughts "But he's also the kind of person who could have me executed if things go wrong."

    gary "What kind of test?"

    benedetto "He didn't say. But Gary, if you impress Lorenzo Capponi..."

    benedetto "You could find yourself with the kind of patronage that makes men legends."

    scene bg capponi_palazzo with fade

    show gary renaissance neutral at center_pos with dissolve

    narrator "The Capponi palazzo is less a house and more a statement about what happens when you have ridiculous amounts of money."

    narrator "The building rises four stories, its facade decorated with carved stone that looks crafted by angels."

    show benedetto neutral at left_pos with dissolve

    benedetto "Remember—be confident but respectful. Show your abilities, but don't seem arrogant."

    benedetto "And whatever you do, don't mention you're Norwegian."

    gary "Norwegian? What?"

    benedetto "I may have told them you're from Germania. It sounds more scholarly."

    scene bg capponi_study with fade

    show capponi neutral at center_pos with dissolve

    narrator "Lorenzo Capponi is exactly what Gary expected a Renaissance banking magnate to look like."

    narrator "Impeccably dressed, carefully groomed, with eyes that are always calculating something."

    capponi "So. You are the German scholar who claims to predict eclipses."

    show gary renaissance neutral at right_pos with dissolve

    gary "I don't claim to predict them. I do predict them."

    capponi "Confidence. I like that."

    capponi "Benedetto tells me you can solve problems that have stumped our finest minds."

    gary "I can certainly try."

    capponi "Good."

    narrator "Lorenzo walks to a wooden cabinet and withdraws a scroll covered with architectural drawings."

    capponi "Three months ago, I commissioned a new warehouse near the Arno."

    capponi "The architect assured me the foundation could support a four-story building filled with grain."

    capponi "However, my engineers now tell me there are... concerns."

    narrator "He unrolls the scroll, revealing incredibly complex architectural plans."

    capponi "They believe the building might collapse under full load."

    capponi "I've invested considerable money in this project. Before I invest more, I want to know:"

    capponi "Will my building stand or fall?"

    narrator "Gary looks at the drawings. This is exactly the kind of problem that will make or break his reputation."

    narrator "He pretends to study the drawings while subtly activating ARIA."

    gary "These measurements... May I ask about the soil composition where the foundation will be laid?"

    capponi "Clay mixed with river sand, approximately three braccia above the water table."

    narrator "ARIA processes the structural data. After a few moments, its verdict appears."

    narrator "The building would fail—but not for the reasons the Renaissance engineers suspected."

    gary "Your engineers are correct to be concerned. But they've identified the wrong problem."

    capponi "Explain."

    narrator "Gary points to specific sections of the drawings, channeling ARIA's analysis."

    gary "The foundation itself is adequate for the planned weight."

    gary "However, the load distribution through the wooden support beams creates stress concentrations at these points."

    gary "Under full grain load, these connections will fail progressively, causing catastrophic collapse."

    capponi "And the solution?"

    gary "Redistribute the load paths using diagonal bracing members here, here, and here."

    gary "Additionally, replace these wooden joints with iron reinforcements."

    gary "The cost will be significant, but far less than rebuilding after a collapse."

    capponi "How can you be certain of this analysis?"

    gary "Mathematics doesn't lie, Signore. The forces acting on this structure follow predictable laws."

    gary "Calculate them correctly, and the outcome becomes clear."

    narrator "Lorenzo calls for his head engineer—Maestro Roberto, gray-haired and skeptical."

    roberto "Signore, this approach... it addresses problems I hadn't even considered."

    roberto "The stress analysis on these joints..."

    narrator "Roberto looks at Gary with new respect."

    roberto "Where did you learn such advanced principles?"

    gary "Universities in Germania have made significant advances in structural mathematics."

    narrator "Which is technically true if you consider MIT to be in Germania and 520 years in the future."

    roberto "Remarkable. With these modifications, the building would be stronger than most palazzos in Florence."

    show capponi neutral

    capponi "It seems your reputation is well-deserved, Master Gary."

    capponi "Tell me, what are your plans in Florence? Do you have permanent patronage?"

    narrator "Gary's heart jumps. This is the moment he'd been working toward."

    gary "I'm currently... exploring opportunities."

    capponi "Then perhaps we should discuss a more formal arrangement."

    capponi "I have many projects that could benefit from your expertise."

    capponi "Architecture, trade route optimization, engineering challenges..."

    capponi "A man of your abilities should not be solving carpentry problems for street merchants."

    # CHOICE: Respond to patronage offer
    menu:
        "How does Gary respond?"

        "Accept eagerly":
            $ capponi_respect += 10
            $ reputation += 10

            gary "I would be honored to work under your patronage, Signore Capponi."

            capponi "Excellent. I knew you were a man of good judgment."

        "Negotiate carefully":
            $ capponi_respect += 5
            $ reputation += 5

            gary "I'm interested, but I'd want to understand the specific terms and expectations."

            capponi "A prudent approach. We can discuss details."

        "Express hesitation":
            $ capponi_respect -= 5
            $ played_safe = True

            gary "That's a generous offer. I'd need some time to consider..."

            capponi "Of course. Though opportunities like this don't wait forever."

    capponi "First, I'd like to demonstrate your capabilities to some associates of mine."

    capponi "There's a gathering tomorrow evening—influential people who appreciate intellectual achievement."

    gary "What kind of gathering?"

    capponi "A dinner party. Some of Florence's finest minds discussing current challenges."

    capponi "Your presence would be... enlightening for everyone involved."

    gary "I'd be honored to attend."

    capponi "Excellent. One more thing, Master Gary."

    capponi "My guests will undoubtedly want to test your abilities. Are you prepared to demonstrate your skills under... scrutiny?"

    gary "What kind of demonstration?"

    capponi "Nothing too challenging. Astronomical calculations, engineering problems, mathematical puzzles."

    capponi "The sort of intellectual entertainment that impresses educated people."

    narrator "Gary feels ARIA shift in his satchel. He can imagine the warnings being displayed."

    narrator "But he's feeling confident now. He just solved a complex structural engineering problem."

    gary "I'm ready for any challenge."

    capponi "I was hoping you'd say that."

    scene black with fade

    show text "{size=+20}END OF PART 1{/size}\n\n{size=+10}Gary has established himself in Florence and attracted the attention of powerful patrons.\n\nBut the real challenges are just beginning...{/size}" with dissolve

    pause 3.0

    hide text with dissolve

    # Update tracking
    $ current_part = 1
    $ months_in_past = 1

    jump part_2
