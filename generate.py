import os
import random
import shutil

def generateFolder(procedure):
    if procedure == "mul":
        os.mkdir("mul")
        os.chdir("mul")
    else:
        os.mkdir("add")
        os.chdir("add")

    generateFiles()
    generate()

def generateFiles(end = 0):

    if end:
        numberOfFiles = random.randint(1, 3)
    else:
        numberOfFiles = random.randint(0, 3)

    for i in range(0, numberOfFiles):
        with open('file' + str(i) + '.txt', 'a') as file:
            for j in range(0, random.randint(1, 6)):
                file.write(str(random.randint(-10, 10) ) + ' ')

def generate(start = 0):

    global levelCounter
    levelCounter +=1

    if start:
        numberOfFolders = 1
    else:
        numberOfFolders = random.randint(0,2)

    if numberOfFolders == 0 or levelCounter > maxLevel:
        generateFiles(1)
        return
    elif numberOfFolders == 1:
        procedure = "mul" if random.randint(0,1) else "add"
        generateFolder(procedure)
    else:
        directory = os.getcwd()
        generateFolder("mul")
        os.chdir(directory)
        generateFolder("add")

    levelCounter -= 1

if os.path.exists('add'):
    shutil.rmtree('add')
if os.path.exists('mul'):
    shutil.rmtree('mul')

levelCounter = 0
maxLevel = random.randint(1, 10)
generate(1)
