import pygame
import math

pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
CELL_SIZE = 5
DRONE_SIZE = 4

pygame.display.set_caption("Directional Pheromone Walk Simulation")

class Territory1:
    
    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        pygame.draw.circle(win, self.color, (x,y), self.radius)

def main():

    run = True
    clock = pygame.time.Clock()
    


    while run:
        clock.tick(60)
        WIN.fill((0,0,0))
        pygame.display.update()
    
    pygame.quit()

main()