# INF-617: Trabalho 1
# Alunos: Liselene Borges e Marcos Scarpim
# Implementação paralela
import os
import time
import multiprocessing
from multiprocessing import Process

num_cpu = multiprocessing.cpu_count()
print("Numero de processadores: ",num_cpu)

# fix this in your computer
os.chdir("/home/liselene/Projects/ComplexData/INF-0617/aula2/gut/")
print("Currente directory: "+os.getcwd())

'''
Count most frequent char in a string

:param content - string to be counted
'''
def count_letters(filename, content):
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
    
    print(filename,letter)

filenames = []

start_time = time.time()

for file in os.listdir("./txt"):
    if file.endswith(".txt"):
        filenames.append(file)


processes = []
count = 0
for filename in filenames:
    f = open("./txt/" + filename, encoding="utf-8", errors="ignore")
    content = f.read()
    f.close()
    
    p = Process(target=count_letters, args=(filename,content,))
    processes.append(p)
    p.start()
    count = count+1

    if(count>num_cpu):
        count = 0
        for p in processes :
            p.join()

for p in processes :
    p.join()  
    
end_time = time.time()
print("Total time = ", end_time - start_time)

print("NOTAS:")
print(" 1 - Foi escolhido fazer em paralelo somente a contagem da letras, uma vez que o acesso ao arquivo não iria ter muito ganho na paralelização pois o meio de acesso é único.")
print(" 2 - Foi feita paralelização de até o número máximo de cpus da máquina")
