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

import pandas as pd
import sklearn

df = pd.read_csv('/Users/andrewtran/repos/5003/midterm/insurance.csv')
print(df.head())