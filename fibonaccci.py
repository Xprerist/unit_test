n = [1, 1]

def reihe_des_fibonacci(b):
    a = 2
    # while a < b:
    while a in range(2, b):
        wert = n[a - 1] + n[a - 2]
        n.append(wert)
        a = a + 1
    golden = n[a - 1]/n[a - 2]
    return(n[a-1], golden)

b = int(input("Gib einen Wert größer 2 ein: "))
zahl, schnitt = reihe_des_fibonacci(b)

def unit_test_fibonacci():
    if b == 3:
        assert abs(schnitt - 1.618) <= 0.419
    elif b == 4:
        assert abs(schnitt - 1.618) <= 0.12
    else:
        assert abs(schnitt - 1.618) <= 0.049


print("Die Reihe: ", n)
print("Der " + str(b) + ". Wert aus der Fibonacci-Reihe beträgt", zahl)
print("Der goldene Schnitt beträgt: ", schnitt)

unit_test_fibonacci()