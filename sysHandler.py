import os
import subprocess

# cmd="ls"
# result = subprocess.check_output(cmd, shell=True)
# print(result.decode('utf-8'))


def interprete(problem, interpreter, inputs) :
    outputs = []
    for i in inputs :
        cmd = interpreter + ' ' + str(problem) + '.py'
        result = subprocess.check_output(cmd, input=i.encode(),shell=True)
        outputs.append(result.decode('utf-8'))
    return outputs

if __name__ == '__main__' :
    outputs = interprete(0, '~/opt/anaconda3/bin/python', ['Well working!!', 'Thank you', 'How about newline?\nIt should not appear...']) 
    print(outputs) # ['Well working!!\n', 'Thank you\n', 'How about newline?\n']