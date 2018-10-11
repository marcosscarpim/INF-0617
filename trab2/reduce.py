import sys
import re
import numpy as np

# contains info of data used
# ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/README.txt

max_var = 0.0
max_date = ""
max_hour = ""
max_lat = ""
max_long = ""
for line in sys.stdin:

    date, hour, lat, long, min_temp, max_temp = line.split(",")
    min_temp = float(min_temp)
    max_temp = float(max_temp)

    var_temp = max_temp - min_temp

    if max_var < var_temp:
        max_var = var_temp
        max_date = date
        max_hour = hour
        max_lat = lat
        max_long = long

print(max_date+ " "+ max_hour+ ", ("+ max_lat+ ", "+ max_long+ "), "+ str(max_var))


