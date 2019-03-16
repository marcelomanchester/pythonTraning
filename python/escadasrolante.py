for x in range(numPessoas):
  novo = int(input())
  if novo < temp:
    contador += novo + 10 - temp
  else:
    contador += 10
  temp = novo + 10
else:
  print(contador)
