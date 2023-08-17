# Import the random module for generating random numbers.
import random

width = 30
height = 20

maze = [[1] * width for i in range(height)]


startX, startY = random.randint(0, width - 1), 0
endX, endY = random.randint(0, width - 1), height - 1
maze[startY][startX] = 0
maze[endY][endX] = 0

stack = [(startX, startY)]

while stack:
    currentX, currentY = stack.pop()

    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
    random.shuffle(directions)

    for dx, dy in directions:
        nextX, nextY = currentX + dx, currentY + dy

        if nextX < 0 or nextY < 0 or nextX >= width or nextY >= height or maze[nextY][nextX] != 1:
            continue

        maze[currentY + dy // 2][currentX + dx // 2] = 0
        maze[nextY][nextX] = 0

        stack.append((nextX, nextY))
