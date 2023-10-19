import sys

" This program calculates the average of three numbers provided by the user"


def my_average(n1,n2,n3):
    """This program receives 3 numbers and returns their average"""
    return (n1+n2+n3)/3


nn1 = input("what is number 1?")
nn2 = input("what is number 2?")
nn3 = input("what is number 3?")

n1 = int(nn1)
n2 = int(nn2)
n3 = int(nn3)

if __name__== '__main__':
    myn1 = float(sys.argv[1])
    myn2 = float(sys.argv[2])
    myn3 = float(sys.argv[3])
    avg = my_average(myn1,myn2,myn3)
    print("I got all the numbers")
    print(f"The result of the average is {avg}")