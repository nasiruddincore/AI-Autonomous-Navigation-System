import pygame

class Agent:
    def __init__(self, start):
        self.position = start
        self.path = []

    def set_path(self, path):
        self.path = path

    def move(self):
        if self.path:
            self.position = self.path.pop(0)

    def draw(self, screen, cell_size):
        pygame.draw.rect(screen, (0,255,0),
                         (self.position[1]*cell_size,
                          self.position[0]*cell_size,
                          cell_size, cell_size))