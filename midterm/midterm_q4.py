'''
Use the insurance.csv data set to ﬁt a multi-linear regression model to predict the charges based on the variables
age and bmi.
(a) If you select patients on the northwest region only, what are the values of your β’s.
(b) What is the R2 of your model?
(c) If your bmi increases by 1 unit while keeping the age constant, what would be the expected increase in charges
according to your model?
(d) Predict the cost for a person in this region whose age is 45.5 and bmi is 24.9.
(e) Now consider another region (e.g., northeast) and describe changes in your previous prediction (if any).
2
'''
#import modules
import pandas as pd
from sklearn.linear_model import LinearRegression
import re

#filepath = '/Users/andrewtran/repos/5003/midterm/insurance.csv'
filepath = 'C:\\Users\\anddt\\OneDrive\\Documents\\GitHub\\UAMS5003\\midterm\\insurance.csv'
df = pd.read_csv(filepath)
print(df.head(), '\n')

#model based on all regions
independent = ['age', 'bmi']
X = df[independent]
y = df.charges
reg = LinearRegression().fit(X,y)
coefficients = reg.coef_
intercept = reg.intercept_
print('Model for all regions:')
print('The values of the betas are below: ')
print('Coefficients: ', coefficients)
print('Intercept: ', intercept, '\n')
print(f'If age stays the same, the charges increase by {coefficients[1]} for an increase in 1 by BMI.')
R2 = reg.score(X, y)
print('R2: ', R2)
print('\n\n')


# selected region model
print('Model for user selected region:')
#functions for region selection and age/bmi selection
def pick_region():
    usrinput = input('Please select a region from northwest, northeast, southwest, southeast: ')
    usrinput = usrinput.lower().strip()
    if re.match(r'^(northwest|northeast|southwest|southeast)$', usrinput):
        print(f'you selected: {usrinput}')
        return usrinput
    else:
        print('not a region to select from')

def variables():
    age = input('Please input an age: ')
    bmi = input('Please enter a BMI: ')
    if re.match(r'^\d+(\.\d+)?$', age) and re.match(r'^\d+(\.\d+)?$', bmi):
        float(age)
        float(bmi)
        test_df = pd.DataFrame([[age, bmi]], columns=['age', 'bmi'])
        return test_df
    else:
        print('inputs are not valid!')

#model based on user selection
filtered_df = df[df['region'] == pick_region()]
independent = ['age', 'bmi']
W = filtered_df[independent]
z = filtered_df.charges
region_reg = LinearRegression().fit(W,z)

coefficients = region_reg.coef_
intercept = region_reg.intercept_
print('The values of the betas are below: ')
print('Coefficients: ', coefficients)
print('Intercept: ', intercept, '\n')
print(f'If age stays the same, the charges increase by {coefficients[1]} for an increase in 1 by BMI.')
R2 = region_reg.score(W, z)
print('R2: ', R2)

test_df = variables()
chargepredict = region_reg.predict(test_df)[0]
print(f'The charge prediction for your {test_df.age[0]} and {test_df.bmi[0]} is {chargepredict}')