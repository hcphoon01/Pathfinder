import pygame

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
lightRED = (200, 0, 0)
lightGREEN = (0, 200, 0)

(width, height) = (800, 800)
(g_width, g_height) = (20, 20)
margin = 1

class Draw:
	def Wall(self, pos, win, status):
		rect, column, row = Rect(pos, True)
		if status == "add":
			colour = BLACK
		elif status == "remove":
			colour = WHITE
		pygame.draw.rect(win, colour, rect)
		coords = []
		coords.extend([column, row])
		return coords

	def Start(self, pos, win, status):
		rect, column, row = Rect(pos, True)
		if status == "add":
			colour = GREEN
		elif status == "remove":
			colour = WHITE
		pygame.draw.rect(win, colour, rect)
		coords = []
		coords.extend([column, row])
		return coords

	def End(self, pos, win, status):
		rect, column, row = Rect(pos, True)
		if status == "add":
			colour = RED
		elif status == "remove":
			colour = WHITE
		pygame.draw.rect(win, colour, rect)
		coords = []
		coords.extend([column, row])
		return coords 

	def closedList(self, pos, win):
		newPos = [pos[0] * 20, pos[1] * 20]
		rect = Rect(newPos)
		colour = lightRED
		pygame.draw.rect(win, colour, rect)

	def openList(self, pos, win):
		newPos = [pos[0] * 20, pos[1] * 20]
		rect = Rect(newPos)
		colour = lightGREEN
		pygame.draw.rect(win, colour, rect)

	def Path(self, pathList, start, end, walls, win):
		for row in range((height // g_height)-2):
				for column in range((width // g_width)-2):
					colour = WHITE
					rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
					pygame.draw.rect(win, colour, rect)
		newStart = [(start[0] + 1) * 20, (start[1] + 1) * 20]
		newEnd = [(end[0] + 1) * 20, (end[1] + 1) * 20]
		self.Start(newStart, win, "add")
		self.End(newEnd, win, "add")
		for wall in walls:
			newWall = [(wall[0] + 1) * 20, (wall[1] + 1) * 20]
			self.Wall(newWall, win, "add")
		for path in pathList:
			if path == start or path == end:
				continue
			newPath = [(path[0] + 1) * 20, (path[1] + 1) * 20]
			rect = Rect(newPath)
			colour = BLUE
			pygame.draw.rect(win, colour, rect)
		
class Rect:
	def __new__(self, pos, extra=None):
		self.margin = margin
		self.width = g_width
		self.height = height
		self.pos = pos
		
		column = pos[0] // (g_width + margin)
		row = pos[1] // (g_height + margin)
		if extra:
			return (((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height), column, row)
		else:
			return ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
