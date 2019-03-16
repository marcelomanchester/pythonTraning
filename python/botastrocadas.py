N = int(input())
dic = {}

for j in range (31):
  dic[j] = []

for x in range(N):
  temp = input().split(' ')
  tamanho = temp[0]
  lado = temp[1]
  dic[int(tamanho)-30] += [lado]
  
pares = 0

for p in range (31):
  if (dic[p].count('E')) >= (dic[p].count('D')):
      pares += dic[p].count('D')
  else:
      pares += dic[p].count('E')

print(pares)

