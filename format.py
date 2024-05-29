#!/bin/python
import os
from pathlib import Path
from PIL import Image
from rembg import remove, new_session
from sys import argv, stdout

def squareImage(image):
    # Get the bounding box
    bbox = image.getbbox()
    cropped = image.crop(bbox)
    
    # Determine width and height of the bounding box
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    
    # Find the maximum dimension
    length = max(width, height)
    padLeft = (length - width) // 2
    if (length - width) % 2 == 1:
        padLeft -= 1
    padTop = (length - height) // 2
    if (length - height) % 2 == 1:
        padTop -= 1
    
    # Create a new image with the new size and a transparent background
    new_image = Image.new("RGBA", (length, length), (0, 0, 0, 0))
    
    # Paste the original image onto the new image with padding
    new_image.paste(cropped, (padLeft, padTop))

    return new_image

def formatImage(targetSize, imagePath, savePath):
    image = Image.open(imagePath)
    formatted = squareImage(remove(image))
    formatted.thumbnail((targetSize, targetSize))
    formatted.save(savePath)
    return

def getFiles(dirPath):
    extensions = ['.png', '.jpg', '.jpeg', '.webp']
    file_list = []
    prefix = dirPath + '/'
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            for extension in extensions:
                if file.lower().endswith(extension):
                    path = root + '/' + file
                    shortened = path.removeprefix(prefix)
                    file_list.append(shortened)
                    break
    return file_list

# Usage 

session = new_session()
targetSize = int(argv[1])
fromDir = argv[2].strip('/')
toDir = argv[3].strip('/')

files = getFiles(fromDir)
for i, file in enumerate(files):
    fromPath = fromDir + '/' + file
    toPath = toDir + '/' + file.rsplit('.',1)[0] + '.png'
    parentDir = toPath.rsplit('/', 1)[0]
    # Print completion percentage
    stdout.write('\33[2K\rFormatting image %d/%d - %s' % (i, len(files),
                                                    toPath))
    Path(parentDir).mkdir(parents=True, exist_ok=True)
    formatImage(targetSize, fromPath, toPath)
