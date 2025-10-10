import sys
sys.path.append("C:\\Users\\Max\\Desktop\\python_labs")

from scr.lib.text import *

inpt_text = input("Введите текст: ")
normalize_text = normalize(inpt_text)

print(f"Всего слов: {len(tokenize(normalize_text))}")

print(f"Уникальных слов: {len(count_freq(tokenize(normalize_text)))}")

print("Топ-5:")
for word, count in top_n(count_freq(tokenize(normalize_text)), 5):
    print(f"{word}:{count}")