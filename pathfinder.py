import pygame
from draw import Draw
import time

(width, height) = (800, 800)
(g_width, g_height) = (20, 20)
margin = 1

elapsed = 0
elapsed = pygame.time.get_ticks() - elapsed

class Node:
    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.position == other.position

def pathfinder(start, end, win, walls=None):
    global elapsed
    startNode = Node(None, start)
    startNode.g = startNode.h = startNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    openList = []
    closedList = []

    openList.append(startNode)

    while len(openList) > 0:
        currentNode = openList[0]
        currentIndex = 0

        for index, item in enumerate(openList):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index
        openList.pop(currentIndex)
        closedList.append(currentNode)
        Draw().closedList(currentNode.position, win)

        if currentNode == endNode:
            path = []
            current = currentNode
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]
            
        children = []
        for newPosition in [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]:
            childPosition = ([newPosition[0] + currentNode.position[0], newPosition[1] + currentNode.position[1]])

            if not ([0, 0]) <= childPosition <= ([37, 37]):
                continue
            if childPosition in walls:
                continue
            
            newNode = Node(currentNode, childPosition)

            children.append(newNode)

        for child in children:

            for closedChild in closedList:
                if child == closedChild:
                    continue

            child.g = currentNode.g + 1
            child.h = ((child.position[0] - endNode.position[0]) ** 2) + ((child.position[1] - endNode.position[1]) ** 2)
            child.f = child.g + child.h

            for openNode in openList:
                if child == openNode and child.g > openNode.g:
                    continue

            openList.append(child)
            Draw().openList(child.position, win)