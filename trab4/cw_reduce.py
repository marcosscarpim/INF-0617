import os
import sys
import csv

os.chdir("/home/liselene/Projects/ComplexData/INF-0617/trab4") 

counts = {}

for line in sys.stdin:
    try:
        word, count = line.split(',')
        count = int(count)
        if word not in counts:
           counts[word] = count
        else :
           counts[word] = counts[word] + count
    except:
        continue

words = sorted(counts, key=counts.get, reverse=True)

with open('words.csv', mode='w') as words_file:
    words_writer = csv.writer(words_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for word in  words[1:3000]:
        words_writer.writerow([word,str(counts[word])])
        #print(word+","+str(counts[word]))

