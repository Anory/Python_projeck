import sys, pygame


pygame.init()
screen = pygame.display.set_mode((350, 620))
# 加载图片
ball = pygame.image.load(".\static\intro_ball.gif")
# 设置颜色
red = pygame.Color(255, 50, 255)
# 获取字体样式对象
font = pygame.font.Font(".\static\simhei.ttf", 16)
# 获取文字对象
text = font.render("得分：", True, red)
# 加载音乐
# bj_music = pygame.mixer.music.load(r".\static\11638.wav")
# 循环播放音乐
# pygame.mixer.music.play(-1)
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 画线(起点，结束， 线的大小)
    # pygame.draw.line(screen, red, (10, 10), (200, 200), 10)
    # 矩形(起点，长宽，线的大小)
    # pygame.draw.rect(screen, red, (200, 200, 100, 100), 3)
    # 绘制
    screen.blit(ball, (100, 100))
    screen.blit(text, (10, 5))
    pygame.display.flip()
