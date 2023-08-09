from cmu_graphics import *
import math
from PIL import Image

#contains all of the classes on user-maze gamemode

class UserMaze: #contains info on the maze itself
    def reset(self): #used to reset the maze
        self.start = False
        self.timeTaken = 0
        self.won = False
        self.tiles = []

        for rowTile in range(self.rows): #resets the board
            rowTiles = []
            for colTile in range(self.cols):
                rowTiles.append(tile('black',self.xOffset + self.tileLength*rowTile, self.yOffset + self.tileLength*colTile,self.tileLength - 1))
            self.tiles.append(rowTiles)

        self.tiles[0][0].color = 'yellow'
        self.tiles[-1][-1].color = 'yellow'

    def __init__(self,x,y,rows,cols,width,height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.tileLength = width//rows
        self.xOffset = x
        self.yOffset = y
        self.tiles = []
        self.start = False
        self.timeTaken = 0
        self.won = False
        

        for rowTile in range(rows): #creates board
            rowTiles = []
            for colTile in range(cols):
                rowTiles.append(tile('black',self.xOffset + self.tileLength*rowTile, self.yOffset + self.tileLength*colTile,self.tileLength - 1))
            self.tiles.append(rowTiles)
        self.tiles[0][0].color = 'yellow'
        self.tiles[-1][-1].color = 'yellow'
   
    def drawMaze(self): #draws the maze
        for rowTiles in self.tiles:
            for t in rowTiles:
                drawRect(t.x,t.y,t.length,t.length, fill = t.color)

    def drawBorder(self): #used to draw the border
        drawRect(self.xOffset - 2,self.yOffset - 2,
                 self.width+2,self.height + 2,fill = None, border = 'black')

    def drawTimer(self): #used to display the timer
        drawRect(self.xOffset + 5,self.yOffset - 50,self.width - 5,30,
                 fill = 'yellow')
        drawLabel(f'Time: {rounded(self.timeTaken*100)/100}',self.xOffset + 2.5 + self.width//2,
                  self.yOffset - 50 + 30//2,font = 'monospace',size = 20)
        
    def drawWinMessage(self): #used to display the win message
        drawRect(120,50,170,280,fill = 'gray',border = 'black')
        drawLabel('You win!',120 + 170/2,70,font = 'monospace',size = 30)
        drawLabel(f'You took {rounded(self.timeTaken*100)/100} secs',120 + 170/2,100
                  ,font = 'monospace',size = 15)
        drawLabel('HighScores!',120 + 170/2,130,size = 20,font = 'monospace')
        scores = open('userMazeHighScores.txt','r')
        s = [ float(i) for i in scores.read().split('~')[:-1]]
        s.sort()
        scores.close()
        for i in range(min(5,len(s))):
            drawLabel(f'{s[i]} seconds',120 + 170/2, 160 + 20*i,size = 15,font = 'monospace')


    def doTilesChange(self,x,y): #checks if any tile was clicked
        for rowTiles in self.tiles:
            for t in rowTiles:
                t.isClick(x,y)



    
class tile: #used for info on the different tiles making up the maze
    def __init__(self,color,x,y,length):
        self.color = color
        self.x = x
        self.y = y
        self.length = length
    def isClick(self,x,y): #checks if a tile was clicked
        if (self.x <= x < self.x + self.length) and (self.y <= y < self.y + self.length): 
            self.color = None if self.color == 'black' else 'black'

class Player: #contains info and methods on the player
    
    def reset(self): #resets the player
        self.gameOver = False
        self.xIndex = 0
        self.yIndex = 0

    def __init__(self,x,y,length):
        self.xIndex = 0
        self.yIndex = 0
        self.x = x
        self.y = y
        self.length = length
        self.gameOver = False
        self.Image = CMUImage(Image.open('penguinSprite.png'))

    def drawPlayer(self): #draws the player
        drawImage(self.Image,self.x + self.length * (self.xIndex),self.y + self.length*(self.yIndex) , width = self.length,height = self.length)

    def move(self,x,y): #used to move the player
        self.xIndex += x
        self.yIndex += y

    def isMoveLegal(self,x,y,maze): #used to check if a move is legal for a pleyr
        return ((0 <= self.xIndex + x < len(maze.tiles)) #to do
                and (0 <= self.yIndex + y < len(maze.tiles[0]))
                and (maze.tiles[self.xIndex + x][self.yIndex + y].color != 'black'))
    
    def checkIfWon(self,m): #used to check if the user has won
        win = self.xIndex == (m.rows - 1) and self.yIndex == (m.cols - 1)
        if win:
            scores = open('userMazeHighScores.txt','a')
            scores.write(f'{rounded(m.timeTaken * 100)/100}~')
            scores.close()
        return win
    
class button:

    def reset(self,color): #used to reset the button
        self.pressed = False
        self.color = color

    def __init__(self,x,y,text,width,height,textSize,color):
        self.x = x
        self.y = y
        self.pressed = False
        self.text = text
        self.width = width
        self.height = height
        self.size = textSize
        self.color = color

    def draw(self): #used to draw the button
        textColor = 'black' if self.color != 'blue' else 'white'
        drawRect(self.x,self.y,self.width,self.height,fill = self.color ,border = 'black')
        drawLabel(self.text,self.x + self.width//2,self.y + self.height//2,
                   font = 'monospace',size = self.size, fill = textColor,
                     bold = True)

    def isClicked(self,x,y):
        if (self.x <= x < self.x + self.width) and (self.y <= y < self.y + self.height):
            return True
        return False


