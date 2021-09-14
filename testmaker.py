# import solution from ps
import httpHelper
import dotenv
import colorText

def menu(problemNumber) :
    while True :
        print('Select  : t(Test by test cases in BOJ), c(Change problem), a(Add test case), q(Quit) : ' , end='')
        usr = input()
        if usr in ['q', 'Q', 'quit'] :
            exit(0)
        if usr in ['t', 'T', 'test'] :
            # To do : evaluates user output, and compare it with correct output.
            pass
        if usr in ['c', 'C', 'change'] :
            # To do : change the problem that user solve
            pass
        if usr in ['a', 'A', 'add'] :
            # To do : add test cases!
            pass

        else :
            print('Type correct option...')

if __name__ == '__main__' :
    print('Type problem number : ', end='')
    problemNumber = input()
    URL = 'https://www.acmicpc.net/problem/' + problemNumber
    print('----- Starting to solve ' + problemNumber + ' -----')

    res = httpHelper.getResponse(URL)
    sampleInputs, sampleOutputs = httpHelper.extractSamples(res.text)
    while True : 
        menu(problemNumber)
        
