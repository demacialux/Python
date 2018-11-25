# -*- coding: utf-8 -*-
# @Author: Clarence
# @Date:   2018-03-09 10:33:03
# @Last Modified by:   Clarence
# @Last Modified time: 2018-03-11 09:47:03
"""
使用sprite中Sprite类中自带的碰撞检测来检测小球是否碰撞
spritecollide(sprite, group, dokill, collided = None)
第四个参数collided=None时是用Rect来检测是否碰撞
collided表示回调函数，指定函数种类会根据指定检测函数来检测碰撞
pygame.sprite.collide_circle():
	collide_circle(left, right) -> bool
	Tests for collision between two sprites, by tesing to 
	see if two circles centered on the sprites overlap.
	Intended to be passed as a collided callback function to
	the *collide functions. Sprites must have a "rect" and an optional
	"radius" attribute.
也就是说这个方法名(地址)传入spritecollide()方法中, sprite精灵必须
要有rect属性，
可选属性为radius.

pygame.sprite.Group()
	A container class to hold an manage multiple Sprite
	objects.
主要的方法有:
pygame.sprite.Group.sprites:
	list of the Sprites this Group contains 
pygame.sprite.Group.copy:
	duplicate the Group
pygame.sprite.Group.add:
	add Sprites to this Group
pygame.sprite.Group.remove:
	remove Sprites to this Group
pygame.sprite.Group.has:
	test if a Group contains Sprites
pygame.sprite.Group.update:
	call the update method on contained Sprites
pygame.sprite.Group.draw:
	blit the Sprite images
pygame.sprite.Group.clear:
	draw a background over the Sprites
pygame.sprite.Group.empty:
	remove all Sprites.
"""
import  pygame
import sys
from pygame.locals import *
from random import *

class Ball(pygame.sprite.Sprite):
	def __init__(self, image, position, speed, bg_size):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		#小球的位置
		self.rect.left, self.rect.top = position
		self.speed = speed
		self.width, self.height = bg_size[0], bg_size[1]
		#self.width = self.width / 2

	'''
	Pygame.Rect.move():
		moves the rectangle 
		move(x, y) -> Rect
		Returns a new rectangle that is moved by the given offset. The
		x and y arguments can be any integer value, positive or 
		negative.
		可以在Rect对象的move方法中添加可正可负的两元素
		如果要实现小球的移动，则要在类中添加一个move()方法，并且在绘图的时候调用小球
		对象的move()方法
	'''
	def move(self):
		self.rect = self.rect.move(self.speed)

		#类似实现贪吃蛇穿入墙壁从对面墙壁出来(左右方向)
		if self.rect.right < 0:
			self.rect.left = self.width
		elif self.rect.left > self.width:
			self.rect.right = 0

		#(上下方向) 从下往上 和 从上往下
		elif self.rect.bottom < 0:
			self.rect.top = self.height
		elif self.rect.top > self.height:
			self.rect.bottom = 0


def main():
	pygame.init()

	ball_image = "gray_ball.png"
	bg_image = "background.png"

	running = True

	# 添加模型的背景音乐
	pygame.mixer.music.load("bg_music.ogg")
	pygame.mixer.music.play()

	# 添加音效
	loser_sound = pygame.mixer.Sound("loser.wav")
	laugh_sound = pygame.mixer.Sound("laugh.wav")
	winner_sound = pygame.mixer.Sound("winner.wav")
	hole_sound = pygame.mixer.Sound("hole.wav")

	# 音乐播放完时游戏结束,将GAMEOVER事件加入到事件队列中去
	# USEREVENT为用户自定义的事件
	# 如果想定义第二个事件可以是GAMEOVERTWO = USEREVENT + 1
	GAMEOVER = USEREVENT
	#背景音乐结束后发生GAMEOVER事件消息
	pygame.mixer.music.set_endevent(GAMEOVER)

	# 根据背景图片指定游戏界面尺寸
	bg_size = width, height = 1024, 681
	screen = pygame.display.set_mode(bg_size)
	pygame.display.set_caption("Play the Ball")

	#.png格式可以加入apha通道
	background = pygame.image.load(bg_image).convert_alpha()

	#用来存放小球对象的列表
	balls = []
	group = pygame.sprite.Group()

	for i in range(5):
		#球的尺寸是100*100 随机产生小球的位置
		position = randint(0, width-100), randint(0, height-100)
		#两个元素的一个列表，表示x轴和y轴方向的速度
		speed = [randint(-10, 10), randint(-10, 10)]
		#实例化小球对象 分别传入Surface对象 位置二元组 速度两元素列表
		ball = Ball(ball_image, position, speed, bg_size)
		#碰撞检测之后不从组里面删除
		while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
			ball.rect.left, ball.rect.top = randint(0, width - 100),\
			randint(0, height - 100)

		balls.append(ball) #将小球加入到小球列表中
		group.add(ball)

	# CLock()对象用来设置小球的帧率
	clock = pygame.time.Clock()

	while  running:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()

			elif event.type == GAMEOVER:
				loser_sound.play()
				pygame.time.delay(2000)
				laugh_sound.play()
				running = False #结束循环

		screen.blit(background, (0, 0))

		for each in balls:
			each.move()
			screen.blit(each.image, each.rect) 

		for each in group:
			group.remove(each)

			if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
				each.speed[0] = -each.speed[0]
				each.speed[1] = -each.speed[1]

			group.add(each)

		pygame.display.flip() #将显示缓冲区中的数据刷入显示器中
		clock.tick(30)




if __name__ == "__main__":
	main()
