from entidade import Entidade


tiro_jogador = Entidade(x = -2, y = -2, vivo = False, direcao = -1)

tiros_inimigos = Entidade(x = -1, y = -1, vivo = False, direcao = 1)

def colisao_tiros():
    if (tiro_jogador.x, tiro_jogador.y) == (tiros_inimigos.x, tiros_inimigos.y):
        tiro_jogador.vivo = False
        tiro_jogador.x = 35
        tiros_inimigos.vivo = False

if __name__=='__main__':
    print()
