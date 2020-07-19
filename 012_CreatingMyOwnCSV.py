###########################################################################################################################################################################################
#SUMMARY: Instead of parsing a CSV, this file will create a CSV, which if you run should save into your PC as a csv file, which will then be able to be opened with something such as Excel
#Date: 19/07/2020
###########################################################################################################################################################################################

import csv

#This will open a new csv file, which you can name anything you want, and then create the writer, which I've called "csv.writer" using the "(q)" variable
with open('NewPlayers.csv', 'w', newline = '') as q:
    newwriter = csv.writer(q)

#This next part, is very simple, you just write the rows, using commas to space them out and a "([" to open it and "])" to close it.
#You can write as many as you want, or only one.
    newwriter.writerow(['Name', 'Hours_Played', 'Score', 'Game'])
    newwriter.writerow(['Jim', '1.2', '5.3', 'Dungens'])
    newwriter.writerow(['Elijah', '2.1', '6.8', 'Halo'])
    newwriter.writerow(['Harry', '3.7', '8.1', 'OnePiece'])

#############
#End of File
#############
