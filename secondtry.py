
from fileinput import filename
from turtle import right
from PIL import Image, ImageFilter, ImageDraw, ImageFont

import os




def getCrop(im):
    sizes = im.size
    X = sizes[0]
    Y = sizes[1]
    #print("length is {} pixels and height is {} pixels".format(X, Y))
    midX = int(X/2)
    midY = int(Y/2)
    #print("mid X is {} and mid Y is {}".format(midX, midY))
    print(im.format, im.mode, im.size)
    left = getLeftSide(im)
    top = getTopEdge(im)
    right = getRightSide(im)
    bot = getBottomEdge(im)
    if left == None and right != None:
        left = right - 1700
    if right == None and left != None:
        right = left + 1700
    if top == None and bot != None:
        top = bot - 1000
    if bot == None and top != None:
        bot = top + 1000
    print("left is {}, top is {}, right is {}, bot is {}".format(left, top, right, bot))
    if left == None or right == None or top == None or bot == None:
        print("there is a none, skip")
        return False, im
    crop = im.crop((left, top, right, bot))
    #crop.show()
    return True, crop

def getLeftSide(im):
    print("finding left side")
    error = ["left side error"]
    sizes = im.size
    y = int(int(sizes[1]) / 2)
    blackCount = 0
    lastX = 0
    for i in range(0, int(int(sizes[0]) / 2)):
        value = im.getpixel((i, y))
        if value <= 30:
            lastX = i
            blackCount += 1
            s = "found black pixel at X = {}, black count is {}".format(lastX, blackCount)
            error.append(s)
        else: 
            if blackCount > 1:
                print("found left black line at x = {} and y = {}".format(lastX, y))
                #draw = ImageDraw.Draw(im)
                #draw.line((lastX, 0, lastX, Y))
                #im.show()
                return lastX
            lastX = 0
            blackCount = 0
    print("cannot find left side?\n")
    print(error)

def getRightSide(im):
    print("finding right side")
    error = ["right side error"]
    sizes = im.size
    y = int(int(sizes[1]) / 2)
    blackCount = 0
    lastX = 0
    for i in range(int(sizes[0])-1, int(int(sizes[0]) / 2), -1):
        value = im.getpixel((i, y))
        if value <= 30:
            lastX = i
            blackCount += 1
            s = "found black pixel at X = {}, black count is {}".format(lastX, blackCount)
            error.append(s)
        else: 
            if blackCount > 1:
                print("found right black line at x = {} and y = {}".format(lastX, y))
                #draw = ImageDraw.Draw(im)
                #draw.line((lastX, 0, lastX, Y))
                #im.show()
                return lastX
            lastX = 0
            blackCount = 0
    print("cannot find right side?\n")
    print(error)

def getBottomEdge(im):
    print("finding bottom edge")
    error = ["bottom error"]
    sizes = im.size
    x = int(int(sizes[0]) / 2)
    blackCount = 0
    lastY = 0
    for i in range(int(sizes[1])-1, int(int(sizes[1]) / 2), -1):
        value = im.getpixel((x, i))
        if value <= 30:
            lastY = i
            blackCount += 1
            s = "found black pixel at Y = {}, black count is {}".format(lastY, blackCount)
            error.append(s)
        else: 
            if blackCount > 1:
                print("found bottom black line at x = {} and y = {}".format(x, lastY))
                #draw = ImageDraw.Draw(im)
                #draw.line((0, lastY, int(sizes[0]) - 1, lastY))
                #im.show()
                return lastY
            lastY = 0
            blackCount = 0
    print("cannot find bottom edge?")
    print(error)

def getTopEdge(im):
    print("finding top edge")
    error = ["top edge error"]
    sizes = im.size
    x = int(int(sizes[0]) / 2)
    blackCount = 0
    lastY = 0
    for i in range(0, int(int(sizes[1]) / 2)):
        value = im.getpixel((x, i))
        if value <= 30:
            lastY = i
            blackCount += 1
            s = "found black pixel at Y = {}, black count is {}".format(lastY, blackCount)
            error.append(s) 
        else: 
            if blackCount > 1:
                print("found top black line at x = {} and y = {}".format(x, lastY))
                #draw = ImageDraw.Draw(im)
                #draw.line((0, lastY, X, lastY))
                #im.show()
                return lastY
            lastY = 0
            blackCount = 0
    print("cannot find top edge?\n")
    print(error)
        

directory = os.fsencode(r"C:\Users\chris\Desktop\images\Processed")


for folder in os.listdir(directory):
     folderName = os.fsdecode(folder)
     #print(folderName)
     for file in os.listdir(r"C:\Users\chris\Desktop\images\Processed\\" + folderName):
        fileName = os.fsdecode(file)
        if "cropped" in fileName:
            print("skipping")
            continue
        print("now cropping " + fileName)
        im = Image.open(r"C:\Users\chris\Desktop\images\Processed\\" + folderName + "\\" + fileName)
        im = im.convert("L")
        cropPassOrFail, crop = getCrop(im)
        if cropPassOrFail == True:
            crop.save(r"C:\Users\chris\Desktop\images\Processed\\" + folderName + "\\" + "cropped" + file)
        elif cropPassOrFail == False:
            crop.save(r"C:\Users\chris\Desktop\images\Processed\\" + folderName + "\\" + "cropped(fail)" + file)
        

# im = Image.open(r"C:\Users\chris\Desktop\images\Processed\\" + "元朝秘史續集卷一" + "\\" + "元朝秘史續集卷一 2.png")
# crop = getCrop(im)
# crop.show()