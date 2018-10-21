import sys
import re
import io


with io.open(sys.stdin.fileno(), 'r', encoding='latin-1') as sin:
    i = 0
    for line in sin:
        try :
            fields = line.split(";")

            # remove votos que não sejam pra governador
            if "GOVERNADOR" not in fields[12]:
                continue
            # remove votos que não sejam de 2014
            if "2014" not in fields[2]:
                continue
 
            num_cand = fields[13].replace("\"", "")
            qtde_votos = fields[14].replace("\n", "").replace("\"", "")

        except:
            continue

        print(num_cand+","+qtde_votos)

