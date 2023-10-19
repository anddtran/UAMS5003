" This program calculates the average of three numbers provided by the user"


def my_average(n1,n2,n3):
    """This program receives 3 numbers and returns their average"""
    return (n1+n2+n3)/3

print("we will calculate average of 3 numbers")
myn1 = float(input("what is number 1? "))
myn2 = float(input("what is number 2? "))
myn3 = float(input("what is number 3? "))

avg = my_average(myn1,myn2,myn3)
print("I got all the numbers")
print(f"The result of the average is {avg}")