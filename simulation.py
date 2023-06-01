import pygame
import math
from Territories.territory import Territory
from Drone.drone import Drone


WIDTH, HEIGHT = 600, 600
CELL_SIZE = 5
DRONE_NUMBER = 20
PHEROMONE_INTENSITY = 500
OBSTACLE_COLOR = (63, 60, 60)
DRONE_COLOR = (66, 229, 214)
WHITE = (255, 255, 255)

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Directional Pheromone Walk Simulation")

def draw_territory(territory):
    for i in range(0, len(territory)):
        for j in range(0, len(territory)):
            if territory[i][j].value == 1:
                pygame.draw.rect(WIN, OBSTACLE_COLOR, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)
            else:
                pheromoneIntensity = territory[i][j].pheromoneIntensity
                if pheromoneIntensity in range(337, 501):
                    pheromoneColor = (229, 66 + (500 - pheromoneIntensity), 66)
                elif pheromoneIntensity in range(174, 337):
                    pheromoneColor = (pheromoneIntensity - 109, 229, 66)
                elif pheromoneIntensity in range(11, 174):
                    pheromoneColor = (66, 229, 66 + (173 - pheromoneIntensity))
                elif pheromoneIntensity in range (1, 11):
                    pheromoneColor = (66 + (10 - pheromoneIntensity), 229, 229)
                else:
                    if(territory[i][j].visited == "F"):
                        pheromoneColor = WHITE
                    else:
                        pheromoneColor = (76, 229, 229)
                pygame.draw.rect(WIN, pheromoneColor, pygame.Rect(j*CELL_SIZE,i*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def draw_drone(pos_x, pos_y):
    pygame.draw.rect(WIN, DRONE_COLOR, pygame.Rect(pos_x*CELL_SIZE,pos_y*CELL_SIZE,CELL_SIZE, CELL_SIZE),0)


def main():
    run = True
    clock = pygame.time.Clock()

    newTerritory = Territory("Territories/territory1.txt")
    territory = newTerritory.matrix

    drones = []

    for i in range(1, DRONE_NUMBER + 1):
        if i%4 == 0:
            drone = Drone("north",0,0,PHEROMONE_INTENSITY)
        elif i%3 == 0:
            drone = Drone("south",0,0,PHEROMONE_INTENSITY)
        elif i%2 == 0:
            drone = Drone("east",0,0,PHEROMONE_INTENSITY)
        else:
            drone = Drone("west",0,0,PHEROMONE_INTENSITY)
        drones.append(drone)


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
            for drone in drones:
                drone.move(territory)
                territory = drone.depositPheromone(territory)
            for row in territory:
                for cell in row:
                    cell.evaporatePheromone()
                    if cell.visited == "F":
                        missingCells = True
        else:
            print("Iterations: ", counter)
        

        
        draw_territory(territory)
        for drone in drones:
            draw_drone(drone.positionX, drone.positionY)
        pygame.display.update()
    
    pygame.quit()

main()