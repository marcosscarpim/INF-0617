import sys

num_votos = {}
for line in sys.stdin:
    try:
        num_cand, qtde_votos = line.split(",")
        num_cand = num_cand
        qtde_votos = int(qtde_votos)
    except:
        continue

    if num_cand in num_votos.keys():
        num_votos[num_cand] += qtde_votos
    else:
        num_votos[num_cand] = qtde_votos

for cand in num_votos.keys():
    if cand == "95":
        print("VOTOS BRANCOS = " + str(num_votos[cand]))
    elif cand == "96":
        print("VOTOS NULOS = " + str(num_votos[cand]))
    else:
        print("CANDIDATO = " + cand + ", VOTOS = " + str(num_votos[cand]))

