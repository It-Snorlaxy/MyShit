import random

class World():

    def __init__(self, width, height):
        self.grid = Grid(width, height)
        self.generations = 0

    def flip(self):
        for cell in self.grid.cells.values():
            cell.toggleAlive()

    def randomize(self):
        chance = random.randint(0,100)
        for cell in self.grid.cells.values():
            roll = random.randint(0,100)
            if roll >= chance:
                cell.toggleAlive()

    def reset(self):
        self.__init__(self.grid.width, self.grid.height)

    def countLiveNeighbours(self, x, y):
        aliveCount = 0
        neighbours = [(-1,-1),(0,-1),(1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0)]
        for neighbor in neighbours:
            coord = (x + neighbor[0], y + neighbor[1])
            if coord in self.grid.cells.keys():
                if self.grid.cells[coord].isAlive:
                    aliveCount += 1
        return aliveCount

    def update(self):
        newGrid = Grid(self.grid.width, self.grid.height)
        for cell in self.grid.cells.keys():
            Live = self.countLiveNeighbours(cell[0],cell[1])
            if self.grid.cells[cell].isAlive:
                if Live < 2:
                    newGrid.cells[cell].isAlive = False
                elif Live == 2 or Live == 3:
                    newGrid.cells[cell].isAlive = True
                elif Live > 3:
                    newGrid.cells[cell].isAlive = False
            elif Live == 3:
                newGrid.cells[cell].isAlive = True
        self.generations += 1
        self.grid.update(newGrid.cells)

    def getDimensions(self):
        return (self.grid.width, self.grid.height)

class Grid():

    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.cells = {}

        for x in range(width):
            for y in range(height):
                self.cells[(x,y)]=Cell()

    def update(self, newCells):
        self.cells = newCells

class Cell:

    def __init__(self, alive=False):
        self.isAlive = alive

    def toggleAlive(self):
        self.isAlive = not self.isAlive



#Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#Any live cell with two or three live neighbours lives on to the next generation.
#Any live cell with more than three live neighbours dies, as if by overpopulation.
#Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
