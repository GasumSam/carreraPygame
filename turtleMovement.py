import pygame, sys
from pygame.locals import*

class Runner():  # situamos un corredor
    __customes = ('turtle', 'snakes', 'tiger', 'zebra', 'parrot')
    
    
    def __init__(self, x=0, y=0, custome = None): #Informamos que lo coloque en una posición
        ixCustome = random.randint(0, 4)   #genera un valor a azar entre 0 y 4
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))  #Cargamos una imagen para el corredor
        self.position = [x, y]  #Si esto está como tupla no podrá cambiar de posición el corredor
        self.name = ""
        
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #self.__screen.fill((0, 255, 0))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner = Runner(320, 240)
        
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.key == KEYDOWN:
                    if event.key == K_UP:
                        # Mover hacia arriba runner
                        
                        '''
                        runnerY = self.runner.position[1]  #Extraigo la posición del corredor
                        runnerY += 1                        #Le sumo uno
                        self.runner.position[1] = runnerY   #Vuelvo a situar la posición del corredor
                        
                        self.runner.position[1] = self.runner.position[1] + 1  #Esto es lo mismo
                        '''
                        self.runner.position[1] -= 5  #Esto es lo mismo más sencillo (en esta caso 5 para que avance más)
                                                
                    elif event.key == K_DOWN:
                        # Mover hacia abajo runner
                        self.runner.position[1] += 5  #La Y en la pantalla va al revés, cuando bajas tienes que sumar. O O está arriba
                    elif event.key == K_LEFT:
                        # Mover hacia la izquierda
                        self.runner.position[1] -= 5
                    elif event.key == K_RIGHT:
                        # Mover hacia la derecha
                        self.runner.position[1] += 5
                    else:
                        pass
                    
            self.__screen.blit(self.__background, (0, 0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            pygame.display.flip()
            
print("my name is{}".format(__name__))
            
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game start()