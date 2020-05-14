import pygame
import sys

class Game():
    
    corredores = []
    
#CONSTRUCTOR    |    creo el fondo, la pantalla y lo ejecuto
    def __init__(self):
        
        self.__screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Carrera de bichos")
        self.background = pygame.image.load("images/background.png")
    
        self.runner = pygame.image.load("images/smallball.png")
    
#EJECUTOR    
    def competir(self):
        
        x = 0
        hayGanador = False 
        #EL BUCLE WHILE VACÍA LOS EVENTOS (INFO DEL JOYSTISK, POR EJEMPLO) QUE SE PRODUZCAN
        while True:
            #comprobación de los eventos
            for event in pygame.event.get():   #event tiene un evento (get), por lo que es un objeto
                if event.type == pygame.QUIT:
                    pygame.quit()  #Salida
                    sys.exit()
                    
                    
    #Refrescar / RENDERIZAR la pantalla           
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip()
        
            x += 3
            if x >= 250:
                hayGanador = True
                
        pygame.quit()
        sys.exit()
#EJECUCIÓN DEL JUEGO    
    
if __name__ == '__main__':
    pygame.init()
    game = Game() 
    
    