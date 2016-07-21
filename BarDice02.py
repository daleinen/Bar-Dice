#!/usr/bin/python

'''
Created on 07JUL16
Edited on ...
@author: daleinen
python03
'''

import collections
import random
import time

# this is the main method of this script
def main():
    
    # printing a welcome message
    print("\nWelcome to BAR DICE 1.0\n© 2016 Black Snake Softworks\n")

    # getting user input for number of players
    num_players = numberPlayers()
    print("-------------------\n")

    # a dictionary of all players
    my_players = createPlayers(num_players)

    # getting starting player
    first_player = startingPlayer(my_players)
    print("\nPlayer", first_player, "will roll first!")
    print("-------------------")

    # getting the players order for game
    player_order = playerOrder(first_player, num_players)

    #setting final_players = to the final 2 or 3 players
    final_players = 0
    if num_players > 3: 
        final_players = oneShake(player_order)
    else: 
        final_players = player_order

    # getting the final winner    
    winner = finalShakes(final_players)

    # function to print final game stats
    printWinner(winner)
    

# function to create an initial dictionary of players, parm = number of players        
def createPlayers(players):

    # creating a dictionary for player numbers and assign default value
    x = {}
    for i in range(players):
        x[i] = 0
    return x

#function to return an inital roll of 5 dice
def diceRoll():

    # creating a list and filling it with five dice rolls
    roll = []
    for _ in range(0,5):
        roll.append(random.randint(1,6))  
    return roll

# function to find winner from final 2-3 players
def finalShakes(players):
  
    # creating a dictionary of the final 3 players
    final_players =  collections.OrderedDict().fromkeys(players, 0)

    print(final_players)

    #while(len(players) > 1):
    
    return 1

# function to get user input for number of players
def numberPlayers():

    # while loop to get user input and error check input
    players = 0
    while(players <= 1 or players > 15):
        try:
            players = int(float(input("How many players in game? ")))
            if players <= 1: 
                print("Please enter a value greater than 1")
            elif players >= 15: 
                print("Please enter a value of 15 or less")
        except: 
            print("Please enter a value greater than 1")   
    return players

#getting number of players down to 3 with one shake
def oneShake(players):

    #creating a dictionary of players and their scores
    scores = collections.OrderedDict()

    #giving each player one shake of the dice
    for i in range(len(players)):
        scores[players[i]] = max(rollValue(diceRoll()))
        print("Player", players[i], "rolls", scores[players[i]])
        time.sleep(0.75)
    
    #getting the high roll
    high = max(scores.values())
    #getting all rolls
    rolls = list(scores.values())

    #if there are more than one high rolls start over
    if rolls.count(high) > 1:
        print ("\nOne tie all tie\n")
        return oneShake(list(scores.keys()))

    #getting rid of the highest rolling player
    for key, value in list(scores.items()):
        if value == high:
            print("\nGoodbye Player", key, "\n")
            del scores[key]
          
    #if more than 3 palyers remain call itself
    if len(scores) > 3:
        return oneShake(list(scores.keys()))

    #return 3 players
    return list(scores.keys())

# function to get the players order for the game
def playerOrder(first, players):

    #creating a list and appending player order
    order = []
    for i in range(0, players):
        if (first + i) <= players: order.append(first + i)
        else: order.append(i - (players - first))

    print("The player order will be:\n")

    #printing player order
    for i in order:
        print("Player", i)
        time.sleep(0.50)
    print()

    return order 

# function to print the winning player
def printWinner(x):
    
    print("The winner is PLAYER", x, "\n")

#function get value of a roll        
def rollValue(lst):

    #getting a count of aces or returning if no ace exists
    aces = lst.count(1)
    if aces == 0: return 0,0

    #creating a list of non aces 
    non = []
    for i in lst:
        if i != 1:
            non.append(i)

    #creating a list, calculating scores, and appending them
    scores = []
    for v in non:
        if (non.count(v) > 1):
            scores.append(v + ((aces + 1) * 10) + (non.count(v) - 1) * 10 )
        else:
            scores.append(v + ((aces + 1) * 10))
         
    return list(set(scores))

# function to get starting player/down to three, parm = 
def startingPlayer(players):

    # giving the players one roll each
    for key, value in players.items():
        players[key] = random.randint(1,6)
        print("Player", key + 1, "rolls", players[key])
        time.sleep(0.75)

    # getting the high roll
    high = max(players.values())

    #checking players list for highest rollers and placing them to winners list   
    winners = {}    
    for key, value in players.items():
        if  value == high:
            winners[key] = 0

    # if high rollers are tied call itself
    if (len(winners) > 1):
        print("\nTie! Roll again players\n")
        return startingPlayer(winners)

    # creating a list of one last remaining player and returning plus 1
    x = list(winners.keys())[0]
    return x + 1

 # running maing method   
if __name__ == '__main__':
    main()