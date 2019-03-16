N = int(input())

lista = input().split(' ')
for j in range(N):
  lista[j] = int(lista[j])
vetor = len(lista)-1
nos = 0
def qsort(arr):
  global nos
  esquerda = []
  direita = []
  if len(arr) <= 1:
    return arr
  else:
    pivo = arr[len(arr)-1]
    for x in arr[:len(arr)-1]:
      if x > pivo:
        nos += 1
        esquerda += [x]
      elif x < pivo:
        direita += [x]
    else:
      return (qsort(arr[:len(arr)-1]))
qsort(lista)

print(nos)
    
