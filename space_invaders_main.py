import time
import random
import msvcrt

linhas = 20
colunas = 36

inimigos = []

mapa = [[' ' for i in range(colunas)]for j in range (linhas)]

for i in range(linhas):
    mapa[i][0] = '#'
    mapa[i][-1] = '#'

for j in range(colunas):
    mapa[0][j] = "#"
    mapa[-1][j] = "#"

class Entidade():
    
    def __init__(self, vivo, x, y, direcao):

        self.x = x
        self.y = y
        self.vivo = vivo
        self.direcao = direcao
        self.delay = 0

    def mover(self):  
        self.x += self.direcao

    def atirar(self):
        if self.direcao == 1:
            if self.delay>1:
                self.y += self.direcao
                self.delay=0
            self.delay+=1
        else:
            self.y += self.direcao

#gerando os inimigos por meio de laços
for i in range(2, 7, 2):
    if i == 4:
        for j in range(7, 28, 2):
            inimigos.append(Entidade(x=j, y=i, vivo = True, direcao = 1))
    else:
        for j in range(6, 30, 2):
            inimigos.append(Entidade(x=j, y=i, vivo = True, direcao = 1))

jogador = Entidade(x = 17, y = 17, vivo = True, direcao = 0)

#os tiros são objetos da classe Entidade
tiro_jogador = Entidade(x = -2, y = -2, vivo = False, direcao = -1)

tiros_inimigos = Entidade(x = -1, y = -1, vivo = False, direcao = 1)

def mov_inimigo():
    coordenadas = [(i.x, i.y) for i in inimigos if i.vivo]

    #finaliza o jogo caso o jogador seja atingido ou não haja mais inimigos
    if ((tiros_inimigos.x, tiros_inimigos.y) == (jogador.x, jogador.y)) or len(coordenadas) == 0:
        jogador.vivo = False

    #atribui as coordenadas de um inimigo aleatório às coordenadas iniciais do disparo
    if tiros_inimigos.vivo == False:
        (tiros_inimigos.x, tiros_inimigos.y) = random.choice(coordenadas)
        tiros_inimigos.vivo = True

    #mantem o tiro se movendo
    if tiros_inimigos.vivo == True:
        tiros_inimigos.atirar()

    #reseta o tiro
    if tiros_inimigos.y >=18:
        tiros_inimigos.vivo = False

    #elimina os inimigos caso sejam atingidos 
    for i in inimigos:
        if (tiro_jogador.x, tiro_jogador.y) == (i.x, i.y) and i.vivo == True:
            i.vivo = False 
            tiro_jogador.vivo = False
            tiro_jogador.x = -2

    #movimento dos inimigos
    for i in inimigos:
        i.delay+=1
        if i.delay >= 15:
            
            if (34, i.y) in coordenadas and i.vivo:
                for j in inimigos:
                    j.direcao = -1
                    j.y += 1
            elif(1, i.y) in coordenadas and i.vivo:
                for j in inimigos:
                    j.direcao = 1
                    j.y += 1
            i.mover()
            i.delay=0

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

def mov_jogador():
    if msvcrt.kbhit():
        #movimento do jogador
        direcao = msvcrt.getch().decode("utf-8").upper()
        if direcao == 'D' and jogador.x < 34:
            jogador.x += 1
        elif direcao == 'A' and jogador.x > 1:
            jogador.x -= 1

    #disparo
        if direcao == 'F' and tiro_jogador.vivo == False:
            (tiro_jogador.x, tiro_jogador.y) = (jogador.x, jogador.y)
            tiro_jogador.vivo = True
    if tiro_jogador.vivo:
        tiro_jogador.atirar()
    if tiro_jogador.y == -1:
        tiro_jogador.vivo = False

def main():
    mov_inimigo()
    Gerar_mapa()
    mov_jogador()

if __name__ == '__main__':
    while True:
        print("\033[H", end="")
        main()
        time.sleep(0.05)
        if jogador.vivo == False:
            print('FIM DE JOGO FIM DE JOGO FIM DE JOGO FIM DE JOGO FIM DE JOGO ')
            break
