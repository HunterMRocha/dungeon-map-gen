import pygame

class Room:
	def __init__(self, x, y, w, h): 
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.rect = (x, y, w, h)

	def draw(self, surf, col): 
		pygame.draw.rect(surf, col, self.rect)

	