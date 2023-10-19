import cowsay

#Create a Python function h that takes one digit, multiplies the digit by 2,
#and returns the sum of the digits from that multiplication.
def h_function(x):
    multiply = str(x * 2)
    digit = [int(d) for d in multiply]  #doing this does not allow for negative numbers or non number characters
    sumdigit = sum(digit)
    return sumdigit

# Create a program in Python that ask the user for a non-negative integer with 10 digits that will be denoted
# n1n2 · · · n9n10
# The program will return True if the following expression is valid using the function h from above
# h(n1) + n2 + h(n3) + n4 + · · · + h(n9) + n10 ≡ 0(mod10)
# Otherwise, it will return False. In simpler terms, it tests whether the sum of the left is divisible by 10 or not

def testint(y):
    number = str(y)
    testdigit = [h_function(int(c)) for c in number]
    modulotest = sum(testdigit)
    return modulotest % 10 == 0


if __name__ == '__main__':
    while True:
        try:
            userinteger = input('test your 10 digit integer: ')
            if len(userinteger) == 10 and userinteger.isdigit() and int(userinteger) >= 0: #only runs the testint function if the length of the integer is 10
                userinteger = int(userinteger)
                if(testint(userinteger)):
                    cowsay.dragon('it is true. your integer passes the test!')
                else:
                    cowsay.cow('nope. this integer has failed')
                break
            else:
                print('please enter a positive 10 digit integer')
        except ValueError:
            print('you didn\'t enter a valid integer!')




