import random

# Создание массива случайных чисел от 1 до 100
array_of_integers = [random.randint(1, 100) for _ in range(100)]
print(array_of_integers)
print('//////////////////////////////////////////')
# Функция для умножения элементов массива
def multiply_array(lst):
    result = 0
    for number in lst:
        result += number
    return result

# Вызов функции с передачей массива
result = multiply_array(array_of_integers)
print(result)