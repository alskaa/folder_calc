import os

def resultInFile(name, procedure) :

    res = 0 if procedure == 'add' else 1
    file = open(name, 'r')
    numbers = file.readline().split(' ')

    if '' in numbers:
        numbers.remove('')

    for number in numbers:
        if procedure == 'mul':
            res*=int(number)
        else:
            res+=int(number)

    file.close()
    return res

def resultInFolder(path, procedure = None) :

    files = os.listdir(path)

    res = 0 if procedure == 'add' else 1

    for file in files:

        if file == 'add' or file == 'mul':
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

mainDirectory = os.getcwd()
result = resultInFolder(mainDirectory, os.listdir(mainDirectory)[0])
print(result)

