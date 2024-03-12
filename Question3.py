def average(a, b, c, d, n):
    total = ((a * 4) + (b * 3) + (c * 2) + (d * 1)) * 3
    avrg = total / (n * 3)
    return avrg

def point_check(n):
    a = 0
    b = 0
    c = 0
    d = 0
    count = 0
    for i in range(1, n+1):
        point = input(f"Nilai MK {i}: ")
        if point == "A":
            a += 1
        elif point == "B":
            b += 1
        elif point == "C":
            c += 1
        elif point == "D":
            d += 1
        else:
            print("Invalid")
        count += 1
    result = round(average(a, b, c, d, count), 2)
    print("Rata-rata = ",result)
    

amnt = input("Jumlah MK: ")

try:
    amnt = int(amnt)
except:
    print("Please use numbers, not words")
    exit()

point_check(amnt)