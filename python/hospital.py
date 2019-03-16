class paciente():
  def __init__ (self,nome, tipo, valor):
    self.nome = nome
    self.tipo = tipo
    self.valor = valor

n = int(input())
pacientes = [None]*n
diamante = []
ouro = []
prata = []
bronze = []
resto = []
premium = []

for x in range(n):
  nome, tipo, valor = input().split()
  if tipo == "premium":
    premium += [paciente(nome, tipo, valor)]
  elif tipo == 'diamante':
    diamante += [paciente(nome, tipo, valor)]
  elif tipo == 'ouro':
    ouro += [paciente(nome, tipo, valor)]
  elif tipo == 'prata':
    prata += [paciente(nome, tipo, valor)]
  elif tipo == "bronze":
    bronze +=  [paciente(nome, tipo, valor)]
  elif tipo == 'resto':
    resto += [paciente(nome, tipo, valor)]
    

def quickSort(arr):
  esquerda = []
  direita = []
  if len(arr) <= 1:
    return arr
  else:
    pivor = (arr[0])
    compara = [pivor.nome]
    for x in arr[1:] :
      if x.valor > pivor.valor:
        esquerda.append(x)
      elif x.valor < pivor.valor:
        direita.append(x)
      elif x.valor == pivor.valor:
        compara.append(x.nome)
        compara.sort()     
            
    else:
      return quickSort(esquerda)+compara+quickSort(direita)

diamante = quickSort(diamante)
ouro = quickSort(ouro)
prata = quickSort(prata)
bronze = quickSort(bronze)
resto = quickSort(resto)
premium = quickSort(premium)

for pr in premium:
  try:
    print(pr.nome)
  except:
    print(pr)
for d in diamante:
  try:
    print(d.nome)
  except:
    print(d)
for o in ouro:
  try:
    print(o.nome)
  except:
    print(o)
for p in prata:
  try:
    print(p.nome)
  except:
    print(p)
for b in bronze:
  try:
    print(b.nome)
  except:
    print(b)
for r in resto:
  try:
    print(r.nome)
  except:
    print(r)




