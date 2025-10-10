
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Теперь можем импортировать функции из lib.text
from lib.text import *

def print_table(words_data):
    """Печатает таблицу со словами и их частотой"""
    if not words_data:
        raise ValueError("print_table: words_data пуст")
    
    # Находим самое длинное слово
    max_word_length = max(len(word) for word, _ in words_data)
    
    # Печатаем заголовок
    print(f"{'слово':<{max_word_length}} | частота")
    print("-" * max_word_length + "-|-" + "-" * 7)
    
    # Печатаем данные
    for word, count in words_data:
        print(f"{word:<{max_word_length}} | {count}")

try:
    inpt_text = input("Введите текст: ")
    normalize_text = normalize(inpt_text)
    tokens = tokenize(normalize_text)
    freq = count_freq(tokens)
    top_words = top_n(freq, 5)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")

    print("Топ-5:")
    print_table(top_words)

except ValueError as e:
    print(f"Ошибка: {e}")