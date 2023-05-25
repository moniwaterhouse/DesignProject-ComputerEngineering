import pygame
import math
from Territories.territory import Territory
from Drone.drone import Drone


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 5
DRONE_SIZE = 4
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (66, 229, 214)
PHEROMONE_INTENSITY = 500

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")

def draw_territory(territory):
    for i in range(0, len(territory)):
        for j in range(0, len(territory)):
            if territory[i][j].value == 1:
                pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)

def draw_drone(pos_x, pos_y):
    pygame.draw.rect(WIN, DRONE_COLOR, pygame.Rect(pos_x*CELL_SIZE,pos_y*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def main():
    run = True
    clock = pygame.time.Clock()

    newTerritory = Territory("Territories/territory1.txt")
    territory = newTerritory.matrix

    drone = Drone("east", 0, 0, PHEROMONE_INTENSITY)

    missingCells = True
    counter = 0

    while run:
        clock.tick(60)
        WIN.fill((255,255,255))

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if missingCells:
            counter = counter + 1
            missingCells = False
            drone.move(territory)
            territory = drone.depositPheromone(territory)
            for row in territory:
                for cell in row:
                    cell.evaporatePheromone()
                    if cell.visited == "F":
                        missingCells = True

        
        draw_territory(territory)
        draw_drone(drone.positionX, drone.positionY)
        pygame.display.update()
    
    pygame.quit()

main()