class Settings():
        """存储外星人入侵的所有设置的类"""

        def __init__(self):
            """初始化游戏的静态设置"""
            #屏幕设置
            self.screen_width = 1200  #屏幕宽度
            self.screen_height = 600  #屏幕长度
            self.bg_color = (255,255,255)  #背景色

            #飞船的设置
            self.ship_speed_factor = 1.5  #飞船速度
            self.ship_limit = 3

            #子弹设置
            self.bullet_speed_factor = 3
            self.bullet_width = 5  #子弹宽度
            self.bullet_height = 15  #子弹长度
            self.bullet_color = 242,143,0  #子弹颜色
            self.bullets_allowed = 5  #可发射的最多子弹数

            #外星人设置
            self.alien_speed_factor = 1
            self.fleet_drop_speed = 10  #外星人下降速度
            self.fleet_direction = 1  #fleet_direction为1表示右移，为-1表示左移 

            self.speedup_scale = 1.1  #以什么样的速度加快游戏节奏
            self.score_scale = 1.5  #外星人点数的提高速度

            self.initialize_dynamic_settings()

        def initialize_dynamic_settings(self):
            """初始化随游戏进行而变化的设置"""
            self.ship_speed_factor = 1.5
            self.bullet_speed_factor = 3
            self.alien_speed_factor = 1

            self.fleet_direction = 1  #fleet_direction为1表向右，为-1表向左
            self.alien_points = 10

        def increase_speed(self):
            """提高速度设置和外星人点数"""
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale

            self.alien_points = int(self.alien_points * self.score_scale)