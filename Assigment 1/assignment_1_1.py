list = []
i = 0
j = 5
while i < j:
    try:
        list.append(float(input("Please enter a positive number: ")))
        if list[-1] < 0:
            print("Number is not positive. Try again:")
            del list[-1]
            i = i
        else:
            i = i + 1
    except ValueError:
        print("Bad input. Please enter a positive number:")



Harmonic_mean = 5/((1/list[0])+(1/list[1])+(1/list[2])+(1/list[3])+(1/list[4]))

print(Harmonic_mean)