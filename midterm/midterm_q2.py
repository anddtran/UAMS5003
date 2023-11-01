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

def m1(mstring):


def m2(m2string):