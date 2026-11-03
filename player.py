import msvcrt
from entidade import Entidade
from tiros import tiro_jogador

jogador = Entidade(x = 17, y = 17, vivo = True, direcao = 0)

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

if __name__=='__main__':
    print()