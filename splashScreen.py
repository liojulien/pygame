import pygame
from Colors import *


pygame.init()
class Block(pygame.sprite.Sprite):
	
	def __init__(self,color,width,height):
		
		super(Block,self).__init__()
		self.image = pygame.Surface((width,height))
		self.image.fill(color)
		self.sound = pygame.mixer.Sound("sounds/jumps.wav")
		self.rect = self.image.get_rect()
	
		
	def set_position(self,x,y):
		self.rect.x = x
		self.rect.y = y
	def set_image(self,filename = None):
		if (filename != None):
			self.image = pygame.image.load(filename)
			self.rect = self.image.get_rect()
	def play_sound(self):
		self.sound.play()
	
		
	def start_menu(self):
		pygame.init()
		window_size = window_width,window_height = 640,480
		w,h = 45,45
		window = pygame.display.set_mode(window_size)
		pygame.display.set_caption("SOKOBAN")
		window.fill(gray)
		clock = pygame.time.Clock()
		frame_per_second = 30
		block_group = pygame.sprite.Group()
		a_block = Block(blue,w,h)
		a_block.set_image("img/menu.jpg")
		block_group.add(a_block)
		block_group.draw(window)
		
		running = True
		
		while running:
			
			for event in pygame.event.get():
				if (event.type == pygame.QUIT):
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p or event.key == pygame.K_r:
						a_block.play_sound()
						
					
						
						
			pygame.display.update()
			clock.tick(frame_per_second)
			
		pygame.quit()
a = Block(red,500,600)
#a.start_menu()
	
	
	
	
