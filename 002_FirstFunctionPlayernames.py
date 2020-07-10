#This function was intended to return the names of every time the player names come up inside the csv file.
#It should return every name 3 times.

import pandas as pd
import numpy as np
import csv
#Importing packages
game_data = pd.read_csv('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
#Parsing the CSV as "game_data"
game_data
game_data2 = [    
    ["John", 0.9  , 9.0, "OnePiece"], 
    ["John" , 2.7, 2.4, "DBFighterZ"], 
    ["John", 2.1  , 8.7, "Halo"]
]
game_data2 = pd.DataFrame(game_data2, index = ["9", "10", "11"], columns =["Name", "Hours_Played", "Score", "Game"])
game_data3=pd.concat([game_data, game_data2])
#Concatting both DataFrames from the previous code into "game_data3"
def get_player_names ():
    playernames=[]
    #Creating the variable and making a loop for every player in the csv
    for players in game_data3.Name:
        game_data3.Name
        if game_data3.Name in playernames:
        #checks if the names in the new array are in there, if they are then it continues. If they aren't, then it will
            continue
            
        else:
            playernames.append(game_data3.Name)
            #If the names aren't already in the array then they'll be added using .append
    return ("The name's of the players are", playernames)
    #This will simply return "The name's of the players are", followed by each player's name in consecution.
get_player_names()
