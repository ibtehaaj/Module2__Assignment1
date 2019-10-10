import os
import numpy as np
from PIL import Image

#function for importing, resizing, converting and loading images to numpy array.
def import_convert_load(path,rootDir):
    try:
        list_of_arrays = []
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                img = Image.open(path + fname)
                new_img = img.resize((200,200))
                #new_img.save(path + fname,'jpeg')
                img_arr = np.array(new_img)
                list_of_arrays.append(img_arr)
        array_of_arrays = np.array(list_of_arrays)
        print("---Images resized and loaded successfully---")
        return array_of_arrays
    except:
        print("Sorry! Something went wrong.")


path = 'Photos/'
rootDir = 'Photos'

#calling function to perform the specified tasks
arr = import_convert_load(path,rootDir)
