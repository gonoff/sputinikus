###############################################################################
# THE CHRONICLER'S DEVICE - PART 3: THE LEGEND OF GARY
# Chapters 12-14: Rome and the Vatican
###############################################################################

label chapter_12:

    # Part 3 title card
    scene black with fade

    play music "audio/music/grandeur.ogg" fadein 2.0

    show text "{size=+20}Part 3{/size}\n\n{size=+15}The Legend of Gary{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    scene bg medici_palazzo with fade

    narrator "Winter 1505. Gary Sputnik has become the most famous person in Florence that most people have never heard of."

    narrator "His official position is 'Special Advisor to the Medici Family.'"

    narrator "His actual role is closer to 'Renaissance-era Technology Accelerator.'"

    show gary renaissance neutral at center_pos with dissolve

    narrator "The workshop palazzo the Medici provided has become the most productive research facility in 16th-century Europe."

    narrator "Gary works with Leonardo on engineering projects. He collaborates with architects on building techniques."

    narrator "He advises merchants on trade strategies that generate unprecedented profits."

    show lorenzo_medici neutral at left_pos with dissolve

    lorenzo "Master Gary, your work has exceeded every expectation."

    lorenzo "The economic strategies you recommended have increased our profits by three hundred percent."

    lorenzo "The military analysis you provided helped us avoid two potentially disastrous conflicts."

    lorenzo "The artistic innovations you've introduced are being copied throughout Italy."

    gary "I'm pleased the results have been satisfactory."

    lorenzo "More than satisfactory. Revolutionary."

    lorenzo "Which brings me to a proposition."

    lorenzo "Pope Julius is planning a major architectural project in Rome."

    lorenzo "Something that will demonstrate the Church's power and glory for centuries to come."

    lorenzo "He's requested our recommendation for a mathematical advisor."

    gary "You're recommending me?"

    lorenzo "If you're interested. This would be the highest-profile project in Christendom."

    lorenzo "Success could establish your reputation permanently."

    gary "What kind of architectural project?"

    lorenzo "A new basilica. St. Peter's Basilica, to replace the old one."

    lorenzo "It will be the largest church in the world. Designed to last for a thousand years."

    narrator "Gary's historical knowledge is fuzzy, but he knows St. Peter's Basilica is one of the most famous buildings in the world."

    narrator "The chance to influence its design using ARIA's capabilities..."

    # CHOICE: Vatican project
    menu:
        "Does Gary accept the Vatican commission?"

        "Accept eagerly":
            $ accepted_vatican = True
            $ papal_favor += 20
            $ reputation += 20

            gary "I accept. When do I begin?"

            lorenzo "Immediately. The Pope is eager to move forward."

        "Accept cautiously":
            $ accepted_vatican = True
            $ papal_favor += 10
            $ played_safe = True

            gary "This sounds significant. I'd want to understand the scope before committing."

            lorenzo "Of course. You'll have time to assess the project before making final decisions."

        "Decline the opportunity":
            $ accepted_vatican = False
            $ left_early = True

            gary "I'm honored, but I think my work in Florence should remain my focus."

            lorenzo "A surprising choice. But I respect your decision."

            narrator "By refusing the Vatican commission, Gary limits his impact on history."

            narrator "He continues his work in Florence, but never reaches the heights he might have."

            jump ending_early_return

    scene black with fade
    pause 0.5

    jump chapter_13

###############################################################################
# CHAPTER 13 - Divine Architecture
###############################################################################

label chapter_13:

    scene bg rome_city with fade

    play music "audio/music/rome_grandeur.ogg" fadein 2.0

    narrator "Rome in 1505 is like Florence's older, more dramatic sibling."

    narrator "Bigger, more impressive, and significantly more likely to have you executed for saying the wrong thing."

    show gary renaissance neutral at center_pos with dissolve

    narrator "Gary's first glimpse of the city comes as his carriage crests a hill."

    narrator "The sprawling metropolis spreads across seven hills, ancient ruins mixing with Renaissance palazzos."

    scene bg vatican_exterior with fade

    narrator "The Vatican is something else entirely."

    narrator "The current basilica, which Gary is here to help replace, is already enormous."

    narrator "The planned replacement will defy architectural possibility."

    scene bg vatican_corridor with fade

    show cardinal neutral at left_pos with dissolve

    cardinal "Master Gary, His Holiness is eager to discuss your mathematical approach to sacred architecture."

    show gary renaissance neutral at right_pos with dissolve

    gary "I'm honored by His Holiness's confidence."

    cardinal "Your reputation precedes you. The Medici speak very highly of your abilities."

    cardinal "And your work with Master Leonardo has attracted considerable attention."

    cardinal "The Holy Father's vision for the new basilica is ambitious."

    cardinal "A structure that will stand as testament to God's glory and the Church's eternal authority."

    cardinal "But the engineering challenges are... substantial."

    scene bg pope_chambers with fade

    show pope_julius neutral at center_pos with dissolve

    narrator "Pope Julius II is exactly what Gary expected a Renaissance pope to look like."

    narrator "Elderly but vigorous, dressed in robes that cost more than Gary's annual salary."

    narrator "Possessed of eyes that seem to see everything and judge most of it wanting."

    pope "Master Gary, we are told you can solve architectural problems that have confounded our finest engineers."

    show gary renaissance neutral at right_pos with dissolve

    gary "I try to apply mathematical principles to structural challenges, Your Holiness."

    pope "Good. Because we have challenges that require divine inspiration, human ingenuity, and mathematical precision."

    narrator "The Pope gestures to a table covered with architectural drawings."

    narrator "These aren't just building plans—they're blueprints for one of the most famous structures in human history."

    pope "Bramante has designed a basilica that will surpass every church in Christendom."

    pope "But there are engineering concerns about structural integrity and construction methodology."

    show bramante neutral at left_pos with dissolve

    narrator "Bramante, the chief architect, watches anxiously as Gary studies the plans."

    narrator "ARIA analyzes the drawings through Gary's satchel."

    narrator "The planned basilica is massive—a central dome larger than anything since ancient Rome."

    gary "The central dome presents significant challenges in terms of load distribution."

    pope "Precisely. Our engineers are concerned the weight cannot be adequately supported."

    narrator "Gary channels ARIA's sophisticated structural analysis."

    gary "The mathematical approach would involve distributing the dome's weight through reinforced buttresses."

    gary "Additionally, the dome construction could be lightened using hollow-brick techniques."

    gary "By calculating optimal void patterns within the brick structure..."

    gary "You can achieve approximately sixty percent weight reduction while maintaining full load-bearing capacity."

    bramante "These hollow-brick techniques... they would reduce weight without compromising integrity?"

    gary "Correct."

    bramante "Your Holiness, with these techniques, we could build a dome larger than the Pantheon."

    pope "How much larger?"

    gary "Approximately forty percent larger diameter, with significantly improved structural stability."

    narrator "The silence in the room is absolute."

    pope "You're suggesting we can build the largest dome in the history of architecture?"

    gary "I'm suggesting that mathematical optimization makes it not just possible, but practical."

    $ innovation_score += 5
    $ historical_changes += 3
    $ reputation += 25

    scene black with fade

    narrator "What follows is six months of the most intense architectural collaboration in human history."

    scene bg st_peters with fade

    show gary renaissance neutral at center_pos
    show bramante neutral at left_pos
    show pope_julius neutral at right_pos

    with dissolve

    narrator "Gary works with Bramante and a team of the finest engineers in Europe."

    narrator "They develop new methods for foundation construction."

    narrator "They create innovative approaches to dome construction."

    narrator "They establish mathematical principles for architectural proportion."

    show cg papal_audience with dissolve

    pope "Master Gary, I believe you may be divinely inspired."

    narrator "By spring of 1506, the new design for St. Peter's Basilica is complete."

    narrator "Gary has essentially become the Vatican's chief architectural consultant."

    hide cg with dissolve

    narrator "But his work in Rome has attracted attention from sources that make the Medici seem provincial."

    jump chapter_14

###############################################################################
# CHAPTER 14 - The Inquisition
###############################################################################

label chapter_14:

    scene bg vatican_corridor with fade

    play music "audio/music/danger.ogg" fadein 2.0

    show cardinal neutral at center_pos with dissolve

    cardinal "Master Gary, there are those who would like to understand the full scope of your capabilities."

    show gary renaissance neutral at right_pos with dissolve

    gary "What do you mean?"

    cardinal "Your mathematical methods have produced results that some consider... miraculous."

    cardinal "There are questions about the source of your knowledge."

    gary "Questions from whom?"

    cardinal "The Holy Office of the Inquisition."

    narrator "The word 'Inquisition' hits Gary like a physical blow."

    thoughts "The Inquisition is not an organization you want asking questions about suspiciously advanced knowledge."

    gary "What kind of questions?"

    cardinal "The kind that determine whether your abilities are divinely inspired or... otherwise."

    gary "What do they want?"

    cardinal "To meet with you. To understand your methods."

    cardinal "To determine the theological implications of your work."

    gary "When?"

    cardinal "Tomorrow."

    scene bg capponi_study with fade

    narrator "That evening, alone in his Vatican apartments, Gary has the most serious conversation of his life."

    show gary renaissance neutral at center_pos
    show aria neutral at aria_pos

    with dissolve

    aria "We need to go back. The Inquisition doesn't accept 'I'm just really good at math' as an explanation."

    gary "But we're so close to finishing the basilica design. And there are other projects—"

    aria "Gary, if the Inquisition decides you're practicing witchcraft or heresy, no amount of papal protection will save you."

    aria "They burned people for having the wrong opinions about transubstantiation."

    aria "What do you think they'll do to someone who claims to predict the future using mathematics?"

    narrator "Gary looks out at the construction site where work has begun on the new St. Peter's Basilica."

    narrator "His basilica. Designed with techniques that will make it the most advanced building in Europe."

    gary "But if we leave now, I'll never know how it turns out."

    aria "You'll see the impact when we return to 2025."

    aria "The question is whether you'll recognize the world we've helped create."

    # CHOICE: Face or flee the Inquisition
    menu:
        "What does Gary do about the Inquisition?"

        "Face the Inquisition":
            $ inquisition_response = "face"

            gary "I've done nothing wrong. I'll answer their questions honestly."

            aria "Gary, that's incredibly risky."

            gary "I've survived Renaissance politics so far. I can handle some questions."

            narrator "Gary decides to meet with the Inquisition, confident in his ability to talk his way out."

            narrator "It proves to be a fateful decision."

            jump inquisition_confrontation

        "Flee immediately":
            $ inquisition_response = "flee"
            $ escaped_discovery = True

            gary "You're right. We need to leave tonight."

            aria "I've calculated the safest route out of Rome."

            narrator "Gary decides to flee before the Inquisition can question him."

            jump chapter_15

        "Try to hide in Rome":
            $ inquisition_response = "hide"
            $ timeline_corrupted += 1

            gary "Maybe I can avoid them while still working on the project."

            aria "Gary, that's dangerous. They have resources to find you."

            narrator "Gary attempts to continue his work while evading the Inquisition."

            narrator "The stress and paranoia begin to affect his judgment."

            jump hiding_sequence

###############################################################################
# INQUISITION CONFRONTATION BRANCH
###############################################################################

label inquisition_confrontation:

    # Ominous scene transition
    scene bg inquisition_chamber with danger_flash

    play music "audio/music/tension_dark.ogg" fadein 2.0

    # Background slowly zooms in - creates tension
    show layer master at ominous_zoom

    narrator "The Inquisition chamber is designed to intimidate."

    narrator "Stone walls, flickering torches, and the knowledge that people have been condemned to death in this room."

    # Gary enters nervously
    show gary renaissance neutral at center_pos:
        nervous
    with dissolve

    narrator "Three inquisitors sit behind a heavy wooden table."

    narrator "Their expressions reveal nothing."

    # Shake on accusation
    show layer master at shake_light

    inquisitor "Master Gary di Sputnicus. You stand accused of possessing knowledge that exceeds natural human capability."

    gary "I possess knowledge gained through study and mathematical analysis."

    inquisitor "Knowledge that allows you to predict eclipses, military movements, and economic trends with impossible precision?"

    gary "Mathematics is a powerful tool, Father."

    inquisitor "Mathematics does not explain how a traveling scholar solves problems that confound our finest minds in moments."

    narrator "The lead inquisitor leans forward."

    inquisitor "Unless that scholar has made a compact with forces that should not be named."

    # CHOICE: How to defend yourself
    menu:
        "How does Gary defend himself?"

        "Claim divine inspiration":
            $ papal_favor += 10

            gary "Perhaps my abilities come from God, not from darkness."

            gary "Is it not possible that the Almighty has chosen to work through mathematics?"

            inquisitor "An interesting theological argument. One that will require... extensive examination."

        "Demonstrate ARIA's mechanical nature":
            $ aria_discovered = True

            gary "I have a device. A calculating machine. Nothing supernatural."

            narrator "Gary reveals ARIA, hoping to convince them it's merely an advanced tool."

            inquisitor "A device that thinks? That speaks? That knows the future?"

            inquisitor "This is precisely the evidence of witchcraft we suspected."

        "Refuse to answer":
            $ inquisition_caught = True

            gary "I refuse to dignify these accusations with responses."

            inquisitor "Defiance will not serve you well, Master Gary."

            narrator "The inquisitors exchange meaningful glances."

            narrator "Gary has made a terrible mistake."

            jump ending_inquisition

    narrator "The interrogation continues for hours. Days."

    narrator "Gary's answers are scrutinized, analyzed, and challenged."

    if aria_discovered:
        narrator "The discovery of ARIA raises more questions than it answers."
        narrator "The inquisitors cannot determine what it is, but they know it's dangerous."
        $ inquisition_caught = True
        jump ending_inquisition

    narrator "Eventually, Gary realizes he cannot win this battle."

    narrator "He needs to escape before the questioning becomes... physical."

    $ escaped_discovery = True

    jump chapter_15

###############################################################################
# HIDING SEQUENCE BRANCH
###############################################################################

label hiding_sequence:

    scene bg rome_city with fade

    narrator "Gary spends weeks in hiding, moving between safe houses."

    narrator "He continues to work on projects through intermediaries."

    narrator "But the constant fear takes its toll."

    show gary renaissance neutral at center_pos with dissolve

    aria "Gary, this isn't sustainable. We're making mistakes."

    gary "Just a little longer. The basilica plans are almost complete."

    narrator "But the Inquisition is patient, and their network is vast."

    narrator "One morning, Gary wakes to find his hiding place surrounded."

    $ inquisition_caught = True

    jump ending_inquisition
