import sys
import re
import numpy as np

# contains info of data used
# ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/README.txt

avg_temp = {}
for line in sys.stdin:

    hour, temp = line.split(",")
    temp = float(temp)

    if hour in avg_temp.keys():
        avg_temp[hour] = [avg_temp[hour][0] + temp , avg_temp[hour][1] + 1]
    else:
        avg_temp[hour] = [temp, 1]


for time in avg_temp:
    print("TIME = "+time+" -----> "+ str(avg_temp[time][0]/avg_temp[time][1]))


