import sys
j, t = input().split()
j, t = int(j), int(t)
sys.setrecursionlimit(100000)
maior = -1

dic = {}
hab = []
times = []
for h in range(t):
  temp = []
  times.append(temp)

for x in range(j):
  novoJ, novaH = input().split()
  novaH = int(novaH)
  dic[int(novaH)] = novoJ
  hab += [novaH]


def qsort(arr): 
  esquerda = []
  direita = []
  if len(arr) <= 1:
    return arr
  else:
    pivo = arr[0]
    for x in arr[1:]:
      if x > pivo:
        esquerda += [x]
      elif x < pivo:
        direita += [x]
    else:
      return (qsort(esquerda)+[pivo]+qsort(direita))

ordenada = qsort(hab)
index = 0

while True:
  i = 0
  if index == len(ordenada):
    break
  while i <= len(times)-1:
    times[i] += [dic[ordenada[index]]]
    index += 1
    i += 1
    if index == len(ordenada):
      break
      


for b, q in enumerate (times):
  q.sort()
  print('Time %d'%(b+1))
  for jj in q:
    print(jj)
  else:
    print('                  ')

  
  
