while True:
    try:
        integer = input("Please enter an integer for scrambling like an egg:")
        k = len(integer)
        if k % 2 == 0:
            s = k // 2
        else:
            s = (k-1) // 2
        #print(k, s)

        mod_integer = ""
        for i in range(s):
            mod_integer += integer[2 * i + 1] + integer[2 * i]

        if k % 2 == 1:
            mod_integer += integer[-1]

        int(mod_integer)
        print(f"Your cooked integer: {mod_integer}")
        break

    except ValueError:
        print("Not an integer.")
