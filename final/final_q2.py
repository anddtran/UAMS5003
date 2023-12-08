'''
A survey was conducted about the reliability of a new test for COVID-19. A precise medical testing classified
the patients as healthy or sick and is encoded in the random variable Status. The area where the survey was
conducted has 10% COVID positive prevalence during the survey time. The output of the test is encoded
with the random variable X can have three outcomes: positive, negative, and inconclusive.
Status                     X
          Positive    Negative   Inconclusive
Healthy     0.08        0.80        0.12
Sick        0.82        0.09        0.09
Table 1: Distribution of the prediction of new test
(a) Using Bayes’ theorem. Calculate P (Status = Healthy|X = Positive).
(b) Implement a Python program in which the user provides the prior prevalence distribution, and returns
the posterior probability P (Status = Healthy|X = x) for each value of x.
'''
import re
import sys

def userinput(): #check user input string to only allow digits and value < 1, then return a list
    usrinput = input('please enter two prior distributions for healthy and sick in that order separated by space(s): ')
    if re.match(r'^(0(\.\d+)?|1(\.0+)?)\s+(0(\.\d+)?|1(\.0+)?)$', usrinput):
        print('The input is accepted...')
        indigit = re.split('\s+', usrinput)
        m = float(indigit[0])
        n = float(indigit[1])
        return m, n
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')

def get_x():
    usrinput = input('Please select status (healthy or sick) and x (capitalized P or N or I) separated by spaces: ')
    if re.match(r'^(healthy|sick)\s+(P|N|I)$', usrinput):
        selection = re.split('\s+', usrinput)
        return selection[0], selection[1]
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('invalid inputs')

def post_prob(m, n, status, x):
    distribution = {
        'healthy' : {'P': 0.08, 'N' : 0.80, 'I' : 0.12}, 
        'sick' : {'P': 0.82, 'N' : 0.09, 'I' : 0.09}, 
        }
    priors = {'healthy': m, 'sick': n}
    total_prob = sum(distribution[status][x] * priors[status] for status in distribution)
    probability = distribution[status][x] * priors[status] / total_prob
    return probability

if __name__ == '__main__':
    m, n = userinput()
    status, x = get_x()
    probability = post_prob(m, n, status, x)
    print(f'The posterior probability for status {status} given x {x} is: {probability}')


'''
To calculate (a), use the P(healthy) = 0.9 and P(sick) = 0.1 for the prior distributions. The result == 0.4675324675324675
For (b), the functions allow us to select x for healthy or sick to calculate the posterior probability
'''