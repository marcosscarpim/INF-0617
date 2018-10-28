import os
import re
import csv

os.chdir("/tmp/data/gut/")

filenames = []
for file in os.listdir("./txt"):
    if file.endswith(".txt"):
        filenames.append(file)

authors = {}
for filename in filenames:
    fname = filename.replace('u-', '')
    with open('master_list.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if fname == row[4]:
                if row[3] in authors:
                    authors[row[3]].append(filename)
                else:
                    authors[row[3]] = [filename]


for author in authors:
    print(author+','+','.join(authors[author]))
