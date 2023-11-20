'''
a) the prior distribution is: 0.2 for 1st grade, 0.5 for 6th grade, 0.3 for 11th grade

b) P(theta = '6th grade' | S = 'M') = (P(S|theta) x P(theta)) / P(S = 'M') = (0.1 x 0.5) / ((0.3×0.2)+(0.1×0.5)+(0.3×0.3)) = 0.25 or 25%

c) Implement a Python program in which the user provides the prior distribution, and returns the posterior probability
P (θ = ”11th Grade”|S = s) for each value of s

            M   E   S
1st Grade  0.3 0.6 0.1
6th Grade  0.1 0.3 0.6
11th Grade 0.3 0.6 0.1
Table 1: Favorite Subjects per grade distribution
'''
import re
import sys

def userinput(): #check user input string to only allow ones and zeros, then return a list
    usrinput = input('please enter three prior distributions for 1st, 6th, and 11th grade in that order separated by space(s): ')
    if re.match(r'^(0(\.\d+)?|1(\.0+)?)\s+(0(\.\d+)?|1(\.0+)?)\s+(0(\.\d+)?|1(\.0+)?)$', usrinput):
        print('The input is accepted...')
        indigit = re.split('\s+', usrinput)
        m = float(indigit[0])
        n = float(indigit[1])
        o = float(indigit[2])
        return m, n, o
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')

def get_grade_subject():
    usrinput = input('Please select a grade from 1, 6, 11 and a subject from M, E, S separated by spaces: ')
    if re.match(r'^(1|6|11)\s*(M|E|S)$', usrinput):
        selection = re.split('\s+', usrinput)
        return selection[0], selection[1]
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('invalid inputs')

def post_prob(m, n, o, grade, subject):
    distribution = {
        '1' : {'M': 0.3, 'E' : 0.6, 'S' : 0.1}, 
        '6' : {'M': 0.1, 'E' : 0.3, 'S' : 0.6}, 
        '11' : {'M': 0.3, 'E' : 0.6, 'S' : 0.1}
        }
    priors = {'1': m, '6': n, '11': o}
    total_prob_subject = sum(distribution[grade][subject] * priors[grade] for grade in distribution)
    probability = distribution[grade][subject] * priors[grade] / total_prob_subject
    return probability

if __name__ == '__main__':
    m, n, o = userinput()
    grade, subject = get_grade_subject()
    probability = post_prob(m, n, o, grade, subject)
    print(f'The posterior probability for grade {grade} given subject {subject} is: {probability}')