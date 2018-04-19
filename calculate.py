import os
import argparse

def resultInFile(name, procedure) :

    res = 0 if procedure == 'add' else 1

    with open(name, 'r') as file:
        numbers = file.readline().split(' ')

    if '' in numbers:
        numbers.remove('')

    for number in numbers:
        if procedure == 'mul':
            res*=int(number)
        else:
            res+=int(number)

    return res

def resultInFolder(path, procedure = None) :

    files = os.listdir(path)

    res = 0 if procedure == 'add' else 1

    for file in files:

        if (file == 'add' or file == 'mul') and os.listdir(os.path.join(path, file)):
            if procedure == 'add':
                res += resultInFolder(os.path.join(path, file), file)
            else:
                res *= resultInFolder(os.path.join(path, file), file)

        if file.endswith('.txt'):
            if procedure == 'add':
                res += resultInFile(os.path.join(path, file), 'add')
            else:
                res *= resultInFile(os.path.join(path, file), 'mul')
    return res

parser = argparse.ArgumentParser()
parser.add_argument('folder')

arguments = parser.parse_args()
print(resultInFolder(os.getcwd(), arguments.folder))

