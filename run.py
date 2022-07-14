import random
import sys
from os import system, name


words = []
for line in open('words.txt', 'r').readlines():
    words.append(line.strip())


def getting_word(hangman_word):
    """
    Choose a random word from the words.txt file
    """
    hangman_word = random.choice(words)
    return hangman_word.upper()


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


def play_again(hangman_word):
    """
    Let the player decide if they want to play
    a new game or exit it.
    """
    while True:
        try_again = input("Would you like to try again? Y/N: ")
        if try_again.lower() == 'y':
            hangman_word = getting_word(words)
            startgame(hangman_word)
            break
        elif try_again.lower() == 'n':
            clear()
            print("Thanks for playing! :)")
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


def main_menu(hangman_word):

    """
    Menu to start a game or read the instructions to how to play!
    """
    clear()
    logo()
    user = input("\nWhat is your name? : ")
    while True:
        choice = input(f"""
                            1.Start Game
                            2.Instructions
                            3.Exit game

                Dear {user} type the number of your choice: """)
        if choice == '1':
            startgame(hangman_word)
            break
        elif choice == '2':
            instructions(hangman_word)
            break
        elif choice == '3':
            clear()
            print('Thanks for playing! :)')
            sys.exit()
        else:
            print('Invalid choice,please choose from option 1,2 or 3!')


def instructions(hangman_word):
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
            main_menu(hangman_word)
            break
        else:
            print("Invalid choice please type Y for yes or N for no!")


def startgame(hangman_word):
    """
    This method will start the game from scratch
    """
    clear()
    logo()
    word = ["_"] * len(hangman_word)
    guessed = False
    tries = 6
    guessed_letters = []
    guessed_word = []
    print(hangmans(tries))
    print('\n', word, '\n')
    print(f"Guessed letters: {guessed_letters} \n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                clear()
                print("You already guessed this letter.")
            elif guess not in hangman_word:
                clear()
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                clear()
                print(f"Good job, {guess} is in the word!")
                guessed_letters.append(guess)
                for i, letter in enumerate(hangman_word):
                    if letter != "_" and guess == letter:
                        word[i] = letter
                if "_" not in word:
                    guessed = True
                    word = hangman_word
        elif len(guess) > 1 and guess.isalpha():
            if guess in guessed_word:
                clear()
                print("You already tried this word")
            elif guess != hangman_word:
                clear()
                print(f"{guess} is not the word!")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True
                word = hangman_word
        else:
            clear()
            print("Not a valid guess!")

        print(hangmans(tries), '\n')
        print('\n', word, '\n')
        print(f" Guessed letters: {guessed_letters}")
    if guessed:
        print("That is the word! You are a WINNER!")
        play_again(hangman_word)
    else:
        clear()
        print(hangmans(0))
        print("Sorry, you run out of tries")
        word = hangman_word
        print("The word was:", word)
        play_again(hangman_word)


def start():
    """
    This is start the game
    """
    hangman_word = getting_word(words)
    main_menu(hangman_word)


start()
