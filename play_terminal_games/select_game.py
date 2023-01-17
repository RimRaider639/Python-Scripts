
from colorama import Fore, init
init()
from all_games import tictactoe, hangman_v1, hangman_v2
def game():
    print(Fore.RED+'\nPRESS 1 to play TicTacToe\nPRESS 2 to play Hangman v1\nPRESS 3 to play Hangman v2\nPRESS 4 to quit'+Fore.WHITE)
    
    while True:
        ask=input('\nWhat do you want to play? ')
        if ask not in ['1', '2', '3', '4']:
            print('Invalid value, try again!')
            continue
        else:
            if ask=='1':
                tictactoe.tictactoe()
            elif ask=='2':
                hangman_v1.hangman()
            elif ask=='3':
                hangman_v2.hangman()
            elif ask=='4':
                break