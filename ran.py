import random
import string
n = string.ascii_letters
y = [c for c in n]
def cr_str(width):
    l = [random.choice(string.ascii_letters) for i in range(width)]
    n = ''
    for el in l:
        n += el
    return n

def generate_random_string(length):
    letters = n
    rand_string = ''.join(random.choice(letters) for i in range(length))
    print("Длинна строки равна",length,":", rand_string)


sl = generate_random_string(int(input('Укажите длинну строки для:')))

def cr_list_str(width, num):
    l = [cr_str(width) for i in range(num) ]
    n = ''
    big = 0
    small = 0
    statb = 0
    stats = 0
    statr = 0
    for el in l:
        n += el
        n += ' '
        for i in el:
            if i.isupper():
                big += 1
            else:
                small += 1
        if big > small:
            statb += 1
            n += '1'
        elif small > big:
            stats += 1
            n += '0'
        else:
            statr += 1
            n += '-1'
        
        n += ' '
    n += ' A = ' + str(statb/(statb+stats+statr)*100) + '%'
    n += ' a = ' + str(stats/(statb+stats+statr)*100) + '%'
    n += ' a == A ' + str(statr/(statb+stats+statr)*100) + '%'
    return n
8
print(cr_list_str(5, 5))