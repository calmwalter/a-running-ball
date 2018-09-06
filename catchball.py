import time
import random
import pygame
# 初始化pygame
pygame.init()
# 随机生成颜色
color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
# 初始化屏幕大小
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# ------------
# 游戏开始选择字体
welcome_font = pygame.font.Font("C:\\WINDOWS\\FONTS\\SIMKAI.TTF", 80)
welcome_font_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
welcome_content = welcome_font.render(
    "WELCOME!", True, welcome_font_color)
welcome_pos = (width / 2 - 100, height / 2 - 300)
# ------------
# 游戏结束选择字体
end_font = pygame.font.Font("C:\\WINDOWS\\FONTS\\SIMKAI.TTF", 80)
end_font_color = (random.randint(0, 255), random.randint(
    0, 255), random.randint(0, 255))
end_content = welcome_font.render(
    "GAME ENDED!", True, end_font_color)
end_pos = (width / 2 - 100, height / 2 - 300)
# ------------
# 游戏底部栏杆
strike = pygame.image.load("strike")
strikerect = strike.get_rect()
strikerect.left = width / 2 - 200
strikerect.bottom = height - 10

# ------------
# 游戏球体
ball = pygame.image.load("ball")
ballrect = ball.get_rect()
speed = [5, 5]
ballrect.left = random.randint(0, width)
ballrect.top = random.randint(0, height - 400)
# ------------
# 游戏开始按钮
start = pygame.image.load("start")
startrect = start.get_rect()
startrect.left = width / 2 - 500
startrect.top = height / 2 + 400
# ------------
# 游戏结束按钮
exitgame = pygame.image.load("exit")
exitrect = exitgame.get_rect()
exitrect.left = width / 2 + 500
exitrect.top = height / 2 + 400
# ------------
# 游戏重新开始按钮
restart = pygame.image.load("restart")
restartrect = restart.get_rect()
restartrect.left = width / 2 - 500
restartrect.top = height / 2 + 400
# ------------
running = True
first_in_game = True
# 运行函数


def gameend():
    """Lanuch while game is at an end."""
    global running
    running = False


def ballbehavior():
    """Handle the ball behavior."""
    global ballrect, strikerect, speed
    if ballrect.top <= 0:
        speed[1] = -speed[1]
    if ballrect.left <= 0 or ballrect.right >= width:
        speed[0] = -speed[0]

    if ballrect.bottom >= strikerect.top:
        print(ballrect.left + 55.5)
        print(strikerect.left)
        print(strikerect.right)
        if ballrect.left + 55.5 >= strikerect.left \
                and ballrect.left + 55.5 <= strikerect.right:
            speed[1] = -speed[1]
        else:
            gameend()


def gameload():
    """Lanuch when the game first start."""
    global screen
    screen.blit(welcome_content, welcome_pos)
    screen.blit(start, startrect)
    screen.blit(exitgame, exitrect)


def gameevent():
    """Handle the events occured while the game running."""
    global running, first_in_game
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            running = False
        if event.type is pygame.MOUSEBUTTONUP:
            p, q = pygame.mouse.get_pos()
            isstart = p > startrect.left and p < startrect.right \
                and q > startrect.top and q < startrect.bottom
            isend = p > exitrect.left and p < exitrect.right \
                and q > exitrect.top and q < exitrect.bottom
            if isend:
                running = False
            if isstart:
                first_in_game = False
                pygame.mouse.set_visible(False)


def gamerunning():
    """Run while game running."""
    global ballrect, screen
    ballbehavior()
    ballrect = ballrect.move(speed)

    x, y = pygame.mouse.get_pos()
    if x >= width - 400:
        x = width - 400
    screen.blit(strike, (x, strikerect.top))
    screen.blit(ball, ballrect)
# ------------
# 游戏主循环


while running:
    gameevent()
    time.sleep(0.0001)
    screen.fill(color)
    if first_in_game:
        gameload()
    else:
        gamerunning()
    pygame.display.flip()
