#this program uses Kelley's Equation to estimate the ability of Premier League football teams.

#imports
import pandas as pd

#use a Bayesian approach to calculate a prior estimate of each team's ability
#this means using last season's table (i'll take five teams to start)
#there are a few ways to enter the data from the table - a dictionary, pandas, SQL. I want to practise pandas, so I've found a csv file to download. Source: https://www.premierleague.com/tables?co=1&se=210&ha=-1

table_2016_2017 = pd.read_csv('league-table-2016-2017.csv')
print(table_2016_2017)

table_2017_2018 = pd.read_csv('league-table-2017-2018.csv')
print(table_2017_2018)

table_2018_2019 = pd.read_csv('league-table-2018-2019.csv')
# print(table_2018_2019)
print(table_2018_2019.columns)
#work out the average points per game (PPG) and add this to the table. To do this, divide Points (Pts) by games played (P)
table_2018_2019['PPG'] = round((table_2018_2019.Pts / table_2018_2019.P), 1)
print(table_2018_2019)

#the equation

#points is the current points this season, games is the current games played this season
def estimate_ability(team, reliability, points, games):
    last_season_row = table_2018_2019.loc[table_2018_2019.Team==team]
    last_season_ppg = last_season_row['PPG'].item()
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

#23/12/2019 - next step is to develop the reliability variable. At the moment, I've made it 1.0, which means that a team's estimated ability is the same as its teacurrent form. That's not much use, so I'm going to add data from previous seasons (go back to 2016-2017). The extent to which season 2016-2017 PPG reflets 2017-2018 PPG is the starting reliability.
