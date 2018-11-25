import pygame  #导入模块pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings  #导入设置
from game_stats import GameStats  #导入统计
from ship import Ship  #导入飞船
from alien import Alien  #导入外星人
from button import Button  #导入开始按钮
from scoreboard import Scoreboard  #导入计分
from music import *  #导入声音

def run_game():
    #初始化python、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()  #创建一个实例，并存入变量
    screen = pygame.display.set_mode((ai_settings.screen_width,
        ai_settings.screen_height))  #创建屏幕（长、宽尺寸）
    pygame.display.set_caption("妮可大战喵帕斯")  #把屏幕尺寸值传递到此

    play_button = Button(ai_settings,screen,'Play')  #创建play按钮

    stats = GameStats(ai_settings)  #创建一个用于存储游戏统计信息的实例
    sb = Scoreboard(ai_settings,screen,stats)

    ship = Ship(ai_settings,screen)  #创建一艘飞船
    bullets = Group()  #创建一个用于存储子弹的编组   
    aliens = Group()  #创建一个外星人编组

    gf.create_fleet(ai_settings,screen,ship,aliens)  #创建外星人群

    bg_music()  #背景音乐
    if pygame.K_y:
        pygame.mixer.music.pause()
    if pygame.K_u:
        pygame.mixer.music.unpause()
    
    #开始游戏的主循环
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)  #检测按键和鼠标事件
        
        if stats.game_active:
            ship.update()  #更新飞船位置
            gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)  #更新子弹的位置
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)  #更新外星人群
        
        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)  #更新屏幕

run_game()  #运行游戏