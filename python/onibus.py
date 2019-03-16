import sys
sys.setrecursionlimit(100000)

class grafo():
  def __init__(self, qntVertices, inicio, fim):
    self.qntVertices = int(qntVertices)
    self.listaAdj = [[] for x in range(int(qntVertices)+1)]
    self.inicio = inicio
    self.anterior = None
    self.fim = fim
  
  def popularLista (self, listaCaminhos):
    for j in listaCaminhos:
      if j != ['']:
        q, g = int(j[0]), int(j[1])
        self.listaAdj[q].append(g)
        self.listaAdj[g].append(q)
 
  def countCaminho (self, vetor):
    if self.fim == self.inicio:
      print(vetor)        
      return True
    for k in (self.listaAdj[self.fim]):
      if k != self.anterior:
        self.anterior, self.fim = self.fim, k
        if (self.countCaminho(vetor + 1)):
          return True
    else:
      return False 
   
a, b, c = input().split(' ')
a, b, c = int(a), int(b), int(c)
lista = []
for x in range (a-1):
  temp = (input().split(' '))
  lista += [temp]

cu = grafo(a, b-1, c-1)
cu.popularLista(lista)
cu.countCaminho(0)

