try:
	import pygame
	import sys
	from pygame.locals import *
	from random import randint
excepet:
	print("load modules erro")
	exit()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT =768
LOW_SPEED =30
HIGH_SPEED = 20
LOW_SIZE =5
HIGH_SIZE = 30
FONT_SIZE=40
FONT_NAME = "myfont.ttf"
FREQUENCE = 50
times = 0

def randomcolor():
	return (randint(0,255),randint(0,255),randint(0,255))

def randomspeed():
	return randint(LOW_SPEED,HIGH_SPEED)

def randomposition():
	return (randint(0,SCREEN_WIDTH),randint(0,SCEEN_HIGHT))

def randomsize():
	return randint(LOW_SIZE,HIGH_SIZE)

def randomname():
	return randint (0,100000)

def randomvalue():
	return fandint(0,9)

class Word(pygame.sprite.Sprite):
	def _init_(self,bornpositon):
		pygame.spritw.Sprite._init_(self)
		self.value = randomvalue()
		self.font = pygame.font.Font(FONT_NAME,FONT_SIZE)
		self.image = pygame.font.render(str(self.value),True,randomcolor())
		self.speed = randomspeed()
		self.rect = self.image.get_rect()
		self.rect.topleft = bornposition

	def update(self):
		self.rect = self.rect.move(0,self.speed)
		if self.rect.top > SCREEN_HEIGHT:
			self.kill()

pygame.init()
screen = pyame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("THE COMPUTER OF YSP")
clock = pygame.time.Clock()
group = pygame.time.Group()
group_count = SCREEN_WIDTH/FONT_SIZE

while True:
	time = clock.tick(FREQUENCE)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			exit()
	screen.fill((0,0,0))
	for i in range(0,int(group_count))
		group.add(Word((i*FONT_SIZE,-FONT_SIZE)))
	group.update()
	group.draw(screen)
	
	pygame.display.update()
		