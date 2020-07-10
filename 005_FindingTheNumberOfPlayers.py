import pandas as pd
import numpy as np
import csv
#Importing packages
game_data = pd.read_csv('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
game_data
#Parsing/reading the CSV file and putting it under the variable name "game_data"
game_data2 = [    
    ["John", 0.9  , 9.0, "OnePiece"], 
    ["John" , 2.7, 2.4, "DBFighterZ"], 
    ["John", 2.1  , 8.7, "Halo"]
]
#Creating a second data frame to add onto the first
game_data2 = pd.DataFrame(game_data2, index = ["9", "10", "11"], columns =["Name", "Hours_Played", "Score", "Game"])
game_data3=pd.concat([game_data, game_data2])
#Concatting both data frames into one called "game_data3"

def getNumberOfPlayers ():
    playercount=[]
    #Setting a variable that will allow me to hold an array called playercount
    for players in game_data3.Name:
    #For every player in the csv file it will repeat this loop
        game_data3.Name
        if players in playercount:
            continue
            
        else:
            playercount.append(players)
        #This checks if the player is in the array, if not, it will add it.
    for element in playercount:
    #And for every element in this new array with the players in it, it will print all the names. If there were 7 names, it'd print 7. In this instance, it prints 4.
        print(element)
    #Once it finds the amount of names in the file, it gets rid of the duplicates
    return len(playercount)
getNumberOfPlayers()
