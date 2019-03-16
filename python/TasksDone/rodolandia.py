
def novaCelula (linha, coluna):
    global arena
    global posicaoAtual
    global figurinhasColetadas
    if arena[linha][coluna] == '*':
        figurinhasColetadas += 1
        posicaoAtual = (linha, coluna)
        arena[linha][coluna] = '.'
    elif arena[linha][coluna] != '#':
        posicaoAtual = (linha, coluna)

def andar(orientacao, posicao):
    global listaDimencoes
    linha = int(posicao[0])
    coluna = int(posicao[1])
    if orientacao == 'N':
        if (linha-1) >= 0:
            novaCelula(linha-1, coluna)
    elif orientacao == 'S':
        if (linha + 1) < int(listaDimencoes[0]):
            novaCelula(linha+1 , coluna)
    elif orientacao == 'O':
        if (coluna -1) >= 0:
            novaCelula(linha, coluna-1)
    elif orientacao == 'L':
        if (coluna + 1) < int(listaDimencoes[1]):
            novaCelula(linha, coluna + 1)                   


def girarEsquerda(orientacao):
    global orientacaoAtual
    if orientacao == 'N':
        orientacaoAtual = 'O'
    elif orientacao == 'O':
        orientacaoAtual = 'S'
    elif orientacao == 'L':
        orientacaoAtual = 'N'
    elif orientacao == 'S':
        orientacaoAtual = 'L'            


def girarDireita(orientacao):
    global orientacaoAtual
    if orientacao == 'N':
        orientacaoAtual = 'L'
    elif orientacao == 'O':
        orientacaoAtual = 'N'
    elif orientacao == 'L':
        orientacaoAtual = 'S'
    elif orientacao == 'S':
        orientacaoAtual = 'O'                

def lerComandos (comando):
    global posicaoAtual
    global orientacaoAtual
    global figurinhasColetadas
    global arena
    global listaDimencoes
    for fatia in range(len(comando)):
        if comando[fatia] == 'D':
            (girarDireita(orientacaoAtual))
        elif comando[fatia] == 'E':
            (girarEsquerda(orientacaoAtual))
        elif comando[fatia] == 'F':
            (andar(orientacaoAtual, posicaoAtual))        
    else:
        return figurinhasColetadas

def criarMatriz (N, M):
    global arena
    global posicaoAtual
    global orientacaoAtual
    #ESTRUTURAÇÃO DA MATRIZ          
    for linha in range (int(N)):
        listaTemp = []
        novaLinha = input('')
        listaTemp = (list(novaLinha))
        if 'N' in novaLinha:
            orientacaoAtual = 'N'
            posicaoAtual = (len(arena), novaLinha.find('N'))
        elif 'L' in novaLinha:
            orientacaoAtual = 'L'
            posicaoAtual = (len(arena), novaLinha.find('L'))
        elif 'O' in novaLinha:
            orientacaoAtual = 'O'
            posicaoAtual = (len(arena), novaLinha.find('O'))
        elif 'S' in novaLinha:
            orientacaoAtual = 'S'
            posicaoAtual = (len(arena), novaLinha.find('S'))
        arena += [listaTemp]

while True:
    arena = []
    listaDimencoes = []
    figurinhasColetadas = 0
    posicaoAtual = None
    orientacaoAtual = None
    dimencoes = input('')
    if dimencoes == '0 0 0':
        break
    else:    
        listaDimencoes = dimencoes.split(' ')
        numeroComandos = int(listaDimencoes[2])
        criarMatriz(listaDimencoes[0], listaDimencoes[1])
        comando = input('')
        if len(comando) == numeroComandos:
            print(lerComandos(comando))
        else:
            print ('número de comandos excede quantidade determinada.')
