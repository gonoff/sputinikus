###############################################################################
# THE CHRONICLER'S DEVICE - PART 2: THE RENAISSANCE GENIUS
# Chapters 7 & 8: The Dinner Party
###############################################################################

label chapter_7:

    # Part 2 title card
    scene black with fade

    play music "audio/music/tension.ogg" fadein 2.0

    show text "{size=+20}Part 2{/size}\n\n{size=+15}The Renaissance Genius{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    scene bg benedetto_shop with fade

    show gary renaissance neutral at center_pos
    show benedetto neutral at left_pos

    with dissolve

    narrator "Benedetto spends most of the next day in barely controlled panic."

    narrator "He's running around Florence trying to acquire clothing appropriate for dining with what he keeps calling 'the most dangerous people in Italy.'"

    gary "Dangerous how?"

    benedetto "Dangerous like sharp knives hidden in silk purses."

    benedetto "These are not just wealthy men, Gary. They are the men who decide which other men get to remain wealthy."

    benedetto "Or alive."

    gary "You're being dramatic."

    benedetto "Am I? Let me tell you who will be at this dinner."

    narrator "Benedetto counts on his fingers."

    benedetto "Lorenzo Capponi, obviously."

    benedetto "Probably his cousin Alessandro, who once had a rival banker's entire family exiled for using the wrong color ink on a contract."

    benedetto "Giuliano de' Medici, who is charming, intelligent, and rumored to have personally strangled a man for looking at his wife incorrectly."

    gary "Anyone else I should worry about?"

    benedetto "Oh, certainly. Francesco Soderini, who can calculate interest rates in his head faster than most men can count to ten."

    benedetto "Possibly Niccolò Machiavelli, if he's in town—you may have heard of him?"

    narrator "Gary hadn't, but nods anyway."

    benedetto "And that's just the politicians and bankers."

    benedetto "There will also be artists, scholars, engineers—all of them brilliant, all of them competitive."

    benedetto "All of them looking for any opportunity to prove they're smarter than everyone else in the room."

    scene black with fade
    pause 0.5

    scene bg benedetto_shop with fade

    show gary renaissance neutral at center_pos
    show aria neutral at aria_pos

    with dissolve

    narrator "That evening, Gary prepares for the most important dinner of his life."

    gary "ARIA, please tell me you're ready for this."

    aria "Gary, I've been analyzing the social dynamics you're about to enter."

    aria "These Renaissance dinner parties were intellectual combat zones."

    aria "People's careers lived or died based on their performance at these gatherings."

    gary "But I have you. We can handle anything they throw at us."

    aria "That's what I'm afraid of. The more impressive you are, the more attention you'll attract."

    aria "And attention from powerful people in this era can be... problematic."

    narrator "Gary adjusts his cap and checks his appearance."

    narrator "He looks like a proper Renaissance scholar—educated but not wealthy, serious but approachable."

    gary "Don't worry so much. I've got this figured out."

    jump chapter_8

###############################################################################
# CHAPTER 8 - The Dinner Party
###############################################################################

label chapter_8:

    scene bg capponi_palazzo_dining with fade

    play music "audio/music/elegant_tension.ogg" fadein 2.0

    narrator "The Capponi palazzo looks even more impressive in the evening, lit by torches that create dramatic shadows."

    narrator "Gary and Benedetto are led through corridors designed to make visitors feel awed and intimidated."

    narrator "They arrive at a dining hall that could host a small army."

    narrator "Tonight it holds only a single long table set for perhaps a dozen people."

    narrator "The other guests are already seated, engaged in animated conversation that stops when Gary enters."

    show capponi neutral at center_pos with dissolve

    capponi "Gentlemen, allow me to present Master Gary of Germania, the scholar I mentioned."

    capponi "Master Gary, please join us."

    narrator "Gary finds himself seated between two of the most dangerous men in Florence."

    show giuliano_medici neutral at left_pos with dissolve

    giuliano_medici "So, Lorenzo tells us you can predict eclipses with mathematical precision."

    show gary renaissance neutral at right_pos with dissolve

    gary "Among other things."

    show machiavelli neutral at center_pos with dissolve

    machiavelli "How refreshing. Another scholar who claims to have discovered the secrets of celestial mechanics."

    narrator "There's something in Machiavelli's tone that suggests this isn't entirely a compliment."

    gary "I don't claim to have discovered anything. I simply apply mathematical principles that are... well-established in my homeland."

    machiavelli "Germania has made remarkable advances recently. Strange that we hear so little about these developments."

    gary "Knowledge travels slowly. Especially across the Alps."

    machiavelli "Indeed. Tell me, Master Gary, what do you think of the current political situation in Italy?"

    narrator "This is exactly the kind of question Gary had been dreading."

    narrator "His knowledge of Renaissance politics is limited to half-remembered history classes."

    # CHOICE: Political discussion
    menu:
        "How does Gary handle the political question?"

        "Be vague and diplomatic":
            $ reputation += 5

            gary "It's... complex."

            machiavelli "Complex. How diplomatic."

        "Attempt a mathematical analysis":
            $ reputation += 15
            $ innovation_score += 1

            gary "Before offering political advice, I would need to analyze the underlying mathematical structures."

            gary "Power distribution and resource allocation follow quantifiable patterns."

            machiavelli "Mathematical structures of power?"

            gary "Everything can be quantified. Political stability, economic efficiency, military effectiveness—"

            gary "They all follow mathematical laws. Most advisors rely on intuition. I prefer numbers."

            giuliano_medici "Show us. Give us an example."

            narrator "Gary settles on an approach that will let ARIA do most of the work."

            gary "Consider how influence compounds when properly invested, like interest in banking."

            gary "If you want to predict alliance stability, calculate benefit rates, trust decay over time, external pressure variables..."

            narrator "He starts explaining equations ARIA is feeding him through subtle vibrations."

            gary "This predicts the current Papal alliance with France will dissolve within eighteen months."

            gary "Incompatible benefit structures and accelerating trust decay."

            narrator "The silence at the table is absolute."

            machiavelli "You're suggesting we can predict political outcomes with the same precision we use for financial calculations?"

            gary "Why not? Human behavior follows patterns. Patterns can be quantified."

        "Deflect entirely":
            $ played_safe = True

            gary "I'm afraid politics isn't my area of expertise. I focus on engineering and mathematics."

            machiavelli "A man who knows his limitations. Refreshing, if somewhat disappointing."

    narrator "Lorenzo clears his throat."

    capponi "Gentlemen, perhaps we should test Master Gary's abilities more thoroughly?"

    narrator "A servant appears with a leather portfolio containing architectural drawings."

    capponi "These are engineering challenges currently facing Florence."

    capponi "The new bridge construction, the cathedral dome repairs, the water supply project."

    capponi "Each project has encountered problems that our finest engineers have been unable to solve."

    capponi "If your mathematical approach is as revolutionary as you suggest..."

    capponi "Surely you can provide solutions that have eluded our local experts?"

    narrator "Gary looks down at the engineering drawings and feels his confidence evaporate."

    narrator "These aren't simple geometry problems. These are complex, real-world challenges."

    narrator "That's when Gary notices something that makes his blood run cold."

    narrator "Sitting at the far end of the table, partially hidden in shadow, is a man who wasn't introduced."

    narrator "A man watching Gary with professional intensity."

    narrator "A man whose clothing and demeanor scream 'I work for people who ask pointed questions about suspicious foreigners.'"

    thoughts "Renaissance dinner parties come with their own version of secret police."

    thoughts "And they want me to prove I'm a genius. Right now."

    # The engineering challenge
    gary "The bridge project. May I examine this one first?"

    capponi "An excellent choice. The Ponte alle Grazie has developed structural problems."

    capponi "Our engineers have proposed several solutions, but none have proven satisfactory."

    narrator "Gary studies the drawings while subtly activating ARIA."

    gary "The original construction date?"

    unknown "Completed in 1237. Stone piers, wooden superstructure, fourteen arches."

    gary "And the specific failure points?"

    giuliano_medici "The seventh and ninth piers show signs of settling."

    giuliano_medici "The wooden deck shows stress fractures at three locations."

    giuliano_medici "Our engineers fear catastrophic failure during the next major flood."

    narrator "ARIA processes the data. The bridge problems are caused by differential settling."

    narrator "The AI provides specific recommendations for stabilization."

    gary "I see the issue. The problem isn't structural weakness—it's foundation inconsistency."

    narrator "Gary starts drawing diagrams showing how settling piers create stress concentrations."

    gary "The solution requires underpinning the affected piers with stone reinforcement."

    gary "Extend foundations to uniform depth. Install tension cables at these specific points..."

    narrator "As Gary explains, the faces around the table shift from skepticism to surprise to awe."

    show sangallo neutral at left_pos with dissolve

    sangallo "This approach to foundation stabilization... where did you encounter such techniques?"

    gary "The mathematical principles are universal. Once you understand load distribution and soil mechanics—"

    sangallo "Soil mechanics? I'm not familiar with this term."

    narrator "Gary realizes he just used a phrase that won't be invented for centuries."

    gary "The mathematical study of earth and stone behavior under load."

    sangallo "Remarkable. Such analysis could revolutionize construction throughout Italy."

    narrator "The mysterious note-taker speaks for the first time."

    show guicciardini neutral at center_pos with dissolve

    guicciardini "Master Gary. Your knowledge seems remarkably... comprehensive for a traveling scholar."

    narrator "Every person at the table turns to look at the speaker."

    narrator "Gary suddenly understands this man is more important than all the other dangerous people combined."

    gary "I beg your pardon?"

    guicciardini "Simply an observation. Your analytical methods are quite advanced."

    guicciardini "Far beyond what we typically see from northern universities."

    gary "I've been fortunate to study with exceptional teachers."

    guicciardini "And these teachers developed these techniques themselves?"

    gary "Knowledge builds upon knowledge. Each generation advances beyond the previous."

    guicciardini "Certainly. Though such advances usually take decades or centuries."

    guicciardini "Your techniques suggest... remarkably rapid progress."

    narrator "The atmosphere has shifted. Underneath the intellectual excitement is growing tension."

    # Benedetto's save
    narrator "That's when Benedetto knocks over his wine cup."

    benedetto "Madonna mia! How clumsy of me!"

    narrator "The brief commotion gives Gary a moment to think."

    narrator "Instead of deflecting, he needs to go on the offensive."

    gary "Signore, I notice you've been documenting our conversation quite thoroughly."

    gary "Are you perhaps conducting some kind of evaluation?"

    guicciardini "Very observant, Master Gary."

    guicciardini "I am Francesco Guicciardini, and I serve various interested parties..."

    guicciardini "...who are curious about unusual visitors to Florence."

    narrator "Gary's blood turns to ice water."

    gary "I hope I haven't said anything to cause concern."

    guicciardini "On the contrary. You've said several things that are quite remarkable."

    guicciardini "Perhaps we could continue this conversation in a more... private setting?"

    # CHOICE: How to respond to Guicciardini
    menu:
        "How does Gary respond to Guicciardini's invitation?"

        "Accept cautiously":
            $ accepted_intelligence = True
            $ guicciardini_trust += 10

            gary "What kind of private setting?"

            guicciardini "The kind where we discuss how your remarkable abilities might serve Florence."

            guicciardini "...and her allies."

            narrator "Gary looks at Lorenzo, who nods encouragingly."

            gary "I'd be honored to serve Florence in any way I can."

            guicciardini "Excellent. Tomorrow morning, then. I'll send a carriage."

        "Try to decline politely":
            $ accepted_intelligence = False
            $ guicciardini_trust -= 10
            $ reputation -= 5

            gary "I'm flattered, but I'm just a scholar. I'm not sure I'd be suited for... official work."

            guicciardini "A modest answer. But I suspect you underestimate yourself."

            guicciardini "Perhaps we'll speak again when you've had time to consider."

            narrator "His tone suggests this isn't really optional."

        "Ask for more information":
            $ accepted_intelligence = True
            $ guicciardini_trust += 5

            gary "What exactly would serving Florence entail?"

            guicciardini "Analysis. Predictions. Solving problems that matter."

            guicciardini "The kind of work that makes men both wealthy and respected."

            gary "Then I'm interested in learning more."

            guicciardini "Good. Tomorrow morning."

    narrator "As the dinner party winds down, Gary realizes he's crossed a threshold."

    narrator "He's no longer just a time-traveling tourist pretending to be a scholar."

    if accepted_intelligence:
        narrator "He's about to become something much more dangerous."

    scene black with fade

    $ current_chapter = 8
    $ dinner_performance = "impressive"

    jump chapter_9
