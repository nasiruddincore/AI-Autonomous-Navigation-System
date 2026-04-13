import numpy as np

def create_grid(rows, cols):
    return np.zeros((rows, cols))

def add_obstacles(grid, obstacle_list):
    for (x, y) in obstacle_list:
        grid[x][y] = 1
    return grid