# import solution from ps
import httpHelper
import dotenv
import colorText

def menu(problemNumber) :
    print('Select  : t(test by test cases in BOJ), s(submit (not implemented yet)), q(quit) : ' , end='')
    usr = input()
    if usr in ['q', 'Q', 'quit'] :
        exit(0)
    if usr in ['t', 'T', 'test'] :
        test()


if __name__ == '__main__' :
    print('Type problem number : ', end='')
    problemNumber = input()
    URL = 'https://www.acmicpc.net/problem/' + problemNumber
    print('----- Starting to solve ' + problemNumber + ' -----')

    res = httpHelper.getResponse(URL)
    sampleInputs, sampleOutputs = httpHelper.extractSamples(res.text)
    while True : 
        
