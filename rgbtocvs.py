# Name: rgbtocvs
# Author: Andrea Aviles
# Purpose: export rbg values to cvs
# Date: 9/10/2019
# Version 1.0
# first version

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
# if we want grayscale we shoulsd used round(pix[0]*0.3+pix[1]*0.59+pix[2]*0.11))

print("Exporting RGB values to CSV")

# create a file with the same name as the image with .cvs as extension
f = open(cosita+".csv", "w")

# write header line
f.write("R,G,B\n")

for y in range(ycount):
 for x in range(xcount):
   r = pix[x,y][0]
   g = pix[x,y][1]
   b = pix[x,y][2]
   # write the row to cvs
   f.write('{0},{1},{2}\n'.format(r,g,b))

print("Export completed")
# close the file
f.close()
