"""
Вводится число найти его максимальный делитель,
являющийся степенью двойки. 10(2) 16(16), 12(4).
"""
user = int(input("Введите число, для определения максимального делителя "))


def get_maxdiv(num):
    a = 1
    while a <= num:
        a <<= 1
    return a >> 1


print(get_maxdiv(user))