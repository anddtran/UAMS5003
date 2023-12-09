'''
Consider the Bayesian belief network that classify ﬁsh (see Figure 1). The node A represents the time of the
year and has four values: a1 =Spring, a2 =Summer, a3 =Fall, and a4 =Winter. The node B represents the
location where the ﬁsh was caught and has values b1 =North Atlantic, and b2 = South Atlantic. The node
X represents the type of ﬁsh and has values x1 =Salmon, and x2 =Sea bass. The node C represents the
”lightness” of the ﬁsh and has values c1 =light, c2 =medium, and c3 =dark. Finally, the node D represents
the thickness and has values d1 =wide, and d2 =thin.

(a) Calculate the join probability of the event that the ﬁsh was caught in the Spring, in the South Atlantic,
and the ﬁsh was salmon and was light and thin. (basically multiply all of the individual probabilities)
joint probability of : a1, b2, x1, c1, d2 == 0.016800000000000002


(b) Write a Python program that provides allows the user to give any event as in (a) and returns the joint
probability for that event.'
see code below


P(a)     a1   a2   a3   a4
        0.25 0.25 0.25 0.25

P(b)    b1       b2
        0.6     0.4

P(x|a, b)   P(x1|ai, bj)       P(x2|ai, bj)
a1, b1          0.5                0.5
a2, b1          0.7                0.3
a3, b1          0.6                0.4
a4, b1          0.8                0.2
a1, b2          0.4                0.6
a2, b2          0.1                0.9
a3, b2          0.2                0.8
a4, b2          0.3                0.7

P(c|x)    P(c1|xi) P(c2|xi) P(c3|xi)
x1          0.6       0.2      0.2
x2          0.2       0.3      0.5

P(d|x)    P(d1|xi)    P(d2|xi)
x1          0.3        0.7
x2          0.6        0.4

Table 2: Conditional Probability Tables
Figure 1: The figure shows a and b go into x and x goes into c and d.
'''

import re
import sys

def userinput(): #take the user input for the findings of a, b, x, c, d
    usrinput = input('please enter your choices in order separated by space(s) from [(a1, a2, a3, a4), (b1, b2), (x1, x2), (c1, c2, c3), (d1, d2)]: ')
    if re.match(r'^(a1|a2|a3|a4)\s+(b1|b2)\s+(x1|x2)\s+(c1|c2|c3)\s+(d1|d2)$', usrinput):
        print('The input is accepted...')
        inputuser   = re.split('\s+', usrinput)
        a = inputuser[0]
        b = inputuser[1]
        x = inputuser[2]
        c = inputuser[3]
        d = inputuser[4]
        return a, b, x, c, d
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')


def calculate_joint_probability(a, b, x, c, d):
    # Define the conditional probability tables as a dictionaries
    P_A = {'a1': 0.25, 'a2': 0.25, 'a3': 0.25, 'a4': 0.25}
    P_B = {'b1': 0.6, 'b2': 0.4}
    P_X_given_A_B = {('a1', 'b1'): {'x1': 0.5, 'x2': 0.5},
                    ('a2', 'b1'): {'x1': 0.7, 'x2': 0.3},
                    ('a3', 'b1'): {'x1': 0.6, 'x2': 0.4},
                    ('a4', 'b1'): {'x1': 0.8, 'x2': 0.2},
                    ('a1', 'b2'): {'x1': 0.4, 'x2': 0.6},
                    ('a2', 'b2'): {'x1': 0.1, 'x2': 0.9},
                    ('a3', 'b2'): {'x1': 0.2, 'x2': 0.8},
                    ('a4', 'b2'): {'x1': 0.3, 'x2': 0.7}}
    P_C_given_X = {'x1': {'c1': 0.6, 'c2': 0.2, 'c3': 0.2},
                   'x2': {'c1': 0.2, 'c2': 0.3, 'c3': 0.5}}
    P_D_given_X = {'x1': {'d1': 0.3, 'd2': 0.7},
                   'x2': {'d1': 0.6, 'd2': 0.4}}

    # Calculate joint probability
    joint_prob = P_A[a] * P_B[b] * P_X_given_A_B[(a, b)][x] * P_C_given_X[x][c] * P_D_given_X[x][d]
    return joint_prob

if __name__ == '__main__':
    print('The node A represents the time of the year and has four values: a1 =Spring, a2 =Summer, a3 =Fall, and a4 =Winter. \n')
    print('The node B represents the location where the ﬁsh was caught and has values b1 =North Atlantic, and b2 = South Atlantic. \n')
    print('The node X represents the type of ﬁsh and has values x1 =Salmon, and x2 =Sea bass. \n')
    print('The node C represents the ”lightness” of the ﬁsh and has values c1 =light, c2 =medium, and c3 =dark.  \n')
    print('Finally, the node D represents the thickness and has values d1 =wide, and d2 =thin. \n')  
    a, b, x, c, d = userinput()
    print(f"Joint Probability: {calculate_joint_probability(a, b, x, c, d)}")
