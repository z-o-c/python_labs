# python_labs

## Лабораторная номер 1

Задание 1
```python
print(f"Привет, {input("Имя: ")}! Через год тебе будет {int(input("Возраст: ")) + 1}.")
```

![Задание номер 1](./images/lab01/img01.png)


Задание 2
```python
num_1 = input()
num_1 = float(num_1.replace(",","."))
num_2 = float(input())
print(f"sum={num_1 + num_2}; avg={((num_1 + num_2)/2):.2f}")
```

![Задание номер 2](./images/lab01/img02.png)


Задание 3
```python
price = float(input("price= "))
discount = float(input("discount= "))
vat = float(input("vat= "))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽\nНДС: {vat_amount:.2f} ₽\nИтого к оплате: {total:.2f} ₽")
```

![Задание номер 3](./images/lab01/img03.png)


Задание 4
```python
min = int(input("Минуты: "))
print(f"{min//60}:{min%60}")
```

![Задание номер 4](./images/lab01/img04.png)


Задание 5
```python
name = " ".join(input("ФИО:").split())
full_name = ""
for i in name:
    if i.isupper():
        full_name += i
print(f"Инициалы: {full_name}. \nДлина (символов): {len(name)}")
```

![Задание номер 5](./images/lab01/img05.png)


Задание 6
```python
def solve():
    true_count = 0
    false_count = 0
    n = int(input())

    for i in range(n):
        line = input().split()
        counter = line[-1]

        if counter == "True":
            true_count += 1
        elif counter == "False":
            false_count += 1

    return print(true_count, false_count)

solve()
```

![Задание номер 6](./images/lab01/img06.png)


Задание 7
```python
def find_word(test):
    end = ""
    count_1 = 0
    count_2 = 0
    for i in test:
        count_1 += 1
        if i.isupper():
            end += i
            break
    
    for i in test:
        count_2 += 1
        if i.isdigit():
            break
    
    end += test[count_2::count_2 - count_1 + 1]
    return end

test = input()
print(find_word(test))
```

![Задание номер 7](./images/lab01/img07.png)

## Лабораторная номер 2

Задание 1
```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает кортеж (минимум, максимум). Если список пуст — ValueError"""
    
    if len(nums) == 0:
        return ValueError("Список пуст")
    
    else:
        return (min(nums),max(nums))

print("min_max")
print("Тест 1:", min_max([3, -1, 5, 5, 0]))
print("Тест 2:", min_max([42]))
print("Тест 3:", min_max([-5, -2, -9]))
print("Тест 4:", min_max([]))
print("Тест 5:", min_max([1.5, 2, 2.0, -3.1]))


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
            return TypeError("строка не строка строк матрицы")
        result.extend(i)    
    
    return result

print(f"\nflatten")
print("Тест 1:", flatten([[1, 2], [3, 4]]))
print("Тест 2:", flatten([[1, 2], (3, 4, 5)]))
print("Тест 3:", flatten([[1], [], [2, 3]]))
print("Тест 4:", flatten([[1, 2], "ab"]))
```

![Задание номер 1](./images/lab02/img01.png)