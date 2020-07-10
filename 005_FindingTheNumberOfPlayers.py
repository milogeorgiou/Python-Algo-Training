#######################################################################################################################
#SUMMARY:
#This function is meant to find the number of players, and output those players.
#For instance, if there was 7 players, it would print them row by row, and then output the number of them, which is 7.
#DATE : 10/07/2020
#ENVIRONMENT : Jupyter Python 3.
#######################################################################################################################

#Importing packages
import pandas as pd
import numpy as np
import csv

#Parsing/reading the CSV file and putting it under the variable name "game_data"
game_data = pd.read_csv('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')

#Creating a second data frame to add onto the first
game_data2 = [    
    ["John", 0.9  , 9.0, "OnePiece"], 
    ["John" , 2.7, 2.4, "DBFighterZ"], 
    ["John", 2.1  , 8.7, "Halo"]
]

#Concatting both data frames into one called "game_data3"
game_data2 = pd.DataFrame(game_data2, index = ["9", "10", "11"], columns =["Name", "Hours_Played", "Score", "Game"])
game_data3 = pd.concat([game_data, game_data2])

##################################################################################################################################################
#SUMMARY: This function is intended to get the name of every player and make sure that the names are not repeated, to retrieve an accurate output.
#Parameters: None
#Output : It will output the number of players, i.e. integer 4.
##################################################################################################################################################
def getNumberOfPlayers ():
    #Phase 0 - Creating Variables
    #Setting a variable that will allow the memory to hold an array called playercount
    playercount = []
    #For every player in the csv file it will repeat this loop
    #Phase 1 - Iterating the rows in the csv file and adding the playernames to an array
    for players in game_data3.Name:
        if players in playercount:
            continue
        else:
            #This checks if the player is in the array, if not, it will add it.
            playercount.append(players)
    
    #Phase 2 - Next loop which will print all the elements in the new array playercount and outside the loop, will return our desired value.
    #And for every element in this new array with the players in it, it will print all the names. If there were 7 names, it'd print 7. In this instance, it prints 4.
    for element in playercount:
        print(element)
    #Once it finds the amount of names in the file, it gets rid of the duplicates
    return len(playercount)

#Main Function
####################
getNumberOfPlayers()
####################
#End of File#
