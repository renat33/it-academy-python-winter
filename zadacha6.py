# Дан список целых чисел. Требуется переместить все ненулевые элементы
# в левую часть списка, не меняя их порядок, а все нули - в правую часть.
# Порядок ненулевых элементов изменять нельзя,
# дополнительный список использовать нельзя, задачу нужно выполнить
# за один проход по списку. Распечатайте полученный список.
list1 = [int(el) for el in input().split()]
for el in range(len(list1)):
    list1.remove(0)
    list1.append(0)
print(list1)
