#build this automaton
# State | Input 0 | Input 1 |
# --------------------------|
#   A   |    E    |    B    |
#   B   |    C    |    E    |
#   C   |    D    |    C    |
#   D   |    E    |    D    |
#   E   |    E    |    E    |
#accepted = {1^g0^k1^p | g = 1 and k = 1 and p ≥ 0}
#because you need a single 1 and a single 0 and as many 1's to keep
#the state at C, which is accepted
import re
import sys

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

def automaton2(sequence):
    # Define state transitions using a dictionary
    transitions = {
        'A': {'0': 'E', '1': 'B'},
        'B': {'0': 'C', '1': 'E'},
        'C': {'0': 'D', '1': 'C'},
        'D': {'0': 'E', '1': 'D'},
        'E': {'0': 'E', '1': 'E'},
    }

    state = 'A'
    for i in sequence:
        state = transitions[state][str(i)] #update the state based on the dictionary

    if state == 'C':
        print('and it succeeds!!')
    else:
        print('but it fails!')

def automaton(list): #first try of the function before trying with dictionary
    state = 'A'
    for i in list:
        if state == 'A' and i == 1:
            state = 'B'
        elif state == 'B' and i == 1:
            state = 'E'
        elif state == 'C' and i == 1:
            state = 'C'
        elif state == 'D' and i == 1:
            state = 'D'
        elif state == 'E' and i == 1:
            state = 'E'
        elif state == 'A' and i == 0:
            state = 'E'
        elif state == 'B' and i == 0:
            state = 'C'
        elif state == 'C' and i == 0:
            state = 'D'
        elif state == 'D' and i == 0:
            state = 'E'
        elif state == 'E' and i == 0:
            state = 'E'
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

