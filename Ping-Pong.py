from pygame import *

init()

#constantes
ancho = 800
alto = 600

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
            finish = True
        if sprite.collide_rect(self,player1) or sprite.collide_rect(self,player2):
            self.speed_x *= -1
        

player1 = Player1("Icon76@2x copy.png", 70,200,20,125,0,15)
player2 = Player2("Icon76@2x copy.png", 700,200,20,125,0,15)
ball = Ball("pokeball.png",350,250,65,65,5,5)


screen = display.set_mode((ancho, alto))
display.set_caption("Ping-Pong")

back = (0, 0, 0)
clock = time.Clock()
FPS = 40
run = True
finish = False
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
    display.update()

pygame.quit()
