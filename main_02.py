import pygame, sys
import random

class Runner():  # situamos un corredor
    def __init__(self, x=0, y=0): #Informamos que lo coloque en una posición
        self.custome = pygame.image.load("images/turtle.png")  #Cargamos una imagen para el corredor
        self.position = [x, y]  #Si esto está como tupla no podrá cambiar de posición el corredor
        self.name = "Tortuga"

    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    runners = []
    __starLine = -5
    __finishLine = 620 
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #self.__screen.fill((0, 255, 0))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
    #Inscripción del corredor en el circuito 
        firstRunner = Runner(self.__starLine, 0) #Cargará un runner en la posición 0,0 (con los atributos de Runner)
        firstRunner.name = "Speedy"
        self.runners.append(firstRunner)
    
    
    def competir(self):    #Seguimos con el bucle básico
        gameOver = False        #gestión de evento
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
    
            self.runners[0].avanzar()  #Al corredor 0 le pido que avance
    
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado".format(self.runners[0].name))
                gameOver = True 
    
    
            self.__screen.blit(self.__background, (0, 0))  #blit es un método por el cual me coloca una variable en una coordenada, en este caso 0, 0
    #game tiene una atributo que se llama lista de corredores
            #En su posición = está first runner, el que tiene como atributos custome y position
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)#Coge al corredor primero con su atuendo, colócalo en la posición que tenga
                            #(arriba) no sé donde está, lo muevo donde esté.
    
            pygame.display.flip()  #Refresco de pantalla
    #Cierra el círculo con el cierre de los programas
        pygame.quit()
        sys.exit()
    
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()