from pygame import display as Window
from pygame import event as Event
from pygame import init as Initialization
from pygame import QUIT as GameEnd
from pygame import Surface as Screen
from pygame.draw import line as DrawLine
from pygame.draw import rect as DrawRect
from pygame.font import Font as Font
from pygame.font import get_fonts as FontsList
from pygame.font import init as FontInit
from pygame.font import SysFont as OSFont
from pygame.time import Clock as Time
from random import shuffle as Mix

Black = (0, 0, 0) #black color tuple
White = (255, 255, 255) #white color tuple

class Pytramino(object):
    def __init__(self, Shape, X = 5 , Y = -1):
        self.shape = Shape
        self.x = X
        self.y = Y
        self.rotation = 0

    def Draw(self, Surface):
        pass

class Grid(object):
    def __init__(self, LockedPos = {}):
        self.Unit = 40 #pixel of a block
        self.WBlocks = 10 #width blocks
        self.HBlocks = 20 #height blocks
        self.GridWidth = self.Unit * self.WBlocks #grid width blocks
        self.GridHeight = self.Unit * self.HBlocks  #grid height blocks
        self.Blocks = [[Black for C in range(self.WBlocks)] for R in range(self.HBlocks)] #blocks of the game grid
        self.LockedPos = LockedPos #locked position

        for R in range(len(self.Blocks)): #loop to set locked positions
            for C in range(len(self.Blocks[R])):
                if (R, C) in self.LockedPos: #check if x and y positions are the same of locked ones
                    Pos = self.LockedPos[(R, C)] #copying position
                    self.Blocks[R][C] = Pos #setting position as block

    def DrawGrid(self, Surface):
        SWidth = Surface.get_width()
        SHeight = Surface.get_height()
        TopLeftX = (SWidth - self.GridWidth) // 2
        TopLeftY = SHeight - self.GridHeight

        for R in range(len(self.Blocks)):
            StartRow = (TopLeftX, TopLeftY + R * self.Unit)
            EndRow = (TopLeftX + self.GridWidth, TopLeftY + R * self.GridWidth)
            DrawLine(Surface, White, StartRow, EndRow)
            for C in range(len(self.Blocks[R])):
                StartCol = (TopLeftX + C * self.Unit, TopLeftY)
                EndCol = (TopLeftX + C * self.Unit, TopLeftY + self.GridHeight)
                DrawLine(Surface, White, StartCol, EndCol)

        # for R in range(len(self.Blocks)):
        #     for C in range(len(self.Blocks[R])):
        #         BlockX = R * self.Unit
        #         BlockY = C * self.Unit
        #         GridBlock = (TopLeftX + BlockX, TopLeftY + BlockY, self.Unit, self.Unit)
        #         DrawRect(Surface, self.Blocks[R][C], GridBlock, 0)

class Game: # game super class
    def __init__(self):
        Initialization()  #game initialization
        FontInit()  #font initialization

        self.WIDTH = 800
        self.HEIGHT = 700
        self.Surface = Window.set_mode((self.WIDTH, self.HEIGHT)) #setting window
        Window.set_caption('Tetris') #window title
        self.Clock = Time()
        self.TitleScreen = StartTitle(self.Surface)
        self.SinglePlayer = Play(self.Surface)

        self.TitleScreen.MainLoop()

class StartTitle: #title screen
    def __init__(self, Surface):
        self.Win = Surface
        self.GameIsInMainMenu = True
        pass

    def DrawText(self, Text, TextFont, TextSize, Color, TopLeftX, TopLeftY): #function to draw text on title screen
        if TextFont in FontsList(): #check if the font is available in the system font list
            TSFont = OSFont(TextFont, TextSize) #setting the font from system font list

        else:
            FontDir = '/Lib/Font/' + TextFont #setting the font directory
            TSFont = Font(FontDir, TextSize) #setting the font from the game lib

        TextSurface = TSFont.render(Text, True, Color) #rendering the text with antialiasing and color
        self.WiN.blit(TextSurface, (TopLeftX, TopLeftY)) #rendering the text a given position

    def MainLoop(self): #title screen main loop
        while self.GameIsInMainMenu:
            for Action in Event.get():

                if Action.type == GameEnd:
                    self.GameIsInMainMenu = False
                    Exit()

class Play: #main gameplay screen
    def __init__(self, Surface):
        self.Win = Surface
        self.Shapes = \
            {
                'S':
                    [
                        [
                            '......',
                            '......',
                            '..00..',
                            '.00...',
                            '......'
                        ],
                        [
                            '.....',
                            '..0..',
                            '..00.',
                            '...0.',
                            '.....'
                        ]
                    ],
                'Z':
                    [
                        [
                            '.....',
                            '.....',
                            '.00..',
                            '..00.',
                            '.....'
                        ],
                        [
                            '.....',
                            '..0..',
                            '.00..',
                            '.0...',
                            '.....'
                        ]
                    ],
                'I':
                    [
                        [
                            '..0..',
                            '..0..',
                            '..0..',
                            '..0..',
                            '.....'
                        ],
                        [
                            '.....',
                            '0000.',
                            '.....',
                            '.....',
                            '.....'
                        ]
                    ],
                'O':
                    [
                        [
                            '.....',
                            '.....',
                            '.00..',
                            '.00..',
                            '.....'
                        ]
                    ],
                'J':
                    [
                        [
                            '.....',
                            '.0...',
                            '.000.',
                            '.....',
                            '.....'
                        ],
                        [
                            '.....',
                            '..00.',
                            '..0..',
                            '..0..',
                            '.....'
                        ],
                        [
                            '.....',
                            '.....',
                            '.000.',
                            '...0.',
                            '.....'
                        ],
                        [
                            '.....',
                            '..0..',
                            '..0..',
                            '.00..',
                            '.....'
                        ]
                    ],
                'L':
                    [
                        [
                            '.....',
                            '...0.',
                            '.000.',
                            '.....',
                            '.....'
                        ],
                        [
                            '.....',
                            '..0..',
                            '..0..',
                            '..00.',
                            '.....'
                        ],
                        [
                            '.....',
                            '.....',
                            '.000.',
                            '.0...',
                            '.....'
                        ],
                        [
                            '.....',
                            '.00..',
                            '..0..',
                            '..0..',
                            '.....'
                        ]
                    ],
                'T':
                    [
                        [
                            '.....',
                            '..0..',
                            '.000.',
                            '.....',
                            '.....'
                        ],
                        [
                            '.....',
                            '..0..',
                            '..00.',
                            '..0..',
                            '.....'
                        ],
                        [
                            '.....',
                            '.....',
                            '.000.',
                            '..0..',
                            '.....'
                        ],
                        [
                            '.....',
                            '..0..',
                            '.00..',
                            '..0..',
                            '.....'
                        ]
                    ],
            }

        self.ShapeColors = \
            [
                (0, 255, 0),
                (255, 0, 0),
                (0, 255, 255),
                (255, 255, 0),
                (255, 165, 0),
                (0, 0, 255),
                (128, 0, 128)
            ]

        self.GameGrid = Grid()
        self.GameIsRunning = True

    def GetPytraminoSequence(self): #function to get a full sequence of pieces (7)
        Sequence = self.Shapes.copy() #local copy of original sequence
        Mix(Sequence) #shuffle of the copy
        Sequence = [Pytramino(Piece) for Piece in Sequence] #object pieces creation
        return Sequence

    def IsOver(self):
        pass

    def DrawText(self, Text, TextFont, TextSize, TopLeftX, TopLeftY):
        pass

    def MainLoop(self): #game main loop
        while self.GameIsRunning:
            for Action in Event.get():

                if Action.type == GameEnd:
                    self.GameIsRunning = False
                    Exit()

def Exit(): #function to close the game properly
    Window.quit() #closing window
    quit() #closing python

if __name__ == '__main__':
    print(FontsList())
    PyTetris = Game()