# Author: Andrea Aviles
# Purpose: get grayscale values of an image
# Date: 9/7/2019
# Version 1.1
# Added pause to display image size

import sys
import os

file_name = input("Enter File Name: ")
#print(file_name)

# lets see if the file exist
if os.path.isfile(file_name) and os.access(file_name, os.R_OK):
    #print("File exists")
    
    # lets separate the file_name from the extension, cosita is the file name without the extension
    cosita = os.path.splitext(file_name)[0]
    #print(cosita)
	
else:
    #if the file does not exist, lets leave
    print("Cannot open file " + file_name)
    sys.exit()

# load image library
from PIL import Image

# loads file into im variable
im = Image.open(file_name)

# loads image into pix variable
pix = im.load()

# im.size is the image array with 2 values, width and height of the image
xcount=im.size[0]
ycount=im.size[1]

print("This image is", xcount, "x", ycount, "or", xcount*ycount, "pixels")
wait = input("Press  <Enter> to continue")

# lets loop to get rgb values
print("RGB Values")
for y in range(ycount):
 for x in range(xcount):
  # get the rgb value for each pixel
  myrgb = pix[x,y]
  print("Position ",x,y,"R",myrgb[0], "B",myrgb[1], "G",myrgb[2])

# lets loop again to get grayscale values
print("\n") # new line
print("Grayscale Values")
for y in range(ycount):
 for x in range(xcount):
  # get the gray value for each pixel
  mygray = pix[x,y]
  # use weighted average as red is more intense
  print("Position ",x,y, round(mygray[0]*0.3+mygray[1]*0.59+mygray[2]*0.11))
  
 