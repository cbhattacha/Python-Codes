import numpy as np

def listgenerator(n):
    ar = np.random.randint(1,21,n)
    arl = list(ar)
    arl.sort()
    return arl

def checkdivisibility(x):
    out = ''
    for item in x:
        if item%3 == 0:
            out = out + 'flip'
        if item%5 == 0:
            out = out + 'flop'
        if out != '':
            out = out + '\n'
    print(out)


n = int(input('Enter length of the list of numbers to be generated:\n'))
x = listgenerator(n)
print('Generated sorted list : ',x)
checkdivisibility(x)
