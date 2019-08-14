import sys, pygame


pygame.init()
red = pygame.Color(255, 50, 255)
screen = pygame.display.set_mode((350, 620))
hero_one = pygame.image.load(".\static\hero1.png")
hero_tow = pygame.image.load(".\static\hero2.png")
font = pygame.font.Font(".\static\simhei.ttf", 16)
text = font.render("得分：", True, red)
bj_music = pygame.mixer.music.load(r".\static\11638.wav")
pygame.mixer.music.play(-1)
# 获取clock对象，然后在游戏主循环里面调用tick方法设置动画帧率（一秒钟播放多少个画面）
clock = pygame.time.Clock()
count = 0
while True:
    count += 1
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 一秒钟播放60帧左右的动画
    clock.tick(60)
    # 填充屏幕颜色
    screen.fill(pygame.Color(255, 255, 255))
    screen.blit(text, (15, 10))
    if count % 5 == 0:
        screen.blit(hero_one, (130, 400))
    else:
        screen.blit(hero_tow, (130, 400))
    pygame.display.flip()
