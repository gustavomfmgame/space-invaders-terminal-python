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


if __name__=='__main__':
    print()