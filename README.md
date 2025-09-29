# python_labs
# Задание №1
```python
print(f"Привет, {input()}! Через год тебе будет {int(input()) + 1}.")
```

# Задание №2
```python
num_1 = input()
num_1 = float(num_1.replace(",","."))
num_2 = float(input())
print(f"sum={num_1 + num_2}; avg={((num_1 + num_2)/2):.2f}")
```

# Задание №3
```python
price = float(input("price= "))
discount = float(input("discount= "))
vat = float(input("vat= "))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки: {base:.2f} ₽\nНДС: {vat_amount:.2f} ₽\nИтого к оплате: {total:.2f} ₽")
```

# Задание №4
```python
min = int(input("Минуты: "))
print(f"{min//60}:{min%60}")
```

# Задание №5
```python
name = " ".join(input("ФИО:").split())
full_name = ""
for i in name:
    if i.isupper():
        full_name += i
print(f"Инициалы: {full_name}. \nДлина (символов): {len(name)}")
```

# Задание №6
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

# Задание №7
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

test = "thisisabracadabraHt1eadljjl12ojh."
print(find_word(test))
```