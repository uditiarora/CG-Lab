import pygame
import time





def flood_fill_4(x,y,f_color,b_color):
		p_color = gameDisplay.get_at((x,y))
		if (p_color != f_color and p_color != b_color):
			gameDisplay.set_at((x,y),f_color)
			pygame.display.update()
			flood_fill_4(x+1,y,f_color,b_color)
			flood_fill_4(x,y+1,f_color,b_color)
			flood_fill_4(x,y-1,f_color,b_color)
			flood_fill_4(x-1,y,f_color,b_color)

def flood_fill_8(x,y,f_color,b_color):
		p_color = gameDisplay.get_at((x,y))
		if (p_color != f_color and p_color != b_color):
			gameDisplay.set_at((x,y),f_color)
			pygame.display.update()
			flood_fill_4(x+1,y,f_color,b_color)
			flood_fill_4(x,y+1,f_color,b_color)
			flood_fill_4(x,y-1,f_color,b_color)
			flood_fill_4(x-1,y,f_color,b_color)
			flood_fill_4(x-1,y-1,f_color,b_color)
			flood_fill_4(x-1,y+1,f_color,b_color)
			flood_fill_4(x+1,y-1,f_color,b_color)
			flood_fill_4(x+1,y+1,f_color,b_color)







pygame.init()

white = (255,255,255,255)
black = (0,0,0,255)

red = (255,0,0,255)
green = (0,255,0,255)
blue = (0,0,255,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(white)

pygame.draw.polygon(gameDisplay, green, ((50,75),(50,100),(100,75),(100,100)),3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if (event.type == pygame.MOUSEBUTTONDOWN):
        	x,y = event.pos
        	flood_fill_8(x,y,red,green)
        	#print(gameDisplay.get_at((x,y)))
    pygame.display.update()
