import numpy as np

#create a list of lifespans (i.e. the age at which members of a population lived to)
lifespans = [0, 85, 31, 90, 76, 2, 50, 78, 86, 40, 89, 92, 64, 58, 73, 68, 4, 70, 89, 93]
sorted_lifespans = np.sort(lifespans)
print(sorted_lifespans)
median = np.median(lifespans)
#expect 71.5
print("The median lifespan is {}.".format(median))

#calculate the first and third quartiles
first_quartile = np.percentile(lifespans, 25)
third_quartile = np.percentile(lifespans, 75)

#expect 50, 71.5, 86
print("The first quartile is {}. The median is {}. The third quartile is {}.".format(first_quartile, median, third_quartile))

#calculate interquartile range (expect about 36)
interquartile_range = third_quartile-first_quartile
print("The interquartile range is {}.".format(interquartile_range))

min=np.min(lifespans)
max=np.max(lifespans)
print("min={} and max={}".format(min, max))
#create five-number summary of lifespans (min, first quartile, median, third quartile, max)
print("The five-number summary of lifespans is (min={min}, first quartile={first}, median={median}, third quartile={third}, max={max})".format(min=min, first=first_quartile, median=median, third=third_quartile, max=max))
