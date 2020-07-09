#This function is meant to get the name of every game in the csv file
#And then print them one by one.

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
#This concats both DataFrames from the previous code into "game_data3"

def Get_Name_Of_Games():
    gamenames=[]
    #Creates an empty array
    for rows in game_data3:
        game_data3.Game
        if game_data3.Game in gamenames:
            continue
        else:
            gamenames.append(game_data3.Game)
            #This will add the games to the array from the csv if they're not already in the array
    return ("Here are the names of the games played",gamenames)
Get_Name_Of_Games()
#This will run the function printing every game row by row.
