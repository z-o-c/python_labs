name = " ".join(input("ФИО:").split())
full_name = ""
for i in name:
    if i.isupper():
        full_name += i
print(f"Инициалы: {full_name}. \nДлина (символов): {len(name)}")