﻿define a = Character("Abdullah")

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
    stop music fadeout 1.0
    jump prologue

label prologue:
    scene outside with Fade(1, 1, 3)
    window show
    with dissolve
    a "...And we're back."
    a "Back at Ressu, this magnificent school"
    a "With a bunch of placeholder text while the writers work on a script"

    show abdullah angry

    a "Hurry up"

    return
