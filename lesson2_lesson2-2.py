# Задача 2. Для списка реализовать обмен значений соседних элементов.
# Т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
q = int(input("How many items in list do you want to add?\n\t Enter items quantity: "))
my_lst = []
for i in range(q):
    my_lst.append(input(f"Item # {i + 1} : "))
print(f"Your item list view:\n{my_lst}")
for x in range(0, (len(my_lst) - 1),2):
    my_lst[x], my_lst[x+1] = my_lst[x+1], my_lst[x]
print(f"Your CHANGED item list view:\n{my_lst}")
