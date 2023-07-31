from cmu_graphics import *
import random 
#credit for the maze generation algorithm I plan to used
# (not fully impletemented at the time of TP0, but rather and buggy 
# edited version that causes an infinite loop in bigger mazes) 
# https://www.algosome.com/articles/maze-generation-depth-first.

class maze:
    mazeX = 50
    mazeY = 50
    mazeWidth = 250
    mazeHeight = 250
    mazeCols = 25
    mazeRows = 25
    tileLength = mazeWidth//mazeCols
    

    def __init__(self):
        pass

class tile:
    def __init__(self,x,y,color):
        self.x = maze.mazeX + x
        self.y = maze.mazeY + y
        self.color = color




def onAppStart(app):

    app.setMaxShapeCount(3000)
    restartApp(app)

def restartApp(app):
    
    app.board = []
    for i in range(maze.mazeRows):
        row = []
        for j in range(maze.mazeCols):
            row.append(0)
        app.board.append(row)
    app.board[0][0] = 1
    app.board[maze.mazeRows - 1][maze.mazeCols - 1] = 1
    makeMaze(app)
    


def redrawAll(app):
    
    drawMaze(app)

    drawBorder()
        
def drawMaze(app):
    
    for row in range(len(app.board)):
        for col in range(len(app.board[0])):
            color = 'black' if app.board[row][col] == 0 else 'white'
            t = tile(col*maze.tileLength,row*maze.tileLength,color)
            drawRect(t.x,t.y,20,20,fill = t.color)



def drawBorder():
    drawRect(maze.mazeX,maze.mazeY,maze.mazeWidth + maze.tileLength/2
             ,maze.mazeHeight + maze.tileLength/2,fill = None,border = 'black')


def isMoveLegal(r1,c1,r2,c2):
    if r1+r2 < 0 or c1+c2 < 0:
        return False
    elif r1+r2 >= maze.mazeRows or c1+c2 >= maze.mazeCols:
        return False
    return True

def makeMaze(app):
    visit = []
    visit.append([0,0])
    currR = 0
    currC = 0
    while [maze.mazeRows -1,maze.mazeCols - 1] not in visit:
        newR = random.randint(-1,1)
        newC = random.randint(-1,1)
        
        while not isMoveLegal(currR,currC,newR,newC):
            newR = random.randint(-1,1)
            newC = random.randint(-1,1)
        
        if random.choice([0,1]) == 1:
            newC = 0
        else:
            newR = 0

        currR += newR
        currC += newC
        visit.append([currR,currC])
        
        app.board[currR][currC] = 1
    

runApp()

