from pygame import *
from time import sleep
window = display.set_mode((700, 500))
display.set_caption('Ping-pong')

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_w, player_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class PlayerSprite1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y += - 10
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += 10
class PlayerSprite2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y += - 10
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += 10
class Ball(GameSprite):
    def update(self):
        if self.rect.x > 0 and self.rect.x < 700:
            self.rect.x += speed_x
            self.rect.y += speed_y
speed_y = 2
speed_x = 2
c1 = 0
c2 = 0
player1 = PlayerSprite1('racket.png', 0, 250, 20, 100, 10)
player2 = PlayerSprite2('racket.png', 680, 250, 20, 100, 10)
ball = Ball('ball.png', 350, 250, 40, 40, 1)
background = transform.scale(image.load('black.jpg'),(700,500))

font.init()
font1 = font.SysFont('Arial', 80)
font2 = font.SysFont('Arial', 20)

clock = time.Clock()
FPS = 60

game = True
while game:

    window.blit(background,(0,0))
    ball.reset()
    player1.reset()
    player2.reset()
    ball.update()
    player1.update()
    player2.update()

    text_end1 = font1.render("Player 1 won!", 1, (255,255,255))
    text_end2 = font1.render("Player 2 won!", 1, (255,255,255))
    count1 = font2.render(str(c1), 1, (255,255,255))
    count2 = font2.render(str(c2), 1, (255,255,255))
    if sprite.collide_rect(player1, ball):
        speed_x *= -1
        speed_y *= -1
        c1 += 1
    if sprite.collide_rect(player2, ball):
        speed_x *= -1
        speed_y *= -1
        c2 += 1
    
    if ball.rect.y > 460 or ball.rect.y < 40:
        speed_y *= -1
    if ball.rect.x <= 0:
        window.blit(text_end2, (50, 250))
        sleep(5)
        game = False
    if ball.rect.x >= 700:
        window.blit(text_end1, (50, 250))
        sleep(5)
        game = False
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(count1, (100, 50))
    window.blit(count2, (595, 50))
    display.update()    
    clock.tick(FPS)