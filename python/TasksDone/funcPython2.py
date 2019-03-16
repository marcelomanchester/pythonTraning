def piramide (number):
    lista =[]
    incremento = 1
    string = ''
    if number != int(number) or number < 1:
        return 'número inválido'
    else:
        for x in range(number):
            string += str(x+1)+' '
            lista.append(string)
        else:
            return (lista)

entrada = int(input('Digite um número: '))
saida = piramide(entrada)
if saida == str(saida):
    print(saida) #DESNECESSÁRIO USAR TRY 
else:
    for x in saida:
        print (x)    
