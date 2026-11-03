from entidade import Entidade
from tiros import tiro_jogador, tiros_inimigos
from player import jogador
import random

inimigos = []

for i in range(2, 7, 2):
    if i == 4:
        for j in range(7, 28, 2):
            inimigos.append(Entidade(x=j, y=i, vivo = True, direcao = 1))
    else:
        for j in range(6, 30, 2):
            inimigos.append(Entidade(x=j, y=i, vivo = True, direcao = 1))
 
def mov_inimigo():
    coordenadas = [(i.x, i.y) for i in inimigos if i.vivo]

    #finaliza o jogo caso o jogador seja atingido ou não haja mais inimigos
    if ((tiros_inimigos.x, tiros_inimigos.y) == (jogador.x, jogador.y)) or len(coordenadas) == 0:
        jogador.vivo = False
        return

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
        if i.delay >= 10:
            
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

if __name__=='__main__':
    print()
