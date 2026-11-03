from tiros import tiros_inimigos
from player import jogador
from inimigo import inimigos

coordenadas = [(i.x, i.y) for i in inimigos if i.vivo]

def fim():
    if ((tiros_inimigos.x, tiros_inimigos.y) == (jogador.x, jogador.y)) or len(coordenadas) == 0:
        jogador.vivo = False

    for i in inimigos:
        if i.y > 17:
            jogador.vivo = False
