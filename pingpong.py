from pygame import *

window = display.set_mode((700,500))
display.set_caption("ping pong game")
background = (255,255,255)
window.fill(background)

clock = time.Clock()
run = True
FPS = 30

player1losing = False
player2losing = False

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
    def __init__(self, ball_x, ball_y, radius, speed):
        self.x = ball_x
        self.y = ball_y
        self.radius = radius
        self.color = (0,0,0)
        self.x_speed = speed
        self.y_speed = speed
        self.speed = speed
    def reset (self):
        draw.circle(window, self.color, (self.x, self.y), self.radius)
    def update (self):
        self.x += self.x_speed
        self.y += self.y_speed
    def wallcollide (self):
        if self.y - self.radius == 0:
            self.y_speed = self.speed
        if self.y + self.radius == 500:
            self.y_speed = -self.speed
    def lose (self):
        global player1losing
        global player2losing
        if self.x - self.radius <= 0:
            player1losing = True 
        if self.x + self.radius >= 700:
            player2losing = True 
    def collide(self, p:Player):
        condition1 = (self.x - self.radius < p.rect.x + p.rect.width)
        condition2 = (self.x + self.radius > p.rect.x)
        condition3 = (self.y + self.radius> p.rect.y)
        condition4 = (self.y - self.radius < p.rect.y + p.rect.height)
        return (condition1 and condition2 and condition3 and condition4)

player1 = Player(670,200, (255,0,0), 10, 100, K_UP, K_DOWN, 6)
player2 = Player(30,200, (0,0,255), 10, 100, K_w, K_s, 6)

pingpong = Pong (350,250, 10, 4)

font.init()
font1 = font.SysFont("Arial", 90)
losing1 = font1.render("Player 2 LOST", 3, (0, 0, 255))
losing2 = font1.render("Player 1 LOST", 3, (255, 0, 0))

while run: 
    for e in event.get(): #event.get gives a list of all event (look at documentation) so it searches through them for pygame.QUIT
        if e.type == QUIT: #if you click "x" then it exits
            run = False #updating window everytime this runs
    if player1losing == False and player2losing == False:
        window.fill(background)
        pingpong.lose()
        pingpong.reset()
        pingpong.wallcollide()
        pingpong.update()

        if pingpong.collide (player1):
            pingpong.x_speed = -pingpong.speed
            pingpong.color == (255,0,0)
        if pingpong.collide (player2):
            pingpong.x_speed = pingpong.speed
            pingpong.color == (0,0,255)
        player1.reset()
        player2.reset()
        player1.move()
        player2.move()
    elif player1losing == True:
        window.fill(background)
        pingpong.reset()

        player1.reset()
        player2.reset()

        window.blit(losing1, (60, 200))
    else:
        window.fill(background)
        pingpong.reset()

        player1.reset()
        player2.reset()

        window.blit(losing2, (60, 200))
    display.update()
    clock.tick(FPS)