user_list1 = [int(el) for el in input().split()]
user_list2 = [int(el) for el in input().split()]
print(len((set(user_list1).intersection(set(user_list2)))))
print(len(set(user_list1) ^ set(user_list2)))