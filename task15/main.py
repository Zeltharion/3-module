def find_common_elements(array1, array2):
    """
    Возвращает массив с общими элементами из двух заданных массивов.
    """
    common_elements = list(set(array1) & set(array2))
    return common_elements


array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

result = find_common_elements(array1, array2)
print('Первый массив:', array1)
print('Второй массив:', array2)
print("\nОбщие элементы:", result)
