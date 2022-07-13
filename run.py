import random
import sys
from os import system, name


words = []
for line in open('words.txt', 'r').readlines():
    words.append(line.strip())


hangman_word = random.choice(words).upper()

guessed_letters = []
guessed_word = []


def clear():
    """
    Clear the terminal if Windows it is using
    the 'cls' statement otherwise (Linux or Mac)
    it uses the 'clear' statement
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def play_again():
    while True:
        try_again = input("Would you like to try again? Y/N: ")
        if try_again.lower() == 'y':
            startgame(hangman_word)
            break
        elif try_again.lower() == 'n':
            sys.exit()
            break
        else:
            print("Invalid choice please type Y for yes or N for no!")


def logo():
    """
    Hangman logo
    """
    print("""
     _
    | |
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_  \\
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
                   """)


def hangmans(parts):
    """
    Hangman art
    """
    parts_shown = ['''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
          |
          |
          |
          |
    =========''']
    return parts_shown[parts]


menu = {}
menu['1'] = 'Start game'
menu['2'] = 'Instructions'
menu['3'] = 'Exit game'


def main_menu():

    """
    Menu to start a game or read the instructions to how to play!
    """
    clear()
    logo()
    while True:
        choice = input("""
                            1.Start Game
                            2.Instructions
                            3.Exit game

                            Make your choice : """)
        if choice == '1':
            startgame(hangman_word)
            break
        elif choice == '2':
            instructions()
            break
        elif choice == '3':
            print('Thanks for playing! :)')
            sys.exit()
        else:
            print('Invalid choice,please choose from option 1,2 or 3!')


def instructions():
    """
    This will tell you how to play the game
    """
    clear()
    logo()
    print("""
    When you start the game you have to type your name in and press enter
    then the game starts.\n
    You will see empty dashes which is shows you
    how many letters are in the random word \n
    what you have to guess letter by letter or if you confident
    you can type the whole word. \n
    You have 6 wrong attemps before the game is finished,\n
    if you can guess it before you can see all the body parts
    on the gallow you WIN! \n
    """)
    while True:
        ready = input("Are you ready for the game? Y/N : ")
        if ready.lower() == 'y':
            startgame(hangman_word)
            break
        elif ready.lower() == 'n':
            main_menu()
            break
        else:
            print("Invalid choice please type Y for yes or N for no!")


def startgame(hangman_word):
    """
    This method will start the game from scratch
    """
    clear()
    logo()
    user = input("\nWhat is your name? : ")
    print(f"\nWelcome {user}, enjoy the game!\n")
    word = " _ " * len(hangman_word)
    guessed = False
    tries = 6
    while not guessed and tries > 0:
        print(hangmans(tries))
        print('\n', word, '\n')
        print(f"Guessed letters: {guessed_letters} \n")
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess not in hangman_word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print("You already guessed this letter.")
            else:
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                letter_in_word = list(word)
                in_letter = [i for i, letter in enumerate(hangman_word)
                             if letter == guess]
                for index in in_letter:
                    letter_in_word[index] = guess
                word = "".join(letter_in_word)
                if "_" not in word:
                    guessed = True
        elif len(guess) == len(hangman_word) and guess.isalpha():
            if guess in guessed_word:
                print("You already tried this word")
            elif guess != word:
                print(guess, "is not the word!")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word = hangman_word
        else:
            print(hangmans(tries))
            print('\n', word, '\n')
            print(f"Guessed letters: {guessed_letters}")
    if guessed:
        print("That is the word! You are a WINNER!")
        play_again()
    else:
        print("Sorry, you run out of tries")
        play_again()


main_menu()
