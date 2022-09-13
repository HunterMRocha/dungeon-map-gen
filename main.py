import pygame
import random
from room import Room 

global fonts
rooms = []
total_rooms = 7
x = 150
y = 150

# CONSTANTS
BLUE = (0, 0, 255)
W, H = 50, 50


def init_screen_and_clock():
	global screen, display, clock
	pygame.init()
	WIN_SIZE = (800, 800)
	pygame.display.set_caption('D&D Map Gen')
	screen = pygame.display.set_mode(WIN_SIZE)
	clock = pygame.time.Clock()

def create_fonts(font_sizes_list):
	"Creates different fonts with one list"
	global fonts
	fonts = []
	for size in font_sizes_list:
		fonts.append(
			pygame.font.SysFont("Arial", size))
	return fonts


def render(fnt, item, col, pos): 
	'Renders font from display_fps'
	text = fnt.render(item, 0, pygame.Color(col))
	screen.blit(text, pos)

def display_fps():
	'data that will be rendered and blitted in _display'
	render(
		fnt=fonts[0],
		item=str(int(clock.get_fps())),
		col='white',
		pos=(0,0)
	)

def build():
	'''
	create and draw rooms
	connect rooms after every two drawn rooms
	'''
	global x, y, W, H
	roomGap = 40
	for i in range(total_rooms):
		rooms.append(Room(x, y, W, H, i+1))
		rooms[i].draw(screen)
		y = random.randint(50, 750)
		x = random.randint(50, 750)
		# make sure new room isn't overlapping old room pos  (still working on this)
		while x < rooms[i].x + rooms[i].width + roomGap and x > rooms[i].x - rooms[i].width - roomGap:
			x = random.randint(50, 750)
		while y < rooms[i].y + rooms[i].height + roomGap and y > rooms[i].y - rooms[i].height - roomGap: 
			y = random.randint(50, 750)

		if i >= 1 and i % 2 == 1: 
			# check horizontal connection
			if rooms[i-1].x < rooms[i].x:
				rooms[i-1].connectHor(screen, rooms[i])

			# check vertical connection
			elif rooms[i-1].y < rooms[i].y:
				rooms[i-1].connectVert(screen, rooms[i])
			

def main():

	init_screen_and_clock()
	fonts = create_fonts([32, 16, 14, 8])

	playing = True
	while playing:
		screen.fill((0, 0, 0))
		display_fps()

		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				playing = False

		# create and draw rooms
		build()

		clock.tick(60)

		pygame.display.flip()


	pygame.quit()

if __name__ == '__main__': 
	main()