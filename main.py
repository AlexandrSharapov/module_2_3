#Задача "Нули ничто, отрицание недопустимо!":

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0 #начальное значение индекса
while index < len(my_list): #индекс меньше длины списка
    if my_list[index] < 0: 
        index += 1 
        continue
    print(my_list[index]) 
    index += 1 