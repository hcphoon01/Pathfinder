import pygame

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

(g_width, g_height) = (20, 20)
margin = 1

class Draw:
	def Wall(self, pos, win, status):
		column = pos[0] // (g_width + margin)
		row = pos[1] // (g_height + margin)
		rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
		if status == "add":
			colour = BLACK
		elif status == "remove":
			colour = WHITE
		pygame.draw.rect(win, colour, rect)
		coords = []
		coords.extend([column, row])
		return coords

	def Start(self, pos, win, status):
		column = pos[0] // (g_width + margin)
		row = pos[1] // (g_height + margin)
		rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
		if status == "add":
			colour = GREEN
		elif status == "remove":
			colour = WHITE
		pygame.draw.rect(win, colour, rect)
		coords = []
		coords.extend([column, row])
		return coords

	def End(self, pos, win, status):
		column = pos[0] // (g_width + margin)
		row = pos[1] // (g_height + margin)
		rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
		if status == "add":
			colour = RED
		elif status == "remove":
			colour = WHITE
		coords = []
		coords.extend([column, row])
		return pygame.draw.rect(win, colour, rect), coords 


		