'''
Created on Oct 4, 2015
Edited on ...
@author: daleinen
python2
'''
import random
import time

# this is the main method of this script
def main():

    #printing a welcome message
    welcome_message = "\nWelcome to BarDice 1.0\n"
    print welcome_message
    
    #getting number of players
    num_players = inputPlayers()
    
    #seeing which player starts game
    first_player = turnRoll(createPlayers(num_players))
    print "\nPlayer", first_player, "will roll first!\n"
    
    #getting the players order for game
    player_order = playerOrder(first_player, num_players)
    
    #if there are 4 or more players we shake once until down to 3
    if num_players > 3:
        final_three = oneShake(player_order)
        #the last three players
        print 'Players', ', '.join(map(str, final_three)), "are the final three"
    #otherwise print 2-3 players
    else:
        print 'Players', ', '.join(map(str, player_order)), "are the final three"
    
    threePlayers(player_order)  
    


# function to get final 'winner' of last three players
def threePlayers(players):
    turn = 1
    dice = 5
    keep = 0
    inputPlayer(3, 1, 5, 0)


    
#function for getting player input on dice rolls
def inputPlayer(player, turn, dice, kept):
    #creating list for roll dice values
    roll = []
    #rolling number of dice players has left
    for _ in range(0,dice):
        roll.append(random.randint(1,6))   
    #returning if no aces    
    if 1 not in roll:
        print roll, "\nSorry no aces"
        return 0

    rollValues = rollValue(roll)
    print "Player", player, "rolls: ", roll
    print "Would you like to keep", rollValues, "in", turn, "(Y for YES)?"
    
    decYN = (str(raw_input())).upper()
    
    decValue = 0
    if (decYN == "Y"):
        while decValue not in rollValues:
            decValue = int(raw_input("Which value/s? "))
        print "Will keep", decValue, "in", turn
        return decValue
    else:
        print "Which non ace value to keep?" 
        
#function for rolling a turn at bar dice
def oneShake(players):
    #creating a dictionary of players and their scores
    scores = {}
    #giving each player one shake of the dice
    for i in range(len(players)):
        scores[players[i]] = max(rollValue(diceRoll()))
        print "Player", players[i], "rolls", scores[players[i]]
        time.sleep(0.75)
    #getting the high roll
    high = max(scores.values())
    #getting all rolls
    rolls = scores.values()
    #if there are more than one high rolls start over
    if rolls.count(high) > 1:
        print "\nOne tie all tie\n"
        return oneShake(scores.keys())
    #getting rid of the highest rolling player
    for key, value in scores.items():
        if value == high:
            print "\nGoodbye player", key, "\n"
            del scores[key]
    #if more than 3 palyers remain call itself
    if len(scores) > 3:
        return oneShake(scores.keys()) 
    #return 3 players
    return scores.keys()

#function get value of a roll        
def rollValue(lst):
    #getting a count of aces or returning if no ace exists
    aces = lst.count(1)
    if aces == 0: return 0,0
    #creating a list of non aces 
    non = []
    for v in lst:
        if v != 1:
            non.append(v)
    #creating a list, calculating scores, and appending them
    scores = []
    for v in non:
        if (non.count(v) > 1):
            scores.append(v + ((aces + 1) * 10) + (non.count(v) - 1) * 10 )
        else:
            scores.append(v + ((aces + 1) * 10))
    #removing duplicates, sorting, and reversing scores        
    scores = list(set(scores))
    scores.sort()
    scores.reverse()
    return scores

# function to return starting player, param = dict of players/starting score   
def turnRoll(players):
    #giving players one roll each
    for key, value in players.items():
        players[key] = random.randint(1,6)
        print "Player", key + 1, "rolls", players[key]
        time.sleep(0.75)
    print players.values()
    #getting the high roll
    high = max(players.values())
    #checking players list for highest rollers and placing them to winners list   
    winners = {}    
    for key, value in players.items():
        if  value == high:
            winners[key] = 0
    #if high rollers are tied call itself
    if (len(winners) > 1):
        print "\nTie! Roll again players\n"
        return turnRoll(winners)
    #return remaining winning player
    return winners.keys()[0] + 1

#function to get the players order for the game
def playerOrder(first, players):
    #creating a list and appending player order
    order = []
    for i in range(0, players):
        if (first + i) <= players:
            order.append(first + i)
        else:
            order.append(i - (players - first))
    return order  

#function to return an inital roll of 5 dice
def diceRoll():
    roll = []
    for _ in range(0,5):
        roll.append(random.randint(1,6))   
    return roll
    
#function to create an initial dictionary of players        
def createPlayers(players):
    #creating a dictionary for player numbers and assign default value
    player_dict = {}
    for i in range(players):
        player_dict[i] = 0
    return player_dict
        
#function to get user input
def inputPlayers():
    #while loop to get user input and error check input
    players = 0
    while players < 2:
        try:
            players = int(raw_input("How many players in game? "))
            if players < 2: print "Please enter a int value greater than 1"
        except: print "Please enter a int value greater than 1"
    print    
    return players

 # running maing method   
if __name__ == '__main__':
    main()