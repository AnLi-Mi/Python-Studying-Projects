# Create a Trading Game simulation: drwa a marble form a bag. The bag has 10 marbles:
# 6 green and 4 red. If you draw green marble you win the same amount you bet,
# if you draw a red marble you lose the amount you bet.
# Marbles are returned to a bag after each round. Before each draw a user can decide
# how mych they want to bet. The user starts a game with 1000$ in the wallet.
# If the user looses half of money then the game is over.

# Extra: replace two marbles: 1 green with black 10x winner marble and 1 red with
# whte 5x looser marble

print('Project - Trading game simulation')

import random

bag=['black', ' green', 'green', 'green', 'green', 'green', 'white', 'red', 'red', 'red']
wallet = 1000
games = 3
for game in range (1, games+1):                 
    bet = int(input('How much do you bet?: '))
    los = random.choice(bag)
    print(f'Round {game}: {los}')
    if los=='green':
        wallet = wallet + bet
        print (f'Great! You have {wallet}$')
    elif los =='black':
        wallet = wallet + 10*bet
        print (f'What a luck! You win {10*bet}$. You have {wallet}$')
    elif los == 'white':
        wallet = wallet - 5*bet
        print (f'What a bad luck! You loose {5*bet}$. You have {wallet}$')
    else:
        wallet = wallet - bet
        print (f'Oh, no... You have {wallet}$')
    if wallet <500:
        print ('You lost... You have less than 500$, you can not play')
        break




