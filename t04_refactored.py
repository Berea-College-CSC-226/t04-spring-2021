######################################################################
# Author: Brian Schack  # Don't change me this time!
# Username: schackb     # Don't change me this time!
#
# Assignment: T04: Adventures in Gitland
#
# Purpose: To recreate a choose-your-own-adventure style game
# by refactoring T01.
#
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
#
# This new version will take advantage of functions, as well as
# demonstrate the value of git as a tool for collaborating.
######################################################################
# Acknowledgements:
#   Original Author: Scott Heggen
#
######################################################################
import random
from time import sleep

delay = 0.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False


def start_story():
    """
    Introduction text for the story. Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(delay)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(delay * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(delay)
    return user


def end_story(user):
    """
    This is the ending to the story. Don't modify this function, either.

    :param user: the user's name
    :return: None
    """
    print("Congratulations, " + user + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay*5)
    print("Now go play again.")


def kill_if_dead(dead):
    """
    Simple function to check if you're dead

    :param dead: A boolean value where false let's the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()

###################################################################################


def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """
    global dead             # You'll need this to be able to modify the dead variable
    direction = input("Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(delay)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(delay)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(delay*2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)

###################################################################################


def team_1_adv():
    pass
    # TODO Add your code here


def team_2_adv():
    pass
    # TODO Add your code here


def team_3_adv():
    pass
    # TODO Add your code here


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():
    pass
    # TODO Add your code here


def team_6_adv():
    pass
    # TODO Add your code here


def team_7_adv():
    pass
    # TODO Add your code here


def team_8_adv():
    """https://docs.google.com/document/d/1JALo9o6gGmR0x8lk4ExV_OCZ8llaRirBdmbvQ8IKKeM/edit
    Brady Bateman
    batemanb """

    global dead
    print("")
    print("You find a chest in the middle of the room.")

    print("1. Check the room for traps. \n"
          "2. Go straight towards the chest, disregarding all sense of caution! \n"
          "3. Turn around. It's obviously a trick.")
    chest = (input("What do you do? [1,2,3]"))

    if (chest == "1") or (chest == "1."):
        # neutral choice
        print("You look around, noticing all sorts of deadly traps. Spike pits, trip wires, the whole shebang")
        sleep(delay)
        print("You carefully maneuver around the traps, and make it to the chest.")
        print("To your surprise, the chest is a mimic. It gnarls its golden teeth at you \n"
              "You fight off the mimic. Oh if only this wasn't a text game. I bet this fight looks awesome!")
        print("You defeat the mimic, and take one of its teeth with you.")
        sleep(delay)
    elif (chest == "2") or (chest == "2."):
        # good choice
        print("I like your moxie, adventurer!\n"
              "You run straight towards the chest, dodging traps and whatnot. \n"
              "You open the chest, and stuff as much loot as you can into your pockets. \n"
              "Yay, you got treasure! I hope it doesn't slow you down!")
        sleep(delay / 2)
        print("(It probably wont)")
        sleep(delay)
    elif (chest == "3") or (chest == "3."):
        # bad choice
        print("You turn around, hoping to go back a chapter or something.")
        sleep(delay)
        print("On your way out the door, you trip over a wire.")
        print("As thousands of arrows pierce through you, you take solace in the fact that you were right.")
        dead = True
    else:
        # hopefully catch-all contingency, also death.
        print("Oh come on! Are you too good for my three choices? You couldn't be bothered to type 1, 2, or 3? \n"
              "I bet you think you're so clever. You're probably wondering what happens if you type something else. \n"
              "Well, I don't like that. Rocks fall on you and you die. Or something, just know that you died!")
        dead = True

    kill_if_dead(dead)

    pass


def team_9_adv():
    pass
    # TODO Add your code here


def team_10_adv():
    pass
    # TODO Add your code here


def team_11_adv():
    pass
    # TODO Add your code here


def team_12_adv():
    pass
    # TODO Add your code here


def team_13_adv():
    pass
    # TODO Add your code here


def team_14_adv():
    pass
    # TODO Add your code here


def team_15_adv():
    pass
    # TODO Add your code here


def team_16_adv():
    pass
    # TODO Add your code here


def team_17_adv():
    pass
    # TODO Add your code here


def team_18_adv():
    pass
    # TODO Add your code here


def team_19_adv():
    pass
    # TODO Add your code here


def team_20_adv():
    pass
    # TODO Add your code here


def main():
    """
    The main function, where the program starts.
    :return: None
    """

    user = start_story()
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story(user)


main()