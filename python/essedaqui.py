numPessoas = int(input())
instante = []
for x in range(numPessoas):
  temp = int(input())
  instante += [temp]

def contar(tempo, atual, i, numPessoas, contador, lista):
  if atual < tempo:
    contador += atual + 10 - tempo
  else:
    contador += 10
  tempo = atual + 10
  if i == (numPessoas-1):
    print(contador)
    return
  else:  
    contar(tempo, lista[i+1], i+1, numPessoas, contador, lista)


contar(0, instante[0], 0, numPessoas, 0, instante)
