import os
import time
from player import mov_jogador
from gerar_mapa import Gerar_mapa
from inimigo import mov_inimigo
from player import jogador

def main():
    mov_inimigo()
    fim()
    Gerar_mapa()
    colisao_tiros()
    mov_jogador()

if __name__ == '__main__':
    while True:
        os.system('cls')
        main()
        time.sleep(0.05)
        if jogador.vivo == False:
            print('FIM DE JOGO FIM DE JOGO FIM DE JOGO FIM DE JOGO FIM DE JOGO ')
            break
