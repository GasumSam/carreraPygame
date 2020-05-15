import pygame, sys
import random

class Runner():  # situamos un corredor
    _customes = ('turtle', 'snakes', 'tiger', 'zebra', 'parrot')
    
    
    
    def __init__(self, x=0, y=0, custome = 'turtle'): #Informamos que lo coloque en una posición
        self.custome = pygame.image.load("images/{}.png".format(custome))  #Cargamos una imagen para el corredor
        self.position = [x, y]  #Si esto está como tupla no podrá cambiar de posición el corredor
        self.name = custome 

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
            import pygame, sys
import random

class Runner():  # situamos un corredor
    _customes = ('turtle', 'snakes', 'tiger', 'zebra', 'parrot')
    
    
    
    def __init__(self, x=0, y=0, custome = 'turtle'): #Informamos que lo coloque en una posición
        self.custome = pygame.image.load("images/{}.png".format(custome))  #Cargamos una imagen para el corredor
        self.position = [x, y]  #Si esto está como tupla no podrá cambiar de posición el corredor
        self.name = custome 

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
            