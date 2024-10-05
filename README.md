# 📚 Big Data Processing Script - Читаем Миллионы Строк

![Logo](pic.jpg)

## Введение

Этот скрипт предназначен для обработки больших текстовых файлов, содержащих миллиарды строк. Он позволяет считывать данные из файла чанками и записывать их обратно в другой файл с визуализацией процесса. Скрипт включает в себя несколько методов для подсчета строк в файле, что позволяет пользователю выбирать наиболее подходящий способ в зависимости от ситуации.

## Основные функции

- **Чтение файлов чанками**: Скрипт считывает данные из исходного файла небольшими частями, что позволяет эффективно обрабатывать даже очень большие файлы без необходимости загружать их целиком в память.

- **Буферизация данных**: Данные, считанные из файла, временно хранятся в буфере. Когда буфер достигает заданного размера, данные записываются в выходной файл. Это помогает оптимизировать записи и уменьшить количество операций ввода-вывода.

- **Оценка количества строк**: Скрипт предлагает два метода подсчета строк в файле:
  - **Точный подсчет**: Считывает файл полностью и считает строки (может занять много времени для больших файлов).
  - **Оценочный подсчет**: Оценивает количество строк на основе размера файла и средней длины строки, что значительно быстрее.

- **Визуализация процесса**: Во время работы скрипта выводится информация о текущем статусе, что позволяет пользователю видеть, какие строки читаются и сколько данных уже записано.

## Примеры использования

Этот скрипт может быть полезен в следующих случаях:

- Обработка логов: Используйте его для анализа больших файлов журналов, где строки имеют фиксированный формат и длину.

- Конвертация данных: Скрипт может быть использован для преобразования данных в другом формате или с изменением регистра символов.

- Удаление дубликатов: Модифицируйте скрипт для фильтрации повторяющихся строк в больших текстовых файлах.

- Подготовка данных: Используйте его для предварительной обработки больших наборов данных перед их анализом или визуализацией.

## Установка

Для работы скрипта не требуется установка дополнительных библиотек, однако рекомендуется использовать Python 3.6 и выше.

1. Скачайте или клонируйте этот репозиторий.
2. Убедитесь, что файл `big_data_input.txt` (или другой файл, который вы хотите обработать) находится в той же директории, что и скрипт.
3. Настройте параметры в конфигурации скрипта, если это необходимо.
4. Запустите скрипт, используя команду:

   ```bash
   python big_data.py

# 📚 Big Data Processing Script

## Introduction

This script is designed for processing large text files containing billions of lines. It allows reading data from a file in chunks and writing it back to another file with process visualization. The script includes several methods for counting lines in a file, enabling the user to choose the most suitable method depending on the situation.

## Key Features

- **Chunk File Reading**: The script reads data from the source file in small parts, allowing efficient processing of even very large files without the need to load them entirely into memory.

- **Data Buffering**: The data read from the file is temporarily stored in a buffer. When the buffer reaches a specified size, the data is written to the output file. This helps optimize writes and reduce the number of input/output operations.

- **Line Count Estimation**: The script offers two methods for counting lines in a file:
  - **Exact Count**: Reads the entire file and counts the lines (may take a long time for large files).
  - **Estimated Count**: Estimates the number of lines based on the file size and average line length, which is significantly faster.

- **Process Visualization**: During the execution of the script, information about the current status is displayed, allowing the user to see which lines are being read and how much data has already been written.

## Examples of Use

This script can be useful in the following scenarios:

- **Log Processing**: Use it to analyze large log files where lines have a fixed format and length.

- **Data Conversion**: The script can be used to convert data to another format or change the case of characters.

- **Duplicate Removal**: Modify the script to filter out duplicate lines in large text files.

- **Data Preparation**: Use it for preprocessing large datasets before analysis or visualization.

## Installation

No additional libraries are required to run the script, but it is recommended to use Python 3.6 or higher.

1. Download or clone this repository.
2. Ensure that the file `big_data_input.txt` (or another file you wish to process) is in the same directory as the script.
3. Configure the parameters in the script settings if necessary.
4. Run the script using the following command:

   ```bash
   python big_data.py

