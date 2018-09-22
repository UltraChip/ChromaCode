## UltraChip's Chromacode Decoder
## v. 1.18.9
##
## Takes a ChromaCode image as input and returns
## the data encoded therein.


# IMPORTS, INITIALIZATIONS, AND GLOBAL VARIABLES

import pygame
import math
import sys

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)


# DEFINE PROCEDURES

def checkCode(image):
    width = image.get_width()
    x, y = 2, 2
    testcolors = [red, green, blue]
    colorIndex = 0
    count, colWidth = detectColumns(image, width)

    if colWidth < 9:
        print ("\nThe squares are too small!")
        return False

    while x < width:
        if image.get_at((x,y)) != testcolors[colorIndex]:
            if image.get_at((x,y)) == white:
                if colorIndex == 2:
                    return True
                colorIndex += 1
                while image.get_at((x,y)) == white:
                    x += 1
                    if x >= width: return False
            else:
                print ("\nCouldn't detect the calibration squares!")
                return False
        x += 1
    return False

def scanImage(image):
    width = image.get_width()
    encodedText = []
    colCount, colWidth = detectColumns(image, width)
    x = int(math.floor(colWidth / 2))
    y = int(math.floor(colWidth / 2))
    squareX, squareY = 1, 1

    while squareY <= colCount:
        while squareX <= colCount:
            encodedText.append(image.get_at((x, y)))
            x += colWidth
            squareX += 1
        squareX = 1
        squareY += 1
        x = int(math.floor(colWidth / 2))
        y += colWidth

    return encodedText

def detectColumns(image, width):
    x, y = 5, 5
    count = 0

    while x < width:
        if image.get_at((x,y)) == white:
            count += 1
            while image.get_at((x,y)) == white:
                x += 1
                if x >= width:
                    break
        x += 1

    if count == 0: count = 1  # Prevents divison-by-zero errors

    colWidth = int(math.floor(width / count))
    return count, colWidth

def decoder(rgbList):
    finalString = ""
    outerIndex, innerIndex = 3, 0  # Skip over the calibration squares

    while outerIndex < len(rgbList):
        while innerIndex < 3:
            finalString += chr(rgbList[outerIndex][innerIndex])
            innerIndex += 1
        outerIndex += 1
        innerIndex = 0

    clipIndex = finalString.find(chr(3))
    return finalString[:clipIndex]


# MAIN PROGRAM

filename = input("\nPlease enter the file name: ")
if filename[-4:] != ".bmp":
    filename += ".bmp"
chromacode = pygame.image.load(filename)

if checkCode(chromacode) == False:
    print("\n!!!QUALITY CHECK FAIL!!!")
    print("The decoder can't properly read the file you gave.\nSorry!")
    sys.exit()

print ("\nQuality Check Passed!")

rgbList = scanImage(chromacode)

#print ("\nRGBLIST IS:\n", rgbList)  # Used for debugging

print ("\nTHE DECODED MESSAGE IS\n----------------------\n" + decoder(rgbList))
