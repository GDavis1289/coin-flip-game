# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 17:34:50 2020

@author: gdavi
"""


# Coin Flip Game!
# A user guesses if a coin will be heads or tails
# They can play as many times as they would like with running totals
# Totals include how many games were played, and how many times they guessed correctly

import random

correctGuesses = 0
gamesPlayed = 0

playGame = 0
while playGame == 0:

# User must guess heads or tails    
    count = 0
    while count < 1:
        user_guess = input('Guess heads or tails (type \'h\' for heads, \'t\' for tails): ')
        guess = user_guess.lower()
        if guess == 'h':
            guess = 'Heads'
            count += 1
        if guess == 't':
            guess = 'Tails'
            count += 1
     
    
    flip = ['Heads', 'Tails']

# The random flip of the coin
    def heads_or_tails(flip):
        return random.choice(flip)

    coinFlip = heads_or_tails(flip)

# The result
    if coinFlip == guess:
        print(coinFlip + '!, you guessed correctly!')
        correctGuesses += 1
        gamesPlayed += 1
        print('Total Correct Guesses: ' + str(correctGuesses))
        print('Total Games Played: ' + str(gamesPlayed))
    else:
        print(coinFlip + ', sorry you guessed incorrectly...')
        gamesPlayed += 1
        print('Total Correct Guesses: ' + str(correctGuesses))
        print('Total Games Played: ' + str(gamesPlayed))
        
# Asking if user wants to play again        
    flipAgain = input('Do you want to flip again? (enter \'YES\' or \'NO\') ')
    playAgain = flipAgain.lower()
    if playAgain == 'no':
        playGame += 1
    elif playAgain != 'yes' or playAgain != 'no':
        flipAgain = input('TRY AGAIN. Do you want to flip again? (enter \'YES\' or \'NO\') ')
        playAgain = flipAgain.lower()
        if playAgain == 'no':
            playGame += 1