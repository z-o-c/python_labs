from io_txt_csv import *

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from lib.text import *

# читаем и обрабатываем первый файл
if len(read_text("data/lab04/input.txt")) == 0:
    write_csv([], "data/lab04/report.csv", header=("word", "count"))
else:
    text_1 = normalize(read_text("data/lab04/input.txt"))
    token_text_1 = tokenize(text_1)
    num_tokens_1 = count_freq(token_text_1)
    top_tokens_1 = top_n(num_tokens_1, 5)

    print("input.txt:")
    print(f"Всего слов: {len(token_text_1)}")
    print(f"Уникальных слов: {len(num_tokens_1)}")
    print("Топ-5:")
    for word, count in top_tokens_1:
        print(f"{word}: {count}")
    print("\n")

    write_csv([(word, count) for word, count in num_tokens_1.items()], "data/lab04/report.csv", header=("word", "count"))

# читаем и обрабатываем несколько входных файлов + «сводный» отчет
text_2 = normalize(read_text("data/lab04/a.txt"))
token_text_2 = tokenize(text_2)
num_tokens_2 = count_freq(token_text_2)
top_tokens_2 = top_n(num_tokens_2, 5)

text_3 = normalize(read_text("data/lab04/b.txt"))
token_text_3 = tokenize(text_3)
num_tokens_3 = count_freq(token_text_3)
top_tokens_3 = top_n(num_tokens_3, 5)

report_per_file = {
    "a.txt": [(word, count) for word, count in num_tokens_2.items()],
    "b.txt": [(word, count) for word, count in num_tokens_3.items()]
}

report_total = count_freq(token_text_2 + token_text_3)
report_total_list = [(word, count) for word, count in report_total.items()]

# записываем отчет по файлам
write_csv([(file, word, count) for file, words in report_per_file.items() for word, count in words], "data/lab04/report_per_file.csv", header=("file", "word", "count"))

# записываем общий отчет
write_csv([(word, count) for word, count in report_total.items()], "data/lab04/report_total.csv", header=("word", "count"))

# выводим красивый отчет в табличном виде
print("Общий отчет:")
print_table(report_total_list)
print("\n")

print("Отчет по файлам:")
print_table_per_file(report_per_file)