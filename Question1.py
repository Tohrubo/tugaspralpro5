def mult(n1, n2):
    count = 0
    r = 0
    print(f"{n1} x {n2} =", end="")
    while count < n1:
        r += n2
        count += 1
        print(f" {n2}", end="")
        if count == n1:
            continue
        else:
            print(" +", end="")
    print(f" = {r}")
n1 = input("Number: ")
n2 = input("Number: ")

try:
    n1 = int(n1)
    n2 = int(n2)
except:
    print("Please use numbers, not words")
    exit()

mult(n1, n2)