import pygame, sys


screen = pygame.display.set_mode((350, 550))


# 实现一个精灵类，后面调用这个类生成一个精灵实例，最后把实例里面的surface对象画到屏幕上
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, init_pos):
        pygame.sprite.Sprite.__init__(self)
        # 生成一个surface对象
        self.image = pygame.Surface([width, height])
        # 填充颜色
        self.image.fill(color)
        # 获取surface对象的宽高(不明白就打印出来看看)
        self.rect = self.image.get_rect()
        # 设置surface要画在屏幕的位置,接收的参数是元组
        self.rect.topleft = init_pos


block1 = Block(pygame.Color(255, 0, 0), 50, 50, (50, 50))
block2 = Block(pygame.Color(0, 255, 0), 50, 50, (90, 90))

# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 在屏幕上绘制精灵
    screen.blit(block1.image, block1.rect)
    screen.blit(block2.image, block2.rect)
    # 矩形碰撞检测
    rest = pygame.sprite.collide_rect(block1, block2)
    print(rest)
    # 链式调用collide_circle_ratio(1) 取值0-1
    rest2 = pygame.sprite.collide_circle_ratio(1)(block1, block2)
    print(rest2)
    pygame.display.flip()
