import pygame, sys


class Game():
    runners = []
    __starLine = 20
    __finishLine = 620 
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #self.__screen.fill((0, 255, 0))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
    
    def competir(self):    #Seguimos con el bucle básico
        gameOver = False    
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
    
    #
            self.__screen.blit(self.__background, (0, 0))  #blit es un método por el cual me coloca una variable en una coordenada, en este caso 0, 0
    
            pygame.display.flip()  #Refresco de pantalla
    #Cierra el círculo con el cierre de los programas
        pygame.quit()
        sys.exit()
    
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()