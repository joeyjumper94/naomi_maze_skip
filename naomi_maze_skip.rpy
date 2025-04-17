init python:
    if not persistent.joeyjumper_naomi_maze_crashes:
        persistent.joeyjumper_naomi_maze_crashes=0

label joeyjumper_naomi_maze_skip_choice:

    #when we move scenes to the start of the underwater maze, we check if we have done this 3 times before using persistent variables
    if persistent.joeyjumper_naomi_maze_crashes>=3:
        #if we have, present a skip menu
        stop music fadeout 1.0
        $ renpy.pause (0.3)
        play sound "fx/system3.wav"

        call syscheck from _call_syscheck_joeyjumper_naomi_maze
        call skiptut from _call_skiptut_joeyjumper_naomi_maze
        if skipbeginning == False:
            if system == "normal":
                s "My records indicate your game has possibly crashed several times in this part. Would you like to skip to the end?"
            elif system == "advanced":
                s "It looks like you've possibly crashed several times here. Skip to the end of this scene?"
            else:
                s "So, it looks like you've crashed out numerous times before. Either you could try this again, or we could save some time and just skip to the end of this scene."
        $ skipbeginning = False

        #if the player choses yes, jump to the end of the maze section.
        menu:
            "Yes. I want to skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                scene black with dissolvemed
                $ renpy.pause (1.0)
                $ persistent.skipnumber += 1
                call skipcheck from _call_skipcheck_joeyjumper_naomi_maze
                $ ecknaomim3breath = 6
                $ ecknaomim3breathpl = 123
                play music "mx/abandonedlab.mp3"
                scene eckoldbiolab with dissolveslow
                $ renpy.pause (3.5)
                jump eck_naomi_m3_biolab
            "No. Don't skip ahead.":
                play sound "fx/system3.wav"
                s "As you wish.{cps=2}..{/cps}{w=1.0}{nw}"
                play music "mx/neptune.mp3"

    #if the player says no to skip or has not triggered the menu, we increase the counter
    $ persistent.joeyjumper_naomi_maze_crashes+=1
    label joeyjumper_naomi_maze_skip_no:
        pass

#this is to be called when the maze is completed or failed
label joeyjumper_naomi_maze_reset:
    $ persistent.joeyjumper_naomi_maze_crashes=0
    return