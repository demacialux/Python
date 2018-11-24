# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-10 16:09:22
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-10 23:34:24
"""
播放声音和音效
将.ogg格式作为背景音乐,.wav作为音效
播放音效:
	-pygame.mixer.Sound对象
Pygame.mixer.Sound:
	Create a new Sound object from a file or buffer object
Load a new sound buffer from a filename, a python file object 
or a readable buffer object. Limited resampling will be performed
to help the sample match the initialize arguments for the mixer.
A Unicade string can only be a file pathname.
Sound对象的方法如下:
	方法						含义
play()				播放音效
stop()				停止播放
fadeout()			淡出
set_volumn()		设置音量
get_volumn()		获取音量
get_num_channels()	计算该音效播放了多少次
get_length()		获得该音效的长度
get_raw()			将该音效以二进制格式的字符串返回
播放背景音乐:
-pygame.mixer.music对象
pygame.mixer.music:
	pygame module for controlling streamed audio
music对象的方法:
	方法						 含义
load()				载入音乐
play()				播放音乐
rewind()			重新播放
stop()				停止播放
pause()				暂停播放
unpause()			恢复播放
fadeout()			淡出
set_volumn()		设置音量
get_volumn()		获取音量
get_busy()			检测音乐流是否正在播放
set_pos()			设置开始播放的位置
get_pos()			获取已经播放的时间
queue()				将音乐文件放入待播放列表中
set_endevent()		在音乐播放完毕时发送事件
get_endevent()		获取音乐播放完毕时发送的事件类型
"""
import pygame
import sys
from pygame.locals import *

pygame.init()
#Initialize the mixer module for Sound loading and playback.
#使用之前最好先初始化一下
pygame.mixer.init()

pygame.mixer.music.load("bg_music.ogg")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play() #开始播放

bird_sound = pygame.mixer.Sound("birdsound.wav")
bird_sound.set_volume(0.2)
dog_sound = pygame.mixer.Sound("dogbark.wav")
dog_sound.set_volume(0.2)


bg_size = width, height = 300, 200
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("MusicPlayDemo")

#空格表示暂停，再次按空格播放音乐
pause = False

pause_image = pygame.image.load("pause.png").convert_alpha()
unpause_image = pygame.image.load("unpause.png").convert_alpha()
pause_rect = pause_image.get_rect()
#将按钮显示到屏幕的正中央
pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2,\
(height - pause_rect.height) // 2

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()

		if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				#鼠标按左键播放狗叫声
				dog_sound.play()
			if event.button == 3:
				#鼠标按右键播放鸟叫声
				bird_sound.play()

		if event.type == KEYDOWN:
			#按下空格键 控制背景音乐的暂停和播放
			if event.key == K_SPACE:
				pause = not pause


	screen.fill((255, 255, 255))

	if pause:
		screen.blit(pause_image, pause_rect)
		pygame.mixer.music.pause()
	else:
		screen.blit(unpause_image, pause_rect)
		pygame.mixer.music.unpause()

	pygame.display.flip()

	clock.tick(30)