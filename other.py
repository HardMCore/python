print('Generator trójkąta równobocznego')
bok = int(input('Podaj wielkosc boku: '))

bok = float(bok / 2)
if bok.is_integer:
    bok = int(bok)
    print(" " * bok + "++")
    for i in range(1, bok + 1):
        print(" " * (bok - i) + "+" + " " * i * 2 + "+")
    print("+" * bok * 2 + "+" * 2)

else:
    bok = int(bok + 0.5)
    print(" " * bok + "++")
    for i in range(1, bok + 1):
        print(" " * (bok - i) + "+" + " " * i * 2 + "+")
    print("+" * bok * 2 + "+" * 2)
