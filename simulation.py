import pygame
import math
from Territories.territory import Territory


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 5
DRONE_SIZE = 4
OBSTACLE_COLOR = (63, 60, 60)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")

def draw_territory(territory):
    for i in range(0, len(territory)):
        for j in range(0, len(territory)):
            if territory[i][j].value == 1:
                pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)



def main():
    run = True
    clock = pygame.time.Clock()

    newTerritory = Territory("Territories/territory1.txt")
    territory = newTerritory.matrix


    while run:
        clock.tick(60)
        WIN.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_territory(territory)
        pygame.display.update()
    
    pygame.quit()

main()