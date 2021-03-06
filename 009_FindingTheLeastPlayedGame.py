##############################################################################################################################################################
#SUMMARY: As the previous file was finding the most played game, this is findingg the least played game with the least hours. Most variables will be reversed.
#Date : 18/07/2020
##############################################################################################################################################################

import pandas as pd
import csv
f = open('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
csv_f = csv.reader(f)

##########################################################################################################
# SUMMARY: I would like to display the game with the least amount of hours and display the hours aswell.
# Parameters: None 
# OUTPUT: It should output "The least played game is Diablo with 3.0 hours"
##########################################################################################################

def gameThatHasTheLeastHoursPlayed():
    #Phase 0 : Creating the variables
    #I created a much larger number than I needed for extra caution, just to make sure it will always be larger.
    min = 891729857623987658723659876239876598273695876236523.0
    game_min=""
    #Creation of the dictionary which will be used to store the calculations 
    myDictionary = {}
    i = 0
    #Phase 1: Populate Dictionary with game names and corresponding hours played
    for row in csv_f:
        #This if statement will ignore the first row with "if i==0...."
        if i == 0:
            i=i+1
            continue
        print(row)
        #This updates the rows with easily accessed variables
        game_name = row[3]
        hoursp = row[2]
        hourspf = float(hoursp)
        #If the game is already inside the dictionary, it will add on the hours, if not, it will create a new value for that game.
        if game_name in myDictionary:
            myDictionary[game_name] += hourspf
        else:
            myDictionary[game_name] = hourspf
    print(myDictionary)
    #Phase 2: Find min in the dictionary
    #For every element in the dictionary, it will now create a score variable, instead of having to call the dictionary's elements every time
    #It will then check if the minimum is larger than the score, if it is, then it will create a new value and override it with the score.
    for element in myDictionary:
        game_name = element
        score = myDictionary[element]
        print(game_name, ",", score)
        if min > score:
            min = score
            game_min = element
            print(score)
            print(element)
    #It then returns the game and the value
    return("The most played game is", game_min, "with", min, "hours")
#The desired output is: "the least played game is diablo with 3.0 hours"
##############
#Main Function
##############
gameThatHasTheLeastHoursPlayed()
############
#End of file
############
