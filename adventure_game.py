# You can use this workspace to write and submit your adventure game project.
import time
import random
import choices
import enum


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')


def print_pause(message, delay=0):
    print(Color.get_color() + message)
    time.sleep(delay)


def enemy(text, enemy_var, enemy_type_var):
    index = 0
    output = []
    while index < len(text):
        if text[index:index + len("<<adj>>")] == "<<adj>>":
            output.append(enemy_type_var)
            index += 7

        elif text[index:index + len("<<noun>>")] == "<<noun>>":
            output.append(enemy_var)
            index += 8

        else:
            output.append(text[index])
            index += 1
    output = "".join(output)
    return output


def intro(enemy_var, enemy_type_var):

    print_pause("You find yourself standing in an open field, filled"
                "with grass and yellow flowers.")
    print_pause(enemy("Rumor has it that a <<adj>> <<noun>> is somewhere "
                      "around here, and has been terrifying the nearby"
                      " village.", enemy_var, enemy_type_var))
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not "
                "very effective) dagger.")


def houseorcave(list_game_box, enemy_var, enemy_type_var):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    response = valid_input("Please enter 1 or 2.\n", ["1", "2"])
    if response == "1":
        house(list_game_box, enemy_var, enemy_type_var)
    elif response == "2":
        cave(list_game_box, enemy_var, enemy_type_var)


def field(list_game_box, enemy_var, enemy_type_var):
    print_pause("You find yourself in a big oprn field.")
    print_pause("Luckily it seems like no one is following you.")
    print_pause("Behind you is a house")
    print_pause("To your left is a dark cave")
    houseorcave(list_game_box, enemy_var, enemy_type_var)


def house(list_game_box, enemy_var, enemy_type_var):
    print_pause("You approach the door of the house.")
    print_pause(enemy("You are about to knock when the door opens"
                      " and out steps a <<noun>>.",
                      enemy_var, enemy_type_var, ))
    print_pause(enemy("Eep! This is the <<noun>>'s house!",
                      enemy_var, enemy_type_var))
    print_pause(enemy("The <<noun>> attacks you!", enemy_var, enemy_type_var))
    if "sword" not in list_game_box:
        print_pause("You feel a bit under-prepared for this, what"
                    " with only having a tiny dagger.")
    fightorrun(list_game_box, enemy_var, enemy_type_var)


def fightorrun(list_game_box, enemy_var, enemy_type_var):
    response = valid_input("Would you like to (1) fight or (2) "
                           "run away?\n", ["1", "2"])
    if "1" in response:
        fight(list_game_box, enemy_var, enemy_type_var)
    elif "2" in response:
        field(list_game_box, enemy_var, enemy_type_var)


def play_again():

    response = valid_input("Would you like to play again?"
                           "(y/n)\n", ["yes", "no", "y", "n"]).lower()
    if "yes" in response or "y" in response:
        print_pause("Game is restarting")
        play_game()
    elif "no" in response or "n" in response:
        print_pause("GAME OVER!")
        return


def fight(list_game_box, enemy_var, enemy_type_var):
    if "sword" in list_game_box:
        print_pause(enemy("As the <<noun>> moves to attack, you"
                          " unsheath your new sword.", enemy_var,
                          enemy_type_var))
        print_pause("The Sword of Ogoroth shines brightly in your hand as"
                    " you brace yourself for the attack.")
        print_pause(enemy("But the <<noun>> takes one look at your"
                          " shiny new toy and runs away!", enemy_var,
                          enemy_type_var))
        print_pause(enemy("You have rid the town of the <<noun>>"
                          "You are victorious!", enemy_var, enemy_type_var))
        play_again()
    else:
        print_pause("You do your best...")
        print_pause(enemy("but your dagger is no match for the <<noun>> .",
                          enemy_var, enemy_type_var))
        print_pause("You have been defeated!")
        play_again()


def cave(list_game_box, enemy_var, enemy_type_var):
    print_pause("You peer cautiously into the cave.")
    if "sword" in list_game_box:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        houseorcave(list_game_box, enemy_var, enemy_type_var)
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger"
                    " and take the sword with you.")
        print_pause("You walk back out to the field.")
        list_game_box.append("sword")
        houseorcave(list_game_box, enemy_var, enemy_type_var)


def play_game():
    gamelist = []
    ENEMY = random.choice(choices.enemy)
    ENEMY_TYPE = random.choice(choices.enemy_type)
    intro(ENEMY, ENEMY_TYPE)
    houseorcave(gamelist, ENEMY, ENEMY_TYPE)


play_game()
