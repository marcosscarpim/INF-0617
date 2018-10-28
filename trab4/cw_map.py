import os
import re

# fix this in your computer
os.chdir("/tmp/data/gut/")

def count_words(content):
    unique_words = set(content)
    for word in unique_words:
        count = content.count(word)
        print ("{0},{1}".format(word,count))

def read_words(content):
    content = content.lower().replace('\'', '')
    p = re.compile('[0-9]')
    content=p.sub('',content)
    p=re.compile(r"_+")
    content=p.sub('',content)
    p = re.compile(r'\W+')
    content=p.sub(' ',content)
    p = re.compile(r'\s+')
    words = p.split(content)
    return words

filenames = []

for file in os.listdir("./txt"):
    if file.endswith(".txt"):
        filenames.append(file)

for filename in filenames:
    f = open("./txt/" + filename, encoding="utf-8", errors="ignore")
    content = f.read()
    words = read_words(content)
    f.close()
    count_words(words)
