define abs = Character("Abdullah")
define abt = Character("Abdullah", what_color="#336fce")
define abe = Character("Abdullah", what_size=52)
define na = Character("Natalie")
define ch = Character("Chong")
define pr = Character("Jaakko")
define qq = Character("???")

label splashscreen:
    scene splash
    with dissolve
    pause 2.5
    return

image disclaimer:
    "disclaimer1.png" with Fade(0.5, 0.5, 2)
    10.0
    "disclaimer2.png" with Fade(0.5, 0.5, 2)
    10.0
    "disclaimer3.png" with Fade(0.5, 0.5, 2)
    10.0
    "disclaimer4.png" with Fade(0.5, 0.5, 2)
    10.0

label start:
    window hide
    $ _game_menu_screen = None
    $ quick_menu = False
    play music "audio/projector.ogg" fadein 1.0
    scene disclaimer
    $ renpy.pause(52.0, hard=True)
    $ _game_menu_screen = "save_screen"
    $ quick_menu = True
    jump prologue

label prologue:
    stop music fadeout 1.0
    scene bg outside with Fade(1, 1, 3)
    window show
    with dissolve
    abt "Ah 'tis a most wonderful morning. Very nice weather!"
    abt "Such joy to come to school every day."
    abs "Oh, hey, who's that?"
    show natalie happy with dissolve
    na "Oh, hello Abdullah. How was your weekend?"
    abs "Pretty dank! I smashed a bunch of kids in Fortnite both days."
    show natalie disappointed
    na "That's great…"
    abt "Hmm, she looks disappointed."
    na "See you soon!"
    abs "See you in class."
    hide natalie with dissolve
    abt "Natalie… I want to be like her. She has all the money-power of the student council, and she's really good at math..."
    abt "Well, time's ticking; better get going to class."
    jump intro

label intro:
    scene bg inside with Fade(2, 1, 3)
    abt "It's the second week of school."
    abt "The summer break was pretty refreshing, but now I have to get back to hard work."
    abt "There are plenty of things waiting for me, from the EE, to my IAs, to the final exams..."
    abt "...to restoring the pride of Ressu, to the Student Council elections, to restoring the justice between the National and IB lines..."
    abt "...to, of course, my love."
    abt "A certain asian girl."
    show chong neutral with dissolve
    ch "Abdullahi! Have you done latest homework?"
    abe "AH!" with hpunch
    abt "No! That's not what I mean! Not Chong, the greatest math teacher of all time!"
    ch "You three homeworks behind already."
    ch "If u need help come to me."
    # TODO: HELP/HINT BUTTON
    abs "Uhh… How would I say this..."
    abt "I'm so fucked… Haven't done a single one this year."

    menu chongchoice:
        abt "What should I tell Chong…?"
        "No, I haven't.":
            ch "Nooooooooooooooooooooooooooooooooo..."
            ch "...oooooooooo problem! Just give it the next time, ok? But hurry."
            abs "Sorry, Chong."
            ch "You an IB2! Need to work for CAS, not CASH, you know!"
        "Of course!":
            ch "Wow, what a good IB student! Fill with academic honesty! Well, I look forward to seeing it in lesson."
            abt "Why the fuck did I do that? I just lied for no reason. That'll get me nowhere, especially with Chong!"
        "Ask for advice":
            ch "Honesty is best policy! You get far in life like that."
            abs "I suppose, yeah"
            jump chongchoice

    abs "Goodbye."
    ch "See you in the lesson!"
    hide chong with dissolve
    abt "Anyway, back to my thoughts… The asian girl who I set my eyes upon..."
    abt "The North Korean exchange student."
    abt "I hope I get to meet her soon."
    abs "Oh, shit! Class is starting!"
    jump villainintro

label villainintro:
    scene bg lunchroom with Fade(2, 1, 3)
    abt "My favourite vegetable soup! Such a bliss."
    abt "Reminds me of myself."
    abt "Oh, I think I can see someone in the distance..."
    show silhouette with moveinleft
    abe "HEY! IBRAHIIM BIN SULTAN OMAR ABDULLE!"
    abt "Never mind, it's those tiny pre-IBs infiltrating the lunchroom at 11:00 again."
    abe "PRE-IBS! GET THE FUCK OUT!"
    hide silhouette with dissolve
    abt "Are the lunch supervisors accepting bribes or what?"
    abt "Well, gonna go find a seat..."
    show president shocked with moveinright
    with hpunch
    with vpunch
    abe "AH!"
    qq "Ah!"
    abs "Huh?"
    qq "Oi anteeks! Oon tosi pahoillani, en halunnut..."
    abs "Huh? What are you saying? Who are you?"
    qq "Oh, you're ii-bee! No Finnish!"
    show president happy
    pr "My name's Jaakko."
    pr "I äm the one and only president of this school!"
    abt "???"
    pr "Haha! Just kidding. But I am running in the student council elections tomorrow!"
    abs "Oh, so am I!"
    show president neutral
    pr "How?"
    abs "What do you mean, how?"
    pr "Well, I see you do not know Finnish language."
    pr "What kind of president doesn't know Finnish?!"
    abs "Well, this IS an international school..."
    show president happy
    pr "And the president's position is only for the best of the best!"
    abs "Are you saying-{nw}"
    pr "No no! I'm sure you're a very good student!"
    abs "Alright, as you say."
    pr "Well, gotta go! Good luck for tomorrow then!"
    abs "See ya."
    jump tbc

label tbc:
    play music "audio/projector.ogg" fadein 1.0
    scene tbc with Fade(1, 1, 3)
    window hide
    $ _game_menu_screen = None
    $ quick_menu = False
    $ renpy.pause(10.0, hard=True)
    stop music fadeout 1.0
    $ _game_menu_screen = "save_screen"
    $ quick_menu = True
    return
