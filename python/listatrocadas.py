N = int(input())

lista = input().split(' ')
for j in range(N):  
  lista[j] = int(lista[j])
vetor = len(lista)-1
nos = 0
while vetor > 0:
  for x in lista[:vetor]:  
    if x > lista[vetor]:
      nos += 1
  else:
      vetor -= 1


print(nos)
