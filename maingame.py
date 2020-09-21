import pygame,sys


#from sokoban import main_loop
mainClock = pygame.time.Clock()
from pygame.locals import *
from Colors import *
import sokoban
from sokoban import lvl
pygame.init()
screen = pygame.display.set_mode((600,600),0,32)
font = pygame.font.SysFont(None, 20)
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsanssms",50)
width = screen.get_width()
height = screen.get_height()
black = (0,0,0)
red = (255,0,0)
green = (34,177,76)

def score(score):
        text = smallfont.render("SCORE: "+str(score),True,black)
        screen.blit(text,[0,0])
def text_objects(text,color,size="small"):
        if size == "small":
                textSurface = smallfont.render(text,True,color)
        if size == "medium":
                textSurface = medfont.render(text,True,color)
        return textSurface,textSurface.get_rect()

def text_to_button(msg,color,x,y,w,h,size="small"):
        textSurf,textRect = text_objects(msg,color,size)
        textRect.center = ((x+(w/2)),y+(h/2))
        screen.blit(textSurf,textRect)
        

def draw_text(text,font,color,surface,x,y):
        textobj = font.render(text,1,color)
        textrect = textobj.get_rect()
        surface.blit(textobj,textrect)

click = False
def main_menu():
	
	
	while True:

			screen.fill((0,0,0))
			
			
			mx,my = pygame.mouse.get_pos()
			btn1 = pygame.Rect(50,100,200,80)
			btn2 = pygame.Rect(50,200,200,80)
			btn3 = pygame.Rect(50,300,200,80)
			btn4 = pygame.Rect(50,400,200,80)
			
			if btn1.collidepoint(mx,my):
					if click:
							game()
			if btn2.collidepoint(mx,my):
					if click:
							option()
			if btn3.collidepoint(mx,my):
					if click:
							level3()
			if btn4.collidepoint(mx,my):
					if click:
							level4()
							
			draw_text('SOKOBAN : ESC to quit or choose your level and use arrow keys to move mario',font,(255,255,255),screen,120,120)
			pygame.draw.rect(screen,(255,0,0),btn1)
			pygame.draw.rect(screen,(255,0,0),btn2)
			pygame.draw.rect(screen,(255,0,0),btn3)
			pygame.draw.rect(screen,(255,0,0),btn4)
			
			text_to_button("LEVEL 1",black,50,100,200,80)
			text_to_button("LEVEL 2",black,50,200,200,80)
			text_to_button("LEVEL 3",black,50,300,200,80)
			text_to_button("LEVEL 4",black,50,400,200,80)
			
			click = False
			for event in pygame.event.get():
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
					if event.type == KEYDOWN:
							if event.key == K_ESCAPE:
									pygame.quit()
									sys.exit()
					if event.type == MOUSEBUTTONDOWN:
							if event.button == 1:
									click = True
							
			pygame.display.update()
			mainClock.tick(50)
lvl = sokoban.lvl                
def game():
		
		running = True
		while running:
			draw_text('LEVEL 1',font,(255,255,255),screen,20,20)
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				
						
			sokoban.main_loop(lvl[0])
							
				
			pygame.display.update()
			mainClock.tick(50)

def option():
	
	running = True
	while running:
			draw_text('LEVEL 2',font,(255,255,255),screen,20,20)
			for event in pygame.event.get():
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
					if event.type == KEYDOWN:
							if event.key == K_ESCAPE:
									running = False
									return
			sokoban.main_loop(lvl[1])
			pygame.display.update()
			mainClock.tick(50) 
			
def level3():
	
	running = True
	while running:
			draw_text('LEVEL 3',font,(255,255,255),screen,20,20)
			for event in pygame.event.get():
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
					if event.type == KEYDOWN:
							if event.key == K_ESCAPE:
									running = False
									return
			sokoban.main_loop(lvl[2])
			pygame.display.update()
			mainClock.tick(50)
			
def level4():
	
	running = True
	while running:
			draw_text('LEVEL 4',font,(255,255,255),screen,20,20)
			for event in pygame.event.get():
					if event.type == QUIT:
							pygame.quit()
							sys.exit()
					if event.type == KEYDOWN:
							if event.key == K_ESCAPE:
									running = False
									return
			sokoban.main_loop(lvl[3])
			pygame.display.update()
			mainClock.tick(50)      
               
main_menu()


