class Settings():
        """存储外星人入侵的所有设置的类"""

        def __init__(self):
            """初始化游戏的设置"""
            #屏幕设置
            self.screen_width = 1200  #屏幕宽度
            self.screen_height = 700  #屏幕长度
            self.bg_color = (247,252,246)  #背景色

            #飞船的设置
            self.ship_speed_factor = 1.5  #飞船速度
            self.ship_limit = 3

            #子弹设置
            self.bullet_speed_factor = 3
            self.bullet_width = 3  #子弹宽度
            self.bullet_height = 15  #子弹长度
            self.bullet_color = 0,231,0  #子弹颜色
            self.bullets_allowed = 5  #可发射的最多子弹数

            #外星人设置
            self.alien_speed_factor = 1
            self.fleet_drop_speed = 10  #外星人下降速度
            self.fleet_direction = 1  #fleet_direction为1表示右移，为-1表示左移 