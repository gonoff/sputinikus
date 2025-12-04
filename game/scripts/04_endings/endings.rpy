###############################################################################
# THE CHRONICLER'S DEVICE - ENDINGS
# All seven possible endings based on player choices
###############################################################################

###############################################################################
# ENDING 1: LEGENDARY (Best Ending - Golden Path)
###############################################################################

label ending_legendary:

    scene black with fade

    play music "audio/music/triumph.ogg" fadein 2.0

    show text "{size=+30}LEGENDARY ENDING{/size}\n\n{size=+15}The Immortal Genius{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show cg ending_legendary with dissolve

    narrator "Gary Sputnik achieved the impossible."

    narrator "He traveled through time, changed the course of human history, and returned to a world transformed by his actions."

    narrator "In the history books, Gary di Sputnicus is remembered as one of humanity's greatest minds."

    narrator "A Renaissance genius whose mathematical innovations accelerated civilization by centuries."

    narrator "A collaborator with Leonardo da Vinci who revolutionized art and engineering."

    narrator "A mysterious figure who appeared from nowhere and vanished into legend."

    narrator "In his own time, Gary is wealthy, respected, and influential."

    narrator "He lives in a world made better by his own efforts—a world where his potential was recognized and nurtured."

    narrator "But most importantly, Gary knows the truth."

    narrator "He knows that one person, with the right knowledge and the courage to act, can change everything."

    narrator "And as he holds the time travel device in his hands, he wonders..."

    narrator "What else could be changed? What else could be improved?"

    narrator "What other adventures await in the infinite corridors of time?"

    hide cg with dissolve

    scene black

    show text "{size=+20}THE END{/size}\n\n{size=+10}...or perhaps, THE BEGINNING?{/size}\n\n{size=+5}Gary Sputnik had discovered that the past was not just history—\nit was raw material for building a better future.\n\nAnd he was just getting started.{/size}" with dissolve

    pause 5.0

    $ persistent.endings_unlocked.add("legendary")
    $ persistent.best_ending_seen = True

    jump game_over

###############################################################################
# ENDING 2: FRAUD EXPOSED
###############################################################################

label ending_fraud_exposed:

    scene black with fade

    play music "audio/music/melancholy.ogg" fadein 2.0

    show text "{size=+30}FRAUD EXPOSED{/size}\n\n{size=+15}The Fall of the False Genius{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show cg ending_fraud with dissolve

    narrator "It was bound to happen eventually."

    narrator "Someone noticed the way Gary always paused before answering. The way he seemed to consult something hidden in his satchel."

    narrator "The way his knowledge was too perfect, too comprehensive, too... impossible."

    narrator "When they searched his belongings and found ARIA, the game was over."

    narrator "They couldn't understand what the device was, but they knew Gary's genius was a lie."

    narrator "The brilliant scholar who had amazed Renaissance Italy was nothing but a fraud with a magical box."

    narrator "Gary fled in disgrace, barely escaping with his life."

    narrator "He returned to 2025 to find that history remembered him differently here."

    narrator "Not as a genius, but as a cautionary tale about deception and hubris."

    narrator "'Gary the Pretender,' they called him. 'The Charlatan of Florence.'"

    narrator "The innovations he'd introduced still existed, but they were attributed to others."

    narrator "The people who discovered his techniques after his disgrace got the credit."

    narrator "Gary lives out his days in obscurity, knowing what he could have achieved..."

    narrator "...if only he'd been more careful."

    hide cg with dissolve

    scene black

    show text "{size=+20}THE END{/size}\n\n{size=+10}Fame built on deception crumbles eventually.\nGary learned this the hard way.{/size}" with dissolve

    pause 4.0

    $ persistent.endings_unlocked.add("fraud_exposed")

    jump game_over

###############################################################################
# ENDING 3: INQUISITION
###############################################################################

label ending_inquisition:

    scene black with fade

    play music "audio/music/dark_fate.ogg" fadein 2.0

    show text "{size=+30}INQUISITION{/size}\n\n{size=+15}The Price of Knowledge{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show cg ending_inquisition with dissolve

    narrator "The Holy Office of the Inquisition had dealt with witches, heretics, and blasphemers."

    narrator "They had never encountered anything like Gary Sputnik."

    narrator "A man who claimed his impossible knowledge came from mathematics."

    narrator "A man whose device spoke with a voice that was not human."

    narrator "A man who knew things that no mortal should know."

    narrator "The trial lasted weeks. Gary tried everything—claiming divine inspiration, demonstrating ARIA's mechanical nature, refusing to answer questions."

    narrator "None of it mattered."

    narrator "In the end, the Inquisitors concluded that Gary's abilities were supernatural in origin."

    narrator "And supernatural abilities that didn't come from God could only come from one other source."

    narrator "Gary Sputnik, known to history as Gary di Sputnicus, was declared a heretic and an agent of darkness."

    narrator "His innovations were suppressed. His collaborators were investigated."

    narrator "The advances he'd introduced were set back by decades as the Church worked to erase his influence."

    narrator "Gary himself... well, the historical records simply say he 'disappeared' after his trial."

    narrator "The time travel device was never found."

    hide cg with dissolve

    scene black

    show text "{size=+20}THE END{/size}\n\n{size=+10}Some powers are not meant to be challenged.\nGary discovered this too late.{/size}" with dissolve

    pause 4.0

    $ persistent.endings_unlocked.add("inquisition")

    jump game_over

###############################################################################
# ENDING 4: LIMITED IMPACT
###############################################################################

label ending_limited_impact:

    scene black with fade

    play music "audio/music/bittersweet.ogg" fadein 2.0

    show text "{size=+30}LIMITED IMPACT{/size}\n\n{size=+15}A Footnote in History{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show cg ending_limited with dissolve

    narrator "Gary returned to 2025 to find... not much had changed."

    narrator "Oh, there were differences. Small ones. Historians mentioned a German scholar named Gary di Sputnicus who had done interesting work in Renaissance Florence."

    narrator "A few innovations could be traced back to his influence. A handful of techniques bore his name."

    narrator "But Gary had been too careful. Too cautious. Too afraid of the risks."

    narrator "He'd introduced improvements gradually, avoided drawing too much attention, never pushed the boundaries of what was possible."

    narrator "As a result, his impact on history was modest at best."

    narrator "Gary's own life was slightly better—a bit more money, a bit more respect—but nothing dramatic."

    narrator "He'd traveled 500 years into the past, worked with Leonardo da Vinci, advised the Medici..."

    narrator "And all he had to show for it was a footnote in obscure historical texts."

    narrator "Sometimes, playing it safe is the biggest risk of all."

    hide cg with dissolve

    scene black

    show text "{size=+20}THE END{/size}\n\n{size=+10}Gary had the chance to change history.\nHe chose not to take it.{/size}" with dissolve

    pause 4.0

    $ persistent.endings_unlocked.add("limited_impact")

    jump game_over

###############################################################################
# ENDING 5: CORRUPTION
###############################################################################

label ending_corruption:

    scene black with fade

    play music "audio/music/dark_power.ogg" fadein 2.0

    show text "{size=+30}CORRUPTION{/size}\n\n{size=+15}The Tyrant's Rise{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show cg ending_corruption with dissolve

    narrator "Power corrupts. Absolute knowledge corrupts absolutely."

    narrator "Gary had started with good intentions, but somewhere along the way, things changed."

    narrator "Why just advise the powerful when you could become powerful yourself?"

    narrator "Why just predict the future when you could shape it to your advantage?"

    narrator "Gary used ARIA's capabilities not to advance civilization, but to advance himself."

    narrator "He manipulated markets, engineered political outcomes, destroyed rivals."

    narrator "He became the shadow behind the thrones of Renaissance Italy."

    narrator "When Gary returned to 2025, he found a world shaped by his ambition."

    narrator "A world where the Sputnik family had been powerful for centuries."

    narrator "A world where Gary was wealthy beyond imagination, but feared rather than respected."

    narrator "A world where innovation served the few instead of the many."

    narrator "Gary had everything he'd ever wanted."

    narrator "Except the ability to look at himself in the mirror."

    hide cg with dissolve

    scene black

    show text "{size=+20}THE END{/size}\n\n{size=+10}Gary got everything he wanted.\nIt was exactly what he deserved.{/size}" with dissolve

    pause 4.0

    $ persistent.endings_unlocked.add("corruption")

    jump game_over

###############################################################################
# ENDING 6: PARADOX
###############################################################################

label ending_paradox:

    scene black with fade

    play music "audio/music/chaos.ogg" fadein 2.0

    show text "{size=+30}PARADOX{/size}\n\n{size=+15}The Broken Timeline{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show cg ending_paradox with dissolve

    narrator "ARIA had warned him. The AI had calculated the risks, identified the dangers, pleaded with Gary to be more careful."

    narrator "But Gary kept pushing. More innovations. Bigger changes. Faster progress."

    narrator "Each modification to history created ripples. Ripples became waves. Waves became tsunamis."

    narrator "And somewhere, somewhen, the accumulated changes broke something fundamental."

    narrator "When Gary activated the time travel device to return home, the universe... hiccuped."

    narrator "He arrived in 2025, but it wasn't the 2025 he'd left. It wasn't any 2025 that should exist."

    narrator "Technology was advanced in some ways, primitive in others. Languages had evolved strangely."

    narrator "Historical events Gary remembered had happened differently, or not at all."

    narrator "He'd created so many changes that history had fractured, forking into a timeline that made no logical sense."

    narrator "Gary was alone in a world he didn't understand, with no way to fix what he'd broken."

    narrator "The time travel device, damaged by the paradox, would never work again."

    narrator "Gary di Sputnicus, Gary Sputnik, was trapped in a reality of his own making."

    hide cg with dissolve

    scene black

    show text "{size=+20}THE END{/size}\n\n{size=+10}Time is a river, not a pool.\nYou cannot change it without consequences.{/size}" with dissolve

    pause 4.0

    $ persistent.endings_unlocked.add("paradox")

    jump game_over

###############################################################################
# ENDING 7: EARLY RETURN
###############################################################################

label ending_early_return:

    scene black with fade

    play music "audio/music/quiet_regret.ogg" fadein 2.0

    show text "{size=+30}EARLY RETURN{/size}\n\n{size=+15}The Road Not Taken{/size}" with dissolve
    pause 2.0
    hide text with dissolve

    show cg ending_early with dissolve

    narrator "Gary made a choice. He chose safety over adventure. Certainty over risk."

    narrator "When the opportunities grew too dangerous, the stakes too high, he retreated."

    narrator "He returned to 2025 having barely scratched the surface of what was possible."

    narrator "The world he came back to was almost identical to the one he'd left."

    narrator "His trip to Renaissance Italy was barely a blip in history—a curious story about a strange German scholar who appeared briefly and then vanished."

    narrator "No innovations attributed to his name. No lasting changes to civilization."

    narrator "Just a man who went to the past and came back without leaving a mark."

    narrator "Gary's life continued as before. Same job. Same apartment. Same unremarkable existence."

    narrator "But now he knew what he could have done. What he could have been."

    narrator "And that knowledge haunted him for the rest of his days."

    narrator "The time travel device sat in his closet, gathering dust."

    narrator "A reminder of the adventure he was too afraid to finish."

    hide cg with dissolve

    scene black

    show text "{size=+20}THE END{/size}\n\n{size=+10}Some opportunities only come once.\nGary let his slip away.{/size}" with dissolve

    pause 4.0

    $ persistent.endings_unlocked.add("early_return")

    jump game_over
