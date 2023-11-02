'''
Concatenate automata M1 and M2
Rule: All accepted strings in M1 are concatenated to the accepting strings of M2.
Write a python program to implement M1 + M2. 
1. Ask for sequence of a's and b's followed by sequence of 0's and 1's
2. Verify that there are no other characters
3. Print out whether sequence is accepted or rejected. 
4. Stop when the word 'exit' is typed. 

M1
Start Q1 | Accept q2
     a  |   b
q1  q3  |   q2 
q2  q2  |   q2   
q3  q3  |   q2 

M2
Start A | Accept C or D
    0   |   1
A   C   |   B
B   B   |   D
C   D   |   C
D   D   |   C
'''
import re
import sys

def userinput(): #check user input string 
    usrinput = input('please enter a string of a\'s and b\'s followed by a string of 0s and 1s: ')
    if re.match('^[a-b]+[0-1]+$', usrinput):
        print('the input is accepted...')
        sequence = [i for i in usrinput]
        return sequence
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')

def splitusrinput(sequence):
    m_list = []
    m2_list = []
    for i in sequence:
        if i == 'a' or i == 'b':
            m_list.append(i)
        elif i == '0' or i == '1':
            m2_list.append(i)
    return m_list, m2_list
            

def automaton1(sequence):
    transitions = {
        'q1': {'a': 'q3', 'b': 'q2'},
        'q2': {'a': 'q2', 'b': 'q2'},
        'q3': {'a': 'q3', 'b': 'q2'},
    }

    state = 'q1'
    for i in sequence:
        state = transitions[state][str(i)]
    
    if state == 'q2':
        return True
    else:
        return False

def automaton2(sequence):
    # Define state transitions using a dictionary
    transitions = {
        'A': {'0': 'C', '1': 'B'},
        'B': {'0': 'B', '1': 'D'},
        'C': {'0': 'D', '1': 'C'},
        'D': {'0': 'D', '1': 'C'},
    }

    state = 'A'
    for i in sequence:
        state = transitions[state][str(i)] #update the state based on the dictionary

    if state == 'C' or state == 'D':
        print('and it succeeds!!')
    else:
        print('but it fails!')

if __name__ == '__main__':
    sequence = userinput()
    str1, str2 = splitusrinput(sequence)
    if automaton1(str1) == True:
        automaton2(str2)
    else:
        print('You failed on M1')
