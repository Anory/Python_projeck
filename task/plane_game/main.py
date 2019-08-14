import pygame, sys
from task.plane_game import constants


def main():
    """游戏主入口"""
    pygame.init()
    width, height = 480, 852
    screen = pygame.display.set_mode((width, height))
    # 加载图片
    dg = pygame.image.load(constants.BG_IMG)
    start_img = pygame.image.load(constants.START_IMG)
    title_img = pygame.image.load(constants.TITLE_IMG)
    # 处理矩形图像的方法，获取图像位置信息
    start_img_rect = start_img.get_rect()
    # 获取图片宽高
    s_width, s_height = start_img.get_size()
    # 修改图片需要绘制在屏幕的位置
    start_img_rect.topleft = (int((width - s_width) / 2), int(height / 2 + s_height))
    print(start_img_rect)
    title_img_rect = title_img.get_rect()
    t_width, t_height = title_img.get_size()
    title_img_rect.topleft = (int((width - t_width) / 2), int(height / 2 - t_height))
    # 加载音乐
    pygame.mixer.music.load(constants.BG_MUSIC)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)  # 音量设置20%
    # 设置游戏窗口标题
    pygame.display.set_caption("飞机大战外星人")
    # 游戏运行状态
    status = 0  # 0准备中  1运行中  2游戏结束
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if status == 0:
                    status = 1

        if status == 0:
            # print(dg.get_rect())
            # < rect(0, 0, 480, 852) >
            # screen.blit(dg, (0, 0))
            screen.blit(dg, dg.get_rect())
            screen.blit(start_img, start_img_rect)
            screen.blit(title_img, title_img_rect)
        elif status == 1:
            screen.blit(dg, dg.get_rect())
        pygame.display.flip()


if __name__ == '__main__':
    main()
