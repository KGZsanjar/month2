# Функция для пузырьковой сортировки
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Функция для двоичного поиска
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return f"Элемент {target} найден на позиции {mid}"

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return f"Элемент {target} не найден"


# Пример использования
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print(f"Отсортированный список: {sorted_list}")

# Используем бинарный поиск
element_to_find = 25
result = binary_search(sorted_list, element_to_find)
print(result)


