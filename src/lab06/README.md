# Лабораторная работа 6: CLI‑утилиты с argparse

- [cli_text](/src/lab06/cli_text.py)
- [cli_convert](/src/lab06/cli_convert.py)
- [Samples](/data/lab06/samples)
- [Out](/data/lab06/out)


## Реализованные CLI‑утилиты

- Модуль `src/lab06/cli_text.py` с подкомандами:
  - `stats --input <txt> [--top 5]` — анализ частот слов в тексте;
  - `cat --input <path> [-n]` — вывод содержимого файла построчно (с нумерацией при `-n`).

- Модуль `src/lab06/cli_convert.py` с подкомандами:
  - `json2csv --in data/samples/people.json --out data/out/people.csv`  
  - `csv2json --in data/samples/people.csv --out data/out/people.json`  
  - `csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx`


## Команды запуска

### Установка зависимостей 

#### Напрямую
```bash
pip install openpyxl
```

#### Через `requirements.txt`
```bash
pip install -r requirements.txt
```
- Эта команда просканирует файл `requirements.txt` и установит все перечисленные в нем пакеты (нужной версии)
    ```txt
    openpyxl==3.1.5 
    ```

## Результаты выполнения

- **cli_text**
  - **cat**

  ![cat](/images/lab06/img01.png)
  - **stats**

  ![stats](/images/lab06/img02.png)
  - **help**

  ![help](/images/lab06/img05.png)

- **cli_convert**
  - **csv2json + json2csv + csv2xlsx**

  ![csv2json + json2csv + csv2xlsx](/images/lab06/img03.png)
  
  - **csv2json**
  
  ![csv2json](/images/lab06/img07.png)

  - **json2csv**

  ![json2csv](/images/lab06/img06.png)
  - **csv2xlsx**

  ![csv2xlsx](/images/lab06/img08.png)
  
  - **help**

  ![help](/images/lab06/img04.png)

## Особенности реализации

### CLI-модуль `cli_text.py`

#### Подкоманда `cat`
Выводит содержимое файла построчно с опциональной нумерацией строк.

**Синтаксис:**
```bash
python src/lab06/cli_text.py cat --input <путь_к_файлу> [-n]
```

**Параметры:**
- `--input` (обязательный) - путь к файлу для чтения
- `-n` (опциональный) - включить нумерацию строк

**Примеры использования:**
```bash
# Простой вывод файла
python src/lab06/cli_text.py cat --input data/lab06/samples/people.txt

# Вывод с нумерацией строк
python src/lab06/cli_text.py cat --input data/lab06/samples/people.txt -n
```

**Особенности реализации:**
- Автоматическое определение кодировки файла (UTF-8)
- Обработка ошибок чтения файла
- Корректное отображение содержимого без лишних символов

#### Подкоманда `stats`
Анализирует частоты слов в текстовом файле и выводит топ-N самых частых слов.

**Синтаксис:**
```bash
python src/lab06/cli_text.py stats --input <путь_к_файлу> [--top N]
```

**Параметры:**
- `--input` (обязательный) - путь к файлу для анализа
- `--top` (опциональный, по умолчанию 5) - количество топ-слов для вывода

**Примеры использования:**
```bash
# Анализ с топ-5 словами (по умолчанию)
python src/lab06/cli_text.py stats --input data/lab06/samples/people.txt

# Анализ с топ-10 словами
python src/lab06/cli_text.py stats --input data/lab06/samples/people.txt --top 10
```

**Особенности реализации:**
- Использует функции из библиотеки `lib.text` для нормализации и токенизации
- Автоматическая нормализация текста (приведение к нижнему регистру, удаление знаков препинания)
- Красивый табличный вывод результатов
- Обработка ошибок файлового ввода-вывода

### CLI-модуль `cli_convert.py`

#### Подкоманда `json2csv`
Конвертирует JSON-файл в CSV формат.

**Синтаксис:**
```bash
python src/lab06/cli_convert.py json2csv --in <входной_json> --out <выходной_csv>
```

**Параметры:**
- `--in` (обязательный) - путь к входному JSON файлу
- `--out` (обязательный) - путь к выходному CSV файлу

**Пример:**
```bash
python src/lab06/cli_convert.py json2csv --in data/lab06/samples/people.json --out data/lab06/out/people.csv
```

#### Подкоманда `csv2json`
Конвертирует CSV-файл в JSON формат.

**Синтаксис:**
```bash
python src/lab06/cli_convert.py csv2json --in <входной_csv> --out <выходной_json>
```

**Параметры:**
- `--in` (обязательный) - путь к входному CSV файлу
- `--out` (обязательный) - путь к выходному JSON файлу

**Пример:**
```bash
python src/lab06/cli_convert.py csv2json --in data/lab06/samples/people.csv --out data/lab06/out/people.json
```

#### Подкоманда `csv2xlsx`
Конвертирует CSV-файл в XLSX формат.

**Синтаксис:**
```bash
python src/lab06/cli_convert.py csv2xlsx --in <входной_csv> --out <выходной_xlsx>
```

**Параметры:**
- `--in` (обязательный) - путь к входному CSV файлу
- `--out` (обязательный) - путь к выходному XLSX файлу

**Пример:**
```bash
python src/lab06/cli_convert.py csv2xlsx --in data/lab06/samples/people.csv --out data/lab06/out/people.xlsx
```

**Особенности реализации:**
- Переиспользование функций конвертации из лабораторной работы 5
- Автоматическое создание выходных директорий
- Валидация входных и выходных путей
- Обработка ошибок конвертации

## Технические детали

### Архитектура CLI-модулей

1. **Использование `argparse`** - стандартная библиотека Python для парсинга аргументов командной строки
2. **Подкоманды** - реализованы через `add_subparsers()` для создания иерархической структуры команд
3. **Валидация параметров** - проверка обязательных аргументов и корректности путей
4. **Обработка ошибок** - информативные сообщения об ошибках с использованием try-except блоков

### Интеграция с существующими модулями

- **`cli_text.py`** использует функции из `lib.text` для анализа текста
- **`cli_convert.py`** переиспользует функции конвертации из лабораторной работы 5
- **Модульная архитектура** - каждый CLI-модуль независим и может использоваться отдельно


### Примеры полного цикла работы

#### Анализ текстового файла:
```bash
# 1. Просмотр содержимого файла
python src/lab06/cli_text.py cat --input data/lab06/samples/people.txt -n

# 2. Анализ частот слов
python src/lab06/cli_text.py stats --input data/lab06/samples/people.txt --top 10
```

#### Конвертация форматов данных:
```bash
# 1. CSV -> JSON
python src/lab06/cli_convert.py csv2json --in data/lab06/samples/people.csv --out data/lab06/out/people.json

# 2. JSON -> CSV
python src/lab06/cli_convert.py json2csv --in data/lab06/samples/people.json --out data/lab06/out/people.csv

# 3. CSV -> XLSX
python src/lab06/cli_convert.py csv2xlsx --in data/lab06/samples/people.csv --out data/lab06/out/people.xlsx
```

### Справка по командам

Для получения справки по любой команде используйте флаг `-h` или `--help`:

```bash
# Общая справка по модулю
python src/lab06/cli_text.py --help
python src/lab06/cli_convert.py --help

# Справка по конкретной подкоманде
python src/lab06/cli_text.py cat --help
python src/lab06/cli_text.py stats --help
python src/lab06/cli_convert.py json2csv --help
```