######################################################################################################################################
#SUMMARY: This will find the best ratio amongst the players, by calculating the values of the hours and bringing an accurate result
#Date: 19/07/2020
#ENVIRONMENT: Jupyter Python 3
######################################################################################################################################

#Importing packages
import pandas as pd
import csv

#Using an easier method to parse/read our CSV file into a dataframe.
f = open('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
csv_f = csv.reader(f)

######################################################################################################################################
#SUMMARY: This will take every score from the player, and their hours played on each game, to work out the average ratio.
#This will be done row by row for every game, and in the end it will output who's ratio is the largest.
#Parameters: None
#Output: "The person with the largest ratio is, Ian, with, 3.435897435897436, score per hour."
######################################################################################################################################

def FindBestRatioOfPlayers():
#Creating the new variables, which will later be used for storing and calculating values
    maxratio=0.0
    maxplayer=""
    #The Dictionary will contain the two variables of the hours played and the score of the player
    newDict={}
    i = 0
    for row in csv_f:
        if i == 0:
            print("---")
			#This print and "if i == 0" will skip the first row, the titles of the values
        else:
			#This next part is creating variables which will hold our rows and turn them into our desired data type, in this case float.
            scoreofrow=row[2]
            scorefloat=float(scoreofrow)
            hoursp=row[1]
            hourspf=float(hoursp)
            playername=row[0]
            if playername in newDict:
			#The if else statement will make variables from the dictionary values and keys, firstly for easier access, but secondly for calculation in the next part.
                oldarray=newDict[playername]
                oldscore=oldarray[0]
                oldhours=oldarray[1]
                newscore=scorefloat+oldarray[0]
                newhours=hourspf+oldarray[1]
                newarray=[newscore, newhours]
                newDict[playername]=newarray
            else:
			#All of this is calculated to create the value array which will hold both the score and hours, later this will be used to create the average ratio.
                valuearray=[scorefloat, hourspf]
                newDict[playername]=valuearray
        i = i + 1
    print(newDict)
    #phase 2 - Creating the average from both the values of the key, playername
    averageDict={}
    for key in newDict:
	#For every key inside our new dictionary, it will create the ratio and the average, so it will take every ratio from the games and divide them by 3 for each player.
        value=newDict[key]
        ratio=(value[0]/value[1])
        averageDict[key]=ratio
    print(averageDict)
    #At the end we expect to have a new dictionary and the key will be the playername and the value will be the average
    #Phase 3 - Find the max average of the player within the dictionary
    #I also expect to have an average which is the largest, and print who's average it is
    for key in averageDict:
        print(key)
        ratiovalue=averageDict[key]
        print(ratiovalue)
        if maxratio < ratiovalue:
            maxratio = ratiovalue
            maxplayer=key
    print()
    print("The person with the largest ratio is", (maxplayer), "with", maxratio, "score per hour.")
###############
#Main Function
###############
FindBestRatioOfPlayers()
###############
#End of File
###############
