import pygame.mixer

pygame.init()
pygame.mixer.init()


def bg_music():
    """背景音乐"""
    pygame.mixer.music.load(r"D:\GitHub\Python\pygame\music\bg_music.ogg")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play() #开始播放


def laugh_sound():
    """发射子弹音效"""
    laugh_sound = pygame.mixer.Sound(r"D:\GitHub\Python\pygame\music\nico.wav")
    laugh_sound.set_volume(0.5)
    laugh_sound.play()
    