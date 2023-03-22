# Задача: Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.

list1 = [int(x) for x in input("Введите списки (между элементами расставьте пробелы) \n Первый: ").split()]
list2 = [int(y) for y in input(" Второй: ").split()]
result = []

for item1 in list1:
    for item2 in list2:
        if item1 != item2 and item2 == list2[-1]:
            result.append(item1)
        elif item1 == item2:
            break

result.sort()
print (list1, list2)
print ("Элементы первого списка, отсутствующие во втором:", result)