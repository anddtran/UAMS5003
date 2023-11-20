'''
(a) Find out what is the missing value. missing value = 0.4
(b) Write down the transition probability matrix (you may consider writing it down in Python as a list of lists). Check the dictionary for the markov probabilty matrix
(c) If the initial probability distribution of the states is πππ(0) = (0.3, 0.2, 0.1, 0.3, 0.1), what is the probability distribu-
tion of the states after the Markov model runs 15 steps.

'''


import re
import sys
import numpy as np

# Define state transitions using a dictionary
transitions = {
    'A': {'B': 0.3, 'E': 0.7},
    'B': {'C': 0.4, 'E': 0.6},
    'C': {'A': 0.4, 'C': 0.3, 'E': 0.3},
    'D': {'D': 0.3, 'E': 0.7},
    'E': {'C': 0.9, 'E': 0.1},
}

initial_distribution = np.array([0.3, 0.2, 0.1, 0.3, 0.1])

def userinput(): #check user input string to only allow ones and zeros, then return a list
    usrinput = input('please enter a string of zeros and ones: ')
    if usrinput.isdigit() and int(usrinput) >= 0 and re.match('^[0-1]*$', usrinput):
        print('the input is accepted...')
        sequence = [int(i) for i in usrinput]
        return sequence
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')


def markov(sequence):
    

    state = 'A'
    for i in sequence:
        state = transitions[state][str(i)] #update the state based on the dictionary

    if state == 'C':
        print('and it succeeds!!')
    else:
        print('but it fails!')


if __name__ == '__main__':
    while True:
        try:
            sequence = userinput()
            automaton2(sequence)
            break
        except SystemExit:
            print('ok you are done')
            break