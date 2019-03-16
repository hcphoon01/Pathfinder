import pygame
from draw import Draw
from tkinter import *
from pathfinder import pathfinder

# Define colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define key presses
	# Mouse keys
M_LEFT = 1
M_RIGHT = 3

(width, height) = (800, 800)
(g_width, g_height) = (20, 20)
margin = 1

wallList = []
start = 0
end = 0

grid = []
for row in range((height // g_height)-2):
	grid.append([])
	for column in range((width // g_width)-2):
		grid[row].append(0)

pygame.init()
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("A* Pathfinding")

win.fill(BLACK)

for row in range((height // g_height)-2):
		for column in range((width // g_width)-2):
			colour = WHITE
			rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
			pygame.draw.rect(win, colour, rect)


done = False

clock = pygame.time.Clock()

while not done:
	for event in pygame.event.get():
		keys = pygame.key.get_pressed()
		mouse = pygame.mouse.get_pressed()
		if event.type == pygame.QUIT:
			done = True

		if mouse[0]:
			if all(a == 0 for a in keys):
				pos = pygame.mouse.get_pos()
				if ([pos[0] // (g_width + margin), pos[1] // (g_height + margin)]) == start or end:
					continue;
				coords = Draw().Wall(pos, win, "add")
				if coords not in wallList:
					wallList.append(coords)
#			if keys[pygame.K_s] and start == 0:
#				pos = pygame.mouse.get_pos()
#				coords = Draw().Start(pos, win, "add")
#				start = coords
#			if keys[pygame.K_e] and end == 0:
#				pos = pygame.mouse.get_pos()
#				coords = Draw().End(pos, win, "add")
#				end = coords
		
		if mouse[2]:
			if all(a == 0 for a in keys):
				pos = pygame.mouse.get_pos()
				if ([pos[0] // (g_width + margin), pos[1] // (g_height + margin)]) in wallList:
					coords = Draw().Wall(pos, win, "remove")
				elif ([pos[0] // (g_width + margin), pos[1] // (g_height + margin)]) == start:
					Draw().Start(pos, win, "remove")
					start = 0
				elif ([pos[0] // (g_width + margin), pos[1] // (g_height + margin)]) == end:
					Draw().End(pos, win, "remove")
					end = 0
			if keys[pygame.K_s] and start != 0:
				pos = pygame.mouse.get_pos()
				Draw().Start(pos, win, "remove")
				start = 0
			if keys[pygame.K_e] and end != 0:
				pos = pygame.mouse.get_pos()
				Draw().End(pos, win, "remove")
				end = 0

		if keys[pygame.K_s] and start == 0:
			pos = pygame.mouse.get_pos()
			coords = Draw().Start(pos, win, "add")
			start = coords
		
		if keys[pygame.K_e] and end == 0:
			pos = pygame.mouse.get_pos()
			coords = Draw().End(pos, win, "add")
			end = coords

		if keys[pygame.K_c]:
			for row in range((height // g_height)-2):
				for column in range((width // g_width)-2):
					colour = WHITE
					rect = ((margin + g_width) * column + margin, (margin + g_height) * row + margin, g_width, g_height)
					pygame.draw.rect(win, colour, rect)
					del wallList[:]
					start = 0
					end = 0

		if keys[pygame.K_SPACE]:
			if start != 0 and end != 0:
				path = pathfinder(start, end, win, wallList)
				Draw().Path(path, start, end, wallList, win)

		if keys[pygame.K_p]:
			print(pygame.mouse.get_pos())

	clock.tick(60)
	pygame.display.flip()

pygame.quit()