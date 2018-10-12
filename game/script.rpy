define abs = Character("Abdullah")
define abt = Character("Abdullah", color="#336fce", what_color="#336fce")
define na = Character("Natalie")

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

    return
