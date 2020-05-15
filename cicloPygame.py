import pygame, sys
#Programa que nos habra pygame

width = 640
height = 480

#Creamos una ventana con anchura y altura determinada
screen = pygame.display.set_mode((width, height))
screen.fill((246, 147, 48))
pygame.display.set_caption("Ciclo básico de pygame")  #Título de pantalla

pygame.font.init()   #Dependiendo de tu sistema puede funcionar pygame.init()

#Creamos una condición

gameOver = False
while not gameOver:
    for event in pygame.event.get():#cogemos cada uno de los eventos para procesarlos
        if event.type == pygame.QUIT:  #Salida del bucle
            gameOver = True

    pygame.display.flip()  #Refresca la imagen  |  #Puede valer update

pygame.quit()  #Cierra Pygame
sys.exit()  #Cierra el sistema y el objeto

#Se trata de un ciclo en el que constantemente se produce un evento y se refresca la pantalla