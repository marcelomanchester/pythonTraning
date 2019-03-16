import sys
sys.setrecursionlimit(100000)

def popularLista (lista, N):
  temp = [[] for x in range(N+10)]
  for x in lista:
    if x == ['']:
      continue
    else:
      q, g = int(x[0]), int(x[1])
      temp[q].append(g)
      temp[g].append(q)
  else:
    return temp


def countCaminho (lista, agora, antes, chegada, incremento):
  if agora == chegada:
    print(incremento)
    return 
  for x in lista[agora]:
    if x == antes:
      continue
    else:
      (countCaminho(lista, x, agora, chegada, incremento+1))


a, b, c = input().split(' ')
a, b, c = int(a), int(b), int(c)
lista = []
for x in range (a-1):
  temp = (input().split(' '))
  lista += [temp]
incremento = 0
grafo = popularLista(lista, a)
countCaminho(grafo, c, None, b, 0)

