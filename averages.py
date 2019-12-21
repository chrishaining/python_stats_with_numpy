import numpy as np

#create a list of lifespans (i.e. the age at which members of a population lived to)
lifespans = [0, 85, 31, 90, 76, 2, 50, 78, 86, 40, 89, 92, 64, 58, 73, 68, 4, 70, 89, 93]

#calculate the size of the population (i.e. the number of people in lifespans survey) - expect 20. This helps me to get a rough feel for the numbers I should expect when calculating averages
population_size = len(lifespans)
# print(population_size)

#sort the lifespans array (useful to give me a rough feel for the numbers I should expect when calculating average)
sorted_lifespans = np.sort(lifespans)
print(sorted_lifespans)
#calculate the mean of lifespans. expect something like 40-60
mean_lifespan = np.mean(lifespans)
print("The mean lifespan is {}.".format(mean_lifespan))

#calculate the median of lifespans. expect 71.5
median_lifespan = np.median(lifespans)
print("The median lifespan is {}".format(median_lifespan))

#calculate how many results are above the mean. expect about 65% (because 13/20 are above mean)
above_mean = int(100 * np.mean(lifespans > mean_lifespan))
print("{}% of people lived longer than the mean lifespan.".format(above_mean))

#calculate how many results are below mean. expect 35%
below_mean = int(100 * np.mean(lifespans < mean_lifespan))
print("{}% of people lived less than the mean lifespan.".format(below_mean))
