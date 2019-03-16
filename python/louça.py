class node():
    def __init__(self, dado):
        self.__dado = dado
        self.__anterior = None
        self.__proximo = None

    def getDado(self):
        return self.__dado

    def setDado(self, novoDado):
        self.__dado = novoDado

    def getAnterior(self):
        return self.__anterior

    def setAnterior(self, novoValor):
        self.__anterior = novoValor

    def getProx(self):
        return self.__proximo

    def setProx(self, novoValor):
        self.__proximo = novoValor


class LDE():
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def getInicio(self):
        return self.__inicio

    def getFim(self):
        return self.__fim

    def empty(self):
        return self.__inicio is None

    def __str__(self):
        if self.empty():
            return "[]"
        else:
            currentNode = self.__inicio
            string = "["
            while currentNode is not None:
                string += str(currentNode.getDado()) + ","
                currentNode = currentNode.getProx()
            return string[:-1] + "]"

    def insertAtBegin(self, dado):
        novoNo = node(dado)
        if self.empty():
            self.__inicio = novoNo
            self.__fim = novoNo
        else:
            novoNo.setProx(self.__inicio)
            self.__inicio = novoNo

    def insertEnd(self, dado):
        novoNo = node(dado)
        if self.empty():
            self.__inicio = novoNo
            self.__fim = novoNo
        else:
            self.__fim.setProx(novoNo)
            self.__fim = novoNo

    def removeBegin(self):
        if self.empty():
            IndexError
        else:
            firstNode = self.__inicio.getDado()
            if self.__inicio == self.__fim:
                self.__inicio = self.__fim = None
            else:
                self.__inicio = self.__inicio.getProx()
            return firstNode

    def removeEnd(self):
        if self.empty():
            IndexError
        else:
            lastNode = self.__fim.getDado()
            if self.__inicio == self.__fim:
                self.__inicio = self.__fim = None
            else:
                currentNode = self.__inicio
                while currentNode.getProx() != self.__fim:
                    currentNode = currentNode.getProx()
                currentNode.setProx(None)
                self.__fim = currentNode
            return lastNode

    def search(self, dado):
        currentNode = self.__inicio
        anterior = None
        while currentNode != None:
            if currentNode.getDado() == dado:
                return dado
            anterior = currentNode
            currentNode = currentNode.getProx()
        return currentNode
    def searchForRemove(self,dado):
      currentNode = self.__inicio
      anterior = None
      while currentNode != None:
        if currentNode.getDado() == dado:
          return (currentNode,anterior)
        anterior = currentNode
        currentNode = currentNode.getProx()
      return (currentNode,anterior)
    def remove(self,dado):
      node,anterior = self.searchForRemove(dado)
      if node != None:
        if anterior != None:
          anterior.setProx(node.getProx())
        else:
          self.__inicio = node.getProx()
numFestas = int(input())
contador = 0
for x in range (numFestas):
  listaMaos = []
  vencedor = None
  mesa = input().split(' ')
  listaMesa = LDE()
  for j in mesa:
    listaMesa.insertEnd(j)
  mao = input().split(' ')
  while mao[0] != '-1':
    temp = LDE()
    for k in mao:
      temp.insertEnd(k)
    listaMaos += [temp]
    mao = input().split(' ')
  while True:
    if vencedor != None:
      print(vencedor)
      break
    contador += 1
    if contador == 1000:
      print(0)
      break
    cartaAtual = listaMesa.removeBegin()
    for jog in (listaMaos):
      compara = jog.removeBegin()
      if cartaAtual != compara:
        jog.insertEnd(compara)
      if jog.empty():
        vencedor = listaMaos.index(jog)+1
        break        
    else:
      listaMesa.insertEnd(cartaAtual)
    
