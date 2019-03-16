class node ():
  def __init__(self, dado):
    self.dado = dado
    self.esquerdo = None
    self.direito = None
    self.pai = None
  
  def setDado(self, dado):
    self.dado = dado
  
  def setDir(self, filho):
    self.direito = filho
    
  def setEsq(self, filho):      
    self.esquerdo = filho
    
  
  def setPai(self, pai):
    self.pai = pai

class tree():
  def __init__(self):
    self.raiz = None
  
  def setRaiz(self, raiz):
    self.raiz = raiz
  
  def getRaiz(self):
    return self.raiz
  
  def IsEmpty(self):
    if self.raiz == None:
      return True
    else:
      return False
  
  def search(self, busca, atual):
    if atual == None or atual.dado == busca:
      return atual
    if atual.dado < busca:
      return (self.search(busca, atual.direito))
    else:
      return(self.search(busca, atual.esquerdo))
  
  def maximo(self, no):
    while no.direito != None:
      no = no.direito
    return no

  def minimo(self, no):
    while no.esquerdo != None:
      no = no.esquerdo
    return no

  def inserir(self, no):
    global lista
    newNode = node(no)
    y = None
    x = self.getRaiz()
    while x != None:
      y = x
      if newNode.dado < x.dado:
        x = x.esquerdo
      else:
        x = x.direito
    newNode.setPai(y)
    if y == None:
      self.setRaiz(newNode)
    else:
      if newNode.dado < y.dado:
        y.setEsq(newNode)
      else:
        y.setDir(newNode)
    lista.append(newNode)  

  def sucessor(self, no):
    if no.direito != None:
      return self.minimo(no.direito)
    else:
      temp = no.pai
      while temp != None and no == temp.direito:
        no = temp
        temp = temp.pai
      return temp  

  def antecessor(self, no):
    if no.esquerdo is not None:
      return self.minimo(no.esquerdo)
    else:
      temp = no.pai
      while temp is not None and no == temp.esquerdo:
        no = temp
        temp = temp.pai
      return temp
  
  def remover(self, x):
    if x.esquerdo == None or x.direito == None:
      y = x
    else:
      y = self.sucessor(x)
    if y.esquerdo != None:
      z = y.esquerdo
    else:
      z = y.direito
    if z != None:
      z.setPai(y.pai)
    if y.pai == None:
      self.setRaiz(z)
    else:
      if y == y.pai.esquerdo:
        y.pai.setEsq(z)
      else:
        y.pai.setDir(z)
    if x != y:
      x.setDado(y.dado)

  def inOrdem(self, node):
    global inOrdemStr
    if node != None:
      self.inOrdem(node.esquerdo)
      inOrdemStr += str((node.dado))
      self.inOrdem(node.direito)
  def posOrdem(self, node):
    global posOrdemStr
    if node != None:
      self.posOrdem(node.esquerdo)
      self.posOrdem(node.direito)
      posOrdemStr += str((node.dado))
  def preOrdem(self, node):
    global preOrdemStr
    if node != None:
      preOrdemStr += str(node.dado)
      self.preOrdem(node.esquerdo)
      self.preOrdem(node.direito)
           
           
lista = []
b = 1
while True:
  try:
    arvore = tree()
    N = int(input())
    print('Caso '+str(b)+':')
    b += 1
    for x in range(N):
      temp = input()
      if temp[0] == 'A':
        arvore.inserir(int(temp[2]))
      elif temp[0] == 'B':
        procura = arvore.search(int(temp[2]), arvore.raiz)
        arvore.remover(procura)
      elif temp[0] == "C":
        procura = arvore.search(int(temp[2]), arvore.raiz)
        if procura != None:
          menor = arvore.antecessor(procura)
          print(menor.dado)
        else:
          print(0)
      elif temp == 'IN':
        if (arvore.IsEmpty()):
          print(0)
        else:
          inOrdemStr = ''
          arvore.inOrdem(arvore.raiz)
          print(inOrdemStr)
      elif temp == "PRE":
        if (arvore.IsEmpty()):
          print(0)
        else:  
          preOrdemStr = ''
          arvore.preOrdem(arvore.raiz)
          print(preOrdemStr)
      elif temp == "POST":
        if (arvore.IsEmpty()):
          print(0)
        else: 
          posOrdemStr = ''
          (arvore.posOrdem(arvore.raiz))
          print(posOrdemStr)
  except EOFError:
    break    

