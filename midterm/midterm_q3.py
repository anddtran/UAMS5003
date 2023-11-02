'''
Compose a Python program that asks the user for two non-negative integers (m, n), and a number p ∈ (0, 1). The
program will build a Boolean matrix A = (ars) of type m × n in which the ars is T with probability p and F with
probability 1 − p. For reproducibility, set the seed of your random number generator to 500323.
'''

import re
import sys
import random 
random.seed(500323)

def userinput(): #check user input string to only allow ones and zeros, then return a list
    usrinput = input('please enter two non-negative integers and a number between 0-1 separated by spaces: ')
    if re.match('^(\d+)\s*(\d+)\s*(0(\.\d*)?|1(\.0*)?)$', usrinput):
        print('the input is accepted...')
        indigit = re.split('\s+', usrinput)
        m = int(indigit[0])
        n = int(indigit[1])
        p = float(indigit[2])
        return m, n, p
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')


def t_or_f(p):
    if random.random() < p:
        return 'T'
    else:
        return 'F'

def matrix(m, n, p):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(t_or_f(p))
        matrix.append(row)
    return matrix

def draw(matrix):
    for row in matrix:
        print(row)

if __name__ == '__main__':
    m, n, p = userinput()
    matrix = matrix(m, n, p)
    draw(matrix)