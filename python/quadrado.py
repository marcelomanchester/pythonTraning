import time
t1 = time.time()
N = int(input())
quadrado = []
somasColunas = [0]*N
for index in range (N):
    listaTemp = []
    novaLinha = (input('')).split(' ')
    for j in range (N):
        novaLinha[j]= int(novaLinha[j])
        somasColunas[j] += novaLinha[j]
    else:    
        quadrado += [novaLinha]

somaCerta = None

for i,x in enumerate (quadrado):
    if somasColunas.count(sum(x)) == 1:
        linha = i
        coluna = somasColunas.index(sum(x))
        somaErrada = somasColunas[coluna]
    else:
        somaCerta = sum(x)

diferenca = somaErrada - somaCerta
print(str(quadrado[linha][coluna] - (diferenca))+ " " +str(quadrado[linha][coluna]))
t2 = time.time()
print(t2 - t1)

















