# Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
# Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
# Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
# Создайте кортеж из одного элемента, чтобы при итерировании по этому
# элементы последовательно выводились значения 1, 2, 3.
# Убедитесь что len() исходного кортежа возвращает 1.
list1 = list("abc")
tup1 = tuple(list1)
tup2 = tuple("abc")
list2 = tup2
a, b, c = 'a', 2, 'python'
tup3 = ("123",)
for el in tup3[0]:
    print(el)
print(len(tup3))
print(list1, tup1, tup2, list2, b, tup3)
