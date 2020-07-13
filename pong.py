import pygame
import os

os.environ["SDL_VIDEO_CENTERED"] = "!"
pygame.init()

class Paddle(object):
    def __init__(self, xpos, ypos, width, height, color, surface):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface
        
        self.yvel = 6
    def draw(self):
        pygame.draw.rect(self.surface, (self.color), (self.xpos, self.ypos, self.width, self.height))
    def rect(self):
        return pygame.Rect(self.xpos, self.ypos, self.width, self.height)
    def move(self, velocity):
        self.ypos += velocity

class Ball(object):
    def __init__(self, xpos, ypos, width, height, color, surface):
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface

        self.xvel = 6
        self.yvel = 6
        self.turn = 0
    def draw(self):
        pygame.draw.rect(self.surface, (self.color), (self.xpos, self.ypos, self.width, self.height))

    def rect(self):
        return pygame.Rect(self.xpos, self.ypos, self.width, self.height)
    
    def move(self):
        self.xpos += self.xvel
        self.ypos += self.yvel

        if self.xpos > WIDTH-self.width:
            self.xvel *= -1

        if self.xpos < 0:
            self.xvel *= -1

        if self.ypos < 0:
            self.yvel *= -1

        if self.ypos > HEIGHT-self.height:
            self.yvel *= -1

        if ball.rect().colliderect(lpaddle.rect()):
            if self.turn == 2:
                self.turn = 0
                self.xvel += int(self.xvel * 0.2)
                self.yvel += int(self.yvel * 0.2)
            self.turn += 1
            self.xvel *= -1
            print(self.xvel)

        if ball.rect().colliderect(rpaddle.rect()):
            self.xvel *= -1

black = (0,0,0)
white = (255,255,255)

WIDTH = 1000
HEIGHT = 600
TITLE = "Pong by @potatochip"
FPS = 60
clock = pygame.time.Clock()

width = 10
height = 100

bwidth = 20
bheight = 20

yvel = 6

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# Objects
lpaddle = Paddle(0, int(HEIGHT/2-height/2), width, height, white ,win)
rpaddle = Paddle(WIDTH-width, int(HEIGHT/2-height/2), width, height, white, win)
ball = Ball(int(WIDTH/2-bwidth/2), int(HEIGHT/2-bheight/2), bwidth, bheight, white, win)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and not lpaddle.ypos < 0:
        lpaddle.move(yvel*-1)
    if keys[pygame.K_s] and not lpaddle.ypos > HEIGHT-height:
        lpaddle.move(yvel)

    rpaddle.ypos = int(ball.ypos-bheight/2)

    ball.move()
        
    win.fill(black)
    pygame.draw.aaline(win, (white), (WIDTH/2, 0), (WIDTH/2, HEIGHT))

    lpaddle.draw()
    rpaddle.draw()
    ball.draw()
    
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()




