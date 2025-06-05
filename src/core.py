# PYTHON VERSION: 3.11.9

import random
import os

import constants as c

def goku_thought():
    result = random.randint(1,3)

    return result

def player_choice():
    while True:
        choice = int(input("Choose:\n"+
                            "[1] - Rock\n"+
                            "[2] - Paper\n"+
                            "[3] - Scissors\n"+
                            "You choose... "))
        if 1 <= choice <= 3:
            break
        else:
            clear_screen()
            print("Not valid. Choose 1, 2 or 3.")

    return choice

def reset_life(player, goku):
    player.set_life(c.MAX_LIFE)
    goku.set_life(c.MAX_LIFE)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def evaluate_result(choice, goku_choice, player, goku):
    if (choice == 1 and goku_choice == 3) or (choice == 2 and goku_choice == 1) or (choice == 3 and goku_choice == 2):
        print("You hit Goku!\n")
        goku.set_life(goku.get_life() - c.HIT)
    elif choice == goku_choice:
        print("You defend yourself.\n")
    elif (choice == 3 and goku_choice == 1) or (choice == 1 and goku_choice == 2) or (choice == 2 and goku_choice == 3):
        print("Goku hits you...\n")
        player.set_life(player.get_life() - c.HIT)

def evaluate_victories(player_life, goku_life, player, goku):
    if player_life <= c.MIN_LIFE:
        print("You lose...")
        goku_victories = goku.set_counter(goku.get_counter() + c.ADD_VICTORY)
        player_victories = player.get_counter()
        goku_victories = goku.get_counter()
    elif goku_life <= c.MIN_LIFE:
        print("You win!")
        player_victories = player.set_counter(player.get_counter() + c.ADD_VICTORY)
        player_victories = player.get_counter()
        goku_victories = goku.get_counter()

    return player_victories, goku_victories

def repeat(player_victories, goku_victories, player, goku):
    while True:
        reset_life(player, goku)

        action = int(input("Do you want to play again?\n"+
               "[1] - Play again\n"+
               "[2] - Check victories\n"+
               "[3] - Stop playing\n"+
               "You choose: "))
    
        match action:
            case 1:
                clear_screen()
                play(player, goku)
            case 2:
                print(f"Your victories: {player_victories}\n"+
                f"Goku's victories: {goku_victories}\n")
            case 3:
                print("You've chosen to stop playing.")
                exit()
            case _:
                clear_screen()
                print("Not valid. Choose a valid option.")

def play(player, goku):
    clear_screen()
    player_life = player.get_life()
    goku_life = goku.get_life()
    
    while player_life > c.MIN_LIFE and goku_life > c.MIN_LIFE:

        choice = player_choice()
        goku_choice = goku_thought()

        clear_screen()

        print("\nGoku has choosen...\n",
              "ROCK!\n" if goku_choice == 1 else "PAPER!\n" if goku_choice == 2 else "SCISSORS!\n")
    
        evaluate_result(choice, goku_choice, player, goku)

        player_life = player.get_life()
        print(f"Remaining life: {player_life}")
        goku_life = goku.get_life()
        print(f"Goku's remaining life: {goku_life}\n")

    player_victories, goku_victories = evaluate_victories(player_life, goku_life, player, goku)

    repeat(player_victories, goku_victories, player, goku)
