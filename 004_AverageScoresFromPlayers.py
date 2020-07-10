import pandas as pd
import numpy as np
import csv
#Importing packages
game_data = pd.read_csv('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
game_data
#Parsing the CSV
game_data2 = [    
    ["John", 0.9  , 9.0, "OnePiece"], 
    ["John" , 2.7, 2.4, "DBFighterZ"], 
    ["John", 2.1  , 8.7, "Halo"]
]
game_data2 = pd.DataFrame(game_data2, index = ["9", "10", "11"], columns =["Name", "Hours_Played", "Score", "Game"])
game_data3=pd.concat([game_data, game_data2])
#Concating both csvs into one called game_data3

def getAverageScoreFromAllPlayers ():
    scores=[]
    averagescores=0.0
    #creating variables for the final output
    for score in game_data3.Score:
        game_data3.Score
        if game_data3.Score in scores:
            continue
            
        else:
            scores.append(game_data3.Score)
            #If the score is not already in the array it adds it from the csv file
    scores2 = len(sum(scores))
    #This takes the length of the sum of the scores, giving the average of the scores.
    print(scores)
    return print("The average scores from all players across all games is", scores2)
#Gets the average score for every player individually and prints it row by row
getAverageScoreFromAllPlayers()
