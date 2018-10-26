import os
import re
import time
from multiprocessing import Process

# fix this in your computer
os.chdir("/home/liselene/Projects/ComplexData/INF-0617/trab4/gut_test/")
print(os.getcwd())

def count_words(content):
    content = content.lower().replace('\n', ' ')
    p = re.compile('[0-9]')
    content=p.sub('',content)
    p = re.compile(r'\W+')
    words = p.split(content)

    unique_words = set(words)
    print(unique_words)
    
#print(content)

#    for char in unique_chars:
#        count = content.count(word)
#        if count > final_count:
#            letter = char
#            final_count = count
#    return letter, final_count

filenames = []

for file in os.listdir("./txt"):
    if file.endswith(".txt"):
        filenames.append(file)

for filename in filenames:
    f = open("./txt/" + filename, encoding="utf-8", errors="ignore")
    content = f.read()
    count_words(content)
    f.close()
    print(filename)

