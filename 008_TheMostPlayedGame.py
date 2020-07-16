#######################################################################################################################
#SUMMARY:
#This function is meant to 
#
#DATE : 15/07/2020
#ENVIRONMENT : Jupyter Python 3.
#######################################################################################################################

#Importing packages
import pandas as pd
import csv

#Parsing/reading the CSV file through the use of the csv package
f = open('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
csv_f = csv.reader(f)

##########################################################################################################################################################################################
#SUMMARY: This function is intended to take every game and calculate the maximum amount of hours that's been played out of the games by putting their total hours played into a dictionary
#Parameters: None
#Output : It should print the csv file, followed by the dictionary. Then row by row it should print every game with it's score next to it individually, then output the final result, which in this case should be Dungens with 17.0 hours.
############################################################################################################################################################################################################################################

#Defining the function
def gameThatHasTheMostHoursPlayed():
    #Phase 0 : Creating the variables, and the dictionary which will be used to hold the names of the games.
    max = 0.0
    game_max=""
    myDictionary = {}
    i = 0
    #Phase 1: Populate Dictionary with game names and corresponding hours played
    for row in csv_f:
		#This i variable will make sure that it does not count the titles of the values, in this case "Name", "Game_Name" and so on.
        if i == 0:
            i=i+1
            continue
        print(row)
		#These now update the variables with the data of the rows to make them easier to access instead of having to go to the rows directly.
        game_name = row[3]
        hoursp = row[2]
        hourspf = float(hoursp)
		#This next part, will check if the name of the games is inside the dictionary, and if it isn't, it will create a new value. If it already exists then it will add it ontop.
        if game_name in myDictionary:
            myDictionary[game_name] += hourspf
        else:
            myDictionary[game_name] = hourspf
    print(myDictionary)
    #Phase 2: Find max in the dictionary
	#For every element in the dictionary it will update the maximum using the score.
	#If the score is larger than the maximum, then the max is equal, therefore updating it everytime there's a bigger score, to calculate the maximum score, for which game is played the most.
    for element in myDictionary:
        game_name = element
        score = myDictionary[element]
        print(game_name, ",", score)
        if max < score:
            max = score
            game_max = element
            print(score)
            print(element)
    return("The most played game is", game_max, "with", max, "hours")
#question 8: the most played game is dungens with 17.0 hours

###############
#Main function:
gameThatHasTheMostHoursPlayed()
###############################
#End of file#
