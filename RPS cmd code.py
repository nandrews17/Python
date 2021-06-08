# nandrews17@georgefox.edu
# Rock Paper Scissors
# 2017-11-15

# Inport Function
import random

# Used Constants
ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'
player = 1
comp = 2
tie = 3
playerMoves = [ROCK, PAPER, SCISSORS]

# MODULE: main
# DEF: Collection and organisation of functions
def main():
    # Running total for score
    score = [0, 0, 0]
    displayWelcomeMessage()
    runAgain = getMenuChoice()
    # Loop for gameplay and score record
    while runAgain == 1:
        userMove = getUserMove()
        compMove = getCompMove()
        winner = compareUserAndCompMoves(userMove, compMove)
        displayResults(userMove, compMove, winner)
        score = updateScore(winner, score)
        runAgain = getRunAgainChoice()
    displayScore(score)

# MODULE: displayWelcomeMessage
# INPUTS: None
# OUTPUTS: None
# DEF: Prints message when program initiates
def displayWelcomeMessage():
    print('Welcome To. . .\n\nRock, Paper, Scissors!\n\n\n',
        ('-' * 13), ' MENU ', ('-' * 13), sep='')

# MODULE: getMenuChoice
# INPUTS: None
# OUTPUTS: runAgain
# DEF: Asks for the choice to play or quit
def getMenuChoice():
    choice = 0
    print('Wana Play?', end='')
    # Extra Sass According To User Imput
    while choice != 1 and choice != 2:
        try:
            choice = int(input(' (1 - Play, 2 - Quit): '))
            while choice != 1 and choice != 2:
                print('\nWow. . .\nDo You Want To Play Or What?', end='')
                choice = int(input (' (1 - Play, 2 - Quit): '))
        except ValueError:
            print('\nThat Is Not Even A Number. . .\nDo You Wana Play?', end='')
            choice = 0
    print('-' * 32)
    return choice

# MODULE: getUserMove
# INPUTS: None
# OUTPUTS: userMove
# DEF: Asks for the player move and changes to int
def getUserMove():
    print('\nAlrighty Then!', 
          '\nSay ROCK, PAPER, SCISSORS, And Then Choose One As Your Move!\n')
    move = input('ROCK! PAPER! SCISSORS! . . . ')
    while move not in playerMoves:
        print("\nAgain? Come On, Let's go!")
        move = input('ROCK! ~ PAPER! ~ SCISSORS! ~ . . . ')
    if move == 'ROCK':
        move = 1
    elif move == 'PAPER':
        move = 2
    elif move == 'SCISSORS':
        move = 3
    return move

# MODULE: getCompMove
# INPUTS: None
# OUTPUTS: compMove
# DEF: Uses random.int function to calculate computer move
def getCompMove():
    move = random.randint(1, 3)
    return move

# MODULE: compareUserAndCompMoves
# INPUTS: userMove, compMove
# OUTPUTS: winner
# DEF: Compares the player's and cpu's moves to determine a winner
def compareUserAndCompMoves(userMove, compMove):
    if userMove == 3 and compMove == 2:
        winner = player
    elif userMove == 2 and compMove == 1:
        winner = player
    elif userMove == 1 and compMove == 3:
        winner = player
    elif userMove - compMove == 0:
        winner = tie
    else:
        winner = comp
    return winner

# MODULE: displayResults
# INPUTS: userMove, compMove, winner
# OUTPUTS: None
# DEF: Changes int to str and prints the cpu movr and winner of the game
def displayResults(userMove, compMove, winner):
    if compMove == 1:
        compMove = 'ROCK'
    elif compMove == 2:
        compMove = 'PAPER' 
    elif compMove == 3:
        compMove = 'SCISSORS'
    if userMove == 1:
        userMove = 'ROCK'
    elif userMove == 2:
        userMove = 'PAPER' 
    elif userMove == 3:
        userMove = 'SCISSORS'
    print('\nThe Computer Chose ', compMove)
    if winner == player:
        print(userMove, 'beats', compMove, 'and You Win!')
    elif winner == comp:
        print(compMove, 'beats', userMove, 'and The CPU Wins!')
    elif winner == tie:
        print("It's A Tie!")

# MODULE: updateScore
# INPUTS: winner, score
# OUTPUTS: score
# DEF: Uses and then modifies running total to keep a score record
def updateScore(winner, score):
    if winner == player:
        score[0] += 1
    elif winner == comp:
        score[1] += 1
    elif winner == tie:
        score[2] += 1
    print('\nHuman:', score[0], 'Computer:', score[1], 'Tie:', score[2])
    print()
    return score

# MODULE: getRunAgainChoice
# INPUTS: None
# OUTPUTS: runAgain
# DEF: Asks for choice to play again or quit
def getRunAgainChoice():
    choice = 0
    print(('-' * 32), '\nPlay Again?', end='')
    while choice != 1 and choice != 2:
        try:
            choice = int(input(' (1 - Play, 2 - Quit): '))
            while choice != 1 and choice != 2:
                print('\nWow. . .\nDo You Want To Play Or What?', end='')
                choice = int(input (' (1 - Play, 2 - Quit): '))
        except ValueError:
            print('\nThat Is Not Even A Number. . .\nDo You Wana Play?', end='')
            choice = 0
    print('-' * 32)
    return choice

# MODULE: displayScore
# INPUTS: score
# OUTPUTS: None
# DEF: Prints the final score
def displayScore(score):
    print('\nFinal Score:')
    print('Human:', score[0], 'Computer:', score[1], 'Tie:', score[2])
    print('\nThanks For Playing!')

# Calls the main function
main()
