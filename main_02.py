import pygame, sys
import random

class Runner():  # situamos un corredor
    __customes = ('turtle', 'snakes', 'tiger', 'zebra', 'parrot')
    
    
    
    def __init__(self, x=0, y=0, custome = None): #Informamos que lo coloque en una posición
        ixCustome = random.randint(0, 4)   #genera un valor a azar entre 0 y 4
        
        self.custome = pygame.image.load("images/{}.png".format(self.__customes[ixCustome]))  #Cargamos una imagen para el corredor
        self.position = [x, y]  #Si esto está como tupla no podrá cambiar de posición el corredor
        self.name = ""

    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    runners = []
    __posY = (160, 200, 240, 280) #Posiciones de línea de salida
    __names = ("Speedy", "Lucera", "Alonso", "Torcuata")
    __starLine = -5
    __finishLine = 620 
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #self.__screen.fill((0, 255, 0))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
    #Inscripción del corredor en el circuito 
        for i in range (4):   #Creamos a los 4 corredores
            theRunner = Runner(self.__starLine, self.__posY[i])  #Cargará un runner en la posición determinada (con los atributos de Runner)
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)  #El corredor se crea en cada ciclo y lo vamos añadiendo
    
    
    def close(self):        #CUANDO SE PRODUCE UN GANADOR TERMINA EL BUCLE
        pygame.quit()
        sys.exit()
    
    def competir(self):    #Seguimos con el bucle básico
        gameOver = False        #gestión de evento
        while not gameOver:   #COMPROBAR EVENTO
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
                                #ACTUALIZA TODO
            for activeRunner in self.runners:  #ITERA para cada active Runner en la lista self Runer
                activeRunner.avanzar()  #Al corredor le pido avanzar
                if activeRunner.position[0] >=  self.__finishLine:
                    print("{} ha ganado".format(activeRunner.name))
                    gameOver = True 
                            #REFRESCA PANTALLA
            self.__screen.blit(self.__background, (0, 0))
            
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
    
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()
            
    ''' 
    
    
            if self.runners[0].position[0] >= self.__finishLine:
                print("{} ha ganado".format(self.runners[0].name))
                gameOver = True 
    
            self.__screen.blit(self.__background, (0, 0))  #blit es un método por el cual me coloca una variable en una coordenada, en este caso 0, 0
    #game tiene una atributo que se llama lista de corredores
            
            #En su posición = está first runner, el que tiene como atributos custome y position


            
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)#Coge al corredor primero con su atuendo, colócalo en la posición que tenga
                            #(arriba) no sé donde está, lo muevo donde esté.
           
            self.__screen.blit(self.runners[0].custome, self.runners[0].position)
            self.__screen.blit(self.runners[1].custome, self.runners[1].position)
            self.__screen.blit(self.runners[2].custome, self.runners[2].position)
            self.__screen.blit(self.runners[3].custome, self.runners[3].position)
       
    #Cuando haces un for in haces un elemento uno a uno en el orden de la memoria del ordenador
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
    #Puedo iterar con un for ix in range
    
    
    
            pygame.display.flip()  #Refresco de pantalla
    #Cierra el círculo con el cierre de los programas
        pygame.quit()
        sys.exit()
    
    '''
    
if __name__ == '__main__':
    game = Game()
    pygame.font.init()
    game.competir()
    
    
    