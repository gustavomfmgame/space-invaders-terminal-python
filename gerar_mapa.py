from player import jogador
from inimigo import inimigos
from tiros import tiros_inimigos, tiro_jogador

linhas = 20
colunas = 36

mapa = [[' ' for i in range(colunas)]for j in range (linhas)]

for i in range(linhas):
    mapa[i][0] = '#'
    mapa[i][-1] = '#'

for j in range(colunas):
    mapa[0][j] = "#"
    mapa[-1][j] = "#"

def Gerar_mapa():

    coordenadas = [(i.x, i.y) for i in inimigos if i.vivo]

    #gera o mapa com as entidades sem alterar a matriz original
    for i, linhas in enumerate(mapa):
        for j, caracteres in enumerate(linhas):
            if (j, i) in coordenadas:
                print("O", end=' ')
            elif (j, i) == (jogador.x, jogador.y):
                print("P", end=' ')
            elif (j, i) == (tiros_inimigos.x, tiros_inimigos.y):
                print('I', end=' ')
            elif (j, i) == (tiro_jogador.x, tiro_jogador.y):
                print('I', end=' ')
            else:
                print(caracteres, end=' ')
        print()

if __name__=='__main__':
    Gerar_mapa()