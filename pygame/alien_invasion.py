import pygame  #导入模块pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings  #导入设置
from ship import Ship  #导入飞船
from alien import Alien  #导入外星人

def run_game():
    #初始化python、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()  #创建一个实例，并存入变量
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))  #创建屏幕（长、宽尺寸）
    pygame.display.set_caption("Alien Invasion")  #把屏幕尺寸值传递到此

    ship = Ship(ai_settings,screen)  #创建一艘飞船
    bullets = Group()  #创建一个用于存储子弹的编组   
    aliens = Group()  #创建一个外星人编组

    gf.create_fleet(ai_settings,screen,aliens)  #创建外星人群

    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)  
        ship.update()  #更新飞船位置
        gf.update_bullets(bullets)  #更新子弹的位置
        gf.update_screen(ai_settings,screen,ship,aliens,bullets)  #更新屏幕和其中出现的元素

run_game()  #运行游戏
