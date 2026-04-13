import pygame
from simulation.grid import create_grid, add_obstacles
from simulation.agent import Agent
from algorithms.astar import astar

ROWS, COLS = 20, 20
CELL_SIZE = 30

pygame.init()
screen = pygame.display.set_mode((COLS*CELL_SIZE, ROWS*CELL_SIZE))
clock = pygame.time.Clock()

grid = create_grid(ROWS, COLS)

obstacles = [(5,5),(5,6),(5,7),(10,10),(11,10)]
grid = add_obstacles(grid, obstacles)

start = (0,0)
goal = (15,15)

agent = Agent(start)
path = astar(grid, start, goal)
agent.set_path(path)

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw grid
    for i in range(ROWS):
        for j in range(COLS):
            color = (255,255,255)
            if grid[i][j] == 1:
                color = (255,0,0)
            pygame.draw.rect(screen, color,
                             (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

    agent.move()
    agent.draw(screen, CELL_SIZE)

    pygame.display.flip()
    clock.tick(5)

pygame.quit()