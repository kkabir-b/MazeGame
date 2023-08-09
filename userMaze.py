from userMazeClasses import *
chosenMaze = UserMaze(100,100,10,10,200,200)

play = Player(100,100,chosenMaze.tileLength)
startButton = button(130,310,'start',140,50,30,'lime')

def restartScreen(): #called to restart the maze
    chosenMaze.reset()
    play.reset()
    startButton.reset('lime')

def userMazeScreenDraw(app):
    
    chosenMaze.drawMaze()
    if not chosenMaze.won:
        chosenMaze.drawTimer()
    play.drawPlayer()
    chosenMaze.drawBorder()
    if not chosenMaze.won:
        startButton.draw()
    
    if chosenMaze.won:
        chosenMaze.drawWinMessage()


def userMazeOnStep(app): #appends timer value
    if chosenMaze.start and not(chosenMaze.won):
        chosenMaze.timeTaken += .1


def userMazeOnMousePress(app,mouseX,mouseY): #used to see if a tile has been clicked
    if startButton.isClicked(mouseX,mouseY):
        chosenMaze.start = True
        startButton.color = 'gray'
    if not chosenMaze.start:
        chosenMaze.doTilesChange(mouseX,mouseY)



def userMazeOnKeyPress(app,key): #used to move the player
    if chosenMaze.start and not chosenMaze.won:
        if key == 'right':
            if play.isMoveLegal(1,0,chosenMaze):
                play.move(1,0)
        elif key == 'left':
            if play.isMoveLegal(-1,0,chosenMaze):
                play.move(-1,0)
        elif key == 'down':
            if play.isMoveLegal(0,1,chosenMaze):
                play.move(0,1)
        elif key == 'up':
            if play.isMoveLegal(0,-1,chosenMaze):
                play.move(0,-1)

    if key == 'r': #resets the maze
        restartScreen()
        
    if play.checkIfWon(chosenMaze): #checks if won
        chosenMaze.won = True
