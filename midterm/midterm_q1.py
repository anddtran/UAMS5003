''' Develop a program in Python that will read the ﬁle sequences.txt (provided with this assignment), and perform the following tasks
    (a) It ﬁnds the number of occurrences of one or more N’s for each line using regular expressions.

    (b) It ﬁnds the number of periods in the whole sequence (i.e. without break lines), and prints out their type.
            Namely, it prints out
            There are x ’.’
            There are y ’..’
            There are z ’...’
            ...

    (c) It ﬁnds out the number of occurrences of CG’s in the whole sequence, and prints out the number or such occurrences.

    (d) The program will ﬁnally generate a ﬁle named sequences CG.txt similar to the sequences.txt but have CG’s
    underscored (i.e., if the original ﬁle has ACGT the new ﬁle will have ACGT instead) '''

import regex as re
import os

file_path = '/Users/andrewtran/repos/5003/midterm/sq.txt'
#file_path = 'C:\\Users\\anddt\\OneDrive\\Documents\\GitHub\\UAMS5003\\midterm\\sq.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        sequence = file.read()
        sequence2 = sequence.replace('\n', '')

# print(sequence2) #used to check the read
nmatches = re.findall(r'N+', sequence2)
dotmatches = re.findall(r'\.+', sequence2)
cgmatches = re.findall(r'CG', sequence2)

print(f'There are {len(nmatches)} number of N+')

for i in range(1, len(max(dotmatches))+1):
    y = dotmatches.count(i*'.')
    x = i * '.'
    print(f'There are {y} number of {x}')

print(f'There are {len(cgmatches)} CG matches')

sequence3 = sequence2.replace('CG', )


#Code GRAVEYARD
#tried some things here, may go back to it later
'''x1 = 0
for i in period_list:
    #match = re.match(r'^\.$', i)
    if i == '.':
    #if re.match(r'^\.$', i):
        x1 += 1
#x1 = [re.match('\.', i) for i in period_list]
x_1 = period_list.count('.')
print(x_1)

period_list =[]
for line in sequence:
    matches = re.findall(r'\.+', line)
    period_list.extend(matches)

#print(period_list)
#print(len(period_list))
#print(max(period_list))
#print(len(max(period_list)))


cgmatches = []
for line in sequences:
    cgmatch = re.findall(r'CG', line)
    cgmatches.extend(cgmatch)
print(f'There are {len(cgmatches)} CG matches')

n_list = []
for line in sequences:
    matches = re.findall(r"N+", line)
    match_count = len(matches)
    n_list.append(match_count)
print(f'Number of N+ matches per line: {n_list}')


'''


