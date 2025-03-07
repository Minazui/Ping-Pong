from pygame import *

init()

#constantes
ancho = 800
alto = 600
speed_ball_x = 6
speed_ball_y = 6
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, speed_x, speed_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        global screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_s] and self.rect.y < alto - 125:
            self.rect.y += self.speed_y
class Player2(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y < alto - 125:
            self.rect.y += self.speed_y
    
class Ball(GameSprite):
    def update(self):
        global finish
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y >= alto - 65 or self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.x >= ancho - 65 or self.rect.x <= 0:
            #finish = True
            self.speed_x *= -1
        if sprite.collide_rect(self,player1) or sprite.collide_rect(self,player2):
            self.speed_x *= -1
        if sprite.collide_rect(self,enemy):
            self.speed_x *= -1
        elif sprite.collide_rect(self,enemy2) or sprite.collide_rect(self,enemy3):
            self.speed_y *= -1
            


class Enemy(GameSprite):
    #Deriva de el constructor de GameSprite 
    def __init__(self, pos_x, pos_y, size_x, size_y, speed_x, speed_y, color):
        sprite.Sprite.__init__(self)        
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.rect = Rect(pos_x,pos_y,size_x,size_y)
        self.rect.x = pos_x
        self.rect.y = pos_y
        #self.line = Line(pos_x,pos_y,size_x)
        self.color = color

    #Dibuaj en pantalla
    def draw(self, pantalla):
        draw.rect(pantalla, self.color, self.rect)

    #Movimiento de el Enemy
    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y >= alto - 60 or self.rect.y <= 0:
            self.speed_y *= -1
    def update2(self,enemy_p):
        self.rect.y = enemy_p.rect.y
        self.rect.x = enemy_p.rect.x
    def update3(self,enemy_p):
        self.rect.y = enemy_p.rect.y + enemy_p.rect.height
        self.rect.x = enemy_p.rect.x 



#Objetos
player1 = Player1("Icon76@2x copy.png", 70,200,20,125,0,15)
player2 = Player2("Icon76@2x copy.png", 700,200,20,125,0,15)
ball = Ball("pokeball.png",300,250,65,65,speed_ball_x,speed_ball_y)
enemy = Enemy(400,300,30,60,5,5,(255,255,0))
enemy2 = Enemy(400,300,30,5,5,5,(255,0,255))
enemy3 = Enemy(400,360,30,5,5,5,(0,255,255))
screen = display.set_mode((ancho, alto))

#Nombre de la ventana
display.set_caption("Ping-Pong")

back = (0, 0, 0)
clock = time.Clock()
FPS = 40
run = True
finish = False
#Bucle principal
while run:
    clock.tick(FPS)
    for evento in event.get():
        if evento.type == QUIT:
            run = False
    if finish == False:
        screen.fill(back)

        player1.reset()
        player1.update()
        player2.reset()
        player2.update()
        ball.reset()
        ball.update()
        #draw.rect(screen,(255,255,255),(200,200,20,80))
        enemy.draw(screen)
        enemy.update()
        enemy2.draw(screen)
        enemy2.update2(enemy)
        enemy3.draw(screen)
        enemy3.update3(enemy)
    display.update()

quit()
