class Settings():
        """存储外星人入侵的所有设置的类"""

        def __init__(self):
            """初始化游戏的设置"""
            #屏幕设置
            self.screen_width = 1000  #屏幕宽度
            self.screen_height = 600  #屏幕长度
            self.bg_color = (247,252,246)  #背景色

            #飞船的设置
            self.ship_speed_factor = 1.5  #飞船速度

            #子弹设置
            self.bullet_speed_factor = 1
            self.bullet_width = 3
            self.bullet_height = 15
            self.bullet_color = 60,60,60
            self.bullets_allowed = 3