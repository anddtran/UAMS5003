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

import regex
import os

file_path = '/Users/andrewtran/repos/5003/midterm/sq.txt'

if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        sequences = f.read()
        print("Length of sequences:", len(sequences)) #check if the file was accessed correctly 

