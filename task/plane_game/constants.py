import os

# 项目文件plane_game路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# assets文件路径
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# 背景图片路径
BG_IMG = os.path.join(ASSETS_DIR, "images/background.png")
# 开始按钮路径
START_IMG = os.path.join(ASSETS_DIR, "images/game_start.png")
# 标题图片路径
TITLE_IMG = os.path.join(ASSETS_DIR, "images/game_title.png")
# 音乐路径
BG_MUSIC = os.path.join(ASSETS_DIR, "sounds/game_bg_music.wav")