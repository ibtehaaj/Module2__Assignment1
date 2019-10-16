import os
import numpy as np
from PIL import Image

#function for grabbing files from the directory
def get_files(path):
    try:
        for dirName, subdirList, fileList in os.walk(rootDir):
            pass
        return fileList
    except:
        print("Directory not found! Please make sure the 'Photos' directory exists in the same directory.")

#function for importing, resizing, converting and loading images to numpy array.
def import_convert_load(rootDir):
    try:
        counter = 0
        #pre-initialized numpy array reserved for images(converted to arrays).
        fileList = get_files(rootDir)
        no_of_files = len(fileList)
        array_of_images = np.zeros((no_of_files,200,200,3))
        for fname in fileList:
            img = Image.open(rootDir + fname)
            new_img = img.resize((200,200))
            img_arr = np.array(new_img)
            array_of_images[counter] = img_arr
            counter += 1
        print("---Images resized and loaded successfully---")
        return array_of_images
    except:
        print("Sorry! Something went wrong.")





rootDir = 'Photos/'

#calling function to perform the specified tasks
arr = import_convert_load(rootDir)
shape = arr.shape
print("Shape:",shape)
