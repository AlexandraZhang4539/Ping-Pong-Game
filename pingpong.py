from pygame import *

window = display.set_mode((700,500))
display.set_caption("ping pong game")
background = (0,0,0)
window.fill(background)

clock = time.Clock()
run = True
FPS = 30

while run: 
    for e in event.get(): #event.get gives a list of all event (look at documentation) so it searches through them for pygame.QUIT
        if e.type == QUIT: #if you click "x" then it exits
            run = False #updating window everytime this runs

    display.update()
    clock.tick(FPS)