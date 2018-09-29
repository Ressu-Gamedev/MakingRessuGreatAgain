define a = Character("Abdullah")
image black = "#000"

label start:
    scene black
    centered "{cps=15}{color=#fff}This visual novel is a work of fiction.{/color}{/cps}"
    centered "{cps=15}{color=#fff}Names, characters, places, events, and incidents are either the products of\nthe authors' imaginations or used in a fictitious manner.{/color}{/cps}"
    centered "{cps=15}{color=#fff}Any resemblance to actual persons, living or dead, or actual events is purely coincidental.{/color}{/cps}"
    centered "{cps=15}{color=#fff}If you disagree, please realise that none of the characters actually act like this in real life.\nWe do not take responsibility for anyone getting offended.{/color}{/cps}"

    scene outside with Dissolve(3)
    a "...And we're back."
    a "Back at Ressu, this magnificent school"
    a "With a bunch of placeholder text while the writers work on a script"

    show abdullah angry

    a "Hurry up"

    return
