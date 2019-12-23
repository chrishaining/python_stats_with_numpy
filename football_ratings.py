#this program uses Kelley's Equation to estimate the ability of Premier League football teams.

#imports
import pandas as pd
# import tkinter as tk
# from tkinter import *

# wind=Tk()
# btn=Button()
# btn.pack()
# btn["text"]="Premier League stats"
#use a Bayesian approach to calculate a prior estimate of each team's ability
#this means using last season's table (i'll take five teams to start)
#there are a few ways to enter the data from the table - a dictionary, pandas, SQL. I want to practise pandas, so I've found a csv file to download. Source: https://www.premierleague.com/tables?co=1&se=210&ha=-1
table_2018_2019 = pd.read_csv('league-table-2018-2019.csv')
# print(table_2018_2019)
print(table_2018_2019.columns)
#work out the average points per game (PPG) and add this to the table. To do this, divide Points (Pts) by games played (P)
table_2018_2019['PPG'] = round((table_2018_2019.Pts / table_2018_2019.P), 1)
print(table_2018_2019)

#the equation
reliability = 0.5

#points is the current points this season, games is the current games played this season
# def estimate_ability(reliability, points, games, last_season_ppg):
#     ability = ((reliability*(round((points/games), 1))) + ((round((1 - reliability), 1)) * last_season_ppg))
#     return ability

def estimate_ability(team, reliability, points, games):
    # last_season_ppg = table_2018_2019.loc[table_2018_2019.Team==team, 'PPG']
    last_season_row = table_2018_2019.loc[table_2018_2019.Team==team]
    last_season_ppg = last_season_row['PPG'].item()
    # return last_season_ppg
    ability = (reliability*(round((points/games), 1))) + ((round((1 - reliability), 1)) * last_season_ppg)
    raw_ability = (reliability*(points/games)) + ((1 - reliability) * last_season_ppg)
    ability = round(raw_ability, 1)
    return "Based on a comparison of current form with last season's results, {}'s ability is {}. The measure of ability is points per game".format(team, ability)

# expect 2.9
test1 = estimate_ability('Liverpool', 1.0, 49, 17)
print(test1)

#expect 1.3 to 1.4
test2 = estimate_ability('Man Utd', 1.0, 25, 18)
print(test2)



# expect about 1.4-1.5 if reliability is 1.0 (i.e. it takes the current PPG); expect 1.9 (last season;s PPG) if reliability is 0; since we are at halfway in the current season (18 games), what if reliability is 0.5? (answer is that it would give PPG of 1.65)
# spurs_ability = estimate_ability(reliability, 26, 18, 1.9)
# print("The estimate of Spurs' ability is {}.".format(spurs_ability))

# liverpool_ability = estimate_ability(reliability, 49, 17, 1.9)
# print("The estimate of Liverpool's ability is {}.".format(liverpool_ability))

#so, this works, but it can be refactored to make it more DRY. next steps - change the estimate_ability function to take the team as an argument. If possible, can I take the information directly from the table? Even better, would it be possible to import the second table, and use this as well. A further development would be to add the outcome of estimate_ability to the new table. Another idea is to calculate the reliability.
