define a = Character("Abdullah")

label splashscreen:
    scene splash
    with dissolve
    pause 2.5
    return

label start:
    window hide
    scene disclaimer1 with Fade(0.5, 0.5, 2)
    $renpy.pause(4, hard=True)
    scene disclaimer2 with Fade(1, 0.5, 2)
    $renpy.pause(4, hard=True)
    scene disclaimer3 with Fade(1, 0.5, 2)
    $renpy.pause(4, hard=True)
    scene disclaimer4 with Fade(1, 0.5, 2)
    $renpy.pause(4, hard=True)

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
