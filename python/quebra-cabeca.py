N = int(input(''))
if N <= 2 or N >= 1000:
    pecas = (input(''))
    listaPecas =  pecas.split(' ')
    sumPecas = int(((1 + N)*N)/2)
    for x in (listaPecas):
        sumPecas -= int(x)
    print(sumPecas)
else:
    print('numero de peças inválido')
      
