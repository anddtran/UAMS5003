list = []
i = 0
j = int(input("How many numbers would you like? "))
denominator = []

while i < j:
    try:
        list.append(float(input("Please enter a positive number: ")))
        if list[-1] < 0:
            print("Try again:")
            del list[-1]
            i = i
        else:
            denominator.append(1/list[i])
            i = i + 1
    except ValueError:
        print("Bad input. Please enter a positive number:")


Harmonic_mean = j/sum(denominator)
print(H)
