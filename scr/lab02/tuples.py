def format_record(rec: tuple[str, str, float]) -> str:
    """ Форматирует запись о студенте в стандартизированную строку."""
    result = []

    if len(rec[0]) == 0:
        return ValueError("пустое ФИО") 
    elif len(rec[1]) == 0:
        return ValueError("пустая группа")
    elif not isinstance(rec[2], float):
        return ValueError("неверный тип GPA") 
    
    full_name = ((rec[0].strip()).title()).split()
    full_name_abbrevition = [str(x) for x in " ".join(full_name) if x.isupper()]
    result.append(f"{full_name[0]} {".".join(full_name_abbrevition[1:])}.")
    result.append(f"гр. {rec[1]}")
    result.append(f"GPA {rec[2]:.2f}")

    return ", ".join(result)


print("Тест 1:", format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print("Тест 2:", format_record(("Петров Пётр", "IKBO-12", 5.0)))
print("Тест 3:", format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print("Тест 4:", format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print("Тест 5:", format_record(("сидорова  анна   сергеевна ", "", 3.999)))
print("Тест 6:", format_record(("Петров Пётр", "IKBO-12", "5.0")))
