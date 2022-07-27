from turtle import back
import pygame
import math

"""
Añadir un boton para alternar entre modo ventana y modo pantalla completa. 
Se debería de cambiar tanto la imagen que es 1080p por otra que sea de menor
resolución como los valores de la resolución (screenWidth y Height) en sí.
"""

#Variables que almacenan la resolución
screenWidth = 1280
screenHeigth = 720

#Variables para almacenar los assets
background = pygame.image.load('img/background1_720.jpg')
alienShip = pygame.image.load('img/alienShip.png')
playerShip = pygame.image.load('img/ship1_vertical.png')
meteor1 = pygame.image.load('img/meteor_01.png')
meteor2 = pygame.image.load('img/meteor_02.png')
meteor3 = pygame.image.load('img/meteor_05.png')

#Titulo de la ventanita
pygame.display.set_caption('Baluza')

#La ventanita, pero
win = pygame.display.set_mode((screenWidth,screenHeigth))

#Esto no se por que lo ha puesto así el coleguita, con while True debería ser
#lo mismo creo, pero no se.
run = True
gameover = False

class Player(object):
    def __init__(self):
        self.img = playerShip
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.x = screenWidth//2
        self.y = screenHeigth//2
        #Controles:
        self.angle = -90 #El angulo de giro inicial de la nave es -90, para que aparezca horizontal (y derecha)
        self.shipRotation = pygame.transform.rotate(self.img, self.angle) #Lo que va a hacer que gire, como parámetros la superficie (imagen) y  el ángulo (angle)
        self.rotatedRect = self.shipRotation.get_rect()
        self.rotatedRect.center = (self.x, self.y) #para que la nave gire con respecto a su centro, definido por x e y (que al final eran height//2)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.width//2, self.y - self.sine * self.height//2) #Esto nos va a decir en que direccion está apuntando la nave, donde está su cara
        
    def drawPlayer(self, win):
        #win.blit(self.img, [self.x, self.y, self.width, self.height])
        win.blit(self.shipRotation, self.rotatedRect)
        
    def turnLeft(self):
        self.angle += 5
        self.shipRotation = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.shipRotation.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.width//2, self.y - self.sine * self.height//2)
    
    def turnRight(self):
        self.angle -= 5
        self.shipRotation = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.shipRotation.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.width//2, self.y - self.sine * self.height//2)
    
    def moveForward(self):
        self.x += self.cosine * 6
        self.y -= self.sine * 6
        self.shipRotation = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.shipRotation.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine + self.width//2, self.y - self.sine * self.height//2)



""" 
Esta funcion pinta la ventana del juego
"""
def redrawGameWindow():
    win.blit(background, (0,0)) #(0,0) > las coordenadas donde se pinta (blit) la imagen
    player.drawPlayer(win) #Pintar al jugador debe ir antes de actualizar la pantalla, si no no se verá
    pygame.display.update() #Esto hay que ponerlo, no se por que pero si no, sin fondo
    
    

player = Player()

clock = pygame.time.Clock()

""" 
Bucle principal del juego
"""

while run:
    clock.tick(60) #juego a 60FPS
    if not gameover:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            player.turnLeft()
        if keys[pygame.K_RIGHT]:
            player.turnRight()
        if keys[pygame.K_UP]:
            player.moveForward()
        pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    redrawGameWindow()
    
    """
    Al abrir el juego podria primero 
    1 - pintar una pantalla con la historia, que sea simplemente una imagen
    2 - empezar la BSO
    3 - pintar un boton que pinte la pantalla ya con la nave y sus muertos
    
    """
    
pygame.quit()
