def odd(ll, up):
    if ll < up:
        if ll % 2 == 0:
            ll += 1
        while ll <= up:
            print(f"{ll},", end="")
            ll += 2
    elif ll > up:
        if ll % 2 == 0:
            ll -= 1
        while ll >= up:
            print(f"{ll},", end="")
            ll -= 2
    else:
        if ll % 2 == 0:
            print(None)
        else:
            print(ll)
in1 = input("Lower limit: ")
in2 = input("Upper limit: ")
try:
    in1 = int(in1)
    in2 = int(in2)
except:
    print("Please use numbers, not words")
    exit()
print("Ganjil: ", end="")
odd(in1, in2)
