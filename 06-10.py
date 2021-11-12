def g():
    a = {}
    while True:
        print('Введите имя(Чтобы выйти нажмите f)')
        v = input()
        if v == 'f':
            print(a)
            break
        else:
            print('(Введите свой номер телефона)')
            c = str(input())
            if (c[0] == "+" and c[2] == "-" and c[6] == "-" and c[10] == "-" and c[13] == "-"):
                 if c[1:].replace("-","").isdigit():
                    a[v] = c
    return 0
g()