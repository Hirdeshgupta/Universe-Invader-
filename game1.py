import pygame
import random
import math
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((800, 600))
# adding caption to the game
pygame.display.set_caption("UNIVERSE INVADER!!")

#adding icon to the game
icon=pygame.image.load('Desktop/rocket.png')
pygame.display.set_icon(icon)

#adding background image
background=pygame.image.load("Desktop/background.png")


# adding font
font=pygame.font.Font("freesansbold.ttf",32)

#function to show score
def show_score(x,y):
    score_value=font.render("SCORE: "+str(score),True,(255,255,255))
    screen.blit(score_value,(x,y))
#adding background sound
mixer.music.load("Desktop/background.wav")
mixer.music.play(-1)
#adding the image of player
player=pygame.image.load("Desktop/player.png")

#adding the image of an enemy
enemy=pygame.image.load("Desktop/enemy.png")

score=0
#adding the image of bullet
bullet=pygame.image.load("Desktop/bullet.png")
bulletX=0
bulletY=470
bulletY_change=15
bullet_state="ready"
playerX=380
playerY=470
playerX_change=0
def player1(x,y):
    screen.blit(player,(x,y))

def enemy1(x,y):
    screen.blit(enemy,(x,y))

def bullet1(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet,(x+16,y+10))
enemyX=random.randint(0,735)
enemyY=random.randint(50,150)
enemyY_change=10
enemyX_change=10

#collision
def iscollision(a,b,c,d):
    distance=math.sqrt(math.pow(a-b,2)+math.pow(c-d,2))
    if distance<=20:
        return True
    else:
        return False

run = True
while run:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change-=10
            if event.key==pygame.K_RIGHT:
                playerX_change+=10
            if event.key==pygame.K_SPACE:
                if bullet_state=="ready":
                    bullet_sound=mixer.Sound("Desktop/laser.wav")
                    bullet_sound.play()
                    bulletX= playerX
                    bullet1(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0








    playerX += playerX_change
    if playerX<0:
        playerX=0
    if playerX>736:
        playerX=736




    if enemyX <= 0:
        enemyX_change+=5
        enemyY+=enemyY_change

    if enemyX >= 736:
        enemyX_change-=5
        enemyY+=enemyY_change

    enemyX += enemyX_change

    if bulletY<=0:
        bulletY=470
        bullet_state="ready"

# persistng the image of bullet
    if bullet_state is "fire":
        bullet1(bulletX,bulletY)
        bulletY-=bulletY_change
    collision=iscollision(bulletX,enemyX,bulletY,enemyY)
    if collision:
        bulletY=470
        bullet_state="ready"
        score+=1
        collision_sound=mixer.Sound("Desktop/explosion.wav")
        collision_sound.play()
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)


    show_score(10,10)
    player1(playerX,playerY)
    enemy1(enemyX,enemyY)




    pygame.display.update()
