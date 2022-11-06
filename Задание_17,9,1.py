def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] < element and array[middle+1] >= element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element <= array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)

while True:
    try:
        array_str = input("Введите последовательность чисел через пробел:\t")
        array = list(map(int, array_str.split()))  # преобразование в список
        if len(array) != 0:
            break
        else:
            print('Введена пустая строка без чисел. Попробуйте ещё раз')

    except ValueError:
        print('В последовательности не только числа. Попробуйте ещё раз')

array_sort = sort(array) # сортировака списка
col = len(array)

while True:
    try:
        element = int(input("Введите число:\t"))
        break
    except ValueError:
        print('Вы ввели не число. Попробуйте снова')

 # если введенное число > самого правого или <= самого левого, выдается сообщение
if element > array[col-1] or element <= array[0]:
    print('Для введенного числа нет нужного промежутка')
else:
    print("Отсортированная последовательность", array)
    k = binary_search(array, element, 0, col-1)
    if k == False:
        print('Для введенного числа нет нужного промежутка')
    else:
        print("Позиция элемента", k)

