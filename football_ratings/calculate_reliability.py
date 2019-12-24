import pandas as pd
import numpy as np
table_2016_2017 = pd.read_csv('league-table-2016-2017.csv')

table_2017_2018 = pd.read_csv('league-table-2017-2018.csv')
table_2018_2019 = pd.read_csv('league-table-2018-2019.csv')


#get the PPG.
table_2016_2017['PPG'] = round((table_2016_2017.Pts / table_2016_2017.P), 1)
print(table_2016_2017)

table_2017_2018['PPG'] = round((table_2017_2018.Pts / table_2017_2018.P), 1)
print(table_2017_2018)
table_2018_2019['PPG'] = round((table_2018_2019.Pts / table_2018_2019.P), 1)


#calculate the reliability. for each team in the newer table, how far is the PPG from the previous year?
corr_2018 = round(table_2017_2018.corrwith(table_2016_2017, axis = 0), 2)
print(corr_2018)
reliability = corr_2018.PPG
print(reliability)

#this gives a reliability of 0.97, but it isn't exactly the figure I want. I'm looking for the reliability for each team's stats, but this gives the average. However, it will do for now.
corr_2019 = round(table_2018_2019.corrwith(table_2017_2018, axis = 0), 2)
print(corr_2019)
reliability = (reliability + corr_2019.PPG) / 2
print(reliability)
#an average of the reliability is 0.96
