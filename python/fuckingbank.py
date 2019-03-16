saque = 22
qntNotas = [5,4,3,10,0,10]
notas = [2,5,10,20,50,100]
key = 5
formas = 0

def troco (nota, qntNota, valor, x):
  global key
  global notas
  global qntNotas
  global formas
  global saque
  if valor < nota or qntNota == 0:
    troco(notas[x-1], qntNotas[x-1], valor, x-1)

  if (valor//nota) <= qntNota:
    valor -=(saque//nota)*nota
    if valor == 0:
      formas += 1
      key -= 1
      if key < 0:
        return (formas)
      else:
        troco(notas[key], qntNotas[key], saque, key)
    else:
      troco(notas[x-1], qntNotas[x-1], valor, x-1)
  else:
    troco(notas[x-1], qntNotas[x-1], valor, x-1)

print (troco(notas[5], qntNotas[5], saque, key))
