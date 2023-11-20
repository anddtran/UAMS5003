'''
(a) Find out what is the missing value. missing value = 0.4 because it needs to add up to 1 and the other value is 0.6

(b) Write down the transition probability matrix (you may consider writing it down in Python as a list of lists). 
    
Matrix is here, built a dictionary with the transition probabilities to use numpy to build a matrix for calculation. 
|      |   A  |   B  |   C  |   D  |   E  |

|  A   |  0.0 | 0.3  | 0.0  | 0.0  | 0.7  |

|  B   |  0.0 | 0.0  | 0.4  | 0.0  | 0.6  |

|  C   |  0.4 | 0.0  | 0.3  | 0.0  | 0.3  |

|  D   |  0.0 | 0.0  | 0.0  | 0.3  | 0.7  |

|  E   |  0.0 | 0.0  | 0.9  | 0.0  | 0.1  |


(c) If the initial probability distribution of the states is πππ(0) = (0.3, 0.2, 0.1, 0.3, 0.1), 
    what is the probability distribution of the states after the Markov model runs 15 steps?
    gonna build a few functions to do this: see below
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
    usrinput = input('please enter the number of steps: ')
    if usrinput.isdigit():
        print('the input is accepted...')
        return int(usrinput)
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')


def markov_states(transitions):
    states = list(transitions.keys()) #get a list of states
    matrix = np.zeros((len(states), len(states))) 
    #np.zeros initializes a matrix with zero value and length of matrix defined by length of states

    #put values in the matrix defined by the dictionary, with 0 as default
    for i, state in enumerate(states): #for each index i in states, and the state (big key)
        for j, next_state in enumerate(states): # inner loop - for each index j and its value (small key) next_state, get the transition probability
            matrix[i, j] = transitions[state].get(next_state, 0) # put the probability in the matrix at i and j
    
    return matrix

def steps_calc(transition_matrix, initial_distribution, steps):
    #Calculate the state distribution after a certain number of steps. linalg.matrix_power() takes the transition matrix to the power of steps 
    #and then the @ multiplies it times the initial_distribution
    return np.linalg.matrix_power(transition_matrix, steps) @ initial_distribution


if __name__ == '__main__':
    # Create the transition matrix
    transition_matrix = markov_states(transitions)
    steps = userinput()

    # Calculate the distribution after x steps
    distribution_after_steps = steps_calc(transition_matrix, initial_distribution, steps)

    print(f"State distribution after {steps} steps:", distribution_after_steps)
