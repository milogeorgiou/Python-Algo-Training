import pandas as pd
import csv
#Importing packages
f = open('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
csv_f = csv.reader(f)
#Using a new method to import a csv, in a much shorter section of code
#With this method I have also removed the second part, with John in it.
def printAllRowOfPlayer(playername):
    for row in csv_f:   
        if row[0] == playername:
            print(row[2])
            #Using the parameter "playername", the user can choose which player to print the score of.
            #This if statement is checking if the name of the row is equal to the "playername" the user has chose
printAllRowOfPlayer("Rick")
#This will print all of "Rick"'s scores
