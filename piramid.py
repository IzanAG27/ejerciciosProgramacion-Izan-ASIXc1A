nivells = int(input(""))

for x in range(1, nivells + 1):
    if x == nivells:
        print("#" * x, end="")
    else:
        print("#" * x)