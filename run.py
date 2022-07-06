import random


def startgame():
    print("Game will start")


def instuctions():
    print("This will tell you what to do")


startgame()


instuctions()

menu = {}
menu['1'] = 'Start game'
menu['2'] = 'Instructions'


def menu():

    """
    Menu to start a game or read the instructions to how to play!
    """

    print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
                   """)

    print()
    choice = input("""
                    1.Start Game
                    2.Instructions
                 """)
    if choice == '1':
        startgame()
    elif choice == '2':
        instuctions()
    elif choice == '':
        None
        
    else:
        print('Invalid choice,please choose from option 1 or 2!')
        menu()
    

menu()
