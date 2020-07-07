# Learned at Automate boring Stuff!
# automatetheboringstuff.com

import random, sys

print('Rock, paper, scissors')

# to keep track of the wins, losses and ties
wins = 0
losses = 0
ties = 0

while True:     # main game
    print('%s Wins, %s Losses, %s Ties' %(wins,losses,ties))
    while True:     # player input
        print('Enter your move: \n 1: Rock \n 2: Paper \n 3: Scissors \n or 0: Quit')
        playerMove = input()
        if playerMove == '0':       # to quit the game
            sys.exit()
        if playerMove == '1' or playerMove == '2' or playerMove == '3':
            break       # to break out the loop
        print('Type either 1, 2, 3 or 0 to quit.')

    # now we display what the player chose
    if playerMove == '1':
        print('ROCK vs...')
    elif playerMove == '2':
        print('PAPER vs...')
    elif playerMove == '3':
        print('SCISSORS vs...')

    # to create a random response from the computer
    computerResponse = random.randint(1,3)
    if computerResponse == 1:
        compMove = '1'
        print('ROCK')
    elif computerResponse == 2:
        compMove = '2'
        print('PAPER')
    elif computerResponse == 3:
        compMove = '3'
        print('SCISSORS')

    # lets get to the end; save and display the results
    if playerMove == compMove:
        print("It's a tie.")
        ties += 1
    elif playerMove == '1' and compMove == '3':
        print('Nice, Rock beats scissors.')
        wins += 1
    elif playerMove == '2' and compMove == '1':
        print('Nice, Paper beats Rock.')
        wins += 1
    elif playerMove == '3' and compMove == '2':
        print('Nice, Scissors beat Paper.')
        wins += 1
    elif playerMove == '1' and compMove == '2':
        print('Sorry, Paper crushed Rock.')
        losses += 1
    elif playerMove == '2' and compMove == '3':
        print('Sorry, Scissors cut Paper.')
        losses += 1
    elif playerMove == '3' and compMove == '1':
        print('Sorry, Rock crushed Scissors.')
        losses += 1