import time
import random
import pygame
pygame.init()
size = width, height = 1920, 1080
speed = [1.0, 1.0]
dropdown = [0, 1]
color = 255, 255, 255
sc = 0
# 载入字体
textfont = pygame.font.Font("C:\\WINDOWS\\FONTS\\SIMKAI.TTF", 30)
textsurface = textfont.render("score:", True, (0, 0, 0))
score = textfont = pygame.font.Font("C:\\WINDOWS\\FONTS\\STHUPO.TTF", 40)
scoresurface = score.render("0", True, (0, 0, 0))

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.mouse.set_visible(False)

# 载入图片
# 鼠标上的球
ball = pygame.image.load("ball")

ball1 = pygame.image.load("ball1")

bomb = pygame.image.load("bomb")
bomb1 = pygame.image.load("bomb")
ballrect = ball.get_rect()
ballrect1 = ball1.get_rect()
bombrect = bomb.get_rect()
bombrect.left = random.random() * (width - 50)

bombrect1 = bomb1.get_rect()
bombrect1.left = random.random() * (width - 50)

ballrect.left = random.random() * (width - 111)
ballrect.top = random.random() * (height - 111)

exitbutton = pygame.image.load("exit")
exitrect = exitbutton.get_rect()
exitrect.top = height - 50
exitrect.left = width - 110

# 判断
running = True
iscover = False
bombcover = False
touch_edge = False
ballvisible = True
while running:
    time.sleep(0.001)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            p, q = pygame.mouse.get_pos()
            j1 = p > exitrect.left & p < exitrect.right
            j2 = q > exitrect.top & q < exitrect.bottom
            if p & q:
                running = False

    ballrect = ballrect.move(speed)
    bombrect = bombrect.move(dropdown)
    bombrect1 = bombrect1.move(dropdown)
    if(bombrect.top >= height):
        bombrect.bottom = 0
        bombrect.left = random.random() * (width - 50)
    if(bombrect1.top >= height):
        bombrect1.bottom = 0
        bombrect1.left = random.random() * (width - 50)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        touch_edge = True
        sc = sc - 1
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        touch_edge = True
        sc = sc - 1

    x, y = pygame.mouse.get_pos()
    # 与小球的碰撞
    u = ballrect.left
    v = ballrect.top
    length = ((x - u)**2 + (y - v)**2)**0.5
    m = u - x
    n = v - y
    t = (m**2 + n**2)**0.5
    if touch_edge is False:
        if length <= 111 and iscover is False:
            speed[1] = n / t * 5
            speed[0] = m / t * 5
            iscover = True
            sc = sc + 1
        if length > 111 and iscover is True:
            iscover = False

    else:
        touch_edge = False
    # 与炸弹的碰撞
    a = bombrect.left
    b = bombrect.top
    length1 = ((u - a)**2 + (v - b)**2)**0.5
    c = a - u
    d = b - v
    t1 = (c**2 + d**2)**0.5

    screen.fill(color)
    scoresurface = score.render(str(sc), True, (0, 0, 0))
    if(length1 <= 80.5):
        screen.blit(exitbutton, exitrect)
        speed[0] = 0
        speed[1] = 0
        dropdown[1] = 0
        ballvisible = False

    screen.blit(textsurface, (10, 14))
    screen.blit(scoresurface, (100, 10))
    screen.blit(ball, ballrect)
    if ballvisible:
        screen.blit(ball1, (x, y))
    screen.blit(bomb, bombrect)
    screen.blit(bomb1, bombrect1)
    pygame.display.flip()


pygame.display.quit()
