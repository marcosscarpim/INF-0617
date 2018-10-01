import os
import time
from multiprocessing import Process

# fix this in your computer
os.chdir("/home/venturus/Documents/Curso - Complex Data/INF-0617/Treino1/gut/gut")
print(os.getcwd())

'''
Count most frequent char in a string

:param content - string to be counted
'''
def count_letters(content):
    # content to lower case, without spaces and line breaks
    content = content.lower().replace(' ', '').replace('\n', '')

    # values to return
    letter = ""
    final_count = 0

    # get all chars in file content
    unique_chars = set(content)

    for char in unique_chars:
        count = content.count(char)
        if count > final_count:
            letter = char
            final_count = count
    return letter, final_count


filenames = []

start_time = time.time()

for file in os.listdir("./txt"):
    if file.endswith(".txt"):
        filenames.append(file)

for filename in filenames:
    f = open("./txt/" + filename, encoding="utf-8", errors="ignore")
    content = f.read()
    f.close()
    letter, count = count_letters(content)
    print(filename, letter)

end_time = time.time()

print("Total time = ", end_time - start_time)