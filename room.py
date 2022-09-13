import pygame
pygame.init()

DARK_BROWN = (99, 89, 56)
rooms_pos = []

class Room:
	def __init__(self, x, y, width, height, id):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.id = id
		rooms_pos.append((self.x, self.y))

	def draw(self, surf, color=DARK_BROWN):
		pygame.draw.rect(surf, color, (self.x, self.y, self.width, self.height))
	
	def getBottomPos(self):
		left = self.x + (self.width//2)
		top = self.y + self.height
		return (left, top)

	def getTopPos(self):
		return (self.x + (self.width//2), self.y)

	def getRightPos(self):
		x = self.x + self.width
		return (x, self.y)

	def getLeftPos(self):
		return (self.x, self.y)
		
	def connectVert(self, surf, room2):
		x1, y1 = self.getTopPos()
		x2, y2 = room2.getBottomPos()
		pygame.draw.line(surf,DARK_BROWN, (x1, y1), (x2, y2-5), 10)

	def connectHor(self, surf, room2):
		x1, y1 = self.getRightPos()
		x2, y2 = room2.getLeftPos()
		if y1 != y2:
			cornerX = x2 + self.width/2
			cornerY = y1 + self.height/2
			pygame.draw.line(surf, DARK_BROWN, (x1, y1+self.width/2), (cornerX, cornerY), 10)
			pygame.draw.line(surf, DARK_BROWN, (cornerX, cornerY-2), (x2+self.width/2, y2+self.width/2) , 10)
		# pygame.draw.line(surf,DARK_BROWN, (x1, y1+self.width/2), (x2, y2+self.width/2), 10)

	def connect(self, surf, room2):
		pass