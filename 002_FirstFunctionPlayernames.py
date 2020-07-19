###########################################################################################################
#SUMMARY : This is meant to find out all of the players who are inside of the csv file.
#It should print them one by one, three per unique name.
#ENVIRONMENT : Jupyter Python 3
#Updated date: 16/07/2020
###########################################################################################################

#It should return every name 3 times.

#Importing packages
import pandas as pd
import numpy as np
import csv

#Parsing the CSV as "game_data"
game_data = pd.read_csv('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')

game_data2 = [    
    ["John", 0.9  , 9.0, "OnePiece"], 
    ["John" , 2.7, 2.4, "DBFighterZ"], 
    ["John", 2.1  , 8.7, "Halo"]
]
#Concatting both DataFrames from the previous code into "game_data3"
game_data2 = pd.DataFrame(game_data2, index = ["9", "10", "11"], columns =["Name", "Hours_Played", "Score", "Game"])
game_data3=pd.concat([game_data, game_data2])

##################################################################################################################################################
#SUMMARY: This function was intended to return the names of every time the player names come up inside the csv file.
#Parameters: None
#Output : This will output the playernames row by row, the expected result would be every name three times
##################################################################################################################################################

def get_player_names ():
    #Creating the variable and making a loop for every player in the csv
    playernames=[]
    for players in game_data3.Name:
        game_data3.Name
		#checks if the names in the new array are in there, if they are then it continues. If they aren't, then it will
        if game_data3.Name in playernames:
            continue
        else:
			#If the names aren't already in the array then they'll be added using .append
            playernames.append(game_data3.Name)
		#This will simply return "The name's of the players are", followed by each player's name in consecution.
    return ("The name's of the players are", playernames)

##################
#Main Function#
##################
get_player_names()
##################
#End of file#
##################
