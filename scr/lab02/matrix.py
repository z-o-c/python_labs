def check_rectangular(matrix):
    """Проверяет, что матрица прямоугольная"""
    if not matrix:
        return
    first_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_len:
            return False

def transpose(mat: list[list[float | int]]) -> list[list]:
    """Транспонирование матрицы (Меняем строки и столбцы местами)"""
    if check_rectangular(mat) == False:
        return ValueError("Рваная матрица")

    if not mat:
        return []
    return [list(item) for item in zip(*mat)]

print(f"\ntranspose")    
print("Тест 1:", transpose([[1, 2, 3]]))
print("Тест 2:", transpose([[1], [2], [3]]))
print("Тест 3:", transpose([[1, 2], [3, 4]]))
print("Тест 4:", transpose([]))    
print("Тест 5:", transpose([[1, 2], [3]])) 

def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает суммы элементов каждой строки матрицы"""
    if check_rectangular(mat) == False:
        return ValueError("Рваная матрица")
    
    return [sum(item) for item in mat]

print(f"\nrow_sumse")    
print("Тест 1:", row_sums([[1, 2, 3], [4, 5, 6]]))
print("Тест 2:", row_sums([[-1, 1], [10, -10]]))
print("Тест 3:", row_sums([[0, 0], [0, 0]]))    
print("Тест 4:", row_sums([[1, 2], [3]])) 

def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает суммы элементов каждого столбца матрицы"""
    if check_rectangular(mat) == False:
        return ValueError("Рваная матрица")
    
    return [sum(item) for item in zip(*mat)]

print(f"\ncol_sums")    
print("Тест 1:", col_sums([[1, 2, 3], [4, 5, 6]]))
print("Тест 2:", col_sums([[-1, 1], [10, -10]]))
print("Тест 3:", col_sums([[0, 0], [0, 0]]))    
print("Тест 4:", col_sums([[1, 2], [3]])) 