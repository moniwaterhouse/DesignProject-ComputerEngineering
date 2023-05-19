import numpy
import random

# Variables

colonySize = 1
initialPI = 500
iterations = 100

class Cell:

  def __init__(self, value):
    # If value = 0 is an empty space, if it is not 0 then is an obstacle
    self.value = value
    self.pheromoneIntensity = 0
    if self.value == 0:
      self.visited = "F"
    else:
      self.visited = "-"
  
  def evaporatePheromone(self):
    self.pheromoneIntensity = self.pheromoneIntensity - 1
    return self.pheromoneIntensity
  
  def depositPheromone(self):
    self.pheromoneIntensity = initialPI
    return self.pheromoneIntensity

class Territory1:

  def __init__(self):
    self.width = 10
    self.length = 10
    self.matrix = []
    for i in range(self.length):
        row = []
        for j in range(self.width):
          if i == 0 and (j in range(8,10)):
            cell = Cell(1)
          elif i == 1 and (j in range(8,10)):
            cell = Cell(1)
          elif i == 2 and (j in range(2,7)):
            cell = Cell(1)
          elif i == 4 and (j in range(2,7)):
            cell = Cell(1)
          elif i in range(5,7) and (j == 2):
            cell = Cell(1)
          elif i == 7 and (j in range(2,8)):
            cell = Cell(1)
          elif i == 8 and (j in range(6,8)):
            cell = Cell(1)
          else:
            cell = Cell(0)
          row.append(cell)
        self.matrix.append(row)

class Drone:

  def __init__(self, initialDirection, initialX, initialY):
    global territory
    self.direction = initialDirection
    self.positionX = initialX
    self.positionY = initialY
    self.northValue = 0
    self.southValue = 0
    self.eastValue = 0
    self.westValue = 0
    self.northPheromone = 0
    self.southPheromone = 0
    self.eastPheromone = 0
    self.westPheromone = 0
  
  def move(self):
    moveOptions = self.getMoveOptions()
    sortedOptions = sorted(moveOptions, key=lambda x: x[1])
    match len(sortedOptions):
      case 1:
        moveDirection = sortedOptions[0][0]
      case 2:
        if sortedOptions[0][1] == sortedOptions[1][1]:
          position = random.randint(0, 1)
          moveDirection = sortedOptions[position][0]
        else:
          moveDirection = sortedOptions[0][0]
      case 3:
        if sortedOptions[0][1] == sortedOptions[1][1]:
          if sortedOptions[0][1] == sortedOptions[2][1]:
            position = random.randint(0, 2)
            moveDirection = sortedOptions[position][0]
          else:
            position = random.randint(0, 1)
            moveDirection = sortedOptions[position][0]
        else:
          moveDirection = sortedOptions[0][0]
    self.changeCell(moveDirection)
    return

  def changeDirection(self, direction):
    cardinalPoints = ["north", "south", "east", "west"]
    cardinalPoints.remove(direction)
    directionIndex = random.randint(0,2)
    newDirection = cardinalPoints[directionIndex]
    self.direction = newDirection
    return newDirection

  def changeCell(self, moveDirection):
    match moveDirection:
      case "north":
        self.positionY = self.positionY - 1
      case "south":
        self.positionY = self.positionY + 1
      case "east":
        self.positionX = self.positionX + 1
      case "west":
        self.positionX = self.positionX - 1

  def getMoveOptions(self):
    self.checkNeighborState()
    moveOptions = []
    match self.direction:
      case "north":      
        if self.eastValue == 0:
          moveOptions.append(("east", self.eastPheromone))
        if self.westValue == 0:
          moveOptions.append(("west", self.westPheromone))
        if self.northValue == 0:
          moveOptions.append(("north", self.northPheromone))
        else:
          if len(moveOptions) == 0:
            self.direction = "south"
            moveOptions.append(("south", self.southPheromone))
          else:
            self.changeDirection("north")

      case "south":
        if self.eastValue == 0:
          moveOptions.append(("east", self.eastPheromone))
        if self.westValue == 0:
          moveOptions.append(("west", self.westPheromone))
        if self.southValue == 0:
          moveOptions.append(("south", self.southPheromone))
        else:
          if len(moveOptions) == 0:
            self.direction = "north"
            moveOptions.append(("north", self.southPheromone))
          else:
            self.changeDirection("south")

      case "east":
        if self.northValue == 0:
          moveOptions.append(("north", self.northPheromone))
        if self.southValue == 0:
          moveOptions.append(("south", self.southPheromone))
        if self.eastValue == 0:
          moveOptions.append(("east", self.eastPheromone))
        else:
          if len(moveOptions) == 0:
            self.direction = "west"
            moveOptions.append(("west", self.southPheromone))
          else:
            self.changeDirection("east")
      case "west":
        if self.northValue == 0:
          moveOptions.append(("north", self.northPheromone))
        if self.southValue == 0:
          moveOptions.append(("south", self.southPheromone))
        if self.westValue == 0:
          moveOptions.append(("west", self.westPheromone))
        else:
          if len(moveOptions) == 0:
            self.direction = "east"
            moveOptions.append(("east", self.southPheromone))
          else:
            self.changeDirection("west")
    
    return moveOptions


  def checkNeighborState(self):
    self.checkNorthNeighbor()
    self.checkSouthNeighbor()
    self.checkEastNeighbor()
    self.checkWestNeighbor()

  def checkNorthNeighbor(self):
    if self.positionY == 0:
      self.northValue = 1
    else:
      self.northValue = territory[self.positionY-1][self.positionX].value
      self.northPheromone = territory[self.positionY-1][self.positionX].pheromoneIntensity
    return

  def checkSouthNeighbor(self):
    if self.positionY == len(territory) - 1:
      self.southValue = 1
    else:
      self.southValue = territory[self.positionY+1][self.positionX].value
      self.southPheromone = territory[self.positionY+1][self.positionX].pheromoneIntensity
    return
  
  def checkEastNeighbor(self):
    if self.positionX == len(territory)-1:
      self.eastValue = 1
    else:
      self.eastValue = territory[self.positionY][self.positionX+1].value
      self.eastPheromone = territory[self.positionY][self.positionX+1].pheromoneIntensity
    return
  
  def checkWestNeighbor(self):
    if self.positionX == 0:
      self.westValue = 1
    else:
      self.westValue = territory[self.positionY][self.positionX-1].value
      self.westPheromone = territory[self.positionY][self.positionX-1].pheromoneIntensity
    return

newTerritory = Territory1()
territory = newTerritory.matrix
for row in territory:
  print("\n")
  for cell in row:
    print(cell.visited, " ", end='')

drone1 = Drone("north",0,0)
drone2 = Drone("south",0,0)
drone3 = Drone("east",0,0)
drone4 = Drone("west",0,0)

drones = [drone1, drone2, drone3, drone4]

missingCells = True
counter = 0

while missingCells:

  counter = counter + 1
  print("---- Iteración ", counter, "----")
  missingCells = False
  
  for drone in drones:
    drone.move()
    posX = drone.positionX
    posY = drone.positionY
    territory[posY][posX].visited = "V"
    territory[posY][posX].depositPheromone()
  
  for row in territory:
    print("\n")
    for cell in row:
      cell.evaporatePheromone()
      print(cell.visited, " , ", " ", end='')
      if cell.visited == "F":
        missingCells = True

  print("\n")   
  print("--------------")
  print("\n")