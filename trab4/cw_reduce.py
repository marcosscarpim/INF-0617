import os
import sys

os.chdir("/tmp/data/") 

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

f = open('trab4/words.txt', mode='w')
for word in  words[1:3001]:
   f.write(word+'\n')
f.close()
