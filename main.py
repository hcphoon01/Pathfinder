<<<<<<< HEAD
import pygame
from draw import Draw

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
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONUP and event.button == M_LEFT:
			draw.addWall(pygame.mouse.get_pos())
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == M_RIGHT:
			pos = pygame.mouse.get_pos()
			column = pos[0] // (g_width + margin)
			row = pos[1] // (g_height + margin)
			grid[row][column] = 0

	clock.tick(60)

	pygame.display.flip()

=======
import pygame
from draw import Draw

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
		if event.type == pygame.QUIT:
			done = True
		elif event.type == pygame.MOUSEBUTTONUP and event.button == M_LEFT:
			draw.addWall(pygame.mouse.get_pos())
		elif event.type == pygame.MOUSEBUTTONDOWN and event.button == M_RIGHT:
			pos = pygame.mouse.get_pos()
			column = pos[0] // (g_width + margin)
			row = pos[1] // (g_height + margin)
			grid[row][column] = 0

	clock.tick(60)

	pygame.display.flip()

>>>>>>> 9ed9dde44e46dc9d7ec244a384416bf374c3de10
pygame.quit()