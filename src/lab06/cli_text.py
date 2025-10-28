import argparse
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.text import *
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True)
    stats_parser.add_argument("--top", type=int, default=5)

    args = parser.parse_args()
    
    # если подкоманда не указана — показать помощь и выйти.
    if not args.command:
        parser.print_help()
        return
    
    if args.command == "cat":
        """ Реализация команды cat """
        file_path = args.input

        if not Path(file_path).exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                for num, line in enumerate(file, start=1):
                    if args.n:
                        print(f"{num}: {line}", end="")
                    else:
                        print(line, end="")

        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")

    elif args.command == "stats":
        """ Реализация команды stats """
        file_path = args.input

        if not Path(file_path).exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        try:    
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
            
            normalize_text = normalize(text)
            tokens = tokenize(normalize_text)
            freq = count_freq(tokens)
            top_words = top_n(freq, args.top)
            print_table(top_words)

        except Exception as e:
            print(f"Ошибка при обработке файла: {e}")

    else:
        parser.print_help()
        return

if __name__ == "__main__":
    main()