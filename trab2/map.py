import sys
import re

# contains info of data used
# ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/README.txt

for line in sys.stdin:

    fields = line.split()

    date = fields[3]
    latitude = fields[7]
    longitude = fields[6]
    hour = fields[4]
    temp = float(fields[9])
    min_temp = float(fields[11])
    max_temp = float(fields[10])

    if min_temp == -9999 or max_temp == -9999 or temp == -9999 or float(fields[12]) == -9999 \
            or any(float(fields[i]) == -9999 for i in range(30, 35)):
        continue

    print(date+","+hour+","+latitude+","+longitude+","+str(min_temp)+","+str(max_temp))