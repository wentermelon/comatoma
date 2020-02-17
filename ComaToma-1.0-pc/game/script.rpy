define toma = Character('Toma')
define mom = Character('Mom', color="#AD6D82")
define harry = Character('Harry', color="#387BB6")
define jenny = Character('Jenny', color="#B64F61")
define monster = Character('???')
define aspie = Character('Aspie', color="#9643F1")
define krius = Character('Krius', color="#25CFAF")
define sprite_1 = Character('Popular Sprite A', color="#48FF00")
define sprite_2 = Character('Popular Sprite B', color="#FF0087")

image bg forest normal = im.FactorScale("bg/bg forest normal.png", 0.25)
image bg tea party = im.FactorScale("bg/bg tea party normal.png", 0.25)
image bg forest evil = im.FactorScale("bg/bg forest evil.png", 0.5)
image bg bedroom = im.FactorScale("bg/bg bedroom.png", 0.25)

image toma = im.FactorScale("characters/toma/toma normal.png", 0.35)
image toma_happy = im.FactorScale("characters/toma/toma happy.png", 0.35)
image mom = im.FactorScale("characters/mom/mom normal.png", 0.4)
image harry = im.FactorScale("characters/harry/harry normal.png", 0.3)
image harry angry = im.FactorScale("characters/harry/harry angry.png", 0.3)
image jenny = im.FactorScale("characters/sprites/jenny normal.png", 0.3)
image aspie = im.FactorScale("characters/sprites/aspie normal.png", 0.3)
image krius = im.FactorScale("characters/sprites/krius normal.png", 0.3)
image krius_sad = im.FactorScale("characters/sprites/krius sad.png", 0.3)
image krius_stache = im.FactorScale("characters/sprites/krius stache.png", 0.3)
image sprite_1 = im.FactorScale("characters/sprites/sprite 1 normal.png", 0.3)
image sprite_2 = im.FactorScale("characters/sprites/sprite 2 normal.png", 0.3)
image sprite_evil = im.FactorScale("characters/sprites/sprite evil normal.png", 1.0)
image salt_small = im.FactorScale("salty.png", 0.3)
image salt_mini = im.FactorScale("salty.png", 0.3)
image salt_big = im.FactorScale("salty.png", 0.5)

transform bounce:
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    repeat 2

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"
        background im.FactorScale("gui/main_menu.png", 0.5)

    text "ComaToma" size 180 xalign 0.5 yalign 0.4 font "AmaticSC-Regular.ttf"

    # The main menu buttons.
    frame:
        style_prefix "mm"
        xalign 0.5
        yalign 0.75

        has vbox
        textbutton _("Start Game") action Start()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("About") action ShowMenu("about")
        textbutton _("Quit") action Quit(confirm=False)

style mm_button:
    size_group "mm"

label start:
    $ sprite_num = 0

    stop music fadeout 1.0
    scene bg bedroom
    show bg bedroom
    with Fade(1.0, 0.5, 0.5)

    show toma:
        xalign 0.5 yalign 1.0 alpha 0.0
        linear 0.5 alpha 1.0

    toma "Why can't I stay home?"

    show toma:
        xalign 0.5 yalign 1.0
        linear 0.5 xalign 0.25

    show mom:
        xalign 0.5 yalign 0.75 alpha 0.0
        linear 0.5 xalign 0.75 yalign 0.75 alpha 1.0

    mom "School is important, honey. I'm sure you'll meet someo-"

    toma "Everyday's the same ..."
    toma "...Why am I even here?"

    mom "Toma, you've barely slept for weeks. It's okay to be anxious but we also have to work on your problem at school - making friends."

    toma "But they won't like me ... I know they won't ..."
    toma "I don't exist to them."

    mom "(sigh)"

    mom "Here."

    "Toma's mother passes a small pill to Toma."

    mom "Just this once, I'll let you have this. It will help you have a long, nice sleep. We'll talk more in the morning."

    toma "Good night, mama."

    mom "Good night, Toma."

    show toma:
        linear 1.0 alpha 0.0
    show mom:
        linear 1.0 alpha 0.0

    "As he takes the pills, Toma soon falls into a spiral of deep sleep... as if he was in a coma."
    "Until..."

label dream_start:

    scene black
    with Fade(1.5, 0.5, 1.0)

    "???" "Psst, Toma ..."
    with Move( (10, 0), (-10, 0), 0.1, bounce=True, repeat=True, delay=0.275 )

    "???" "Psssst ..."
    with Move( (20, 0), (-20, 0), 0.1, bounce=True, repeat=True, delay=0.5 )

    "???" "By my heavenly strands, wake up!"
    with Move( (50, 0), (-50, 0), 0.1, bounce=True, repeat=True, delay=0.75 )


    play music "audio/forest_day.mp3" fadein 1.0 fadeout 1.0 loop
    scene bg forest normal
    with dissolve

    "Toma wakes up."

    show toma:
        xalign 0.25 yalign 1.0 alpha 0.0
        linear 0.5 alpha 1.0

    show harry:
        xalign 0.75 yalign 0.4 alpha 0.0
        linear 0.5 alpha 1.0
        bounce

    harry "Finally! A fine morning, my boy!"

    toma "Who ... who are you?"

    show harry:
        bounce

    harry "Why, I'm Harry, of course! Your one and only moustachio, at your service!"
    harry "Anyhow, your fellow sprites are waiting for you outside!"

    toma "...My friends?"

    harry "That's for you to decide. Although, I feel like you shouldn-"

    show toma:
        linear 5.0 xalign -10.0

    "Toma excitedly runs off."

    harry "What an energetic boy..."

label jenny:
    scene bg forest normal
    with dissolve

    show toma_happy:
        xalign 2.0 yalign 1.0
        linear 2.0 xalign 1.1

    show harry:
        xalign 1.8 yalign 0.15
        linear 2.0 xalign 0.8

    $ renpy.pause( 2.0, hard=True )

    show sprite_1:
        xalign 0.7 yalign 0.5 alpha 0.0
        linear 0.5 alpha 1.0
        bounce
    sprite_1 "Toma, what took you so long?"

    show sprite_2:
        xalign 0.6 yalign 0.6 alpha 0.0
        linear 0.5 alpha 1.0
        bounce
    sprite_2 "Yeah! You know we can't play without you!"

    toma "Sorry, guys but I'm ready now! Let's go!"

    show jenny:
        xalign 0.0 yalign 0.6
        linear 1.0 xalign 0.4

    $ renpy.pause( 1.0, hard=True )

    with hpunch
    jenny "HELP!!"

    stop music fadeout 1.0
    play music "audio/forest_night.mp3" fadein 1.0 fadeout 1.0 loop

    show sprite_evil:
        xalign -5.0
        linear 2.0 xalign -0.5

    show toma_happy:
        linear 1.0 alpha 0.0

    show toma:
        xalign 1.1 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0

    show harry:
        bounce
    harry "That's Jenny! Quickly, Toma! We must go help her!"

    show sprite_1:
        bounce
    sprite_1 "She's marked by the Dark One! Let her be eaten!"

    show sprite_2:
        bounce
    sprite_2 "We can't get it too! Better her than us!"

    show sprite_1:
        bounce
    sprite_1 "Is she even a sprite?! She's cursed!"

    show sprite_2:
        bounce
    sprite_2 "Let's leave, Toma!"

    show harry:
        bounce
    harry "Nonsense! Toma, what should we do?"

    menu:
        "Run away!":
            jump jenny_bad

        "Help the sprite!":
            jump jenny_good

label jenny_good:

    $ sprite_num += 1

    toma "Hey! Leave her alone!"

    monster "..."

    show salt_small:
        xalign 0.8 yalign 0.15 alpha 0.0
        linear 1.0 alpha 1.0 rotate 360.0
        linear 1.0 rotate 720.0 xalign -0.5

    $ renpy.pause( 2.0, hard=True )
    with hpunch
    show sprite_evil:
        bounce
    harry "*throws salt shaker*"

    show harry:
        bounce
    harry "Check your pockets, Toma!"
    hide salt_small

    "Toma check his pockets and finds a salt shaker just like the one Harry threw..."

    show salt_small:
        xalign 1.0 yalign 0.9 alpha 0.0
        linear 1.0 alpha 1.0
        linear 1.0 rotate 945.0 xalign 0.1 yalign 0.0
        bounce
        linear 1.0 alpha 0.0
    $ renpy.pause( 3.0, hard=True )
    with vpunch
    show sprite_evil:
        bounce
    toma "*throws salt shaker*"

    show harry:
        bounce
    harry "It's working!"

    stop music fadeout 1.0
    play music "audio/forest_day.mp3" fadein 1.0 fadeout 1.0 loop

    show sprite_evil:
        linear 10.0 xalign -10.0

    show sprite_1:
        bounce
    sprite_1 "She's coming!"

    show sprite_2:
        bounce
    sprite_2 "Ugh, we're leaving!"

    show sprite_1:
        linear 10.7 xalign 10.7

    show sprite_2:
        linear 10.6 xalign 10.6

    harry "Those selfish cowards..."
    harry "Are you alright?"
    jenny "Thank you, Harry and ... whoever you are."
    toma "Toma. And you are?"
    jenny "I'm Jenny."

    show toma:
        linear 1.0 alpha 0.0

    show toma_happy:
        xalign 1.1 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0

    jenny "Toma, you have a lovely name and a big heart."
    toma "It's only right to help those in need..."
    jenny "Still. I won't forget it."
    jenny "Thank you."

    scene black
    with fade
    "Harry escorts Jenny home while Toma continues to walk through the forest alone and stumbles upon a small party."

    jump aspie

label jenny_bad:

    toma "It's none of our business, let's run!"

    show harry:
        bounce
    harry "She's a sprite, just like you!"

    show sprite_1:
        bounce
    sprite_1 "Oh please, Moustachio. Toma's smarter than that."

    show sprite_2:
        bounce
    sprite_2 "Yes, Harry. You just don't understand. She's the worst!"

    show sprite_evil:
        linear 0.12 xalign 0.35
    with vpunch
    with Fade(0.1, 0.0, 0.5, color="#ff0000")
    hide jenny

    jenny "NOOO!!!"

    show harry:
        bounce
    harry "Jenny!!"

    show sprite_evil:
        linear 2.0 xalign -5.0

    toma "I don't know her so why should I help her?"
    harry "She could have been! Your heart is as cold as ice, gripped by fear."
    harry "A shame, Toma."
    toma "Who cares? She's just another sprite..."
    toma "I have all the friends I need."

    scene black
    with fade
    "Harry walks away in disbelief and Toma continues walking through the forest alone and stumbles upon a small party."

    jump aspie

label aspie:
    stop music fadeout 1.0
    play music "audio/forest_day.mp3" fadein 1.0 fadeout 1.0 loop

    scene bg tea party
    with fade

    show aspie:
        xalign 0.9 yalign 0.65 alpha 0.0
        linear 0.5 alpha 1.0

    show sprite_1:
        xalign 0.4 yalign 0.5 alpha 0.0
        linear 0.5 alpha 1.0

    show sprite_2:
        xalign 0.5 yalign 0.6 alpha 0.0
        linear 0.5 alpha 1.0

    show toma:
        xalign -1.0 yalign 1.0 alpha 0.0
        linear 2.0 xalign 0.0 alpha 1.0

    $ renpy.pause( 2.0, hard=True )

    toma "Are you having a tea party?"

    show sprite_1:
        bounce
    sprite_1 "Why, yes we are. Would you like to join us?"

    toma "Are you sure...?"

    show sprite_2:
        bounce
    sprite_2 "Of course, we're more than happy for you to join us!"

    show toma:
        linear 1.0 alpha 0.0

    show toma_happy:
        xalign 0.0 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0

    sprite_1 "It's almost perfect."

    toma "Almost? Why? What's wrong?"

    sprite_1 "Well, Aspie's here... He's not exactly the brightest..."
    sprite_2 "... Or the most entertaining."

    toma "I'm s-s-sorry ... I just wanted to join you guys"

    show sprite_1:
        bounce
    sprite_1 "Don't be sorry! Now that you're here, we don't need Aspie anymore."

    menu:
        "Let Aspie stay.":
            jump aspie_good

        "(Stay silent.)":
            jump aspie_bad

    label aspie_good:

        $ sprite_num += 1

        toma "Let him stay. I'm sure we can all live with it."

        show sprite_2:
            bounce
        sprite_2 "Are you blind?! He's so quiet. He's just like a ghost."

        show sprite_1:
            bounce
        sprite_1 "Even a ghost would have more personality."

        show toma_happy:
            linear 1.0 alpha 0.0

        show toma:
            xalign 0.0 yalign 1.0 alpha 0.0
            linear 1.0 alpha 1.0

        toma "Take that back! You think you're better than him? But you know what, you're just some low-life bullies."

        show sprite_2:
            bounce
        sprite_2 "We thought you were cool, Toma, but you're just a lame walnut just like Aspie."

        show sprite_1:
            bounce
        sprite_1 "Let's get out of here!"

        show sprite_1:
            linear 2.0 xalign 2.0

        show sprite_2:
            linear 2.0 xalign 2.0

        show toma:
            linear 1.0 xalign 0.25

        show aspie:
            linear 1.0 xalign 0.75

        $ renpy.pause( 1.0, hard=True )

        show aspie:
            bounce
        aspie "You d-d-don't need to s-s-stay out of pity ..."
        aspie "They're r-r-right, you know..."
        aspie "I'm just a no-good s-s-sprite with no p-p-personality..."

        show toma:
            linear 1.0 alpha 0.0

        show toma_happy:
            xalign 0.25 yalign 1.0 alpha 0.0
            linear 1.0 alpha 1.0

        toma "That's not true and I know it."
        toma "It doesn't matter what others say about you."
        toma "We don't need to pretend to be someone we're not to be wanted. We're enough."

        show aspie:
            bounce
        aspie "T-t-toma..."
        aspie "T-t-thank you... *cries*"

        toma "Don't cry! Here, have some cake! Stop crying!"

        scene black
        with fade
        "After comforting Aspie, Toma continues walking through the forest alone."
        "Harry finally catches up to Toma."

        jump krius

    label aspie_bad:

        show sprite_1:
            bounce
        sprite_1 "Get out of here you chicken nugget."

        show aspie:
            bounce
        aspie "I-i-i'm not a chicken nugget! I'm not one of those meataterians ..."

        show sprite_2:
            bounce
        sprite_2 "Aren't you? Why else would you be so different?"

        show toma_happy:
            linear 1.0 alpha 0.0

        show toma:
            xalign 0.0 yalign 1.0 alpha 0.0
            linear 1.0 alpha 1.0

        aspie "D-d-do you think I'm like that, T-t-toma? Do you want to l-l-leave? ..."

        toma "It's their party so ... it's their rules ..."

        show sprite_1:
            bounce
        sprite_1 "HA! Not even Toma wants you around. Just leave, you squirrel boy."

        show aspie:
            linear 2.0 xalign 2.0

        toma "Is it okay to treat him like that?"

        show sprite_2:
            bounce
        sprite_2 "Aw, you're too good on him, Toma. He'll be fine. He's used to it."

        scene black
        with fade
        "Toma enjoys himself at the party."
        "As Toma leaves the party, Harry catches up to Toma."

        jump krius

label krius:
    scene bg forest normal
    with dissolve
    $ renpy.pause( 1.0, hard=True )

    show toma:
        xalign -1.0 yalign 1.0
        linear 1.0 xalign 0.0

    show harry:
        xalign -0.33 yalign 0.4
        linear 1.0 xalign 0.33

    $ renpy.pause( 2.0, hard=True )

    show harry:
        bounce

    harry "Toma boy, where are your friends?"
    toma "I guess they're all busy..."

    harry "A strange, strange dilemma."

    show harry:
        bounce

    harry "Oh, hold on boyo!"

    with vpunch

    harry "Do you hear that?"
    harry "A sprite is in distress!"

    toma "What? Must be your imagination, Harry. I don't hear anything."

    harry "Shh ... someone's coming!"

    show krius:
        xalign 1.75 yalign 0.4
        linear 2.0 xalign 0.75

    "???" "*mumbles*"
    "???" "Stupid, stupid..."
    "???" "Why am I like this? I should just let the Dark One take me."
    "???" "Nobody loves me ... and they won't miss me either."
    "???" "I can just disappear."

    show harry:
        bounce

    harry "Did you hear that, lad? Krius might need your help."

    toma "Hey, what's wrong?"

    krius "I should just let myself go. I don't deserve to be a sprite."

    toma "What makes you say that?"

    krius "It's mid-spring but the forest is cold. Everywhere is cold. Why am I always cold inside?"

    menu:
        "\"Stop complaining.\"":
            jump krius_bad

        "\"No, you matter.\"":
            jump krius_good

label krius_good:

    $ sprite_num += 1

    show toma:
        linear 1.0 alpha 0.0

    show toma_happy:
        xalign 0.0 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0

    toma "Don't say that, my friend. I know it's hard but it won't last forever. Please, don't give up."

    krius "Easy for you to say. You're so popular here."

    toma "At the end of the day, popularity doesn't mean anything."

    toma "Just like you, I still feel alone even with the other sprites around me."

    toma "Since we're so alike, can we be friends and help each other out?"

    show harry:
        bounce
    harry "Come now, Krius. Please listen to Toma. We're here to help."

    show krius:
        bounce
    krius "Do you really mean that? You guys really do care?"

    toma "Of course we do!"

    show krius:
        bounce
    krius "Thank you for caring about me. If you need me, I'll always be there for you."

    show krius:
        linear 2.0 xalign 1.75

    show toma_happy:
        linear 1.0 xalign 0.75

    show harry:
        bounce
    harry "You did a good thing today, boy."
    harry "You changed his life for the better."

    toma "I hope he finds some comfort in my words."

    show toma_happy:
        linear 1.0 alpha 0.0

    show toma:
        xalign 0.75 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0

    jump pre_ending

label krius_bad:

    krius "I don't deserve to be a sprite. I should just let myself go."

    toma "Why not do something with your life for once?"

    krius "I've tried everything. Nothing works. Maybe the problem isn't the world around me, but me."

    toma "It can't be helped then. You're a goner."

    show harry:
        bounce
    harry "Now, Toma, we shouldn't bring him down."
    harry "He is a sprite who can make a difference. He just needs a friend."

    krius "No, Monsieur Harry, he is right. A friend won't solve my problem."
    with vpunch
    krius "I AM THE PROBLEM!!"

    show krius:
        linear 2.0 xalign 1.75

    show toma:
        linear 1.0 xalign 0.75

    show harry:
        linear 1.0 alpha 1.0
        linear 1.0 alpha 0.0

    show harry angry:
        xalign 0.33  yalign 0.4 alpha 0.0
        linear 1.0 alpha 1.0
    harry "Are you happy now son? You drove Krius to give up his moustache!"

    show harry angry:
        bounce
    harry "He can never return to this land now. He'll forever be a lost soul."

    show harry angry:
        linear 1.0 alpha 0.0

    show harry:
        xalign 0.33 yalign 0.4 alpha 0.0
        linear 1.0 alpha 1.0

label pre_ending:

    play music "audio/forest_night.mp3" fadein 1.0 fadeout 1.0

    "Toma feels a chilling sensation down his spine."

    with hpunch

    toma "What's that in the bushes?"
    harry "Other than dear Krius, not a hair."
    toma "I guess it's just a trick of my eyes..."
    harry "TOMA, BEHIND YOU!!"

    with hpunch
    with Fade(0.1, 0.0, 0.5, color="#ff0000")

    scene bg forest evil
    with fade

    show toma:
        xalign 0.8 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0

    show sprite_evil:
        xalign 0.05 alpha 0.0
        linear 1.0 alpha 1.0

    if sprite_num == 3:
        jump good_ending
    else:
        jump bad_ending

label good_ending:

    monster "Toma, you have been a nuisance for too long."

    show sprite_evil:
        bounce
    monster "For every sprite you took away from me, I will cut a piece of you and savor it."

    toma "That's where you're wrong! I have my good old salt shaker ..."
    "Toma rustles through his pockets looking for his salt shaker but with no luck."
    toma "... Oh. It's not here."

    show sprite_evil:
        bounce
    monster "It's futile to resist. No one can save you now."

    show jenny:
        xalign 2.0 yalign 0.5
        linear 1.0 xalign 0.5

    show aspie:
        xalign 2.0 yalign 0.1
        linear 1.0 xalign 0.55

    show krius:
        xalign 2.0 yalign 0.6
        linear 1.0 xalign 0.95

    show harry:
        xalign 2.0 yalign 0.1
        linear 1.0 xalign 0.9

    $ renpy.pause( 1.0, hard=True )
    "Sprites" "Toma!! We're here to take you home!"

    toma "Jenny ... Aspie ... Krius ... and Harry!!"

    "Sprites" "We brought salt too!"

    monster "No, not again! Anything but the salt!"

    harry "Sprites, you know what to do!"

    show salt_small:
        xalign 0.5 yalign 0.5 alpha 0.0
        linear 1.0 xalign 0.05 yalign 0.0 alpha 1.0 rotate 495.0
        bounce
        linear 1.0 alpha 0.0

    show salt_mini:
        xalign 0.95 yalign 0.6 alpha 0.0
        linear 1.0 xalign 0.45 yalign 0.0 alpha 1.0 rotate 585.0
        bounce
        linear 1.0 alpha 0.0

    with vpunch

    "The sprites each threw a salt shaker at the creature, weakening it."

    $ renpy.pause( 1.0, hard=True )

    harry "Toma, you must deal the final blow!"

    "Toma searches his pockets once again ... but finds a much larger salt shaker than before."

    show salt_big:
        xalign 0.8 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0 xalign 0.45 yalign -0.75 rotate 585.0
        bounce
        linear 1.0 alpha 0.0

    "Toma throws the mega salt shaker at the creature with all his might."
    with Fade(0.1, 0.0, 0.5, color="#ff0000")

    $ renpy.pause( 1.0, hard=True )

    show sprite_evil:
        linear 2.0 yalign -2.0 alpha 0.0

    monster "NOOO!!!"
    "The monster makes a gurgling noise as he slowly melts away into the dirt."

    $ renpy.pause( 2.0, hard=True )

    play music "audio/forest_day.mp3" fadein 1.0 fadeout 1.0

    show jenny:
        bounce
    jenny "Are you alright?!"

    show toma:
        linear 1.0 alpha 0.0

    show toma_happy:
        xalign 0.8 yalign 1.0 alpha 0.0
        linear 1.0 alpha 1.0

    show aspie:
        bounce
    aspie "We were so worried about you!"

    toma "I'm okay. Thank you for your help."

    show harry:
        bounce
    harry "Toma, I knew you were special the moment you entered our forest."
    harry "Through your actions, you've helped these sprites and made their lives richer and happier beyond compare."
    harry "And now, you have defeated our greatest enemy."

    show harry:
        bounce
    harry "For this, you will receive the Moustache of Courage!"
    harry "Its beauty and power have no equal in all realms..."

    toma "Thank you ..."
    toma "It's my honor to accept it but I couldn't have done it without you guys."

    show jenny:
        bounce
        bounce

    show aspie:
        bounce
        bounce

    show krius:
        bounce
        bounce

    krius "He's finally going home! We will never forget what you've done for us."

    "Sprites" "Have a wonderful journey, our friend!"

    scene bg bedroom
    with fade

    "As the sun rose from its slumber, so did the people of Owlville."
    "Toma slowly rose, rubbing his eyes, feeling ready to take on the day."

    show toma_happy:
        xalign 0.5 yalign 1.0 alpha 0.0
        linear 0.5 xalign 0.25 alpha 1.0

    show mom:
        xalign 0.5 yalign 0.75 alpha 0.0
        linear 0.5 xalign 0.75 yalign 0.75 alpha 1.0
        bounce

    mom "Are you feeling better?"

    toma "*smiles*"
    show toma_happy:
        bounce
    toma "I'm ready to go to school!"

    # RESERVE FOR SCHOOL SETTING
    scene black
    with fade

    "As Toma walks around during recess, he sees a boy in his grade being picked on by a group of upperclassmen."
    "Despite the fear in his heart telling him not to interfere, he steps forward to defend the boy."
    with vpunch
    "The boy looks at Toma in surprise."
    "The bullies begin to approach Toma but the principal passes by and takes them to his office."
    "Toma and the boy become fast friends."
    "This marks the beginning of a new chapter in Toma's life."

    scene bg happy ending
    with dissolve
    $ renpy.pause( 2.0, hard=True )

    "Thank you for playing!"

    return

label bad_ending:

    monster "Hello, Toma."
    monster "But first, thank you for sending those sprites to me."
    monster "Their despair and loneliness made it easy to lure them."
    monster "I took them apart piece by piece. No cry for help."
    monster "Just acceptance."
    monster "Now, it's your turn."

    show toma:
        bounce
    with vpunch
    toma "HARRY!!"

    toma "Harry ... or someone will find me ..."
    toma "They won't just leave me here ..."

    show sprite_evil:
        bounce
    monster "What makes you think Harry didn't know?"
    monster "He sent you here to die."

    toma "He wouldn't ..."
    toma "Please spare me ... I'll do anything."

    monster "I know you would."
    monster "You let them die, after all."

    toma "AHHHH!!!"

    show sprite_evil:
        linear 0.2 xalign 0.95

    with hpunch
    with Fade(0.1, 0.0, 0.5, color="#ff0000")

    $ renpy.pause( 1.0, hard=True )

    scene black
    with fade

    "..."

    scene bg bedroom

    "As the sun rose from its slumber, so did the people of Owlville."

    show mom:
        xalign 0.5 alpha 0.0
        linear 1.0 alpha 1.0

    "Expecting a much more lively Toma after finally having a good night's sleep, his mother attempts to wake him gently."

    with hpunch

    "No reaction."
    "Worried, her gentle shakes turn urgent."

    with hpunch

    "Toma's eyelids stay shut."

    scene black
    with fade

    "In the hospital, the doctors try everything but cannot explain his unforunate condition."
    "To this day, Toma is stuck in his sleep, eternally comatose."

    scene bg bad ending
    with dissolve
    $ renpy.pause( 2.0, hard=True )

    "Thank you for playing!"

    return
