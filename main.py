import os
import shutil
import glob
import subprocess

def cleanDirectory(dir):
    files = glob.glob(dir)
    for f in files:
        os.remove(f)

def copyInput():
    fileNames = os.listdir("./input")
    inputName = fileNames[0]
    inputPath = "./input/"+inputName
    outputPath = "./output/"+inputName
    shutil.copyfile(inputPath,outputPath)
    return [inputPath,outputPath]



def getCodeFilePaths(dir): 
    arr = []
    for root, subdirs, files in os.walk(dir):
        if len(files) > 0:
            for file in files:
                arr.append(root[7:]+"/"+file)
    return arr

if not os.path.exists('output'):
    os.makedirs('output')

cleanDirectory('./output/*')
cleanDirectory('./temp/*')

paths = copyInput()
inputPath = paths[0]
outputPath = paths[1]

codeFilePaths = getCodeFilePaths("./code")

os.chdir("./code")
javaProcess = ("javac -cp ../"+inputPath+" -d ../temp").split(" ") + codeFilePaths

subprocess.call( javaProcess )
os.chdir("../")

tempFilePaths = getCodeFilePaths("./temp")

replaceNum = 0

for tempFile in tempFilePaths:
    subprocess.call(["jar", "uf",outputPath,"-C","temp",tempFile])
    print("Overriding or adding: "+tempFile)
    replaceNum += 1

print("Process complete")
print("Input file: "+inputPath)
print("Output file: "+outputPath)
print("Number of files replaced or added: "+str(replaceNum))