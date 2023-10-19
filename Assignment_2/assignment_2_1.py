def print_art(): # defining the function to print the art, using other functions for different parts of the art
    global x
    top_bot('.')  # top line uses period as "flair" argument
    second_secondlast()  # starts with backslash
    middle() # alternates starting with '(' or ')'
    x += 1   # increment x so that the second_secondlast function changes starting slash
    second_secondlast()  # starts with forward slash (using if/else and the variable x)
    top_bot('\'')  # bottom line uses apostrophe as "flair" argument

def top_bot(flair):               # print top and bottom line in the pattern but rounded down in multiple of 4 (i.e. 28, 29, 30, 31 have the same length)
    print(flair, end="")
    if width % 4 == 0:
        for i in range(width):
            print('-', end="")
    else:                          # round down in multiple of 4
        for i in range(width - (width % 4)):
            print('-', end="")
    print(flair)

def second_secondlast():           # print second or second to last line in pattern to match length of top_bot (slashes and spaces are multiple of 4)
    print('|', end="")
    if x == 0:
        for i in range(int((width / 4))):
            print("\  /", end="")
    elif x == 1:
        for i in range(int((width / 4))):
            print("/  \\", end="")
    print('|')

def middle():                       # prints middle section in pattern to match length of top_bot (parentheses and spaces are multiple of 4)
    for i in range((height - 4)):
        print("|", end="")
        if i % 2 != 0:
            for i in range(int((width / 4))):
                print(" )( ", end="")
            i += 1
        else:
            for i in range(int((width / 4))):
                print("(  )", end="")
            i += 1
        print("|")

if __name__ == '__main__':          # main using the defined functions
    while True:
        try:
            width = int(input("please input width: "))
            height = int(input("please input height: "))
            x = 0

            if width <= 0 or height <= 0:
                print("please enter positive numbers only")
                continue
            else:
                print_art()
                break
        except ValueError:
            print("please enter positive integers")
            continue
