import sys
import re

# contains info of data used
# ftp://ftp.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/README.txt

for line in sys.stdin:

    fields = line.split()

    hour = fields[4]
    temp = float(fields[9])

    if temp == -9999:
        continue

    print(hour+","+str(temp))