##########################################################################################################################################
#SUMMARY: This function is intended to find the player that has played the most hours on a certain game, depending on the paramters put in
#ENVIRONMENT: Jupyter Python 3
#Date: 18/07/2020
##########################################################################################################################################

#Importing packages
import pandas as pd
import csv

#Parsing the CSV file with an easier more efficient method
f = open('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
csv_f = csv.reader(f)

##########################################################################################################################################
#SUMMARY : This function is intended to find the player with the most hours on the specified game, in this case. Dungens.
#Parameters: "game_target" - This could be any game_name inside of our CSV file/Data frame
#Output :
def playerNameThatPlayedTheMostHours(game_target):
    #Phase 0 : Creating the variables
    max = 0.0
    game_max=""
    myDictionary = {}
    i = 0
    #Phase 1: Populate Dictionary with game names and corresponding hours played
    for row in csv_f:
	#This if statement will skip the first row, the names of the values, i.e. "Name", "Game_name"
        if i == 0:
            i=i+1
            continue
		#This will check if the row is equal to our paramter, if it is, then it will overwrite new values for the rows.
		#It will then create a dictionary to hold the new calculated values for the specified game.
        if row[3] == game_target:
            print(row)
            player= row[0]
            hoursp = row[1]
            hourspf = float(hoursp)
        if player in myDictionary and row[3] == game_target:
            myDictionary[player] += hourspf
        else:
            myDictionary[player] = hourspf
    print(myDictionary)
    #Phase 2: Find max in the dictionary
	#For every element in the dictionary, it will check for the maximum, by checking if the "max" variable is smaller than hours, if so it so,
	#It will overwrite the max variable with the larger "hours"
    for element in myDictionary:
        player = element
        hours = myDictionary[element]
        #print(player, ",", hours)
        if max < hours:
            if row[3] == game_target:
                continue
            max = hours
            playermax = element
            print(hours)
            print(element)
			#The desired output for this would be "The player with the most hours on, dungens, is Rick with 3.2 hours."
    return ("The player with the most hours on", game_target, "is", playermax, "with", max, "hours.")
	################
	#Main Function:
	###############
playerNameThatPlayedTheMostHours('Dungens')
############
#End of File
############
