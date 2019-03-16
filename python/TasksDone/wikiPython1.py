def piramide (numero):
    if numero != int(numero) or numero < 1:
        return ('número inválido')
    else:
        linha = [(x+1)*(str(x+1)+' ') for x in range (numero)]
        return(linha)
entrada = int(input('Digite um número:'))   
saida = (piramide(entrada))
for x in saida:
    print (x)
