from pygame import *

window = display.set_mode((700,500))
display.set_caption("ping pong game")
background = (70,50,140)
window.fill(background)

clock = time.Clock()
run = True
FPS = 30

class Player():
    def __init__(self, player_x, player_y, color, w, h, inputup, inputdown, speed):
        self.rect = Rect (player_x,player_y,w,h)
        self.speed = speed
        self.color = color
        self.up = inputup
        self.down = inputdown

    def reset (self):
        draw.rect(window, self.color, self.rect)
    def move (self):
        keys = key.get_pressed()
        if keys[self.up]:
            self.rect.y -= self.speed
        if keys[self.down]:
            self.rect.y += self.speed

class Pong():
    def __init__(self, ball_x, ball_y, color, radius, x_speed, y_speed):
        self.x = ball_x
        self.y = ball_y
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
    def reset (self):
        draw.circle(window, self.color, (self.x, self.y), self.radius)
    def update(self):
        self.x -= self.x_speed

def collide(b:Pong, p:Player):
    condition1 = (b.x - b.radius < p.rect.x + p.rect.width)
    condition2 = (b.x + b.radius > p.rect.x)
    condition3 = (b.y + b.radius> p.rect.y)
    condition4 = (b.y - b.radius < p.rect.y + p.rect.height)
    return (condition1 and condition2 and condition3 and condition4)

player1 = Player(670,200, (255,255,255), 10, 100, K_UP, K_DOWN, 15)
player2 = Player(30,200, (255,255,255), 10, 100, K_w, K_s, 15)

pingpong = Pong (350,250,(255,10,2), 20, 10, 2)

while run: 
    for e in event.get(): #event.get gives a list of all event (look at documentation) so it searches through them for pygame.QUIT
        if e.type == QUIT: #if you click "x" then it exits
            run = False #updating window everytime this runs
    window.fill(background)
    pingpong.reset()
    pingpong.update()

    player1.reset()
    player2.reset()
    player1.move()
    player2.move()

    if collide (pingpong, player2):
        print ("collided p2 and ball")
    display.update()
    clock.tick(FPS)