import pygame
import random
Black = (0,0,0)
Green = (0, 250, 0)
Yellow = (250, 250, 0) 
screen = pygame.display.set_mode((800, 500))
screen.fill(Black)
pygame.display.set_caption('Ping Pong')
direct = random.randint(0,1)
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 20)
score = 0
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
ball = Ball(400, 200)
player = Player(350, 400)
    pygame.display.flip() #DRAW AND UPDATE
    screen.fill(Black)
    pygame.draw.rect(screen, Yellow, pygame.Rect(player.x , player.y, 100, 20))
    pygame.draw.circle(screen, Green, (ball.x, ball.y), 20)
    pygame.draw.rect(screen, (250,0,0), pygame.Rect(0, 480, 800, 500))
    scoretext = font.render("Score: " + str(score) , True, (0,250,250))
    textRect = scoretext.get_rect()
    textRect.center = (50, 20)
    screen.blit(scoretext, textRect)
for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
        pygame.quit()
move = pygame.key.get_pressed()
if move[pygame.K_LEFT]: 
    player.x -= 0.5
    if player.x < 0:
        player.x = 0
elif move[pygame.K_RIGHT]:
    player.x += 0.5
    if player.x > 700:
        player.x = 700
    if direct == 0: # LEFT UP
        ball.x -= 0.4
        ball.y -= 0.4
        if ball.x < 20:
            direct = 1
        if ball.y < 20:
            direct = 3
    if direct == 1: # RIGHT UP
        ball.x += 0.4
        ball.y -= 0.4
        if ball.x > 780:
            direct = 0
        if ball.y < 20:
            direct = 2
    if direct == 2: # RIGHT DOWN
        ball.x += 0.4
        ball.y += 0.4
        if ball.y >= player.y - 20 and ball.y <= player.y + 20 and ball.x >= player.x and ball.x <= player.x + 100:
            direct = 1
            score += 1
        if ball.x > 780:
            direct = 3
    if direct == 3: # LEFT DOWN
        ball.x -= 0.4
        ball.y += 0.4
        if ball.y >= player.y - 20 and ball.y <= player.y + 20 and ball.x >= player.x and ball.x <= player.x + 100:
            direct = 0
            score += 1
        if ball.x < 20:
            direct = 2
        if ball.y >= 480:
            start = False
screen.fill((250,250,250))
font = pygame.font.Font('freesansbold.ttf', 40)
text = font.render("You Lose :))", True, (250,0,0))
textRect = text.get_rect()
textRect.center = (400, 250)
screen.blit(text, textRect)
text = font.render("Score: " + str(score), True, (0,100,250))
textRect = text.get_rect()
textRect.center = (400, 300)
screen.blit(text, textRect)
pygame.display.flip()
pygame.time.delay(6000)
pygame.quit()