import pygame.font

class Scoreboard():
    """显示得分信息的类"""

    def __init__(self,ai_settings,screen,stats):
        """初始化显示得分涉及的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #显示得分信息时的字体设置
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()  #准备初始得分图像