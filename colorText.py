def printDarkGrey(text, end='\n') :
    print('\033[1;30;40m' + text + '\033[0m', end)

def printRed(text, end='\n') :
    print('\033[1;31;40m' + text + '\033[0m', end)

def printGreen(text, end='\n') :
    print('\033[1;32;40m' + text + '\033[0m', end)

def printYellow(text, end='\n') :
    print('\033[1;33;40m' + text + '\033[0m', end)

def printBlue(text, end='\n') :
    print('\033[1;34;40m' + text + '\033[0m', end)


if __name__ == '__main__' :
    printRed('is it red???', end='')