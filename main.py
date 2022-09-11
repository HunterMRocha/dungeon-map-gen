import pygame
from room import Room 

pygame.init()

# CONSTANTS
WIN_SIZE = (800, 800)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode(WIN_SIZE)

playing = True
while playing:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			playing = False


	r = Room(100, 100, 50, 50)
	r.draw(screen, BLUE)


pygame.quit()