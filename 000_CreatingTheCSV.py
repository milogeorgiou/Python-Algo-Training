#This reads/parses a CSV with players in a file with data on their game score and game time on each game, following their names.
import pandas as pd
import numpy as np
import csv
# ^^ Importing all the packages 
game_data = pd.read_csv('C:/Users/mgthe/OneDrive/Documents/game_scores.csv')
# ^^ Importing the CSV I will use for the later functions.
game_data
# ^^ Shows CSV when compiled