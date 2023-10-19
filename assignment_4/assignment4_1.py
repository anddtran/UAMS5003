#Suppose we have strings of length 4 for the alphabet Σ = {0, 1}. We define a distance (called dist)
#between two strings A and B as the the number of characters that are different between the two strings.
#Note that all the distances between any two strings belong to the set K = {0, 1, 2, 3, 4}

#Design a program in Python that creates a dictionary D1 where the keys are elements of the set K. The values for a
#specific key consist of a list of all the strings that have a distance k from the one string 1111. For instance

# key value
# k = 0: [1111]
# k = 1 : [1110, 1101, 1011, 0111]

#Your program should print the dictionary for all values of K.

def possiblelist():
    #lists all the possibilities for a 4 digit number with alphabet Σ = {0, 1}
    possibilities = []
    for i in range(16):
        bin_num = format(i, '04b')
        possibilities.append(bin_num)
    return possibilities

def compare(a, b):
    #compares each possibility to 1111 and defines the distance (dist) between the two strings #hammingdistance
    dist = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dist += 1
    return dist

if __name__ == '__main__':
    D1 = {}
    possibilities = possiblelist()
    distances = []
    four = []
    three = []
    two = []
    one = []
    zero = []
    for num in possibilities:
        distance = compare(num, '1111')
        distances.append(distance)
        if distance == 4:
            four.append(num)
            D1[4] = four
        elif distance == 3:
            three.append(num)
            D1[3] = three
        elif distance == 2:
            two.append(num)
            D1[2] = two
        elif distance == 1:
            one.append(num)
            D1[1] = one
        else:
            zero.append(num)
            D1[0] = zero
    for k, v in D1.items():
        print(f'k = {k}: {v}')






