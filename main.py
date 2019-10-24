import os
import numpy as np
from PIL import Image


#function for catching files from given directory
def get_files(path):
    try:
        for dirName, subdirList, fileList in os.walk(path):
            pass
        return fileList
    except:
        print("Directory not found! Please make sure the 'Photos' directory exists in the same directory.")



#function for generating 4D array of specified size
def create_array(files):
    try:
        no_of_files = len(files)
        return np.empty((no_of_files,200,200,3))
    except:
        print("Something went wrong!")


# function for resizing and saving images
def resize_image(fileList, path):
    try:
        for file in fileList:
            img = Image.open(path + "/" + file)
            new_img = img.resize((200,200))
            new_img.save("Photos" + "/" + file)
    except:
        print("Sorry! Something went wrong :-(")


#function for converting images to numpy array
def convert_to_array(files, array, path):
    counter = 0
    try:
        for file in files:
            img = Image.open(path + "/" + file)
            arr = np.array(img)
            array[counter] = arr
            counter += 1
        return array
    except:
        print("Something went wrong! :-(")


# main function for calling all the above functions
def main():
    try:
        path = "Photos"
        fileList = get_files(path)
        image_array = create_array(fileList)
        resize_image(fileList, path)
        print("Congratulations! Images successfully resized and converted to numpy array! :-)")
        return convert_to_array(fileList,image_array,path)
    except:
        print("Something went wrong! :-(")

array = main()

