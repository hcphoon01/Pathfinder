<<<<<<< HEAD
import pygame

class Draw:
	def addWall(pos):
		column = pos[0] // (g_width + margin)
		row = pos[1] // (g_height + margin)
		rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
		colour = BLACK
=======
import pygame

class Draw:
	def addWall(pos):
		column = pos[0] // (g_width + margin)
		row = pos[1] // (g_height + margin)
		rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
		colour = BLACK
>>>>>>> 9ed9dde44e46dc9d7ec244a384416bf374c3de10
		return pygame.draw.rect(win, colour, rect)