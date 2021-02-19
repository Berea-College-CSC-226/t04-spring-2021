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

delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!
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
    print(
        "Congratulations, " + user + ', you have made it to the end of this... strange... adventure. I hope you feel accomplished.')
    print()
    print()
    print()
    sleep(delay * 5)
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
    global dead  # You'll need this to be able to modify the dead variable
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
        sleep(delay * 2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print(
            "You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)


###################################################################################


def team_1_adv():
    pass
    """
    https: // docs.google.com / document / d / 1oL8oNDMjbVw4Va6CKVTdKbtZn4cUsCLsCUzcN7tEMT0 / edit?usp = sharing
    Cienna-Paige Slattery
    Micho Constantino 
    :return: none
    """

action = input(
    "You can (1) seek light in the cave, (2) become familiar with the cave,"
    "(3) make a fire with rocks, or (4) wait for help] \n Type your number choice: ")
if action == "4":
    # bad choice
    print("You let animals find you, so they tear you limb by limb. You have failed your mission. \n")
    quit()
elif action == "1":
    # good choice
    print("luckily, you're able to find a light. Now, you are presented with a new challenge. "
          "\n You must find rescue a woman and her children from a goblin guarded tower. \n")
else:
    # neutral
    print("you are safe. You've found a new place in the cave. Next, you have to find a way out \n")
sleep(delay * 5)

def team_2_adv():
    global dead
    choice = input(
        "You trip over something. You look down and see it's a box.  What do you do with it? [Open/Nothing/Carry]")
    choice.lower()
    if choice.lower() == "open":
        # Good choice
        print("You find a gift card to the Berea College Visitor Center! Neat!")
        sleep(delay)
    elif choice.lower() == "carry":
        # Bad choice
        print("You put the box in your backpack and keep walking.")
        sleep(delay)
        print("You walk a few steps and you begin to hear a mysterious ticking noise.")
        print("The box is going to explode! Oh no!")
        sleep(delay)
        print("B O O M")
        dead = True
    else:
        # Neutral choice
        print(
            "You keep walking. You're almost tempted to turn around and open the box, but you don't. Not today, Satan.")
        sleep(delay)
    if dead:
        print("You died. Loser.")
        quit()


def team_3_adv():
    """""
    https://docs.google.com/document/d/1LlQ1Esbro-cAhvMp-DPGm2-ajqDeqIyDS6K2ma1YwlQ/edit?ts=602e703f#
    """


print()
print(
    "You Enter a forest temple, the doors close behind you and uo ahead is a knight fully armored and taking a fighting stance.")
print("There is a treasure chest behind him filled to the brim with gold and other goodies")
print()
print("In front of you are three different choices for weapons to fight the knight with")       # Start of the story plot
sleep(delay * 2)
print("1.Sword")
print("2.Crossbow")
print("3.Spear")

weapon_Choice =input("Please enter which one:")                                                 # gives users the ability to pick the weapon

if weapon_Choice == "3" or weapon_Choice == "spear" or weapon_Choice == "Spear":                # Best case scenario
    print("You pick up the spear, throw it across the room right into the knights eye opening")
    print("you render the knight unconsious and leave with the treasure behind him")
elif weapon_Choice == "1" or weapon_Choice == "Sword" or weapon_Choice == "sword":              # Worst ca scenario
    print("you pick up the sword and charge at the knight full speed")
    print("The knight crushes you in combat and pins you down with his sword at your neck ")
    print(
        "He gives you one last chance and if you can guess how many gold bars is in the chest with a differnce of 5 above or below")
    # Hacker challenge

    guess = int(input("Take your best guess:"))                                                 # Gives the user one last attempt to leave safely
    if guess >= 15 and guess <= 25:
        print("Amazing! your guess was correct, and the night lets you walk away")
    else:
        print("You guesss wrong, you die a slow and miserable death")
        dead = True
elif weapon_Choice == "2" or weapon_Choice == "crossbow" or weapon_Choice == "Crossbow":       # Neutral case scenario
    print("You pick up the crossbow and start shooting arrows at the knight")
    print(
        "However, the arrows are useless to the knights armor \nSince you kept your distance you made a run for it and left the temple with no treasure")
else:
    print("Please enter a valid weapon choice! to try again press the green play button")      # account for user error

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():
    """
    https://docs.google.com/document/d/1bCYJYtok5onV5DGtv9x4DXAgQ3yie-QJa_cHRUUtoNQ/edit?usp=sharing
    Tallis Matus
    Falsai Kimbugwe
    :return:
    """
    global dead
    print("you found a  girl chained to the wall. what do you do?")
    choice = input("Choose from these choices: Free her, Move along, Get help")
    if choice == "Free her":
        # "Oh thank you!" says the girl. Now she is your responsibility
        print("The girl is grateful. She offers help to lead you out of the labyrinth.")
        sleep(delay)
    elif choice == "Move along":
        # Oh, you are a terrible human being. You refused to help a struggling girl
        print("You follow the route taking you out the cave without any remorse to what you just did.")
        sleep(delay)
        # Giving the user a second chance.
        print("You come across a pit. You hear something at the bottom of it")
        choice2 = input("Do you Jump forward or Turn back")
        if choice2 == "Jump forward":
            sleep(delay)
            print("Oh no.")
            print("You fall into a pond full of hungry alligators who rip you into pieces once you reach the bottom.")
            dead = True
        else:
            print("You decide to not jump across the pit. You go back to where you were, the girl is already gone.")
            sleep(delay)
    else:
        # What a human? You are showing empathy and character.
        print("You realise you can not help the girl, so you decide to go get help.")
        print("As you walk a bit, you remember that you are there by yourself and the girl in the labyrinth")
        print("You turn to look at the girl to figure it out and boom, the girl is gone.")
        print("Now you are all alone. scared and wanting help to be out of this nightmare.")
        sleep(delay)
    if dead == True:
        print("Oh no. You have died. Try again with a different choice tomorrow.")
        quit()


def team_6_adv():
    pass
    """ google doc link:https://docs.google.com/document/d/1OIUxTwJOszrJMrQHqYuGBvy05NGGfQF24aFNgNDDL9w/edit?usp=sharing """
    """ Beau Schneider/ Sabdi Lopez"""

    user_input = input('you stubble opon an apple sitting on the ground. do you choose to eat it?  [yes/no/]')
    if user_input == 'yes':
        print('Good Choice! You eat the apple and it makes you super strong!')
        sleep(delay)
        print("")
        print("")
    elif user_input == 'no':
        print('Oh no... you did not eat the apple!')
        print('the apple has turned into a giant snaked and eaten you...')
        print("")
        print('Oh no! you died! try again by pressing the green play button in the top right corner!')
        quit()
    else:
        print('continue on your journey...')
        print("")


def team_7_adv():
    """https://docs.google.com/document/d/1xX3LFlyEv8COTRD6cXeQ8j0J-84W3V8S4ojz7PZPZ7A/edit
    Luke Wilson
    Malena Leon Hidalgo
    :return:none
    """
    pass
    die = False
    print("Now an evil spell has teleported you in a castle with monsters. Your goal is to escape!")

    direction = input("You are in a dungeon, the door is open, what way do you go? [right, left, up, down]")
    if direction == "right":
        # good ending
        print("You find the entrance to the castle door and escape!")

    elif direction == "left":
        # bad ending
        print("A spooky skeleton finds you and shoots you with an arrow!")
        die = True

    else:
        # neutral ending
        print("A werewolf hurts you but you manage to escape!")

    if die:
        print("Oh no, you have died!")


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
    random.shuffle(paths)  # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()  # Runs each function in the paths list

    end_story(user)


main()
