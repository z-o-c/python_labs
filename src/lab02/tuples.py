def format_record(rec: tuple[str, str, float]) -> str:
    """ Форматирует запись о студенте в стандартизированную строку."""

    if not isinstance(rec, tuple):
        raise ValueError("входные данные должны быть tuple")
    elif len(rec) != 3:
        raise ValueError("tuple должен содержать ровно 3 элемента")

    result = []

    if len(rec[0]) == 0:
        raise ValueError("пустое ФИО") 
    elif len(rec[1]) == 0:
        raise ValueError("пустая группа")
    elif not isinstance(rec[2], float):
        raise ValueError("неверный тип GPA") 
    
    full_name = ((rec[0].strip()).title()).split()
    full_name_abbrevition = [str(x) for x in " ".join(full_name) if x.isupper()]
    result.append(f"{full_name[0]} {".".join(full_name_abbrevition[1:])}.")
    result.append(f"гр. {rec[1]}")
    result.append(f"GPA {rec[2]:.2f}")

    return ", ".join(result)

try:
    print("Тест 1:", format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print("Тест 2:", format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print("Тест 3:", format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print("Тест 4:", format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
    print("Тест 5:", format_record(("сидорова  анна   сергеевна ", "", 3.999)))

except ValueError as e:
     print(f"Ошибка {e}")
