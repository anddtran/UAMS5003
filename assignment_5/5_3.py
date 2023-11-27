'''
3. Using the survey.txt file split the rows into two files (say survey1.txt and survey2.txt) with around 50% of the
              total rows each following this strategy:
    Strategy: Randomly select (with equal probability) which row goes into each file.
              Use bnlearn to answer the following questions
(a) Find the best DAG structure that fits surveyi.txt (i = 1, 2).
(b) Print out each DAG. Describe the differences (if any)
    --It looks like due to the way I shuffle the rows randomly in the code, I get different DAGs due to new survey1 and survey2 each time I run the whole code. 
'''

import pandas as pd
import random
import bnlearn as bn

# Load the data from survey.txt, using sep since it is space separated instead of comma, and header = 0 for the first row as column names
data = pd.read_csv('C:\\Users\\anddt\\OneDrive\\Documents\\GitHub\\UAMS5003\\assignment_5\\survey.txt', sep='\s+', header=0)
print(data.columns)
# Randomly shuffle the rows, frac=1 takes all rows, drop=True drops the original index column
shuffled_data = data.sample(frac=1).reset_index(drop=True)

# Split the data into two halves, without knowing the actual length of the file
midpoint = len(shuffled_data) // 2
survey1 = shuffled_data.iloc[:midpoint, :]
survey2 = shuffled_data.iloc[midpoint:, :]

# Save to new files
survey1.to_csv('survey1.txt', index=False)
survey2.to_csv('survey2.txt', index=False)

# Load the datasets
data1 = pd.read_csv('survey1.txt')
data2 = pd.read_csv('survey2.txt')


# Learn the structure
dag1 = bn.structure_learning.fit(data1)
dag2 = bn.structure_learning.fit(data2)
dagcomplete = bn.structure_learning.fit(data)

# Print out the DAGs
print("DAG for survey1.txt:")
print(dag1['adjmat'])

print("\nDAG for survey2.txt:")
print(dag2['adjmat'])

print("\nDAG for survey.txt:")
print(dagcomplete['adjmat'])


'''
Output:

DAG for survey1.txt:
target            Age  R(size?)  Education  Occupation    Sex  Transportation
source
Age             False     False      False       False  False           False
R(size?)        False     False       True       False  False            True
Education        True     False      False        True   True           False
Occupation      False     False      False       False  False           False
Sex             False     False      False       False  False           False
Transportation  False     False      False       False  False           False

DAG for survey2.txt:
target            Age  R(size?)  Education  Occupation    Sex  Transportation
source
Age             False     False      False       False  False           False
R(size?)        False     False      False       False  False           False
Education       False     False      False       False  False           False
Occupation      False     False      False       False  False           False
Sex             False     False      False       False  False           False
Transportation  False     False      False       False  False           False

DAG for survey.txt:
target            Age  R(size?)  Education  Occupation    Sex  Transportation
source
Age             False     False      False       False  False           False
R(size?)        False     False       True       False  False            True
Education        True     False      False        True   True           False
Occupation      False     False      False       False  False           False
Sex             False     False      False       False  False           False
Transportation  False     False      False       False  False           False
'''