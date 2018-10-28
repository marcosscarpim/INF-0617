import os
import re
import csv
import sys
import operator

os.chdir("/tmp/data/")


def get_complexity(words, freq_words):
    comp_counter = 0
    unique_words = list(set(words))
    for word in unique_words:
        if word not in freq_words:
            comp_counter += 1

    return comp_counter / len(unique_words)


def read_words(content):
    content = content.lower().replace('\'', '')
    p = re.compile('[0-9]')
    content = p.sub('', content)
    p = re.compile(r'\W+')
    content = p.sub(' ', content)
    p = re.compile(r'\s+')
    words = p.split(content)
    return words


# read words
freq_words = []
f = open('trab4/words.txt', 'r')
lines = f.readlines()
for line in lines:
    freq_words += line

author_complexity = {}
for line in sys.stdin:
    try:
        author_list = line.strip('\n').split(',')
        author = author_list[0]
        words = []
        for filename in author_list[1:]:
            f = open("gut/txt/" + filename, encoding="utf-8", errors="ignore")
            content = f.read()
            test = read_words(content)
            words += read_words(content)
            f.close()

        complexity = get_complexity(words, freq_words)
        author_complexity[author] = complexity
    except Exception as e:
        print("EXCEPTION: " + str(e))
        continue

sorted_result = sorted(author_complexity.items(), key=lambda kv: kv[1], reverse=True)
for author, complexity in sorted_result:
    print(author+","+str(complexity))
