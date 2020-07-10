import pandas as pd
import csv
#Importing packages
f = open('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
csv_f = csv.reader(f)
#Using the shorter more effective csv reading method

def playerNameThatPlayedTheMostHours():
    #Phase 0 : Creating the variables
    max = 0.0
    game_max=""
    myDictionary = {}
    i = 0
    #Phase 1: Populate Dictionary with game names and corresponding hours played
    for row in csv_f:
        if i == 0:
            i=i+1
            #This variable i will make it so it skips the first row in the dictionary, containing the names of the columns.
            continue
        print(row)
        player = row[0]
        hoursp = row[1]
        #These variables override the rows that contain the player names and the hours played to make it easier to access.
        hourspf = float(hoursp)
        #This makes the hoursplayed into a float, so we can find the maximum with a readable value.
        if player in myDictionary:
            myDictionary[player] += hourspf
            #This checks if the player is already in the dictionary, if it is then it adds the value on top using hourspf.
        else:
            myDictionary[player] = hourspf
            #If it is not in the dictionary, then it will create a new value using the float variable we created.
    print(myDictionary)
    #Phase 2: Find max in the dictionary
    for element in myDictionary:
        player = element
        hours = myDictionary[element]
        #This replaces the element we've used in this for loop with "player" to make it easier to calculate a result.
        print(player, ",", hours)
        if max < hours: 
            max = hours
            #Within this if loop, it checks if the value of max is lower than the value of hours
            #If it is, it will override the max with the value of hours
            playermax = element
            #This changes the playermax's value to the value of element, which will allow us to output our desired result in the end line.
            print(hours)
            print(element)
    return ("The player", playermax, "has played the most, with", max, "hours")
#the player rick has played the most, with 9.6 hours
playerNameThatPlayedTheMostHours()
