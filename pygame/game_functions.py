import sys  #导入模块sys，用于退出游戏
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:  #➡键向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:  #⬅键向左移动
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  #空格键发射子弹
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:  #q键退出游戏
        sys.exit()

def fire_bullet(ai_settings,screen,ship,bullets):
    """如果还没有达到限制，就发射一颗子弹"""
    #创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings,screen,ship,bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    bullets.update()  #更新子弹的位置
    for bullet in bullets.copy():  #删除已消失的子弹
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_screen(ai_settings,screen,ship,aliens,bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    #每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)  #使用ai_settings访问背景色

    #在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()  #将飞船绘制到屏幕上
    aliens.draw(screen)  #将外星人绘制到屏幕上

    pygame.display.flip()  #让最近的绘制屏幕可见

def get_number_aliens_x(ai_settings,alien_width):
    """计算每行可容纳多少个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(ai_settings,screen,aliens):
    """创建外星人群"""
    #创建一个外星人，并计算每行可以容纳多少个外星人
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)

    #创建第一行外星人
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings,screen,aliens,alien_number)
       