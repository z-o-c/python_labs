def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает кортеж (минимум, максимум). Если список пуст — ValueError"""
    
    if len(nums) == 0:
        raise ValueError("Список пуст")
    
    else:
        return (min(nums),max(nums))
try:
    print("min_max")
    print("Тест 1:", min_max([3, -1, 5, 5, 0]))
    print("Тест 2:", min_max([42]))
    print("Тест 3:", min_max([-5, -2, -9]))
    print("Тест 4:", min_max([1.5, 2, 2.0, -3.1]))
    print("Тест 5:", min_max([]))
except ValueError as e:
    print(f"Ошибка: {e}")


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный список уникальных значений (по возрастанию)"""
    return list(sorted(set(nums)))

print(f"\nunique_sorted")
print("Тест 1:", unique_sorted([3, 1, 2, 1, 3]))
print("Тест 2:", unique_sorted([]))
print("Тест 3:", unique_sorted([-1, -1, 0, 2, 2]))
print("Тест 4:", unique_sorted([1.0, 1, 2.5, 2.5, 0]))


def flatten(mat: list[list | tuple]) -> list:
    """«Расплющивает» список списков/кортежей в один список по строкам (row-major).
    Если встретилась строка/элемент, который не является списком/кортежем — TypeError"""
    result = []

    for i in mat:
        if not isinstance(i, (list, tuple)):
            raise TypeError("строка не строка строк матрицы")
        result.extend(i)    
    
    return result

try:
    print(f"\nflatten")
    print("Тест 1:", flatten([[1, 2], [3, 4]]))
    print("Тест 2:", flatten([[1, 2], (3, 4, 5)]))
    print("Тест 3:", flatten([[1], [], [2, 3]]))
    print("Тест 4:", flatten([[1, 2], "ab"]))
except TypeError as e:
    print(f"Ошибка: {e}")