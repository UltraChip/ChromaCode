## UltraChip's ChromaCode Encoder
## v. 1.18.9
##
## Takes a string as input and encodes it in to 
## a "ChromaCode", an image made up of a grid of
## squares wherein data is encoded in the square's
## colors. See the documentation for more info.


# IMPORT AND INITIALIZE LIBRARIES

import pygame
import math

pygame.init()


# DEFINE PROCEDURES

def encodeText(text):  # Takes the string and turns it in to a list of
    i = 0              # RGB tuples.
    encoded = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

    text += chr(3)  # Add 'End of Text' marker.
    
    while i <= (len(text)-1):
        encoded.append(buildRGB(i, text))
        i += 3
    return encoded

def buildRGB(ndex, text):  # Takes three sequential characters
    i = 1                  # and converts it in to a single RGB
    rgb = []               # tuple.
    
    while i <= 3:
        if ndex >= len(text):
            rgb.append(0)
        else:
            rgb.append(ord(text[ndex]))
        i += 1
        ndex += 1
    return tuple(rgb)

def drawQR(encoded, winSize):
    colTotal = int(math.ceil(math.sqrt(len(encoded))))
    squareTotal = colTotal**2
    squareSize = ((winSize - 2) / colTotal) - 2
    i = 0
    x = 2
    y = 2
    colCount = 1
    
    window = pygame.display.set_mode((winSize, winSize))
    pygame.display.set_caption("ChromaQR")
    window.fill((255,255,255))
    
    while i < squareTotal:
        if i <= (len(encoded)-1):
            #print ("\n ", encoded[i], x, y)  # Debugging data
            pygame.draw.rect(window, encoded[i], (x,y,squareSize,squareSize), 0)
        else:
            pygame.draw.rect(window, (0,0,0), (x,y,squareSize,squareSize), 0)
        if colCount == colTotal:
            x = 2
            colCount = 1
            y += squareSize + 2
        else:
            x += squareSize + 2
            colCount += 1
        i += 1
    return window


# MAIN PROGRAM

filename = input("\nPlease enter the file name: ")
if filename[-4:] != ".bmp":
    filename += ".bmp"
winSize = int(input("\nPlease enter the image size in pixels^2: "))
theString = input("\nPlease enter the string you would like to encode: ")

colorCoded = encodeText(theString)

#print ("\nTHE RGB VALUES ARE:\n", colorCoded)  # Debugging data

QRimage = drawQR(colorCoded, winSize)

pygame.display.update()
pygame.image.save(QRimage, filename)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
