# python_labs

>  Ссылки на материалы каждой лабораторной работы: подробные описания (README), исходный код и каталоги данных.

>  Условия задач:[python_bivt](https://github.com/outtathe/python_bivt)

## Лабораторная номер 1

- [README](src/lab01/README.md) — подробное описание лабораторной

- Код — исходные файлы заданий:
  - [ex01](src/lab01/ex01.py)
  - [ex02](src/lab01/ex02.py)
  - [ex03](src/lab01/ex03.py)
  - [ex04](src/lab01/ex04.py)
  - [ex05](src/lab01/ex05.py)
  - [ex06](src/lab01/ex06.py)
  - [ex07](src/lab01/ex07.py)
  
## Лабораторная номер 2

- [README](src/lab02/README.md) — подробное описание лабораторной

- Код — исходные файлы заданий:
  - [arrays](src/lab02/arrays.py)
  - [matrix](src/lab02/matrix.py)
  - [tuples](src/lab02/tuples.py)

## Лабораторная номер 3

- [README](src/lab03/README.md) — подробное описание лабораторной

- Код — исходные файлы заданий:
  - [text_stats](src/lab03/text_stats.py)


## Лабораторная работа 4: Работа с файлами и CSV

- [README](src/lab04/README.md) — подробное описание лабораторной

- Код — исходные файлы лабораторных скриптов:
  - [io_txt_csv](src/lab04/io_txt_csv.py)
  - [text_report](src/lab04/text_report.py)

- Data — входные/выходные данные для примеров:
  - [lab04](data/lab04/)

## Лабораторная работа 5: Конвертация форматов данных

- [README](src/lab05/README.md) — подробное описание лабораторной

- Код — функции конвертации форматов:
  - [JSON <-> CSV](src/lab05/json_csv.py)
  - [CSV -> XLSX](src/lab05/csv_xlsx.py)

- Data — примеры входных данных и результаты:
  - [Samples](data/lab05/samples)
  - [Out](data/lab05/out)


## Лабораторная работа 6: CLI‑утилиты с argparse

- [README](src/lab06/README.md) — подробное описание лабораторной

- Код — CLI‑скрипты с подкомандами:
    - [cli_text](src/lab06/cli_text.py)
    - [cli_convert](src/lab06/cli_convert.py)

- Data — пример входных данных и результаты:
    - [Samples](data/lab06/samples)
    - [Out](data/lab06/out)

## Лабораторная работа 7: Тестирование (pytest + black)

- [README](src/lab07/README.md) — подробное описание лабораторной

- Тесты — модульные тесты для функций:
    - [test_text](tests/test_text.py) — тесты для функций из `src/lib/text.py`
    - [test_json_csv](tests/test_json_csv.py) — тесты для функций конвертации

- Конфигурация:
    - [pyproject.toml](pyproject.toml) — настройки pytest, black и покрытия кода

## Лабораторная работа 8: Модели данных и сериализация

- [README](src/lab08/README.md) — подробное описание лабораторной

- Код — модели данных и сериализация:
    - [models](src/lab08/models.py) — класс `Student` с валидацией данных
    - [serialize](src/lab08/serialize.py) — функции сериализации/десериализации в JSON

- Data — примеры данных:
    - [lab08](data/lab08/) — JSON файлы со студентами

## Лабораторная работа 9: Управление группой студентов с хранением в CSV

- [README](src/lab09/README.md) — подробное описание лабораторной

- Код — класс для управления группой студентов:
    - [group](src/lab09/group.py) — класс `Group` с операциями CRUD для работы с CSV

- Data — примеры данных:
    - [lab09](data/lab09/) — CSV файл со студентами