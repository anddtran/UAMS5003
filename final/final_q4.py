'''
Suppose a terrain is represented by a two dimensional grid of elevation values. A peak is a grid point whose
four neighboring cells (left, right, up and down) have strictly lower elevation values (see the corresponding
graphical representation in figure 2). 

Write a Python program ask for the user for the size of the grid (say n
by m), generates elevation randomly following a N (0, 10) distribution. 

The output would be the number of peaks and the location of each one of them. 

Note. For the points located on the grid’s border consider only the neighbors within the grid

see the pdf for the figure

Process: generate a grid n x m, give each node an elevation randomly N(0,10), count the number of peaks and give the location
'''
import re
import sys
import random
import numpy as np


# get size of grid
def userinput(): #check user input string to only allow digits, then return m and n
    usrinput = input('please enter grid size m and n separated by spaces: ')
    if re.match(r'^(\d+)\s+(\d+)$', usrinput):
        print('The input is accepted...')
        indigit = re.split('\s+', usrinput)
        m = int(indigit[0])
        n = int(indigit[1])
        return m, n
    elif usrinput.lower() == 'exit':
        sys.exit()
    else:
        print('the input is rejected')

# give elevation
def elevation():
    elevation = random.randint(0,10)
    return elevation

# create grid matrix
def matrix_create(m, n):
    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(elevation())
        matrix.append(row)
    return matrix

def np_matrix(matrix):
    matrix = np.array(matrix)
    return matrix

# get neighbors
#if mi = 0, disregard mi - 1, if mi = m, disregard mi + 1
#if ni = 0, disregard ni - 1, if ni = n, disregard ni + 1
#takes the input from inside findpeak()
def neighbors(i, j, m, n):
    valid_neighbors = []
    if i > 0:  # Up
        valid_neighbors.append((i - 1, j))
    if i < m - 1:  # Down
        valid_neighbors.append((i + 1, j))
    if j > 0:  # Left
        valid_neighbors.append((i, j - 1))
    if j < n - 1:  # Right
        valid_neighbors.append((i, j + 1))

    return valid_neighbors



#function to check if the node is a peak and give location, add location m,n to a list as a list of lists
#iterate through each node and compare elevations using the neighbors function
#if elevation at mi, nj is > the elevation for the possibilities, add [mi, nj] to peak list
def findpeak(matrix):
    peaklist = []
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            # Get the current cell elevation
            current_elevation = matrix[i][j]
            # Get the valid neighbors
            cell_neighbors = neighbors(i, j, m, n)
            # Check if current cell elevation is higher than all of its neighbors
            # all() is a function to check true/false, list comprehension method for comparison
            if all(current_elevation > matrix[x][y] for x, y in cell_neighbors):
                peaklist.append([i, j])
    return peaklist


# count the peaks in the list
def countpeaks(peaklist):
    number_of_peaks = len(peaklist)
    return number_of_peaks


if __name__ == '__main__':
    m, n = userinput()
    matrix = matrix_create(m, n)
    grid = np_matrix(matrix)
    peaklist = findpeak(grid)
    peak_count = countpeaks(peaklist)
    print(f'{grid}')
    print(f'There are {peak_count} peaks at the locations: {peaklist}')

    





