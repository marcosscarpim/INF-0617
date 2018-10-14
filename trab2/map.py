import sys
import re

# contains info of data used
# ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/README.txt

for line in sys.stdin:

    fields = line.split()

    if any(float(fields[i]) == -9999 for i in range(9, 12)) \
            or any(float(fields[i]) == -9999 for i in range(30, 37)) \
            or any(float(fields[i]) == -99 for i in range(28, 30))\
            or float(fields[12]) == -9999:
        continue

    date = fields[3]
    latitude = fields[7]
    longitude = fields[6]
    hour = fields[4]
    temp = float(fields[9])
    min_temp = float(fields[11])
    max_temp = float(fields[10])

    print(date+","+hour+","+latitude+","+longitude+","+str(min_temp)+","+str(max_temp))