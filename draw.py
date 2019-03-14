import pygame

class Draw:
	def addWall(pos):
		column = pos[0] // (g_width + margin)
		row = pos[1] // (g_height + margin)
		rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
		colour = BLACK
		return pygame.draw.rect(win, colour, rect)