import os
import shutil
import glob

def cleanOutput():
    files = glob.glob('./output/*')
    for f in files:
        os.remove(f)

def copyInput():
    fileNames = os.listdir("./input")
    fileName = fileNames[0]
    shutil.copyfile("./input/"+fileName,"./output/"+fileName)

cleanOutput()
copyInput()
