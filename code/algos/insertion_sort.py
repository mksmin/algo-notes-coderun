# Insertion Sort

def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        ind = step - 1

        # Сравниваем ключ с каждым элементов слева от него, пока не найдем меньший или не дойдем до начала массива
        # Для сортировки по убыванию меняем знак < на > в key < arr[ind]
        while ind >= 0 and key < arr[ind]:
            arr[ind + 1] = arr[ind]  # сдвигаем элемент вправо
            ind -= 1

        # Размещаем ключ на своем месте
        arr[ind + 1] = key


data = [9, 5, 1, 4, 3]
insertion_sort(data)
print('Sorted Array in Ascending Order:')
print(data)
