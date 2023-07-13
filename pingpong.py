from pygame import *

window = display.set_mode((700,500))
display.set_caption("ping pong game")
background = (70,50,140)
window.fill(background)

clock = time.Clock()
run = True
FPS = 30

class Player():
    def __init__(self, player_x, player_y, color, w, h, speed):
        self.rect = Rect (player_x,player_y,w,h)
        self.speed = speed
        self.color = color

    def reset (self):
        draw.rect(window, self.color, self.rect)

player1 = Player(30,200, (255,255,255), 10, 100, 5)
player2 = Player(670,200, (255,255,255), 10, 100, 5)

while run: 
    for e in event.get(): #event.get gives a list of all event (look at documentation) so it searches through them for pygame.QUIT
        if e.type == QUIT: #if you click "x" then it exits
            run = False #updating window everytime this runs
    player1.reset()
    player2.reset()
    display.update()
    clock.tick(FPS)