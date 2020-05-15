import turtle
import random

class Race():     #Los corredores y sus atributos
    players = []
    players_colors = ['red', 'green', 'blue', 'orange']
    players_initY = [-30, -10, 10, 30]
    
    def __init__(self, width, height):
        self.players = []
        self.width = width
        self.height = height
        
        self.screen = turtle.Screen()   #Crea la pantalla con el módulo turtle
        self.screen.setup(width, height)  #Establece ancho y alto pantalla
        self.screen.bgcolor('lightgray')    #Color
        
        self.starline = -width / 2 + 20     #POsición de inicio y final de pantalla
        self.finishline = width / 2 - 20
        
        self.__iniPlayers()   #Llamada a jugadores
        
    def __iniPlayers(self):
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.pu()
            new_turtle.color(self.players_colors[i])
            new_turtle.setpos(self.starline, self.players_initY[i] * self.height/200)
            self.players.append(new_turtle)
            
    def competir(self):
        winner = False
        
        while winner == False:
            for i in range(4):
                player = self.players[i]
                advance = random.randint(0,5)
                player.fd(advance)
                xcor = player.xcor()
                if xcor >= self.finishline:
                    winner = True
                    print("The winner is {} turtle". format(player.color()[0]))
                    break

if __name__ == '__main__':  #Definimos si estamos en el módulo principal
    r = Race(640, 480)  #Creamos la carrera
    r.competir()        #Los ponemos a competir
    
    
        
        